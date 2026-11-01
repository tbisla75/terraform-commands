# AWS, Azure, GCP and bare-metal provisioning — explained simply

This is a **conceptual deployment checklist**, not a file containing CLI code blocks. It explains which platform to choose and what must exist before you can safely deploy a cluster. For individual Terraform fields, see the [Terraform simple reference index](README.md).

| Platform | What Terraform usually provisions | What you still need to verify |
|---|---|---|
| AWS EKS | Managed Kubernetes control plane, EC2 node group, IAM | VPC private subnets, DNS, NAT, load balancers, EBS CSI, backups |
| Azure AKS | Managed control plane, VM node pools, Azure identities | VNet, NSGs, private DNS, Entra permissions, disk CSI |
| Google GKE | Managed control plane, node pools, cloud IAM | VPC, subnet secondary ranges, NAT, workload identity, authorized API CIDRs |
| kubeadm on VMs/bare metal | OS VMs/physical hosts, load balancer and networking | Manual kubeadm init/join, CNI, CSI, etcd HA, backup and worker lifecycle |
| OpenShift | Underlying cloud infrastructure plus supported installer workflow | RHCOS, DNS/VIPs, Red Hat pull secret, SCCs, Operators, OADP/etcd backups |

**Key distinction:** Terraform infrastructure `apply` does not automatically make the resulting system production-ready. Monitor, validate quotas, test recovery, and get customer approval for any real cloud changes.
