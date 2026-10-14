# Skill Installation and Host Configuration

The sole entry point for skill installation is `scripts/install.py`, which requires Python 3.11+. Run it from the repository root. By default, the installer only previews changes and does not write any target files.

```sh
python3 scripts/install.py --target codex
python3 scripts/install.py --target zcode --home "/absolute/custom home"
```

After reviewing the preview, add `--apply` to perform the installation. When updating an existing installation, add `--replace`: the installer first backs up the exact targets that will be replaced, then installs the new version.

Backups are stored in `sfd-backups/` under the host home directory, with `manifest.json` recording the restoration locations.

The default host home is determined by `CODEX_HOME` / `ZCODE_HOME` when set, otherwise `~/.codex` / `~/.zcode`. The `--home` option specifies the **host home directory**, not the skills directory. `--host` is an alias for `--target`.

```sh
python3 scripts/install.py --target codex --apply --replace
```

## Installation Scope

- Installs the complete skill directories under the repository's `skills/`, including SFD, code-review, the three QC skills, and all other existing skills. The three QC skills must remain at the same directory level and share the general-audit knowledge base.
- Installs host-native roles from `agents/codex/` or `agents/zcode/`, depending on the selected host. The corresponding SFD dispatch documentation is embedded into the installed `model-routing.md`, and `installation.json` is written. **Do not install SFD by copying only its `SKILL.md`.**
- Does not modify the host's global configuration. The repository-root `AGENTS.md` is installed only when `--include-agents-md` is explicitly provided. Overwriting an existing file still requires `--replace`.
- Does not run `git pull`. To update, pull and review the repository changes yourself before running the installer. The old `sync_codex_config.py` has been superseded by this installer.
- Leaves unrelated skills and native roles in the target directories untouched. Installation is rejected if a source or target path contains symbolic links, preventing writes outside the intended directories.
- An existing legacy `code-audit` installation blocks a full installation. With `--replace`, it is backed up before being removed from the active skills directory. Historical audit reports within projects are unaffected.
- To update only code-review, use `--only code-review`. This mode does not install SFD, QC, native roles, or external profiles, and does not remove the legacy `code-audit`.
- To remove legacy SFD Codex-native roles, additionally specify `--retire-legacy-agents`. This requires a full installation with `--target codex --replace`. Only the legacy role names explicitly listed by the installer are removed, and they are backed up first.

## External Profiles

The installer preserves both host-specific and shared SFD spawn profiles.

By default, it determines the external-subagent data directory as follows:

- **macOS:** `~/Library/Application Support/external-subagent`
- **Other systems:** `$XDG_DATA_HOME/external-subagent`, falling back to `~/.local/share/external-subagent` if `XDG_DATA_HOME` is unset.

If the directory does not exist, the installer issues a warning and skips profile installation. Use `--profiles-dir` to explicitly specify a target directory.

Existing profiles with the same name but different contents require `--replace` to be backed up and replaced.

When removing obsolete `sfd-*.json` profiles, the installer uses the combined profile inventory of both hosts. Profiles still used by the other host, as well as non-SFD files, are preserved.

Skills, roles, and profiles affected by the current installation are staged together. Ordinary installation failures trigger a rollback. However, running multiple installers concurrently against the same host home is unsupported, and recovery from power loss is not guaranteed.

Installation does **not** configure or launch external-subagent, connect to model APIs, or verify that live role discovery and model identities are correct.

Before use, you must still validate the following in the actual host environment: role discovery, AGENTS isolation, model/effort settings, and external execution capabilities.

## QC Usage and Reminders

The three QC entry points serve different purposes:

- **quality-steward:** Lightweight triage to determine whether an audit is warranted.
- **general-audit:** Independent, in-depth project auditing.
- **deployment-preflight:** User-triggered pre-release checks.

Example requests:

- "Use quality-steward to check whether an audit is warranted right now."
- "Use general-audit to perform a routine audit."
- "This release candidate is ready for delivery. Run deployment-preflight checks, but do not deploy."

Installation does not register repositories, run scans, install timers, modify Git hooks, or authorize audits or deployments.

For model assignments, scheduling, and repository registration file requirements, see [QC Host Configuration](QUALITY-HOST-CONFIG.zh-CN.md). That document is not copied into the host's skills directory.

The existing Git audit reminder system can still be enabled separately, as described in the [Git Hook Documentation](git-hook.md).
