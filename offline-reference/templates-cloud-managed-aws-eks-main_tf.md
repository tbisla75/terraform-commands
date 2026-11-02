# Offline command / configuration reference: `templates/cloud-managed/aws-eks/main.tf`

Generated from repository source by `tools/build_offline_reference.py`. **67 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/cloud-managed/aws-eks/main.tf`](../templates/cloud-managed/aws-eks/main.tf)

### 1. Configuration field required_version

**Source line:** 4. **Language:** hcl. **Full syntax:** required_version = ">= 1.8.0"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 2. Configuration field aws

**Source line:** 6. **Language:** hcl. **Full syntax:** aws = { source = "hashicorp/aws", version = ">= 5.0, < 7.0" }

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 3. Terraform provider: `aws`

**Source line:** 9. **Purpose:** Declare a provider object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 4. Terraform variable: `region`

**Source line:** 10. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 5. Terraform variable: `cluster_name`

**Source line:** 11. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 6. Terraform variable: `subnet_ids`

**Source line:** 12. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 7. Configuration field type

**Source line:** 13. **Language:** hcl. **Full syntax:** type = list(string)

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 8. Configuration field condition

**Source line:** 15. **Language:** hcl. **Full syntax:** condition = length(var.subnet_ids) >= 2

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 9. Configuration field error_message

**Source line:** 16. **Language:** hcl. **Full syntax:** error_message = "Specify >=2 private subnets in different AZs."

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 10. Terraform variable: `kubernetes_version`

**Source line:** 19. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 11. Terraform variable: `node_instance_types`

**Source line:** 20. **Purpose:** Declare a variable object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 12. Configuration field type

**Source line:** 21. **Language:** hcl. **Full syntax:** type = list(string)

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 13. Configuration field default

**Source line:** 22. **Language:** hcl. **Full syntax:** default = ["m6i.large"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 14. Terraform data: `aws_caller_identity current`

**Source line:** 24. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 15. Terraform data: `aws_iam_policy_document eks_assume`

**Source line:** 25. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 16. Configuration field actions

**Source line:** 27. **Language:** hcl. **Full syntax:** actions = ["sts:AssumeRole"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 17. Configuration field type

**Source line:** 29. **Language:** hcl. **Full syntax:** type = "Service"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 18. Configuration field identifiers

**Source line:** 30. **Language:** hcl. **Full syntax:** identifiers = ["eks.amazonaws.com"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 19. Terraform data: `aws_iam_policy_document node_assume`

**Source line:** 34. **Purpose:** Declare a data object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 20. Configuration field actions

**Source line:** 36. **Language:** hcl. **Full syntax:** actions = ["sts:AssumeRole"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 21. Configuration field type

**Source line:** 38. **Language:** hcl. **Full syntax:** type = "Service"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 22. Configuration field identifiers

**Source line:** 39. **Language:** hcl. **Full syntax:** identifiers = ["ec2.amazonaws.com"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 23. Terraform resource: `aws_iam_role cluster`

**Source line:** 43. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 24. Configuration field name_prefix

**Source line:** 44. **Language:** hcl. **Full syntax:** name_prefix = "${var.cluster_name}-control-"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 25. Configuration field assume_role_policy

**Source line:** 45. **Language:** hcl. **Full syntax:** assume_role_policy = data.aws_iam_policy_document.eks_assume.json

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 26. Terraform resource: `aws_iam_role_policy_attachment cluster`

**Source line:** 47. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 27. Configuration field role

**Source line:** 48. **Language:** hcl. **Full syntax:** role = aws_iam_role.cluster.name

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 28. Configuration field policy_arn

**Source line:** 49. **Language:** hcl. **Full syntax:** policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 29. Terraform resource: `aws_iam_role node`

**Source line:** 51. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 30. Configuration field name_prefix

**Source line:** 52. **Language:** hcl. **Full syntax:** name_prefix = "${var.cluster_name}-nodes-"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 31. Configuration field assume_role_policy

**Source line:** 53. **Language:** hcl. **Full syntax:** assume_role_policy = data.aws_iam_policy_document.node_assume.json

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 32. Terraform resource: `aws_iam_role_policy_attachment worker`

**Source line:** 55. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 33. Configuration field role

**Source line:** 56. **Language:** hcl. **Full syntax:** role = aws_iam_role.node.name

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 34. Configuration field policy_arn

**Source line:** 57. **Language:** hcl. **Full syntax:** policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 35. Terraform resource: `aws_iam_role_policy_attachment registry`

**Source line:** 59. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 36. Configuration field role

**Source line:** 60. **Language:** hcl. **Full syntax:** role = aws_iam_role.node.name

**What it does:** Selected node role or permissions context.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 37. Configuration field policy_arn

**Source line:** 61. **Language:** hcl. **Full syntax:** policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 38. Terraform resource: `aws_eks_cluster this`

**Source line:** 63. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 39. Configuration field name

**Source line:** 64. **Language:** hcl. **Full syntax:** name = var.cluster_name

**What it does:** Resource/cluster/host identity in the enclosing object.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 40. Configuration field role_arn

**Source line:** 65. **Language:** hcl. **Full syntax:** role_arn = aws_iam_role.cluster.arn

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 41. Configuration field version

**Source line:** 66. **Language:** hcl. **Full syntax:** version = var.kubernetes_version

**What it does:** Version constraint or pinned version; check compatibility.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 42. Configuration field subnet_ids

**Source line:** 68. **Language:** hcl. **Full syntax:** subnet_ids = var.subnet_ids

**What it does:** Network subnet IDs for the resource; ensure AZ diversity.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 43. Configuration field endpoint_private_access

**Source line:** 69. **Language:** hcl. **Full syntax:** endpoint_private_access = true

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 44. Configuration field endpoint_public_access

**Source line:** 70. **Language:** hcl. **Full syntax:** endpoint_public_access = false

**What it does:** Whether control-plane API is exposed publicly.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 45. Configuration field enabled_cluster_log_types

**Source line:** 72. **Language:** hcl. **Full syntax:** enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 46. Configuration field depends_on

**Source line:** 74. **Language:** hcl. **Full syntax:** depends_on = [aws_iam_role_policy_attachment.cluster]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 47. Terraform resource: `aws_eks_addon vpc_cni`

**Source line:** 76. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 48. Configuration field cluster_name

**Source line:** 77. **Language:** hcl. **Full syntax:** cluster_name = aws_eks_cluster.this.name

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 49. Configuration field addon_name

**Source line:** 78. **Language:** hcl. **Full syntax:** addon_name = "vpc-cni"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 50. Terraform resource: `aws_eks_addon coredns`

**Source line:** 80. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 51. Configuration field cluster_name

**Source line:** 81. **Language:** hcl. **Full syntax:** cluster_name = aws_eks_cluster.this.name

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 52. Configuration field addon_name

**Source line:** 82. **Language:** hcl. **Full syntax:** addon_name = "coredns"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 53. Terraform resource: `aws_eks_addon kube_proxy`

**Source line:** 84. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 54. Configuration field cluster_name

**Source line:** 85. **Language:** hcl. **Full syntax:** cluster_name = aws_eks_cluster.this.name

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 55. Configuration field addon_name

**Source line:** 86. **Language:** hcl. **Full syntax:** addon_name = "kube-proxy"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 56. Terraform resource: `aws_eks_node_group workers`

**Source line:** 88. **Purpose:** Declare a resource object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 57. Configuration field cluster_name

**Source line:** 89. **Language:** hcl. **Full syntax:** cluster_name = aws_eks_cluster.this.name

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 58. Configuration field node_group_name

**Source line:** 90. **Language:** hcl. **Full syntax:** node_group_name = "general"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 59. Configuration field node_role_arn

**Source line:** 91. **Language:** hcl. **Full syntax:** node_role_arn = aws_iam_role.node.arn

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 60. Configuration field subnet_ids

**Source line:** 92. **Language:** hcl. **Full syntax:** subnet_ids = var.subnet_ids

**What it does:** Network subnet IDs for the resource; ensure AZ diversity.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 61. Configuration field instance_types

**Source line:** 93. **Language:** hcl. **Full syntax:** instance_types = var.node_instance_types

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 62. Configuration field desired_size

**Source line:** 95. **Language:** hcl. **Full syntax:** desired_size = 3

**What it does:** Desired managed worker group size.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 63. Configuration field min_size

**Source line:** 96. **Language:** hcl. **Full syntax:** min_size = 3

**What it does:** Lower autoscaling bound; assess availability.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 64. Configuration field max_size

**Source line:** 97. **Language:** hcl. **Full syntax:** max_size = 6

**What it does:** Upper autoscaling bound; assess quota and costs.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 65. Configuration field depends_on

**Source line:** 100. **Language:** hcl. **Full syntax:** depends_on = [aws_iam_role_policy_attachment.worker, aws_iam_role_policy_attachment.registry]

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 66. Terraform output: `cluster_name`

**Source line:** 102. **Purpose:** Declare a output object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

### 67. Terraform output: `cluster_endpoint`

**Source line:** 103. **Purpose:** Declare a output object. Terraform validates provider schema, references and lifecycle during plan. **Safety:** Real changes require an approved apply; data sources can query provider APIs during plan. Confirm every resource argument against the installed provider schema.

