# Offline infrastructure template explanation: templates/kubeadm-ha/kubeadm-config.yaml

Source: [templates/kubeadm-ha/kubeadm-config.yaml](../templates/kubeadm-ha/kubeadm-config.yaml). These HCL/YAML settings have **no effect until an authorized provision/installer runs**. Review schema and provider compatibility with vendor documentation and obtain cost/change approval.

### 1. `apiVersion` = `kubeadm.k8s.io/v1beta4`

**Source line:** 3. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `apiVersion` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 2. `kind` = `InitConfiguration`

**Source line:** 4. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `kind` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 3. `nodeRegistration` = ``

**Source line:** 5. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `nodeRegistration` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 4. `criSocket` = `unix:///run/containerd/containerd.sock`

**Source line:** 6. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `criSocket` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 5. `apiVersion` = `kubeadm.k8s.io/v1beta4`

**Source line:** 8. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `apiVersion` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 6. `kind` = `ClusterConfiguration`

**Source line:** 9. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `kind` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 7. `kubernetesVersion` = `v1.37.0 # choose an actually published supported patch and test version skew`

**Source line:** 10. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `kubernetesVersion` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 8. `controlPlaneEndpoint` = `"k8s-api.example.internal:6443"`

**Source line:** 11. **Meaning:** Stable HA API endpoint resolved to external control-plane load balancer.

**Syntax:** key `controlPlaneEndpoint` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 9. `clusterName` = `enterprise-k8s`

**Source line:** 12. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `clusterName` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 10. `networking` = ``

**Source line:** 13. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `networking` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 11. `podSubnet` = `"10.244.0.0/16" # must match selected CNI`

**Source line:** 14. **Meaning:** CIDR used for pods; must match CNI and not overlap networks.

**Syntax:** key `podSubnet` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 12. `serviceSubnet` = `"10.96.0.0/12"`

**Source line:** 15. **Meaning:** Service VIP range; must not overlap pods/on-prem.

**Syntax:** key `serviceSubnet` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 13. `dnsDomain` = `"cluster.local"`

**Source line:** 16. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `dnsDomain` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 14. `apiServer` = ``

**Source line:** 17. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `apiServer` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 15. `certSANs` = ``

**Source line:** 18. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `certSANs` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 16. `controllerManager` = `{}`

**Source line:** 21. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `controllerManager` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 17. `scheduler` = `{}`

**Source line:** 22. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `scheduler` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 18. `apiVersion` = `kubelet.config.k8s.io/v1beta1`

**Source line:** 24. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `apiVersion` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 19. `kind` = `KubeletConfiguration`

**Source line:** 25. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `kind` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

### 20. `cgroupDriver` = `systemd`

**Source line:** 26. **Meaning:** Configures the field in its parent Terraform resource or Kubernetes/OpenShift installer object; its meaning depends on parent block and installed schema.

**Syntax:** key `cgroupDriver` is assigned a typed HCL expression or YAML scalar/list item; nested indentation and blocks determine scope. **Expected effect:** changes the declared desired state only. **Before applying:** confirm that this is supported by the chosen release and does not expose credentials or replace/destroy resources.

