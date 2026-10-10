# Accumulation in AI-led development

**Trigger:** long-lived agent-authored code, plans/tests/docs generated together, repeated pattern copying, fragmented sessions or delegated implementation. These are opportunities to investigate correlated assumptions, not proof that AI caused a defect.

**Hypotheses worth distinguishing:** a plan invented a requirement and tests now enforce it; an implementation mistake became the oracle; a workaround spread to siblings; “completed” artifacts hide an unimplemented consumer; ownership changed but entry points/runbooks still point elsewhere; several agents each tested their side of an incompatible seam.

**Investigate:** choose a critical outcome or repeated repair hotspot. Reconstruct the requirement from explicit decisions and actual consumers independently of the latest plan. Compare current code with the relevant accepted boundary and targeted history, not every session ever recorded. Follow a real value through producer and consumer. Inspect why a regression test expects that result. When summaries claim review/test execution, reconcile a meaningful sample with actual invocations/results if available.

**Counterevidence:** generated artifacts can be correct and valuable; human-authored tests can share the same circularity. A locally unusual abstraction may enforce a real contract. Do not infer defect probability, model identity or poor quality from authorship labels.

**Expansion:** if one copied mechanism is wrong, inspect plausible siblings and the shared origin. If summaries selectively omit failed work, investigate the relevant evidence population, not every private transcript. Seek the actual cause before adding a harness rule.

**Closure/learning:** a useful lesson identifies a repeatable trigger and decisive check. Mechanical invariant checks may be cheaper than longer prompts, but only encode a validated, stable project invariant. Retire obsolete model-specific workarounds.
