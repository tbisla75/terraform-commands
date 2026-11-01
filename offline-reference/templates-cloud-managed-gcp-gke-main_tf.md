# Offline command / configuration reference: `templates/cloud-managed/gcp-gke/main.tf`

Generated from repository source by `tools/build_offline_reference.py`. **14 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/cloud-managed/gcp-gke/main.tf`](../templates/cloud-managed/gcp-gke/main.tf)

### 1. Terraform provider: `google`

**Source line:** 8. **Purpose:** Declare a provider object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 2. Terraform variable: `project_id`

**Source line:** 12. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 3. Terraform variable: `region`

**Source line:** 13. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 4. Terraform variable: `cluster_name`

**Source line:** 14. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 5. Terraform variable: `network`

**Source line:** 15. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 6. Terraform variable: `subnetwork`

**Source line:** 16. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 7. Terraform variable: `pods_secondary_range_name`

**Source line:** 17. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 8. Terraform variable: `services_secondary_range_name`

**Source line:** 18. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 9. Terraform variable: `release_channel`

**Source line:** 19. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 10. Terraform variable: `authorized_admin_cidrs`

**Source line:** 23. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 11. Terraform variable: `node_service_account`

**Source line:** 24. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 12. Terraform resource: `google_container_cluster this`

**Source line:** 25. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 13. Terraform resource: `google_container_node_pool apps`

**Source line:** 58. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 14. Terraform output: `cluster_name`

**Source line:** 78. **Purpose:** Declare a output object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

