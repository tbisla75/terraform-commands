# Offline command / configuration reference: `templates/openshift-ipi/agent-config.baremetal.yaml`

Generated from repository source by `tools/build_offline_reference.py`. **1 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/openshift-ipi/agent-config.baremetal.yaml`](../templates/openshift-ipi/agent-config.baremetal.yaml)

### 1. Configuration example (yaml)

**Source line:** 1. **Purpose:** Define declarative settings, not a standalone CLI command. Review image references, identity, network addresses, permissions and secrets.

```yaml
# Agent-based OpenShift: all six hosts require unique discovered MACs and stable DNS/DHCP.
# Using DHCP makes customer DHCP reservations, default gateway, DNS and lease persistence mandatory.
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: ocp-prod
rendezvousIP: 192.0.2.21 # replace with reachable master-0 IP
hosts:
- hostname: master-0
  role: master
  interfaces:
  - name: eno1
    macAddress: "02:00:00:00:00:21"
  rootDeviceHints:
    deviceName: /dev/sda
- hostname: master-1
  role: master
  interfaces:
  - name: eno1
    macAddress: "02:00:00:00:00:22"
  rootDeviceHints:
    deviceName: /dev/sda
- hostname: master-2
  role: master
  interfaces:
  - name: eno1
    macAddress: "02:00:00:00:00:23"
  rootDeviceHints:
    deviceName: /dev/sda
- hostname: worker-0
  role: worker
  interfaces:
  - name: eno1
    macAddress: "02:00:00:00:00:24"
  rootDeviceHints:
    deviceName: /dev/sda
- hostname: worker-1
  role: worker
  interfaces:
  - name: eno1
    macAddress: "02:00:00:00:00:25"
  rootDeviceHints:
    deviceName: /dev/sda
- hostname: worker-2
  role: worker
  interfaces:
  - name: eno1
    macAddress: "02:00:00:00:00:26"
  rootDeviceHints:
    deviceName: /dev/sda
```

**Syntax:** YAML/HCL keys and indentation map to release-specific APIs. **Safety:** Applying may change live infrastructure; validate schema, diff and recovery first.

