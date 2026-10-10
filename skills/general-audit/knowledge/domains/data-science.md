# Data pipelines, numerical and scientific software

**Use when:** a pipeline, backfill, analysis or physical/numerical transformation must produce correct and complete results. AI-authored software is not automatically this domain.

**Misleading reassurance:** processing finished, row counts match and output hashes are stable, but values, population, units or the scientific interpretation are wrong. Small jobs pass while continuation changes behavior.

**Investigate:** name the expected population and each transformation's contract, including identities, time/window boundaries, units, precision, missing values and duplicate/late records where applicable. Trace selection → transformation → persisted output → consumer. Separate successful rows, intentionally deferred records and actual failures. Determine whether checkpoint meaning survives process restart.

**Distinguish:** reconcile a small independently derived fixture and a realistic boundary-sized case through the real entry point. Check aggregate and per-record invariants; test interruption/resume when it is a supported path. Use a trustworthy reference, conservation/monotonicity relation or analytically known case only when its preconditions hold. For ML evaluation, examine train/evaluation isolation and preprocessing ownership, not just the score.

**Counterevidence:** numerical tolerances and approximation can be valid requirements. Missing/late data can be intentional rather than corrupt; deferred work can be correct if its liveness contract is explicit. A prior implementation can reproduce a prior bug, and a physically plausible output is not proof of calibration.

**Expand/stop:** follow discrepancies to the selection or transformation owner. Without real measurements or deployment data, separate software evidence from scientific/operational validity. Never demand new expensive data collection simply to finish a code audit.

Probe designs are audit hypotheses, not universal numerical laws.
