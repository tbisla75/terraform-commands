# Offline command / configuration reference: `templates/cloud-managed/aws-eks/main.tf`

Generated from repository source by `tools/build_offline_reference.py`. **21 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/cloud-managed/aws-eks/main.tf`](../templates/cloud-managed/aws-eks/main.tf)

### 1. Terraform provider: `aws`

**Source line:** 9. **Purpose:** Declare a provider object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 2. Terraform variable: `region`

**Source line:** 10. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 3. Terraform variable: `cluster_name`

**Source line:** 11. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 4. Terraform variable: `subnet_ids`

**Source line:** 12. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 5. Terraform variable: `kubernetes_version`

**Source line:** 19. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 6. Terraform variable: `node_instance_types`

**Source line:** 20. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 7. Terraform data: `aws_caller_identity current`

**Source line:** 24. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 8. Terraform data: `aws_iam_policy_document eks_assume`

**Source line:** 25. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 9. Terraform data: `aws_iam_policy_document node_assume`

**Source line:** 34. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 10. Terraform resource: `aws_iam_role cluster`

**Source line:** 43. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 11. Terraform resource: `aws_iam_role_policy_attachment cluster`

**Source line:** 47. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 12. Terraform resource: `aws_iam_role node`

**Source line:** 51. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 13. Terraform resource: `aws_iam_role_policy_attachment worker`

**Source line:** 55. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 14. Terraform resource: `aws_iam_role_policy_attachment registry`

**Source line:** 59. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 15. Terraform resource: `aws_eks_cluster this`

**Source line:** 63. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 16. Terraform resource: `aws_eks_addon vpc_cni`

**Source line:** 76. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 17. Terraform resource: `aws_eks_addon coredns`

**Source line:** 80. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 18. Terraform resource: `aws_eks_addon kube_proxy`

**Source line:** 84. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 19. Terraform resource: `aws_eks_node_group workers`

**Source line:** 88. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 20. Terraform output: `cluster_name`

**Source line:** 102. **Purpose:** Declare a output object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 21. Terraform output: `cluster_endpoint`

**Source line:** 103. **Purpose:** Declare a output object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

