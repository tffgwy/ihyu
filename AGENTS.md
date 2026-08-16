# Novel Forge project rules

This repository contains two related layers:

1. The original GitHub beginner guide.
2. A file-backed workflow for planning, drafting, reviewing, and maintaining
   Chinese web fiction.

## Operating rules

- Treat `PROJECT_CONTEXT.md`, `.novel/novel-state.json`, approved canon files,
  and accepted review decisions as stronger than chat memory.
- AI output is a candidate. It does not become canon until a human or project
  owner accepts it and records the decision.
- Do not claim that this repository retrains a foundation model. It improves
  writing reliability through project memory, structured prompts, ledgers,
  deterministic checks, and revision loops.
- Do not start or call Ollama, gpt-oss, bge, embeddings, loopback model
  endpoints, or other local-model tooling in this repository unless the user
  explicitly re-authorizes local models in the current request.
- Do not promise perfect novels, guaranteed signing, guaranteed traffic,
  detector evasion, or a 100% acceptance rate. Quality gates improve
  observable craft and process stability; they do not control a platform's
  decision.
- Do not imitate a living author's recognizable style or copy protected prose.
  Extract general craft mechanisms and write original material.

## Writing workflow

Before drafting:

1. Read `PROJECT_CONTEXT.md`.
2. Read `.novel/novel-state.json`, the hook ledger, and the payoff ledger.
3. Check the current market evidence status in `docs/market-gate.md`.
4. Create or update a chapter brief from `templates/chapter-brief.md`.

After a candidate draft:

1. Run `tools/novel_quality_audit.py` on the candidate.
2. Check continuity, character voice, open loops, and state changes.
3. Record accepted changes in `.novel/decision-log.md`.
4. Update state and ledgers only after acceptance.
5. Keep rejected candidates outside canon or label them clearly as rejected.

## Chapter acceptance standard

Every accepted chapter should make its local promise visible through action.
It should contain a meaningful goal, pressure, a consequential choice, a cost,
some form of local emotional movement, and a changed ending state. Exposition
should enter through conflict, choices, objects, or consequences rather than a
detached encyclopedia passage.

The system should actively look for:

- weak or delayed opening pressure;
- generic protagonist reactions;
- mechanical parallel sentences and repeated emotional labels;
- author-guide narration and card-like setting dumps;
- unexplained power jumps, missing costs, and broken knowledge boundaries;
- hooks that are opened without a planned recovery path;
- endings that summarize the chapter instead of changing the situation.

## Git hygiene

- Keep commits focused and descriptive.
- Run the local quality commands before pushing.
- Never commit secrets, tokens, private source material, or generated local
  model data.
- Keep `rank_scout_status=data_required` until current authorized market data
  is actually imported and verified.
