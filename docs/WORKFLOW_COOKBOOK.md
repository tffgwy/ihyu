# Workflow cookbook

## Start a new book

1. Fill `PROJECT_CONTEXT.md`.
2. Fill `.novel/reader-promise-ledger.json`.
3. Copy `templates/story-bible.json` and complete the story engine.
4. Create the first `templates/chapter-brief.md` copy.
5. Assemble the prompt pack:

```bash
python tools/assemble_prompt_pack.py --output promptpacks/generated/novel-forge-core.md
```

## Plan a chapter

1. Read the current state and ledgers.
2. Fill a chapter brief.
3. Fill a scene contract for the most important scene.
4. Fill a unit emotion plan.
5. Check that every planned payoff creates a new problem or new state.

## Review a candidate

```bash
python tools/novel_quality_audit.py --path path/to/chapter.md --fail-on P1
python tools/score_chapter.py --path path/to/chapter.md --min-score 70
python tools/run_quality_suite.py --json
```

Then use `templates/review-report.md` to record P0/P1/P2 findings.

## Accept a chapter

Accept only after:

- no unresolved P0;
- P1 findings have either been fixed or explicitly accepted as intentional;
- hook and payoff ledgers are updated;
- state delta is recorded;
- the next chapter's starting state is clear.

## Improve the AI workflow

When a prompt change improves output, add:

- the old failure in `evals/cases/`;
- the new expected behavior in `evals/rubrics/`;
- a decision note in `.novel/decision-log.md`;
- a regenerated prompt pack.
