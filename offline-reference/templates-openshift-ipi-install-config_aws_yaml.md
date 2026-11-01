# Offline infrastructure template explanation: templates/openshift-ipi/install-config.aws.yaml

Source: [templates/openshift-ipi/install-config.aws.yaml](../templates/openshift-ipi/install-config.aws.yaml). These HCL/YAML settings have **no effect until an authorized provision/installer runs**. Review schema and provider compatibility with vendor documentation and obtain cost/change approval.

### 1. `apiVersion` = `v1`

**Source line:** 3. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `apiVersion` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 2. `baseDomain` = `example.com`

**Source line:** 4. **Meaning:** Approved DNS root for cluster and API/app names.

**Syntax:** key `baseDomain` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 3. `metadata` = ``

**Source line:** 5. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `metadata` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 4. `name` = `ocp-prod`

**Source line:** 6. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 5. `compute` = ``

**Source line:** 7. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `compute` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 6. List item `- name: worker`

**Meaning:** names a component in a YAML sequence, scoped by indentation. Confirm control-plane vs worker semantics before installing.

### 7. `replicas` = `3`

**Source line:** 9. **Meaning:** Number of instances; plan quorum/headroom.

**Syntax:** key `replicas` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 8. `controlPlane` = ``

**Source line:** 10. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `controlPlane` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 9. `name` = `master`

**Source line:** 11. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `name` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 10. `replicas` = `3`

**Source line:** 12. **Meaning:** Number of instances; plan quorum/headroom.

**Syntax:** key `replicas` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 11. `platform` = ``

**Source line:** 13. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `platform` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 12. `aws` = ``

**Source line:** 14. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `aws` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 13. `region` = `eu-central-1`

**Source line:** 15. **Meaning:** Cloud region in which resources are created.

**Syntax:** key `region` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 14. `networking` = ``

**Source line:** 18. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `networking` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 15. `networkType` = `OVNKubernetes`

**Source line:** 19. **Meaning:** Cluster CNI networking type for target OpenShift release.

**Syntax:** key `networkType` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 16. `clusterNetwork` = ``

**Source line:** 20. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `clusterNetwork` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 17. `hostPrefix` = `23`

**Source line:** 22. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `hostPrefix` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 18. `serviceNetwork` = ``

**Source line:** 23. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `serviceNetwork` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 19. `pullSecret` = `'REPLACE_WITH_VALID_REDHAT_PULL_SECRET_JSON'`

**Source line:** 25. **Meaning:** Sensitive Red Hat registry authentication; NEVER commit a real value.

**Syntax:** key `pullSecret` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 20. `sshKey` = `'ssh-ed25519 REPLACE_WITH_PUBLIC_KEY'`

**Source line:** 26. **Meaning:** Public administrative SSH key (not private key).

**Syntax:** key `sshKey` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 21. `publish` = `Internal`

**Source line:** 27. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `publish` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

