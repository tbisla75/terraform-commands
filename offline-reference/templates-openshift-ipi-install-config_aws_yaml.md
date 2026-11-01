# Offline command / configuration reference: `templates/openshift-ipi/install-config.aws.yaml`

Generated from repository source by `tools/build_offline_reference.py`. **1 items**. This copy works offline. No commands were executed.

⚠️ **Version-aware reference, not a substitute for vendor docs.** Every individual command is preserved with purpose, flags, placeholders, expected output and risk. Ambiguous flags are marked as command-specific. Always verify flags against your installed CLI.

**Original file:** [`templates/openshift-ipi/install-config.aws.yaml`](../templates/openshift-ipi/install-config.aws.yaml)

### 1. Configuration example (yaml)

**Source line:** 1. **Purpose:** Define declarative settings, not a standalone CLI command. Review image references, identity, network addresses, permissions and secrets.

```yaml
# OpenShift installer input template for AWS. Use selected supported OpenShift 4.x installer.
# Rename to install-config.yaml inside a new protected install directory. Never commit real pullSecret/SSH keys.
apiVersion: v1
baseDomain: example.com
metadata:
  name: ocp-prod
compute:
- name: worker
  replicas: 3
controlPlane:
  name: master
  replicas: 3
platform:
  aws:
    region: eu-central-1
    # Use platform version supported private networking/network selection;
    # installer will create infrastructure unless supplying existing VPC/subnets.
networking:
  networkType: OVNKubernetes
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  serviceNetwork:
  - 172.30.0.0/16
pullSecret: 'REPLACE_WITH_VALID_REDHAT_PULL_SECRET_JSON'
sshKey: 'ssh-ed25519 REPLACE_WITH_PUBLIC_KEY'
publish: Internal
```

**Syntax:** YAML/HCL keys and indentation map to release-specific APIs. **Safety:** Applying may change live infrastructure; validate schema, diff and recovery first.

