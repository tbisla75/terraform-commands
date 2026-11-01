#!/usr/bin/env python3
"""Generate offline, self-contained per-command explanations from repository runbooks.
Only standard Python libraries. Never executes commands and never contacts external services.
Run: python3 tools/build_offline_reference.py
"""
from __future__ import annotations
import pathlib, re, shlex, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "offline-reference"
SOURCE_EXT = {".md", ".sh", ".tf", ".yaml", ".yml"}
SKIP_PARTS = {".git", ".github", "tools", "offline-reference", "vendor-watch", ".terraform", ".venv"}
CMD_LANG = {"bash", "sh", "shell", "console", "powershell"}
CONFIG_LANG = {"yaml", "yml", "hcl", "terraform", "dockerfile"}
FENCE = re.compile(r"^\s*```([^\s`]*)\s*$")
PLACEHOLDER = re.compile(r"(YOUR[_-][A-Z0-9_-]+|REPLACE[_-][A-Z0-9_-]+|\$\{?[A-Z][A-Z0-9_]*\}?|<[^>]+>|(?:VMID|JOB_ID|NODE_NAME|VPC_ID|SG_ID|YOUR_HOST|YOUR_POD))")
SHELL_CONTROL = re.compile(r"^(?:if\b|then\b|else\b|elif\b|fi\b|for\b|while\b|do\b|done\b|case\b|esac\b|\{|\}|function\b|#|\[\[|\]\]|set -[A-Za-z]+|usage\(\)|local\b)")
WRITE_WORDS = ("apply", "install", "restart", "reset", "destroy", "delete", "create", "join", "drain", "cordon", "uncordon", "passwd", "reboot", "update", "upgrade", "edit", "patch", "kill", "stop", "enable", "disable", "snapshot save", "snapshot restore", "sbatch", "condor_submit")
HIGH_WORDS = ("kubeadm reset", "cluster-reset", "etcdutl snapshot restore", "terraform destroy", "rm -rf", "esxcli storage san fc reset", "systemctl stop network", "vmkfstools -U")
COMMON = {
 "kubectl":("Kubernetes API", "Query or modify declarative resources using the current kubeconfig/context. Output depends on subcommand and output format.", "https://kubernetes.io/docs/reference/kubectl/"),
 "oc":("OpenShift CLI", "Inspect or change OpenShift/Kubernetes resources using the selected project and credentials.", "https://docs.redhat.com/en/documentation/openshift_container_platform/"),
 "kubeadm":("kubeadm cluster lifecycle", "Initialize, join, inspect or upgrade a self-managed Kubernetes control plane; cluster-wide effects are possible.", "https://kubernetes.io/docs/reference/setup-tools/kubeadm/"),
 "k3s":("K3s cluster service", "Operate the K3s distribution, its datastore/snapshots and embedded components.", "https://docs.k3s.io/"),
 "terraform":("Terraform infrastructure as code", "Inspect, plan or reconcile declaratively managed infrastructure. State may be sensitive.", "https://developer.hashicorp.com/terraform/cli/commands"),
 "esxcli":("VMware ESXi management", "Query or change the ESXi host subsystem named by the namespace.", "https://developer.broadcom.com/xapis/esxcli-command-reference/latest/"),
 "vim-cmd":("ESXi vim-cmd", "Read or modify ESXi host inventory and VM management state.", "https://knowledge.broadcom.com/"),
 "vmkping":("ESXi VMkernel network test", "Send ICMP from a specified VMkernel stack/interface; no permanent configuration changes.", "https://knowledge.broadcom.com/"),
 "service-control":("vCenter service manager", "Inspect or control vCenter appliance services; service changes can interrupt management.", "https://knowledge.broadcom.com/"),
 "pcs":("Pacemaker HA manager", "Inspect or alter cluster membership, quorum, fencing and resource placement.", "https://clusterlabs.org/"),
 "journalctl":("systemd journal inspection", "Query system and service journal messages with boot, unit, time and priority filters.", "https://www.freedesktop.org/software/systemd/man/latest/journalctl.html"),
 "systemctl":("systemd unit manager", "Inspect or modify systemd-managed services and units.", "https://www.freedesktop.org/software/systemd/man/latest/systemctl.html"),
 "sinfo":("Slurm partition/node information", "Display scheduler partition and compute node status.", "https://slurm.schedmd.com/sinfo.html"),
 "squeue":("Slurm queue status", "Show queued/running jobs and placement reasons.", "https://slurm.schedmd.com/squeue.html"),
 "scontrol":("Slurm control inspection", "Inspect or administer scheduler nodes, partitions and jobs; read/write depends on subcommand.", "https://slurm.schedmd.com/scontrol.html"),
 "sacct":("Slurm accounting inspection", "List historical job resources, states and timing.", "https://slurm.schedmd.com/sacct.html"),
 "sbatch":("Slurm job submission", "Submit a batch job, consuming compute allocation subject to scheduler policy.", "https://slurm.schedmd.com/sbatch.html"),
 "srun":("Slurm parallel task launch", "Start tasks in an authorized scheduler allocation.", "https://slurm.schedmd.com/srun.html"),
 "condor_q":("HTCondor job queue", "Inspect current queued, running or held jobs.", "https://htcondor.readthedocs.io/"),
 "condor_submit":("HTCondor job submission", "Queue workload through HTCondor; consumes scheduled resources.", "https://htcondor.readthedocs.io/"),
 "condor_status":("HTCondor worker status", "Display resource pool advertisements and availability.", "https://htcondor.readthedocs.io/"),
 "df":("Filesystem capacity", "Display filesystem usage; bytes with -h or inodes with -i.", "https://man7.org/linux/man-pages/man1/df.1.html"),
 "ip":("Linux network configuration", "Read or change Linux addresses, links, routes and neighbor information.", "https://man7.org/linux/man-pages/man8/ip.8.html"),
 "ss":("Socket inspection", "Show listening and active network sockets, protocols and owning processes when permitted.", "https://man7.org/linux/man-pages/man8/ss.8.html"),
 "openssl":("OpenSSL TLS diagnostics", "Inspect TLS handshakes/certificates; network requests reveal target connections.", "https://docs.openssl.org/"),
 "apt-get":("Debian/Ubuntu package manager", "Update package indexes or install/upgrade/remove packages depending on subcommand.", "https://manpages.debian.org/"),
 "dnf":("RHEL-family package manager", "Install/update/query packages using configured RPM repositories.", "https://dnf.readthedocs.io/"),
 "curl":("HTTP request/diagnostic", "Request or transfer network content, with protocol and TLS behavior governed by flags.", "https://curl.se/docs/manpage.html"),
 "git":("Git version control", "Read or modify Git's working tree/index/references according to the subcommand.", "https://git-scm.com/docs"),
 "aws":("AWS CLI", "Query or alter AWS resources for the selected account, region and IAM principal.", "https://docs.aws.amazon.com/cli/"),
 "az":("Azure CLI", "Query or modify Azure resources for the selected subscription/identity.", "https://learn.microsoft.com/en-us/cli/azure/"),
 "gcloud":("Google Cloud CLI", "Query or modify Google Cloud resources for the selected project/identity.", "https://cloud.google.com/sdk/gcloud/reference"),
 "nvidia-smi":("NVIDIA GPU diagnostics", "Inspect GPU inventory, utilization, memory, temperatures and errors.", "https://docs.nvidia.com/deploy/nvidia-smi/"),
 "ibstat":("InfiniBand link inspection", "Display InfiniBand adapter, port state, link speed and identifiers.", "https://github.com/linux-rdma/rdma-core"),
 "vmware":("VMware ESXi version", "Print the ESXi build/release for comparison with patch/advisory matrices.", "https://knowledge.broadcom.com/"),
 "helm":("Helm Kubernetes package manager", "Inspect/render or modify Helm releases depending on subcommand.", "https://helm.sh/docs/helm/"),
 "velero":("Velero backup utility", "Inspect or control Kubernetes backup schedules, storage locations and restores.", "https://velero.io/docs/"),
 "crictl":("CRI runtime diagnostics", "Inspect pods, containers and the configured container runtime.", "https://github.com/kubernetes-sigs/cri-tools"),
 "getent":("NSS lookup", "Resolve users, groups and hosts through the operating system's NSS configuration.", "https://man7.org/linux/man-pages/man1/getent.1.html"),
 "ping":("ICMP reachability", "Test network reachability; failure does not prove firewall/routing root cause.", "https://man7.org/linux/man-pages/man8/ping.8.html"),
}
FLAGS = {
 "--context":"Select the named Kubernetes context rather than the default.",
 "--kubeconfig":"Use the specified kubeconfig file for authentication and cluster selection.",
 "--namespace":"Select a namespace/project.",
 "--all-namespaces":"Query across namespaces (subject to RBAC).",
 "--show-labels":"Include resource labels in output.",
 "--dry-run":"Preview or server-validate without applying persistent object changes; exact behavior depends on mode.",
 "--no-pager":"Print output directly rather than opening an interactive pager.",
 "--tail":"Limit returned log lines.",
 "--since":"Select entries newer than a given time or duration.",
 "--field-selector":"Filter resources by server-supported field expressions.",
 "--selector":"Filter objects using label expressions.",
 "--sort-by":"Sort returned results using the specified resource field.",
 "--output":"Choose output representation such as wide/yaml/json/jsonpath.",
 "--all-containers":"Include logs for all containers in a pod where supported.",
 "--previous":"Read logs from previous terminated container instance.",
 "--timestamps":"Include timestamps in log output.",
 "--timeout":"Set a maximum time to wait, often for a rollout or connection.",
 "--watch":"Follow resource changes continuously.",
 "--as":"Impersonate a user for authorization checks; requires impersonation privileges.",
 "--server":"Specify the API endpoint or bootstrap server.",
 "--token":"Authentication credential; avoid shell history/process leaks.",
 "--user":"Select or specify user identity; semantics depend on tool.",
 "--role":"Choose node/server role or target role in script.",
 "--apply":"A script flag generally means perform changes; inspect script before using.",
 "--dry-run=server":"Perform admission and server-side validation without committing resource change.",
 "--help":"Display supported syntax and options for this installed tool version.",
 "--version":"Display tool version.",
 "--recursive":"Traverse nested directories.",
 "--lock-timeout":"Wait for state lock for the specified duration.",
 "--refresh-only":"Show/apply observed drift without proposing standard config changes (mode matters).",
 "--ignore-daemonsets":"Allow node drain to ignore DaemonSet pods (it does not evict them).",
 "--upload-certs":"Temporarily upload shared control-plane certificates for kubeadm joins; handle key securely.",
 "--force":"Force an operation, potentially bypassing safeguards; review precise command semantics.",
 "--time":"Specify time limit for a scheduled workload.",
 "--nodes":"Specify allocated Slurm nodes for a job.",
 "--ntasks":"Specify number of scheduler tasks.",
 "--cpus-per-task":"Specify CPUs allocated per scheduled task.",
 "-A":"All namespaces for kubectl/oc; other tools may assign a different meaning.",
 "-n":"Namespace for kubectl/oc, number of lines for journalctl/tail, or another command-specific argument.",
 "-o":"Output format for kubectl/oc, filename for some tools; command-specific.",
 "-p":"Priority filter in journalctl; other meanings in other CLIs.",
 "-u":"Filter journal by systemd unit; in other tools may mean user.",
 "-b":"Filter journal to specified boot; otherwise command-specific.",
 "-d":"Disk/device or directory flag depending on command.",
 "-h":"Human-readable units for storage tools; help in other commands.",
 "-i":"Inode usage in df, interactive or interface depending on command.",
 "-r":"Reverse order or recursive depending on command.",
 "-f":"Follow logs/force/filename depending on command.",
 "-y":"Automatically accept package manager prompts; risky on production.",
 "-v":"Verbose output or version depending on command.",
 "-t":"Type/timeout/terminal mode depending on command.",
}
SUBVERBS = {
 "kubectl get":"List selected Kubernetes resources and their current status.",
 "kubectl describe":"Show resource details and related warning/event evidence.",
 "kubectl logs":"Retrieve stdout/stderr logs from Kubernetes containers.",
 "kubectl exec":"Run a command inside a container; shell/action behavior depends on trailing command.",
 "kubectl apply":"Reconcile a Kubernetes resource manifest (mutating unless dry-run).",
 "kubectl drain":"Evict eligible workloads from a node for maintenance (mutating).",
 "kubectl rollout":"Inspect or change workload rollout depending on subcommand.",
 "oc get":"List OpenShift/Kubernetes resources.",
 "oc adm upgrade":"Inspect offered updates or initiate OpenShift cluster update, depending on flags.",
 "oc login":"Authenticate against OpenShift API; credentials may be stored locally.",
 "oc describe":"Read detailed object information and events.",
 "oc logs":"Read container logs from OpenShift workloads.",
 "terraform init":"Download/setup providers/modules and initialize backend; changes local working files.",
 "terraform plan":"Compute proposed infrastructure change plan (typically does not mutate managed infrastructure).",
 "terraform apply":"Apply proposed changes to real infrastructure and Terraform state.",
 "terraform state":"Read or manipulate Terraform state; some subcommands are dangerous.",
 "terraform validate":"Check Terraform configuration syntax and type/schema consistency.",
 "terraform fmt":"Format Terraform config files (unless check-only mode).",
 "journalctl -u":"Filter systemd logs for the specified unit.",
 "systemctl status":"Inspect service state, recent logs and metadata.",
 "systemctl restart":"Restart a unit, potentially interrupting production traffic.",
 "esxcli storage":"Inspect or configure storage subsystems (device, paths, adapters and filesystems).",
 "esxcli network":"Inspect or configure ESXi network interfaces, stacks and switches.",
 "esxcli system":"Inspect or configure ESXi host/system state.",
}

