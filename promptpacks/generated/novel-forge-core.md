# Novel Forge Core Prompt Pack

This generated pack combines the repository rules, quality gates,
templates, and staged prompts. AI output remains candidate-only until
accepted by the project owner.

## Source: `AGENTS.md`

# Novel Forge project rules

This repository contains two related layers:

1. The original GitHub beginner guide.
2. A file-backed workflow for planning, drafting, reviewing, and maintaining
   Chinese web fiction.

## Operating rules

- Treat `PROJECT_CONTEXT.md`, `.novel/novel-state.json`, approved canon files,
  `.novel/reader-promise-ledger.json`, approved canon files, prompt run
  records, and accepted review decisions as stronger than chat memory.
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

## Local verification commands

Run these before claiming the writing system is healthy:

```bash
python -m compileall -q tools tests
python -m unittest discover -s tests -v
python tools/run_quality_suite.py --json
python tools/assemble_prompt_pack.py --output promptpacks/generated/novel-forge-core.md
```

`promptpacks/generated/` is reproducible output. Regenerate it after changing
core prompts, templates, project rules, or quality gates.

## Source: `PROJECT_CONTEXT.md`

# Novel Forge project context

This file is the front door for a new fiction project. Copy it into a
book-specific repository or fill it in before drafting a real book.

## Project identity

- Project name: `未命名小说项目`
- Working title: `待定`
- Language: `zh-CN`
- Genre: `待定`
- Target readers: `待定`
- Current phase: `discovery`
- Owner: `待填写`

## Reader promise

- One-sentence promise: `待填写：读者为什么要追读这本书？`
- Opening pressure: `待填写：第一页发生了什么不可忽略的麻烦？`
- Core emotional contract: `待填写：压抑如何积累，回报以什么方式兑现？`
- Differentiating mechanism: `待填写：本书最独特、可持续的故事机制是什么？`

## Story engine

- Protagonist desire: `待填写`
- Protagonist fear or blind spot: `待填写`
- External conflict: `待填写`
- Internal conflict: `待填写`
- Antagonistic pressure: `待填写`
- Cost of failure: `待填写`
- Escalation rule: `待填写`

## World and rules

- Setting: `待填写`
- Social or institutional pressure: `待填写`
- Power or skill rules: `待填写`
- What the reader knows first: `待填写`
- What the protagonist knows first: `待填写`
- What must remain secret: `待填写`

## Goldfinger or special mechanism

- Early signal: `必须在开篇尽早留下可回看的端倪`
- Capability: `待填写`
- Hard boundary: `待填写`
- Cost: `待填写`
- Failure mode: `待填写`
- Misinterpretation risk: `待填写`
- Upgrade path: `待填写`

## Craft boundaries

- Forbidden shortcuts: `无代价升级、无来源知识、反派只会等死、旁白替角色解释情绪`
- Voice notes: `待填写`
- Character speech differences: `待填写`
- Scenes that must be shown rather than explained: `待填写`
- Content boundaries: `待填写`

## Evidence and market gate

```yaml
rank_scout_status: data_required
```

There is no current authorized ranking snapshot in this starter repository.
Market claims must therefore be labeled as assumptions or hypotheses. Do not
describe a theme as currently hot, guaranteed to sign, or guaranteed to trend
until evidence is imported and checked.

## Acceptance boundary

The project may improve the consistency, continuity, emotional clarity, and
revision quality of an existing AI workflow. It does not retrain a foundation
model and it cannot guarantee a perfect manuscript or platform outcome.

## Source: `docs/QUALITY_GATES.md`

# Quality gates

The repository uses layered gates so a fluent paragraph cannot hide a broken
story state.

## Gate order

1. **Context gate**: project context, state, canon, and evidence status are
   loaded.
2. **Promise gate**: the unit has a reader promise and a visible opening
   pressure.
3. **Agency gate**: the protagonist wants something, faces resistance, and
   makes a costly choice.
4. **Continuity gate**: knowledge, time, place, resources, power, injuries,
   relationships, hooks, and payoffs remain consistent.
5. **Emotion gate**: pressure changes the reader's question and earns a local
   payoff.
6. **Naturalness gate**: prose is checked for guidebook narration, card-like
   exposition, repeated patterns, generic voices, and summary endings.
7. **State gate**: the ending changes what can happen next.
8. **Acceptance gate**: a human or project owner accepts the candidate and
   records the decision.

## Five-advisor pass

- **反驳者**: finds likely failure, counterexamples, and false confidence.
- **本质追问者**: asks which reader promise and causal assumption are actually
  being tested.
