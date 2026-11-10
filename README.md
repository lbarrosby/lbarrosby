### Lucas Barros

Based in Rio de Janeiro. I design and operate Kubernetes platforms for teams that ship to production every day, mostly in financial services.

Over the last years that meant running a fleet of 330 clusters behind ArgoCD, Atlantis and Rancher, turning EKS provisioning from a two-day manual process into a 40-minute Terraform/Terragrunt pipeline, moving a 3,000 jobs/day Jenkins farm to immutable infrastructure, and treating cloud cost as an engineering metric rather than a finance report.

I care about boring, predictable infrastructure: everything in code, every change reviewed, upgrades that nobody notices.

**Open source**

Contributing upstream across the cloud native ecosystem: CNCF projects like Kubernetes, Envoy, Prometheus, Argo, Crossplane, Headlamp and CoreDNS, plus Terraform providers, Helm charts and AI infrastructure tooling (NVIDIA device plugin, Ray, deepwiki-open).

<!--START_SECTION:activity-->
<img src="https://img.shields.io/badge/upstream%20PRs-627-1F6FEB?style=flat-square" alt="Upstream PRs"> <img src="https://img.shields.io/badge/merged-179-8957E5?style=flat-square" alt="Merged"> <img src="https://img.shields.io/badge/projects-255-2EA043?style=flat-square" alt="Projects"> <img src="https://img.shields.io/badge/merged%20in%20official%20CNCF%20graduated%20repos-6-0086FF?style=flat-square" alt="Merged in repositories the CNCF lists for graduated projects"> <a href="https://lbarrosby.github.io/lbarrosby/"><img src="https://img.shields.io/badge/filter%20%26%20search-all%20PRs-F78166?style=flat-square&logo=githubpages&logoColor=white" alt="Filter and search all PRs"></a> <img src="https://img.shields.io/badge/thanked%20by%20maintainers-79-DB61A2?style=flat-square" alt="Thanked by maintainers">

