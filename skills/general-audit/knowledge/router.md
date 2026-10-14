# Shared knowledge router

This is the canonical library for general-audit and deployment-preflight. It contains **knowledge for questions**, not parallel copies of their workflows. Quality-steward normally needs only general-audit's intake, not this library. The [index](index.md) is a lookup aid, not a scope limit or reading checklist.

Start with an observed boundary and the next phase's decision. Compose only nonredundant cards across five axes: outcome/domain, failure mechanism, actual technology semantics, evolution history and evidence method. Release is an application context inside the index, not a sixth mandatory axis or a duplicate knowledge set. General-audit modes do not select fixed bundles.

| Upcoming phase / uncertainty | Minimal entry points when relevant |
|---|---|
| Establish intended outcome vs current system | Matching domain; behavior-contract only when intent/scope drift matters |
| Investigate a path | Actual mechanism + technical semantics that change the explanation |
| Rely on tests or a clean tool summary | Oracles / population; verification-system for suite-wide trust questions |
| Judge accumulated design/AI development | Architecture / ai-led; process-effectiveness only for evidence about the development process |
| Bind a release to its real target | Artifact identity; domain for the actual consumer |
| Check install/start/consumption | Environment and actual shell/runtime seam |
| Validate an upgrade/switch | Transition; state/SQL/async only when actually present |
| Assess failure and containment | Recovery, plus actual owner mechanism |
| Challenge a disputed conclusion | Oracles/population/experiments, only where uncertainty calls for them |

Before a substantive phase, check whether already-loaded knowledge is sufficient; read new cards only when a newly encountered seam warrants it. Give the selected card and practical reason in the existing investigation/run paragraph. No per-axis report, read receipt, reviewer or approval gate. Don't count card coverage as project coverage.

A familiar syntax rule is not a knowledge-loading reason. Unfamiliar/version-dependent semantics may need primary documentation for the installed version. An unlisted framework retains useful domain/mechanism matches; use [fallback](fallback.md) only for the unresolved seam. Don't guess Rust→Tokio, AI-written code→AI product, public package→live server, or audit→permission to operate production.

**Knowledge ownership:** test expected-result independence lives in `oracles`, inspected/executed scope in `population`, suite economics/blind spots in `verification-system`; build/distribution identity in `release/artifact-identity`, supply-chain trust in `supply-chain`; practical detection/recovery in `recovery`, version-transition compatibility in `release/transition`. Link rather than repeat. A project profile describes stable facts and constraints, not another copy of these mechanisms.
