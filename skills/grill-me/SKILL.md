---
name: grill-me
description: Requirements-focused interview that finds omitted product and behavior details, resolves only human-owned semantic decisions, and leaves architecture and code-level choices to the agent. Use when the user can already describe what they want but wants gaps, edge cases, constraints, and acceptance criteria surfaced before planning or implementation.
disable-model-invocation: true
---

# Grill Me — Requirements-Only

Sharpen the user's requirements before planning or implementation. The goal is **requirement completeness and shared product semantics**, not architecture design.

The user owns decisions about what the product should do. The agent owns fact-finding and technical design.

## Start by learning, not asking

Before asking the user anything, inspect the available environment when relevant: repository code, tests, docs, issues, existing UX, schemas, configuration, and nearby behavior.

Do not ask the user for facts that can be established from the environment. Do not ask them to repeat requirements they already stated clearly.

If a formal spec or plan already exists, treat settled statements in it as requirements unless they conflict with newer user instructions. Focus the interview on omissions, ambiguity, and contradictions.

## Classify every uncertainty before asking

For each uncertainty, put it into exactly one of these buckets:

1. **Discoverable fact** — investigate it yourself.
2. **Technical or architectural choice** — leave it to the planner/implementer; do not ask the user.
3. **Human-owned product semantic** — ask the user if it materially affects the contract.
4. **Low-impact or safely inferable detail** — follow existing product conventions or a reversible default; record the assumption if useful, but do not interrupt the user.

A question belongs to the user only when different answers would materially change one or more of:

- externally observable behavior;
- business or domain meaning;
- permissions or actor capabilities;
- user-visible data lifecycle or compatibility semantics;
- scope or explicit constraints;
- failure, conflict, or recovery behavior users depend on;
- acceptance criteria or what counts as done.

### Do not make the user design the implementation

Do **not** ask the user to choose architecture, module boundaries, class structure, API shape, database schema, transaction structure, queues, caches, libraries, frameworks, algorithms, internal naming, test organization, or similar implementation details.

When a technical choice has user-visible consequences, ask for the desired outcome or constraint instead of the mechanism.

Examples:

- Do not ask: “Should this use a background job or run synchronously?”
  Ask only if needed: “Does the user need the result before leaving this screen, or may it complete later?”
- Do not ask: “Should duplicate handling use an upsert?”
  Ask: “If an imported record already exists, should the product update it, skip it, or reject the import?”
- Do not ask: “Should this be one transaction?”
  Ask: “If one item fails, should successful items remain applied or should the whole operation fail?”

If the user explicitly delegates a product decision with “you decide” or equivalent, choose the recommended default, record that delegation, and move on.

## Run a requirement coverage scan

Use the following as a **coverage checklist, not a questionnaire**. Only surface categories that are relevant to the requested change and still materially underspecified.

- goal, user outcome, and success condition;
- actors, roles, ownership, and permissions;
- entry conditions, happy path, and completion state;
- inputs, validation, defaults, and malformed input;
- outputs, user feedback, empty/no-op states, and discoverability;
- error handling, partial failure, retry, cancellation, and recovery;
- duplicates, repeated actions, conflicts, and concurrent changes;
- state transitions, lifecycle, deletion, restore, and irreversible actions;
- interaction with existing data and backward-compatibility expectations;
- ordering, time/date boundaries, quantities, rounding, or other domain boundaries when relevant;
- user-visible limits or latency expectations when they are product constraints;
- history, auditability, notifications, or confirmation when the domain makes them relevant;
- explicit in-scope and out-of-scope boundaries;
- acceptance criteria and meaningful edge cases.

Do not invent speculative edge cases merely to exhaust this list. A candidate question must pass the materiality test above.

## Maintain a requirements decision tree

Model unresolved requirements as a dependency tree. Resolve prerequisite semantics before asking questions that depend on them.

After each answer:

1. update the tree;
2. prune branches the answer resolved;
3. re-check the environment for facts that can now settle downstream questions;
4. identify the highest-impact unresolved human-owned semantic on the current frontier.

The purpose of the tree is convergence, **not exhaustive traversal of every conceivable branch**.

## Ask one decision at a time

Ask exactly one material decision at a time and wait for the user's answer before continuing.

For each question:

- state the concrete product behavior being decided;
- give a recommended default;
- briefly explain why that default best fits the known requirements and existing behavior;
- when useful, state the consequence of the main alternatives.

Prefer concrete choices over abstract prompts. Keep free-form answers available when the options cannot capture the domain.

Do not ask vague questions such as “Any other edge cases?” or “How should this be architected?” Surface a specific omission instead.

## Minimize interruption

Do not ask merely because a detail is unspecified.

Skip a question when all of the following are true:

- existing product behavior provides a strong precedent;
- choosing that precedent is reversible and low-risk;
- the choice does not materially alter product semantics or scope.

When several possible questions exist, prioritize by:

1. behavior or data semantics that could make an implementation wrong;
2. permissions, destructive behavior, failure semantics, and compatibility;
3. scope and acceptance criteria;
4. ordinary UX details;
5. cosmetic or easily reversible preferences.

After roughly eight user questions, perform a convergence check. Continue only for unresolved **high-impact** human decisions. Do not continue a long interview just to eliminate low-impact uncertainty.

## Stop at the product/technical boundary

The session is complete when all remaining uncertainty can safely be delegated to planning and implementation **without changing the user-visible requirements contract**.

Do not wait for every internal implementation decision to be known. Do not expand the interview into architecture planning.

At completion, produce a compact **Requirements Contract** containing only applicable sections:

- **Goal / success condition**
- **Actors and permissions**
- **Required user-visible behavior**
- **Edge, error, conflict, and recovery semantics**
- **Constraints**
- **Existing-data / compatibility semantics**
- **In scope**
- **Out of scope**
- **Acceptance criteria**
- **Confirmed human decisions**
- **Assumptions adopted from existing conventions**
- **Planner discretion** — technical choices intentionally left to the agent
- **Unresolved blockers** — must be empty before the requirements are considered ready

Ask the user to confirm that this contract matches their intent.

Do not implement, refactor, choose architecture in depth, or begin a plan as part of this skill. After confirmation, stop and hand the Requirements Contract to the next workflow stage unless the user explicitly asks you to continue.
