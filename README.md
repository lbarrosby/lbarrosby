### Lucas Barros

Based in Rio de Janeiro. I design and operate Kubernetes platforms for teams that ship to production every day, mostly in financial services.

Over the last years that meant running a fleet of 330 clusters behind ArgoCD, Atlantis and Rancher, turning EKS provisioning from a two-day manual process into a 40-minute Terraform/Terragrunt pipeline, moving a 3,000 jobs/day Jenkins farm to immutable infrastructure, and treating cloud cost as an engineering metric rather than a finance report.

I care about boring, predictable infrastructure: everything in code, every change reviewed, upgrades that nobody notices.

**Open source**

Contributing upstream across the cloud native ecosystem: CNCF projects like Kubernetes, Envoy, Prometheus, Argo, Crossplane, Headlamp and CoreDNS, plus Terraform providers, Helm charts and AI infrastructure tooling (NVIDIA device plugin, Ray, deepwiki-open).

<!--START_SECTION:activity-->
<a href="https://github.com/search?q=author%3Albarrosby+is%3Apr+is%3Amerged+org%3Akubernetes+org%3Akubernetes-sigs&type=pullrequests"><img src="badges/cdfb77d446ffc926.svg" alt="Merged in the Kubernetes project"></a><br><img src="badges/00124a43c8fe0af7.svg" alt="Upstream PRs"> <img src="badges/02cd0e35cedc0c6f.svg" alt="Merged"> <img src="badges/24dc85b513d6a318.svg" alt="Projects"> <img src="badges/009f701e2c07284f.svg" alt="Merged in repositories the CNCF lists for graduated projects"> <a href="https://lbarrosby.github.io/lbarrosby/"><img src="badges/6d7d221d62de220b.svg" alt="Filter and search all PRs"></a> <img src="badges/5bdfe0f26df2cc4f.svg" alt="Thanked by maintainers"> <a href="https://github.com/kubernetes/kubernetes/pulls?q=is%3Apr+author%3Albarrosby+is%3Amerged"><img src="badges/66875a619a3f6bd5.svg" alt="Merged in kubernetes/kubernetes"></a>

### <img src="https://raw.githubusercontent.com/kubernetes/kubernetes/master/logo/logo.svg" width="26" height="26" align="top" alt="Kubernetes"> Kubernetes

35 pull requests merged across 13 repositories of the Kubernetes project (`kubernetes` and `kubernetes-sigs`), reviewed and approved by Kubernetes maintainers.