**Merged** · official CNCF project repositories first · [see all 179 with filters](https://lbarrosby.github.io/lbarrosby/)

<details open><summary><b>Official CNCF Graduated projects</b> · 6 merged in 4 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/Karmada-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Karmada: official repository of a CNCF graduated project" title="Karmada: official repository of a CNCF graduated project"><br>[karmada-io/karmada](https://github.com/karmada-io/karmada) | [fix(resourceinterpreter): skip Ingress TLS entries without secretName in dependencies](https://github.com/karmada-io/karmada/pull/8029) | 2026-11-10 | [@karmada-bot](https://github.com/karmada-bot) | 🙏 [@zhzhuang-zju](https://github.com/karmada-io/karmada/pull/8029#issuecomment-6678810771): <i>"Thanks"</i> |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [in_tcp: fix inflated output emit_count when a message arrives in several reads](https://github.com/fluent/fluentd/pull/5608) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5608#pullrequestreview-5835281054): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/CoreDNS-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="CoreDNS: official repository of a CNCF graduated project" title="CoreDNS: official repository of a CNCF graduated project"><br>[coredns/coredns](https://github.com/coredns/coredns) | [plugin/acl: only add the EDE OPT record when the request has EDNS](https://github.com/coredns/coredns/pull/8749) | 2026-11-07 | [@yongtang](https://github.com/yongtang) |  |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [parser_syslog, in_syslog: fix handling of a priority on a later line](https://github.com/fluent/fluentd/pull/5598) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5598#pullrequestreview-5795032353): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [record_accessor: raise ConfigError for a non-integer array index](https://github.com/fluent/fluentd/pull/5596) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5596#pullrequestreview-5794474836): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/Rook-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [osd: don't wipe metadata devices of existing OSDs](https://github.com/rook/rook/pull/18686) | 2026-11-05 | [@arttor](https://github.com/arttor) | 🙏 [@arttor](https://github.com/rook/rook/pull/18686#pullrequestreview-5789316361): <i>"thanks for the fix."</i> |

</details>

<details open><summary><b>Official CNCF Incubating projects</b> · 3 merged in 2 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/Contour-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Contour: official repository of a CNCF incubating project" title="Contour: official repository of a CNCF incubating project"><br>[projectcontour/contour](https://github.com/projectcontour/contour) | [Set alt_stat_name for DNS name clusters](https://github.com/projectcontour/contour/pull/7821) | 2026-11-09 | [@tsaarni](https://github.com/tsaarni) | 🙏 [@tsaarni](https://github.com/projectcontour/contour/pull/7821#pullrequestreview-5803527120): <i>"Thank you for contributing!"</i> |
| <img src="https://img.shields.io/badge/Lima-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limactl edit: warn when changing the VM type of an existing instance](https://github.com/lima-vm/lima/pull/5743) | 2026-11-05 | [@AkihiroSuda](https://github.com/AkihiroSuda) |  |
| <img src="https://img.shields.io/badge/Lima-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limayaml: don't panic when the latest config fails to load](https://github.com/lima-vm/lima/pull/5738) | 2026-11-05 | [@unsuman](https://github.com/unsuman) | 🙏 [@AkihiroSuda](https://github.com/lima-vm/lima/pull/5738#pullrequestreview-5784793825): <i>"Thanks"</i> |

</details>

<details open><summary><b>Official CNCF Sandbox projects</b> · 5 merged in 2 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/kube--vip-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="kube-vip: official repository of a CNCF sandbox project" title="kube-vip: official repository of a CNCF sandbox project"><br>[kube-vip/kube-vip](https://github.com/kube-vip/kube-vip) | [fix(services): do not treat DHCP placeholder VIPs as shared](https://github.com/kube-vip/kube-vip/pull/1838) | 2026-11-09 | [@Cellebyte](https://github.com/Cellebyte) |  |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [backend: auth: Accept a single string groups claim in /me](https://github.com/kubernetes-sigs/headlamp/pull/8262) | 2026-11-05 | [@skoeva](https://github.com/skoeva) | 🙏 [@skoeva](https://github.com/kubernetes-sigs/headlamp/pull/8262#pullrequestreview-5785420953): <i>"lgtm, thanks"</i> |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Resolve HTTPRoute parent and backend refs](https://github.com/kubernetes-sigs/headlamp/pull/8254) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: util: Use desired DaemonSet pods as the total](https://github.com/kubernetes-sigs/headlamp/pull/8259) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Match NetworkPolicy podSelector fully](https://github.com/kubernetes-sigs/headlamp/pull/8245) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |

</details>

<details><summary><b>Latest merges elsewhere</b> · 15 most recent of 165 (ecosystem, Terraform providers, Helm charts, tools)</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| [xorbitsai/inference](https://github.com/xorbitsai/inference) | [fix(audio): flush the StreamWriter tail when streaming speech on torchaudio < 2.9](https://github.com/xorbitsai/inference/pull/6061) | 2026-11-10 | [@qinxuye](https://github.com/qinxuye) |  |
| <img src="https://img.shields.io/badge/Fluentd%20ecosystem-not%20the%20main%20repo-555?style=flat-square" alt="Fluentd ecosystem: not the main Fluentd repository" title="Fluentd ecosystem: not the main Fluentd repository"><br>[fluent/fluent-plugin-opensearch](https://github.com/fluent/fluent-plugin-opensearch) | [out_opensearch,in_opensearch: rebuild the client when only the port, scheme or path of a host changes](https://github.com/fluent/fluent-plugin-opensearch/pull/202) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluent-plugin-opensearch/pull/202#pullrequestreview-5839113640): <i>"Thanks for the fix."</i> |
| [kokuwaio/helm-charts](https://github.com/kokuwaio/helm-charts) | [fix(mysqldump): delete expired backups again in housekeeping](https://github.com/kokuwaio/helm-charts/pull/258) | 2026-11-10 | [@monotek](https://github.com/monotek) |  |
| <img src="https://img.shields.io/badge/CoreDNS%20ecosystem-not%20the%20main%20repo-555?style=flat-square" alt="CoreDNS ecosystem: not the main CoreDNS repository" title="CoreDNS ecosystem: not the main CoreDNS repository"><br>[coredns/helm](https://github.com/coredns/helm) | [fix: keep trafficDistribution inside the deployment.enabled guard](https://github.com/coredns/helm/pull/290) | 2026-11-10 | [@hagaibarel](https://github.com/hagaibarel) | 🙏 [@hagaibarel](https://github.com/coredns/helm/pull/290#issuecomment-6762305088): <i>"Thanks for the PR!"</i> |
| [kubecolor/kubecolor](https://github.com/kubecolor/kubecolor) | [feat: colorize kubectl taint output](https://github.com/kubecolor/kubecolor/pull/393) | 2026-11-10 | [@applejag](https://github.com/applejag) | 🙏 [@applejag](https://github.com/kubecolor/kubecolor/pull/393#issuecomment-6761940787): <i>"Thank you for this!"</i> |
| [tensorchord/Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) | [Add AI observability pack to Observability](https://github.com/tensorchord/Awesome-LLMOps/pull/1126) | 2026-11-10 | [@NeroHin](https://github.com/NeroHin) | 🙏 [@NeroHin](https://github.com/tensorchord/Awesome-LLMOps/pull/1126#pullrequestreview-5837612769): <i>"Thanks!"</i> |
| [helmfile/helmfile](https://github.com/helmfile/helmfile) | [docs: document trackFailOnError and helmStuckGrace](https://github.com/helmfile/helmfile/pull/2886) | 2026-11-10 | [@yxxhero](https://github.com/yxxhero) |  |
| [equinix/terraform-provider-equinix](https://github.com/equinix/terraform-provider-equinix) | [fix: keep the configured stream_id in stream subscription and alert rule data sources](https://github.com/equinix/terraform-provider-equinix/pull/1133) | 2026-11-10 | [@tng1-equinix](https://github.com/tng1-equinix) |  |
| [equinix/terraform-provider-equinix](https://github.com/equinix/terraform-provider-equinix) | [fix: remove equinix_fabric_connection from state when it no longer exists](https://github.com/equinix/terraform-provider-equinix/pull/1103) | 2026-11-10 | [@tng1-equinix](https://github.com/tng1-equinix) |  |
| [otwld/ollama-helm](https://github.com/otwld/ollama-helm) | [fix: keep service ipFamilies inside the non-Knative Service](https://github.com/otwld/ollama-helm/pull/296) | 2026-11-10 | [@jdetroyes](https://github.com/jdetroyes) |  |
| [otwld/ollama-helm](https://github.com/otwld/ollama-helm) | [fix: allow revisionHistoryLimit to be set to 0](https://github.com/otwld/ollama-helm/pull/295) | 2026-11-10 | [@jdetroyes](https://github.com/jdetroyes) |  |
| [fluent-plugins-nursery/fluent-plugin-concat](https://github.com/fluent-plugins-nursery/fluent-plugin-concat) | [Fix timeout flush stopping when a partial_ordinal cannot be converted](https://github.com/fluent-plugins-nursery/fluent-plugin-concat/pull/164) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) |  |
| [fluent-plugins-nursery/fluent-plugin-kubernetes_metadata_filter](https://github.com/fluent-plugins-nursery/fluent-plugin-kubernetes_metadata_filter) | [Point the container to the pod once a later lookup finds it](https://github.com/fluent-plugins-nursery/fluent-plugin-kubernetes_metadata_filter/pull/438) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent-plugins-nursery/fluent-plugin-kubernetes_metadata_filter/pull/438#pullrequestreview-5821215808): <i>"Thanks for the fix and the test."</i> |
| [fluent-plugins-nursery/fluent-plugin-cloudwatch-logs](https://github.com/fluent-plugins-nursery/fluent-plugin-cloudwatch-logs) | [Fix log_group_aws_tags placeholders resolved only for the first chunk](https://github.com/fluent-plugins-nursery/fluent-plugin-cloudwatch-logs/pull/290) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent-plugins-nursery/fluent-plugin-cloudwatch-logs/pull/290#pullrequestreview-5821683645): <i>"Thanks for the fix."</i> |
| [equinix/terraform-provider-equinix](https://github.com/equinix/terraform-provider-equinix) | [fix: mark Fabric credential attributes as sensitive](https://github.com/equinix/terraform-provider-equinix/pull/1101) | 2026-11-09 | [@ctreatma](https://github.com/ctreatma) |  |

[All 165 of them, with filters](https://lbarrosby.github.io/lbarrosby/)

</details>

**In review** · 448 open pull requests · [browse and filter](https://lbarrosby.github.io/lbarrosby/)

- Official CNCF Graduated: 36 in 16 repos
- Official CNCF Incubating: 10 in 3 repos
- Official CNCF Sandbox: 15 in 6 repos
- CNCF ecosystem: 127 in 60 repos
- Other: 260 in 159 repos

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
