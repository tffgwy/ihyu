"""Assemble a copyable Novel Forge prompt pack from repository files."""

from __future__ import annotations

import argparse
from pathlib import Path


CORE_FILES = [
    "AGENTS.md",
    "PROJECT_CONTEXT.md",
    "docs/QUALITY_GATES.md",
    "docs/EVALUATION_RUBRIC.md",
    "docs/market-gate.md",
    ".novel/style-risk-blacklist.md",
    "templates/chapter-brief.md",
    "templates/scene-contract.md",
    "templates/unit-emotion-plan.json",
    "templates/review-report.md",
    "prompts/01-project-architect.md",
    "prompts/02-chapter-planner.md",
    "prompts/03-draft-candidate.md",
    "prompts/04-continuity-editor.md",
    "prompts/05-emotion-editor.md",
    "prompts/06-naturalness-editor.md",
    "prompts/07-final-acceptance.md",
]


def assemble(root: Path) -> str:
    chunks = [
        "# Novel Forge Core Prompt Pack",
        "",
        "This generated pack combines the repository rules, quality gates,",
        "templates, and staged prompts. AI output remains candidate-only until",
        "accepted by the project owner.",
        "",
    ]
    for relative in CORE_FILES:
        path = root / relative
        if not path.exists():
            raise FileNotFoundError(relative)
        chunks.extend(
            [
                f"## Source: `{relative}`",
                "",
                path.read_text(encoding="utf-8").strip(),
                "",
            ]
        )
    return "\n".join(chunks).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = assemble(args.root)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        print(f"prompt pack written: {args.output}")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
