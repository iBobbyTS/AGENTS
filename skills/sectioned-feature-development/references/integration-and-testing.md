# Integration and Proportional Testing

## Contents

1. [Validation tiers](#validation-tiers)
2. [Checkpoint triggers](#checkpoint-triggers)
3. [Integration review boundary](#integration-review-boundary)
4. [Evidence failures](#evidence-failures)
5. [Final-head evidence](#final-head-evidence)
6. [Merge readiness](#merge-readiness)

## Validation tiers

### Tier 1 — targeted

Run after implementation and each repair:

- exact regression tests for changed behavior;
- direct owner/module tests;
- narrow lint/type/static checks for touched code;
- smallest deterministic reproduction.

### Tier 2 — section/package

Run before `FINAL_BOUNDED`:

- section/package/service test suite;
- relevant lint/typecheck/build;
- representative integration path for the section;
- migration/schema checks when touched.

### Tier 3 — feature/repository

Run at final integration or when repository rules require:

- full repository suite;
- application build/bundle;
- browser/E2E flow;
- deployment/migration dry run;
- cross-service integration.

Do not run Tier 3 after every local repair. Reuse an identical successful check when the relevant product/test head and environment are unchanged; agent handoff or a fresh reviewer does not itself invalidate CI evidence. A test-only local oracle change stays at Tier 1/2 unless it modifies shared/global test infrastructure. Tier 3 validates only the already-listed feature acceptance criteria and repository-required gates; it cannot create new routes, flows, analyzers, or governance obligations.

## Checkpoint triggers

Run a checkpoint when a later section begins consuming a new:

- public/serialized contract;
- schema or migration stage;
- permission/trust boundary;
- state owner or concurrency protocol;
- queue/background workflow;
- deployment/flag/rollout path;
- compatibility stage.

A checkpoint verifies producer-consumer composition and representative behavior. It uses the same finding taxonomy, five-part blocking proof, and scope authority as section review. It does not re-review every accepted local diff.

## Integration review boundary

Before dispatching an integration reviewer, write an `unproven_composition` list naming the exact cross-section/runtime/process behaviors not already proven by section/package/consumer evidence. Dispatch only when the list is non-empty. Exact package publication plus exact consumer installation, tests, and build may prove composition without another reviewer. For a single section whose bounded review covered the complete feature path—or any feature whose list is empty—omit the redundant reviewer and run only the required Tier 3 gate.

When required, freeze the exact feature product/test head, assert that no product writer/reviewer is active, and dispatch one fresh reviewer with a stable task/session ID distinct from the plan reviewer and every product writer, composing the request from [INTEGRATION-REVIEW-REQUEST.template.md](../assets/INTEGRATION-REVIEW-REQUEST.template.md). The final integration review asks what local section reviews could not prove:

- Does the original feature outcome work end to end?
- Do section contracts compose correctly?
- Are ordering, state, errors, permissions, migration, and cleanup correct across boundaries?
- Are feature non-goals and branch scope preserved?
- Do rollout/rollback/observability requirements actually requested by the feature hold?

Integration composition creates no new requirement authority. Admit only feature-diff-caused composition defects, necessary merge-blocking dependencies, or evidence gaps tied to an existing feature acceptance criterion/repository gate.

It does not:

- repeat local style/maintainability review;
- audit unrelated modules;
- create a repository-wide governance initiative;
- strengthen security/durability/compatibility beyond the approved feature;
- reopen accepted sections without concrete combined-behavior evidence.

Use one cumulative integration repair budget of at most five waves across checkpoints and final integration. Rerunning final evidence does not reset it. After the cap, allow at most one bounded main-orchestrator (plan-author) diagnosis/recovery event; if the next repair/final pass does not close, report `not-mergeable` or stop for a genuine owner decision rather than expanding the feature.

## Evidence failures

Classify an unavailable service, credential, platform, flaky environment, wrong selector, or broken test harness as evidence failure.

Respond proportionally:

- correct the selector or local oracle;
- use a deterministic fake/probe when contract-appropriate;
- report the unverified path and residual risk;
- defer environment-specific validation to final integration when necessary.

Do not create a generic sandbox, network/process interceptor, or large test framework unless the feature contract already requires proving that property.

## Final-head evidence

The reviewed/tested product-and-test head must equal the delivered head used for readiness. Later process/docs-only commits do not invalidate evidence. Later product/test changes require a bounded closure of only that range plus affected checks; do not reopen accepted sections.

## Merge readiness

State one:

- `mergeable`: required behavior and integration evidence pass; no unresolved blocker.
- `not-mergeable`: material blocker remains.
- `insufficient-evidence`: behavior may be correct but required validation could not be obtained.

Include:

- feature base/head;
- accepted sections;
- cross-section findings and repairs;
- Tier 3 checks run/not run;
- owner decisions;
- residual risk and deferred non-blocking work.
