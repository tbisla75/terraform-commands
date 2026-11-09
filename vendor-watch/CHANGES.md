# Vendor-change candidates — human review required

No production commands are auto-replaced. Review the changed vendor release/advisory and amend the correct runbooks in this PR.

## Terraform CLI releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v1.17.1`
- Vendor document: https://github.com/hashicorp/terraform/releases/tag/v1.17.1
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform AWS provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v6.72.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.72.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform AzureRM provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v5.13.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-azurerm/releases/tag/v5.13.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- `azurerm_netapp_volume` - remove the default for `unix_permissions` as this prevented provisioning SMB or dual protocol volumes with NTFS security style ([#33766](https://github.com/hashicorp/terraform-provider-azurerm/issues/33766))
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform Google provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v8.10.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-google/releases/tag/v8.10.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