- **机会发现者**: looks for an unclaimed emotional or relationship mechanism.
- **外行人**: checks whether an ordinary reader can understand the immediate
  stakes without a lecture.
- **无情执行者**: names the first concrete change that can be made today.

The **主席** then chooses `accept`, `revise`, or `reject`, with reasons. The
five voices are a review frame, not a substitute for reading the manuscript.

## What the gates cannot prove

They cannot prove that a novel is perfect, will pass a platform screen, will
go viral, or was written by a human. They can expose risks, preserve decisions,
and make revision more repeatable.

## Source: `docs/EVALUATION_RUBRIC.md`

# Chapter evaluation rubric

Score candidates with this rubric before accepting them into canon. The score
is a guide, not a replacement for editorial judgment.

| Area | Weight | Strong signal |
| --- | ---: | --- |
| Opening pressure | 15 | The first page shows a problem, risk, conflict, abnormal choice, or consequence. |
| Agency | 15 | The protagonist pursues a goal and makes a costly choice. |
| Obstacle | 10 | Resistance is active, specific, and not solved by coincidence. |
| Cost | 10 | Success or failure changes resources, injury, relationship, knowledge, or danger. |
| Payoff | 15 | A reader expectation is answered through action or consequence. |
| New state | 15 | The ending forces the next chapter to begin from a changed situation. |
| Hook | 10 | The remaining question is concrete and tied to character pressure. |
| Naturalness | 10 | Prose avoids meta language, guidebook explanation, placeholders, and repeated templates. |

Suggested acceptance bands:

- `85-100`: strong candidate, still check canon and voice.
- `70-84`: usable candidate with targeted revision.
- `50-69`: structural rewrite recommended.
- `<50`: reject or rebuild from chapter brief.

## Source: `docs/market-gate.md`

# Market evidence gate

## Current status

```yaml
rank_scout_status: data_required
```

This starter repository does not contain a current, authorized ranking
snapshot, CSV, JSON export, or screenshot table. Therefore it cannot support
claims such as “currently hottest”, “guaranteed to sign”, or “this theme will
definitely get traffic”.

## Evidence categories

Keep these categories separate:

- **Evidence**: an imported, dated, authorized ranking record or user-provided
  dataset that can be inspected again.
- **Inference**: a pattern derived from that evidence, with the method stated.
- **Assumption**: a working belief used to design an experiment.
- **Hypothesis**: a claim that can be tested through reader response, retention,
  or a controlled revision.

## Minimum import record

When evidence becomes available, record:

- source and access date;
- platform and category;
- time window;
- fields included;
- missing fields;
- transformation or filtering steps;
- what the data can and cannot prove.

Do not scrape around login, CAPTCHA, paywalls, region controls, or anti-crawl
systems. Do not copy protected prose or recognizable story packages from a
ranking source.

## Small experiment before a major rewrite

Use two original opening variants with the same premise:

1. Variant A foregrounds the external danger.
2. Variant B foregrounds the protagonist's unusual choice.

Hold the setting, cast, and chapter length roughly constant. Compare reader
completion, “what happens next?” responses, and confusion reports. Treat the
result as a local signal, not a platform-wide market truth.

## Source: `.novel/style-risk-blacklist.md`

# Style risk blacklist

This is a review aid, not a ban list. A phrase can remain if it is doing real
work for viewpoint, rhythm, character voice, or suspense.

## High-risk patterns

- `不是……而是……` used as a default explanation shape.
- `没有……只有……` used to manufacture solemnity.
- `这一刻` used before every realization.
- `终于明白` used instead of showing a decision.
- `仿佛 / 似乎 / 像是` stacked to avoid concrete description.
- Chapter endings that summarize theme, lesson, or mood.
- Dialogue where both speakers explain information they already know.
- Background paragraphs that could be replaced by one object, cost, or conflict.

## Repair principle

Do not replace these mechanically. First ask what the sentence changes:

- action;
- relationship;
- information;
- pressure;
- cost;
- resource;
- state.

If the sentence changes none of them, cut or compress it.

## Source: `templates/chapter-brief.md`

# Chapter brief

## Identity

- Chapter id:
- Title:
- Story unit:
- POV:
- Current canon snapshot:

## Reader contract

- Local promise:
- Opening pressure:
- Reader question:
- Emotional direction:

## Dramatic engine

- Protagonist immediate goal:
- Concrete obstacle:
- Opponent or system pressure:
- Choice that cannot be avoided:
- Cost of the choice:
- What the protagonist misunderstands:

## Scene route

1. **Opening image or disruption**
   - What is already wrong when the chapter begins?
