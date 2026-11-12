### Lucas Barros

Based in Rio de Janeiro. I design and operate Kubernetes platforms for teams that ship to production every day, mostly in financial services.

Over the last years that meant running a fleet of 330 clusters behind ArgoCD, Atlantis and Rancher, turning EKS provisioning from a two-day manual process into a 40-minute Terraform/Terragrunt pipeline, moving a 3,000 jobs/day Jenkins farm to immutable infrastructure, and treating cloud cost as an engineering metric rather than a finance report.

I care about boring, predictable infrastructure: everything in code, every change reviewed, upgrades that nobody notices.

**Open source**

Contributing upstream across the cloud native ecosystem: CNCF projects like Kubernetes, Envoy, Prometheus, Argo, Crossplane, Headlamp and CoreDNS, plus Terraform providers, Helm charts and AI infrastructure tooling (NVIDIA device plugin, Ray, deepwiki-open).

<!--START_SECTION:activity-->
<img src="https://img.shields.io/badge/upstream%20PRs-683-1F6FEB?style=flat-square" alt="Upstream PRs"> <img src="https://img.shields.io/badge/merged-255-8957E5?style=flat-square" alt="Merged"> <img src="https://img.shields.io/badge/projects-270-2EA043?style=flat-square" alt="Projects"> <img src="https://img.shields.io/badge/merged%20in%20official%20CNCF%20graduated%20repos-7-0086FF?style=flat-square" alt="Merged in repositories the CNCF lists for graduated projects"> <a href="https://lbarrosby.github.io/lbarrosby/"><img src="https://img.shields.io/badge/filter%20%26%20search-all%20PRs-F78166?style=flat-square&logo=githubpages&logoColor=white" alt="Filter and search all PRs"></a> <img src="https://img.shields.io/badge/thanked%20by%20maintainers-117-DB61A2?style=flat-square" alt="Thanked by maintainers">

