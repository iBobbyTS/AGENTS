#!/usr/bin/env python3
"""Scan enrolled repositories, log commit deltas and advance observation cursors."""
from __future__ import annotations

import argparse
from datetime import datetime
import fcntl
import json
import os
from pathlib import Path
import re
import tempfile

from collect import Git, ObservationError, text


def load_repos(raw: str) -> list[dict]:
    rows = []
    seen = set()
    for number, line in enumerate(raw.splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError as exc:
            raise ValueError(f"invalid JSON on registry line {number}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"registry line {number} must be an object")
        path, base = row.get("repo_path"), row.get("last_commit")
        if not isinstance(path, str) or not Path(path).expanduser().is_absolute():
            raise ValueError(f"registry line {number} needs an absolute repo_path")
        if not isinstance(base, str) or not re.fullmatch(r"[0-9a-fA-F]{4,64}", base):
            raise ValueError(f"registry line {number} needs a last_commit hash")
        identity = str(Path(path).expanduser().resolve())
        if identity in seen:
            raise ValueError(f"duplicate repo_path on registry line {number}")
        seen.add(identity)
        rows.append(row)
    return rows


def observe(row: dict) -> dict:
    root = Path(row["repo_path"]).expanduser().resolve()
    git = Git(root)
    actual = Path(text(git.require("rev-parse", "--show-toplevel")).removesuffix("\n")).resolve()
    if actual != root:
        raise ObservationError("repo_path must identify the worktree root")
    if git.require("rev-parse", "--is-shallow-repository").strip() != b"false":
        raise ObservationError("shallow history cannot establish a complete commit count")
    head = text(git.require("rev-parse", "--verify", "HEAD^{commit}")).strip()
    base = text(git.require("rev-parse", "--verify", "--end-of-options",
                            row["last_commit"] + "^{commit}")).strip()
    code, _ = git.run("merge-base", "--is-ancestor", base, head)
    if code:
        raise ObservationError("last_commit is not a verified ancestor of current HEAD")
    count = int(git.require("rev-list", "--count", base + ".." + head).strip())
    if text(git.require("rev-parse", "--verify", "HEAD^{commit}")).strip() != head:
        raise ObservationError("HEAD changed during observation; retry this repository")
    return {"repo_path": row["repo_path"], "last_commit": row["last_commit"],
            "current_commit": head, "commit_count": count,
            "status": "changed" if count else "unchanged"}


def replace_registry(path: Path, rows: list[dict]) -> None:
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=".repos-", delete=False) as stream:
            temporary = Path(stream.name)
            for row in rows:
                stream.write(json.dumps(row, ensure_ascii=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def scan(state_dir: Path) -> dict:
    registry = state_dir / "repos.jsonl"
    # Require an existing registry; never invent enrolled repositories.
    if not registry.is_file():
        raise ValueError("repository registry is missing: " + str(registry))
    with (state_dir / ".scan.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise ValueError("another repository scan is in progress") from exc
        original = registry.read_text(encoding="utf-8")
        rows = load_repos(original)
        results, sections = [], []
        for row in rows:
            try:
                result = observe(row)
            except (ObservationError, OSError, ValueError) as exc:
                results.append({"repo_path": row["repo_path"],
                                "last_commit": row["last_commit"],
                                "status": "error", "error": str(exc)})
                continue
            results.append(result)
            if result["commit_count"]:
                # Escape line breaks in paths so one entry remains one heading.
                heading = row["repo_path"].replace("\r", "\\r").replace("\n", "\\n")
                sections.append(f"## {heading}\ncommit since last inspection("
                                f"{row['last_commit']}...{result['current_commit']}: "
                                f"{result['commit_count']})\n\n")
            row["last_commit"] = result["current_commit"]
        # Don't overwrite edits made by a registry editor during Git observations.
        if registry.read_text(encoding="utf-8") != original:
            raise ValueError("registry changed during scan; no cursors updated")
        reports = state_dir / "inspections"
        reports.mkdir(parents=True, exist_ok=True)
        report = reports / (datetime.now().astimezone().strftime("%Y%m%d") + ".md")
        # Log before advancing: failed registry writes may duplicate a section on
        # retry, but a successful cursor advance always has its recorded range.
        with report.open("a", encoding="utf-8") as stream:
            stream.write("".join(sections))
            stream.flush()
            os.fsync(stream.fileno())
        replace_registry(registry, rows)
        return {"inspection_file": str(report), "repos": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path,
                        default=Path.home() / ".agent-work" / "quality-steward")
    args = parser.parse_args()
    try:
        result = scan(args.state_dir.expanduser().resolve())
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True))
        return 1
    print(json.dumps(result, ensure_ascii=True))
    return 2 if any(repo["status"] == "error" for repo in result["repos"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
