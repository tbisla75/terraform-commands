# Terraform / cluster template explained simply: templates/kubeadm-ha/kubeadm-config.yaml

This document explains **each significant configuration key** without needing ChatGPT. Templates are starters: do not treat placeholders as a runnable production cluster. Exact field support depends on Terraform provider version or OpenShift/kubeadm version. Original: [templates/kubeadm-ha/kubeadm-config.yaml](../templates/kubeadm-ha/kubeadm-config.yaml).

## 1. `apiVersion` = `kubeadm.k8s.io/v1beta4`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `apiVersion` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 2. `kind` = `InitConfiguration`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `kind` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 3. `nodeRegistration`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `nodeRegistration` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 4. `criSocket` = `unix:///run/containerd/containerd.sock`

**What it means:** Path to containerd's CRI socket so kubeadm contacts the right runtime.

**Syntax:** `criSocket` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 5. `apiVersion` = `kubeadm.k8s.io/v1beta4`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `apiVersion` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 6. `kind` = `ClusterConfiguration`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `kind` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 7. `kubernetesVersion` = `v1.37.0 # choose an actually published supported patch and test version ske`

**What it means:** Control plane Kubernetes version for kubeadm; choose a real supported patch release.

**Syntax:** `kubernetesVersion` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 8. `controlPlaneEndpoint` = `"k8s-api.example.internal:6443"`

**What it means:** Stable TCP API load balancer DNS:6443 used by every kubeadm node.

**Syntax:** `controlPlaneEndpoint` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 9. `clusterName` = `enterprise-k8s`

**What it means:** Kubernetes cluster identifier.

**Syntax:** `clusterName` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 10. `networking`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `networking` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 11. `podSubnet` = `"10.244.0.0/16" # must match selected CNI`

**What it means:** Kubernetes Pod subnet; match CNI and avoid overlapping external networks.

**Syntax:** `podSubnet` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 12. `serviceSubnet` = `"10.96.0.0/12"`

**What it means:** Kubernetes Service subnet; should not overlap pods, hosts or on-prem routes.

**Syntax:** `serviceSubnet` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 13. `dnsDomain` = `"cluster.local"`

**What it means:** Internal Kubernetes DNS suffix.

**Syntax:** `dnsDomain` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 14. `apiServer`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `apiServer` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 15. `certSANs`

**What it means:** Names/IP addresses written into the API server certificate; include the LB hostname/VIP.

**Syntax:** `certSANs` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 16. `controllerManager` = `{}`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `controllerManager` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 17. `scheduler` = `{}`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `scheduler` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 18. `apiVersion` = `kubelet.config.k8s.io/v1beta1`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `apiVersion` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 19. `kind` = `KubeletConfiguration`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `kind` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 20. `cgroupDriver` = `systemd`

**What it means:** Which Linux cgroup mode kubelet uses; should match container runtime.

**Syntax:** `cgroupDriver` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

