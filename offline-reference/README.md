# Offline command reference: Terraform infrastructure as code and cluster provisioning

**This directory is self-contained**. Download the GitHub repo as ZIP or clone it before travel; links to local Markdown below work without internet. Every listed example has an offline description of purpose, syntax, options, expected behavior and operational risk; confirm version-specific flags with the actual installed CLI/vendor documentation.

| Original runbook/template | Offline explanation |
|---|---|
| [01-CLI-STATE-WORKSPACES.md](../01-CLI-STATE-WORKSPACES.md) | [Offline explanation](01-CLI-STATE-WORKSPACES_md.md) |
| [02-ENTERPRISE-IAC-SECURITY.md](../02-ENTERPRISE-IAC-SECURITY.md) | [Offline explanation](02-ENTERPRISE-IAC-SECURITY_md.md) |
| [03-ADVANCED-TROUBLESHOOTING.md](../03-ADVANCED-TROUBLESHOOTING.md) | [Offline explanation](03-ADVANCED-TROUBLESHOOTING_md.md) |
| [04-CLOUD-PROVISIONING-CHECKLIST.md](../04-CLOUD-PROVISIONING-CHECKLIST.md) | [Offline explanation](04-CLOUD-PROVISIONING-CHECKLIST_md.md) |
| [05-GITLAB-TERRAFORM-PIPELINE.md](../05-GITLAB-TERRAFORM-PIPELINE.md) | [Offline explanation](05-GITLAB-TERRAFORM-PIPELINE_md.md) |
| [06-TERRAFORM-AND-TEMPLATE-SYNTAX-CHATGPT.md](../06-TERRAFORM-AND-TEMPLATE-SYNTAX-CHATGPT.md) | [Offline explanation](06-TERRAFORM-AND-TEMPLATE-SYNTAX-CHATGPT_md.md) |
| [templates/cloud-managed/aws-eks/main.tf](../templates/cloud-managed/aws-eks/main.tf) | [Offline explanation](templates-cloud-managed-aws-eks-main_tf.md) |
| [templates/cloud-managed/azure-aks/main.tf](../templates/cloud-managed/azure-aks/main.tf) | [Offline explanation](templates-cloud-managed-azure-aks-main_tf.md) |
| [templates/cloud-managed/gcp-gke/main.tf](../templates/cloud-managed/gcp-gke/main.tf) | [Offline explanation](templates-cloud-managed-gcp-gke-main_tf.md) |
| [templates/kubeadm-ha/kubeadm-config.yaml](../templates/kubeadm-ha/kubeadm-config.yaml) | [Offline explanation](templates-kubeadm-ha-kubeadm-config_yaml.md) |
| [templates/openshift-ipi/install-config.aws.yaml](../templates/openshift-ipi/install-config.aws.yaml) | [Offline explanation](templates-openshift-ipi-install-config_aws_yaml.md) |
| [templates/openshift-ipi/install-config.azure.yaml](../templates/openshift-ipi/install-config.azure.yaml) | [Offline explanation](templates-openshift-ipi-install-config_azure_yaml.md) |
| [templates/openshift-ipi/install-config.gcp.yaml](../templates/openshift-ipi/install-config.gcp.yaml) | [Offline explanation](templates-openshift-ipi-install-config_gcp_yaml.md) |
| [templates/openshift-ipi/install-config.baremetal-agent.yaml](../templates/openshift-ipi/install-config.baremetal-agent.yaml) | [Offline explanation](templates-openshift-ipi-install-config_baremetal-agent_yaml.md) |
| [templates/openshift-ipi/agent-config.baremetal.yaml](../templates/openshift-ipi/agent-config.baremetal.yaml) | [Offline explanation](templates-openshift-ipi-agent-config_baremetal_yaml.md) |

## Local refresh and vendor changes

```bash
python3 tools/build_offline_reference.py
python3 tools/vendor_watch.py
```

**Local build** reads repository files without internet. The **vendor check requires internet** and updates only the vendor-watch review records; it does not silently replace production commands. The scheduled GitHub Action opens a review PR if authorized. See [vendor change dashboard](../vendor-watch/README.md).
