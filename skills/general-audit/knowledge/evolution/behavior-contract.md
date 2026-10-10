# Behavior and scope drift

**Trigger:** replacement/refactor, large milestone, repeated “fixes” changing normal behavior, new generated requirements or mismatch between actual users and test scenarios.

**Hypothesis:** internally consistent code/tests satisfy a contract reconstructed from the implementation, not the intended product; a rewrite preserves unreachable platform machinery but loses reachable business semantics; intentional new behavior is incorrectly labeled regression.

**Distinguish:** establish a small set of supported scenarios from independent user decisions/contracts/consumer behavior before reading the new implementation as the answer. Compare observable effects, error meaning and ownership across the real path. Legacy behavior is characterization evidence, not automatic authority to preserve known defects. Explicit changes/exclusions need their real decision source. For a migration, distinguish required compatibility from deliberately retired behavior.

**Counterevidence:** an approved product change can invalidate old goldens. A temporary adapter may support an actual version cohort. Missing undocumented arbitrary framework behavior is not automatically a defect in a bounded business rewrite.

**Expansion:** check sibling consumers affected by the changed semantic assumption. Don't inventory every historical language/runtime feature or turn a local inconsistency into a new product roadmap. If authority conflicts, expose the product decision needed rather than select whichever behavior currently passes.

**Closure:** supported intended outcomes are traced to actual observations, or a precise missing/extra behavior is linked to consequence and authority. Knowledge about independent test expectations remains in [oracles](../evidence/oracles.md).

Project constraints are authority only where actually applicable.
