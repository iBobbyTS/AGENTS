# Full-stack planning

Axis: `domain` (cross-layer application delivery). Language, framework and platform are separate evidence-based routes.

Select when one requested outcome crosses client/UI, server/service and its response or data consumers, even inside one SvelteKit repository. Combine with actual language/framework files; never infer a Java backend from “full stack.” Use [boundary-handoff](../boundary-handoff.md) once.

## Inspect before choosing sections

Trace the real interaction: component/client action → request builder → route/auth → service/data owner → response encoder → client decoder/state update → other named readers. Find actual serialization, authorization and ordering conventions; do not infer a backend stack from UI dependencies.

## Answer only changed-seam questions

| Question | PLAN contribution |
|---|---|
| Is the client calling an action, REST endpoint, RPC or form? | Exact input/envelope/decoded result example with source path |
| Does displayed data represent a subset? | Visible/enabled/paginated/global set semantics on both sides |
| What happens after successful persistence? | State refresh/optimistic replacement, sibling readers and cache invalidation actually needed |
| What does failure leave behind? | Validation rejection vs network loss vs committed-but-unacknowledged; rollback only when justified |
| Which consumers are named by the requirement? | Each gets an edit owner or evidence-backed unchanged verification |
| What must be executable before the next worker starts? | Producer fixture/real client code and accepted dependency or same-parent checkpoint |

Preserve identity, status/error mapping, numeric/date representation and absent values where crossing the wire can change meaning. Do not add concurrency/risk guarantees simply because client/server are separate.

## Decomposition

Use a vertical business parent. Producer persistence and UI integration can be serial subsections with explicit shared examples; they do not receive separate acceptance if both are needed for the outcome. If one producer is independently useful, document its safe intermediate consumer and defer only clearly excluded future behavior. Avoid a test/docs/registration-only final section hiding an incomplete feature.

Parallel consumers require an already agreed usable producer contract, isolated worktrees/resources, and the reviewed PLAN's explicit permission. A mocked interface does not authorize concurrent edits to its owner.

## Smallest meaningful acceptance

Use one representative round trip through the actual client and server adapter and one activated failure. For reorder/save UI, use at least two distinguishable items, relevant subset members, actual response shape and retry/rollback behavior. A one-item render proves layout only. Test the named sibling reader when global state is part of the requirement.

Use an existing integration or component setup. Keep backend contract evidence separate from browser-only state evidence and state the remaining authenticated/real-service gap. Do not demand production access just to make the PLAN pass.

## Exclude

No automatic BFF, shared schema package, schema/codegen migration, distributed transaction, global cache, new auth framework or generalized end-to-end harness. Their necessity must come from the approved outcome/source, not this playbook.

## Sources

[Google small changes](https://google.github.io/eng-practices/review/developer/small-cls.html); [consumer tests](https://docs.pact.io/consumer); [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html). Methods are adapted; no Pact/OpenAPI adoption is required.
