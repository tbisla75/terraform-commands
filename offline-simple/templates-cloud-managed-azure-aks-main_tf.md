# Terraform / cluster template explained simply: templates/cloud-managed/azure-aks/main.tf

This document explains **each significant configuration key** without needing ChatGPT. Templates are starters: do not treat placeholders as a runnable production cluster. Exact field support depends on Terraform provider version or OpenShift/kubeadm version. Original: [templates/cloud-managed/azure-aks/main.tf](../templates/cloud-managed/azure-aks/main.tf).

## 1. `required_version` = `">= 1.8.0"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `required_version` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 2. `azurerm` = `{ source = "hashicorp/azurerm", version = ">= 4.0, < 6.0" }`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `azurerm` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 3. provider azurerm 

**What this means:** Configures which vendor/cloud API Terraform connects to. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 4. variable subscription_id 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 5. variable resource_group_name 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 6. variable location 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 7. variable cluster_name 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 8. variable vnet_subnet_id 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 9. variable kubernetes_version 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 10. variable admin_group_object_ids 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 11. data azurerm_resource_group existing

**What this means:** Reads existing infrastructure without creating it (subject to provider behavior). The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 12. resource azurerm_kubernetes_cluster this

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 13. `name` = `var.cluster_name`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 14. `location` = `var.location`

**What it means:** Cloud deployment location; choose one supporting the requested resources/zones.

**Syntax:** `location` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 15. `resource_group_name` = `data.azurerm_resource_group.existing.name`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `resource_group_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 16. `dns_prefix` = `var.cluster_name`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `dns_prefix` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 17. `kubernetes_version` = `var.kubernetes_version`

**What it means:** Managed Kubernetes version; must be available in region and supported by the provider.

**Syntax:** `kubernetes_version` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 18. `private_cluster_enabled` = `true`

**What it means:** Whether Azure AKS API is private; access needs VNet/VPN/bastion.

**Syntax:** `private_cluster_enabled` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 19. `local_account_disabled` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `local_account_disabled` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 20. `role_based_access_control_enabled` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `role_based_access_control_enabled` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 21. `sku_tier` = `"Standard"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `sku_tier` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 22. `oidc_issuer_enabled` = `true`

**What it means:** Enables OIDC identity issuance for AKS workload federation.

**Syntax:** `oidc_issuer_enabled` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 23. `workload_identity_enabled` = `true`

**What it means:** Allows workloads to authenticate to Azure services without static keys.

**Syntax:** `workload_identity_enabled` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 24. `name` = `"system"`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 25. `vm_size` = `"Standard_D4s_v5"`

**What it means:** Azure VM shape determining CPU/RAM and charges.

**Syntax:** `vm_size` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 26. `node_count` = `3`

**What it means:** Worker count, with per-zone semantics depending on provider.

**Syntax:** `node_count` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 27. `vnet_subnet_id` = `var.vnet_subnet_id`

**What it means:** Azure subnet resource ID where AKS nodes attach.

**Syntax:** `vnet_subnet_id` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 28. `zones` = `["1", "2", "3"]`

**What it means:** Availability zones for resilience; confirm supported regions.

**Syntax:** `zones` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 29. `max_pods` = `30`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `max_pods` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 30. `only_critical_addons_enabled` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `only_critical_addons_enabled` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 31. `network_plugin` = `"azure"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `network_plugin` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 32. `network_plugin_mode` = `"overlay"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `network_plugin_mode` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 33. `azure_rbac_enabled` = `true`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `azure_rbac_enabled` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 34. `admin_group_object_ids` = `var.admin_group_object_ids`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `admin_group_object_ids` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 35. resource azurerm_kubernetes_cluster_node_pool apps

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 36. `name` = `"apps"`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 37. `kubernetes_cluster_id` = `azurerm_kubernetes_cluster.this.id`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `kubernetes_cluster_id` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 38. `vm_size` = `"Standard_D4s_v5"`

**What it means:** Azure VM shape determining CPU/RAM and charges.

**Syntax:** `vm_size` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 39. `node_count` = `3`

**What it means:** Worker count, with per-zone semantics depending on provider.

**Syntax:** `node_count` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 40. `vnet_subnet_id` = `var.vnet_subnet_id`

**What it means:** Azure subnet resource ID where AKS nodes attach.

**Syntax:** `vnet_subnet_id` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 41. `zones` = `["1", "2", "3"]`

**What it means:** Availability zones for resilience; confirm supported regions.

**Syntax:** `zones` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 42. `mode` = `"User"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `mode` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 43. output cluster_name 

**What this means:** Exposes a calculated value after planning/apply. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

