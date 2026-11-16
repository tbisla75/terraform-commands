# Offline command / configuration reference: `templates/cloud-managed/azure-aks/main.tf`

Generated from repository source by `tools/build_offline_reference.py`. **43 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/cloud-managed/azure-aks/main.tf`](../templates/cloud-managed/azure-aks/main.tf)

### 1. Configuration field required_version

**Source line:** 3. **Language:** hcl. **Full syntax:** required_version = ">= 1.8.0"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 2. Configuration field azurerm

**Source line:** 5. **Language:** hcl. **Full syntax:** azurerm = { source = "hashicorp/azurerm", version = ">= 4.0, < 6.0" }

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 3. Terraform provider: `azurerm`

**Source line:** 8. **Purpose:** Declare a provider object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 4. Terraform variable: `subscription_id`

**Source line:** 9. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 5. Terraform variable: `resource_group_name`

**Source line:** 10. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 6. Terraform variable: `location`

**Source line:** 11. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 7. Terraform variable: `cluster_name`

**Source line:** 12. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 8. Terraform variable: `vnet_subnet_id`

**Source line:** 13. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 9. Terraform variable: `kubernetes_version`

**Source line:** 14. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 10. Terraform variable: `admin_group_object_ids`

**Source line:** 15. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 11. Terraform data: `azurerm_resource_group existing`

**Source line:** 16. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 12. Terraform resource: `azurerm_kubernetes_cluster this`

**Source line:** 17. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 13. Configuration field name

**Source line:** 18. **Language:** hcl. **Full syntax:** name = var.cluster_name

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 14. Configuration field location

**Source line:** 19. **Language:** hcl. **Full syntax:** location = var.location

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 15. Configuration field resource_group_name

**Source line:** 20. **Language:** hcl. **Full syntax:** resource_group_name = data.azurerm_resource_group.existing.name

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 16. Configuration field dns_prefix

**Source line:** 21. **Language:** hcl. **Full syntax:** dns_prefix = var.cluster_name

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 17. Configuration field kubernetes_version

**Source line:** 22. **Language:** hcl. **Full syntax:** kubernetes_version = var.kubernetes_version

**What it does:** Pinned target Kubernetes version supported by provider and region.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 18. Configuration field private_cluster_enabled

**Source line:** 23. **Language:** hcl. **Full syntax:** private_cluster_enabled = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 19. Configuration field local_account_disabled

**Source line:** 24. **Language:** hcl. **Full syntax:** local_account_disabled = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 20. Configuration field role_based_access_control_enabled

**Source line:** 25. **Language:** hcl. **Full syntax:** role_based_access_control_enabled = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 21. Configuration field sku_tier

**Source line:** 26. **Language:** hcl. **Full syntax:** sku_tier = "Standard"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 22. Configuration field oidc_issuer_enabled

**Source line:** 27. **Language:** hcl. **Full syntax:** oidc_issuer_enabled = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 23. Configuration field workload_identity_enabled

**Source line:** 28. **Language:** hcl. **Full syntax:** workload_identity_enabled = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 24. Configuration field name

**Source line:** 30. **Language:** hcl. **Full syntax:** name = "system"

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 25. Configuration field vm_size

**Source line:** 31. **Language:** hcl. **Full syntax:** vm_size = "Standard_D4s_v5"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 26. Configuration field node_count

**Source line:** 32. **Language:** hcl. **Full syntax:** node_count = 3

**What it does:** Desired node pool size; check zone and cost semantics.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 27. Configuration field vnet_subnet_id

**Source line:** 33. **Language:** hcl. **Full syntax:** vnet_subnet_id = var.vnet_subnet_id

**What it does:** Azure VNet subnet resource ID.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 28. Configuration field zones

**Source line:** 34. **Language:** hcl. **Full syntax:** zones = ["1", "2", "3"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 29. Configuration field max_pods

**Source line:** 35. **Language:** hcl. **Full syntax:** max_pods = 30

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 30. Configuration field only_critical_addons_enabled

**Source line:** 36. **Language:** hcl. **Full syntax:** only_critical_addons_enabled = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 31. Configuration field network_plugin

**Source line:** 41. **Language:** hcl. **Full syntax:** network_plugin = "azure"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 32. Configuration field network_plugin_mode

**Source line:** 42. **Language:** hcl. **Full syntax:** network_plugin_mode = "overlay"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 33. Configuration field azure_rbac_enabled

**Source line:** 45. **Language:** hcl. **Full syntax:** azure_rbac_enabled = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 34. Configuration field admin_group_object_ids

**Source line:** 46. **Language:** hcl. **Full syntax:** admin_group_object_ids = var.admin_group_object_ids

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 35. Terraform resource: `azurerm_kubernetes_cluster_node_pool apps`

**Source line:** 49. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 36. Configuration field name

**Source line:** 50. **Language:** hcl. **Full syntax:** name = "apps"

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 37. Configuration field kubernetes_cluster_id

**Source line:** 51. **Language:** hcl. **Full syntax:** kubernetes_cluster_id = azurerm_kubernetes_cluster.this.id

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 38. Configuration field vm_size

**Source line:** 52. **Language:** hcl. **Full syntax:** vm_size = "Standard_D4s_v5"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 39. Configuration field node_count

**Source line:** 53. **Language:** hcl. **Full syntax:** node_count = 3

**What it does:** Desired node pool size; check zone and cost semantics.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 40. Configuration field vnet_subnet_id

**Source line:** 54. **Language:** hcl. **Full syntax:** vnet_subnet_id = var.vnet_subnet_id

**What it does:** Azure VNet subnet resource ID.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 41. Configuration field zones

**Source line:** 55. **Language:** hcl. **Full syntax:** zones = ["1", "2", "3"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 42. Configuration field mode

**Source line:** 56. **Language:** hcl. **Full syntax:** mode = "User"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 43. Terraform output: `cluster_name`

**Source line:** 59. **Purpose:** Declare a output object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

