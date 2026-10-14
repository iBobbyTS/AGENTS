---
name: deployment-preflight
description: Manually requested pre-release or pre-deployment safety review for a concrete candidate and real transition, using a stable per-project release profile. Works for services, static sites, desktop apps, CLI/libraries and other deliverables without requiring CI/CD. Create or reconcile the profile, inspect risk-selected evidence and issue advisory readiness. Never publish, deploy, migrate production or accept risks on the user's behalf.
---

# Deployment preflight

Answer: **Can this particular candidate be delivered through this project's actual release path under the stated conditions?** This is not a whole-project audit or permission to execute the release. General-audit findings are useful inputs, not prerequisites or automatic clearance.

## 1. Establish authority, candidate and stable profile

Run on an explicit user preflight request or a separately authorized preflight-only trigger. Do not treat a steward recommendation as deploy authority. Read permitted evidence and create local reports; actual product commands require their own permitted scope. No production mutation, package publication, dependency install, backup/restore on live systems, secret extraction, product edits or deployment is implicit. “Dry-run” is not a permission or safety guarantee: inspect what the command and its hooks really execute. Use disposable environments only when authorized and available.

Locate the existing project release model; otherwise draft one from [PROFILE template](templates/PROFILE.md) and observed files. Record source/provenance and unknowns. Do not force a long questionnaire: infer verifiable facts, ask only for indispensable target/authority facts unavailable elsewhere, and continue independent checks. Never present a guessed production topology as established fact.

Bind this run to the actual candidate artifact/source+dirty state, intended target/channel, current deployed or supported-consumer version(s), and configuration relevant to the transition. `HEAD~1` is not the deployed baseline. For first release, establish that fact and inspect first-install/activation; for packages/desktop software, supported upgrade origins may be several versions, not one server revision. Unknown material identity prevents a confident readiness verdict.

The profile holds durable topology, entry points, state owners, distribution method, compatibility/recovery promises, evidence sources and permission limits. This run holds current versions, diffs, checks and results. Use [profile lifecycle](references/profile-lifecycle.md). Changes to runtime support, permissions, signing, secrets interface, channels or actual state can invalidate profile facts even without a large architecture refactor. Check drift lightly each run and patch only affected facts under appropriate edit authority; don't rewrite the entire profile or stop all independent work for a harmless difference.

## 2. Plan the actual transition and load relevant knowledge

Read the shared [router](../general-audit/knowledge/router.md). It is the single canonical knowledge library, not a requirement to execute general-audit. The three skills are installed as siblings; if knowledge cannot be located, disclose the dependency gap and use project evidence/primary docs without claiming those cards were used.

Sketch **current users/system → preparation → switch/distribution → first real use → failure detection → containment/recovery**. Include only reachable coexistence/order/state combinations. Select the domain and release cards that change this plan; before each substantive phase load its additional relevant knowledge, reusing already loaded cards. Don't read a database guide for a stateless release or duplicate the library by profile.

Every run addresses these outcome questions at an appropriate depth:
1. Is this the intended artifact, consumer/target and supported environment?
2. Can it be installed/started/consumed with the actual configuration, permissions and dependencies?
3. Does the real transition preserve required behavior, compatibility and owned state?
4. Can failure be noticed and contained/recovered within the project's real promises?
5. Is the necessary evidence current and sufficient, and who owns unresolved decisions?

These aren't five mandatory test suites. A tiny static site and a staged stateful service require different evidence. A profile is a starting model, not a whitelist preventing discovery of new risks.

## 3. Inspect and validate proportionately

Compare actual release inputs, build/package contents, launch/install paths, configuration interface, relevant permissions and environment against the profile and current change. Follow actual consumers rather than only source compilation. Where delivery depends on install/configuration, migration or recovery guidance, use [documentation integrity](../general-audit/knowledge/mechanisms/documentation-integrity.md) to check the instructions actually reaching this candidate's users/operators, including material warnings and version/channel alignment. This is a selected release assertion, not a whole-docs audit or automatic style gate. Load the canonical release/artifact, environment and transition cards as applicable. Shared SQL/state cards apply only when the real transition uses those mechanisms; migration is one risk class, not the default center of the review.

Reuse trustworthy evidence when candidate, environment, relevant inputs and assumptions match. A source test on a different package doesn't certify the delivered artifact. CI is optional; local/manual evidence is valid with target, method and limitations recorded. If a required probe cannot safely run, inspect what can be established statically and mark the remaining assertion unknown. Do not install infrastructure just to complete the checklist.

Use risk-selected probes: actual package consumer or startup, representative upgrade/compatibility, deployment ordering, state continuity, observation and recovery where relevant. No live chaos/deploy rehearsal by default. Distinguish source trace, synthetic/disposable test, actual staging check and pending production activation checks. Never claim a post-deploy check has passed before deployment.

Check failure boundaries and recovery options, not a universal reversible-migration requirement. Application rollback, data restore, forward repair, release withdrawal and support for old clients are different operations with different limits. Validate the option the project truly relies on. A release step that cannot be safely undone needs an explicit point-of-no-return and viable containment strategy; don't invent an easy downgrade.

Recheck profile/target drift that affects findings. A stale profile is not automatically total failure, but a material unresolved model mismatch makes the relevant readiness claim incomplete. Route a systemic issue to general-audit as a pointer, not an automatic additional gate. Immediate release-blocking consequences still belong in this preflight.

## 4. Produce advisory readiness and stop

Use [REPORT template](templates/REPORT.md). Lead with exact target, result and actionable reasons; concise human summary first, evidence behind it. Enumerate blocking facts, material unknowns, accepted risks with **actual human authority**, and proposed manual sequence/checkpoints. Record what was examined and what wasn't; no invented completeness percentage.

Results:
- **READY** — necessary pre-release assertions supported for this defined transition; not a guarantee or deploy permission.
- **READY_WITH_ACCEPTED_RISKS** — remaining risk is within an explicit, applicable user acceptance; cite that authority. The agent cannot create it.
- **BLOCKED** — a demonstrated incompatibility/unsafe condition violates required release constraints; show missing evidence separately if also present.
- **INSUFFICIENT_EVIDENCE** — a necessary assertion cannot be established. Pending risk approval is not “accepted.”

Routine post-activation observation can be a documented manual checkpoint without being a pre-release blocker; prerequisite facts needed for a safe switch cannot be relabeled “check after deploying.” Don't declare READY subject to unresolved safety essentials. No risk acceptance rewrites an observed failure as passed evidence.

Save the run at an existing compatible location or `.agent-work/deployment-preflight/runs/<run-id>/REPORT.md`; keep the stable profile separate. Readiness applies only to identified inputs/environment and stated freshness assumptions. New relevant changes invalidate affected checks. Never update “last deployed revision” just because preflight finished: only an actual deployment receipt/user-confirmed observation can do that. Stop before publish/deploy. Human release authority remains separate.
