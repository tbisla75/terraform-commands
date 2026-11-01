# Terraform / cluster template explained simply: templates/cloud-managed/aws-eks/main.tf

This document explains **each significant configuration key** without needing ChatGPT. Templates are starters: do not treat placeholders as a runnable production cluster. Exact field support depends on Terraform provider version or OpenShift/kubeadm version. Original: [templates/cloud-managed/aws-eks/main.tf](../templates/cloud-managed/aws-eks/main.tf).

## 1. `required_version` = `">= 1.8.0"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `required_version` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 2. `aws` = `{ source = "hashicorp/aws", version = ">= 5.0, < 7.0" }`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `aws` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 3. provider aws 

**What this means:** Configures which vendor/cloud API Terraform connects to. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 4. variable region 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 5. variable cluster_name 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 6. variable subnet_ids 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 7. `type` = `list(string)`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `type` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 8. `condition` = `length(var.subnet_ids) >= 2`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `condition` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 9. `error_message` = `"Specify >=2 private subnets in different AZs."`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `error_message` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 10. variable kubernetes_version 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 11. variable node_instance_types 

**What this means:** Defines an input value supplied by tfvars, environment or a calling module. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 12. `type` = `list(string)`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `type` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 13. `default` = `["m6i.large"]`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `default` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 14. data aws_caller_identity current

**What this means:** Reads existing infrastructure without creating it (subject to provider behavior). The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 15. data aws_iam_policy_document eks_assume

**What this means:** Reads existing infrastructure without creating it (subject to provider behavior). The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 16. `actions` = `["sts:AssumeRole"]`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `actions` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 17. `type` = `"Service"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `type` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 18. `identifiers` = `["eks.amazonaws.com"]`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `identifiers` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 19. data aws_iam_policy_document node_assume

**What this means:** Reads existing infrastructure without creating it (subject to provider behavior). The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 20. `actions` = `["sts:AssumeRole"]`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `actions` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 21. `type` = `"Service"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `type` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 22. `identifiers` = `["ec2.amazonaws.com"]`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `identifiers` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 23. resource aws_iam_role cluster

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 24. `name_prefix` = `"${var.cluster_name}-control-"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `name_prefix` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 25. `assume_role_policy` = `data.aws_iam_policy_document.eks_assume.json`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `assume_role_policy` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 26. resource aws_iam_role_policy_attachment cluster

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 27. `role` = `aws_iam_role.cluster.name`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 28. `policy_arn` = `"arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `policy_arn` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 29. resource aws_iam_role node

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 30. `name_prefix` = `"${var.cluster_name}-nodes-"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `name_prefix` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 31. `assume_role_policy` = `data.aws_iam_policy_document.node_assume.json`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `assume_role_policy` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 32. resource aws_iam_role_policy_attachment worker

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 33. `role` = `aws_iam_role.node.name`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 34. `policy_arn` = `"arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `policy_arn` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 35. resource aws_iam_role_policy_attachment registry

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 36. `role` = `aws_iam_role.node.name`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 37. `policy_arn` = `"arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `policy_arn` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 38. resource aws_eks_cluster this

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 39. `name` = `var.cluster_name`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 40. `role_arn` = `aws_iam_role.cluster.arn`

**What it means:** Cloud IAM role authorized for the managed service.

**Syntax:** `role_arn` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 41. `version` = `var.kubernetes_version`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `version` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 42. `subnet_ids` = `var.subnet_ids`

**What it means:** Existing private subnet IDs used by managed cluster resources; distribute across availability zones.

**Syntax:** `subnet_ids` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 43. `endpoint_private_access` = `true`

**What it means:** Whether private network clients can reach the EKS API.

**Syntax:** `endpoint_private_access` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 44. `endpoint_public_access` = `false`

**What it means:** Whether the control-plane endpoint is reachable from the public internet.

**Syntax:** `endpoint_public_access` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 45. `enabled_cluster_log_types` = `["api", "audit", "authenticator", "controllerManager", "scheduler"]`

**What it means:** Control-plane logs exported for troubleshooting and audit.

**Syntax:** `enabled_cluster_log_types` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 46. `depends_on` = `[aws_iam_role_policy_attachment.cluster]`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `depends_on` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 47. resource aws_eks_addon vpc_cni

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 48. `cluster_name` = `aws_eks_cluster.this.name`

**What it means:** Name of the Kubernetes/managed-cluster resource.

**Syntax:** `cluster_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 49. `addon_name` = `"vpc-cni"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `addon_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 50. resource aws_eks_addon coredns

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 51. `cluster_name` = `aws_eks_cluster.this.name`

**What it means:** Name of the Kubernetes/managed-cluster resource.

**Syntax:** `cluster_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 52. `addon_name` = `"coredns"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `addon_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 53. resource aws_eks_addon kube_proxy

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 54. `cluster_name` = `aws_eks_cluster.this.name`

**What it means:** Name of the Kubernetes/managed-cluster resource.

**Syntax:** `cluster_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 55. `addon_name` = `"kube-proxy"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `addon_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 56. resource aws_eks_node_group workers

**What this means:** Declares a cloud/Kubernetes object Terraform may create, modify or delete. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 57. `cluster_name` = `aws_eks_cluster.this.name`

**What it means:** Name of the Kubernetes/managed-cluster resource.

**Syntax:** `cluster_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 58. `node_group_name` = `"general"`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `node_group_name` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 59. `node_role_arn` = `aws_iam_role.node.arn`

**What it means:** IAM role assumed by compute nodes, needs least privilege.

**Syntax:** `node_role_arn` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 60. `subnet_ids` = `var.subnet_ids`

**What it means:** Existing private subnet IDs used by managed cluster resources; distribute across availability zones.

**Syntax:** `subnet_ids` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 61. `instance_types` = `var.node_instance_types`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `instance_types` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 62. `desired_size` = `3`

**What it means:** Requested worker count in AWS EKS node group.

**Syntax:** `desired_size` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 63. `min_size` = `3`

**What it means:** Minimum worker count; too low may break high availability.

**Syntax:** `min_size` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 64. `max_size` = `6`

**What it means:** Maximum autoscaling worker count; affects quota/cost.

**Syntax:** `max_size` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 65. `depends_on` = `[aws_iam_role_policy_attachment.worker, aws_iam_role_policy_attachment.regi`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `depends_on` is the field name; `=` assigns a typed HCL value. Nested `{}` blocks determine which resource it belongs to.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Run `terraform fmt`, `terraform init`, `terraform validate`, then review `terraform plan` before applying.

## 66. output cluster_name 

**What this means:** Exposes a calculated value after planning/apply. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

## 67. output cluster_endpoint 

**What this means:** Exposes a calculated value after planning/apply. The quoted words name the resource type/provider or variable and its local identifier. **Check:** provider/API permissions, backend, changes, resource cost and deletion behavior.

