# Bounded Patchset Review

## Contents

1. [Review roles](#review-roles)
2. [Review assurance](#review-assurance)
3. [Causality boundary](#causality-boundary)
4. [Finding classes](#finding-classes)
5. [Blocking proof](#blocking-proof)
6. [Initial bounded review](#initial-bounded-review)
7. [Repair-delta review](#repair-delta-review)
8. [Closing clean round](#closing-clean-round)
9. [Sticky coverage](#sticky-coverage)
10. [Reset rules](#reset-rules)
11. [Review packets](#review-packets)

## Review roles

The parent `$sectioned-feature-development` orchestrator owns scope, admission, repair waves, and acceptance. Each `$code-review` invocation is a **single review pass**. Do not let the child reviewer start its own repair loop, ask to continue after a cap, rewrite the section contract, or delegate the same review again.

The plan reviewer must never code-review the same feature. Every independent coverage slot is distinct from the implementer/repairer. A same-slot local repair check is delta closure, not a second independent clean; the final B acceptance pass follows the full current bounded scope after material repair. Provider choice belongs to the embedded profile. The initial closing-round reviewer is fresh and distinct from the plan reviewer, implementer, repairer and primary reviewer; a later B continuation preserves that independence and records its actual context. Silent-slot retirement overrides this freshness invariant: the productive slot closes even when it is the primary reviewer ([reviewer-orchestration.md](reviewer-orchestration.md)). Record stable task/session IDs; a profile label alone is not identity. The main agent may admit findings but may not implement or repair product code.

A reviewer runs against a frozen product/test head. No writer may edit the reviewed range until the reviewer returns or is explicitly cancelled and stopped. Cancellation does not provide review coverage. In the serial path, a later section waits for current-parent acceptance under all required review/check obligations, plus prerequisite integration. BLOCKED and ABANDONED do not satisfy dependencies. Only explicitly authorized independent parents in isolated worktrees may overlap as defined by parallel-execution.md. Main, not reviewer CLEAN or process completion, closes the handoff.

The embedded dispatch profile owns the native and external code-reviewer routes. Each is one direct route, not a native wrapper that calls another reviewer. Record the real transport and returned ID.

Use:

- `INITIAL_BOUNDED`: one discovery pass over the stable section diff.
- `REPAIR_DELTA`: closure of frozen findings and repair-caused risk.
- `FINAL_BOUNDED`: one closing clean-pair round over the current diff.
- `SUBSECTION_DELTA` / `PARENT_RECONCILIATION`: parent-side accumulation modes defined in [subsections.md](subsections.md).
- `INTEGRATION`: emergent cross-section behavior only.

## Review assurance

Every parent acceptance closes with the two independent coverage slots; the schedule and counting rules live in [reviewer-orchestration.md](reviewer-orchestration.md).

## Causality boundary

A section review asks:

> What material defect did this diff introduce, newly depend on, expose, or make reachable?

It does not ask:

> What else could be improved anywhere in the section, module, feature, or repository?

Unchanged code may be read to prove:

- execution reachability;
- the real contract or owner;
- direct callers/callees and side effects;
- regression impact;
- whether a proposed abstraction duplicates an existing one.

Unrelated defects in unchanged code are `PREEXISTING_OUT_OF_SCOPE`.

## Finding classes

### `DIFF_CAUSED`

The current section diff creates an incorrect behavior, regression, unsafe transition, contract mismatch, or material maintainability defect.

### `MERGE_BLOCKING_DEPENDENCY`

The defect existed before, but a necessary acceptance path now depends on, activates, serializes, or publicly exposes its faulty behavior. Incidental traversal through a shared entry point, proximity to changed code, or merely becoming easier to notice is insufficient. Repair only the smallest dependency needed for safe merge.

### `PREEXISTING_OUT_OF_SCOPE`

The defect existed before and current behavior does not depend on or change its reachability. It does not block this section.

### `SCOPE_PROPOSAL`

The concern requires a new product promise, supported environment, threat actor, durability/compatibility guarantee, generic framework, global analyzer, CI policy, or future-proofing mechanism. It is non-blocking unless the owner approves it.

### `DEFERRED_OWNER`

The behavior is assigned to a named later section and the current intermediate state remains correct.

### `EVIDENCE_GAP`

An already-required behavior lacks adequate evidence. Cite the exact acceptance-criterion ID or repository-required gate that existed before the review. The repair is the smallest test/oracle necessary to prove it—not a generalized harness or sandbox. A reviewer preference for stronger proof is `SCOPE_PROPOSAL` or `NIT_DEBT`.

### `NIT_DEBT`

Style, preference, polish, or bounded debt with no material merge risk.

## Blocking proof

A blocking finding must include:

| Field | Required evidence |
|---|---|
| Causality | Changed hunk/contract or repair delta that creates/newly relies on the issue |
| Reachability | Concrete trigger in the frozen supported environment |
| Authority | Existing requirement, invariant, repository rule, or established behavior |
| Materiality | Correctness, security, data, reliability, compatibility, or maintainability consequence |
| Bounded repair | Smallest fix remains inside the frozen allowed-to-edit owners and adds no unapproved guarantee |

Discard or downgrade a candidate when one field is missing. If a genuine blocker requires editing a new owner, the reviewer reports the causal chain and stops; only the main agent may amend the manifest or rebound ownership. If the repair would create a second authoritative semantic rule or leave sibling callers wrong, report a bounded foundational-versus-local owner decision rather than silently widening. Cosmetic helper extraction remains non-blocking.

For security findings also require:

- protected asset;
- current actor and capability;
- entry point/data flow;
- trust boundary;
- preconditions;
- supported deployment.

Do not assume arbitrary same-UID attackers, malicious in-process Python objects, multi-tenant operation, hostile filesystem rebinding, multi-process writers, or untrusted archives unless authoritative project evidence supports them.

## Initial bounded review

Run at most once per stable section baseline.

The reviewer receives:

- exact `BASE..HEAD`;
- feature outcome and non-goals;
- section contract;
- frozen scope manifest: allowed-to-edit owners, inspect-only dependency paths, excluded mechanisms, and direct impact cone;
- relevant repository rules;
- required checks;
- the dispatched report path — the reviewer's single authorized `.agent-work` write.

The reviewer should:

1. inspect the entire current diff once;
2. select only risk lenses triggered by the changed behavior;
3. trace at least one critical changed path for medium/high-risk sections;
4. generate and falsify hypotheses before reporting;
5. batch root causes before repair;
6. record the files/symbols/contracts/path families reviewed;
7. for any inspection beyond the named cone, record the exact data/control/serialization/contract chain from a changed symbol and stop at the candidate—do not fan out recursively.

It must not:

- audit the repository;
- search for unrelated historical bugs;
- demand future-proofing;
- add a new threat model or compatibility promise;
- turn route-level regression into a generic analyzer;
- turn local persistence into an outbox/journal unless required;
- implement or repair findings itself.

## Repair-delta review

After repair, review only:

```text
PREVIOUS_REVIEWED_HEAD..CURRENT_HEAD
+ open finding acceptance criteria
+ conclusions invalidated by the repair
+ direct new behavior introduced by the repair
```

A delta reviewer may admit a new root cause only if the delta causes it, activates it on a necessary acceptance path, or invalidates earlier evidence. “I looked at another unchanged area this time” is not sufficient. The repair agent may edit only frozen repair owners; a needed new owner returns to the main agent before code changes.

The delta report should answer:

- Is each frozen finding closed?
- Did the repair introduce a direct regression?
- Which previous coverage entries became invalid?
- Which targeted checks prove closure?

Do not rescan the original section. Do not reset because HEAD changed.

## Closing clean round

Run as the second independent coverage slot after the initial discovery/repair, with required checks in place. Its route follows the embedded profile; provider identity is not inferred from a round label.

Use a fresh reviewer. Give it:

- current complete section diff;
- frozen contract and non-goals;
- direct impact cone;
- current validation results;
- concise closed finding IDs and changed owners.

Do not give it rejected hypotheses or persuasive reviewer narratives.

The closing reviewer is not another open-ended discovery pass. It verifies only:

- contract correctness of the final diff;
- one highest-risk end-to-end changed path;
- repair impact cones;
- accidental mechanism/scope growth;
- test sufficiency proportional to the section.

It reports only a new `DIFF_CAUSED`, tightly proven `MERGE_BLOCKING_DEPENDENCY`, or acceptance-criterion-anchored `EVIDENCE_GAP`. Any resulting repair counts toward the same cumulative five-wave section budget. Slot validity, carry-forward and silent-slot retirement follow [reviewer-orchestration.md](reviewer-orchestration.md).

## Sticky coverage

Record reviewed coverage in the parent's FEATURE-STATE ledger lines, referencing the reviewer's own report file for detail: changed files and symbols; critical paths; contracts and invariants; triggered risk lenses; tests/experiments; explicit gaps.

Deterministic check evidence remains reusable until its inputs/environment change. Prior review coverage is an opinion, not proof that unchanged in-scope code is correct; full bounded B may discover a missed defect. Preserve unaffected entries across delta reviews and closing rounds.

A new reviewer does not invalidate existing coverage merely because it has a different context or may choose another lens. A fresh reviewer also does not require rerunning identical successful validation against the same code head; independent analysis and CI rerun are separate decisions.

## Reset rules

Reset to another initial bounded review only when a repair materially changes:

- public/serialized API or schema;
- authorization, tenant isolation, or trust boundary;
- persistence, migration, durability, or recovery contract;
- state ownership or concurrency semantics;
- destructive/deployment/rollback behavior;
- supported environment or section goal;
- most of the section's architecture/behavior.

Do not reset for:

- local bug fixes;
- added targeted tests;
- line movement;
- plan/review schema changes;
- fingerprints;
- skill updates;
- different reviewer preference;
- evidence files moving in Git history.

## Final-head evidence

Before section or feature readiness, record the exact product/test head covered by the required clean reviewer outcome and checks. Later process/docs-only commits do not invalidate it. Any later product/test change requires affected check/coverage closure and the required full bounded B for the current unaccepted parent; it does not reopen accepted predecessors or the full initial review.

## Review packets

Use the bundled `SECTION-REVIEW-REQUEST.template.md`. Key mode-specific instructions:

### Initial

```text
Mode: INITIAL_BOUNDED
Perform one single-pass diff review. Do not repair. Report only current-diff material defects.
```

### Delta

```text
Mode: REPAIR_DELTA
Review only REPAIR_BASE..HEAD, frozen finding IDs, and invalidated impact cone. Do not reopen unchanged scope.
```

### Final

```text
Mode: FINAL_BOUNDED
Independently verify the current complete diff and highest-risk changed path. Do not audit the repository or strengthen the contract.
```

## Delegated companion contract

The installed companion uses `context=DELEGATED_PASS` (delegated-pass.md). Parent alone owns admission/acceptance; reviewer returns CLEAN, MATERIAL_CANDIDATES, or INSUFFICIENT_EVIDENCE. The parent closes with two independent clean coverages using its embedded profile, both covering the final candidate. `unproven_composition` controls whether another integration reviewer is needed, not whether required checks run.

## Final-candidate discovery is not a retrospective audit

A's valid coverage may be carried forward with affected-edge verification. After B reports a material defect and it is repaired, obtain B's FINAL_BOUNDED over the current complete PLAN/parent and direct neighbors; do not limit it to the last patch or claim unchanged code was proved correct merely because a previous pass missed it. This is not a whole-repository audit or a fresh A+B streak. Keep the original cumulative budget and actual B identity. Retrospective cost/quality analysis belongs to general-audit; current required behavior and real consumers do not. See reviewer-orchestration.md for the single authority on round sequencing.
