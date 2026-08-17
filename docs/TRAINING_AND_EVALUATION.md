# Training and evaluation boundary

When this repository says “make the AI stronger,” it means strengthening the
project workflow first:

- better context;
- better prompts;
- better failure examples;
- better review rubrics;
- better deterministic checks;
- better state persistence;
- better revision loops.

It does not mean this repository has fine-tuned a model unless a separate,
authorized training pipeline, dataset license review, compute environment,
training log, and evaluation report are added.

## Safe improvement loop

1. Write a chapter brief.
2. Generate one or more candidate drafts.
3. Run deterministic checks.
4. Score the chapter with `tools/score_chapter.py`.
5. Review with the five-advisor frame.
6. Record accepted decisions and rejected failure modes.
7. Add anonymized, authorized examples to `evals/cases/`.
8. Re-run the suite before changing prompts.

## If real fine-tuning is added later

Before any model training, require:

- rights-confirmed training data;
- removal of private text, secrets, and unauthorized samples;
- clear train/dev/test split;
- baseline and post-training evaluation;
- regression checks for hallucinated canon, style imitation, and unsafe claims;
- documentation of model, date, parameters, dataset hash, and observed failure
  modes.

Do not train on copyrighted books, private drafts, user chats, ranking pages,
or third-party samples without explicit rights.

## Evaluation dimensions

| Dimension | What it checks |
| --- | --- |
| Opening pressure | Does the first scene contain conflict, risk, abnormal choice, or consequence? |
| Agency | Does the protagonist choose under pressure rather than get rescued by plot? |
| Cost | Does success or failure change resources, injury, relationship, knowledge, or risk? |
| Payoff | Does the chapter answer a reader expectation before opening the next question? |
| State change | Is the next chapter forced to start from a changed situation? |
| Continuity | Do knowledge, power, time, location, injury, and resources remain consistent? |
| Naturalness | Does prose avoid guidebook narration, meta language, and repetitive templates? |
| Originality boundary | Does it avoid copying protected expression or recognizable author style? |
