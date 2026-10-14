# AGENTS.md

My personal Coding Agent constraints, shared here for backup and reference.

This README was written entirely by hand, without AI assistance. Almost all other files in this repository are 100% AI-generated. The English version was translated by GPT 6.1 Sol.

[中文版](README.zh-cn.md)

## Table of Contents

- [AGENTS.md](#agentsmd-file)
- [Git Hook](#git-hook)
- [Skills](#skills)

### Sectioned Feature Development
- [grill-me](#grill-me): Clarifies requirements without asking about product architecture.
- [sectioned-feature-development](#sectioned-feature-development): Breaks large features into sections for implementation. Includes a planning knowledge base.
- [code-review](#code-review): Reviews code after a feature change.

### Quality Control
- [quality-steward](#quality-steward): Determines whether a project is due for an audit. Recommended for periodic automated execution.
- [general-audit](#general-audit): Periodic project audits, including an audit knowledge base.
- [deployment-preflight](#deployment-preflight): Pre-deployment checks.

### Debug
- [adaptive-debugging](#adaptive-debugging): A debugging workflow to follow after the first fix attempt fails. Includes a debugging knowledge base.
- [debug-notes-to-engineering-notes](#debug-notes-to-engineering-notes): Used only when official documentation is incomplete or incorrect. Works with [adaptive-debugging](#adaptive-debugging), burning your own tokens to light the debugging path for those who come after you.

### Other Tools
- [feishu-message-sender](#feishu-message-sender): Sends periodic progress updates through a Feishu custom bot during long-running tasks.

## AGENTS.md File

[AGENTS.md](AGENTS.md) is the default filename used by Coding Agents such as Codex and ZCode for their instructions and constraints.

There are two levels of `AGENTS.md`:
- `~/.codex/AGENTS.md`: Global instructions.
- `AGENTS.md` in the project root: Project-specific instructions.

Main responsibilities:

[To be completed]

## Git Hook

The hook scripts are included in this repository. After cloning, run `./scripts/install-git-hooks.sh` from the repository root to enable them for the current repository. See [git-hook.md](docs/git-hook.md) for configuration and verification instructions.

- Every completed audit must have `Maintenance-Audit: true` in its commit message.
- The reminder scripts are located in `.githooks/` and do not depend on absolute paths in the user's home directory.
- On every commit, Git reminds you when the next audit is due or whether the configured audit interval has already been exceeded.

## Skills

### Sectioned Feature Development

#### [grill-me](skills/grill-me)

Users should be able to clearly describe what they want. The Agent uses this skill to ask only about requirements the user has not explained clearly, without asking architecture- or code-level questions.

> This skill is an independently rewritten, requirements-focused adaptation inspired by Matt Pocock's `grill-me` / `grilling` skills from [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills). The upstream project is licensed under the MIT License. Upstream copyright: Copyright (c) 2026 Matt Pocock

#### [sectioned-feature-development](skills/sectioned-feature-development/)

For large features, a complete plan must be created before implementation begins. The feature is then implemented section by section.

The general workflow looks like this:

```c
skill sectioned_feature_development() {
    Main Agent creates a complete plan, divides it into sections/subsections,
    and assigns models to each;

    GPT 6 Astra (Xhigh) performs Plan Review;

    for section in sections {
        Extract the section into a separate file;

        switch (section definition) {
            case impl_std:
                DeepSeek V4.1 Flash (high) implements the section;
            case impl_large:
                GPT 6.1 Sol (high) implements the section;
        }

        while (true) {  // Code review loop
            Invoke GLM 5.3 with $code-review;
            Once issues are resolved, run another review with GPT 6.1 Sol;

            if (loop count > 5) {
                Package an advisor_pack for GPT 6 Astra Pro to adjudicate;
                break;
            }
        }
    }
}
```

#### [code-review](skills/code-review/)

Written entirely by GPT 5.6 Sol Pro. I haven't actually read through the details myself, but it has worked quite well in practice.

### Quality Control

#### [quality-steward](skills/quality-steward)

Suitable for automated execution. Configure the repositories that need monitoring, and have the Agent check their commits at startup to determine whether an audit is due.

I recommend assigning this to a Flash-tier model. It doesn't require particularly strong reasoning capabilities.

#### [general-audit](skills/general-audit/)

An auditing methodology researched and developed by `GPT 6 Astra Pro`, with web research. Covers most major audit areas.

#### [deployment-preflight](skills/deployment-preflight)

Checks deployment safety, including whether a deployment could cause database data loss or other issues.

### Debug

#### [adaptive-debugging](skills/adaptive-debugging)

Includes a debugging knowledge base.

Starts with an **evidence inventory**: what changed during the previous attempt, why it failed to resolve the issue, what the current failure looks like, and whether a runnable reproduction is available. The workflow then proceeds with the original debugging process.

New addition: records debugging attempts under `.agent-work/debug` so that, after multiple context compactions during particularly difficult debugging sessions, the Agent doesn't forget which unsuccessful approaches have already been tried.

#### [debug-notes-to-engineering-notes](skills/debug-notes-to-engineering-notes)

After resolving an issue using [adaptive-debugging](#adaptive-debugging), this skill consolidates the records from `.agent-work/debug` into `docs/engineering-notes` for future development and other contributors.

It documents correct approaches, failed attempts, discrepancies with official documentation, and version-specific findings.

It does **not** document project-specific or implementation conventions.

### Other Tools

#### [feishu-message-sender](skills/feishu-message-sender)

Recommended for long-running tasks. Don't have the Agent poll for status updates in the foreground.

This skill copies a template script, modifies it, and launches it in the background. It uses your Feishu bot to send:
- A notification when the task starts.
- Hourly progress reports.
- A final summary when the task finishes.

Bot configuration is stored at `~/.config/feishu-message-sender/secret.json`:

```json
{
  "webhook": "https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxx",
  "secret": "signature secret",
  "name": "name of this computer"
}
```

Official Feishu documentation: [Custom Bot Usage Guide](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot?lang=zh-CN) ([Markdown version](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot.md), recommended when providing documentation to an Agent).