# Terraform and cluster IaC templates explained simply

**Start here when ChatGPT or the internet is unavailable.** These are practical, plain-English explanations of the actual commands in the corresponding repository. Every entry includes the exact original command, what it does on that platform, syntax and switches, what you should see, common failures and whether it can affect production. Templates are explained field-by-field. Original technical runbooks and [advanced offline annotations](../offline-reference/README.md) remain available.

**Safety:** generic commands and example values are not automatically safe for every product version, OS or customer. Verify selected host/context, rights and vendor release. A broad command or tool-specific option may need local `--help` verification. Never upload real credentials or customer data to ChatGPT.

| Subject | Plain-English guide | Original runbook |
|---|---|---|
| `01-CLI-STATE-WORKSPACES.md` | [Simple explanation](01-CLI-STATE-WORKSPACES_md.md) | [Original](../01-CLI-STATE-WORKSPACES.md) |
| `02-ENTERPRISE-IAC-SECURITY.md` | [Simple explanation](02-ENTERPRISE-IAC-SECURITY_md.md) | [Original](../02-ENTERPRISE-IAC-SECURITY.md) |
| `03-ADVANCED-TROUBLESHOOTING.md` | [Simple explanation](03-ADVANCED-TROUBLESHOOTING_md.md) | [Original](../03-ADVANCED-TROUBLESHOOTING.md) |
| `04-CLOUD-PROVISIONING-CHECKLIST.md` | [Simple explanation](04-CLOUD-PROVISIONING-CHECKLIST_md.md) | [Original](../04-CLOUD-PROVISIONING-CHECKLIST.md) |
| `05-GITLAB-TERRAFORM-PIPELINE.md` | [Simple explanation](05-GITLAB-TERRAFORM-PIPELINE_md.md) | [Original](../05-GITLAB-TERRAFORM-PIPELINE.md) |
| `06-TERRAFORM-AND-TEMPLATE-SYNTAX-CHATGPT.md` | [Simple explanation](06-TERRAFORM-AND-TEMPLATE-SYNTAX-CHATGPT_md.md) | [Original](../06-TERRAFORM-AND-TEMPLATE-SYNTAX-CHATGPT.md) |
| `templates/cloud-managed/aws-eks/main.tf` | [Simple explanation](templates-cloud-managed-aws-eks-main_tf.md) | [Original](../templates/cloud-managed/aws-eks/main.tf) |
| `templates/cloud-managed/azure-aks/main.tf` | [Simple explanation](templates-cloud-managed-azure-aks-main_tf.md) | [Original](../templates/cloud-managed/azure-aks/main.tf) |
| `templates/cloud-managed/gcp-gke/main.tf` | [Simple explanation](templates-cloud-managed-gcp-gke-main_tf.md) | [Original](../templates/cloud-managed/gcp-gke/main.tf) |
| `templates/kubeadm-ha/kubeadm-config.yaml` | [Simple explanation](templates-kubeadm-ha-kubeadm-config_yaml.md) | [Original](../templates/kubeadm-ha/kubeadm-config.yaml) |
| `templates/openshift-ipi/install-config.aws.yaml` | [Simple explanation](templates-openshift-ipi-install-config_aws_yaml.md) | [Original](../templates/openshift-ipi/install-config.aws.yaml) |
| `templates/openshift-ipi/install-config.azure.yaml` | [Simple explanation](templates-openshift-ipi-install-config_azure_yaml.md) | [Original](../templates/openshift-ipi/install-config.azure.yaml) |
| `templates/openshift-ipi/install-config.gcp.yaml` | [Simple explanation](templates-openshift-ipi-install-config_gcp_yaml.md) | [Original](../templates/openshift-ipi/install-config.gcp.yaml) |
| `templates/openshift-ipi/install-config.baremetal-agent.yaml` | [Simple explanation](templates-openshift-ipi-install-config_baremetal-agent_yaml.md) | [Original](../templates/openshift-ipi/install-config.baremetal-agent.yaml) |
| `templates/openshift-ipi/agent-config.baremetal.yaml` | [Simple explanation](templates-openshift-ipi-agent-config_baremetal_yaml.md) | [Original](../templates/openshift-ipi/agent-config.baremetal.yaml) |

## What is in each explanation?

1. **What it does:** in everyday English, including the specific platform effect.
2. **How to read it:** tool, action, flags, target names, shell operators and example placeholders.
3. **What you should see:** successful response and the sort of failure to investigate.
4. **Can it change production?** privileged actions, credentials, blast radius and safe checks.
5. **Where to look next:** the original, more technical runbook and the installed CLI's help.

### Updates and review

The existing [weekly vendor tracker](../vendor-watch/README.md) detects vendor release/documentation changes but **does not automatically rewrite these explanations**. When a vendor changes CLI behavior, update both the source runbook and this simple explanation after verifying release notes/lab results; otherwise the old explanation can be stale. The original [offline generator](../tools/build_offline_reference.py) maintains `offline-reference/`, not this curated `offline-simple/` copy.
