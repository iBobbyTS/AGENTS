# Debugging Completion Report Template

Use this structure. Omit sections only when genuinely inapplicable.

## Status

`fixed` | `not fixed` | `blocked by missing evidence` | `mitigated, root cause unresolved`

## Failure contract

- **Expected:**
- **Observed:**
- **Reproduction/observation:**
- **Environment/build:**
- **Impact:**

## Root cause

State the causal mechanism, not only the failing component.

```text
trigger → first divergence → propagation → observed symptom
```

## Decisive evidence

- Failing observation:
- Passing control/counterfactual:
- Relevant trace, crash UUID, request ID, query, profile, or test artifact:
- Contradictory hypotheses ruled out:

## Repair

- Files/configuration/artifacts changed:
- Why this change addresses the causal source:
- Intentional behavior or contract changes, if any:
- Temporary instrumentation removed or retained:

## Verification

- Original reproduction result:
- Regression test/result:
- Neighboring checks:
- Environment/build/distribution parity:
- Repetition/stress evidence for intermittent failures:

## Prior failed attempts

Summarize what was tried and what was learned.

## Remaining uncertainty and follow-up

State residual risk, untested environments, observational limits, or operational mitigation. Do not present uncertainty as resolved.
