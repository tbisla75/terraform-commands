# Vendor-change candidates — human review required

No production commands are auto-replaced. Review the changed vendor release/advisory and amend the correct runbooks in this PR.

## Terraform CLI releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v1.17.2`
- Vendor document: https://github.com/hashicorp/terraform/releases/tag/v1.17.2
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform AWS provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v6.73.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.73.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- BREAKING CHANGES:
- resource/aws_networksecuritymanager_rule: Fix the first apply of more than one rule in an account that has never used AWS Network Security Manager failing with `ConflictException: Account or org is already onboarded` ([#50807](https://githu
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform AzureRM provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v5.14.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-azurerm/releases/tag/v5.14.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- `azurerm_kubernetes_cluster_node_pool` - add support for the `security` block ([#33837](https://github.com/hashicorp/terraform-provider-azurerm/issues/33837))
- `azurerm_kubernetes_cluster` - add support for the `default_node_pool.security` block ([#33837](https://github.com/hashicorp/terraform-provider-azurerm/issues/33837))
- `azurerm_role_assignment` - use deterministic generation for the `name` property to align with ARM, Bicep, and Azure CLI ([#32446](https://github.com/hashicorp/terraform-provider-azurerm/issues/32446))
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform Google provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v8.11.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-google/releases/tag/v8.11.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- vertexai: deprecated `optimized` on `google_vertex_ai_feature_online_store`. Use `bigtable` for online serving instead. ([#13700](https://github.com/hashicorp/terraform-provider-google-beta/pull/13700))
- saasruntime: fixed `google_saas_runtime_release` deletion returning before the resource was removed (beta) ([#13729](https://github.com/hashicorp/terraform-provider-google-beta/pull/13729))
- saasruntime: fixed `google_saas_runtime_rollout_kind` deletion returning before the resource was removed (beta) ([#13729](https://github.com/hashicorp/terraform-provider-google-beta/pull/13729))
- saasruntime: fixed `google_saas_runtime_unit_kind` deletion returning before the resource was removed (beta) ([#13729](https://github.com/hashicorp/terraform-provider-google-beta/pull/13729))
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