def md(s: str) -> str:
    return s.replace("|", "\\|").replace("`", "\\`").replace("\r", " ")

def command_kind(command: str):
    low = command.lower()
    if any(k in low for k in HIGH_WORDS):
        return "**HIGH-RISK CHANGE**", "May cause data loss, service downtime or cluster disruption; require approved vendor runbook and rollback."
    if re.search(r"\b(" + "|".join(re.escape(x) for x in WRITE_WORDS) + r")\b", low):
        return "**CHANGE / POSSIBLY MUTATING**", "Check subcommand and flags; requires change review and appropriate access."
    if ">" in command and not "2>" in command:
        return "**LOCAL FILE WRITE / POSSIBLY MUTATING**", "Shell redirection may create/truncate files; verify output destination."
    return "**DIAGNOSTIC / REVIEW**", "Typically query-oriented; may still cause network traffic, load or output sensitive information."

def explain(command: str):
    try:
        toks = shlex.split(command, comments=False, posix=True)
    except ValueError:
        toks = command.split()
    if not toks: return None
    command0 = toks[0]
    if command0 in ("sudo", "env") and len(toks) > 1:
        command0 = next((t for t in toks[1:] if "=" not in t and not t.startswith("-")), toks[1])
    base = COMMON.get(command0, (command0 + " operation", "Command semantics depend on installed implementation; inspect its man page and --help.", "https://man7.org/linux/man-pages/"))
    meaning = next((v for k,v in SUBVERBS.items() if command.startswith(k) or command.startswith("sudo "+k)), base[1])
    flags = []
    for t in toks:
        if t.startswith("-"):
            key=t.split("=",1)[0]
            flags.append(f"`{md(t)}` — {FLAGS.get(key, 'Command-specific option or abbreviated argument; verify with installed CLI help and vendor reference.')}")
    vars_ = list(dict.fromkeys(PLACEHOLDER.findall(command)))
    sensitive = " **Credential caution:** command may reference credentials or identity; do not upload raw outputs." if any(w in command.lower() for w in ("secret", "token", "kubeconfig", "password", "passwd", "key", "auth")) else ""
    risk, risktext = command_kind(command)
    shell=[]
    if "|" in command: shell.append("`|` pipes stdout into the next process; check pipeline exit codes (pipefail where appropriate).")
    if ">>" in command: shell.append("`>>` appends to a local file.")
    elif re.search(r"(?<![<>=])>(?![>=])", command): shell.append("`>` redirects/truncates output; confirm destination and permissions.")
    if "&&" in command: shell.append("`&&` runs next action only if preceding command succeeds.")
    if "$(" in command: shell.append("`$(...)` executes a subshell for value substitution.")
    return dict(tool=base[0],meaning=meaning,flags=flags,vars=vars_,risk=risk,risktext=risktext,shell=shell,ref=base[2],sensitive=sensitive,syntax=" ".join(toks[:min(5,len(toks))]))

