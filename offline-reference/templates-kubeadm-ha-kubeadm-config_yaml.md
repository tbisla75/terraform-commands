# Offline command / configuration reference: `templates/kubeadm-ha/kubeadm-config.yaml`

Generated from repository source by `tools/build_offline_reference.py`. **20 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/kubeadm-ha/kubeadm-config.yaml`](../templates/kubeadm-ha/kubeadm-config.yaml)

### 1. Configuration field apiVersion

**Source line:** 3. **Language:** yaml. **Full syntax:** apiVersion = kubeadm.k8s.io/v1beta4

**What it does:** API/schema version of the Kubernetes/OpenShift resource or installer config.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 2. Configuration field kind

**Source line:** 4. **Language:** yaml. **Full syntax:** kind = InitConfiguration

**What it does:** The resource type handled by the target API.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 3. Configuration field nodeRegistration

**Source line:** 5. **Language:** yaml. **Full syntax:** nodeRegistration = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 4. Configuration field criSocket

**Source line:** 6. **Language:** yaml. **Full syntax:** criSocket = unix:///run/containerd/containerd.sock

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 5. Configuration field apiVersion

**Source line:** 8. **Language:** yaml. **Full syntax:** apiVersion = kubeadm.k8s.io/v1beta4

**What it does:** API/schema version of the Kubernetes/OpenShift resource or installer config.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 6. Configuration field kind

**Source line:** 9. **Language:** yaml. **Full syntax:** kind = ClusterConfiguration

**What it does:** The resource type handled by the target API.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 7. Configuration field kubernetesVersion

**Source line:** 10. **Language:** yaml. **Full syntax:** kubernetesVersion = v1.37.0 # choose an actually published supported patch and test version skew

**What it does:** Requested kubeadm cluster version.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 8. Configuration field controlPlaneEndpoint

**Source line:** 11. **Language:** yaml. **Full syntax:** controlPlaneEndpoint = "k8s-api.example.internal:6443"

**What it does:** Stable HA load balancer endpoint for Kubernetes API.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 9. Configuration field clusterName

**Source line:** 12. **Language:** yaml. **Full syntax:** clusterName = enterprise-k8s

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 10. Configuration field networking

**Source line:** 13. **Language:** yaml. **Full syntax:** networking = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 11. Configuration field podSubnet

**Source line:** 14. **Language:** yaml. **Full syntax:** podSubnet = "10.244.0.0/16" # must match selected CNI

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 12. Configuration field serviceSubnet

**Source line:** 15. **Language:** yaml. **Full syntax:** serviceSubnet = "10.96.0.0/12"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 13. Configuration field dnsDomain

**Source line:** 16. **Language:** yaml. **Full syntax:** dnsDomain = "cluster.local"

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 14. Configuration field apiServer

**Source line:** 17. **Language:** yaml. **Full syntax:** apiServer = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 15. Configuration field certSANs

**Source line:** 18. **Language:** yaml. **Full syntax:** certSANs = 

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 16. Configuration field controllerManager

**Source line:** 21. **Language:** yaml. **Full syntax:** controllerManager = {}

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 17. Configuration field scheduler

**Source line:** 22. **Language:** yaml. **Full syntax:** scheduler = {}

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 18. Configuration field apiVersion

**Source line:** 24. **Language:** yaml. **Full syntax:** apiVersion = kubelet.config.k8s.io/v1beta1

**What it does:** API/schema version of the Kubernetes/OpenShift resource or installer config.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 19. Configuration field kind

**Source line:** 25. **Language:** yaml. **Full syntax:** kind = KubeletConfiguration

**What it does:** The resource type handled by the target API.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

### 20. Configuration field cgroupDriver

**Source line:** 26. **Language:** yaml. **Full syntax:** cgroupDriver = systemd

**What it does:** A versioned configuration argument in its enclosing resource/block. Confirm exact type, default, scope and supported values from the installed provider or API schema.

**Expected effect:** Declarative value is only interpreted when the relevant tool applies, installs, builds or reconciles this configuration. **Safety:** Inspect enclosing object, secrets, permissions and lifecycle; validate schema and a test plan/dry-run before production. Do not assume this syntax exists on older releases.

