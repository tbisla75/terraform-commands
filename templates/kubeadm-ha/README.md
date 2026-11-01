# kubeadm HA cluster — customer-ready installation template

**Design:** 3 dedicated control-plane nodes + >=3 workers; external redundant TCP/6443 LB (VIP/DNS), stable DNS/NTP, reserved routable host IPs, 2+ racks/hosts, CSI/CNI, registry, external storage, monitoring, backups and restore test. This is a **deployment starter**, not a ready-to-operate production cluster without these integrations.

## 0. Prerequisites

1. Review [Linux preparation script](https://github.com/tbisla75/Linux-Commands/blob/main/scripts/prepare-kubernetes-node.sh); dry-run, then apply to each supported Ubuntu/Debian/RHEL Linux machine.
2. Configure HAProxy/AVI/F5/VIP for `k8s-api.example.internal:6443` forwarding to the 3 control-plane API ports. Validate reachability/health and certificate SANs. Configure workload ingress separately on 80/443.
3. Confirm firewall/security groups permit node traffic, etcd CP-to-CP TCP/2379-2380, kubelet TCP/10250, CNI-specific ports, and DNS/NTP. Never open Kubernetes API to the whole Internet.
4. Choose and validate supported CNI (Calico/Cilium/etc), CSI, Gateway/Ingress, LB implementation and cluster lifecycle. Reference Pod CIDR 10.244.0.0/16 only if your chosen CNI supports it.
5. Replace placeholders in [kubeadm-config.yaml](kubeadm-config.yaml), pin a compatible patch version; check your kubeadm supports `v1beta4`.

## 1. First control-plane node — approved CHANGE

```bash
sudo kubeadm init --config kubeadm-config.yaml --upload-certs
mkdir -p "$HOME/.kube"
sudo install -m 600 /etc/kubernetes/admin.conf "$HOME/.kube/config"
kubectl get nodes -o wide
```

**SECURITY:** `admin.conf`, `kubeadm join` token and uploaded `certificate-key` grant sensitive access. Treat as secrets; store only in a protected vault. Do not paste their output into GitHub or ChatGPT.

## 2. Install networking and join other nodes

Apply a **version-pinned, vendor-approved CNI manifest** only after verifying CRDs, eBPF/kernel support, policy and Pod CIDR. Do not paste unknown `curl | kubectl apply`.

From approved first control-plane node, generate join information:

```bash
sudo kubeadm token create --print-join-command
sudo kubeadm init phase upload-certs --upload-certs
```

On other control-plane nodes, execute the approved join command with `--control-plane --certificate-key <SECRET>`; on workers execute join without these flags. Keep certificates and token confidential. Confirm etcd quorum/API and node readiness after **each** control-plane join; do not join all CPs blindly in parallel.

## 3. Validate and productionize

```bash
kubectl get nodes -o wide
kubectl get pods -A
kubectl get --raw='/readyz?verbose'
kubectl get storageclass,csidriver
kubectl get pdb -A
kubectl get networkpolicy -A
```

Add enterprise storage, application ingress/WAF, SSO/RBAC, Pod Security Admission, registry, cert-manager, monitoring, backup and hardened remote access. Test failure of one CP/worker, backup restore, PV data recovery and rolling upgrades before customer acceptance.

**Rollback:** For workload issues revert GitOps manifests. For control-plane/etcd corruption follow reviewed DR runbook; **do not run `kubeadm reset` on every node**. See [kubeadm upgrade recovery](https://github.com/tbisla75/kubernetes-commands/blob/main/06-KUBEADM-UPGRADE-RECOVERY.md).

Refs: [Kubernetes HA kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/), [kubeadm config](https://kubernetes.io/docs/reference/config-api/kubeadm-config.v1beta4/).
