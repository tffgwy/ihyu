# Writing AI architecture

Novel Forge is an operating system around a writing model, not a claim that
the repository itself retrains model weights.

## Layers

1. **Authority layer**: `AGENTS.md`, `PROJECT_CONTEXT.md`, state files, ledgers,
   and accepted decision logs.
2. **Planning layer**: story bible, reader promise, chapter brief, emotion plan,
   and scene contract.
3. **Generation layer**: staged prompts that produce candidate material only.
4. **Review layer**: continuity, emotion, naturalness, five-advisor review, and
   final acceptance.
5. **Deterministic layer**: Python tools that catch structural omissions,
   placeholders, meta language, and mechanical prose risks.
6. **Persistence layer**: accepted decisions, hook/payoff ledgers, state deltas,
   handoff records, and prompt run records.

## Data flow

```text
PROJECT_CONTEXT.md
    -> story bible
    -> reader promise ledger
    -> chapter brief
    -> candidate prompt
    -> candidate draft
    -> deterministic audit
    -> human/editor review
    -> accepted state delta
    -> updated ledgers and next chapter brief
```

## Why this helps

- The model receives the same durable constraints every run.
- Failures become review findings instead of disappearing in chat history.
- Hooks, payoffs, market assumptions, and character voice get tracked in files.
- Quality gates can be run locally and in GitHub Actions.
- New prompts can be compared against old examples without guessing.

## What remains human-owned

- Final creative taste.
- Copyright and privacy judgment.
- Whether a risk is intentional.
- Which candidate becomes canon.
- Whether a market hypothesis is worth testing.
