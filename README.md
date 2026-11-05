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
<img src="https://img.shields.io/badge/upstream%20PRs-96-1F6FEB?style=flat-square" alt="Upstream PRs"> <img src="https://img.shields.io/badge/merged-8-8957E5?style=flat-square" alt="Merged"> <img src="https://img.shields.io/badge/projects-65-2EA043?style=flat-square" alt="Projects">

**Merged**

- [tsuru/charts](https://github.com/tsuru/charts): [fix(tsuru-prometheus-pool): honor securityContext from values](https://github.com/tsuru/charts/pull/53)
- [tsuru/charts](https://github.com/tsuru/charts): [ci: publish charts as OCI artifacts to GHCR](https://github.com/tsuru/charts/pull/55)
- [hetznercloud/hcloud-cloud-controller-manager](https://github.com/hetznercloud/hcloud-cloud-controller-manager): [fix(load-balancer): trim spaces in comma separated annotations](https://github.com/hetznercloud/hcloud-cloud-controller-manager/pull/1411)
- [openobserve/openobserve-helm-chart](https://github.com/openobserve/openobserve-helm-chart): [fix(openobserve-collector): apply image.pullPolicy to the collectors](https://github.com/openobserve/openobserve-helm-chart/pull/286)
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open): [feat: add Helm chart](https://github.com/AsyncFuncAI/deepwiki-open/pull/621)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: resourceMap: Resolve HTTPRoute parent and backend refs](https://github.com/kubernetes-sigs/headlamp/pull/8254)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: util: Use desired DaemonSet pods as the total](https://github.com/kubernetes-sigs/headlamp/pull/8259)
- [tsuru/tsuru-client](https://github.com/tsuru/tsuru-client): [fix: keep the current target in sync on target update](https://github.com/tsuru/tsuru-client/pull/283)

**In review**

| Project | Latest pull request |
|---|---|
| [vultr/terraform-provider-vultr](https://github.com/vultr/terraform-provider-vultr) | [Mark credential attributes as sensitive](https://github.com/vultr/terraform-provider-vultr/pull/811) · +1 more |
| [digitalocean/terraform-provider-digitalocean](https://github.com/digitalocean/terraform-provider-digitalocean) | [spaces: remove bucket CORS configuration from state when it is gone](https://github.com/digitalocean/terraform-provider-digitalocean/pull/1633) |
| [kubernetes-sigs/cluster-inventory-api](https://github.com/kubernetes-sigs/cluster-inventory-api) | [access: sort profile-sourced exec env vars by name](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/96) · +1 more |
| [exoscale/terraform-provider-exoscale](https://github.com/exoscale/terraform-provider-exoscale) | [fix(block_storage_volume_snapshot): remove from state when deleted outside of Terraform](https://github.com/exoscale/terraform-provider-exoscale/pull/642) |
| [kubernetes-sigs/e2e-framework](https://github.com/kubernetes-sigs/e2e-framework) | [conditions: wait for observed generation in DaemonSetReady](https://github.com/kubernetes-sigs/e2e-framework/pull/607) · +2 more |
| [cert-manager/cert-manager](https://github.com/cert-manager/cert-manager) | [fix(pki): accept lowercase attribute type names in literalSubject](https://github.com/cert-manager/cert-manager/pull/9556) |
| [metallb/metallb](https://github.com/metallb/metallb) | [config: detect duplicate BGPPeers that only differ by name](https://github.com/metallb/metallb/pull/3182) |
| [stakater/Reloader](https://github.com/stakater/Reloader) | [fix(handler): treat non-2xx --webhook-url responses as failures](https://github.com/stakater/Reloader/pull/1269) |
| [aws/aws-cli](https://github.com/aws/aws-cli) | [Write JSON file cache entries atomically](https://github.com/aws/aws-cli/pull/10856) |
| [cloudflare/cfssl](https://github.com/cloudflare/cfssl) | [signer: trim spaces and skip empty entries in SplitHosts](https://github.com/cloudflare/cfssl/pull/1463) |
| [awslabs/eks-node-viewer](https://github.com/awslabs/eks-node-viewer) | [fix: update node usage when a bound pod's requests change](https://github.com/awslabs/eks-node-viewer/pull/547) |
| [bitnami/sealed-secrets](https://github.com/bitnami/sealed-secrets) | [fix(kubeseal): fail on malformed documents instead of skipping them](https://github.com/bitnami/sealed-secrets/pull/2097) · +1 more |
| [istio/istio](https://github.com/istio/istio) | [gateway: honor exportTo when resolving Hostname backendRefs](https://github.com/istio/istio/pull/62659) |
| [otwld/ollama-helm](https://github.com/otwld/ollama-helm) | [fix: keep service ipFamilies inside the non-Knative Service](https://github.com/otwld/ollama-helm/pull/296) · +1 more |
| [kubernetes-sigs/kwok](https://github.com/kubernetes-sigs/kwok) | [heap: update the key when pushing an existing item](https://github.com/kubernetes-sigs/kwok/pull/1801) |

…and pull requests in 48 more projects.
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
