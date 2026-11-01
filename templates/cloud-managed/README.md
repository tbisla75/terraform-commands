# Managed Kubernetes Terraform starter templates: EKS / AKS / GKE

These templates are intended as **adaptable starting configurations** for enterprise environments with **pre-existing approved private networking, identity, remote Terraform state and cloud credentials**. They are **not turnkey production deployments**: egress/NAT, private DNS/API access, compliant ingress, WAF, backup, CSI storage classes, GitOps, policy, monitoring, cost guardrails, state backend and DR must be supplied or tested. Validate platform/provider/version support and quotas in the target region.

| Provider | Template | Required network/infrastructure |
|---|---|---|
| AWS | [aws-eks/main.tf](aws-eks/main.tf) | 2–3 private subnets in different AZs, VPC DNS, NAT or VPC endpoints, IAM/network review |
| Azure | [azure-aks/main.tf](azure-aks/main.tf) | Existing resource group, approved AKS subnet, private DNS and VNet access, Entra group |
| Google | [gcp-gke/main.tf](gcp-gke/main.tf) | Existing VPC, subnet with POD/SVC secondary ranges, Cloud NAT, DNS and regional quota |

## Example rollout (AWS)

```bash
cd templates/cloud-managed/aws-eks
cp terraform.tfvars.example terraform.tfvars
# Edit ALL placeholders and configure a secure remote state backend BEFORE applying.
terraform fmt -recursive
terraform init
terraform validate
terraform plan -out=tfplan
# CHANGE — only after peer review of the saved plan:
terraform apply tfplan
```

🔴 **Do not run from the public repo with real credentials or committed tfvars/state**. Provider APIs change and no live AWS/Azure/GCP deployment was executed to validate these templates. Validate using `terraform validate` with pinned providers and authorized cloud sandbox before customer use.

### Security considerations

- Private APIs (EKS and AKS examples); cloud client needs VPN, VNet connectivity or bastion.
- EKS: configure EBS CSI with Pod Identity/IRSA and appropriate IAM; managed addons, encrypted disks and node access policy; add EKS access entries/role mapping for operators.
- AKS: adjust node zone configuration to actual region, ensure cluster identity permissions on existing subnet and suitable private DNS configuration.
- GKE: example private nodes with public control endpoint; restrict master authorized networks / switch to private endpoint according to access design. **Do not expose administrative API without IP restrictions**, even though IAM still applies.
- Protect Terraform state in encrypted, locked, access-controlled backend; never commit it. Define `prevent_destroy`/deletion protection and DR restoration strategy as relevant.
- For production: policy/scanning and GitLab MR plan gate; apply only through protected approval, then bootstrap Argo CD and backup.

## OpenShift cloud installations

Do not replace the supported OpenShift Installer with arbitrary VM scripts. See [OpenShift IPI starters](../openshift-ipi/README.md). Cloud platform install config must be validated for selected OpenShift version, DNS and topology.

**Docs:** [AWS EKS](https://docs.aws.amazon.com/eks/), [Azure AKS](https://learn.microsoft.com/en-us/azure/aks/), [Google GKE](https://cloud.google.com/kubernetes-engine/docs).
