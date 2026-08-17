"""Score a candidate chapter with a transparent heuristic rubric."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.novel_quality_audit import audit_text


@dataclass(frozen=True)
class DimensionScore:
    name: str
    points: int
    max_points: int
    evidence: str


PRESSURE_TERMS = ("追", "逃", "拦", "债", "死", "伤", "火", "断", "限时", "威胁", "异常")
AGENCY_TERMS = ("选择", "决定", "必须", "转身", "推开", "拒绝", "握住", "冲", "跑", "交出")
OBSTACLE_TERMS = ("挡", "拦", "锁", "护卫", "敌", "门外", "不能", "失败", "代价")
COST_TERMS = ("血", "伤", "失去", "暴露", "代价", "欠", "断", "锁", "死", "罚")
PAYOFF_TERMS = ("亮", "开", "倒", "赢", "救", "变了", "退", "落锁", "回答", "兑现")
STATE_TERMS = ("从此", "已经", "再也", "变了", "落锁", "新", "暴露", "留下", "不能回")
HOOK_TERMS = ("谁", "为什么", "怎么", "秘密", "声音", "锁链", "门后", "下一", "忽然")


def _contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def _score_binary(
    text: str,
    terms: tuple[str, ...],
    name: str,
    max_points: int,
    evidence_window: int = 220,
) -> DimensionScore:
    if _contains_any(text, terms):
        evidence = next(term for term in terms if term in text)
        return DimensionScore(name, max_points, max_points, f"found signal: {evidence}")
    return DimensionScore(
        name,
        0,
        max_points,
        text[:evidence_window].replace("\n", " "),
    )


def score_text(text: str) -> dict[str, object]:
    stripped = text.strip()
    opening = stripped[:800]
    ending = stripped[-800:] if stripped else ""
    audit_findings = audit_text(text)
    severe_findings = [item for item in audit_findings if item.severity in {"P0", "P1"}]

    dimensions = [
        _score_binary(opening, PRESSURE_TERMS, "opening_pressure", 15),
        _score_binary(stripped, AGENCY_TERMS, "agency", 15),
        _score_binary(stripped, OBSTACLE_TERMS, "obstacle", 10),
        _score_binary(stripped, COST_TERMS, "cost", 10),
        _score_binary(stripped, PAYOFF_TERMS, "payoff", 15),
        _score_binary(ending, STATE_TERMS, "new_state", 15),
        _score_binary(ending, HOOK_TERMS, "hook", 10),
    ]

    naturalness_points = 10
    if any(item.severity == "P0" for item in audit_findings):
        naturalness_points = 0
    elif severe_findings:
        naturalness_points = 3
    elif audit_findings:
        naturalness_points = 7
    dimensions.append(
        DimensionScore(
            "naturalness",
            naturalness_points,
            10,
            f"audit findings: {len(audit_findings)}",
        )
    )

    total = sum(item.points for item in dimensions)
    if total >= 85:
        band = "strong"
    elif total >= 70:
        band = "usable"
    elif total >= 50:
        band = "rewrite"
    else:
        band = "reject"

    return {
        "score": total,
        "max_score": 100,
        "band": band,
        "dimensions": [asdict(item) for item in dimensions],
        "audit_finding_count": len(audit_findings),
        "severe_finding_count": len(severe_findings),
    }


def render_text(path: Path, payload: dict[str, object]) -> str:
    lines = [
        f"Novel Forge score: {path}",
        f"score: {payload['score']}/{payload['max_score']}",
        f"band: {payload['band']}",
        f"audit findings: {payload['audit_finding_count']}",
    ]
    for item in payload["dimensions"]:  # type: ignore[index]
        lines.append(
            f"- {item['name']}: {item['points']}/{item['max_points']} "
            f"({item['evidence']})"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, required=True)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--min-score", type=int, default=0)
    args = parser.parse_args()

    payload = score_text(args.path.read_text(encoding="utf-8"))
    if args.format == "json":
        print(json.dumps({"path": str(args.path), **payload}, ensure_ascii=False, indent=2))
    else:
        print(render_text(args.path, payload))
    return int(payload["score"] < args.min_score)


if __name__ == "__main__":
    raise SystemExit(main())
