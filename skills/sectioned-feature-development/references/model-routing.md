# Task–model routing

The dispatch profile embedded below is this host's only execution route. Main chooses a **logical implementation tier**; the embedded profile fixes each concrete route — native rows name the host agent, external rows name an installer-managed spawn preset carrying subagent, model, effort, permission mode and the role's developer instructions ([external-subagent.md](external-subagent.md)). This is a requested policy, not a claim of cost-optimal capability.

<!-- installer: begin dispatch-profile embed -->
In the repository source the per-host profile tables live in [dispatch/](dispatch/); installing replaces this placeholder block with this host's profile.
<!-- installer: end dispatch-profile embed -->

## Logical implementation tiers

| Tier | Task family | Selection |
|---|---|---|
| impl_std | The packet already resolves what counts as correct: every semantic decision is made before dispatch (frozen contract plus a concrete in-repo analogue), and each governing invariant is independently falsifiable | the embedded profile's impl_std route |
| impl_large | At least one semantic decision must still be made by the implementer, or one invariant bundle is only violated in combination across shared state, or this is a first implementation with no in-repo analogue | the embedded profile's impl_large route |

Three decidable criteria set the tier; none of them is speed, price or token rate. (1) **Ambiguity resolution time**: if the implementer must still decide what counts as correct at any seam, the unit is impl_large no matter how small. (2) **Invariant visibility**: invariants that hold or fail one path at a time support impl_std; a bundle of cross-state invariants whose violations appear only in combination — single-path tests stay green — selects impl_large as a whole. Multiple independently specified requirements mutating the same shared async state (a component/service task lifecycle, save pipeline, or cache) are the canonical bundle. (3) **False-clean rework radius**: when a missed defect repairs locally inside one owner, impl_std risk is contained; when it forces cross-owner rework, that radius — not any model's unit price — is the reason to pay for impl_large.

Decide the tier after assessing how far the packet can be frozen, never before. When the contract can be fully frozen pre-dispatch (frozen table, fixture set, or a pattern precedent from an accepted prior unit), prefer decomposing into impl_std packets at those frozen interfaces; when interleaving semantics can only be resolved during implementation, keep the unit whole on impl_large and do not split it. A first implementation with no in-repo analogue defaults to impl_large regardless of size; conversely, coarse granularity on the higher tier is not itself a defect — never split just to appear economical.

Before PLAN review, every parent and every executable child records its own Implementer (`impl_std` or `impl_large`), rationale and the following task evidence: concrete analogue; resolved/bounded/structural ambiguity; actual producer→normalizer→store→projection→consumer semantic hops; local/shared async or transactional state; whether the governing invariants fail visibly per path or only in combination; decisive/partial/missing oracle; novel reasoning and expected consequence of a false clean. Parent assignment does not fill in a missing child assignment. A two-line concurrency bug may be large; line count and a security label alone do not determine a tier. Do not prewrite every implementation detail, and never split through an invariant bundle to force a cheaper role — [subsections.md](subsections.md) defines when a cost-motivated split is legitimate.

A fresh current plan uses only the two current tiers. Do not rewrite archived plans. The logical tier and its route are plan records; the TASK packet carries no routing metadata.

After a failure first distinguish model/semantic, plan/requirement, environment/tooling and evidence gaps. Only genuine semantic under-routing supports upgrading unresolved work. Record the evidence and adjust affected remaining assignments through a bounded plan delta; never reset accepted work or exhaust a manufactured model ladder. Runtime/auth/MCP errors are not reasons to change model. Missing external configuration blocks the planned route.

## Bounded exploration

Use the embedded profile's explorer route for one bounded owner/consumer/test map when cheaper than main reading directly. Respect applicable CodeGraph exploration rules. Return path/symbol/line, source head, claim→evidence, unknowns and a suggested next read directly in the final answer; usually at most eight source pointers, with an explicit truncation note when necessary. The explorer writes no report file and never touches `.agent-work`. No product decisions, plan rewriting, acceptance or nested subagents.

Requested and observed model/effort are separate facts recorded in the existing ledger fields; whether a wrong-route result may fill an intended slot is judged when the result returns ([reviewer-orchestration.md](reviewer-orchestration.md)), and the efficiency impact of a mismatch is reviewed at the per-section [efficiency checkpoint](efficiency-checkpoints.md). No extra production experiments are authorized for measurement.

## Route substitution

The embedded profile fixes each route. A user-specified route at call time overrides its row for that call: follow the user's request, record the requested and runtime-admitted values, and never relabel the substitution as the profile's default. Independent coverage still shares blind spots: verify with concrete source-derived counterexamples rather than count agreement. Do not split one invariant into artificial cheap tasks to route around the table.

## Escalation

There is no model-level advisor route. For a genuinely unresolved cross-owner/state contract, repeated semantic failure after one evidence-producing correction, contradictory reviewer remedies, or a missing decisive oracle, escalate one bounded question to the external advisor ([advisor-escalation.md](advisor-escalation.md)) — the PLAN advisor at plan stage, the CODE advisor for a repair lineage. An advisor analysis is not a third reviewer appended to every feature, and a solved spelling change or a CLI configuration error is never an escalation.

Each escalation needs a specific unresolved question, consequence, bounded evidence and exit criterion. A budget trigger pauses and diagnoses; it never makes CLEAN optional. Do not infer money or subscription quota from API list prices. Compare physical calls, cache-aware usage, wall time and accepted outcomes only when the same task/head/harness/account evidence supports it; aliases do not prove an exact model release.
