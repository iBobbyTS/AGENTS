# Services and end-to-end business actions

**Use when:** a request, job or event promises a business result across entry points, authorization, persistence and downstream effects. Full-stack paths can belong here without separate frontend/backend audits.

**Misleading reassurance:** each handler validates its own input and every component has tests, but no test carries the same identity, version and payload through the real composition.

**Investigate:** choose a consequential action. Trace who can initiate it, where the decision becomes authoritative, what is durably committed, what the caller is told, and what another consumer subsequently sees. Look for different rules between API, background worker, CLI, webhook or admin paths. Compare missing/null/zero values, units, identifiers, serialization and error meaning only where consumers actually depend on them.

**Distinguish:** drive the same permitted and rejected scenario through applicable real entry points. Include one supported interruption or changed-state case near the decision/effect boundary. Check persisted and downstream state, not just HTTP success. For an event path, inspect replay/duplicate behavior and the acknowledgement point; select the async/durable-state card when that uncertainty matters.

**Counterevidence:** shared authoritative validation, an enforced invariant at the state owner, or an explicitly different adapter contract may make local inconsistency harmless or intentional. Do not require all adapters to have identical syntax, nor invent transactions across unrelated operations.

**Expand/stop:** follow shared decision helpers and real consumers of a broken contract. Stop where source and configuration establish containment. Treat an inaccessible third-party guarantee as a named dependency, not proof of local failure or safety.

The scenario method is not a prescribed enterprise readiness checklist.
