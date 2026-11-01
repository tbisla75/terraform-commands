# Cloud and bare-metal cluster infrastructure: AWS, Azure, GCP, vSphere, physical

| Deployment | Recommended Kubernetes path | OpenShift path | Dependencies |
|---|---|---|---|
| AWS | EKS managed Kubernetes; kubeadm self-managed only if required | Supported AWS IPI/UPI OpenShift | VPC, private subnets, NAT/egress, IAM, EBS CSI, Route53, LB |
| Azure | AKS managed Kubernetes | Supported Azure IPI/UPI OpenShift | VNet, private subnet, Entra ID, DNS private zones, Azure Disk CSI, LB |
| Google Cloud | GKE managed Kubernetes | Supported GCP IPI/UPI OpenShift | VPC, Cloud NAT, Cloud DNS, IAM/workload identity, PD CSI |
| VMware vSphere | kubeadm VMs or platform-specific distro | OpenShift IPI/UPI/agent-based, RHCOS | vCenter, datastores, portgroups, DNS, AVI/F5/HAProxy LB, CSI |
| Bare metal | kubeadm or K3s Linux nodes with external LB | RHCOS IPI/UPI/agent-based installer | BMC, PXE/ISO, DNS/NTP, redundant switches, enterprise storage |

**Production guardrails:** network segmentation, encrypted backups, cloud logs and audit, quotas/alerts, N+1 worker resources, multi-zone/host spread, load balancer redundancy, OIDC and MFA, CSI/PV backups, Pod Security/SCC, upgrade strategy and failure drills.

**Terraform advice:** Terraform provision cloud *infrastructure*, IAM, subnets and managed EKS/AKS/GKE resources; cluster bootstrap (kubeadm) and OpenShift IPI often involve installer-driven imperative steps and should not be replaced by unsafe `remote-exec` commands in production. Use version-pinned, reviewed modules and a GitLab pipeline with protected plans and manual apply.

Refs: [EKS docs](https://docs.aws.amazon.com/eks/), [AKS docs](https://learn.microsoft.com/en-us/azure/aks/), [GKE docs](https://cloud.google.com/kubernetes-engine/docs), [OpenShift installation](https://docs.redhat.com/en/documentation/openshift_container_platform/).