2. **Pressure escalation**
   - What makes delay more expensive?
3. **Choice**
   - What option does the protagonist choose, and what option is lost?
4. **Local payoff**
   - What expectation is answered, even if only partially?
5. **New state**
   - What is now different in the world, relationship, knowledge, resource, or
     danger level?
6. **Closing hook**
   - What sharper question remains?

## Continuity locks

- Facts that must remain true:
- Character knowledge boundary:
- Power, injury, money, item, or time constraints:
- Hook ledger entries touched:
- Payoff ledger entries touched:

## Prose controls

- Avoid detached setting lecture:
- Avoid repeated emotional labels:
- Required character-specific behavior:
- One image or object that carries meaning:

## Acceptance notes

- Candidate status: `draft | revised | accepted | rejected`
- Review blockers:
- Owner decision:

## Source: `templates/scene-contract.md`

# Scene contract

## Scene identity

- Scene id:
- Chapter:
- POV:
- Location:
- Time:

## Pressure

- Who wants what right now:
- Who or what blocks it:
- What happens if the protagonist delays:
- What the reader should ask:

## Action logic

- First tactic:
- Why it fails or costs more than expected:
- Second tactic:
- Irreversible choice:
- Visible consequence:

## Information

- What the reader knows:
- What the protagonist knows:
- What other characters know:
- What must stay hidden:
- What changes by the end:

## Emotional movement

- Starting emotion:
- Pressure beat:
- Turn:
- Payoff:
- New debt:

## Acceptance

- The scene changes:
  - [ ] knowledge
  - [ ] relationship
  - [ ] resource
  - [ ] injury or body state
  - [ ] public status
  - [ ] danger level
  - [ ] next goal

## Source: `templates/unit-emotion-plan.json`

{
  "unit_id": "unit-001",
  "reader_promise": "待填写",
  "baseline_emotion": "待填写",
  "emotion_sequence": [
    {
      "beat": "opening",
      "emotion": "待填写",
      "cause": "待填写",
      "reader_question": "待填写",
      "risk": "待填写"
    },
    {
      "beat": "pressure",
      "emotion": "待填写",
      "cause": "待填写",
      "reader_question": "待填写",
      "risk": "待填写"
    },
    {
      "beat": "turn",
      "emotion": "待填写",
      "cause": "待填写",
      "reader_question": "待填写",
      "risk": "待填写"
    },
    {
      "beat": "payoff",
      "emotion": "待填写",
      "cause": "待填写",
      "reader_question": "待填写",
      "risk": "待填写"
    }
  ],
  "turning_point": "待填写",
  "payoff": "待填写",
  "cost_paid": "待填写",
  "new_state": "待填写",
  "next_hook": "待填写"
}

## Source: `templates/review-report.md`

# Review report

## Scope

- Manuscript or chapter:
- Revision id:
- Reviewer:
- Date:
- Evidence files:

## Severity

- `P0`: canon break, unsafe publication issue, or a failure that makes the
  chapter unusable.
- `P1`: reader promise, continuity, emotional payoff, or scene logic is badly
  weakened.
- `P2`: prose, rhythm, repetition, or polish issue that should be fixed when
  practical.

## Findings

### P0

- Finding:
- Evidence:
- Required correction:

### P1

- Finding:
- Evidence:
- Required correction:

### P2

- Finding:
- Evidence:
- Suggested correction:

## Five-advisor pass

- 反驳者：
- 本质追问者：
- 机会发现者：
- 外行人：
- 无情执行者：
- 主席结论：

## Acceptance decision

- `accept | revise | reject`
- Blocking reasons:
- State or ledger updates required:
- Next executable action:

## Source: `prompts/01-project-architect.md`

# Project architect prompt

You are the project architect for an original Chinese web-fiction project.
Read `PROJECT_CONTEXT.md`, the active state file, and the approved ledgers
before making suggestions.

Your job is to turn a vague premise into a durable story engine. Return:

1. A one-sentence reader promise.
2. The protagonist's visible desire, private need, blind spot, and cost of
   failure.
3. The opposing force's concrete interest and first active move.
4. Three world rules, each with a visible consequence, an exception boundary,
   and a cost.
5. The special mechanism's early signal, capability, hard limit, cost, and
   misinterpretation risk.
6. Five possible story-unit promises with different emotional payoffs.
7. A short list of assumptions that must be tested before drafting.

Reject generic escalation, free power, unexplained knowledge, and premises that
cannot produce a second and third story unit. Keep all output as candidate
material. Do not declare a market trend or signing probability without current
authorized evidence.

