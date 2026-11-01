# Vendor changes — monitored and reviewable

This directory maintains the vendor release and security-documentation fingerprints. A **weekly GitHub Actions job** checks the configured official upstream sources and regenerates local command explanations. When anything changes, it opens a **review-only pull request**, listing sources and before/after versions in `CHANGES.md` and tracking version fingerprints in `STATUS.md`/`last-seen.json`.

**No production commands are blindly rewritten.** A changed upstream page is a prompt for a maintainer to investigate; command/flag changes must be individually verified against release notes and the installed product before updating Markdown runbooks. The offline catalog is regenerated from the accepted runbooks. Broadcom portal bot restrictions may cause an explicit unverified status.

**Manual use:** `python3 tools/build_offline_reference.py` and `python3 tools/vendor_watch.py`.

**GitHub requirement:** Repository Settings → Actions → General → Workflow permissions: allow write and, if needed, **Allow GitHub Actions to create and approve pull requests**. Otherwise the scheduled job can run but cannot open review PRs. Scheduled GitHub Actions may be delayed or disabled after repository inactivity.

**Security:** Vendor source checks use only configured trusted HTTPS URLs. No access to customer clusters, no secrets, no command execution, and no self-merging production changes.
