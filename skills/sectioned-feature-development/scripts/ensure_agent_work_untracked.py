#!/usr/bin/env python3
"""Keep .agent-work as local, untracked Git state.

The command is deliberately conservative:
- it refuses to modify tracking when any .agent-work path is already tracked;
- otherwise it adds a local exclude entry through .git/info/exclude;
- it never edits repository .gitignore or the index.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

EXIT_ALREADY_TRACKED = 3
EXCLUDE_PATTERN = ".agent-work/"


def _git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown git error"
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def _is_equivalent_exclude(line: str) -> bool:
    value = line.strip()
    if not value or value.startswith("#") or value.startswith("!"):
        return False
    value = value.replace("\\", "/")
    if value.startswith("/"):
        value = value[1:]
    while value.endswith("*"):
        value = value[:-1]
    value = value.rstrip("/")
    return value == ".agent-work" or value.startswith(".agent-work/")


def ensure_untracked(start: Path) -> tuple[Path, Path, bool]:
    root = Path(_git(start, "rev-parse", "--show-toplevel").strip()).resolve()
    tracked = [
        line
        for line in _git(root, "ls-files", "--", ".agent-work").splitlines()
        if line.strip()
    ]
    if tracked:
        sample = "\n".join(f"  - {item}" for item in tracked[:20])
        more = "" if len(tracked) <= 20 else f"\n  ... and {len(tracked) - 20} more"
        raise AlreadyTrackedError(
            ".agent-work contains tracked paths; no tracking or ignore state was changed. "
            "Ask the user before untracking them in a separate process-only commit:\n"
            f"{sample}{more}"
        )

    exclude_raw = _git(root, "rev-parse", "--git-path", "info/exclude").strip()
    exclude = Path(exclude_raw)
    if not exclude.is_absolute():
        exclude = (root / exclude).resolve()
    exclude.parent.mkdir(parents=True, exist_ok=True)
    existing = exclude.read_text(encoding="utf-8") if exclude.exists() else ""
    if any(_is_equivalent_exclude(line) for line in existing.splitlines()):
        return root, exclude, False

    prefix = existing
    if prefix and not prefix.endswith("\n"):
        prefix += "\n"
    content = prefix + EXCLUDE_PATTERN + "\n"

    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{exclude.name}.", dir=exclude.parent, text=True
    )
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, exclude)
    finally:
        if tmp.exists():
            tmp.unlink()
    return root, exclude, True


class AlreadyTrackedError(RuntimeError):
    """Raised when changing local exclude state would conceal tracked workflow files."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="repository path or a path inside it (default: current directory)",
    )
    parser.add_argument("--repo", dest="repo_alias", help="alias for positional repository path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root, exclude, changed = ensure_untracked(Path(args.repo_alias or args.path).resolve())
    except AlreadyTrackedError as exc:
        print(f"ALREADY_TRACKED: {exc}", file=sys.stderr)
        return EXIT_ALREADY_TRACKED
    except (RuntimeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    action = "added local exclude" if changed else "local exclude already present"
    print(f"ok: {root} ({action}: {exclude})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
