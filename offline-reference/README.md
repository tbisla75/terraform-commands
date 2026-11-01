# Offline-first command reference — full local catalog

This directory is committed to Git and can be cloned, downloaded or printed for **offline** incident response. It is generated from the actual command examples and declarative templates in this repository; it does not rely on ChatGPT being available.

**Important:** An offline explanation is a helpful annotated starting point, not a guaranteed validated syntax for every release. Dynamic command flags should be verified using your installed CLI help/man pages and supported vendor procedures. Destructive changes require peer review.

**Indexed items:** 114 across 13 source files.

| Source | Offline explanations | Items |
|---|---|---:|
| `01-CLI-STATE-WORKSPACES.md` | [Open offline reference](01-CLI-STATE-WORKSPACES_md.md) | 23 |
| `02-ENTERPRISE-IAC-SECURITY.md` | [Open offline reference](02-ENTERPRISE-IAC-SECURITY_md.md) | 16 |
| `03-ADVANCED-TROUBLESHOOTING.md` | [Open offline reference](03-ADVANCED-TROUBLESHOOTING_md.md) | 15 |
| `05-GITLAB-TERRAFORM-PIPELINE.md` | [Open offline reference](05-GITLAB-TERRAFORM-PIPELINE_md.md) | 7 |
| `templates/cloud-managed/aws-eks/main.tf` | [Open offline reference](templates-cloud-managed-aws-eks-main_tf.md) | 21 |
| `templates/cloud-managed/azure-aks/main.tf` | [Open offline reference](templates-cloud-managed-azure-aks-main_tf.md) | 12 |
| `templates/cloud-managed/gcp-gke/main.tf` | [Open offline reference](templates-cloud-managed-gcp-gke-main_tf.md) | 14 |
| `templates/kubeadm-ha/kubeadm-config.yaml` | [Open offline reference](templates-kubeadm-ha-kubeadm-config_yaml.md) | 1 |
| `templates/openshift-ipi/agent-config.baremetal.yaml` | [Open offline reference](templates-openshift-ipi-agent-config_baremetal_yaml.md) | 1 |
| `templates/openshift-ipi/install-config.aws.yaml` | [Open offline reference](templates-openshift-ipi-install-config_aws_yaml.md) | 1 |
| `templates/openshift-ipi/install-config.azure.yaml` | [Open offline reference](templates-openshift-ipi-install-config_azure_yaml.md) | 1 |
| `templates/openshift-ipi/install-config.baremetal-agent.yaml` | [Open offline reference](templates-openshift-ipi-install-config_baremetal-agent_yaml.md) | 1 |
| `templates/openshift-ipi/install-config.gcp.yaml` | [Open offline reference](templates-openshift-ipi-install-config_gcp_yaml.md) | 1 |

## How to update locally

```bash
python3 tools/build_offline_reference.py
git diff -- offline-reference/
```

This generator does **not** infer new vendor commands, does **not** run shell commands, and does **not** grant access to systems. A scheduled vendor-watch workflow separately proposes release changes for review.
