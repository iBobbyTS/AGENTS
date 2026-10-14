## Debugging skill routing

Apply this routing before selecting a debugging skill:

- On the first attempt, solve a clearly local, deterministic, low-risk issue directly **without** invoking `$adaptive-debugging` when the exact cause is apparent, the change is isolated, and the original symptom can be verified immediately.
- Invoke `$adaptive-debugging` **before a second repair attempt** whenever the first proposed or applied fix did not eliminate the original failure.
- Invoke `$adaptive-debugging` immediately when the initial issue is intermittent, cross-layer, environment/CI/production-only, concurrent, performance- or memory-related, a crash/hang/data-integrity issue, expensive to reproduce, or involves networking, containers, database locks/transactions, Swift/macOS runtime behavior, signing, notarization, Gatekeeper, sandbox, or entitlements.
- When `$adaptive-debugging` is active, do not also invoke another generic systematic-debugging skill for the same investigation. Domain-specific tools or references may still be used.
- A failed fix is evidence. Do not stack guesses; return to root-cause localization.
