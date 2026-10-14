---
name: code-review
description: "Evidence-based review of a PR, commit range, section or repair delta. In delegated sectioned-feature-development mode, execute one bounded checkpoint, reconciliation or full pass and return candidates/coverage without taking over admission, implementation or acceptance."
---
# Code Review

## Select execution context first

- `DELEGATED_PASS`: parent provides a frozen packet; read [delegated-pass.md](references/delegated-pass.md). Protocol: [delegated-pass.md](references/delegated-pass.md). This path overrides standalone loops/acceptance below.
- `STANDALONE`: direct user review request; follow [standalone-workflow.md](references/standalone-workflow.md). Default review-only; no repairs without authorization.

No worktree writes, nested reviewers, changed requirements, invented test authority, or acceptance verdict in a delegated pass. Report candidates, causal evidence, checks and inspected boundaries. A code-review invocation is one task, not a second orchestrator.

Load [review-coverage.md](references/review-coverage.md) for triggered correctness lenses and [ai-agent-risk-catalog.md](references/ai-agent-risk-catalog.md) only when relevant to the changed behavior. Historical review loop documentation is standalone-only.

## Role, provider and parent handoff

`$code-review` is this review method, not a provider alias. Never forward a delegated task to another reviewer or transport, and never relabel a result as another provider's. Main owns dispatch, rounds, admission and the release of successors.
