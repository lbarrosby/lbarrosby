### Lucas Barros

<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=20&duration=3500&pause=1200&color=58A6FF&center=true&vCenter=true&width=640&lines=Platform+engineering+on+Kubernetes;Terraform+%C2%B7+GitOps+%C2%B7+Atlantis+%C2%B7+Envoy;Boring%2C+predictable+infrastructure" alt="Platform engineering on Kubernetes">
</p>

Platform engineer based in Rio de Janeiro. I design and operate Kubernetes platforms for teams that ship to production every day, mostly in financial services.

Over the last years that meant running a fleet of 330 clusters behind ArgoCD, Atlantis and Rancher, turning EKS provisioning from a two-day manual process into a 40-minute Terraform/Terragrunt pipeline, moving a 3,000 jobs/day Jenkins farm to immutable infrastructure, and treating cloud cost as an engineering metric rather than a finance report.

I care about boring, predictable infrastructure: everything in code, every change reviewed, upgrades that nobody notices.

**Open source**

Contributing upstream across the CNCF landscape, from graduated projects like Kubernetes, Envoy, Prometheus, Argo and OPA to sandbox ones like Headlamp, kube-vip, OpenEBS and Submariner, plus the Kubernetes pt-br docs localization.

<!--START_SECTION:activity-->
<img src="https://img.shields.io/badge/upstream%20PRs-42-1F6FEB?style=flat-square" alt="Upstream PRs"> <img src="https://img.shields.io/badge/merged-1-8957E5?style=flat-square" alt="Merged"> <img src="https://img.shields.io/badge/projects-30-2EA043?style=flat-square" alt="Projects">

