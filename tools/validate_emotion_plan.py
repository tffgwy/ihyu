"""Validate the structured emotion plan used by chapter planning."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {
    "unit_id",
    "reader_promise",
    "emotion_sequence",
    "turning_point",
    "payoff",
    "cost_paid",
    "new_state",
    "next_hook",
}
BEAT_FIELDS = {"beat", "emotion", "cause", "reader_question", "risk"}


def load_plan(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("emotion plan root must be an object")
    return payload


def validate_plan(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    errors.extend(
        f"missing field: {field}"
        for field in sorted(REQUIRED_FIELDS - plan.keys())
    )
    sequence = plan.get("emotion_sequence")
    if not isinstance(sequence, list) or len(sequence) < 3:
        errors.append("emotion_sequence must contain at least three beats")
    else:
        for index, beat in enumerate(sequence):
            if not isinstance(beat, dict):
                errors.append(f"emotion_sequence[{index}] must be an object")
                continue
            missing = BEAT_FIELDS - beat.keys()
            errors.extend(
                f"emotion_sequence[{index}] missing field: {field}"
                for field in sorted(missing)
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("templates/unit-emotion-plan.json"),
    )
    args = parser.parse_args()
    try:
        errors = validate_plan(load_plan(args.path))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"emotion plan validation failed: {exc}")
        return 1
    if errors:
        print("emotion plan validation failed")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"emotion plan validation passed: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
