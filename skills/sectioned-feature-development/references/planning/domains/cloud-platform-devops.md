# Cloud / platform / DevOps

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Deployment/configuration/IaC/CI/service-operability behavior is the requested change.

Do not select merely because an app is deployed in cloud but only local business logic changes.

## Decisions before sectioning

- Name control plane, desired/observed state, actual target environment and ownership of deployment resources.
- Specify readiness versus liveness, rollout/rollback and config/secret boundaries only as required.
- Identify reversible and destructive operations; approvals for real apply/release remain explicit.

## Handoff and smallest useful evidence

Reuse repository validate/plan/dry-run plus the bounded target check. A mocked manifest does not prove live rollout; unavailable credentials remain a gap. Mechanical CI changes should not be split into artificial business sections.

## Scope boundary

No new cluster, service mesh, universal observability, supply-chain policy or cloud migration. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Kubernetes pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
