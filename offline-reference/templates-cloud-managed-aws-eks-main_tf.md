# Offline infrastructure template explanation: templates/cloud-managed/aws-eks/main.tf

Source: [templates/cloud-managed/aws-eks/main.tf](../templates/cloud-managed/aws-eks/main.tf). These HCL/YAML settings have **no effect until an authorized provision/installer runs**. Review schema and provider compatibility with vendor documentation and obtain cost/change approval.

### 1. `required_version` = `">= 1.8.0"`

**Source line:** 4. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `required_version` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 2. `aws` = `{ source = "hashicorp/aws", version = ">= 5.0, < 7.0" }`

**Source line:** 6. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `aws` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 3. provider aws 

**Purpose:** Terraform provider block. **Syntax:** provider keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 4. variable region 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 5. variable cluster_name 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 6. variable subnet_ids 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 7. `type` = `list(string)`

**Source line:** 13. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `type` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 8. `condition` = `length(var.subnet_ids) >= 2`

**Source line:** 15. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `condition` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 9. `error_message` = `"Specify >=2 private subnets in different AZs."`

**Source line:** 16. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `error_message` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 10. variable kubernetes_version 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 11. variable node_instance_types 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 12. `type` = `list(string)`

**Source line:** 21. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `type` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 13. `default` = `["m6i.large"]`

**Source line:** 22. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `default` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 14. data aws_caller_identity current

**Purpose:** Terraform data block. **Syntax:** data keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 15. data aws_iam_policy_document eks_assume

**Purpose:** Terraform data block. **Syntax:** data keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 16. `actions` = `["sts:AssumeRole"]`

**Source line:** 27. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `actions` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 17. `type` = `"Service"`

**Source line:** 29. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `type` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 18. `identifiers` = `["eks.amazonaws.com"]`

**Source line:** 30. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `identifiers` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 19. data aws_iam_policy_document node_assume

**Purpose:** Terraform data block. **Syntax:** data keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 20. `actions` = `["sts:AssumeRole"]`

**Source line:** 36. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `actions` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 21. `type` = `"Service"`

**Source line:** 38. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `type` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 22. `identifiers` = `["ec2.amazonaws.com"]`

**Source line:** 39. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `identifiers` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 23. resource aws_iam_role cluster

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 24. `name_prefix` = `"${var.cluster_name}-control-"`

**Source line:** 44. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name_prefix` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 25. `assume_role_policy` = `data.aws_iam_policy_document.eks_assume.json`

**Source line:** 45. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `assume_role_policy` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 26. resource aws_iam_role_policy_attachment cluster

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 27. `role` = `aws_iam_role.cluster.name`

**Source line:** 48. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `role` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 28. `policy_arn` = `"arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"`

**Source line:** 49. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `policy_arn` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 29. resource aws_iam_role node

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 30. `name_prefix` = `"${var.cluster_name}-nodes-"`

**Source line:** 52. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name_prefix` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 31. `assume_role_policy` = `data.aws_iam_policy_document.node_assume.json`

**Source line:** 53. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `assume_role_policy` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 32. resource aws_iam_role_policy_attachment worker

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 33. `role` = `aws_iam_role.node.name`

**Source line:** 56. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `role` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 34. `policy_arn` = `"arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"`

**Source line:** 57. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `policy_arn` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 35. resource aws_iam_role_policy_attachment registry

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 36. `role` = `aws_iam_role.node.name`

**Source line:** 60. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `role` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 37. `policy_arn` = `"arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly"`

**Source line:** 61. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `policy_arn` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 38. resource aws_eks_cluster this

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 39. `name` = `var.cluster_name`

**Source line:** 64. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 40. `role_arn` = `aws_iam_role.cluster.arn`

**Source line:** 65. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `role_arn` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 41. `version` = `var.kubernetes_version`

**Source line:** 66. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `version` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 42. `subnet_ids` = `var.subnet_ids`

**Source line:** 68. **Meaning:** Existing approved subnets that must span failure domains.

**Syntax:** key `subnet_ids` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 43. `endpoint_private_access` = `true`

**Source line:** 69. **Meaning:** Whether API is reachable privately.

**Syntax:** key `endpoint_private_access` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 44. `endpoint_public_access` = `false`

**Source line:** 70. **Meaning:** Whether the API is publicly exposed.

**Syntax:** key `endpoint_public_access` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 45. `enabled_cluster_log_types` = `["api", "audit", "authenticator", "controllerManager", "scheduler"]`

**Source line:** 72. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `enabled_cluster_log_types` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 46. `depends_on` = `[aws_iam_role_policy_attachment.cluster]`

**Source line:** 74. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `depends_on` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 47. resource aws_eks_addon vpc_cni

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 48. `cluster_name` = `aws_eks_cluster.this.name`

**Source line:** 77. **Meaning:** Stable cluster identifier used in APIs, DNS and costs.

**Syntax:** key `cluster_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 49. `addon_name` = `"vpc-cni"`

**Source line:** 78. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `addon_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 50. resource aws_eks_addon coredns

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 51. `cluster_name` = `aws_eks_cluster.this.name`

**Source line:** 81. **Meaning:** Stable cluster identifier used in APIs, DNS and costs.

**Syntax:** key `cluster_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 52. `addon_name` = `"coredns"`

**Source line:** 82. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `addon_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 53. resource aws_eks_addon kube_proxy

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 54. `cluster_name` = `aws_eks_cluster.this.name`

**Source line:** 85. **Meaning:** Stable cluster identifier used in APIs, DNS and costs.

**Syntax:** key `cluster_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 55. `addon_name` = `"kube-proxy"`

**Source line:** 86. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `addon_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 56. resource aws_eks_node_group workers

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 57. `cluster_name` = `aws_eks_cluster.this.name`

**Source line:** 89. **Meaning:** Stable cluster identifier used in APIs, DNS and costs.

**Syntax:** key `cluster_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 58. `node_group_name` = `"general"`

**Source line:** 90. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `node_group_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 59. `node_role_arn` = `aws_iam_role.node.arn`

**Source line:** 91. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `node_role_arn` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 60. `subnet_ids` = `var.subnet_ids`

**Source line:** 92. **Meaning:** Existing approved subnets that must span failure domains.

**Syntax:** key `subnet_ids` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 61. `instance_types` = `var.node_instance_types`

**Source line:** 93. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `instance_types` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 62. `desired_size` = `3`

**Source line:** 95. **Meaning:** Desired node group capacity.

**Syntax:** key `desired_size` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 63. `min_size` = `3`

**Source line:** 96. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `min_size` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 64. `max_size` = `6`

**Source line:** 97. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `max_size` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 65. `depends_on` = `[aws_iam_role_policy_attachment.worker, aws_iam_role_policy_attachment.registry]`

**Source line:** 100. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `depends_on` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 66. output cluster_name 

**Purpose:** Terraform output block. **Syntax:** output keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 67. output cluster_endpoint 

**Purpose:** Terraform output block. **Syntax:** output keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

