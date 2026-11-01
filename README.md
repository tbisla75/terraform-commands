# Terraform Commands — Enterprise IaC and Cluster Deployment Templates

## Start here — plain-English explanations (offline)

**[Open the simplified command-by-command guide](offline-simple/README.md).** Every command is shown with a practical explanation of what it does on this platform, why you would run it, how to read its options and result, and whether it changes production. This is the recommended starting point if ChatGPT is offline. The original advanced explanations remain under [`offline-reference/`](offline-reference/README.md).

## Offline use and automatic vendor reviews

- **[Offline overview](OFFLINE-OVERVIEW.md)** — conceptual guide and safety workflow available without ChatGPT.
- **[Complete local command reference](offline-reference/README.md)** — locally stored command-by-command explanations and syntax from the runbooks.
- **[Vendor change dashboard](vendor-watch/STATUS.md)** and **[proposed changes](vendor-watch/CHANGES.md)** — show monitored release/command review candidates.
- **[Current vendor baseline and regenerated offline docs — draft PR #1](https://github.com/tbisla75/terraform-commands/pull/1)** — review the actual detected release notes and file diffs before merging.
- **[Weekly update workflow](.github/workflows/offline-and-vendor-watch.yml)** — rebuilds offline docs and checks vendor references each Monday; raises a review-only GitHub PR if workflow permissions permit. It never silently replaces vendor commands.

**For fully offline access, clone this repository or download its ZIP in advance.** ChatGPT explanation links are optional; the local Markdown command reference works without them.


Production-oriented Terraform command reference, with individual ChatGPT explanations, cloud infrastructure starter configurations, kubeadm HA setup and OpenShift Installer inputs.

> 🟢 Review/validate first. 🟠 Apply is a production change. 🔴 Never commit state, real tfvars, cloud credentials, Red Hat pull secrets, kubeconfigs or customer topology.

## Terraform commands

| Runbook | Contents |
|---|---|
| [01 — Terraform CLI and State](01-CLI-STATE-WORKSPACES.md) | Init, plan, apply, import, state, workspaces |
| [02 — Security and CI](02-ENTERPRISE-IAC-SECURITY.md) | OIDC, state, scanning, policy, protected pipelines |
| [03 — Advanced Troubleshooting](03-ADVANCED-TROUBLESHOOTING.md) | State locks, drift, provider failures, resource import/replacement |
| [04 — Cloud Provisioning Checklist](04-CLOUD-PROVISIONING-CHECKLIST.md) | AWS, Azure, Google Cloud, vSphere, bare metal |
| [05 — GitLab Terraform Pipeline](05-GITLAB-TERRAFORM-PIPELINE.md) | Protected validate/plan/manual-apply CI/CD |
| [06 — Terraform and Template Syntax](06-TERRAFORM-AND-TEMPLATE-SYNTAX-CHATGPT.md) | 🧠 ChatGPT per-resource and YAML explanations |

## Cluster provisioning templates

| Target | Starter files | Notes |
|---|---|---|
| Kubernetes HA on VMs/bare metal | [kubeadm HA template](templates/kubeadm-ha/README.md) | 3 CP + >=3 workers; requires LB, CNI, CSI and production integrations |
| EKS on AWS | [EKS Terraform](templates/cloud-managed/aws-eks/main.tf) | Managed control plane; existing private VPC subnets |
| AKS on Azure | [AKS Terraform](templates/cloud-managed/azure-aks/main.tf) | Managed control plane; existing VNet and private DNS |
| GKE on Google Cloud | [GKE Terraform](templates/cloud-managed/gcp-gke/main.tf) | Private workers; approved administrative API CIDRs and Cloud NAT |
| OpenShift IPI AWS/Azure/GCP | [OpenShift cloud installer inputs](templates/openshift-ipi/README.md) | RHCOS + supported openshift-install |
| OpenShift bare metal | [Agent-based six-node template](templates/openshift-ipi/agent-config.baremetal.yaml) | 3 masters + 3 workers; real MACs/VIPs/DNS required |

## Start with the Terraform cloud starter

```bash
cd templates/cloud-managed/aws-eks
cp terraform.tfvars.example terraform.tfvars
# Edit placeholders and configure remote locked state and cloud identity.
terraform init
terraform validate
terraform plan -out=tfplan
# CHANGE only after approval:
terraform apply tfplan
```

[🧠 Explain Terraform init](https://chatgpt.com/?q=Explain%20terraform%20init%20full%20syntax%20security%20and%20state%20backend) · [🧠 Explain Terraform plan](https://chatgpt.com/?q=Explain%20terraform%20plan%20-out%3Dtfplan%20including%20sensitive%20output%20and%20state%20locking) · [🧠 Explain Terraform apply](https://chatgpt.com/?q=Explain%20terraform%20apply%20tfplan%20full%20syntax%20risk%20and%20production%20change%20control)

**Status:** These are deployment **starters**, not one-click certified enterprise production environments. I have not run `terraform validate` with provider plugins or deployed them to your cloud accounts. Cloud and OpenShift installation depend on validated release/region/network/service quotas, available permissions and production security controls. Add monitoring, backup/DR, GitOps, ingress/WAF, registry, identity and documented support/patch processes before declaring production ready.

Related: [Linux node preparation](https://github.com/tbisla75/Linux-Commands), [Kubernetes operations](https://github.com/tbisla75/kubernetes-commands), [OpenShift operations](https://github.com/tbisla75/Open-Shift-Commands).