**Merged** · official CNCF project repositories first · [see all 255 with filters](https://lbarrosby.github.io/lbarrosby/)

<details open><summary><b>Official CNCF Graduated projects</b> · 7 merged in 5 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/Kubernetes-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Kubernetes: official repository of a CNCF graduated project" title="Kubernetes: official repository of a CNCF graduated project"><br>[kubernetes/cloud-provider-openstack](https://github.com/kubernetes/cloud-provider-openstack) | [[occm] Rename listener when its pool already has the new cluster-name](https://github.com/kubernetes/cloud-provider-openstack/pull/3283) | 2026-11-12 | bot |  |
| <img src="https://img.shields.io/badge/Karmada-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Karmada: official repository of a CNCF graduated project" title="Karmada: official repository of a CNCF graduated project"><br>[karmada-io/karmada](https://github.com/karmada-io/karmada) | [fix(resourceinterpreter): skip Ingress TLS entries without secretName in dependencies](https://github.com/karmada-io/karmada/pull/8029) | 2026-11-10 | [@karmada-bot](https://github.com/karmada-bot) | 🙏 [@zhzhuang-zju](https://github.com/karmada-io/karmada/pull/8029#issuecomment-6678810771): <i>"Thanks"</i> |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [in_tcp: fix inflated output emit_count when a message arrives in several reads](https://github.com/fluent/fluentd/pull/5608) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5608#pullrequestreview-5835281054): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/CoreDNS-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="CoreDNS: official repository of a CNCF graduated project" title="CoreDNS: official repository of a CNCF graduated project"><br>[coredns/coredns](https://github.com/coredns/coredns) | [plugin/acl: only add the EDE OPT record when the request has EDNS](https://github.com/coredns/coredns/pull/8749) | 2026-11-07 | [@yongtang](https://github.com/yongtang) |  |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [parser_syslog, in_syslog: fix handling of a priority on a later line](https://github.com/fluent/fluentd/pull/5598) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5598#pullrequestreview-5795032353): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [record_accessor: raise ConfigError for a non-integer array index](https://github.com/fluent/fluentd/pull/5596) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5596#pullrequestreview-5794474836): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/Rook-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [osd: don't wipe metadata devices of existing OSDs](https://github.com/rook/rook/pull/18686) | 2026-11-05 | [@arttor](https://github.com/arttor) | 🙏 [@arttor](https://github.com/rook/rook/pull/18686#pullrequestreview-5789316361): <i>"thanks for the fix."</i> |

</details>

<details open><summary><b>Official CNCF Incubating projects</b> · 4 merged in 3 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/OpenCost-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="OpenCost: official repository of a CNCF incubating project" title="OpenCost: official repository of a CNCF incubating project"><br>[opencost/opencost](https://github.com/opencost/opencost) | [fix(inferencecost): keep only grouped properties when aggregating](https://github.com/opencost/opencost/pull/4175) | 2026-11-10 | [@ameijer](https://github.com/ameijer) | 🙏 [@ameijer](https://github.com/opencost/opencost/pull/4175#pullrequestreview-5843570063): <i>"thank you cc @simanadler"</i> |
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

<details><summary><b>Latest merges elsewhere</b> · 15 most recent of 239 (ecosystem, Terraform providers, Helm charts, tools)</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| [opentelekomcloud/terraform-provider-opentelekomcloud](https://github.com/opentelekomcloud/terraform-provider-opentelekomcloud) | [[Fix] SDRS: remove deleted replication pairs from state on read](https://github.com/opentelekomcloud/terraform-provider-opentelekomcloud/pull/3620) | 2026-11-12 | bot |  |
| <img src="https://img.shields.io/badge/Kubernetes%20SIG%20subproject-not%20the%20main%20repo-555?style=flat-square" alt="Kubernetes SIG subproject: not the main Kubernetes repository" title="Kubernetes SIG subproject: not the main Kubernetes repository"><br>[kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver) | [Reject GPU sharing configs that set the other strategy's config](https://github.com/kubernetes-sigs/dra-example-driver/pull/298) | 2026-11-12 | bot |  |
| <img src="https://img.shields.io/badge/Kubernetes%20SIG%20subproject-not%20the%20main%20repo-555?style=flat-square" alt="Kubernetes SIG subproject: not the main Kubernetes repository" title="Kubernetes SIG subproject: not the main Kubernetes repository"><br>[kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver) | [Remove the temp checkpoint file when writing the checkpoint fails](https://github.com/kubernetes-sigs/dra-example-driver/pull/297) | 2026-11-12 | bot |  |
| [fluent-plugins-nursery/fluent-plugin-concat](https://github.com/fluent-plugins-nursery/fluent-plugin-concat) | [Keep the timestamp of a standalone line after a multiline with use_first_timestamp](https://github.com/fluent-plugins-nursery/fluent-plugin-concat/pull/174) | 2026-11-12 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent-plugins-nursery/fluent-plugin-concat/pull/174#pullrequestreview-5856871144): <i>"Thanks for the fix."</i> |
| [fluent-plugins-nursery/fluent-plugin-cloudwatch-logs](https://github.com/fluent-plugins-nursery/fluent-plugin-cloudwatch-logs) | [Keep the chunk when retention_in_days_key has an invalid value](https://github.com/fluent-plugins-nursery/fluent-plugin-cloudwatch-logs/pull/299) | 2026-11-12 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent-plugins-nursery/fluent-plugin-cloudwatch-logs/pull/299#pullrequestreview-5856230295): <i>"Thanks for the fix."</i> |
| <img src="https://img.shields.io/badge/Fluentd%20ecosystem-not%20the%20main%20repo-555?style=flat-square" alt="Fluentd ecosystem: not the main Fluentd repository" title="Fluentd ecosystem: not the main Fluentd repository"><br>[fluent/fluent-plugin-kafka](https://github.com/fluent/fluent-plugin-kafka) | [out_rdkafka: Fix write failing on every chunk with Fluentd v1](https://github.com/fluent/fluent-plugin-kafka/pull/610) | 2026-11-12 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluent-plugin-kafka/pull/610#pullrequestreview-5854076131): <i>"Thanks."</i> |
| <img src="https://img.shields.io/badge/Fluentd%20ecosystem-not%20the%20main%20repo-555?style=flat-square" alt="Fluentd ecosystem: not the main Fluentd repository" title="Fluentd ecosystem: not the main Fluentd repository"><br>[fluent/fluent-plugin-kafka](https://github.com/fluent/fluent-plugin-kafka) | [out_kafka_buffered: Fix endless retries with an invalid partition or a non-String key](https://github.com/fluent/fluent-plugin-kafka/pull/609) | 2026-11-12 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluent-plugin-kafka/pull/609#pullrequestreview-5853980162): <i>"Thanks for bringing the #577 and #603 fixes to kafkabuffered."</i> |
| [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) | [fix: use the shared WebSocket URL helper in slides and workshop pages](https://github.com/AsyncFuncAI/deepwiki-open/pull/622) | 2026-11-12 | [@sng-asyncfunc](https://github.com/sng-asyncfunc) |  |
| [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) | [fix: fall back to the bundled config file when DEEPWIKI_CONFIG_DIR lacks it](https://github.com/AsyncFuncAI/deepwiki-open/pull/630) | 2026-11-12 | [@sng-asyncfunc](https://github.com/sng-asyncfunc) |  |
| [fluent-plugins-nursery/fluent-plugin-remote_syslog](https://github.com/fluent-plugins-nursery/fluent-plugin-remote_syslog) | [Add use_event_time to send the event time as the syslog timestamp](https://github.com/fluent-plugins-nursery/fluent-plugin-remote_syslog/pull/94) | 2026-11-12 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent-plugins-nursery/fluent-plugin-remote_syslog/pull/94#pullrequestreview-5854175620): <i>"Thank you for working on this."</i> |
| [aws/karpenter-provider-aws](https://github.com/aws/karpenter-provider-aws) | [fix: render settings.vmMemoryOverheadPercent when it is 0](https://github.com/aws/karpenter-provider-aws/pull/9852) | 2026-11-12 | [@AndrewSirenko](https://github.com/AndrewSirenko) |  |
| <img src="https://img.shields.io/badge/Kubernetes%20SIG%20subproject-not%20the%20main%20repo-555?style=flat-square" alt="Kubernetes SIG subproject: not the main Kubernetes repository" title="Kubernetes SIG subproject: not the main Kubernetes repository"><br>[kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) | [🐛 (helm/v2-alpha): keep the manager replicas from the kustomize manifest](https://github.com/kubernetes-sigs/kubebuilder/pull/6168) | 2026-11-11 | [@camilamacedo86](https://github.com/camilamacedo86) | 🙏 [@camilamacedo86](https://github.com/kubernetes-sigs/kubebuilder/pull/6168#issuecomment-6799462991): <i>"Great job 👍"</i> |
| <img src="https://img.shields.io/badge/kagent%20ecosystem-not%20the%20main%20repo-555?style=flat-square" alt="kagent ecosystem: not the main kagent repository" title="kagent ecosystem: not the main kagent repository"><br>[kagent-dev/tools](https://github.com/kagent-dev/tools) | [fix(logger): honor LOG_LEVEL](https://github.com/kagent-dev/tools/pull/100) | 2026-11-11 | [@dimetron](https://github.com/dimetron) |  |
| <img src="https://img.shields.io/badge/Kubernetes%20SIG%20subproject-not%20the%20main%20repo-555?style=flat-square" alt="Kubernetes SIG subproject: not the main Kubernetes repository" title="Kubernetes SIG subproject: not the main Kubernetes repository"><br>[kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) | [🐛 (API): return the error from closing a file written by the scaffold](https://github.com/kubernetes-sigs/kubebuilder/pull/6170) | 2026-11-11 | [@camilamacedo86](https://github.com/camilamacedo86) | 🙏 [@camilamacedo86](https://github.com/kubernetes-sigs/kubebuilder/pull/6170#pullrequestreview-5860926201): <i>"Great work 🥇"</i> |
| [jenkinsci/explain-error-plugin](https://github.com/jenkinsci/explain-error-plugin) | [fix: parse Bitbucket Server HTTPS URLs under a context path](https://github.com/jenkinsci/explain-error-plugin/pull/271) | 2026-11-11 | [@shenxianpeng](https://github.com/shenxianpeng) |  |

[All 239 of them, with filters](https://lbarrosby.github.io/lbarrosby/)

</details>

**In review** · 428 open pull requests · [browse and filter](https://lbarrosby.github.io/lbarrosby/)

- Official CNCF Graduated: 36 in 15 repos
- Official CNCF Incubating: 9 in 3 repos
- Official CNCF Sandbox: 15 in 6 repos
- CNCF ecosystem: 124 in 59 repos
- Other: 244 in 155 repos

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
