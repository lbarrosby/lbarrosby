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
<img src="https://img.shields.io/badge/upstream%20PRs-166-1F6FEB?style=flat-square" alt="Upstream PRs"> <img src="https://img.shields.io/badge/merged-23-8957E5?style=flat-square" alt="Merged"> <img src="https://img.shields.io/badge/projects-99-2EA043?style=flat-square" alt="Projects">

**Merged**

- [prometheus-community/helm-charts](https://github.com/prometheus-community/helm-charts): [[prometheus-blackbox-exporter] Set port names on self ServiceMonitor endpoints](https://github.com/prometheus-community/helm-charts/pull/7518)
- [prometheus-community/helm-charts](https://github.com/prometheus-community/helm-charts): [[prometheus-operator-admission-webhook] Fix serviceMonitor.metricRelabelings value name](https://github.com/prometheus-community/helm-charts/pull/7507)
- [rook/rook](https://github.com/rook/rook): [osd: don't wipe metadata devices of existing OSDs](https://github.com/rook/rook/pull/18686)
- [aminueza/terraform-provider-minio](https://github.com/aminueza/terraform-provider-minio): [fix(replication): reject two rules on the same target endpoint](https://github.com/aminueza/terraform-provider-minio/pull/1262)
- [kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver): [Reject GPU sharing configs that omit the strategy config instead of panicking](https://github.com/kubernetes-sigs/dra-example-driver/pull/296)
- [lima-vm/lima](https://github.com/lima-vm/lima): [limactl edit: warn when changing the VM type of an existing instance](https://github.com/lima-vm/lima/pull/5743)
- [lima-vm/lima](https://github.com/lima-vm/lima): [limayaml: don't panic when the latest config fails to load](https://github.com/lima-vm/lima/pull/5738)
- [sergelogvinov/proxmox-cloud-controller-manager](https://github.com/sergelogvinov/proxmox-cloud-controller-manager): [fix: remove the right addresses when several are ignored](https://github.com/sergelogvinov/proxmox-cloud-controller-manager/pull/350)
- [fluent/fluent-plugin-kafka](https://github.com/fluent/fluent-plugin-kafka): [out_kafka2: Unsubscribe ActiveSupport notifications on shutdown](https://github.com/fluent/fluent-plugin-kafka/pull/601)
- [sergelogvinov/proxmox-cloud-controller-manager](https://github.com/sergelogvinov/proxmox-cloud-controller-manager): [fix: keep ip_sort_order cidrs out of the ignore list](https://github.com/sergelogvinov/proxmox-cloud-controller-manager/pull/349)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [backend: auth: Accept a single string groups claim in /me](https://github.com/kubernetes-sigs/headlamp/pull/8262)
- [tsuru/charts](https://github.com/tsuru/charts): [fix(tsuru-prometheus-pool): honor securityContext from values](https://github.com/tsuru/charts/pull/53)
- [tsuru/charts](https://github.com/tsuru/charts): [ci: publish charts as OCI artifacts to GHCR](https://github.com/tsuru/charts/pull/55)
- [openebs/lvm-localpv](https://github.com/openebs/lvm-localpv): [feat(chart): allow extra args for the controller CSI sidecars](https://github.com/openebs/lvm-localpv/pull/528)
- [fluent/fluent-plugin-kafka](https://github.com/fluent/fluent-plugin-kafka): [in_kafka_group, in_rdkafka_group: Fix records skipped with time_source record](https://github.com/fluent/fluent-plugin-kafka/pull/598)
- [hetznercloud/hcloud-cloud-controller-manager](https://github.com/hetznercloud/hcloud-cloud-controller-manager): [fix(load-balancer): trim spaces in comma separated annotations](https://github.com/hetznercloud/hcloud-cloud-controller-manager/pull/1411)
- [openobserve/openobserve-helm-chart](https://github.com/openobserve/openobserve-helm-chart): [fix(openobserve-collector): apply image.pullPolicy to the collectors](https://github.com/openobserve/openobserve-helm-chart/pull/286)
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open): [feat: add Helm chart](https://github.com/AsyncFuncAI/deepwiki-open/pull/621)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: resourceMap: Resolve HTTPRoute parent and backend refs](https://github.com/kubernetes-sigs/headlamp/pull/8254)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: util: Use desired DaemonSet pods as the total](https://github.com/kubernetes-sigs/headlamp/pull/8259)
- [tsuru/tsuru-client](https://github.com/tsuru/tsuru-client): [fix: keep the current target in sync on target update](https://github.com/tsuru/tsuru-client/pull/283)
- [coredns/helm](https://github.com/coredns/helm): [docs: note that the ServiceMonitor needs the metrics Service](https://github.com/coredns/helm/pull/288)
- [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp): [frontend: resourceMap: Match NetworkPolicy podSelector fully](https://github.com/kubernetes-sigs/headlamp/pull/8245)

**In review**

| Project | Pull requests |
|---|---|
| [prometheus-community/helm-charts](https://github.com/prometheus-community/helm-charts) | [[prometheus-systemd-exporter] Render env values in the DaemonSet](https://github.com/prometheus-community/helm-charts/pull/7525)<br>[[alertmanager-snmp-notifier] Honor namespaceOverride on all resources](https://github.com/prometheus-community/helm-charts/pull/7509)<br>[[prometheus-pgbouncer-exporter] Pass config.extraArgs to the exporter](https://github.com/prometheus-community/helm-charts/pull/7505) |
| [aminueza/terraform-provider-minio](https://github.com/aminueza/terraform-provider-minio) | [fix(replication): change a rule's target bucket on the same endpoint](https://github.com/aminueza/terraform-provider-minio/pull/1264)<br>[fix(replication): set the ID before removing unused remote targets](https://github.com/aminueza/terraform-provider-minio/pull/1263) |
| [knative/eventing](https://github.com/knative/eventing) | [fix(trigger): track the subscriber with the Trigger as observer](https://github.com/knative/eventing/pull/9509) |
| [falcosecurity/falcosidekick](https://github.com/falcosecurity/falcosidekick) | [fix(handlers): skip outputs whose client was not created](https://github.com/falcosecurity/falcosidekick/pull/1478) |
| [karmada-io/karmada](https://github.com/karmada-io/karmada) | [fix(resourceinterpreter): skip Ingress TLS entries without secretName in dependencies](https://github.com/karmada-io/karmada/pull/8029) |
| [etcd-io/auger](https://github.com/etcd-io/auger) | [Skip tombstone revisions when listing key summaries](https://github.com/etcd-io/auger/pull/540) |
| [dapr/components-contrib](https://github.com/dapr/components-contrib) | [fix(state/redis): return empty results instead of an error when a query matches nothing](https://github.com/dapr/components-contrib/pull/4742) |
| [lima-vm/lima](https://github.com/lima-vm/lima) | [limatmpl: strip native arch aliases from image-derived instance names](https://github.com/lima-vm/lima/pull/5747)<br>[guestagent: don't run kubectl when no kubeconfig is found](https://github.com/lima-vm/lima/pull/5746) |
| [projectcontour/contour](https://github.com/projectcontour/contour) | [Set alt_stat_name for DNS name clusters](https://github.com/projectcontour/contour/pull/7821) |
| [DataDog/integrations-extras](https://github.com/DataDog/integrations-extras) | [Add vLLM Production Stack integration](https://github.com/DataDog/integrations-extras/pull/3272)<br>[Add Volcano integration](https://github.com/DataDog/integrations-extras/pull/3271)<br>[Add Hugging Face TEI integration](https://github.com/DataDog/integrations-extras/pull/3270)<br>[Add llama.cpp integration](https://github.com/DataDog/integrations-extras/pull/3269) |
| [kubernetes-sigs/aws-ebs-csi-driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) | [Honor leaderElection values for csi-resizer and allow lease tuning in the chart schema](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/3101) |
| [argoproj/argo-helm](https://github.com/argoproj/argo-helm) | [fix(argocd-image-updater): mount the secret created by certificateSecret](https://github.com/argoproj/argo-helm/pull/4207)<br>[fix(argo-cd): render server.service.externalIPs as a list](https://github.com/argoproj/argo-helm/pull/4206)<br>[fix(argocd-image-updater): Allow webhook port in NetworkPolicy when service.enabled is set](https://github.com/argoproj/argo-helm/pull/4204) |
| [sergelogvinov/proxmox-csi-plugin](https://github.com/sergelogvinov/proxmox-csi-plugin) | [docs: explain why volume snapshots need the root@pam password](https://github.com/sergelogvinov/proxmox-csi-plugin/pull/687) |
| [goharbor/terraform-provider-harbor](https://github.com/goharbor/terraform-provider-harbor) | [fix(#650): retention policy replaced on every plan when scope is a plain project ID](https://github.com/goharbor/terraform-provider-harbor/pull/666) |
| [tsuru/terraform-provider-tsuru](https://github.com/tsuru/terraform-provider-tsuru) | [fix: reject malformed import IDs for tsuru_cluster_pool and tsuru_pool_constraint](https://github.com/tsuru/terraform-provider-tsuru/pull/106)<br>[fix: report non-API errors from retried tsuru calls](https://github.com/tsuru/terraform-provider-tsuru/pull/105)<br>[feat: add tsuru_pool data source](https://github.com/tsuru/terraform-provider-tsuru/pull/102)<br>[fix: drop tsuru_app_cname and tsuru_app_router from state when removed outside terraform](https://github.com/tsuru/terraform-provider-tsuru/pull/98) |
| [fluent/fluentd](https://github.com/fluent/fluentd) | [record_accessor: raise ConfigError for a non-integer array index](https://github.com/fluent/fluentd/pull/5596) |
| [tsuru/nginx-operator](https://github.com/tsuru/nginx-operator) | [fix: don't panic updating an ingress when nginx sets no ingress annotations](https://github.com/tsuru/nginx-operator/pull/59) |
| [scaleway/terraform-provider-scaleway](https://github.com/scaleway/terraform-provider-scaleway) | [fix: #4587 accept offer-specific private network options on baremetal servers](https://github.com/scaleway/terraform-provider-scaleway/pull/4590) |
| [tsuru/deploy-agent](https://github.com/tsuru/deploy-agent) | [fix: return an error instead of panicking on a truncated build context archive](https://github.com/tsuru/deploy-agent/pull/58) |
| [tsuru/charts](https://github.com/tsuru/charts) | [fix(tsuru-prometheus-pool): select pods by the release's Prometheus name](https://github.com/tsuru/charts/pull/57) |
| [fluent/fluent-operator](https://github.com/fluent/fluent-operator) | [fix(helm): use the buffer scope in the Fluentd OpenSearch output](https://github.com/fluent/fluent-operator/pull/2115)<br>[fix(helm): honor logstashFormat: false in the Fluentd ES and OpenSearch outputs](https://github.com/fluent/fluent-operator/pull/2114)<br>[fix(helm): honor logstashFormat: false in the Elasticsearch ClusterOutput](https://github.com/fluent/fluent-operator/pull/2113) |
| [coredns/coredns](https://github.com/coredns/coredns) | [plugin/acl: only add the EDE OPT record when the request has EDNS](https://github.com/coredns/coredns/pull/8749)<br>[plugin/header: keep rules from every header block](https://github.com/coredns/coredns/pull/8746) |
| [openebs/lvm-localpv](https://github.com/openebs/lvm-localpv) | [fix(chart): render lvmNode and lvmController labels](https://github.com/openebs/lvm-localpv/pull/534) |
| [openebs/zfs-localpv](https://github.com/openebs/zfs-localpv) | [fix(helm): render zfsNode and zfsController updateStrategy](https://github.com/openebs/zfs-localpv/pull/791) |
| [openobserve/terraform-provider-openobserve](https://github.com/openobserve/terraform-provider-openobserve) | [fix: keep the configured JSON text when the server document matches](https://github.com/openobserve/terraform-provider-openobserve/pull/17) |
| [openobserve/openobserve-helm-chart](https://github.com/openobserve/openobserve-helm-chart) | [fix(openobserve,openobserve-standalone): pass group, kind and port to HTTPRoute parentRefs](https://github.com/openobserve/openobserve-helm-chart/pull/289)<br>[fix(openobserve): honor postgres.spec.enableSuperuserAccess](https://github.com/openobserve/openobserve-helm-chart/pull/288) |
| [tsuru/tsuru-client](https://github.com/tsuru/tsuru-client) | [fix(metadata): accept the -t type in any case](https://github.com/tsuru/tsuru-client/pull/288)<br>[chore(docker): bump runtime image to alpine 3.24.3](https://github.com/tsuru/tsuru-client/pull/286)<br>[fix: print an empty JSON array for empty lists with --json](https://github.com/tsuru/tsuru-client/pull/285) |
| [tsuru/tsuru](https://github.com/tsuru/tsuru) | [fix(api): return 400 when creating a team token with an invalid token_id](https://github.com/tsuru/tsuru/pull/2936)<br>[ci: pin third-party actions to commit SHAs and restrict token permissions](https://github.com/tsuru/tsuru/pull/2934)<br>[fix(api): return 409 when creating a team token with an existing token_id](https://github.com/tsuru/tsuru/pull/2933) |
| [Mongey/terraform-provider-kafka](https://github.com/Mongey/terraform-provider-kafka) | [Support importing kafka_quota](https://github.com/Mongey/terraform-provider-kafka/pull/690) |
| [vultr/terraform-provider-vultr](https://github.com/vultr/terraform-provider-vultr) | [Mark credential attributes as sensitive](https://github.com/vultr/terraform-provider-vultr/pull/811)<br>[Remove database sub-resources from state when the database is gone](https://github.com/vultr/terraform-provider-vultr/pull/810) |
| [digitalocean/terraform-provider-digitalocean](https://github.com/digitalocean/terraform-provider-digitalocean) | [spaces: remove bucket CORS configuration from state when it is gone](https://github.com/digitalocean/terraform-provider-digitalocean/pull/1633) |
| [kubernetes-sigs/cluster-inventory-api](https://github.com/kubernetes-sigs/cluster-inventory-api) | [access: sort profile-sourced exec env vars by name](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/96)<br>[access: do not modify the provider exec config](https://github.com/kubernetes-sigs/cluster-inventory-api/pull/93) |
| [exoscale/terraform-provider-exoscale](https://github.com/exoscale/terraform-provider-exoscale) | [fix(block_storage_volume_snapshot): remove from state when deleted outside of Terraform](https://github.com/exoscale/terraform-provider-exoscale/pull/642) |
| [kubernetes-sigs/e2e-framework](https://github.com/kubernetes-sigs/e2e-framework) | [conditions: wait for observed generation in DaemonSetReady](https://github.com/kubernetes-sigs/e2e-framework/pull/607)<br>[utils: use go env to find the go install directory](https://github.com/kubernetes-sigs/e2e-framework/pull/605)<br>[watcher: stop the event loop when the watch ends](https://github.com/kubernetes-sigs/e2e-framework/pull/603) |
| [cert-manager/cert-manager](https://github.com/cert-manager/cert-manager) | [fix(pki): accept lowercase attribute type names in literalSubject](https://github.com/cert-manager/cert-manager/pull/9556) |
| [metallb/metallb](https://github.com/metallb/metallb) | [config: detect duplicate BGPPeers that only differ by name](https://github.com/metallb/metallb/pull/3182) |
| [stakater/Reloader](https://github.com/stakater/Reloader) | [fix(handler): treat non-2xx --webhook-url responses as failures](https://github.com/stakater/Reloader/pull/1269) |
| [aws/aws-cli](https://github.com/aws/aws-cli) | [Write JSON file cache entries atomically](https://github.com/aws/aws-cli/pull/10856) |
| [cloudflare/cfssl](https://github.com/cloudflare/cfssl) | [signer: trim spaces and skip empty entries in SplitHosts](https://github.com/cloudflare/cfssl/pull/1463) |
| [awslabs/eks-node-viewer](https://github.com/awslabs/eks-node-viewer) | [fix: update node usage when a bound pod's requests change](https://github.com/awslabs/eks-node-viewer/pull/547) |
| [bitnami/sealed-secrets](https://github.com/bitnami/sealed-secrets) | [fix(kubeseal): fail on malformed documents instead of skipping them](https://github.com/bitnami/sealed-secrets/pull/2097)<br>[fix(helm): use the container ports in the NetworkPolicy ingress rule](https://github.com/bitnami/sealed-secrets/pull/2096) |
| [istio/istio](https://github.com/istio/istio) | [gateway: honor exportTo when resolving Hostname backendRefs](https://github.com/istio/istio/pull/62659) |
| [otwld/ollama-helm](https://github.com/otwld/ollama-helm) | [fix: keep service ipFamilies inside the non-Knative Service](https://github.com/otwld/ollama-helm/pull/296)<br>[fix: allow revisionHistoryLimit to be set to 0](https://github.com/otwld/ollama-helm/pull/295) |
| [kubernetes-sigs/kwok](https://github.com/kubernetes-sigs/kwok) | [heap: update the key when pushing an existing item](https://github.com/kubernetes-sigs/kwok/pull/1801) |
| [open-webui/helm-charts](https://github.com/open-webui/helm-charts) | [fix(terminals): match operator labels in default terminalPodSelector](https://github.com/open-webui/helm-charts/pull/459) |
| [aziontech/lib](https://github.com/aziontech/lib) | [fix(utils): keep '=' in cookie values in parseRequest](https://github.com/aziontech/lib/pull/495)<br>[fix(utils): treat paths with a dot in a parent segment as routes](https://github.com/aziontech/lib/pull/494)<br>[fix(cookies): emit Max-Age=0 when maxAge is 0](https://github.com/aziontech/lib/pull/493)<br>[fix(cookies): keep '=' in cookie values when parsing](https://github.com/aziontech/lib/pull/492) |
| [runatlantis/atlantis](https://github.com/runatlantis/atlantis) | [fix: read pre-v0.44.0 pull records with int policy approvals](https://github.com/runatlantis/atlantis/pull/7059)<br>[fix: reject targeted plan for a missing dir before creating its status](https://github.com/runatlantis/atlantis/pull/7055) |
| [MagaluCloud/mgc-sdk-go](https://github.com/MagaluCloud/mgc-sdk-go) | [fix(client): let errors.Is/As see the error wrapped by RetryError](https://github.com/MagaluCloud/mgc-sdk-go/pull/198)<br>[fix(http): always send the request when MaxAttempts is zero or negative](https://github.com/MagaluCloud/mgc-sdk-go/pull/197) |
| [MagaluCloud/terraform-provider-mgc](https://github.com/MagaluCloud/terraform-provider-mgc) | [fix(blockstorage): remove volume from state when it no longer exists](https://github.com/MagaluCloud/terraform-provider-mgc/pull/329)<br>[fix(vm): remove instance from state when it no longer exists](https://github.com/MagaluCloud/terraform-provider-mgc/pull/328) |
| [ansible-collections/community.proxmox](https://github.com/ansible-collections/community.proxmox) | [fix(proxmox_kvm): return newid when the clone target already exists](https://github.com/ansible-collections/community.proxmox/pull/559) |
| [bpg/terraform-provider-proxmox](https://github.com/bpg/terraform-provider-proxmox) | [fix(acme): remove dns plugin from state when deleted outside terraform](https://github.com/bpg/terraform-provider-proxmox/pull/3259)<br>[fix(vm): read back usb4 and higher host USB devices](https://github.com/bpg/terraform-provider-proxmox/pull/3258) |
| [hetznercloud/hcloud-go](https://github.com/hetznercloud/hcloud-go) | [fix(exp): escape backslashes in TXT records and keep escapes in one chunk](https://github.com/hetznercloud/hcloud-go/pull/963) |
| [hetznercloud/terraform-provider-hcloud](https://github.com/hetznercloud/terraform-provider-hcloud) | [fix(server): do not delete primary ip already assigned to the server](https://github.com/hetznercloud/terraform-provider-hcloud/pull/1558) |
| [helmfile/helmfile](https://github.com/helmfile/helmfile) | [fix: keep elements added to an existing array by --state-values-set](https://github.com/helmfile/helmfile/pull/2873) |
| [aws-ia/terraform-aws-eks-blueprints-addons](https://github.com/aws-ia/terraform-aws-eks-blueprints-addons) | [fix: Keep nested prefixes in the Velero backup location](https://github.com/aws-ia/terraform-aws-eks-blueprints-addons/pull/524) |
| [kubernetes-sigs/descheduler](https://github.com/kubernetes-sigs/descheduler) | [fix(helm): allow setting serviceMonitor.honorLabels to false](https://github.com/kubernetes-sigs/descheduler/pull/1940) |
| [NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin) | [Inspect embedded config.map entries before adding SYS_ADMIN](https://github.com/NVIDIA/k8s-device-plugin/pull/2155) |
| [terraform-aws-modules/terraform-aws-iam](https://github.com/terraform-aws-modules/terraform-aws-iam) | [fix: Keep IRSA policy count known when policy documents are not read](https://github.com/terraform-aws-modules/terraform-aws-iam/pull/671)<br>[fix: Add `ec2:DescribeVpcPeeringConnections` to the LBC TargetGroupBinding only policy](https://github.com/terraform-aws-modules/terraform-aws-iam/pull/670) |
| [github-aws-runners/terraform-aws-github-runner](https://github.com/github-aws-runners/terraform-aws-github-runner) | [fix(termination-watcher): keep retry queue visibility timeout at or above the Lambda timeout](https://github.com/github-aws-runners/terraform-aws-github-runner/pull/5576) |
| [kubernetes-sigs/jobset](https://github.com/kubernetes-sigs/jobset) | [helm: default the ServiceMonitor client cert to the release's metrics secret](https://github.com/kubernetes-sigs/jobset/pull/1389) |
| [equinix/terraform-provider-equinix](https://github.com/equinix/terraform-provider-equinix) | [fix: remove equinix_fabric_connection from state when it no longer exists](https://github.com/equinix/terraform-provider-equinix/pull/1103)<br>[fix: mark Fabric credential attributes as sensitive](https://github.com/equinix/terraform-provider-equinix/pull/1101)<br>[fix: stop mutating the shared Network Edge client user agent](https://github.com/equinix/terraform-provider-equinix/pull/1100) |
| [terrakube-io/terrakube-helm-chart](https://github.com/terrakube-io/terrakube-helm-chart) | [fix(otel): quote defaulted values in the otel ConfigMaps](https://github.com/terrakube-io/terrakube-helm-chart/pull/304)<br>[fix(api): render automountServiceAccountToken when it is false](https://github.com/terrakube-io/terrakube-helm-chart/pull/303) |
| [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) | [fix(docker): actually install certificates from CUSTOM_CERT_DIR](https://github.com/AsyncFuncAI/deepwiki-open/pull/623)<br>[fix: use the shared WebSocket URL helper in slides and workshop pages](https://github.com/AsyncFuncAI/deepwiki-open/pull/622) |
| [tsuru/kubernetes-router](https://github.com/tsuru/kubernetes-router) | [ci: pin third-party actions to commit SHAs and restrict token permissions](https://github.com/tsuru/kubernetes-router/pull/61)<br>[fix(ingress): remove certificate without panicking when ingress has multiple TLS entries](https://github.com/tsuru/kubernetes-router/pull/60) |
| [tsuru/go-tsuruclient](https://github.com/tsuru/go-tsuruclient) | [fix(config): keep token files readable only by the owner](https://github.com/tsuru/go-tsuruclient/pull/38) |
| [tsuru/rpaas-operator](https://github.com/tsuru/rpaas-operator) | [fix: return the get error before using the rpaas instance in reconcile](https://github.com/tsuru/rpaas-operator/pull/204) |
| [tsuru/acl-operator](https://github.com/tsuru/acl-operator) | [fix: stop requeueing deleted tsuru apps and cronjobs](https://github.com/tsuru/acl-operator/pull/14) |
| [coredns/helm](https://github.com/coredns/helm) | [fix: default the server port when it is not set](https://github.com/coredns/helm/pull/289) |
| [goharbor/harbor-helm](https://github.com/goharbor/harbor-helm) | [feat(core): add core.existingSecretKey for the core secret](https://github.com/goharbor/harbor-helm/pull/2432) |
| [memcached/memcached](https://github.com/memcached/memcached) | [contrib: add a Helm chart](https://github.com/memcached/memcached/pull/1338) |
| [flant/shell-operator](https://github.com/flant/shell-operator) | [[shell-operator] feat: add a generic Helm chart](https://github.com/flant/shell-operator/pull/963) |
| [gruntwork-io/terragrunt](https://github.com/gruntwork-io/terragrunt) | [fix: include init in get_terraform_commands_that_need_vars for OpenTofu >= 1.8](https://github.com/gruntwork-io/terragrunt/pull/7252) |
| [ray-project/ray](https://github.com/ray-project/ray) | [[Java] Bump log4j to 2.25.5 and jackson-databind to 2.18.11](https://github.com/ray-project/ray/pull/67828) |
| [argoproj-labs/terraform-provider-argocd](https://github.com/argoproj-labs/terraform-provider-argocd) | [feat(account_token): add optional token_id attribute](https://github.com/argoproj-labs/terraform-provider-argocd/pull/975) |
| [stern/stern](https://github.com/stern/stern) | [fix: compile the highlight regexp once per tail](https://github.com/stern/stern/pull/406) |
| [goharbor/harbor](https://github.com/goharbor/harbor) | [fix: return 404 for role ids outside the int32 range](https://github.com/goharbor/harbor/pull/24308) |
| [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | [feat(health): add health checks for Strimzi KafkaMirrorMaker and KafkaMirrorMaker2 (#5048)](https://github.com/argoproj/argo-cd/pull/30778)<br>[fix(cli): include argocd-cmd-params-cm in admin export/import (#9506)](https://github.com/argoproj/argo-cd/pull/30759)<br>[fix(cli): report server version as unavailable in core mode (#9747)](https://github.com/argoproj/argo-cd/pull/30758) |
| [kubernetes-sigs/aws-load-balancer-controller](https://github.com/kubernetes-sigs/aws-load-balancer-controller) | [fix(helm): quote default-tags and aws-vpc-tags args](https://github.com/kubernetes-sigs/aws-load-balancer-controller/pull/4943) |
| [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Use targetRefs for backend policy relations](https://github.com/kubernetes-sigs/headlamp/pull/8256) |
| [open-feature/java-sdk-contrib](https://github.com/open-feature/java-sdk-contrib) | [fix(flagd): stop the FlagStore streamer thread on shutdown](https://github.com/open-feature/java-sdk-contrib/pull/1967) |
| [litmuschaos/litmus](https://github.com/litmuschaos/litmus) | [fix(authentication): check the stored role before letting an owner leave](https://github.com/litmuschaos/litmus/pull/5712) |
| [openkruise/charts](https://github.com/openkruise/charts) | [fix(kruise): point CRD conversion webhooks at the chart webhook service](https://github.com/openkruise/charts/pull/230) |
| [openebs/dynamic-localpv-provisioner](https://github.com/openebs/dynamic-localpv-provisioner) | [fix(helm): render localpv.securityContext on the provisioner container](https://github.com/openebs/dynamic-localpv-provisioner/pull/386) |
| [kube-logging/fluent-plugin-label-router](https://github.com/kube-logging/fluent-plugin-label-router) | [Add worker_id label to router metrics with multiple workers](https://github.com/kube-logging/fluent-plugin-label-router/pull/32) |
| [submariner-io/submariner-charts](https://github.com/submariner-io/submariner-charts) | [Omit ceIPSecPSK when no IPsec PSK is set](https://github.com/submariner-io/submariner-charts/pull/799) |
| [carvel-dev/vendir](https://github.com/carvel-dev/vendir) | [Explain when a github release has no assets to fetch](https://github.com/carvel-dev/vendir/pull/482) |
| [kube-vip/kube-vip](https://github.com/kube-vip/kube-vip) | [fix(services): do not treat DHCP placeholder VIPs as shared](https://github.com/kube-vip/kube-vip/pull/1838) |
| [konveyor/tackle2-hub](https://github.com/konveyor/tackle2-hub) | [:bug: Validate shared api.Document fields against their schema](https://github.com/konveyor/tackle2-hub/pull/1183) |
| [crossplane/crossplane](https://github.com/crossplane/crossplane) | [test(e2e): cover CRD hand-off for control planes upgraded from v1.20](https://github.com/crossplane/crossplane/pull/8011) |
| [open-policy-agent/java-opa-sdk](https://github.com/open-policy-agent/java-opa-sdk) | [fix(cli): print counters and histograms in the metrics table](https://github.com/open-policy-agent/java-opa-sdk/pull/269) |
| [kubernetes/website](https://github.com/kubernetes/website) | [[pt-br] Add tasks/configure-pod-container/configure-projected-volume-storage.md](https://github.com/kubernetes/website/pull/59012)<br>[[pt-br] Add tasks/configure-pod-container/attach-handler-lifecycle-event.md](https://github.com/kubernetes/website/pull/59011)<br>[[pt-br] Add tasks/configure-pod-container/configure-pod-initialization.md](https://github.com/kubernetes/website/pull/59010)<br>[[pt-br] Add tasks/configure-pod-container/pull-image-private-registry.md](https://github.com/kubernetes/website/pull/59006)<br>[[pt-br] Add tasks/configure-pod-container/assign-cpu-resource.md](https://github.com/kubernetes/website/pull/59005)<br>[[pt-br] Add tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md](https://github.com/kubernetes/website/pull/59002)<br>[[pt-br] Add tasks/configure-pod-container/assign-memory-resource.md](https://github.com/kubernetes/website/pull/59000)<br>[[pt-br] Add concepts/architecture/leases.md](https://github.com/kubernetes/website/pull/58998) |
| [prometheus/alertmanager](https://github.com/prometheus/alertmanager) | [ui: stop building a Brotli variant of index.html](https://github.com/prometheus/alertmanager/pull/5724) |
| [envoyproxy/gateway](https://github.com/envoyproxy/gateway) | [fix(status): merge policy ancestor status across controllers](https://github.com/envoyproxy/gateway/pull/10516)<br>[docs: move Gateway Exported Metrics from Tasks to Concepts](https://github.com/envoyproxy/gateway/pull/10515) |
| [prometheus/node_exporter](https://github.com/prometheus/node_exporter) | [fix(diskstats): drop sector metrics on darwin](https://github.com/prometheus/node_exporter/pull/3885) |
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
