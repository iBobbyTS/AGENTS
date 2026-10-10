# Trust in the verification system

**Trigger:** escaped defects despite green tests, major test rewrites, long/flaky suites, suppressed checks or critical behavior with unclear evidence. No CI by itself is not a trigger for infrastructure work.

**Hypothesis:** the available verification selects convenient behaviors rather than consequential ones; expensive/flaky checks are bypassed; existing regression checks no longer discriminate the original bug; coverage numbers disguise a missing consumer layer.

**Distinguish:** choose a small number of important outcomes and trace which existing test/manual observation would fail for a plausible incorrect implementation. Use [oracles](../evidence/oracles.md) for expected-result independence and [population](../evidence/population.md) for what really executed; don't duplicate those checks. A focused mutation/fault or replay of a representative known defect can test discrimination, under audit permission and without editing the product. Compare failing/ignored tests and rerun policy with the claims people rely on.

**Counterevidence:** not every layer needs its own harness. A cheap consumer integration test may subsume multiple mock-level checks. Manual evidence can be appropriate for a supported small project. A mutation equivalent under the real contract is not a test failure, and a high mutation score is not a correctness certificate.

**Expansion:** follow a recurring blind spot or workflow that masks red results. Don't install new frameworks or run whole-repository mutation campaigns just to raise a metric. For costly suites, select representative high-consequence paths and preserve missing breadth.

**Closure:** demonstrate a meaningful incorrect behavior is distinguished, or identify the precise missing verification and its consequence. Recommend the smallest improvement to the real evidence system, not blanket coverage targets.
