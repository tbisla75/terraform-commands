#!/usr/bin/env python3
"""Track authoritative vendor releases and published reference pages.
No vendor commands are executed and no production runbook is rewritten automatically.
Updates vendor-watch/{STATUS,CHANGES,last-seen}. GitHub Actions opens an approval PR.
"""
from __future__ import annotations
import datetime, hashlib, json, os, pathlib, urllib.request, urllib.error
ROOT = pathlib.Path(__file__).resolve().parents[1]
DIR = ROOT / "vendor-watch"
CONFIG = DIR / "sources.json"
STATE = DIR / "last-seen.json"
USER_AGENT = "offline-commands-vendor-watch/1.0 (GitHub Actions; release-monitor)"

def read_json(path, default):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError): return default

def download(url, accept="application/json"):
    headers={"User-Agent":USER_AGENT,"Accept":accept}
    tok=os.environ.get("GITHUB_TOKEN","")
    if tok and url.startswith("https://api.github.com/"):
        headers["Authorization"]="Bearer "+tok
        headers["X-GitHub-Api-Version"]="2022-11-28"
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=18) as response:
        data=response.read(450000)
    return data

def check_source(source):
    kind=source["kind"]; url=source["url"]; ident=source["id"]
    if kind=="github_release":
        obj=json.loads(download(url).decode("utf-8"))
        version=obj.get("tag_name")
        if not version:raise RuntimeError("GitHub release missing tag_name")
        return {"id":ident,"version":version,"url":obj.get("html_url",url),"published_at":obj.get("published_at",""),"source":url,"status":"OK"}
    if kind=="text_marker":
        # Vendor pages can be dynamic/block automated traffic; do not treat failed checks as no changes.
        body=download(url,accept="text/html,text/plain,application/xml").decode("utf-8","replace")
        if len(body)<250:raise RuntimeError("Page unexpectedly short; bot challenge or inaccessible page?")
        # Hash response after stripping volatile whitespace. A change is a REVIEW SIGNAL, not proof of a command change.
        normalized=" ".join(body.split())
        return {"id":ident,"version":"sha256:"+hashlib.sha256(normalized.encode()).hexdigest()[:20],"url":url,"published_at":"","source":url,"status":"OK"}
    raise RuntimeError("Unsupported source kind: "+kind)

def main():
    DIR.mkdir(exist_ok=True)
    config=read_json(CONFIG,{"sources":[]})
    previous=read_json(STATE,{})
    observed=dict(previous)
    changes=[]; errors=[]
    for item in config.get("sources",[]):
        try:
            cur=check_source(item)
            old=previous.get(item["id"])
            observed[item["id"]]=cur
            if old is None:
                changes.append((item,cur,None,"First baseline: review before accepting"))
            elif old.get("version")!=cur["version"]:
                changes.append((item,cur,old,"Vendor release/reference changed; manual command review REQUIRED"))
        except (urllib.error.URLError,urllib.error.HTTPError,TimeoutError,ValueError,RuntimeError,KeyError) as e:
            errors.append((item,str(e)[:220]))
    # Only change tracked files when there are new observations/changes; avoid a PR every week just for time.
    if changes:
        STATE.write_text(json.dumps(observed,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    status=["# Vendor update checks — review dashboard","",
            "This is a **vendor-release change detector**, not an automatic compatibility guarantee. A release tag or docs page change does **not** prove that any command has changed. Never merge generated command modifications without human review.","",
            "| Source | Latest observed | Official link |","|---|---|---|"]
    for item in config.get("sources",[]):
        cur=observed.get(item["id"],{})
        ver=cur.get("version","not yet verified")
        if ver.startswith("sha256:"):ver="page fingerprint "+ver[7:20]
        status.append(f"| {item.get('label',item['id'])} | `{ver}` | [source]({item['url']}) |")
    status += ["","## Manual validation before changing any example","",
              "1. Open the official release notes/advisory and compare the affected tool/CLI command syntax to the current runbook.",
              "2. Confirm behavior in the *installed* vendor release using `--help`, man pages, version-specific docs, a lab and the support matrix.",
              "3. Update commands, warning labels, expected output and rollback procedures; add exact vendor reference and affected version.",
              "4. Re-run `python3 tools/build_offline_reference.py` and review all offline explanation diffs.",
              "5. Run peer review/CI. Merge only approved, tested changes; never auto-apply a production command change.",
              "",
              "**Note:** VMware/Broadcom portals and some vendor sites may block automated reads. An unavailable upstream check must be treated as *unknown*, not as up-to-date."]
    new_status="\n".join(status)+"\n"
    p=DIR/"STATUS.md"
    if not p.exists() or p.read_text(encoding="utf-8")!=new_status:
        # Status changes only when versions/fingerprints change (not each run).
        p.write_text(new_status,encoding="utf-8")
    if changes or errors:
        report=["# Vendor-change candidates — human review required","",
                "No production commands are auto-replaced. Review the changed vendor release/advisory and amend the correct runbooks in this PR.",""]
        for item,cur,old,why in changes:
            report += [f"## {item.get('label',item['id'])}", "",
                       f"- Result: {why}",
                       f"- Previous observed: `{old.get('version','none') if old else 'none'}`",
                       f"- New observed: `{cur['version']}`",
                       f"- Vendor document: {cur['url']}",
                       f"- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.",
                       ""]
        for item,error in errors:
            report+= [f"## Verification unavailable: {item.get('label',item['id'])}", "",
                      f"- Error: {error}",
                      f"- Vendor URL: {item['url']}",
                      "- This source was **not verified**; retain last known observation and investigate manually.", ""]
        (DIR/"CHANGES.md").write_text("\n".join(report)+"\n",encoding="utf-8")
    print(json.dumps({"changed":len(changes),"unavailable":len(errors),"checked":len(config.get('sources',[]))}))
    # Alert on unavailable upstream, but allow healthy sources to report.
    if errors: print("WARN: some vendor sources could not be checked; see CHANGES.md")

if __name__=="__main__":
    main()
