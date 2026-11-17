### Lucas Barros

Based in Rio de Janeiro. I design and operate Kubernetes platforms for teams that ship to production every day, mostly in financial services.

Over the last years that meant running a fleet of 330 clusters behind ArgoCD, Atlantis and Rancher, turning EKS provisioning from a two-day manual process into a 40-minute Terraform/Terragrunt pipeline, moving a 3,000 jobs/day Jenkins farm to immutable infrastructure, and treating cloud cost as an engineering metric rather than a finance report.

I care about boring, predictable infrastructure: everything in code, every change reviewed, upgrades that nobody notices.

**Open source**

Contributing upstream across the cloud native ecosystem: CNCF projects like Kubernetes, Envoy, Prometheus, Argo, Crossplane, Headlamp and CoreDNS, plus Terraform providers, Helm charts and AI infrastructure tooling (NVIDIA device plugin, Ray, deepwiki-open).

<!--START_SECTION:activity-->
<img src="https://img.shields.io/badge/upstream%20PRs-859-1F6FEB?style=flat-square" alt="Upstream PRs"> <img src="https://img.shields.io/badge/merged-409-8957E5?style=flat-square" alt="Merged"> <img src="https://img.shields.io/badge/projects-294-2EA043?style=flat-square" alt="Projects"> <img src="https://img.shields.io/badge/merged%20in%20official%20CNCF%20graduated%20repos-13-0086FF?style=flat-square" alt="Merged in repositories the CNCF lists for graduated projects"> <a href="https://lbarrosby.github.io/lbarrosby/"><img src="https://img.shields.io/badge/filter%20%26%20search-all%20PRs-F78166?style=flat-square&logo=githubpages&logoColor=white" alt="Filter and search all PRs"></a> <img src="https://img.shields.io/badge/thanked%20by%20maintainers-184-DB61A2?style=flat-square" alt="Thanked by maintainers"> <a href="https://github.com/kubernetes/kubernetes/pulls?q=is%3Apr+author%3Albarrosby+is%3Amerged"><img src="https://img.shields.io/badge/merged%20in%20kubernetes%2Fkubernetes-1-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Merged in kubernetes/kubernetes"></a>