| Repository | Pull request | Merged | Approved by |
|---|---|---|---|
| [kubernetes/autoscaler](https://github.com/kubernetes/autoscaler) <sub>official</sub> | [cluster-autoscaler/chart: keep PDB minAvailable/maxUnavailable with a custom selector](https://github.com/kubernetes/autoscaler/pull/10634) | 2026-11-25 |  |
| [kubernetes-sigs/jobset](https://github.com/kubernetes-sigs/jobset) <sub>SIG subproject</sub> | [Skip nodeSelector strategy pods in the exclusive placement pod reconciler](https://github.com/kubernetes-sigs/jobset/pull/1396) | 2026-11-18 | [@jianqiaol](https://github.com/jianqiaol) |
| [kubernetes-sigs/node-feature-discovery](https://github.com/kubernetes-sigs/node-feature-discovery) <sub>SIG subproject</sub> | [fix(kernel): parse version components when the suffix starts with '+'](https://github.com/kubernetes-sigs/node-feature-discovery/pull/2663) | 2026-11-17 |  |
| [kubernetes-sigs/node-feature-discovery](https://github.com/kubernetes-sigs/node-feature-discovery) <sub>SIG subproject</sub> | [fix(nodefeaturerule): evaluate each term with its own match result](https://github.com/kubernetes-sigs/node-feature-discovery/pull/2662) | 2026-11-17 |  |
| [kubernetes-sigs/cluster-inventory-api](https://github.com/kubernetes-sigs/cluster-inventory-api) <sub>SIG subproject</sub> | [access: do not panic on an empty additional-envs extension](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/100) | 2026-11-17 | [@kahirokunn](https://github.com/kahirokunn) |
| [kubernetes-sigs/jobset](https://github.com/kubernetes-sigs/jobset) <sub>SIG subproject</sub> | [Reject invalid onJobFailureMessagePatterns in the webhook](https://github.com/kubernetes-sigs/jobset/pull/1394) | 2026-11-16 | [@jianqiaol](https://github.com/jianqiaol), [@kannon92](https://github.com/kannon92) |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) <sub>SIG subproject</sub> | [fix(sandboxd): return 404 for a path under a regular file](https://github.com/kubernetes-sigs/agent-sandbox/pull/2220) | 2026-11-16 | [@aditya-shantanu](https://github.com/aditya-shantanu) |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) <sub>core</sub> | [cloud-provider: validate --concurrent-service-syncs](https://github.com/kubernetes/kubernetes/pull/143991) | 2026-11-16 | [@liggitt](https://github.com/liggitt) |
| [kubernetes-sigs/jobset](https://github.com/kubernetes-sigs/jobset) <sub>SIG subproject</sub> | [Update LastTransitionTime when an exclusive condition is set to False](https://github.com/kubernetes-sigs/jobset/pull/1398) | 2026-11-16 |  |
| [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) <sub>SIG subproject</sub> | [🐛 (go/v4): use k8s.io/api/rbac as the import path for the rbac.authorization core group](https://github.com/kubernetes-sigs/kubebuilder/pull/6167) | 2026-11-15 | [@camilamacedo86](https://github.com/camilamacedo86) |
| [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) <sub>SIG subproject</sub> | [🐛 (API): make the title template function in DefaultFuncMap usable](https://github.com/kubernetes-sigs/kubebuilder/pull/6166) | 2026-11-15 | [@camilamacedo86](https://github.com/camilamacedo86) |
| [kubernetes/cloud-provider-openstack](https://github.com/kubernetes/cloud-provider-openstack) <sub>official</sub> | [[occm] Rename listener when its pool already has the new cluster-name](https://github.com/kubernetes/cloud-provider-openstack/pull/3283) | 2026-11-12 |  |
| [kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver) <sub>SIG subproject</sub> | [Reject GPU sharing configs that set the other strategy's config](https://github.com/kubernetes-sigs/dra-example-driver/pull/298) | 2026-11-12 |  |
| [kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver) <sub>SIG subproject</sub> | [Remove the temp checkpoint file when writing the checkpoint fails](https://github.com/kubernetes-sigs/dra-example-driver/pull/297) | 2026-11-12 |  |
| [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) <sub>SIG subproject</sub> | [🐛 (helm/v2-alpha): keep the manager replicas from the kustomize manifest](https://github.com/kubernetes-sigs/kubebuilder/pull/6168) | 2026-11-11 | [@camilamacedo86](https://github.com/camilamacedo86) |
| [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) <sub>SIG subproject</sub> | [🐛 (API): return the error from closing a file written by the scaffold](https://github.com/kubernetes-sigs/kubebuilder/pull/6170) | 2026-11-11 | [@camilamacedo86](https://github.com/camilamacedo86) |
| [kubernetes-sigs/controller-tools](https://github.com/kubernetes-sigs/controller-tools) <sub>SIG subproject</sub> | [:bug: markers: parse bool-prefixed bare strings as strings](https://github.com/kubernetes-sigs/controller-tools/pull/1505) | 2026-11-11 | [@sbueringer](https://github.com/sbueringer) |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) <sub>SIG subproject</sub> | [fix(sandboxd): reject stdin EOF for a PTY process](https://github.com/kubernetes-sigs/agent-sandbox/pull/2225) | 2026-11-09 | [@aditya-shantanu](https://github.com/aditya-shantanu) |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) <sub>SIG subproject</sub> | [fix(go-sdk): report ErrSandboxDeleted only when the claim is gone](https://github.com/kubernetes-sigs/agent-sandbox/pull/2223) | 2026-11-09 | [@aditya-shantanu](https://github.com/aditya-shantanu) |
| [kubernetes-sigs/cluster-inventory-api](https://github.com/kubernetes-sigs/cluster-inventory-api) <sub>SIG subproject</sub> | [access: only set rest.Config.Proxy when the profile has a proxy URL](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/98) | 2026-11-09 | [@kahirokunn](https://github.com/kahirokunn) |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) <sub>SIG subproject</sub> | [fix(go-sdk): apply RequestTimeout to Run on sandboxd](https://github.com/kubernetes-sigs/agent-sandbox/pull/2221) | 2026-11-08 | [@aditya-shantanu](https://github.com/aditya-shantanu) |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) <sub>SIG subproject</sub> | [fix(sandboxd): delete a symlink itself, not its target](https://github.com/kubernetes-sigs/agent-sandbox/pull/2218) | 2026-11-08 | [@aditya-shantanu](https://github.com/aditya-shantanu) |
| [kubernetes-sigs/kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) <sub>SIG subproject</sub> | [🐛 (API): keep the target's line endings in UncommentCode and CommentCode](https://github.com/kubernetes-sigs/kubebuilder/pull/6160) | 2026-11-07 |  |
| [kubernetes-sigs/jobset](https://github.com/kubernetes-sigs/jobset) <sub>SIG subproject</sub> | [helm: default the ServiceMonitor client cert to the release's metrics secret](https://github.com/kubernetes-sigs/jobset/pull/1389) | 2026-11-07 | [@kannon92](https://github.com/kannon92) |
| [kubernetes-sigs/jobset](https://github.com/kubernetes-sigs/jobset) <sub>SIG subproject</sub> | [Reject a ReplicatedJob that depends on itself](https://github.com/kubernetes-sigs/jobset/pull/1392) | 2026-11-06 | [@kannon92](https://github.com/kannon92) |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) <sub>SIG subproject</sub> | [fix(sandbox-router): keep the request body open across dial retries](https://github.com/kubernetes-sigs/agent-sandbox/pull/2202) | 2026-11-06 | [@aditya-shantanu](https://github.com/aditya-shantanu) |
| [kubernetes-sigs/gateway-api-inference-extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) <sub>SIG subproject</sub> | [fix(lwepp): respond with 503 when no endpoint is eligible](https://github.com/kubernetes-sigs/gateway-api-inference-extension/pull/3084) | 2026-11-06 | [@nicolexin](https://github.com/nicolexin) |
| [kubernetes-sigs/external-dns](https://github.com/kubernetes-sigs/external-dns) <sub>SIG subproject</sub> | [refactor(validation): return field.ErrorList from config validators](https://github.com/kubernetes-sigs/external-dns/pull/6929) | 2026-11-06 | [@ivankatliarchuk](https://github.com/ivankatliarchuk) |
| [kubernetes-sigs/cluster-inventory-api](https://github.com/kubernetes-sigs/cluster-inventory-api) <sub>SIG subproject</sub> | [access: do not modify the provider exec config](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/93) | 2026-11-06 | [@kahirokunn](https://github.com/kahirokunn) |
| [kubernetes-sigs/cluster-inventory-api](https://github.com/kubernetes-sigs/cluster-inventory-api) <sub>SIG subproject</sub> | [access: sort profile-sourced exec env vars by name](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/96) | 2026-11-06 | [@kahirokunn](https://github.com/kahirokunn) |
| [kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver) <sub>SIG subproject</sub> | [Reject GPU sharing configs that omit the strategy config instead of panicking](https://github.com/kubernetes-sigs/dra-example-driver/pull/296) | 2026-11-05 |  |
| [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) <sub>SIG subproject</sub> | [backend: auth: Accept a single string groups claim in /me](https://github.com/kubernetes-sigs/headlamp/pull/8262) | 2026-11-05 | [@skoeva](https://github.com/skoeva) |
| [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) <sub>SIG subproject</sub> | [frontend: resourceMap: Resolve HTTPRoute parent and backend refs](https://github.com/kubernetes-sigs/headlamp/pull/8254) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |
| [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) <sub>SIG subproject</sub> | [frontend: util: Use desired DaemonSet pods as the total](https://github.com/kubernetes-sigs/headlamp/pull/8259) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |
| [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) <sub>SIG subproject</sub> | [frontend: resourceMap: Match NetworkPolicy podSelector fully](https://github.com/kubernetes-sigs/headlamp/pull/8245) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |

---

**Merged** · official CNCF project repositories first · [see all 528 with filters](https://lbarrosby.github.io/lbarrosby/)

<details open><summary><b>Official CNCF Graduated projects</b> · 19 merged in 8 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="badges/13186f79da2018f1.svg" alt="Kubernetes: official repository of a CNCF graduated project" title="Kubernetes: official repository of a CNCF graduated project"><br>[kubernetes/autoscaler](https://github.com/kubernetes/autoscaler) | [cluster-autoscaler/chart: keep PDB minAvailable/maxUnavailable with a custom selector](https://github.com/kubernetes/autoscaler/pull/10634) | 2026-11-25 | bot |  |
| <img src="badges/8f0673e820b2ef29.svg" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [helm: pass mapOptions and unmapOptions to EC pool storage classes](https://github.com/rook/rook/pull/18854) | 2026-11-23 | [@travisn](https://github.com/travisn) |  |
| <img src="badges/fd4069de81811b28.svg" alt="CoreDNS: official repository of a CNCF graduated project" title="CoreDNS: official repository of a CNCF graduated project"><br>[coredns/coredns](https://github.com/coredns/coredns) | [plugin/header: keep rules from every header block](https://github.com/coredns/coredns/pull/8746) | 2026-11-23 | [@mqasimsarfraz](https://github.com/mqasimsarfraz) | 🙏 [@mqasimsarfraz](https://github.com/coredns/coredns/pull/8746#pullrequestreview-5941853745): <i>"Thanks for addressing the comments, LGTM!"</i> |
| <img src="badges/8f0673e820b2ef29.svg" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [osd: requeue the disruption controller while a failure domain drains](https://github.com/rook/rook/pull/18752) | 2026-11-19 | [@sp98](https://github.com/sp98) |  |
| <img src="badges/ed3d1dd4865eb0d6.svg" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [config: parse a fractional number before a size or time unit](https://github.com/fluent/fluentd/pull/5625) | 2026-11-19 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5625#pullrequestreview-5839800958): <i>"Thanks for the PR and the clear description."</i> |
| <img src="badges/065aa6c1ca606d35.svg" alt="cert-manager: official repository of a CNCF graduated project" title="cert-manager: official repository of a CNCF graduated project"><br>[cert-manager/cert-manager](https://github.com/cert-manager/cert-manager) | [fix(pki): accept lowercase attribute type names in literalSubject](https://github.com/cert-manager/cert-manager/pull/9556) | 2026-11-17 | bot |  |
| <img src="badges/8f0673e820b2ef29.svg" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [helm: honor allowVolumeExpansion false on pool storage classes](https://github.com/rook/rook/pull/18802) | 2026-11-16 | [@travisn](https://github.com/travisn) |  |
| <img src="badges/13186f79da2018f1.svg" alt="Kubernetes: official repository of a CNCF graduated project" title="Kubernetes: official repository of a CNCF graduated project"><br>[kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | [cloud-provider: validate --concurrent-service-syncs](https://github.com/kubernetes/kubernetes/pull/143991) | 2026-11-16 | bot |  |
| <img src="badges/ed3d1dd4865eb0d6.svg" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [in_syslog: Treat a PRI above 191 as invalid](https://github.com/fluent/fluentd/pull/5635) | 2026-11-16 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5635#pullrequestreview-5913937246): <i>"Thanks for the fix."</i> |
| <img src="badges/ed3d1dd4865eb0d6.svg" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [time: fix wrong %N/%L subseconds when EventTime and Integer times share a second](https://github.com/fluent/fluentd/pull/5634) | 2026-11-15 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5634#pullrequestreview-5884939807): <i>"Thanks for the clear report and the reproduction."</i> |
| <img src="badges/8f0673e820b2ef29.svg" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [helm: pass monitoring.metricsDisabled to the CephCluster](https://github.com/rook/rook/pull/18753) | 2026-11-13 | [@travisn](https://github.com/travisn) |  |
| <img src="badges/8f0673e820b2ef29.svg" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [helm: render CephBlockPool storage class labels as YAML](https://github.com/rook/rook/pull/18754) | 2026-11-13 | [@travisn](https://github.com/travisn) |  |
| <img src="badges/13186f79da2018f1.svg" alt="Kubernetes: official repository of a CNCF graduated project" title="Kubernetes: official repository of a CNCF graduated project"><br>[kubernetes/cloud-provider-openstack](https://github.com/kubernetes/cloud-provider-openstack) | [[occm] Rename listener when its pool already has the new cluster-name](https://github.com/kubernetes/cloud-provider-openstack/pull/3283) | 2026-11-12 | bot |  |
| <img src="badges/2dff89346c0975e4.svg" alt="Karmada: official repository of a CNCF graduated project" title="Karmada: official repository of a CNCF graduated project"><br>[karmada-io/karmada](https://github.com/karmada-io/karmada) | [fix(resourceinterpreter): skip Ingress TLS entries without secretName in dependencies](https://github.com/karmada-io/karmada/pull/8029) | 2026-11-10 | [@karmada-bot](https://github.com/karmada-bot) | 🙏 [@zhzhuang-zju](https://github.com/karmada-io/karmada/pull/8029#issuecomment-6678810771): <i>"Thanks"</i> |
| <img src="badges/ed3d1dd4865eb0d6.svg" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [in_tcp: fix inflated output emit_count when a message arrives in several reads](https://github.com/fluent/fluentd/pull/5608) | 2026-11-10 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5608#pullrequestreview-5835281054): <i>"Thanks!"</i> |
| <img src="badges/fd4069de81811b28.svg" alt="CoreDNS: official repository of a CNCF graduated project" title="CoreDNS: official repository of a CNCF graduated project"><br>[coredns/coredns](https://github.com/coredns/coredns) | [plugin/acl: only add the EDE OPT record when the request has EDNS](https://github.com/coredns/coredns/pull/8749) | 2026-11-07 | [@yongtang](https://github.com/yongtang) |  |
| <img src="badges/ed3d1dd4865eb0d6.svg" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [parser_syslog, in_syslog: fix handling of a priority on a later line](https://github.com/fluent/fluentd/pull/5598) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5598#pullrequestreview-5795032353): <i>"Thanks!"</i> |
| <img src="badges/ed3d1dd4865eb0d6.svg" alt="Fluentd: official repository of a CNCF graduated project" title="Fluentd: official repository of a CNCF graduated project"><br>[fluent/fluentd](https://github.com/fluent/fluentd) | [record_accessor: raise ConfigError for a non-integer array index](https://github.com/fluent/fluentd/pull/5596) | 2026-11-06 | [@Watson1978](https://github.com/Watson1978) | 🙏 [@Watson1978](https://github.com/fluent/fluentd/pull/5596#pullrequestreview-5794474836): <i>"Thanks!"</i> |
| <img src="badges/8f0673e820b2ef29.svg" alt="Rook: official repository of a CNCF graduated project" title="Rook: official repository of a CNCF graduated project"><br>[rook/rook](https://github.com/rook/rook) | [osd: don't wipe metadata devices of existing OSDs](https://github.com/rook/rook/pull/18686) | 2026-11-05 | [@arttor](https://github.com/arttor) | 🙏 [@arttor](https://github.com/rook/rook/pull/18686#pullrequestreview-5789316361): <i>"thanks for the fix."</i> |

</details>

<details open><summary><b>Official CNCF Incubating projects</b> · 7 merged in 3 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="badges/a3d970d64c74f408.svg" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [downloader: don't leave a partial file at the local path](https://github.com/lima-vm/lima/pull/5751) | 2026-11-15 | [@jandubois](https://github.com/jandubois) | 🙏 [@jandubois](https://github.com/lima-vm/lima/pull/5751#pullrequestreview-5908833280): <i>"Thanks, LGTM"</i> |
| <img src="badges/a3d970d64c74f408.svg" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limatmpl: strip native arch aliases from image-derived instance names](https://github.com/lima-vm/lima/pull/5747) | 2026-11-15 | [@jandubois](https://github.com/jandubois) | 🙏 [@jandubois](https://github.com/lima-vm/lima/pull/5747#pullrequestreview-5908820167): <i>"Thanks, LGTM"</i> |
| <img src="badges/5d97640d55949dcd.svg" alt="OpenCost: official repository of a CNCF incubating project" title="OpenCost: official repository of a CNCF incubating project"><br>[opencost/opencost](https://github.com/opencost/opencost) | [fix(metrics): scale container_gpu_allocation on time-sliced and vGPU nodes](https://github.com/opencost/opencost/pull/4173) | 2026-11-13 | [@ameijer](https://github.com/ameijer) | 🙏 [@ameijer](https://github.com/opencost/opencost/pull/4173#pullrequestreview-5894171351): <i>"good catch!"</i> |
| <img src="badges/5d97640d55949dcd.svg" alt="OpenCost: official repository of a CNCF incubating project" title="OpenCost: official repository of a CNCF incubating project"><br>[opencost/opencost](https://github.com/opencost/opencost) | [fix(inferencecost): keep only grouped properties when aggregating](https://github.com/opencost/opencost/pull/4175) | 2026-11-10 | [@ameijer](https://github.com/ameijer) | 🙏 [@ameijer](https://github.com/opencost/opencost/pull/4175#pullrequestreview-5843570063): <i>"thank you cc @simanadler"</i> |
| <img src="badges/8f6922db595b1bff.svg" alt="Contour: official repository of a CNCF incubating project" title="Contour: official repository of a CNCF incubating project"><br>[projectcontour/contour](https://github.com/projectcontour/contour) | [Set alt_stat_name for DNS name clusters](https://github.com/projectcontour/contour/pull/7821) | 2026-11-09 | [@tsaarni](https://github.com/tsaarni) | 🙏 [@tsaarni](https://github.com/projectcontour/contour/pull/7821#pullrequestreview-5803527120): <i>"Thank you for contributing!"</i> |
| <img src="badges/a3d970d64c74f408.svg" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limactl edit: warn when changing the VM type of an existing instance](https://github.com/lima-vm/lima/pull/5743) | 2026-11-05 | [@AkihiroSuda](https://github.com/AkihiroSuda) |  |
| <img src="badges/a3d970d64c74f408.svg" alt="Lima: official repository of a CNCF incubating project" title="Lima: official repository of a CNCF incubating project"><br>[lima-vm/lima](https://github.com/lima-vm/lima) | [limayaml: don't panic when the latest config fails to load](https://github.com/lima-vm/lima/pull/5738) | 2026-11-05 | [@unsuman](https://github.com/unsuman) | 🙏 [@AkihiroSuda](https://github.com/lima-vm/lima/pull/5738#pullrequestreview-5784793825): <i>"Thanks"</i> |

</details>

<details open><summary><b>Official CNCF Sandbox projects</b> · 8 merged in 3 repos</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| <img src="badges/1544ca4e025b6e25.svg" alt="K8sGPT: official repository of a CNCF sandbox project" title="K8sGPT: official repository of a CNCF sandbox project"><br>[k8sgpt-ai/k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) | [fix: declare the limit parameter on the MCP list-resources tool](https://github.com/k8sgpt-ai/k8sgpt/pull/1923) | 2026-11-19 | [@AlexsJones](https://github.com/AlexsJones) | 🙏 [@AlexsJones](https://github.com/k8sgpt-ai/k8sgpt/pull/1923#pullrequestreview-5810724055): <i>"Nice find, : the handler already binds limit, so this is the missing half rather than…"</i> |
| <img src="badges/1544ca4e025b6e25.svg" alt="K8sGPT: official repository of a CNCF sandbox project" title="K8sGPT: official repository of a CNCF sandbox project"><br>[k8sgpt-ai/k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) | [fix: require a namespace for namespaced kinds in MCP get-resource](https://github.com/k8sgpt-ai/k8sgpt/pull/1924) | 2026-11-17 | [@AlexsJones](https://github.com/AlexsJones) | 🙏 [@AlexsJones](https://github.com/k8sgpt-ai/k8sgpt/pull/1924#pullrequestreview-5810724210): <i>"Good catch, : a 404 that reads like 'the pod doesn't exist' is exactly the kind of…"</i> |
| <img src="badges/acabcf4c9fd668a4.svg" alt="kube-vip: official repository of a CNCF sandbox project" title="kube-vip: official repository of a CNCF sandbox project"><br>[kube-vip/kube-vip](https://github.com/kube-vip/kube-vip) | [fix(kubevip): write log level, on-demand election and egress backend into manifests](https://github.com/kube-vip/kube-vip/pull/1861) | 2026-11-17 | [@Cellebyte](https://github.com/Cellebyte) |  |
| <img src="badges/acabcf4c9fd668a4.svg" alt="kube-vip: official repository of a CNCF sandbox project" title="kube-vip: official repository of a CNCF sandbox project"><br>[kube-vip/kube-vip](https://github.com/kube-vip/kube-vip) | [fix(services): do not treat DHCP placeholder VIPs as shared](https://github.com/kube-vip/kube-vip/pull/1838) | 2026-11-09 | [@Cellebyte](https://github.com/Cellebyte) |  |
| <img src="badges/a68a46f27a4ecda8.svg" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [backend: auth: Accept a single string groups claim in /me](https://github.com/kubernetes-sigs/headlamp/pull/8262) | 2026-11-05 | [@skoeva](https://github.com/skoeva) | 🙏 [@skoeva](https://github.com/kubernetes-sigs/headlamp/pull/8262#pullrequestreview-5785420953): <i>"lgtm, thanks"</i> |
| <img src="badges/a68a46f27a4ecda8.svg" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Resolve HTTPRoute parent and backend refs](https://github.com/kubernetes-sigs/headlamp/pull/8254) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |
| <img src="badges/a68a46f27a4ecda8.svg" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: util: Use desired DaemonSet pods as the total](https://github.com/kubernetes-sigs/headlamp/pull/8259) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |
| <img src="badges/a68a46f27a4ecda8.svg" alt="Headlamp: official repository of a CNCF sandbox project" title="Headlamp: official repository of a CNCF sandbox project"><br>[kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Match NetworkPolicy podSelector fully](https://github.com/kubernetes-sigs/headlamp/pull/8245) | 2026-11-04 | [@skoeva](https://github.com/skoeva) |  |

</details>

<details><summary><b>Latest merges elsewhere</b> · 15 most recent of 494 (ecosystem, Terraform providers, Helm charts, tools)</summary>

| Project | Pull request | Merged | Merged by | Kind words |
|---|---|---|---|---|
| [bpg/terraform-provider-proxmox](https://github.com/bpg/terraform-provider-proxmox) | [fix(vm): keep a cloned VM in state when a later create step fails](https://github.com/bpg/terraform-provider-proxmox/pull/3342) | 2026-11-28 | [@bpg-dev](https://github.com/bpg-dev) | 🙏 [@bpg-dev](https://github.com/bpg/terraform-provider-proxmox/pull/3342#pullrequestreview-6099068515): <i>"Thanks a lot for the fix!"</i> |
| [openlit/openlit](https://github.com/openlit/openlit) | [fix(go-sdk): read chat and embedding prices from assets/pricing.json](https://github.com/openlit/openlit/pull/1924) | 2026-11-28 | [@AmanAgarwal041](https://github.com/AmanAgarwal041) |  |
| [adriannovegil/awesome-observability](https://github.com/adriannovegil/awesome-observability) | [Add OpenTelemetry eBPF Instrumentation to Tracing](https://github.com/adriannovegil/awesome-observability/pull/214) | 2026-11-28 | [@adriannovegil](https://github.com/adriannovegil) | 🙏 [@adriannovegil](https://github.com/adriannovegil/awesome-observability/pull/214#issuecomment-7238391857): <i>"Thanks for the contribution — merged and included in the list."</i> |
| [adriannovegil/awesome-observability](https://github.com/adriannovegil/awesome-observability) | [Add Uptime Kuma to Uptime](https://github.com/adriannovegil/awesome-observability/pull/213) | 2026-11-28 | [@adriannovegil](https://github.com/adriannovegil) | 🙏 [@adriannovegil](https://github.com/adriannovegil/awesome-observability/pull/213#issuecomment-7238391661): <i>"Thanks for the contribution — merged and included in the list."</i> |
| [adriannovegil/awesome-observability](https://github.com/adriannovegil/awesome-observability) | [Add Pyrra to Alerts](https://github.com/adriannovegil/awesome-observability/pull/209) | 2026-11-28 | [@adriannovegil](https://github.com/adriannovegil) | 🙏 [@adriannovegil](https://github.com/adriannovegil/awesome-observability/pull/209#issuecomment-7238391181): <i>"Thanks for the contribution — merged and included in the list."</i> |
| [adriannovegil/awesome-observability](https://github.com/adriannovegil/awesome-observability) | [Add OpenObserve to APM](https://github.com/adriannovegil/awesome-observability/pull/208) | 2026-11-28 | [@adriannovegil](https://github.com/adriannovegil) | 🙏 [@adriannovegil](https://github.com/adriannovegil/awesome-observability/pull/208#issuecomment-7238390993): <i>"Thanks for the contribution — merged and included in the list."</i> |
| <img src="badges/fec5b9ebc5575a4c.svg" alt="KEDA ecosystem: not the main KEDA repository" title="KEDA ecosystem: not the main KEDA repository"><br>[kedacore/http-add-on](https://github.com/kedacore/http-add-on) | [fix(interceptor): fall back to shorter path when route headers do not match](https://github.com/kedacore/http-add-on/pull/1834) | 2026-11-27 | [@linkvt](https://github.com/linkvt) | 🙏 [@linkvt](https://github.com/kedacore/http-add-on/pull/1834#pullrequestreview-5825332556): <i>"Thank you that's a great finding, I only have one comment to improve the test but…"</i> |
| <img src="badges/c8d3be1688bb4bdb.svg" alt="Harbor ecosystem: not the main Harbor repository" title="Harbor ecosystem: not the main Harbor repository"><br>[goharbor/terraform-provider-harbor](https://github.com/goharbor/terraform-provider-harbor) | [fix: remove harbor_user from state when the user no longer exists](https://github.com/goharbor/terraform-provider-harbor/pull/667) | 2026-11-27 | [@flbla](https://github.com/flbla) |  |
| <img src="badges/c8d3be1688bb4bdb.svg" alt="Harbor ecosystem: not the main Harbor repository" title="Harbor ecosystem: not the main Harbor repository"><br>[goharbor/terraform-provider-harbor](https://github.com/goharbor/terraform-provider-harbor) | [fix(project_member_user): return update errors and read member_id](https://github.com/goharbor/terraform-provider-harbor/pull/668) | 2026-11-27 | [@flbla](https://github.com/flbla) |  |
| <img src="badges/c8d3be1688bb4bdb.svg" alt="Harbor ecosystem: not the main Harbor repository" title="Harbor ecosystem: not the main Harbor repository"><br>[goharbor/terraform-provider-harbor](https://github.com/goharbor/terraform-provider-harbor) | [fix(#650): retention policy replaced on every plan when scope is a plain project ID](https://github.com/goharbor/terraform-provider-harbor/pull/666) | 2026-11-27 | [@flbla](https://github.com/flbla) |  |
| [jenkinsci/mcp-server-plugin](https://github.com/jenkinsci/mcp-server-plugin) | [Count open SSE and Streamable HTTP clients in /mcp-health activeConnections](https://github.com/jenkinsci/mcp-server-plugin/pull/293) | 2026-11-26 | [@olamy](https://github.com/olamy) |  |
| [elastic/terraform-provider-ec](https://github.com/elastic/terraform-provider-ec) | [Send search_lake data_retention for ec_security_project](https://github.com/elastic/terraform-provider-ec/pull/1125) | 2026-11-26 | [@dimuon](https://github.com/dimuon) | 🙏 [@dimuon](https://github.com/elastic/terraform-provider-ec/pull/1125#pullrequestreview-6072046228): <i>"Thanks for addressing this"</i> |
| [ansible-collections/community.proxmox](https://github.com/ansible-collections/community.proxmox) | [fix(proxmox_user): compare groups regardless of order](https://github.com/ansible-collections/community.proxmox/pull/568) | 2026-11-26 | [@IamLunchbox](https://github.com/IamLunchbox) |  |
| [ansible-collections/community.proxmox](https://github.com/ansible-collections/community.proxmox) | [fix(proxmox_backup_schedule): handle jobs without a vmid list](https://github.com/ansible-collections/community.proxmox/pull/567) | 2026-11-26 | [@IamLunchbox](https://github.com/IamLunchbox) |  |
| [ansible-collections/community.proxmox](https://github.com/ansible-collections/community.proxmox) | [fix: treat tasks that end with warnings as successful](https://github.com/ansible-collections/community.proxmox/pull/566) | 2026-11-26 | [@IamLunchbox](https://github.com/IamLunchbox) |  |

[All 494 of them, with filters](https://lbarrosby.github.io/lbarrosby/)

</details>

**In review** · 378 open pull requests · [browse and filter](https://lbarrosby.github.io/lbarrosby/)

- Official CNCF Graduated: 31 in 15 repos
- Official CNCF Incubating: 7 in 4 repos
- Official CNCF Sandbox: 13 in 5 repos
- CNCF ecosystem: 117 in 60 repos
- Other: 210 in 133 repos

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
