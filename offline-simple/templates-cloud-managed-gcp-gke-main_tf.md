# Terraform / cluster template explained simply: templates/cloud-managed/gcp-gke/main.tf

This document explains **each significant configuration key** without needing ChatGPT. Templates are starters: do not treat placeholders as a runnable production cluster. Exact field support depends on Terraform provider version or OpenShift/kubeadm version. Original: [templates/cloud-managed/gcp-gke/main.tf](../templates/cloud-managed/gcp-gke/main.tf).

## 1. `required_version` = `">= 1.8.0"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `required_version` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 2. `google` = `{ source = "hashicorp/google", version = ">= 5.0, < 8.0" }`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `google` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 3. provider google 

**What this means:** Configures which vendor/cloud API Terraform connects to. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 4. `project` = `var.project_id`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `project` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 5. `region` = `var.region`

**What it means:** Selected cloud region.

**Syntax:** `region` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 6. variable project_id 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 7. variable region 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 8. variable cluster_name 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 9. variable network 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 10. variable subnetwork 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 11. variable pods_secondary_range_name 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 12. variable services_secondary_range_name 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 13. variable release_channel 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 14. `type` = `string`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `type` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 15. `default` = `"REGULAR"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `default` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 16. variable authorized_admin_cidrs 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 17. variable node_service_account 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 18. resource google_container_cluster this

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 19. `name` = `var.cluster_name`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 20. `location` = `var.region`

**What it means:** Cloud deployment location; choose one supporting the requested resources/zones.

**Syntax:** `location` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 21. `network` = `var.network`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `network` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 22. `subnetwork` = `var.subnetwork`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `subnetwork` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 23. `remove_default_node_pool` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `remove_default_node_pool` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 24. `initial_node_count` = `1`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `initial_node_count` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 25. `cluster_secondary_range_name` = `var.pods_secondary_range_name`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `cluster_secondary_range_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 26. `services_secondary_range_name` = `var.services_secondary_range_name`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `services_secondary_range_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 27. `enable_private_nodes` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `enable_private_nodes` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 28. `enable_private_endpoint` = `false`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `enable_private_endpoint` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 29. `master_ipv4_cidr_block` = `"172.16.0.0/28" # must not overlap VPC/on-prem routes`

**What it means:** Reserved IP range for GKE control plane; do not overlap VPC/on-prem.

**Syntax:** `master_ipv4_cidr_block` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 30. `for_each` = `var.authorized_admin_cidrs`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `for_each` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 31. `cidr_block` = `cidr_blocks.value`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `cidr_block` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 32. `display_name` = `"approved-administrator"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `display_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 33. `workload_pool` = `"${var.project_id}.svc.id.goog"`

**What it means:** Google Workload Identity pool linking Kubernetes and GCP service accounts.

**Syntax:** `workload_pool` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 34. `logging_service` = `"logging.googleapis.com/kubernetes"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `logging_service` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 35. `monitoring_service` = `"monitoring.googleapis.com/kubernetes"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `monitoring_service` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 36. `deletion_protection` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `deletion_protection` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 37. resource google_container_node_pool apps

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 38. `name` = `"apps"`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 39. `cluster` = `google_container_cluster.this.name`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `cluster` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 40. `location` = `var.region`

**What it means:** Cloud deployment location; choose one supporting the requested resources/zones.

**Syntax:** `location` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 41. `node_count` = `1 # per zone; 3 regional zones => 3 total nodes`

**What it means:** Worker count, with per-zone semantics depending on provider.

**Syntax:** `node_count` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 42. `auto_repair` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `auto_repair` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 43. `auto_upgrade` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `auto_upgrade` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 44. `machine_type` = `"e2-standard-4"`

**What it means:** GPU/CPU/RAM machine shape determining capacity and cost.

**Syntax:** `machine_type` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 45. `service_account` = `var.node_service_account`

**What it means:** Service identity granted permissions to GKE node VMs.

**Syntax:** `service_account` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 46. `oauth_scopes` = `["https://www.googleapis.com/auth/cloud-platform"]`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `oauth_scopes` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 47. `enable_secure_boot` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `enable_secure_boot` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 48. `enable_integrity_monitoring` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `enable_integrity_monitoring` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 49. output cluster_name 

**What this means:** Exposes a calculated value after planning/apply. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

