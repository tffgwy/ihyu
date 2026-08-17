"""Run the deterministic Novel Forge repository checks."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.novel_quality_audit import audit_file
from tools.score_chapter import score_text
from tools.validate_emotion_plan import load_plan, validate_plan
from tools.validate_story_state import load_state, validate_state


@dataclass(frozen=True)
class CheckResult:
    name: str
    passed: bool
    detail: str


def run_suite(root: Path) -> list[CheckResult]:
    results: list[CheckResult] = []

    state_path = root / ".novel" / "novel-state.json"
    state_errors = validate_state(load_state(state_path))
    results.append(CheckResult("state", not state_errors, "; ".join(state_errors) or "ok"))

    state = load_state(state_path)
    rank_ok = state.get("rank_scout_status") == "data_required"
    results.append(
        CheckResult(
            "rank_scout_status",
            rank_ok,
            f"rank_scout_status={state.get('rank_scout_status')}",
        )
    )

    emotion_path = root / "templates" / "unit-emotion-plan.json"
    emotion_errors = validate_plan(load_plan(emotion_path))
    results.append(
        CheckResult("emotion_plan", not emotion_errors, "; ".join(emotion_errors) or "ok")
    )

    strong_case = root / "evals" / "cases" / "strong-opening.md"
    strong_findings = audit_file(strong_case)
    strong_score = score_text(strong_case.read_text(encoding="utf-8"))
    results.append(
        CheckResult(
            "strong_opening_case",
            not any(item.severity in {"P0", "P1"} for item in strong_findings)
            and int(strong_score["score"]) >= 70,
            f"score={strong_score['score']}, findings={len(strong_findings)}",
        )
    )

    weak_case = root / "evals" / "cases" / "weak-ai-opening.md"
    weak_findings = audit_file(weak_case)
    weak_score = score_text(weak_case.read_text(encoding="utf-8"))
    results.append(
        CheckResult(
            "weak_ai_case",
            any(item.severity in {"P0", "P1"} for item in weak_findings)
            and int(weak_score["score"]) < 70,
            f"score={weak_score['score']}, findings={len(weak_findings)}",
        )
    )

    required_files = [
        "docs/WRITING_AI_ARCHITECTURE.md",
        "docs/TRAINING_AND_EVALUATION.md",
        "docs/EVALUATION_RUBRIC.md",
        "promptpacks/README.md",
        "templates/scene-contract.md",
        "templates/chapter-state-delta.json",
        ".novel/reader-promise-ledger.json",
    ]
    missing = [name for name in required_files if not (root / name).exists()]
    results.append(
        CheckResult("required_files", not missing, ", ".join(missing) if missing else "ok")
    )
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results = run_suite(args.root)
    if args.json:
        print(json.dumps([asdict(item) for item in results], ensure_ascii=False, indent=2))
    else:
        for item in results:
            status = "PASS" if item.passed else "FAIL"
            print(f"{status} {item.name}: {item.detail}")
    return int(not all(item.passed for item in results))


if __name__ == "__main__":
    raise SystemExit(main())
