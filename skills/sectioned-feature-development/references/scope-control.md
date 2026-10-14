# Scope and Over-Design Control

## Contents

1. [Authority hierarchy](#authority-hierarchy)
2. [Initial-plan authority gate](#initial-plan-authority-gate)
3. [Active-contract sanitation](#active-contract-sanitation)
4. [Minimum sufficient design](#minimum-sufficient-design)
5. [Security and threat models](#security-and-threat-models)
6. [Persistence and recovery](#persistence-and-recovery)
7. [Generic governance and analyzers](#generic-governance-and-analyzers)
8. [Testing infrastructure](#testing-infrastructure)
9. [Scope-growth signals](#scope-growth-signals)
10. [Correction protocol](#correction-protocol)

## Authority hierarchy

Use this order:

1. explicit user-approved behavior and decisions;
2. repository-local rules and current production contracts;
3. current code/tests as evidence of established behavior that the requested change must preserve;
4. accepted feature and section contracts as an index of the authority above, never as a source of new authority;
5. reviewer or planner suggestions.

Plans and contracts cannot bootstrap scope by declaring a new behavior, option, proof obligation, or mechanism and then citing themselves. Reviewer/planner suggestions cannot override levels 1–3. They are candidates to classify, not requirements to implement. The approved scope is monotonic during implementation/review: it may be narrowed or simplified, but it may grow only through an explicit owner decision. Repeated agreement does not create authority.

## Initial-plan authority gate

Before writing the section graph, record the original user request verbatim and the smallest end-to-end observable outcome that satisfies it. For every proposed section, acceptance criterion, optional control/UI surface, compatibility promise, support harness, or structural mechanism, record:

- its external authority anchor;
- why it is necessary for that minimum outcome;
- why the existing owner/path cannot satisfy the outcome more simply.

Valid anchors are explicit owner intent, a repository-required rule/gate or current production contract, and a demonstrated correctness dependency on the requested acceptance path. A draft plan, another section, a reviewer suggestion, broader “completeness,” or future-proofing is not an anchor.

When ambiguity remains, choose the narrower functional interpretation and surface the broader alternative as a non-blocking proposal. Do not silently add settings, status projections, UI, docs programs, compatibility ledgers, standalone evidence publishers, security wrappers, or generalized test infrastructure merely because they would make the feature feel more complete.

## Active-contract sanitation

When adopting this skill mid-feature, preserve accepted code and evidence but inspect the active, unaccepted contract before continuing. For every guarantee, oracle, structural allowance, supported actor/environment, and blocker, record its authority at levels 1–4 above.

- Keep anchored items.
- Downgrade reviewer-authored, unanchored items to `SCOPE_PROPOSAL` and remove them from repair/test obligations.
- Do not reopen accepted sections merely because a newer workflow uses different artifacts.
- Do not let an old over-expanded contract manufacture a new `EVIDENCE_GAP`.

This is contract sanitation, not a new audit or plan-review cycle.

## Minimum sufficient design

For audit-remediation features, freeze the accepted audit finding IDs before implementation. Code review verifies the repair diff; unrelated pre-existing findings return to a separate audit backlog instead of expanding the active feature.


A design is sufficient when it satisfies the frozen behavior and repository obligations with the smallest coherent ownership change.

Before adding a mechanism, ask:

- Which approved requirement needs it?
- Which existing owner cannot satisfy that requirement locally?
- What simpler existing path was considered?
- Does this mechanism create another API, lifecycle, state machine, migration, or failure mode?
- Will the feature remain correct if the mechanism is omitted?

If the feature remains correct without the proposed mechanism, omit that mechanism.

For unanchored support machinery already present in an active feature, deletion is the default. `SIMPLIFY_CURRENT` may retain only the smallest part required by a separately anchored acceptance criterion; it must not preserve a proof system merely because time was already spent building it.

Before implementation and before the first review, compare the product outcome with the proposed product, test, harness, and process burden. There is no fixed LOC ratio, but a supporting harness/test/process surface that dominates the actual feature is a stop signal: re-check authority and remove unanchored work before asking reviewers to improve it.

Complexity estimates are diagnostic, not validity gates. Exceeding an estimate triggers a simplification check, not automatic rollback or clean-room retry.

### Foundational owner versus local patch

Do not automatically prefer either the narrowest file edit or the widest foundational refactor. Surface one bounded owner decision only when all are true:

- the local patch would create a second authoritative implementation of validation, normalization, routing, persistence, selection, or state-transition semantics; or it would leave sibling callers wrong;
- an existing shared owner can fix the root rule coherently;
- changing that owner materially expands the allowed-to-edit manifest or impact cone.

Present the smallest shared-owner fix and the smallest local patch with their residual risks. Do not propose a framework, service, or unrelated cleanup. Cosmetic deduplication, a single-use helper, or a one-field dictionary wrapper is non-blocking and should not interrupt the user.

## Security and threat models

Security review must match the actual artifact and deployment.

Freeze only:

- asset;
- current actor/capability;
- entry point and trust boundary;
- supported deployment/concurrency model;
- guarantees already required.

Examples of likely scope proposals rather than blockers:

- protecting a private test harness against arbitrary malicious in-process objects;
- defending a single-user local directory against a same-UID hostile process;
- adding multi-tenant isolation to a non-multi-tenant tool;
- adding multi-process writer coordination to a single-writer service;
- sanitizing arbitrary exception object graphs when the component never receives secrets;
- hardening against arbitrary malicious archive formats when inputs are internal/trusted.

Use ordinary secure defaults proportional to the artifact—private permissions, atomic replace, static error messages, cleanup—without turning them into a general capability/security framework.

## Persistence and recovery

Do not infer transaction journals, outboxes, manifests, restart recovery, or historical reconstruction from a local consistency bug.

Add persistence/recovery machinery only when:

- an authoritative requirement requires restart durability or multi-step atomicity;
- the existing repository architecture already uses that mechanism for the same owner;
- a simpler local transaction/ordering fix cannot satisfy the contract.

A reviewer may identify data loss or corruption caused by the diff. It may not silently upgrade the product to stronger durability or recovery semantics.

## Generic governance and analyzers

A feature-specific regression does not automatically justify:

- whole-tree static source inventory;
- custom AST or grammar framework;
- runtime detector/coordinator;
- global CI prohibition;
- permanent policy registry;
- repository-wide “future regression prevention” system.

Prefer:

- explicit tests for changed routes/owners;
- existing lint/static tools;
- one representative integration/browser flow;
- documentation in the existing owner.

A generalized governance system is a separate feature requiring explicit scope, ownership, rollout, and maintenance commitment.

## Testing infrastructure

Tests should prove current behavior, not become a new product.

Do not add a test-only section or generalized sandbox merely to satisfy review evidence. Keep the smallest oracle with the behavior section.

A test-only change should not force broad product re-review unless it changes shared setup, global fixtures, build behavior, or production code generation.

Do not require a test commit to appear before a product commit in Git history. Current code plus current deterministic results are the evidence.

## Scope-growth signals

Stop and classify when any appears:

- section count grows because reviewers propose new guarantees;
- a local change creates a new registry/service/framework not in the plan;
- tests or review artifacts exceed the product diff in complexity;
- repeated work is about fingerprints, lineage, provenance, or template compliance rather than behavior;
- reviewers discuss unsupported actors/environments more than current users/flows;
- a local route/service fix turns into whole-repository governance;
- accepted predecessor sections are reopened without product-code change;
- a small fifth-round omission triggers full rearchitecture or clean-room rebuild.

## Correction protocol

When scope drift is detected:

1. Freeze the user-approved outcome and current correct behavior.
2. Classify each added mechanism as requirement-anchored or review-created.
3. Remove or simplify review-created mechanisms before splitting them into more sections.
4. Restore the proportional environment/threat model.
5. Preserve validated product fixes that remain aligned.
6. Re-run only tests/review invalidated by the simplification.
7. Record rejected proposals as non-blocking notes; do not add them to descendant plans.

Use `SIMPLIFY_CURRENT` at hard cap when over-design is the dominant cause.