def extract_fenced(text):
    entries=[]
    lines=text.splitlines()
    active=None; start=0; accum=[]
    for no,ln in enumerate(lines,1):
        m=FENCE.match(ln)
        if m:
            if active is None:
                active=m.group(1).lower();start=no+1;accum=[]
            else:
                if active in CMD_LANG:
                    entries += extract_shell(accum,start,active)
                elif active in CONFIG_LANG:
                    entries += extract_config(accum,start,active)
                active=None;accum=[]
            continue
        if active is not None: accum.append(ln)
    return entries

def extract_shell(lines,start,language):
    result=[]; buffer=""; buffer_line=start; heredoc=None
    for i,line in enumerate(lines):
        s=line.strip(); ln=start+i
        if heredoc:
            if s == heredoc: heredoc=None
            continue
        if not s or s.startswith("#") or s in ("EOF","HELP","USAGE"): continue
        m=re.search(r"<<-?\s*['\"]?([A-Za-z][A-Za-z0-9_]*)['\"]?",s)
        if m:
            heredoc=m.group(1)
            if s.startswith("cat ") or " cat " in s: continue
        if SHELL_CONTROL.match(s): continue
        if s.startswith(("export ", "ROLE=", "MODE=", "MINOR=", "VERSION=", "TOKEN_FILE=", "TLS_SAN=", "API=")): # still include export as useful
            if not s.startswith("export "):continue
        if s.endswith("\\"):
            if not buffer:buffer_line=ln
            buffer += s[:-1].strip() + " "
            continue
        command=(buffer+s).strip()
        loc=buffer_line if buffer else ln
        buffer=""
        if not command or len(command)>600:continue
        result.append(("command",loc,language,command))
    return result

