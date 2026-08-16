"""Validate the file-backed project state without external services."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = {
    "schema_version",
    "project",
    "rank_scout_status",
    "canon",
    "chapter_range",
    "protagonist",
    "open_loops",
    "hooks",
    "payoffs",
    "policy",
    "last_accepted_change",
}
ALLOWED_RANK_STATUS = {"data_required", "verified", "stale", "not_applicable"}


def load_state(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("state root must be an object")
    return payload


def validate_state(state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_TOP_LEVEL - state.keys()
    errors.extend(f"missing top-level key: {key}" for key in sorted(missing))
    if state.get("rank_scout_status") not in ALLOWED_RANK_STATUS:
        errors.append("rank_scout_status must be a supported status")

    policy = state.get("policy")
    if not isinstance(policy, dict):
        errors.append("policy must be an object")
    else:
        if policy.get("local_models_allowed") is not False:
            errors.append("policy.local_models_allowed must be false")
        if policy.get("ai_output_is_candidate") is not True:
            errors.append("policy.ai_output_is_candidate must be true")
        if policy.get("human_acceptance_required") is not True:
            errors.append("policy.human_acceptance_required must be true")

    for key in ("canon", "chapter_range", "protagonist", "hooks", "payoffs"):
        if not isinstance(state.get(key), dict):
            errors.append(f"{key} must be an object")
    if not isinstance(state.get("open_loops"), list):
        errors.append("open_loops must be an array")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        type=Path,
        default=Path(".novel/novel-state.json"),
    )
    args = parser.parse_args()
    try:
        errors = validate_state(load_state(args.path))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"state validation failed: {exc}")
        return 1
    if errors:
        print("state validation failed")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"state validation passed: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
