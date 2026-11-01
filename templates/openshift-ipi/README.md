# OpenShift IPI AWS / Azure / GCP — production deployment starters

**OpenShift != kubeadm:** its normal bootstrap/control-plane OS is **Red Hat Enterprise Linux CoreOS (RHCOS)**, installed with the official `openshift-install` provisioning workflow. **Do not run Ubuntu/Debian/RHEL kubeadm preparation scripts on OpenShift masters.**

These are **installer input examples**, NOT complete ready-to-run production cloud templates. Every example requires real cloud account, permissions, DNS, networking, SSH public key, valid Red Hat pull secret, version compatibility, subnet/egress design, encryption, support subscription and platform-specific mandatory inputs. The exact schema can differ by release; validate against your pinned OpenShift installer version.

## Standard workflow

1. Select release and install architecture (IPI, UPI or agent-based on supported platforms).
2. Prepare AWS/Azure/GCP IAM and billing, networking, DNS zone, quotas, private cluster access, registry egress/mirrors and approved CA.
3. Copy chosen example to a **protected, ignored** installer directory as `install-config.yaml`; populate all placeholders. **Never commit** secrets or generated `auth/kubeconfig`.
4. On an authorized workstation with matching `openshift-install` binary, validate assets and run:

```bash
mkdir -p "$HOME/ocp-installs/customer-prod"
chmod 700 "$HOME/ocp-installs/customer-prod"
# MANUALLY place reviewed install-config.yaml in directory; do not commit it to Git
openshift-install create manifests --dir="$HOME/ocp-installs/customer-prod"
openshift-install create cluster --dir="$HOME/ocp-installs/customer-prod" --log-level=info
export KUBECONFIG="$HOME/ocp-installs/customer-prod/auth/kubeconfig"
oc get clusteroperators
oc get clusterversion
oc get nodes -o wide
```

**IMPORTANT:** `create manifests` consumes `install-config.yaml`, so keep a **secure backup** before running it. Do not run `create cluster` without reviewed DNS/LB, customer cost approval and cluster configuration. The installer may create billable cloud resources.

## Bare metal or VMware vSphere

For a 3-control-plane + 3-worker agent-based **bare-metal example**, use [install-config.baremetal-agent.yaml](install-config.baremetal-agent.yaml) and [agent-config.baremetal.yaml](agent-config.baremetal.yaml). Replace every MAC, hostname, DHCP reservation, VIP, root disk, pull secret and public SSH key; the documentation-address IPs are deliberately not deployable. Run `openshift-install agent create image --dir=YOUR_PROTECTED_INSTALL_DIR` only with a reviewed supported installer release and both files in a secured directory; boot RHCOS agent ISO/PXE only after verifying the physical disks being overwritten.


Use supported **agent-based / assisted / IPI / UPI** installation with RHCOS and Ignition. You need approved physical server firmware, BMC/IPMI/Redfish where applicable, ISO/PXE, API+ingress VIPs, etcd-sized SSDs, DNS/NTP, machine networks, ingress LB and storage CSI. Do not assume AWS/Azure/GCP install-config works on bare metal.

## Enterprise production acceptance

- 3 control-plane nodes, >=3 application workers for common HA design; size from workloads and zone placement.
- Private API or tightly restricted public API, private networking, dedicated ingress/WAF, LBs and certificate lifecycle.
- Identity integration (OIDC/LDAP), RBAC/SCC, dedicated monitoring and logs/SIEM, backup OADP/etcd and tested DR.
- GitLab + OpenShift GitOps via Operator and protected promotion approval; container registry and image signing.
- Inventory cluster subscription, cost, support SLAs, upgrade channels and app/persistent-data owners.

**Rollbacks:** OpenShift version downgrades are not supported. For bad application releases revert GitOps; for failed cluster updates diagnose CVO/MCO and seek Red Hat support. See [upgrade guide](https://github.com/tbisla75/Open-Shift-Commands/blob/main/06-OPENSHIFT-CLUSTER-UPGRADE-RECOVERY.md).

Docs: [OpenShift installation overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/ocp-installation-overview).
