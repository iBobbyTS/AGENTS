# Scientific / numerical / simulation software

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

The change computes a scientific/numerical result or modifies a simulation/analysis contract.

Do not select merely because Python/R/C++ exists; the domain follows the task outcome.

## Decisions before sectioning

- State quantities, units, coordinate/time conventions, tolerances and a reference calculation.
- Separate algorithm/model choice from implementation/optimization; confirm authority before changing scientific meaning.
- Record input size, numerical conditioning, deterministic/stochastic assumptions and actual hardware/library effects where relevant.

## Handoff and smallest useful evidence

Use analytical/conservation/reference fixtures and numerical tolerances through the real computation. Benchmark on justified input shapes only; a seed does not promise identical results on every platform.

## Scope boundary

No new scientific claim, statistic/metric change, GPU rewrite, benchmark suite or universal determinism guarantee. No route creates a product requirement, extra review or new test framework.

## Sources and status

[R language definition](https://cran.r-project.org/doc/manuals/r-release/R-lang.html); [PyTorch reproducibility source](https://raw.githubusercontent.com/pytorch/pytorch/main/docs/source/notes/randomness.md). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
