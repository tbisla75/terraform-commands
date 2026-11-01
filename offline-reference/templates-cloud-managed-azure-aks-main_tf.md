# Offline infrastructure template explanation: templates/cloud-managed/azure-aks/main.tf

Source: [templates/cloud-managed/azure-aks/main.tf](../templates/cloud-managed/azure-aks/main.tf). These HCL/YAML settings have **no effect until an authorized provision/installer runs**. Review schema and provider compatibility with vendor documentation and obtain cost/change approval.

### 1. `required_version` = `">= 1.8.0"`

**Source line:** 3. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `required_version` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 2. `azurerm` = `{ source = "hashicorp/azurerm", version = ">= 4.0, < 6.0" }`

**Source line:** 5. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `azurerm` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 3. provider azurerm 

**Purpose:** Terraform provider block. **Syntax:** provider keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 4. variable subscription_id 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 5. variable resource_group_name 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 6. variable location 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 7. variable cluster_name 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 8. variable vnet_subnet_id 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 9. variable kubernetes_version 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 10. variable admin_group_object_ids 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 11. data azurerm_resource_group existing

**Purpose:** Terraform data block. **Syntax:** data keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 12. resource azurerm_kubernetes_cluster this

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 13. `name` = `var.cluster_name`

**Source line:** 18. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 14. `location` = `var.location`

**Source line:** 19. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `location` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 15. `resource_group_name` = `data.azurerm_resource_group.existing.name`

**Source line:** 20. **Meaning:** Azure resource group target.

**Syntax:** key `resource_group_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 16. `dns_prefix` = `var.cluster_name`

**Source line:** 21. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `dns_prefix` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 17. `kubernetes_version` = `var.kubernetes_version`

**Source line:** 22. **Meaning:** Supported version (must exist in selected cloud region).

**Syntax:** key `kubernetes_version` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 18. `private_cluster_enabled` = `true`

**Source line:** 23. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `private_cluster_enabled` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 19. `local_account_disabled` = `true`

**Source line:** 24. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `local_account_disabled` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 20. `role_based_access_control_enabled` = `true`

**Source line:** 25. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `role_based_access_control_enabled` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 21. `sku_tier` = `"Standard"`

**Source line:** 26. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `sku_tier` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 22. `oidc_issuer_enabled` = `true`

**Source line:** 27. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `oidc_issuer_enabled` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 23. `workload_identity_enabled` = `true`

**Source line:** 28. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `workload_identity_enabled` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 24. `name` = `"system"`

**Source line:** 30. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 25. `vm_size` = `"Standard_D4s_v5"`

**Source line:** 31. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `vm_size` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 26. `node_count` = `3`

**Source line:** 32. **Meaning:** Node pool capacity; regional/zone semantics differ.

**Syntax:** key `node_count` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 27. `vnet_subnet_id` = `var.vnet_subnet_id`

**Source line:** 33. **Meaning:** Azure network subnet resource identifier.

**Syntax:** key `vnet_subnet_id` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 28. `zones` = `["1", "2", "3"]`

**Source line:** 34. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `zones` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 29. `max_pods` = `30`

**Source line:** 35. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `max_pods` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 30. `only_critical_addons_enabled` = `true`

**Source line:** 36. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `only_critical_addons_enabled` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 31. `network_plugin` = `"azure"`

**Source line:** 41. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `network_plugin` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 32. `network_plugin_mode` = `"overlay"`

**Source line:** 42. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `network_plugin_mode` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 33. `azure_rbac_enabled` = `true`

**Source line:** 45. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `azure_rbac_enabled` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 34. `admin_group_object_ids` = `var.admin_group_object_ids`

**Source line:** 46. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `admin_group_object_ids` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 35. resource azurerm_kubernetes_cluster_node_pool apps

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 36. `name` = `"apps"`

**Source line:** 50. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 37. `kubernetes_cluster_id` = `azurerm_kubernetes_cluster.this.id`

**Source line:** 51. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `kubernetes_cluster_id` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 38. `vm_size` = `"Standard_D4s_v5"`

**Source line:** 52. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `vm_size` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 39. `node_count` = `3`

**Source line:** 53. **Meaning:** Node pool capacity; regional/zone semantics differ.

**Syntax:** key `node_count` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 40. `vnet_subnet_id` = `var.vnet_subnet_id`

**Source line:** 54. **Meaning:** Azure network subnet resource identifier.

**Syntax:** key `vnet_subnet_id` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 41. `zones` = `["1", "2", "3"]`

**Source line:** 55. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `zones` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 42. `mode` = `"User"`

**Source line:** 56. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `mode` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 43. output cluster_name 

**Purpose:** Terraform output block. **Syntax:** output keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

