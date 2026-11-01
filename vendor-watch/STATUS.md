# Vendor update checks — review dashboard

This is a **vendor-release change detector**, not an automatic compatibility guarantee. A release tag or docs page change does **not** prove that any command has changed. Never merge generated command modifications without human review.

| Source | Latest observed | Official link |
|---|---|---|
| Terraform CLI releases | `v1.17.1` | [source](https://api.github.com/repos/hashicorp/terraform/releases/latest) |
| Terraform AWS provider releases | `v6.71.0` | [source](https://api.github.com/repos/hashicorp/terraform-provider-aws/releases/latest) |
| Terraform AzureRM provider releases | `v5.12.0` | [source](https://api.github.com/repos/hashicorp/terraform-provider-azurerm/releases/latest) |
| Terraform Google provider releases | `v8.9.0` | [source](https://api.github.com/repos/hashicorp/terraform-provider-google/releases/latest) |

## Manual validation before changing any example

1. Open the official release notes/advisory and compare the affected tool/CLI command syntax to the current runbook.
2. Confirm behavior in the *installed* vendor release using `--help`, man pages, version-specific docs, a lab and the support matrix.
3. Update commands, warning labels, expected output and rollback procedures; add exact vendor reference and affected version.
4. Re-run `python3 tools/build_offline_reference.py` and review all offline explanation diffs.
5. Run peer review/CI. Merge only approved, tested changes; never auto-apply a production command change.

**Note:** VMware/Broadcom portals and some vendor sites may block automated reads. An unavailable upstream check must be treated as *unknown*, not as up-to-date.
