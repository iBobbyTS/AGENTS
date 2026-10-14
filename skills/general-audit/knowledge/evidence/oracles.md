# Independent expected outcomes and circular proof

**Trigger:** generated tests, snapshots, old/new differential tests, numerical pipelines, hashes/metrics or “all tests pass” used to establish a product claim.

**Hypothesis:** the expected value is derived from the same implementation assumption as the result; both sides of a differential test share a bug; a complete and authentic artifact records the wrong behavior.

**Distinguish:** follow one important assertion back to its source of truth. Is it a user-approved rule, independent calculation, real protocol consumer, domain constraint or merely a captured implementation output? Construct a small case whose expected outcome can be justified without copying the implementation. Use conservation, metamorphic relations or round trips only when they would actually reject the suspected bug; mutually wrong encoder/decoder pairs can round-trip successfully.

Inspect whether changing the suspected rule to a wrong alternative would fail the existing test. Use an isolated mutation/model if safe; do not alter the user's source or regenerate expected snapshots to make tests green. For scientific/ML work, separate data provenance and evaluation isolation from actual validity of the target/measurement.

**Counterevidence:** golden fixtures can be strong when independently reviewed and contract-grounded. Not every test needs a separate human oracle; a well-established invariant or independently implemented reference may suffice. Requiring two models is not an independence mechanism when both read the same erroneous authority.

**Outcome:** report exactly what the evidence establishes. Reproducibility, authenticity, coverage and semantic correctness are different claims. A test gap can explain weak assurance without proving a product defect; a demonstrated wrong value is a finding even if coverage is high.
