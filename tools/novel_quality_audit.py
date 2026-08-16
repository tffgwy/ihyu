"""Audit a candidate fiction draft with deterministic, explainable checks.

The checks are risk signals, not an automatic literary verdict. A human still
decides whether a warning is intentional and whether a revision belongs in
canon.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    message: str
    evidence: str


META_PATTERNS = (
    ("meta.ai", "作为AI"),
    ("meta.chapter", "本章将"),
    ("meta.reader", "读者可以"),
    ("meta.process", "接下来我们"),
    ("meta.summary", "总结一下"),
    ("meta.author", "作者注"),
)
PLACEHOLDER_PATTERNS = (
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bXXX\b",
    r"\{\{[^}]+\}\}",
    r"\[[^]\n]{1,20}(?:姓名|地点|待填|占位)[^]\n]*\]",
)
MECHANICAL_PATTERNS = (
    ("mechanical.contrast", r"不是[^。！？\n]{0,35}而是"),
    ("mechanical.exclusive", r"没有[^。！？\n]{0,35}只有"),
    ("mechanical.epiphany", r"终于明白"),
    ("mechanical.moment", r"这一刻"),
    ("mechanical.simile", r"仿佛|似乎|像是"),
)
GUIDE_PATTERNS = (
    ("guide.sequence", r"(?:^|\n)\s*(?:首先|其次|再次|最后)[：:]"),
    ("guide.definition", r"(?:所谓|顾名思义|简单来说)[：:]"),
    ("guide.reader", r"(?:你可以看到|我们可以看到|由此可见)"),
)
PRESSURE_TERMS = (
    "追", "逃", "拦", "债", "死", "伤", "火", "门", "断", "失去", "威胁",
    "交易", "限时", "暴露", "抓住", "拒绝", "选择", "代价", "秘密", "异常",
)


def _first_match(text: str, pattern: str) -> str | None:
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(0) if match else None


def _line_evidence(text: str, match: str) -> str:
    index = text.find(match)
    if index < 0:
        return match
    line = text.count("\n", 0, index) + 1
    return f"第{line}行：{match[:80]}"


def audit_text(text: str) -> list[Finding]:
    findings: list[Finding] = []
    stripped = text.strip()
    if not stripped:
        return [
            Finding("structure.empty", "P0", "候选正文为空。", "无正文内容")
        ]

    opening = stripped[:2000]
    if not any(term in opening for term in PRESSURE_TERMS):
        findings.append(
            Finding(
                "opening.pressure",
                "P1",
                "开头未检测到明显的目标、压力、冲突或异常选择信号。",
                opening[:120].replace("\n", " "),
            )
        )

    for code, literal in META_PATTERNS:
        if literal in text:
            findings.append(
                Finding(
                    code,
                    "P1",
                    "出现写作过程或作者导游式元话语。",
                    _line_evidence(text, literal),
                )
            )

    for pattern in PLACEHOLDER_PATTERNS:
        match = _first_match(text, pattern)
        if match:
            findings.append(
                Finding(
                    "structure.placeholder",
                    "P0",
                    "正文仍包含占位符或待补内容。",
                    _line_evidence(text, match),
                )
            )

    for code, pattern in MECHANICAL_PATTERNS:
        match = _first_match(text, pattern)
        if match:
            severity = "P2" if code != "mechanical.contrast" else "P1"
            findings.append(
                Finding(
                    code,
                    severity,
                    "检测到可能的机械化表达，需结合语境人工判断。",
                    _line_evidence(text, match),
                )
            )

    for code, pattern in GUIDE_PATTERNS:
        match = _first_match(text, pattern)
        if match:
            findings.append(
                Finding(
                    code,
                    "P1",
                    "检测到可能的作者导游症或卡片式说明。",
                    _line_evidence(text, match),
                )
            )

    paragraph_lengths = [
        len(part.strip())
        for part in re.split(r"\n\s*\n", stripped)
        if part.strip()
    ]
    if len(paragraph_lengths) >= 5 and len(set(paragraph_lengths)) <= 2:
        findings.append(
            Finding(
                "rhythm.uniform",
                "P2",
                "多个段落长度高度一致，可能产生卡片式节奏。",
                f"段落长度样本：{paragraph_lengths[:8]}",
            )
        )

    if re.search(r"(?:本章|这一章).{0,20}(?:总结|说明|告诉我们)", stripped):
        findings.append(
            Finding(
                "ending.summary",
                "P1",
                "结尾可能在总结章节，而不是改变故事状态。",
                stripped[-160:].replace("\n", " "),
            )
        )

    return findings


def audit_file(path: Path) -> list[Finding]:
    return audit_text(path.read_text(encoding="utf-8"))


def _severity_rank(severity: str) -> int:
    return {"P0": 0, "P1": 1, "P2": 2}.get(severity, 9)


def render_text(path: Path, findings: Iterable[Finding]) -> str:
    findings = sorted(findings, key=lambda item: _severity_rank(item.severity))
    lines = [f"Novel Forge audit: {path}", f"findings: {len(findings)}"]
    if not findings:
        lines.append("status: pass")
        return "\n".join(lines)
    lines.append("status: review")
    for finding in findings:
        lines.append(
            f"- [{finding.severity}] {finding.code}: {finding.message} "
            f"({finding.evidence})"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, required=True)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument(
        "--fail-on",
        choices=("none", "P0", "P1", "P2"),
        default="P0",
        help="Return non-zero when a finding reaches this severity.",
    )
    args = parser.parse_args()

    findings = audit_file(args.path)
    if args.format == "json":
        payload = {
            "path": str(args.path),
            "finding_count": len(findings),
            "findings": [asdict(item) for item in findings],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_text(args.path, findings))

    if args.fail_on == "none":
        return 0
    threshold = _severity_rank(args.fail_on)
    return int(any(_severity_rank(item.severity) <= threshold for item in findings))


if __name__ == "__main__":
    raise SystemExit(main())
