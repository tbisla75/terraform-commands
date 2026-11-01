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
- New observed: `v6.71.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.71.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- resource/aws_lakeformation_resource_lf_tag: Fix crash during refresh when an LF-Tag assignment has been removed outside Terraform ([#50626](https://github.com/hashicorp/terraform-provider-aws/issues/50626))
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform AzureRM provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v5.12.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-azurerm/releases/tag/v5.12.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

## Terraform Google provider releases

- Result: First baseline: review before accepting
- Previous observed: `none`
- New observed: `v8.9.0`
- Vendor document: https://github.com/hashicorp/terraform-provider-google/releases/tag/v8.9.0
- Upstream release-note lines mentioning CLI/security/breaking changes (unverified candidates):
- container: deprecated `addons_config.parallelstore_csi_driver_config` on `google_container_cluster`. Use `addons_config.lustre_csi_driver_config` instead ([#30328](https://github.com/hashicorp/terraform-provider-google/pull/30328))
- container: deprecated `remove_default_node_pool` on `google_container_cluster` in favor of omitting `initial_node_count` and `node_config` (or setting `initial_node_count = 0`). When this is set to `true` and the default node pool was not c
- parallelstore: deprecated `google_parallelstore_instance`. Use `google_lustre_instance` instead ([#30328](https://github.com/hashicorp/terraform-provider-google/pull/30328))
- container: updated `initial_node_count` on `google_container_cluster` so it can be removed from config or set to `null` without creating a diff while still respecting `0` when set in config ([#30375](https://github.com/hashicorp/terraform-p
- provider: fixed a bug where `google_apikeys_key`, `google_assured_workloads_workload`, `google_cloudbuild_worker_pool`, `google_clouddeploy_delivery_pipeline`, `google_clouddeploy_target`, `google_container_aws_cluster`, `google_container_a
- provider: fixed a bug where `google_apikeys_key`, `google_assured_workloads_workload`, `google_cloudbuild_worker_pool`, `google_clouddeploy_delivery_pipeline`, `google_clouddeploy_target`, `google_container_aws_cluster`, `google_container_a
- provider: fixed a bug where `google_compute_firewall_policy_association`, `google_compute_firewall_policy_rule`, `google_compute_organization_security_policy_association`, `google_compute_organization_security_policy_rule`, `google_endpoint
- provider: removed an extra sleep on IAM writes while several concurrent changes are happening, backoff and terminate for a longer window (90s + grace period) ([#30057](https://github.com/hashicorp/terraform-provider-google/pull/30057))
- Action: inspect breaking changes, deprecations, flags, authentication, support matrix, examples; amend runbooks and re-generate offline catalog; obtain review.

