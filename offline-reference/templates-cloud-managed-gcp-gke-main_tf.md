# Offline infrastructure template explanation: templates/cloud-managed/gcp-gke/main.tf

Source: [templates/cloud-managed/gcp-gke/main.tf](../templates/cloud-managed/gcp-gke/main.tf). These HCL/YAML settings have **no effect until an authorized provision/installer runs**. Review schema and provider compatibility with vendor documentation and obtain cost/change approval.

### 1. `required_version` = `">= 1.8.0"`

**Source line:** 3. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `required_version` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 2. `google` = `{ source = "hashicorp/google", version = ">= 5.0, < 8.0" }`

**Source line:** 5. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `google` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 3. provider google 

**Purpose:** Terraform provider block. **Syntax:** provider keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 4. `project` = `var.project_id`

**Source line:** 9. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `project` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 5. `region` = `var.region`

**Source line:** 10. **Meaning:** Cloud region in which resources are created.

**Syntax:** key `region` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 6. variable project_id 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 7. variable region 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 8. variable cluster_name 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 9. variable network 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 10. variable subnetwork 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 11. variable pods_secondary_range_name 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 12. variable services_secondary_range_name 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 13. variable release_channel 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 14. `type` = `string`

**Source line:** 20. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `type` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 15. `default` = `"REGULAR"`

**Source line:** 21. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `default` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 16. variable authorized_admin_cidrs 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 17. variable node_service_account 

**Purpose:** Terraform variable block. **Syntax:** variable keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

## 18. resource google_container_cluster this

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 19. `name` = `var.cluster_name`

**Source line:** 26. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 20. `location` = `var.region`

**Source line:** 27. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `location` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 21. `network` = `var.network`

**Source line:** 28. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `network` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 22. `subnetwork` = `var.subnetwork`

**Source line:** 29. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `subnetwork` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 23. `remove_default_node_pool` = `true`

**Source line:** 30. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `remove_default_node_pool` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 24. `initial_node_count` = `1`

**Source line:** 31. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `initial_node_count` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 25. `cluster_secondary_range_name` = `var.pods_secondary_range_name`

**Source line:** 34. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `cluster_secondary_range_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 26. `services_secondary_range_name` = `var.services_secondary_range_name`

**Source line:** 35. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `services_secondary_range_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 27. `enable_private_nodes` = `true`

**Source line:** 38. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `enable_private_nodes` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 28. `enable_private_endpoint` = `false`

**Source line:** 39. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `enable_private_endpoint` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 29. `master_ipv4_cidr_block` = `"172.16.0.0/28" # must not overlap VPC/on-prem routes`

**Source line:** 40. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `master_ipv4_cidr_block` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 30. `for_each` = `var.authorized_admin_cidrs`

**Source line:** 44. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `for_each` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 31. `cidr_block` = `cidr_blocks.value`

**Source line:** 46. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `cidr_block` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 32. `display_name` = `"approved-administrator"`

**Source line:** 47. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `display_name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 33. `workload_pool` = `"${var.project_id}.svc.id.goog"`

**Source line:** 52. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `workload_pool` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 34. `logging_service` = `"logging.googleapis.com/kubernetes"`

**Source line:** 54. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `logging_service` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 35. `monitoring_service` = `"monitoring.googleapis.com/kubernetes"`

**Source line:** 55. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `monitoring_service` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 36. `deletion_protection` = `true`

**Source line:** 56. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `deletion_protection` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 37. resource google_container_node_pool apps

**Purpose:** Terraform resource block. **Syntax:** resource keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

### 38. `name` = `"apps"`

**Source line:** 59. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 39. `cluster` = `google_container_cluster.this.name`

**Source line:** 60. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `cluster` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 40. `location` = `var.region`

**Source line:** 61. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `location` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 41. `node_count` = `1 # per zone; 3 regional zones => 3 total nodes`

**Source line:** 62. **Meaning:** Node pool capacity; regional/zone semantics differ.

**Syntax:** key `node_count` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 42. `auto_repair` = `true`

**Source line:** 64. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `auto_repair` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 43. `auto_upgrade` = `true`

**Source line:** 65. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `auto_upgrade` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 44. `machine_type` = `"e2-standard-4"`

**Source line:** 68. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `machine_type` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 45. `service_account` = `var.node_service_account`

**Source line:** 69. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `service_account` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 46. `oauth_scopes` = `["https://www.googleapis.com/auth/cloud-platform"]`

**Source line:** 70. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `oauth_scopes` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 47. `enable_secure_boot` = `true`

**Source line:** 73. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `enable_secure_boot` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 48. `enable_integrity_monitoring` = `true`

**Source line:** 74. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `enable_integrity_monitoring` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

## 49. output cluster_name 

**Purpose:** Terraform output block. **Syntax:** output keyword and quoted provider/type and optional local object name, followed by nested HCL attributes/blocks. **Dependency:** selected provider/module release schema and credentials. **Risk:** real cloud state changes on apply; a plan can expose sensitive state. Validate and inspect diffs before apply.