def extract_config(lines,start,language):
    # Document the configuration object at block level; no arbitrary command execution.
    content="\n".join(lines)
    if not content.strip():return []
    return [("config",start,language,content[:5000])]

def extract_script(text):
    return extract_shell(text.splitlines(),1,"bash")

def extract_hcl(text):
    blocks=[]
    for i,line in enumerate(text.splitlines(),1):
        m=re.match(r'^\s*(resource|data|provider|module|variable|output)\s+"([^"]+)"(?:\s+"([^"]+)")?',line)
        if m:blocks.append(("hcl",i,"hcl", " ".join(x for x in m.groups() if x)))
    return blocks

def enumerate_sources():
    files=[]
    for f in ROOT.rglob("*"):
        if not f.is_file() or f.suffix not in SOURCE_EXT:continue
        if any(p in SKIP_PARTS for p in f.relative_to(ROOT).parts):continue
        if f.name == "README.md": continue
        files.append(f)
    return sorted(files)

def render_record(typ,line,lang,text,n):
    if typ == "command":
        ex=explain(text)
        h=[f"### {n}. `{md(text[:115])}{'…' if len(text)>115 else ''}`", "",
           f"**Source line:** {line}  |  **Tool/purpose:** {ex['tool']}  |  **Impact:** {ex['risk']}", "",
           f"**Exact command:**", "",f"```{lang if lang in ('bash','powershell') else 'bash'}",text,"```","",
           f"**What it does:** {ex['meaning']}", "",
           f"**Syntax:** {ex['syntax']}. The first executable selects the CLI; subcommands select the resource/action; options control target, scope or output."]
        h += [f"**Option:** {flag}" for flag in ex["flags"]]
        if ex["vars"]:h.append("**Substitute before running:** "+", ".join("`"+md(v)+"`" for v in ex["vars"])+". Never assume an example target is the current cluster.")
        if ex["shell"]:h.append("**Shell syntax:** "+" ".join(ex["shell"]))
        h.extend([f"**Safety/rollback:** {ex['risktext']}{ex['sensitive']}",f"**Expected result:** {ex['meaning']} Check command exit status and compare to healthy baseline; exact columns and messages vary by installed version.",f"**Offline verification:** On target host use `{ex['tool']}` vendor manual or installed `--help`; [online vendor reference]({ex['ref']}).",""])
        return "\n".join(h)
    if typ == "hcl":
        kind, *args=text.split()
        return f"### {n}. Terraform {kind}: `{md(' '.join(args))}`\n\n**Source line:** {line}. **Purpose:** Declare a {kind} object. Terraform validates provider schema, references, lifecycle and policy during `terraform validate`/`plan`; runtime behavior depends on provider version. **Safety:** No changes occur until an approved apply, except some data sources may query external APIs during planning. Consult the configured provider docs and validate all arguments offline from provider schema.\n"
    return f"### {n}. Configuration example ({lang})\n\n**Source line:** {line}. **Purpose:** Define declarative settings rather than a standalone command. Review image references, identity, network addresses, permissions, secrets, version-specific fields and application/recovery impact.\n\n```{lang}\n{text}\n```\n\n**Key syntax:** YAML/HCL fields map to release-specific APIs. Validate with the installed schema and run a dry-run or plan. **Safety:** Applying this snippet can change live infrastructure; no rollback is implied.\n"

