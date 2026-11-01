# Offline command / configuration reference: `templates/kubeadm-ha/kubeadm-config.yaml`

Generated from repository source by `tools/build_offline_reference.py`. **1 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/kubeadm-ha/kubeadm-config.yaml`](../templates/kubeadm-ha/kubeadm-config.yaml)

### 1. Configuration example (yaml)

**Source line:** 1. **Purpose:** Define declarative settings, not a standalone CLI command. Review image references, identity, network addresses, permissions and secrets.

```yaml
# Example cluster config for FIRST control-plane node; adjust IP/DNS, version, pod/service CIDRs,
# and external LB before use. Not an installer. A separate approved CNI and CSI are REQUIRED.
apiVersion: kubeadm.k8s.io/v1beta4
kind: InitConfiguration
nodeRegistration:
  criSocket: unix:///run/containerd/containerd.sock
---
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.37.0 # choose an actually published supported patch and test version skew
controlPlaneEndpoint: "k8s-api.example.internal:6443"
clusterName: enterprise-k8s
networking:
  podSubnet: "10.244.0.0/16" # must match selected CNI
  serviceSubnet: "10.96.0.0/12"
  dnsDomain: "cluster.local"
apiServer:
  certSANs:
    - k8s-api.example.internal
    - 10.10.10.100
controllerManager: {}
scheduler: {}
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
cgroupDriver: systemd
```

**Syntax:** YAML/HCL keys and indentation map to release-specific APIs. **Safety:** Applying may change live infrastructure; validate schema, diff and recovery first.