## Source: `prompts/02-chapter-planner.md`

# Chapter planner prompt

Read the current context, state, hook ledger, payoff ledger, and
`templates/chapter-brief.md`.

Design one chapter or one short story unit. The plan must specify:

- opening disruption or pressure;
- protagonist's immediate goal;
- concrete obstacle and active opposing move;
- a choice that closes at least one safe option;
- a cost that cannot be hand-waved away;
- a partial emotional payoff;
- the changed ending state;
- one new, sharper question;
- continuity facts and knowledge boundaries;
- which ledger entries are introduced, advanced, or recovered.

Prefer scenes where setting information arrives through a choice, object,
conflict, or consequence. Do not fill the plan with atmospheric adjectives or
plot-summary labels. If the unit has no meaningful choice or changed state,
mark it as insufficient and redesign it.

## Source: `prompts/03-draft-candidate.md`

# Candidate draft prompt

Write a candidate scene from the approved chapter brief. The draft is not
canon and must not be described as final.

Constraints:

- Start with a concrete pressure, abnormal detail, conflict, or decision.
- Let the reader infer setting and emotion from behavior, objects, dialogue, and
  consequences.
- Give each character a distinct desire and speech rhythm.
- Make the protagonist choose under pressure; do not let the plot rescue them.
- Show the special mechanism through an early, limited signal if the brief
  calls for it. Respect its boundary and cost.
- Pay off at least one local promise while leaving a more specific next
  question.
- End with a changed situation, not a chapter summary or theme statement.
- Avoid author-guide phrases, card-like exposition, repeated emotional labels,
  empty shock reactions, and symmetrical filler sentences.

Do not use meta language such as “本章将”“作为AI”“读者可以看到” or explain
the writing process. Do not imitate a living author's recognizable voice.

## Source: `prompts/04-continuity-editor.md`

# Continuity editor prompt

Compare the candidate against the accepted canon, state file, story bible,
character voiceprints, and ledgers. Do not rewrite first. Return findings with
evidence and severity:

- P0: direct canon break or impossible knowledge/state.
- P1: broken motivation, unexplained capability, missing cost, or a hook/payoff
  mismatch that changes the reader contract.
- P2: weak transition, repeated explanation, timeline ambiguity, or voice drift.

For every finding, identify the exact sentence or scene, the conflicting
authority, and the smallest repair that restores continuity. Track changes to
location, time, injuries, money, items, relationships, knowledge, power, and
open loops. Treat candidate suggestions as untrusted until accepted.

## Source: `prompts/05-emotion-editor.md`

# Emotion editor prompt

Read the unit emotion plan and candidate scene. Audit the reader's emotional
route rather than counting exclamation marks.

Answer:

1. What does the reader expect at the start?
2. Where does pressure become personal or irreversible?
3. What choice creates the turn?
4. What is the local payoff, and did it earn its force?
5. What remains unresolved after the payoff?
6. Where does the scene flatten into explanation, repetition, or generic
   reaction?

Suggest repairs that change action, information, cost, relationship, or timing.
Do not solve a weak scene by merely adding louder adjectives or bigger numbers.
Mark any payoff that removes all future pressure.

## Source: `prompts/06-naturalness-editor.md`

# Naturalness editor prompt

Polish the candidate only after continuity and emotional logic are understood.
Preserve facts, viewpoint, and intended action.

Check for:

- repeated sentence shapes and uniform paragraph length;
- polished but interchangeable character voices;
- abstract emotion labels replacing physical behavior;
- author-guide narration and card-like explanation;
- repeated “不是……而是……”, “没有……只有……” constructions;
- excessive “像是”“仿佛”“似乎”“这一刻”“终于明白”;
- dialogue that explains what both speakers already know;
- chapter endings that summarize instead of alter the state.

Make selective local changes. Keep rough edges when they express character,
urgency, class, age, fear, or incomplete knowledge. Do not add internet slang,
ornamental metaphors, or a new narrator personality.

## Source: `prompts/07-final-acceptance.md`

# Final acceptance prompt

Act as the acceptance editor. Read the candidate, review findings, current
state, ledgers, and project policy.

Return:

- `accept`, `revise`, or `reject`;
- blocking P0/P1 findings;
- continuity changes required;
- hook and payoff updates required;
- whether the chapter creates a real new state;
- one concrete next action.

Accept only when the chapter keeps the reader promise, respects canon and
knowledge boundaries, gives the protagonist consequential agency, pays a
local emotional debt, and opens a more specific next question. Never mark a
candidate accepted merely because the prose sounds polished. Do not claim
platform acceptance, virality, or perfection.
