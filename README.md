### Lucas Barros

<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=20&duration=3500&pause=1200&color=58A6FF&center=true&vCenter=true&width=640&lines=Platform+engineering+on+Kubernetes;Terraform+%C2%B7+GitOps+%C2%B7+Atlantis+%C2%B7+Envoy;Boring%2C+predictable+infrastructure" alt="Platform engineering on Kubernetes">
</p>

Platform engineer based in Rio de Janeiro. I design and operate Kubernetes platforms for teams that ship to production every day, mostly in financial services.

Over the last years that meant running a fleet of 330 clusters behind ArgoCD, Atlantis and Rancher, turning EKS provisioning from a two-day manual process into a 40-minute Terraform/Terragrunt pipeline, moving a 3,000 jobs/day Jenkins farm to immutable infrastructure, and treating cloud cost as an engineering metric rather than a finance report.

I care about boring, predictable infrastructure: everything in code, every change reviewed, upgrades that nobody notices.

**Open source**

Contributing upstream across the cloud native ecosystem: CNCF projects like Kubernetes, Envoy, Prometheus, Argo, Crossplane, Headlamp and CoreDNS, plus Terraform providers, Helm charts and AI infrastructure tooling (NVIDIA device plugin, Ray, deepwiki-open).

<!--START_SECTION:activity-->
<img src="https://img.shields.io/badge/upstream%20PRs-96-1F6FEB?style=flat-square" alt="Upstream PRs"> <img src="https://img.shields.io/badge/merged-6-8957E5?style=flat-square" alt="Merged"> <img src="https://img.shields.io/badge/projects-65-2EA043?style=flat-square" alt="Projects">

**Merged**

- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open): [feat: add Helm chart](https://github.com/AsyncFuncAI/deepwiki-open/pull/621)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: resourceMap: Resolve HTTPRoute parent and backend refs](https://github.com/kubernetes-sigs/headlamp/pull/8254)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: util: Use desired DaemonSet pods as the total](https://github.com/kubernetes-sigs/headlamp/pull/8259)
- [tsuru/tsuru-client](https://github.com/tsuru/tsuru-client): [fix: keep the current target in sync on target update](https://github.com/tsuru/tsuru-client/pull/283)
- [coredns/helm](https://github.com/coredns/helm): [docs: note that the ServiceMonitor needs the metrics Service](https://github.com/coredns/helm/pull/288)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: resourceMap: Match NetworkPolicy podSelector fully](https://github.com/kubernetes-sigs/headlamp/pull/8245)

**In review**

| Project | Latest pull request |
|---|---|
| [sergelogvinov/proxmox-cloud-controller-manager](https://github.com/sergelogvinov/proxmox-cloud-controller-manager) | [fix: keep ip_sort_order cidrs out of the ignore list](https://github.com/sergelogvinov/proxmox-cloud-controller-manager/pull/349) |
| [MagaluCloud/mgc-sdk-go](https://github.com/MagaluCloud/mgc-sdk-go) | [fix(http): always send the request when MaxAttempts is zero or negative](https://github.com/MagaluCloud/mgc-sdk-go/pull/197) |
| [kubernetes-sigs/cluster-inventory-api](https://github.com/kubernetes-sigs/cluster-inventory-api) | [access: do not modify the provider exec config](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/93) |
| [MagaluCloud/terraform-provider-mgc](https://github.com/MagaluCloud/terraform-provider-mgc) | [fix(blockstorage): remove volume from state when it no longer exists](https://github.com/MagaluCloud/terraform-provider-mgc/pull/329) · +1 more |
| [hetznercloud/hcloud-cloud-controller-manager](https://github.com/hetznercloud/hcloud-cloud-controller-manager) | [fix(load-balancer): trim spaces in comma separated annotations](https://github.com/hetznercloud/hcloud-cloud-controller-manager/pull/1411) |
| [ansible-collections/community.proxmox](https://github.com/ansible-collections/community.proxmox) | [fix(proxmox_kvm): return newid when the clone target already exists](https://github.com/ansible-collections/community.proxmox/pull/559) |
| [bpg/terraform-provider-proxmox](https://github.com/bpg/terraform-provider-proxmox) | [fix(acme): remove dns plugin from state when deleted outside terraform](https://github.com/bpg/terraform-provider-proxmox/pull/3259) · +1 more |
| [hetznercloud/hcloud-go](https://github.com/hetznercloud/hcloud-go) | [fix(exp): escape backslashes in TXT records and keep escapes in one chunk](https://github.com/hetznercloud/hcloud-go/pull/963) |
| [hetznercloud/terraform-provider-hcloud](https://github.com/hetznercloud/terraform-provider-hcloud) | [fix(server): do not delete primary ip already assigned to the server](https://github.com/hetznercloud/terraform-provider-hcloud/pull/1558) |
| [helmfile/helmfile](https://github.com/helmfile/helmfile) | [fix: keep elements added to an existing array by --state-values-set](https://github.com/helmfile/helmfile/pull/2873) |
| [aws-ia/terraform-aws-eks-blueprints-addons](https://github.com/aws-ia/terraform-aws-eks-blueprints-addons) | [fix: Keep nested prefixes in the Velero backup location](https://github.com/aws-ia/terraform-aws-eks-blueprints-addons/pull/524) |
| [kubernetes-sigs/descheduler](https://github.com/kubernetes-sigs/descheduler) | [fix(helm): allow setting serviceMonitor.honorLabels to false](https://github.com/kubernetes-sigs/descheduler/pull/1940) |
| [bitnami/sealed-secrets](https://github.com/bitnami/sealed-secrets) | [fix(helm): use the container ports in the NetworkPolicy ingress rule](https://github.com/bitnami/sealed-secrets/pull/2096) |
| [NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin) | [Inspect embedded config.map entries before adding SYS_ADMIN](https://github.com/NVIDIA/k8s-device-plugin/pull/2155) |
| [terraform-aws-modules/terraform-aws-iam](https://github.com/terraform-aws-modules/terraform-aws-iam) | [fix: Keep IRSA policy count known when policy documents are not read](https://github.com/terraform-aws-modules/terraform-aws-iam/pull/671) · +1 more |

…and pull requests in 50 more projects.
<!--END_SECTION:activity-->

**Projects**

- [helm-charts](https://github.com/lbarrosby/helm-charts): production-ready Helm charts with secure defaults, Gateway API, HPA/KEDA and schema-validated values, tested and released from CI
- [terraform-aws-platform](https://github.com/lbarrosby/terraform-aws-platform): opinionated Terraform modules for EKS platforms (VPC, EKS with access entries and Pod Identity, Karpenter), tested with mock providers and laid out for Terragrunt

<br>

<a href="https://www.linkedin.com/in/lucas-rbarros"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="mailto:lucasbarros.kam@gmail.com"><img src="https://img.shields.io/badge/Email-1F2937?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
<img src="https://komarev.com/ghpvc/?username=lbarrosby&style=flat-square&color=1F2937&label=profile+views" alt="Profile views">

<br>

**Certifications**

<p>
<img src="https://img.shields.io/badge/CKA-Certified%20Kubernetes%20Administrator%20·%202024-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="CKA">
<img src="https://img.shields.io/badge/HashiCorp-Terraform%20Associate%20·%202022-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="Terraform Associate">
<img src="https://img.shields.io/badge/AWS-Solutions%20Architect%20Associate%20·%202022-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS Solutions Architect Associate">
<img src="https://img.shields.io/badge/Tigera-Calico%20Operator%20eBPF%20·%202024-FB8C00?style=flat-square" alt="Calico Operator eBPF">
<img src="https://img.shields.io/badge/VMware-Double%20VCP%20(DCV%20%2B%20CMA)%20·%202022-607078?style=flat-square&logo=vmware&logoColor=white" alt="VMware Double VCP">
<img src="https://img.shields.io/badge/AWS-Cloud%20Practitioner%20·%202022-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS Cloud Practitioner">
<img src="https://img.shields.io/badge/Microsoft-Azure%20Fundamentals%20·%202022-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" alt="Azure Fundamentals">
</p>

**Platform** &nbsp;
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes">
<img src="https://img.shields.io/badge/Amazon%20EKS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="EKS">
<img src="https://img.shields.io/badge/Rancher-0075A8?style=flat-square&logo=rancher&logoColor=white" alt="Rancher">
<img src="https://img.shields.io/badge/Envoy-AC6199?style=flat-square&logo=envoyproxy&logoColor=white" alt="Envoy">
<img src="https://img.shields.io/badge/Istio-466BB0?style=flat-square&logo=istio&logoColor=white" alt="Istio">
<img src="https://img.shields.io/badge/Cilium-F8C517?style=flat-square&logo=cilium&logoColor=black" alt="Cilium">

**Delivery** &nbsp;
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="Terraform">
<img src="https://img.shields.io/badge/Atlantis-0A4D8C?style=flat-square" alt="Atlantis">
<img src="https://img.shields.io/badge/Argo%20CD-EF7B4D?style=flat-square&logo=argo&logoColor=white" alt="Argo CD">
<img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" alt="Helm">
<img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white" alt="Jenkins">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
<img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible">

**Observability** &nbsp;
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus">
<img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana">
<img src="https://img.shields.io/badge/Datadog-632CA6?style=flat-square&logo=datadog&logoColor=white" alt="Datadog">

**Cloud & code** &nbsp;
<img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS">
<img src="https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" alt="Azure">
<img src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="GCP">
<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">

<br>

<p>
  <img height="170" src="https://raw.githubusercontent.com/lbarrosby/lbarrosby/output/profile-summary-card-output/github_dark/0-profile-details.svg" alt="Profile details">
</p>
<p>
  <img height="170" src="https://raw.githubusercontent.com/lbarrosby/lbarrosby/output/profile-summary-card-output/github_dark/3-stats.svg" alt="Stats">
  <img height="170" src="https://raw.githubusercontent.com/lbarrosby/lbarrosby/output/profile-summary-card-output/github_dark/2-most-commit-language.svg" alt="Languages">
  <img height="170" src="https://streak-stats.demolab.com/?user=lbarrosby&theme=github-dark-blue&hide_border=true" alt="Streak">
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lbarrosby/lbarrosby/output/github-contribution-grid-snake-dark.svg">
  <img alt="Contributions" src="https://raw.githubusercontent.com/lbarrosby/lbarrosby/output/github-contribution-grid-snake.svg">
</picture>
