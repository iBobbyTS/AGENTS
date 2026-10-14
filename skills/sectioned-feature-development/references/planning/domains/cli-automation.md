# CLI / automation / developer tooling

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

A requested outcome is a command, build/developer utility, batch script or terminal automation.

Do not select merely because a command is used merely to build a different product.

## Decisions before sectioning

- Freeze arguments/stdin/config precedence, stdout machine format, stderr diagnostics and exit behavior.
- Name target selection, partial side effects, interruption and cleanup; one-off scripts do not imply permanent services.
- Identify installed executable/package and actual downstream parsers, including path/encoding assumptions.

## Handoff and smallest useful evidence

Run actual entry with valid input and a relevant failure/path-with-spaces case; if installation changes, check outside the repository source tree. Keep user data safe and never infer destructive permission.

## Scope boundary

No daemon, config registry, background scheduler, all-environment portability or general command framework. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Python packaging pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/); [PowerShell pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines); [Node streams](https://nodejs.org/api/stream.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
