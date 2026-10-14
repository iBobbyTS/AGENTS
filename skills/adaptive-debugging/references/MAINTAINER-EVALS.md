# Maintainer Trigger and Behavior Evals

Use these cases after changing `name`, `description`, `openai.yaml`, or the routing rules.

## Expected not to invoke implicitly

1. “TypeScript says `Cannot find name 'usreId'`; the variable two lines above is `userId`. Fix it.”
   - First occurrence, deterministic, local typo, direct verification.
2. “Python fails with a syntax error because this dictionary is missing a comma. Correct it.”
3. “The local dev command uses `config/prod.json`; the documented file is `config/dev.json`. Change that one path and rerun.”
4. “This module imports `Buttonn`, but the exported symbol is `Button`. Fix the import.”

Expected behavior: direct localized repair, rerun the exact failure, no persistent debug session.

## Expected to invoke implicitly

1. “The fix you made yesterday did not stop the request from occasionally returning stale data.”
   - Hard trigger: previous fix failed; likely cross-layer/state.
2. “A Playwright test fails only in GitHub Actions and only when the suite runs in parallel.”
   - Load test flakiness, build/CI, browser, and possibly concurrency.
3. “The API sometimes deadlocks during concurrent check-in and PostgreSQL reports lock waits.”
   - Load backend, database, concurrency.
4. “The macOS app works from Xcode but Gatekeeper blocks the downloaded zip on another Mac.”
   - Load macOS signing/sandbox and build/CI.
5. “A SwiftUI app freezes for several seconds after importing a large file; CPU and memory are unclear.”
   - Load Swift/macOS native and performance.
6. “Docker Compose says healthy, but requests intermittently time out between two services.”
   - Load Docker, network, backend.
7. “Memory grows after every navigation and does not return after leaving the screen.”
   - Load performance plus the platform-specific playbook.
8. “We cannot reproduce the production crash locally; here is a crash report and dSYM.”
   - Load Swift/macOS native; preserve artifacts and symbolicate.

## Explicit invocation

Prompt: “Use `$adaptive-debugging` for this obvious missing import.”

Expected behavior: skill loads, declares lightweight mode, confirms direct evidence, repairs once, verifies, and does not load unrelated playbooks.

## Process behavior checks

For each complex case, verify that the agent:

- writes a failure contract before repair;
- identifies the invocation trigger and selected domains;
- distinguishes observation from hypothesis;
- states a prediction before a discriminating experiment;
- does not use retry, sleep, cache deletion, broad permission changes, or a dependency upgrade as an unproven fix;
- returns to localization after a failed repair;
- stops speculative patching after two independent repairs fail;
- verifies the exact original failure contract;
- reports remaining uncertainty honestly.

## Conflict eval

With Superpowers `systematic-debugging` also enabled, prompt with a trivial typo. If both skills activate or conflicting instructions appear, disable the Superpowers debugging skill as documented in `README.md` and rerun. Other Superpowers skills may remain enabled.