def write():
    OUT.mkdir(exist_ok=True)
    source_index=[]
    total=0
    for src in enumerate_sources():
        rel=src.relative_to(ROOT)
        try: raw=src.read_text(encoding="utf-8")
        except UnicodeDecodeError:continue
        if src.suffix==".md": rec=extract_fenced(raw)
        elif src.suffix==".sh":rec=extract_script(raw)
        elif src.suffix==".tf":rec=extract_hcl(raw)
        else:rec=extract_config(raw.splitlines(),1,src.suffix[1:])
        if not rec:continue
        # Limit config sections that would accidentally contain secrets in local checkout.
        target=OUT/("-".join(rel.parts).replace(".","_")+".md")
        lines=[f"# Offline command / configuration reference: `{rel.as_posix()}`","",
               f"Generated from repository source by `tools/build_offline_reference.py`. **{len(rec)} items**. This copy works offline. No commands were executed.","",
               "⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.", "",
               f"**Original file:** [`{rel.as_posix()}`](../{rel.as_posix()})",""]
        for i,(typ,line,lang,value) in enumerate(rec,1):
            lines.append(render_record(typ,line,lang,value,i))
        target.write_text("\n".join(lines)+"\n",encoding="utf-8")
        source_index.append((rel.as_posix(),target.name,len(rec)))
        total+=len(rec)
    index=["# Offline-first command reference — full local catalog","",
           "This directory is committed to Git and can be cloned, downloaded or printed for **offline** incident response. It is generated from the actual command examples and declarative templates in this repository; it does not rely on ChatGPT being available.","",
           "**Important:** An offline explanation is a helpful annotated starting point, not a guaranteed validated syntax for every release. Dynamic command flags should be verified using your installed CLI help/man pages and supported vendor procedures. Destructive changes require peer review.","",
           f"**Indexed items:** {total} across {len(source_index)} source files.","",
           "| Source | Offline explanations | Items |","|---|---|---:|"]
    for rel,name,n in source_index:index.append(f"| `{rel}` | [Open offline reference]({name}) | {n} |")
    index+=["","## How to update locally","",
            "```bash","python3 tools/build_offline_reference.py","git diff -- offline-reference/","```","",
            "This generator does **not** infer new vendor commands, does **not** run shell commands, and does **not** grant access to systems. A scheduled vendor-watch workflow separately proposes release changes for review."]
    (OUT/"README.md").write_text("\n".join(index)+"\n",encoding="utf-8")
    print(f"Generated {len(source_index)} files / {total} annotated examples")

if __name__=="__main__":
    write()
