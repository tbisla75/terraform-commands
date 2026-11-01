# Offline command / configuration reference: `templates/openshift-ipi/install-config.baremetal-agent.yaml`

Generated from repository source by `tools/build_offline_reference.py`. **1 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/openshift-ipi/install-config.baremetal-agent.yaml`](../templates/openshift-ipi/install-config.baremetal-agent.yaml)

### 1. Configuration example (yaml)

**Source line:** 1. **Purpose:** Define declarative settings, not a standalone CLI command. Review image references, identity, network addresses, permissions and secrets.

```yaml
# Agent-based bare-metal OpenShift install-config.yaml example; replace all placeholders.
# 3 master / 3 worker RHCOS hosts; DHCP example. Requires external DNS and approved VIPs.
apiVersion: v1
baseDomain: example.internal
metadata:
  name: ocp-prod
compute:
- name: worker
  replicas: 3
controlPlane:
  name: master
  replicas: 3
networking:
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: 192.0.2.0/24 # documentation-only; replace with actual routable customer CIDR
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  serviceNetwork:
  - 172.30.0.0/16
platform:
  baremetal:
    apiVIPs:
    - 192.0.2.10
    ingressVIPs:
    - 192.0.2.11
pullSecret: 'REPLACE_WITH_VALID_REDHAT_PULL_SECRET_JSON'
sshKey: 'ssh-ed25519 REPLACE_WITH_PUBLIC_KEY'
```

**Syntax:** YAML/HCL keys and indentation map to release-specific APIs. **Safety:** Applying may change live infrastructure; validate schema, diff and recovery first.

