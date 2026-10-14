# PowerShell

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed .ps1/.psm1 or PowerShell command/parameter logic.

Do not select merely because the target is Windows; PowerShell may be cross-platform and Windows may use other languages.

## Decisions before sectioning

- Confirm PowerShell edition/version, module imports and host platform.
- Distinguish object pipelines and parameter binding from native argv/stdout; do not paste Bash quoting rules.
- Name terminating/non-terminating errors, native exit status, encoding and remote/session lifetime when changed.

## Handoff and smallest useful evidence

Use the real command pipeline with representative object/property binding and a failure; inspect actual values rather than formatted display text.

## Scope boundary

No execution-policy weakening, administrator escalation, remoting framework or Bash emulation. No route creates a product requirement, extra review or new test framework.

## Sources and status

[PowerShell pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
