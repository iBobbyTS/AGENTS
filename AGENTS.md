## Language and repository

- Reply and write plans in Chinese unless requested otherwise. Follow applicable repository rules; document reusable project conventions in `.agents/skills/`.
- Use Colima when Docker is needed on this machine; prefer `docker-compose` spelling.

## Git and work ownership
- Preserve unrelated user work. Do not reset, clean, rewrite history, delete, push, merge to the target branch or create a PR without authorization; inspect an appropriate dry-run/diff before destructive actions.
- Do not commit without authorization, except that explicitly invoking or approving `$sectioned-feature-development` authorizes its bounded feature/worker branches and implementation/repair/integration commits. This does not authorize merging to main or pushing.
- A feature branch from main needs no extra approval. From a non-main branch, ask whether to branch from main, from current, or first merge current into main.
- Never stage/commit `.agent-work/`; exclude it locally. Already tracked workflow files need an explicit index-cleanup decision. Parallel worktrees belong under `./git-worktree` with `/git-worktree/` in `.gitignore`.
- For a plain “commit/提交”, inspect the actual work and exclude temporary/output/system files, stage only intended files, then make a Conventional Commit without unrelated post-commit audits.

## Workflow and quality
- Use `$sectioned-feature-development` for genuinely non-trivial behavior, changed cross-owner/state/protocol semantics, an unclear impact cone or a whole-change attempt that failed to converge. An exact local change does not trigger solely because its file is security/routing/persistence-related. Use the skill's late-adoption rule if scope grows.
- The skill owns plan, model, section, review, repair, parallel and audit procedures; do not duplicate them here. Automatic activation is announced and waits for first-plan approval; explicit invocation proceeds until a real decision/blocker.
- Add meaningful behavior regression tests and use the existing UI validation workflow. Report checks not run. Reuse trustworthy unchanged-head/environment evidence instead of rerunning checks on every handoff.
- Run `git diff --check` once before commit, no post-check required.
- Reuse the canonical semantic owner. Ask for a bounded foundation-versus-local-patch decision only when the choice changes authorized scope, compatibility or risk.
- Independent approved work may proceed concurrently in isolated worktrees.
- Two equivalent no-progress attempts require a different evidence-producing strategy; without one, report the blocker. Use `$adaptive-debugging` for repeated or long-lived debugging.
- Completed plans stay closed. A later request is assessed afresh unless I explicitly request reopening.
- For ordinary non-sectioned approved plans, use `.agent-work/PLAN.md` and archive under `.agent-work/plans/` when complete; reread after context compaction.
- When building/compiling is needed, before running, verify you're using the binary from the latest code, not the one from last build. 

## CodeGraph
- Initialize CodeGraph at the repository root if `.codegraph/` is absent and code exploration is required.
- In an indexed repository, use `codegraph_explore` or `codegraph explore` before grep/find/manual reading when locating or understanding code; return exact source/symbol references.
- Before the final response, run `codegraph sync` in every changed indexed project. Do not sync after each minor edit.

## Programming Language Specific Requirements
### Rust
- Before running Cargo commands that build or compile artifacts (`cargo build`, ...), run `cargo clean` first unless user explicitly asks to keep the existing build cache.
- Use uv to manage python environment, unless the repo's AGENTS.md requires conda. 

## `.agent-work` Working Directory and Temporary Files
- Keep each project's Codex state in `.agent-work/` at the repository root, leave it untracked, and add it to the local Git exclude file. Use `plans/`, `reviews/`, `audit/`, `debug/`, and `handoffs/` according to purpose; each skill defines its own skill-specific directories.
- Keep only essential state files at the current task root. Store temporary scripts, logs, screenshots, downloads, caches, and intermediate artifacts by task under `.agent-work/tmp/<task-slug>/`. Store Playwright and similar tool data under `.agent-work/tooling/<tool>/<task-slug>/`. Do not write these files to the system `/tmp`, the repository root, or other unapproved directories.
- Use lowercase names for new directories. Treat `PLANS/` as a legacy name. Use `archive/<task-slug>/` for closed-task archives, and `audit-packs/<task-slug>/` and `experiments/<task-slug>/` for audit packs and reproducible experiment materials, respectively. Place deliverables in the project's designated `outputs/` directory.
- Archive task state when the task ends to prevent files from different tasks from being mixed together or overwriting one another. Do not delete files still referenced by running tasks. Before reorganizing files, generate a read-only inventory containing each file's path, type, size, owning task, and reference status. Do not move, delete, compress, or rename files without authorization.
