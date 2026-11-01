# Terraform template syntax: offline explanation index

The original guide is a list of links to ChatGPT, not a shell command list. For **offline, field-by-field explanations**, use the following templates instead:

- [AWS EKS HCL fields](templates-cloud-managed-aws-eks-main_tf.md)
- [Azure AKS HCL fields](templates-cloud-managed-azure-aks-main_tf.md)
- [Google GKE HCL fields](templates-cloud-managed-gcp-gke-main_tf.md)
- [kubeadm HA Kubernetes YAML](templates-kubeadm-ha-kubeadm-config_yaml.md)
- [OpenShift AWS installer YAML](templates-openshift-ipi-install-config_aws_yaml.md)
- [OpenShift Azure installer YAML](templates-openshift-ipi-install-config_azure_yaml.md)
- [OpenShift GCP installer YAML](templates-openshift-ipi-install-config_gcp_yaml.md)
- [OpenShift bare-metal installer YAML](templates-openshift-ipi-install-config_baremetal-agent_yaml.md)
- [OpenShift bare-metal host/agent YAML](templates-openshift-ipi-agent-config_baremetal_yaml.md)

**What the fields mean:** Terraform `resource` blocks describe cloud objects, `variable` blocks accept site-specific inputs, and `output` blocks display results. OpenShift installer YAML declares control-plane/worker counts, host/network identity, DNS/VIPs and registry access; the host-specific agent file identifies actual NICs/disks. Incorrect values may create unexpected costs or overwrite physical disks, so validate the full configuration before installation.
