# Offline operations overview — Terraform infrastructure as code and cluster provisioning

This overview is intended for engineers with no internet access. The per-command breakdown lives in [offline-reference/README.md](offline-reference/README.md). The repository Markdown runbooks are preserved for incident-by-incident operational guidance.

## What the repository covers

- **terraform init/validate/plan/apply and state security**
- **resource lifecycle, import, drift and recovery**
- **AWS EKS/Azure AKS/Google GKE reference infrastructure**
- **OpenShift IPI and bare-metal agent-based installation inputs**
- **GitLab CI protected plan and human-approved apply**

## Working offline safely

1. Verify the host/customer/cluster identity before starting diagnosis. For Kubernetes/OpenShift also confirm kubeconfig/context/project; for VMware confirm ESXi/vCenter name/build; for Terraform confirm state backend, workspace, cloud account and plan.
2. Use read-only inventory commands and record incident time, customer impact, and one healthy comparison node.
3. Find the exact command under [Offline command reference](offline-reference/README.md); read every argument and placeholder. Changes need approval, exact vendor release support and documented rollback.
4. Check the locally installed command's `--help`, OS man pages or `esxcli --help` where appropriate. If local tooling cannot resolve syntax, **do not assume** the offline text covers every vendor variation.
5. Keep secrets, keys, Terraform state, kubeconfigs, vCenter authentication data and customer topology out of GitHub/issues/ChatGPT.
6. When reconnected, open the [Vendor change tracker](vendor-watch/README.md) for review-only upgrade/security candidates.

## Common diagnostic hierarchy

- Layer 1: access/authentication, API/network reachability, DNS and time.
- Layer 2: control plane/service availability and resource capacity.
- Layer 3: workload/job/VM events, system logs, storage and network dependencies.
- Layer 4: root-cause evidence from healthy vs affected nodes and upstream providers.
- Layer 5: approved remediation, validation, regression checks, backup/recovery and post-incident record.

## Change risk and vendor support

**Read-only** queries may still reveal personal/customer information or produce some load. **Changes** can impact resource state, cluster quorum, mounted volumes, storage paths or shared jobs; require customer authorization. **High risk** operations such as etcd restore, ESXi SAN reset, destructive Terraform changes, cluster power actions or raw snapshot deletion are not universal paste-and-run fixes.

**Official documentation starting point:** https://developer.hashicorp.com/terraform/cli

## Vendor automation

The GitHub Action runs weekly and on manual dispatch. It uses the repo's [source configuration](vendor-watch/sources.json), writes [reviewable vendor status](vendor-watch/STATUS.md) and an eventual changes report. It must not be treated as an accurate CVE applicability test; releases/advisories must be checked manually against installed versions and hardware/provider compatibility. **Offline catalogs are rebuilt from the runbooks, not from AI-generated guesses about new vendor commands.**
