# Offline command / configuration reference: `templates/cloud-managed/azure-aks/main.tf`

Generated from repository source by `tools/build_offline_reference.py`. **12 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/cloud-managed/azure-aks/main.tf`](../templates/cloud-managed/azure-aks/main.tf)

### 1. Terraform provider: `azurerm`

**Source line:** 8. **Purpose:** Declare a provider object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 2. Terraform variable: `subscription_id`

**Source line:** 9. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 3. Terraform variable: `resource_group_name`

**Source line:** 10. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 4. Terraform variable: `location`

**Source line:** 11. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 5. Terraform variable: `cluster_name`

**Source line:** 12. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 6. Terraform variable: `vnet_subnet_id`

**Source line:** 13. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 7. Terraform variable: `kubernetes_version`

**Source line:** 14. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 8. Terraform variable: `admin_group_object_ids`

**Source line:** 15. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 9. Terraform data: `azurerm_resource_group existing`

**Source line:** 16. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 10. Terraform resource: `azurerm_kubernetes_cluster this`

**Source line:** 17. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 11. Terraform resource: `azurerm_kubernetes_cluster_node_pool apps`

**Source line:** 49. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 12. Terraform output: `cluster_name`

**Source line:** 59. **Purpose:** Declare a output object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

