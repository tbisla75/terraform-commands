# Terraform / cluster template explained simply: templates/openshift-ipi/install-config.gcp.yaml

This document explains **each significant configuration key** without needing ChatGPT. Templates are starters: do not treat placeholders as a runnable production cluster. Exact field support depends on Terraform provider version or OpenShift/kubeadm version. Original: [templates/openshift-ipi/install-config.gcp.yaml](../templates/openshift-ipi/install-config.gcp.yaml).

## 1. `apiVersion` = `v1`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `apiVersion` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 2. `baseDomain` = `example.com`

**What it means:** Parent DNS domain for OpenShift API and application DNS names.

**Syntax:** `baseDomain` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 3. `metadata`

**What it means:** A group of identity/label settings for the cluster.

**Syntax:** `metadata` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 4. `name` = `ocp-prod`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 5. `compute`

**What it means:** Worker machines running application workloads.

**Syntax:** `compute` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 6. `name` = `worker`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 7. `replicas` = `3`

**What it means:** Number of instances of this role, important for HA and capacity.

**Syntax:** `replicas` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 8. `controlPlane`

**What it means:** Master/control-plane machines running the Kubernetes API and etcd.

**Syntax:** `controlPlane` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 9. `name` = `master`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 10. `replicas` = `3`

**What it means:** Number of instances of this role, important for HA and capacity.

**Syntax:** `replicas` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 11. `platform`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `platform` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 12. `gcp`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `gcp` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 13. `projectID` = `REPLACE_WITH_GCP_PROJECT_ID`

**What it means:** The Google Cloud project that owns the cluster and billing.

**Syntax:** `projectID` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 14. `region` = `europe-west1`

**What it means:** Selected cloud region.

**Syntax:** `region` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 15. `networking`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `networking` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 16. `networkType` = `OVNKubernetes`

**What it means:** Cluster networking plugin; OpenShift typically uses OVNKubernetes.

**Syntax:** `networkType` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 17. `clusterNetwork`

**What it means:** Pod overlay network: must not overlap surrounding network ranges.

**Syntax:** `clusterNetwork` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 18. `cidr` = `10.128.0.0/14`

**What it means:** IP address range in CIDR notation; verify no overlap with VPC/VNet/onsite networks.

**Syntax:** `cidr` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 19. `hostPrefix` = `23`

**What it means:** How many bits define per-node Pod subnets; affects maximum nodes/IPs.

**Syntax:** `hostPrefix` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 20. `serviceNetwork`

**What it means:** IP range for internal Kubernetes Services, not ordinary host addresses.

**Syntax:** `serviceNetwork` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 21. `pullSecret` = `'REPLACE_WITH_VALID_REDHAT_PULL_SECRET_JSON'`

**What it means:** Sensitive Red Hat registry credentials. Never commit a real pull secret.

**Syntax:** `pullSecret` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Never put real private credentials in Git.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 22. `sshKey` = `'ssh-ed25519 REPLACE_WITH_PUBLIC_KEY'`

**What it means:** Public SSH access key for authorized administrators. This must not be a private key.

**Syntax:** `sshKey` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Never put real private credentials in Git.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 23. `publish` = `Internal`

**What it means:** Controls whether cluster endpoints are internal/private or externally published (supported platforms may vary).

**Syntax:** `publish` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

