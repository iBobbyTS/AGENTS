#!/usr/bin/env python3
"""Create and append privacy-aware Markdown notes for complex debugging sessions.

This script does not run diagnostic commands. It only creates and updates a
structured evidence ledger under .agent-work/debug/.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

CATEGORY_LABELS = {
    "evidence": "Evidence",
    "hypothesis": "Hypothesis",
    "experiment": "Experiment",
    "decision": "Decision",
    "verification": "Verification",
    "attempt": "Repair Attempt",
}

SECRET_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s,;]+"),
        r"\1<REDACTED>",
    ),
    (
        re.compile(
            r"(?i)\b(password|passwd|secret|token|api[_-]?key|access[_-]?token|refresh[_-]?token)"
            r"(\s*[:=]\s*)(['\"]?)[^\s,;&'\"]+\3"
        ),
        r"\1\2<REDACTED>",
    ),
    (
        re.compile(
            r"(?i)([?&](?:password|passwd|secret|token|api[_-]?key|access[_-]?token|refresh[_-]?token)=)"
            r"[^&#\s]+"
        ),
        r"\1<REDACTED>",
    ),
    (
        re.compile(
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----.*?"
            r"-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
            re.DOTALL,
        ),
        "<REDACTED PRIVATE KEY>",
    ),
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stamp() -> str:
    return utc_now().strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"[-_.]{2,}", "-", value).strip("-._")
    if not value:
        raise ValueError("slug must contain at least one ASCII letter or digit")
    return value[:80]


def redact(value: str | None) -> str:
    if value is None:
        return ""
    output = value
    for pattern, replacement in SECRET_PATTERNS:
        output = pattern.sub(replacement, output)
    return output


def resolve_notes(session: str) -> Path:
    path = Path(session).expanduser().resolve()
    if path.is_dir():
        path = path / "debug.md"
    if path.name != "debug.md" or not path.exists():
        raise FileNotFoundError(f"debug session notes not found: {path}")
    return path


def append_block(path: Path, lines: Iterable[str]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines).rstrip() + "\n")


def cmd_init(args: argparse.Namespace) -> int:
    root = Path(args.root).expanduser().resolve()
    issue_slug = slugify(args.slug)
    folder_stamp = utc_now().strftime("%Y%m%d-%H%M%SZ")
    session = root / ".agent-work" / "debug" / f"{folder_stamp}-{issue_slug}"
    session.mkdir(parents=True, exist_ok=False)
    (session / "evidence").mkdir()

    title = redact(args.title or issue_slug.replace("-", " ").title())
    notes = session / "debug.md"
    notes.write_text(
        f"""# Debug Session — {title}

- **Created (UTC):** {stamp()}
- **Status:** investigating
- **Slug:** `{issue_slug}`

## Failure contract

- **Expected:**
- **Observed:**
- **Exact reproduction or observation procedure:**
- **Environment/build/version/commit:**
- **Frequency and earliest known occurrence:**
- **Scope and impact:**
- **Prior attempts and outcomes:**

## Routing

- **Mode:** systematic
- **Trigger:**
- **Loaded playbooks:**
- **Risk constraints:**

## Causal map

```text
trigger → boundary → state transformation → boundary → observed failure
```

## Evidence ledger

## Hypothesis ledger

| Hypothesis | Supporting evidence | Contradicting evidence | Unique prediction | Discriminating test | Status |
|---|---|---|---|---|---|

## Experiments and repair attempts

## Root cause

## Repair

## Verification

## Cleanup and remaining uncertainty

""",
        encoding="utf-8",
    )
    print(session)
    return 0


def cmd_record(args: argparse.Namespace) -> int:
    notes = resolve_notes(args.session)
    label = CATEGORY_LABELS[args.category]
    title = redact(args.title)
    lines = [f"\n### {label}: {title}", "", f"- **Time (UTC):** {stamp()}"]

    fields = (
        ("Observation", args.observation),
        ("Command/procedure", args.command),
        ("Prediction", args.prediction),
        ("Result", args.result),
        ("Inference", args.inference),
        ("Status", args.status),
    )
    for name, value in fields:
        if value:
            lines.append(f"- **{name}:** {redact(value)}")

    if args.artifact:
        lines.append("- **Artifacts:**")
        for artifact in args.artifact:
            lines.append(f"  - `{redact(artifact)}`")

    append_block(notes, lines)
    print(notes)
    return 0


def cmd_close(args: argparse.Namespace) -> int:
    notes = resolve_notes(args.session)
    lines = [
        "\n## Session closure",
        "",
        f"- **Time (UTC):** {stamp()}",
        f"- **Status:** {args.status}",
        f"- **Summary:** {redact(args.summary)}",
    ]
    if args.uncertainty:
        lines.append(f"- **Remaining uncertainty:** {redact(args.uncertainty)}")
    append_block(notes, lines)
    print(notes)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="Create a new .agent-work/debug session")
    init.add_argument("--root", default=".", help="Repository/workspace root")
    init.add_argument("--slug", required=True, help="Short ASCII issue identifier")
    init.add_argument("--title", help="Human-readable failure summary")
    init.set_defaults(func=cmd_init)

    record = sub.add_parser("record", help="Append a structured ledger entry")
    record.add_argument("--session", required=True, help="Session directory or debug.md")
    record.add_argument("--category", required=True, choices=sorted(CATEGORY_LABELS))
    record.add_argument("--title", required=True)
    record.add_argument("--observation")
    record.add_argument("--command")
    record.add_argument("--prediction")
    record.add_argument("--result")
    record.add_argument("--inference")
    record.add_argument("--status")
    record.add_argument("--artifact", action="append", help="Artifact path; repeatable")
    record.set_defaults(func=cmd_record)

    close = sub.add_parser("close", help="Append final status and summary")
    close.add_argument("--session", required=True, help="Session directory or debug.md")
    close.add_argument(
        "--status",
        required=True,
        choices=("fixed", "not-fixed", "blocked", "mitigated"),
    )
    close.add_argument("--summary", required=True)
    close.add_argument("--uncertainty")
    close.set_defaults(func=cmd_close)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
