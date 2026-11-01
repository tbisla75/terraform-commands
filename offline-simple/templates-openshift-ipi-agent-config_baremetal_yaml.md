# Terraform / cluster template explained simply: templates/openshift-ipi/agent-config.baremetal.yaml

This document explains **each significant configuration key** without needing ChatGPT. Templates are starters: do not treat placeholders as a runnable production cluster. Exact field support depends on Terraform provider version or OpenShift/kubeadm version. Original: [templates/openshift-ipi/agent-config.baremetal.yaml](../templates/openshift-ipi/agent-config.baremetal.yaml).

## 1. `apiVersion` = `v1beta1`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `apiVersion` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 2. `kind` = `AgentConfig`

**What it means:** Sets the named property in its parent cloud resource, node pool or installer object. The exact meaning depends on the parent block and vendor/provider release.

**Syntax:** `kind` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

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

## 5. `rendezvousIP` = `192.0.2.21 # replace with reachable master-0 IP`

**What it means:** Agent-based OpenShift bootstrap host/IP where cluster agents contact each other.

**Syntax:** `rendezvousIP` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 6. `hosts`

**What it means:** List of physical servers or VM hosts being discovered/configured.

**Syntax:** `hosts` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 7. `hostname` = `master-0`

**What it means:** The unique Linux hostname of the target machine.

**Syntax:** `hostname` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 8. `role` = `master`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 9. `interfaces`

**What it means:** Network interface entries per host.

**Syntax:** `interfaces` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 10. `name` = `eno1`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 11. `macAddress` = `"02:00:00:00:00:21"`

**What it means:** Physical NIC hardware address; the installer uses it to identify the correct machine.

**Syntax:** `macAddress` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 12. `rootDeviceHints`

**What it means:** Rules for choosing which disk to install the OS on. **Wrong value can erase the wrong disk.**

**Syntax:** `rootDeviceHints` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 13. `deviceName` = `/dev/sda`

**What it means:** Selected device such as `/dev/sda`; verify real serial/path before installing.

**Syntax:** `deviceName` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 14. `hostname` = `master-1`

**What it means:** The unique Linux hostname of the target machine.

**Syntax:** `hostname` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 15. `role` = `master`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 16. `interfaces`

**What it means:** Network interface entries per host.

**Syntax:** `interfaces` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 17. `name` = `eno1`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 18. `macAddress` = `"02:00:00:00:00:22"`

**What it means:** Physical NIC hardware address; the installer uses it to identify the correct machine.

**Syntax:** `macAddress` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 19. `rootDeviceHints`

**What it means:** Rules for choosing which disk to install the OS on. **Wrong value can erase the wrong disk.**

**Syntax:** `rootDeviceHints` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 20. `deviceName` = `/dev/sda`

**What it means:** Selected device such as `/dev/sda`; verify real serial/path before installing.

**Syntax:** `deviceName` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 21. `hostname` = `master-2`

**What it means:** The unique Linux hostname of the target machine.

**Syntax:** `hostname` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 22. `role` = `master`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 23. `interfaces`

**What it means:** Network interface entries per host.

**Syntax:** `interfaces` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 24. `name` = `eno1`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 25. `macAddress` = `"02:00:00:00:00:23"`

**What it means:** Physical NIC hardware address; the installer uses it to identify the correct machine.

**Syntax:** `macAddress` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 26. `rootDeviceHints`

**What it means:** Rules for choosing which disk to install the OS on. **Wrong value can erase the wrong disk.**

**Syntax:** `rootDeviceHints` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 27. `deviceName` = `/dev/sda`

**What it means:** Selected device such as `/dev/sda`; verify real serial/path before installing.

**Syntax:** `deviceName` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 28. `hostname` = `worker-0`

**What it means:** The unique Linux hostname of the target machine.

**Syntax:** `hostname` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 29. `role` = `worker`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 30. `interfaces`

**What it means:** Network interface entries per host.

**Syntax:** `interfaces` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 31. `name` = `eno1`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 32. `macAddress` = `"02:00:00:00:00:24"`

**What it means:** Physical NIC hardware address; the installer uses it to identify the correct machine.

**Syntax:** `macAddress` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 33. `rootDeviceHints`

**What it means:** Rules for choosing which disk to install the OS on. **Wrong value can erase the wrong disk.**

**Syntax:** `rootDeviceHints` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 34. `deviceName` = `/dev/sda`

**What it means:** Selected device such as `/dev/sda`; verify real serial/path before installing.

**Syntax:** `deviceName` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 35. `hostname` = `worker-1`

**What it means:** The unique Linux hostname of the target machine.

**Syntax:** `hostname` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 36. `role` = `worker`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 37. `interfaces`

**What it means:** Network interface entries per host.

**Syntax:** `interfaces` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 38. `name` = `eno1`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 39. `macAddress` = `"02:00:00:00:00:25"`

**What it means:** Physical NIC hardware address; the installer uses it to identify the correct machine.

**Syntax:** `macAddress` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 40. `rootDeviceHints`

**What it means:** Rules for choosing which disk to install the OS on. **Wrong value can erase the wrong disk.**

**Syntax:** `rootDeviceHints` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 41. `deviceName` = `/dev/sda`

**What it means:** Selected device such as `/dev/sda`; verify real serial/path before installing.

**Syntax:** `deviceName` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 42. `hostname` = `worker-2`

**What it means:** The unique Linux hostname of the target machine.

**Syntax:** `hostname` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 43. `role` = `worker`

**What it means:** Which machine is master/control plane or worker.

**Syntax:** `role` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 44. `interfaces`

**What it means:** Network interface entries per host.

**Syntax:** `interfaces` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 45. `name` = `eno1`

**What it means:** Name of this particular resource, machine, node group or installer section.

**Syntax:** `name` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. A change can replace or alter infrastructure when the plan/installer is executed.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 46. `macAddress` = `"02:00:00:00:00:26"`

**What it means:** Physical NIC hardware address; the installer uses it to identify the correct machine.

**Syntax:** `macAddress` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 47. `rootDeviceHints`

**What it means:** Rules for choosing which disk to install the OS on. **Wrong value can erase the wrong disk.**

**Syntax:** `rootDeviceHints` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

## 48. `deviceName` = `/dev/sda`

**What it means:** Selected device such as `/dev/sda`; verify real serial/path before installing.

**Syntax:** `deviceName` is the field name; `:` starts a YAML value. Indentation and `-` determine whether it belongs to a map or list.

**Before you use it:** Confirm the actual customer values, CIDRs, regions, storage and API support. Hardware identity and target-disk mistakes can prevent installation or erase the wrong drive.

**How to validate:** Check schema with the matching kubeadm/OpenShift installer release; confirm DNS/network/host identities before installation.