| Project | Latest pull request | |
|---|---|---|
| [argoproj-labs/terraform-provider-argocd](https://github.com/argoproj-labs/terraform-provider-argocd) | [feat(account_token): add optional token_id attribute](https://github.com/argoproj-labs/terraform-provider-argocd/pull/975) | `open` |
| [rook/rook](https://github.com/rook/rook) | [osd: don't wipe metadata devices of existing OSDs](https://github.com/rook/rook/pull/18686) | `open` |
| [tsuru/tsuru-client](https://github.com/tsuru/tsuru-client) | [fix: keep the current target in sync on target update](https://github.com/tsuru/tsuru-client/pull/283) | `open` |
| [stern/stern](https://github.com/stern/stern) | [fix: compile the highlight regexp once per tail](https://github.com/stern/stern/pull/406) | `open` |
| [terraform-aws-modules/terraform-aws-iam](https://github.com/terraform-aws-modules/terraform-aws-iam) | [fix: Add `ec2:DescribeVpcPeeringConnections` to the LBC TargetGroupBinding only policy](https://github.com/terraform-aws-modules/terraform-aws-iam/pull/670) | `open` |
| [goharbor/harbor](https://github.com/goharbor/harbor) | [fix: return 404 for role ids outside the int32 range](https://github.com/goharbor/harbor/pull/24308) | `open` |
| [tsuru/terraform-provider-tsuru](https://github.com/tsuru/terraform-provider-tsuru) | [fix: drop tsuru_app_cname and tsuru_app_router from state when removed outside terraform](https://github.com/tsuru/terraform-provider-tsuru/pull/98) | `open` |
| [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | [feat(health): add health checks for Strimzi KafkaMirrorMaker and KafkaMirrorMaker2 (#5048)](https://github.com/argoproj/argo-cd/pull/30778) · +2 more | `open` |
| [kubernetes-sigs/aws-load-balancer-controller](https://github.com/kubernetes-sigs/aws-load-balancer-controller) | [fix(helm): quote default-tags and aws-vpc-tags args](https://github.com/kubernetes-sigs/aws-load-balancer-controller/pull/4943) | `open` |
| [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | [frontend: resourceMap: Use targetRefs for backend policy relations](https://github.com/kubernetes-sigs/headlamp/pull/8256) · +2 more | `open` |
| [open-feature/java-sdk-contrib](https://github.com/open-feature/java-sdk-contrib) | [fix(flagd): stop the FlagStore streamer thread on shutdown](https://github.com/open-feature/java-sdk-contrib/pull/1967) | `open` |
| [litmuschaos/litmus](https://github.com/litmuschaos/litmus) | [fix(authentication): check the stored role before letting an owner leave](https://github.com/litmuschaos/litmus/pull/5712) | `open` |
| [openkruise/charts](https://github.com/openkruise/charts) | [fix(kruise): point CRD conversion webhooks at the chart webhook service](https://github.com/openkruise/charts/pull/230) | `open` |
| [lima-vm/lima](https://github.com/lima-vm/lima) | [limayaml: don't panic when the latest config fails to load](https://github.com/lima-vm/lima/pull/5738) | `open` |
| [openebs/dynamic-localpv-provisioner](https://github.com/openebs/dynamic-localpv-provisioner) | [fix(helm): render localpv.securityContext on the provisioner container](https://github.com/openebs/dynamic-localpv-provisioner/pull/386) | `open` |
| [kube-logging/fluent-plugin-label-router](https://github.com/kube-logging/fluent-plugin-label-router) | [Add worker_id label to router metrics with multiple workers](https://github.com/kube-logging/fluent-plugin-label-router/pull/32) | `open` |
| [openebs/lvm-localpv](https://github.com/openebs/lvm-localpv) | [feat(chart): allow extra args for the controller CSI sidecars](https://github.com/openebs/lvm-localpv/pull/528) | `open` |
| [submariner-io/submariner-charts](https://github.com/submariner-io/submariner-charts) | [Omit ceIPSecPSK when no IPsec PSK is set](https://github.com/submariner-io/submariner-charts/pull/799) | `open` |
| [carvel-dev/vendir](https://github.com/carvel-dev/vendir) | [Explain when a github release has no assets to fetch](https://github.com/carvel-dev/vendir/pull/482) | `open` |
| [kube-vip/kube-vip](https://github.com/kube-vip/kube-vip) | [fix(services): do not treat DHCP placeholder VIPs as shared](https://github.com/kube-vip/kube-vip/pull/1838) | `open` |
| [konveyor/tackle2-hub](https://github.com/konveyor/tackle2-hub) | [:bug: Validate shared api.Document fields against their schema](https://github.com/konveyor/tackle2-hub/pull/1183) | `open` |
| [crossplane/crossplane](https://github.com/crossplane/crossplane) | [test(e2e): cover CRD hand-off for control planes upgraded from v1.20](https://github.com/crossplane/crossplane/pull/8011) | `open` |
| [open-policy-agent/java-opa-sdk](https://github.com/open-policy-agent/java-opa-sdk) | [fix(cli): print counters and histograms in the metrics table](https://github.com/open-policy-agent/java-opa-sdk/pull/269) | `open` |
| [fluent/fluent-plugin-kafka](https://github.com/fluent/fluent-plugin-kafka) | [in_kafka_group, in_rdkafka_group: Fix records skipped with time_source record](https://github.com/fluent/fluent-plugin-kafka/pull/598) | `open` |
| [coredns/helm](https://github.com/coredns/helm) | [docs: note that the ServiceMonitor needs the metrics Service](https://github.com/coredns/helm/pull/288) | `open` |
| [kubernetes/website](https://github.com/kubernetes/website) | [[pt-br] Add tasks/configure-pod-container/configure-projected-volume-storage.md](https://github.com/kubernetes/website/pull/59012) · +7 more | `open` |
| [prometheus/alertmanager](https://github.com/prometheus/alertmanager) | [ui: do not serve Brotli-encoded HTML](https://github.com/prometheus/alertmanager/pull/5724) | `open` |
| [envoyproxy/gateway](https://github.com/envoyproxy/gateway) | [fix(status): merge policy ancestor status across controllers](https://github.com/envoyproxy/gateway/pull/10516) · +1 more | `open` |
| [prometheus/node_exporter](https://github.com/prometheus/node_exporter) | [fix(diskstats): drop sector metrics on darwin](https://github.com/prometheus/node_exporter/pull/3885) | `open` |
| [runatlantis/atlantis](https://github.com/runatlantis/atlantis) | [fix: reject targeted plan for a missing dir before creating its status](https://github.com/runatlantis/atlantis/pull/7055) | `open` |
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
