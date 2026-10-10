# Bash / POSIX shell

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed shell scripts or shell command composition.

Do not select merely because a command is executed somewhere; PowerShell and other shells have different languages.

## Decisions before sectioning

- Confirm shebang, dialect, platform utilities and native command versions.
- Separate argument arrays from interpolated command text; handle spaces, newlines, quoting and option terminators where affected.
- Name pipeline exit behavior, traps, temporary-file ownership and partial side effects without relying on set -e as universal rollback.

## Handoff and smallest useful evidence

Execute the actual script with a path containing spaces and a relevant child failure; reuse available shells and existing lint/tests, not a new orchestration framework.

## Scope boundary

No blanket shell-to-Python rewrite, destructive cleanup, assumed GNU utilities on all hosts or global permission changes. No route creates a product requirement, extra review or new test framework.

## Sources and status

[GNU Bash manual](https://www.gnu.org/software/bash/manual/html_node/Shell-Syntax.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