☸️ **Merged into the Kubernetes core repository** ([kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)): [cloud-provider: validate --concurrent-service-syncs](https://github.com/kubernetes/kubernetes/pull/143991) (2026-11-16 · approved by [@liggitt](https://github.com/liggitt))

**Merged** · official CNCF project repositories first · [see all 409 with filters](https://lbarrosby.github.io/lbarrosby/)

<details open><summary><b>Official CNCF Graduated projects</b> · 13 merged in 6 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/Rook-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [helm: honor allowVolumeExpansion false on pool storage classes](https://github.com/rook/rook/pull/18802) | 2026-11-16 | [@travisn](https://github.com/travisn) |  |
| <img src="https://img.shields.io/badge/Kubernetes-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Kubernetes: official repository of a CNCF graduated project" title="Kubernetes: official repository of a CNCF graduated project"><br>[kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | [cloud-provider: validate --concurrent-service-syncs](https://github.com/kubernetes/kubernetes/pull/143991) | 2026-11-16 | bot |  |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [in_syslog: Treat a PRI above 191 as invalid](https://github.com/fluent/fluentd/pull/5635) | 2026-11-16 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5635#pullrequestreview-5913937246): <i>"Thanks for the fix."</i> |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [time: fix wrong %N/%L subseconds when EventTime and Integer times share a second](https://github.com/fluent/fluentd/pull/5634) | 2026-11-15 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5634#pullrequestreview-5884939807): <i>"Thanks for the clear report and the reproduction."</i> |
| <img src="https://img.shields.io/badge/Rook-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [helm: pass monitoring.metricsDisabled to the CephCluster](https://github.com/rook/rook/pull/18753) | 2026-11-13 | [@travisn](https://github.com/travisn) |  |
| <img src="https://img.shields.io/badge/Rook-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [helm: render CephBlockPool storage class labels as YAML](https://github.com/rook/rook/pull/18754) | 2026-11-13 | [@travisn](https://github.com/travisn) |  |
| <img src="https://img.shields.io/badge/Kubernetes-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Kubernetes: official repository of a CNCF graduated project" title="Kubernetes: official repository of a CNCF graduated project"><br>[kubernetes/cloud-provider-openstack](https://github.com/kubernetes/cloud-provider-openstack) | [[occm] Rename listener when its pool already has the new cluster-name](https://github.com/kubernetes/cloud-provider-openstack/pull/3283) | 2026-11-12 | bot |  |
| <img src="https://img.shields.io/badge/Karmada-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Karmada: official repository of a CNCF graduated project" title="Karmada: official repository of a CNCF graduated project"><br>[karmada-io/karmada](https://github.com/karmada-io/karmada) | [fix(resourceinterpreter): skip Ingress TLS entries without secretName in dependencies](https://github.com/karmada-io/karmada/pull/8029) | 2026-11-10 | [@karmada-bot](https://github.com/karmada-bot) | 🙏 [@zhzhuang-zju](https://github.com/karmada-io/karmada/pull/8029#issuecomment-6678810771): <i>"Thanks"</i> |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [in_tcp: fix inflated output emit_count when a message arrives in several reads](https://github.com/fluent/fluentd/pull/5608) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5608#pullrequestreview-5835281054): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/CoreDNS-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="CoreDNS: official repository of a CNCF graduated project" title="CoreDNS: official repository of a CNCF graduated project"><br>[coredns/coredns](https://github.com/coredns/coredns) | [plugin/acl: only add the EDE OPT record when the request has EDNS](https://github.com/coredns/coredns/pull/8749) | 2026-11-07 | [@yongtang](https://github.com/yongtang) |  |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [parser_syslog, in_syslog: fix handling of a priority on a later line](https://github.com/fluent/fluentd/pull/5598) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5598#pullrequestreview-5795032353): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/Fluentd-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [record_accessor: raise ConfigError for a non-integer array index](https://github.com/fluent/fluentd/pull/5596) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5596#pullrequestreview-5794474836): <i>"Thanks!"</i> |
| <img src="https://img.shields.io/badge/Rook-official%20·%20CNCF%20Graduated-0086FF?style=flat-square&logo=cncf&logoColor=white" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [osd: don't wipe metadata devices of existing OSDs](https://github.com/rook/rook/pull/18686) | 2026-11-05 | [@arttor](https://github.com/arttor) | 🙏 [@arttor](https://github.com/rook/rook/pull/18686#pullrequestreview-5789316361): <i>"thanks for the fix."</i> |

</details>

<details open><summary><b>Official CNCF Incubating projects</b> · 7 merged in 3 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/Lima-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [downloader: don't leave a partial file at the local path](https://github.com/lima-vm/lima/pull/5751) | 2026-11-15 | [@jandubois](https://github.com/jandubois) | 🙏 [@jandubois](https://github.com/lima-vm/lima/pull/5751#pullrequestreview-5908833280): <i>"Thanks, LGTM"</i> |
| <img src="https://img.shields.io/badge/Lima-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limatmpl: strip native arch aliases from image-derived instance names](https://github.com/lima-vm/lima/pull/5747) | 2026-11-15 | [@jandubois](https://github.com/jandubois) | 🙏 [@jandubois](https://github.com/lima-vm/lima/pull/5747#pullrequestreview-5908820167): <i>"Thanks, LGTM"</i> |
| <img src="https://img.shields.io/badge/OpenCost-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="OpenCost: official repository of a CNCF incubating project" title="OpenCost: official repository of a CNCF incubating project"><br>[opencost/opencost](https://github.com/opencost/opencost) | [fix(metrics): scale container_gpu_allocation on time-sliced and vGPU nodes](https://github.com/opencost/opencost/pull/4173) | 2026-11-13 | [@ameijer](https://github.com/ameijer) | 🙏 [@ameijer](https://github.com/opencost/opencost/pull/4173#pullrequestreview-5894171351): <i>"good catch!"</i> |
| <img src="https://img.shields.io/badge/OpenCost-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="OpenCost: official repository of a CNCF incubating project" title="OpenCost: official repository of a CNCF incubating project"><br>[opencost/opencost](https://github.com/opencost/opencost) | [fix(inferencecost): keep only grouped properties when aggregating](https://github.com/opencost/opencost/pull/4175) | 2026-11-10 | [@ameijer](https://github.com/ameijer) | 🙏 [@ameijer](https://github.com/opencost/opencost/pull/4175#pullrequestreview-5843570063): <i>"thank you cc @simanadler"</i> |
| <img src="https://img.shields.io/badge/Contour-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Contour: official repository of a CNCF incubating project" title="Contour: official repository of a CNCF incubating project"><br>[projectcontour/contour](https://github.com/projectcontour/contour) | [Set alt_stat_name for DNS name clusters](https://github.com/projectcontour/contour/pull/7821) | 2026-11-09 | [@tsaarni](https://github.com/tsaarni) | 🙏 [@tsaarni](https://github.com/projectcontour/contour/pull/7821#pullrequestreview-5803527120): <i>"Thank you for contributing!"</i> |
| <img src="https://img.shields.io/badge/Lima-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limactl edit: warn when changing the VM type of an existing instance](https://github.com/lima-vm/lima/pull/5743) | 2026-11-05 | [@AkihiroSuda](https://github.com/AkihiroSuda) |  |
| <img src="https://img.shields.io/badge/Lima-official%20·%20CNCF%20Incubating-8957E5?style=flat-square&logo=cncf&logoColor=white" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limayaml: don't panic when the latest config fails to load](https://github.com/lima-vm/lima/pull/5738) | 2026-11-05 | [@unsuman](https://github.com/unsuman) | 🙏 [@AkihiroSuda](https://github.com/lima-vm/lima/pull/5738#pullrequestreview-5784793825): <i>"Thanks"</i> |

</details>

<details open><summary><b>Official CNCF Sandbox projects</b> · 6 merged in 2 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="https://img.shields.io/badge/kube--vip-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="kube-vip: official repository of a CNCF sandbox project" title="kube-vip: official repository of a CNCF sandbox project"><br>[kube-vip/kube-vip](https://github.com/kube-vip/kube-vip) | [fix(kubevip): write log level, on-demand election and egress backend into manifests](https://github.com/kube-vip/kube-vip/pull/1861) | 2026-11-17 | [@Cellebyte](https://github.com/Cellebyte) |  |
| <img src="https://img.shields.io/badge/kube--vip-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="kube-vip: official repository of a CNCF sandbox project" title="kube-vip: official repository of a CNCF sandbox project"><br>[kube-vip/kube-vip](https://github.com/kube-vip/kube-vip) | [fix(services): do not treat DHCP placeholder VIPs as shared](https://github.com/kube-vip/kube-vip/pull/1838) | 2026-11-09 | [@Cellebyte](https://github.com/Cellebyte) |  |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [backend: auth: Accept a single string groups claim in /me](https://github.com/kubernetes-sigs/headlamp/pull/8262) | 2026-11-05 | [@skoeva](https://github.com/skoeva) | 🙏 [@skoeva](https://github.com/kubernetes-sigs/headlamp/pull/8262#pullrequestreview-5785420953): <i>"lgtm, thanks"</i> |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Resolve HTTPRoute parent and backend refs](https://github.com/kubernetes-sigs/headlamp/pull/8254) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: util: Use desired DaemonSet pods as the total](https://github.com/kubernetes-sigs/headlamp/pull/8259) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |
| <img src="https://img.shields.io/badge/Headlamp-official%20·%20CNCF%20Sandbox-6E7781?style=flat-square&logo=cncf&logoColor=white" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Match NetworkPolicy podSelector fully](https://github.com/kubernetes-sigs/headlamp/pull/8245) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |

</details>

<details><summary><b>Latest merges elsewhere</b> · 15 most recent of 383 (ecosystem, Terraform providers, Helm charts, tools)</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| [terraform-aws-modules/terraform-aws-iam](https://github.com/terraform-aws-modules/terraform-aws-iam) | [fix: Add `ec2:DescribeVpcPeeringConnections` to the LBC TargetGroupBinding only policy](https://github.com/terraform-aws-modules/terraform-aws-iam/pull/670) | 2026-11-17 | [@bryantbiggs](https://github.com/bryantbiggs) |  |
| [syself/cluster-api-provider-hetzner](https://github.com/syself/cluster-api-provider-hetzner) | [🐛 Return the actual error when deleting placement groups fails](https://github.com/syself/cluster-api-provider-hetzner/pull/2354) | 2026-11-17 | [@abdullah599](https://github.com/abdullah599) | 🙏 [@abdullah599](https://github.com/syself/cluster-api-provider-hetzner/pull/2354#pullrequestreview-5916569924): <i>"Thank you for your contribution!"</i> |
| [jenkinsci/explain-error-plugin](https://github.com/jenkinsci/explain-error-plugin) | [fix: keep the executable bit of files auto-fix modifies on GitHub](https://github.com/jenkinsci/explain-error-plugin/pull/276) | 2026-11-17 | [@shenxianpeng](https://github.com/shenxianpeng) |  |
| [jenkinsci/explain-error-plugin](https://github.com/jenkinsci/explain-error-plugin) | [fix: use the branch the SCM client created for the auto-fix](https://github.com/jenkinsci/explain-error-plugin/pull/275) | 2026-11-17 | [@shenxianpeng](https://github.com/shenxianpeng) |  |
| [jenkinsci/explain-error-plugin](https://github.com/jenkinsci/explain-error-plugin) | [fix: find the labels of a language given as a tag with a region](https://github.com/jenkinsci/explain-error-plugin/pull/274) | 2026-11-17 | [@shenxianpeng](https://github.com/shenxianpeng) | 🙏 [@shenxianpeng](https://github.com/jenkinsci/explain-error-plugin/pull/274#pullrequestreview-5938590638): <i>"Thanks for the PR！"</i> |
| [opentelekomcloud/terraform-provider-opentelekomcloud](https://github.com/opentelekomcloud/terraform-provider-opentelekomcloud) | [[Fix] VPCEP: remove deleted endpoints from state on read](https://github.com/opentelekomcloud/terraform-provider-opentelekomcloud/pull/3636) | 2026-11-17 | bot |  |
| [traefik/traefik-helm-chart](https://github.com/traefik/traefik-helm-chart) | [fix(poddisruptionbudget): keep minAvailable and maxUnavailable when set to 0](https://github.com/traefik/traefik-helm-chart/pull/2107) | 2026-11-17 | [@traefiker](https://github.com/traefiker) | 🙏 [@mloiseleur](https://github.com/traefik/traefik-helm-chart/pull/2107#pullrequestreview-5922009274): <i>"LGTM, thanks."</i> |
| [traefik/traefik-helm-chart](https://github.com/traefik/traefik-helm-chart) | [fix(daemonset): keep revisionHistoryLimit when set to 0](https://github.com/traefik/traefik-helm-chart/pull/2106) | 2026-11-17 | [@traefiker](https://github.com/traefiker) | 🙏 [@mloiseleur](https://github.com/traefik/traefik-helm-chart/pull/2106#pullrequestreview-5922008849): <i>"LGTM, thanks."</i> |
| [DataDog/terraform-provider-datadog](https://github.com/DataDog/terraform-provider-datadog) | [[datadog_tag_indexing_rule] Fix ValidateConfig error when options is unknown](https://github.com/DataDog/terraform-provider-datadog/pull/4517) | 2026-11-17 | bot | 🙏 [@fpighi](https://github.com/DataDog/terraform-provider-datadog/pull/4517#issuecomment-6943741011): <i>"No, thank you!"</i> |
| <img src="https://img.shields.io/badge/Kubernetes%20SIG%20subproject-not%20the%20main%20repo-555?style=flat-square" alt="Kubernetes SIG subproject: not the main Kubernetes repository" title="Kubernetes SIG subproject: not the main Kubernetes repository"><br>[kubernetes-sigs/node-feature-discovery](https://github.com/kubernetes-sigs/node-feature-discovery) | [fix(kernel): parse version components when the suffix starts with '+'](https://github.com/kubernetes-sigs/node-feature-discovery/pull/2663) | 2026-11-17 | bot | 🙏 [@ArangoGutierrez](https://github.com/kubernetes-sigs/node-feature-discovery/pull/2663#pullrequestreview-5935581060): <i>"Thanks for this, nodes running Debian 13 or Raspberry Pi OS kernels will now get the…"</i> |
| <img src="https://img.shields.io/badge/Kubernetes%20SIG%20subproject-not%20the%20main%20repo-555?style=flat-square" alt="Kubernetes SIG subproject: not the main Kubernetes repository" title="Kubernetes SIG subproject: not the main Kubernetes repository"><br>[kubernetes-sigs/node-feature-discovery](https://github.com/kubernetes-sigs/node-feature-discovery) | [fix(nodefeaturerule): evaluate each term with its own match result](https://github.com/kubernetes-sigs/node-feature-discovery/pull/2662) | 2026-11-17 | bot | 🙏 [@ArangoGutierrez](https://github.com/kubernetes-sigs/node-feature-discovery/pull/2662#pullrequestreview-5935571910): <i>"Thanks for this!"</i> |
| [ovh/terraform-provider-ovh](https://github.com/ovh/terraform-provider-ovh) | [fix(dedicated_server): remove deleted servers from the state](https://github.com/ovh/terraform-provider-ovh/pull/1597) | 2026-11-17 | [@amstuta](https://github.com/amstuta) | 🙏 [@amstuta](https://github.com/ovh/terraform-provider-ovh/pull/1597#pullrequestreview-5922591953): <i>"Thanks for your contribution!"</i> |
| [deliveryhero/helm-charts](https://github.com/deliveryhero/helm-charts) | [[stable/superset]: use superset.podAnnotations on the web Deployment and fix the worker HPA target](https://github.com/deliveryhero/helm-charts/pull/847) | 2026-11-17 | [@max-rocket-internet](https://github.com/max-rocket-internet) | 🙏 [@max-rocket-internet](https://github.com/deliveryhero/helm-charts/pull/847#pullrequestreview-5934855243): <i>"Thanks 💚"</i> |
| [CloudPirates-io/helm-charts](https://github.com/CloudPirates-io/helm-charts) | [[nginx] Accept an integer metrics.service.nodePort](https://github.com/CloudPirates-io/helm-charts/pull/1933) | 2026-11-17 | [@zOnlyKroks](https://github.com/zOnlyKroks) |  |
| [CloudPirates-io/helm-charts](https://github.com/CloudPirates-io/helm-charts) | [[mariadb] Accept an integer service.nodePort](https://github.com/CloudPirates-io/helm-charts/pull/1930) | 2026-11-17 | [@zOnlyKroks](https://github.com/zOnlyKroks) |  |

[All 383 of them, with filters](https://lbarrosby.github.io/lbarrosby/)

</details>

**In review** · 450 open pull requests · [browse and filter](https://lbarrosby.github.io/lbarrosby/)

- Official CNCF Graduated: 35 in 17 repos
- Official CNCF Incubating: 7 in 4 repos
- Official CNCF Sandbox: 15 in 6 repos
- CNCF ecosystem: 124 in 65 repos
- Other: 269 in 163 repos

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
