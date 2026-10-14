# Section Planning

## Contents

1. [Purpose](#purpose)
2. [Choose the first slice](#choose-the-first-slice)
3. [A valid section](#a-valid-section)
4. [Structural allowance](#structural-allowance)
5. [Boundaries and deferred work](#boundaries-and-deferred-work)
6. [Invalid section patterns](#invalid-section-patterns)
7. [Plan-review gate](#plan-review-gate)
8. [Triggered plan-review lenses](#triggered-plan-review-lenses)
9. [Examples](#examples)
10. [Composable knowledge](#composable-knowledge)

## Purpose

Sectioning reduces cognitive and integration risk only when each section represents one coherent behavior increment. Splitting by directory, layer, or evidence artifact can make the plan longer without making the change safer.

For a qualifying multi-session program only, use [long-horizon planning](long-horizon.md) to separate the complete roadmap from the small working horizon. A milestone spanning several independently failing production state machines is not one bounded section; a high section count alone does not prove reviewability. This adds no ordinary-task phase.

The plan should answer:

- What did the user actually request, in their own words?
- Which explicit examples, failing cases, counterexamples, or later corrections constrain that request?
- What is the smallest end-to-end behavior that satisfies the current, non-superseded request?
- What observable behavior becomes true after this section?
- Which external authority makes this section necessary, and why is a smaller existing path insufficient?
- Which existing owner is responsible?
- What exact code and semantic impact cone may change?
- Which behavior is deliberately not part of this section?
- What evidence is sufficient to accept it?

## Composable knowledge

Before drafting section boundaries, read [planning/router.md](planning/router.md) once and select knowledge for the changed path. Consult [planning/index.md](planning/index.md) only for uncertain dimensions; read the matching specialized guides needed to resolve the actual boundary. Use universal only for a named uncovered part after index consultation and matched-guide reading; do not substitute universal for an available relevant guide. This is the existing PLAN phase, not an extra review, pass, script or user approval.

Record the four-axis assessment, paths actually read, short evidence-based reasons and any named universal fallback in the existing PLAN routing paragraph. Resolve overlapping advice into one boundary/example and one check. The independent PLAN reviewer checks the recorded route against source, consulting the planning index only for a material unresolved match; the author's selection list is evidence, not the entire available library. Do not supply the author's prior conversation or another reviewer's verdict. A missing route name or unselected irrelevant checklist item never blocks; a concrete failure needs existing authority.

For producer/consumer work, use [boundary-handoff](planning/boundary-handoff.md): original example -> actual request serialization -> owner/state -> response -> actual named consumers. Label source-inspected, observed, planned and unknown evidence. PLAN can specify a future test and its create-before-run owner; it need not execute unfinished code. Handoff replaces planned samples with actual producer evidence; consumers must use the same real shape.

If a user-named downstream reader needs changes, give it an edit owner now, not only inspect permission or a late cleanup section. If unchanged, explain the source/check proving preservation. Do not split one invariant just to match library files or model names. Reuse the existing parent/subsection, assurance, scope and finite review policies below.

## Choose the first slice

When an external seam or architecture assumption is uncertain, begin with the smallest real probe or walking skeleton that can falsify the assumption. Authentication method, endpoint, response shape, protocol, or third-party semantics are not stable plan inputs unless repository source/docs make them authoritative.

Examples:

- Observe the actual request metadata shape before building a registry around it.
- Exercise one canonical provider call before creating a general provider framework.
- Modify one representative route and reload flow before building a whole-repository URL analyzer.
- Prove the current persistence owner and failure behavior before introducing an outbox or journal.

A probe should produce durable knowledge or a minimal production path. It should not become a second framework.

## A valid section

A section should normally have:

- one primary behavior owner;
- one coherent outcome;
- one authority anchor outside the plan itself and a necessity statement tied to the minimum feature outcome;
- one bounded changed contract;
- one frozen scope manifest separating allowed-to-edit owners from inspect-only dependency paths and explicit exclusions;
- one direct semantic impact cone;
- one review intensity (`MECHANICAL`, `BOUNDED`, or `HIGH_RISK`);
- fixed two-clean-round acceptance with the embedded profile's reviewer routes;
- one set of targeted tests;
- no undocumented dependency on a future section for correctness.

Section IDs are handles for `.agent-work/` plan, packet and ledger files only. Repository artifacts — file and directory names, tests, fixtures, docs, configuration, identifiers, UI strings, code comments — are named after the feature or behavior they own (`tests/runtime-selection.test.mjs`, `docs/gap-handoff.md`), never after a section ID or any other SFD process label; when a repository artifact name would otherwise collide or be too generic, record a feature slug in the plan and use that.

Branch names and commit messages on delivered history follow the same rule: the feature branch and each commit message are named after the feature or behavior they carry, never after a section ID or any other SFD process label — including commits serialized from parallel worktrees. The short-lived parallel worktree branches and directories [parallel-execution.md](parallel-execution.md) prescribes are process infrastructure, not delivered artifacts, and keep their section-based names.

A section may touch multiple files and layers when those edits are required for one vertical behavior. File count alone does not define reviewability.

The section graph is not allowed to create its own requirements. A downstream section cannot be justified only because an upstream plan promised a new UI, proof harness, compatibility layer, status surface, or generalized mechanism. Trace it back to user intent, a current repository/production obligation, or a demonstrated correctness dependency; otherwise remove it from the feature.

Prefer sections such as:

- “Parse and normalize the quota signal at the existing API boundary.”
- “Keep one turn bound to its selected account until a confirmed quota terminal signal.”
- “Remove report month/year from the page URL while preserving reload defaults.”
- “Expose DeepSeek's single-query capability through the existing provider projection.”

Avoid sections such as:

- “Backend changes.”
- “Security hardening.”
- “Build a generalized URL governance system.”
- “Rehabilitate review evidence.”
- “Final cleanup and everything else.”

## Structural allowance

Every section contract includes an **Allowed structural changes** list. This is an authorization boundary, not a prediction.

List only mechanisms required by the approved behavior, for example:

```text
- Extend the existing AccountRegistry with one per-turn affinity map.
- Add one provider capability enum value and reuse the existing projection path.
- Add explicit route-level regression tests in the existing test module.
```

When the list is empty, the implementer may make local edits and small local helpers inside the allowed-to-edit manifest but may not add a new service, registry, persistence layer, background worker, parser framework, global analyzer, CI policy, public config surface, or security subsystem.

A reviewer cannot add an item to this list or expand the allowed-to-edit manifest. It may inspect an unlisted dependency only through a recorded causal chain from changed code. A required new mechanism or repair owner is either:

- already implied by an authoritative repository contract and accepted by the main agent; or
- a product/architecture decision for the owner.

## Boundaries and deferred work

Write non-goals as concrete exclusions, not generic “out of scope” prose.

Good examples:

- No multi-process durability or restart persistence.
- No replay after downstream bytes have been emitted.
- No same-UID hostile process model.
- No whole-repository source analyzer or permanent CI prohibition.
- No public Admin DTO exposure until S04.

Deferred work must have a named later owner and a correct intermediate state. A reviewer may block on deferred work only when the current state is already incorrect or unsafe before the later section runs.

## Invalid section patterns

### Process-only section

Do not create a section only to:

- move a test earlier in Git ancestry;
- obtain a “clean lineage”;
- re-prove accepted predecessor behavior unchanged by product code.

### Governance expansion

A local feature does not automatically authorize a repository-wide analyzer, policy, registry, or CI guard. Prefer explicit regression tests for the changed routes/owners.

### Threat-model expansion

A test harness, local script, single-user tool, or private directory does not automatically require protection against arbitrary in-process objects, same-UID hostile processes, multi-tenant access, or malicious filesystem rebinding.

### Layer-only split

Splitting “models,” “services,” and “UI” into separate sections may leave each section semantically incomplete. Prefer a vertical behavior slice unless compatibility staging requires a layer boundary.

## Plan-review gate

Run one fresh, read-only plan review after `PLAN-FULL.md` passes mechanical validation and before product-code implementation. Its purpose is to catch the wrong plan at lower cost, not to add another design committee.

### Requirement/example traceability

Before review, build a compact matrix:

| ID | Current instruction/example/correction | Supersedes | Acceptance criterion | Test or probe |
|---|---|---|---|---|

Every named real-world failure and expected counterexample must be represented. If the user corrects an earlier implementation direction, mark the old one `SUPERSEDED`; it cannot remain an alternative requirement. This is especially important for bug reports where a generic contract can pass while the reported fixture still fails.

### Review packet

Use [PLAN-REVIEW-REQUEST.template.md](../assets/PLAN-REVIEW-REQUEST.template.md). Provide only:

- original user request, later explicit owner decisions, and the requirement/example matrix;
- minimum sufficient end-to-end outcome and authority map;
- repository rules/current production contracts;
- relevant source/architecture seams needed to verify buildability;
- PLAN-FULL and explicit exclusions;
- validation tiers and any unresolved external assumptions;
- selected planning reference paths/reasons, the shared boundary examples and named consumer ownership (no additional routing report).

Do not prime the reviewer with a desired verdict or proposed additional architecture.

### Permitted checks

Review in this order; do not spend time making an unnecessary mechanism internally perfect:

1. **Necessity:** for every new marker, migration representation, backup/rollback contract, registry, shared abstraction, proof harness, analyzer, or validation obligation, first prove it is required by external authority or unavoidable correctness. Otherwise classify the whole item `PLAN_SCOPE_EXPANSION` and do not generate secondary blockers about its edge cases.
2. **Traceability:** every current requirement/example/correction maps to acceptance evidence, and every behavior/section/UI/config/compatibility surface maps to authority.
3. **Minimum closure:** the plan solves the full user-visible request without optional completeness work.
4. **Buildability:** owners/seams exist, dependencies are acyclic, predecessors produce what consumers need, and uncertain external seams are probed before architecture depends on them.
5. **Ownership coherence:** the plan does not duplicate one semantic rule across owners or stack local guards around a shared defect without an explicit foundational-vs-local owner decision.
6. **Scope proportionality:** no process/evidence-only section, generalized hardening, future-proofing, or proof system; validation is tiered rather than broad-suite-per-edit.
7. **Contract integrity:** section boundaries preserve correct intermediate states and do not hide cross-section API/schema/state mismatches.
8. **Review proportionality:** two clean rounds are fixed; actual semantic risk determines breadth. The embedded dispatch profile supplies the reviewer routes. Do not add review rounds from module labels, repository size or test count.

Within these checks, verify that a selected domain/language/adapter/concern really occurs in the changed path and the concrete example survives the actual producer/consumer boundary. An asserted behavior of an external system is verified at its consumption site ([boundary-handoff](planning/boundary-handoff.md)): a definition-site citation alone is an evidence gap, not coverage. Route omissions matter only if they expose a material plan defect; a playbook suggestion alone is `PLAN_NIT` or `PLAN_SCOPE_EXPANSION`, not new authority. Distinguish PLAN_OMISSION from PLAN_ALREADY_REQUIRED_BUT_NOT_IMPLEMENTED; `PLAN_ALREADY_REQUIRED_BUT_NOT_IMPLEMENTED` is not solved by extending the plan indefinitely.

It does not perform repository audit, propose a preferred architecture merely because it is cleaner, add unrequested edge cases, or write implementation details beyond the minimum correction needed to make the existing plan executable.

## Triggered plan-review lenses

Apply these only when the planned change activates the corresponding semantic risk. They sharpen the existing plan review; they do not add a second reviewer or broaden the product.

### Representation and precedence lens

For a data/config/schema/model-shape change, enumerate the existing representations that produce, normalize, persist, override, project, edit, or default the value. Freeze:

- missing vs explicit `null`, zero, empty, masked, sentinel, placeholder, and legacy-absent states when they have distinct semantics;
- authoritative producer and fallback/default producers;
- whether fallback depends on **presence** or **validity/eligibility**;
- persisted override and merge/shadow precedence;
- server -> serialized JSON -> browser/runtime representation -> input/editor -> save round-trip, including numeric range/precision limits;
- compatibility/removal behavior actually requested;
- one acceptance case proving every newly required field survives the authoritative path.

This catches plans that update the canonical resource but omit saved overrides, materialized defaults, third-party presets, explicit-null semantics, fallback ordering, or browser representation. Do not turn the matrix into a repository-wide schema inventory.

### Foundation-versus-local-patch lens

Apply when a plan would implement the same validation, normalization, routing, persistence, selection, or state-transition rule in more than one owner, or when local guards are being stacked around a defect owned by a shared component.

The reviewer must identify:

- the existing authoritative owner, if one exists;
- which sibling callers remain wrong under the local-patch option;
- the smallest bounded foundational correction;
- the smallest local correction and its explicit residual duplication/risk.

When changing the foundation materially widens scope, classify this as `OWNER_DECISION` and present only those two bounded alternatives. Do not silently choose the wider foundation change, and do not create a service/framework. A cosmetic helper extraction, one-field dictionary wrapper, or single-use abstraction is `PLAN_NIT`, not a blocker.

### Lifecycle and failure-state lens

For async requests, retries, replay, cancellation, process restarts, background work, or UI drafts, write the smallest transition table covering:

- start/in-flight/success/failure/cancel/retry states;
- late or stale result ownership;
- partial side effects and replay eligibility;
- persisted-but-not-applied or stopped-but-recoverable states;
- exact state that a user retry resumes.

The reviewer checks that each accepted failure state has an owner and observable outcome. It must not require a generalized state-machine framework.

### Inventory completeness lens

For version adaptation, migration, source inventory, provider/catalog propagation, or a field rename across representations, require a bounded machine-assisted inventory of the relevant owner class before implementation. The plan reviewer verifies that the inventory method and exclusions are credible and that every discovered owner is assigned or explicitly excluded. It does not conduct an open-ended repository audit or require proof beyond the named owner class.

### Candidate classes and admission

Classify each candidate exactly once:

- `PLAN_BLOCKER`: existing authority or source reality proves the plan is incomplete, contradictory, or unbuildable.
- `PLAN_SCOPE_EXPANSION`: plan item lacks external authority or is not unavoidable; remove/defer it rather than implement it.
- `OWNER_DECISION`: the user/repository owner must decide product semantics, compatibility, migration meaning, threat model, or rollout.
- `PLAN_NIT`: non-blocking wording, formatting, or optional optimization.

Every `PLAN_BLOCKER` must include:

- authority/requirement ID;
- concrete source or repository evidence;
- expected failure if unchanged;
- affected section/owner;
- smallest plan-only correction;
- confirmation that the correction adds no new product guarantee.

The main agent owns admission. Record admission compactly in FEATURE-STATE ledger lines, preserving the reviewers' own report files separately; do not create RAW/ADMISSION pairs. A missing original example/test mapping is a `PLAN_BLOCKER`; an obsolete instruction retained after a user correction is `PLAN_SCOPE_EXPANSION`.

### Sufficient detail, not a fully prewritten implementation

A plan is executable when the required outcome, cross-owner interfaces, current owners, dependency order, allowed edits, meaningful checks and safe intermediate states are clear. A reviewer must identify a concrete ambiguity that could produce an authority-backed failure, not merely request more detail.

- A new test/probe/source file may be absent before implementation when its owning section and create-before-run responsibility are declared. Its absence alone is not a blocker.
- Internal helper names, exact private types/library calls, probe output filenames and private JSON layouts are normally implementer decisions. Freeze them only when an existing public/shared consumer or repository requirement needs that exact contract. Cite that authority; do not turn a suggestion into a new acceptance obligation.
- Review verifies declaration of required checks; it does not require the unfinished feature's tests/build/live results before implementation. Basic section-ID/dependency/role syntax is checked once by the helper; other formatting belongs to the parent and cannot create paid review work.
- Temporary migration coexistence may be explicitly allowed until the consuming section removes the old owner. Do not demand a future consumer/adaptor in an earlier section's acceptance; move that consumer-specific evidence to its owning section or integration.
- Each candidate proposes a bounded correction. The reviewer does not write an admission ledger, approve its own suggested scope, demand an additional full review, or decide that a new R2/R3 label resets the review allowance.

### Finite recheck rule

Both embedded-profile independent PLAN coverages are required ([reviewer-orchestration.md](reviewer-orchestration.md)); both clean records must cover the final executable plan. Main saves the original reports and owns admission. After ordinary corrections rerun the structural validator only if IDs/dependencies/tiers changed. One bounded PLAN_DELTA per originating round verifies admitted material corrections and invalidated coverage; it is not another full review.

No third full pass, repeating committee, recursive planning agent, evidence-only section or matching-hash approval. Report a real unresolved owner/scope/capability decision when bounded closure is exhausted. A rename, changed hash or new reviewer label never resets that policy. No implementer is spawned until both rounds, admission and necessary deltas actually finish.

## Examples

### Account quota switching

Better sequence:

1. Probe actual metadata and terminal signal path.
2. Add minimal per-turn affinity in the existing owner.
3. Add safe switch/replay only for confirmed quota exhaustion before output.
4. Integrate with UI/status if requested.

Do not start with a generalized scheduler, parser framework, persistent registry, or hostile-input model unless required.

Settings/status UI belongs in the feature only when explicitly requested or required by an existing repository product convention. A backend switch mechanism does not automatically authorize a configuration surface or monitoring dashboard.

### Hosted-search provider integration

Better sequence:

1. Exercise one official provider request/response seam.
2. Normalize the minimum result/citation/error contract in the existing provider owner.
3. Activate it through the existing configuration/public path required for actual use.
4. Add focused behavior tests and the repository's existing integration gate.

Do not create a standalone evidence publisher, hostile-object parser, credential-reconstruction proof system, custom compatibility program, or general provider framework unless an external authority independently requires it.

### URL state removal

Better sequence:

1. Remove internal UI state from representative routes.
2. Preserve explicit allowlisted functional query parameters.
3. Add route-level regressions and one browser flow.
4. Integrate across remaining named routes.

Do not add a whole-tree source detector or permanent URL grammar/CI governance system unless the owner requested that separate feature.

## Stage-evidence lessons

Before freezing a relevant parent, include a concrete producer→public entry→consumer path and an executable example. If a consumer needs an increment early, make it a genuinely accepted section; otherwise keep related internal modules as subsections and require parent reconciliation.

For UI async changes, freeze one repeated-event trajectory (edit→save→navigate/close→late result→repeat) and the authoritative pending/identity owner. For representation changes, freeze missing/null/zero/invalid and server→serializer→browser→save round trips. For algorithms, name expected cardinality and a worst-case oracle. For runtime work, state the actual success/terminal/cancel contract and the order of deterministic versus live evidence. These lenses do not authorize unrelated hardening.

Separate PLAN_OMISSION from PLAN_ALREADY_REQUIRED_BUT_NOT_IMPLEMENTED: `PLAN_ALREADY_REQUIRED_BUT_NOT_IMPLEMENTED` needs the exact requirement and production test in the task packet, not more plan reviewers.

Sections are selected by business acceptance; subsection choice must identify a real internal module increment, a meaningful task-model boundary, or both. Never split by LOC alone or manufacture an interface merely to use a cheaper worker — the oracle test separating a legitimate cost-motivated split from manufacturing is in [subsections.md](subsections.md).

## Readable plan contract

PLAN-FULL is Markdown, not a narrative file paired with a machine-readable JSON schedule. The section helper checks IDs, dependency existence/cycles, parent membership and an explicit profile-resolved impl route per unit. Required business authority, constraints, tests and joint oracles remain semantic PLAN-review responsibilities; no fixed heading vocabulary, field count or hash grants approval. Missing formatting alone is not a new review candidate. Ordinary corrected PLAN text can be admitted by main with the original result preserved; changed substantive boundaries receive only the authorized delta recheck.

## Unit size follows the contract, not a worker invocation

Choose a parent by one independently meaningful accepted outcome. Use children for its producer/consumer or state-transition pieces when one packet would hide ownership, repair history or an untested handoff. Freeze their shared contract and joint oracle before splitting; a lifecycle adapter can need separate projection, interaction ownership and reconnect checkpoints without creating three independent products. Do not divide merely by language, line count or number of files.

If one worker will implement two nominal parents with one combined acceptance, decide before PLAN review whether they are really one parent with children. Do not claim two serial parent acceptances from one combined result. Conversely, a small cohesive change does not need a child for every function. Record a one-line parallel/serial reason in the existing plan, using actual owner/contract/resource dependencies; no parallelism quota or extra planning report.
