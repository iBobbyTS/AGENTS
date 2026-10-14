# Git Hook Audit Reminder System

The goal of this system is simple: automatically remind users when a maintainability audit is due whenever they commit changes to a Git-managed project developed with the involvement of AI agents.

## Design Principles

1. Reminder logic belongs in Git hooks, not in the agent's own decision-making process.
2. Executable scripts are version-controlled with the repository. Machine-wide installation only modifies the user's own Git configuration.
3. Reminders must be non-blocking. They only print messages and must never prevent a commit from succeeding.
4. Explicit audit markers take precedence over inference. The most recent commit containing `Maintenance-Audit: true` is considered the latest audit checkpoint.
5. Configuration keys, script names, and output messages consistently use the `agent` namespace, without depending on any specific agent host.

## Configuration

The reminder reads `agent.*` configuration at two levels, with repository-local settings taking precedence over global defaults:

```sh
git config --local  agent.maintainabilityAuditInterval <N>   # Repository-specific interval; overrides global
git config --global agent.maintainabilityAuditInterval <N>   # Global default interval
git config --local  agent.maintainabilityAuditBaseline <HEAD_SHA>   # Optional baseline
```

The recommended global default is **100**: all repositories without their own configuration receive an audit reminder every 100 commits. If a particular project needs more or less frequent audits, simply set a local value (such as 50 or 200) without affecting other repositories.

- `agent.maintainabilityAuditInterval` specifies the audit interval. It must be numeric; values ≤ 0 disable reminders.
- `agent.maintainabilityAuditBaseline` is an optional baseline, typically set to the current `HEAD` when enabling the system.
- If the repository already contains a commit marked with `Maintenance-Audit: true`, the script prioritizes that commit.
- Repositories with neither an audit marker nor a baseline remain silent, preventing huge unaudited commit counts from appearing immediately in older repositories that have never adopted the system.
- Set the environment variable `AGENT_MAINTAINABILITY_AUDIT_REMINDER=0` to temporarily suppress reminders.

## Installation

### Option 1: Machine-Wide (Recommended, One-Time Setup)

Copy the scripts from `.githooks/` to `~/.githooks/` and ensure they remain executable. Then run:

```sh
git config --global core.hooksPath ~/.githooks
git config --global agent.maintainabilityAuditInterval 100
```

Afterward, commits in all repositories on this machine will go through these hooks. Individual repositories can still override the interval using their local `agent.maintainabilityAuditInterval` setting.

Do not leave unrelated existing hooks (such as lefthook or git-lfs shims) in `~/.githooks/`, as they may print warnings about missing configurations in every repository.

### Option 2: Repository-Level (Single Repository Only)

Commit the `.githooks/` directory to the repository. After cloning, run the following from the repository root:

```sh
git config --local core.hooksPath .githooks
```

This command only configures the current repository and does not modify global Git settings.

This repository (AGENTS) uses the repository-level approach.

Both installation methods use identical reminder scripts. With machine-wide installation, script updates must be copied again manually.

## Repository Reminder Script

`.githooks/agent-maintainability-audit-reminder` is included in the repository and has only three responsibilities:

1. Read the current repository's local configuration, falling back to the global `agent.maintainabilityAuditInterval` when no local value is set.
2. Calculate how many commits remain until the next audit, or how many commits the audit is overdue by.
3. Print the reminder and exit with status code `0`.

The following Git hook entry points are provided, all forwarding to the same script:

- `post-commit`
- `post-merge`
- `post-rewrite`
- `post-applypatch`
- `post-checkout`

Commits are the primary use case. The other hooks prevent commit counts from becoming inaccurate after merges, history rewrites, or branch switches.

There are two standardized reminder messages:

```text
[agent] Project audit recommended in <N> commits.
[agent] Last audit was <N> commits ago. Please schedule an audit soon.
```

Reminders remain silent until at least 90 commits have passed since the last audit, preventing countdown messages from appearing immediately after an audit marker is created.

This also means that repositories configured with an interval below 90 will only see the second message after the audit becomes overdue.

## Onboarding a New Repository

1. Confirm that the repository is under Git version control.
2. Choose an audit interval measured in commits, not days or weeks. Set it using `git config --local agent.maintainabilityAuditInterval <N>`. If omitted, the global default (100) applies.
3. If the repository already has commits, and there is no requirement to wait for an explicit audit marker before starting the count, set the current `HEAD` as the baseline using `git config --local agent.maintainabilityAuditBaseline <HEAD_SHA>`.
4. When an audit is completed, include `Maintenance-Audit: true` in the commit message as an explicit audit marker.

Once configured, Git will automatically display audit reminders at the appropriate hook points as the user continues committing changes.

## Add One Line to the Host's Commit Instructions

If the agent host (such as Codex) supports commit instructions, add:

```text
After committing, report audit reminder shown by git hooks.
```

This instructs the agent to include any Git hook audit reminder in its post-commit report, so the user doesn't miss the reminder when only reviewing the commit result.

## Maintenance Conventions

- Do not store per-repository state inside `.githooks/`. State must remain in each repository's local Git configuration and Git history.
- Never allow reminders to block normal commits.
- Do not implement audit intervals as daily or weekly scheduled tasks. This is fundamentally a Git history length problem.
- Do not infer audit checkpoints when an explicit `Maintenance-Audit: true` marker is available.
- Repository-level installation must be performed separately in each new clone or worktree using `git config --local core.hooksPath .githooks`, because `core.hooksPath` is a local Git configuration setting and is not version-controlled. Machine-wide installation does not have this limitation.

## Minimum Verification

After installation, verify at least the following:

1. **Commit reminders:** `[agent]` reminders appear after `git commit`. To test, temporarily set the local interval to a value between 90 and 100 and make more than 90 commits after the baseline.
2. **Audit counter reset:** After a commit containing the audit marker, subsequent commit counting resets.
3. **Configuration precedence:** The repository-local interval overrides the global default. Removing the local value restores the global default.
