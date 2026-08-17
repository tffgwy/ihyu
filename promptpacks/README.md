# Prompt packs

Prompt packs are compiled, reviewable operating prompts assembled from project
rules, context, templates, quality gates, and staged prompts.

Regenerate the core pack after changing any prompt or gate:

```bash
python tools/assemble_prompt_pack.py --output promptpacks/generated/novel-forge-core.md
```

The generated file is committed so GitHub users can copy one complete prompt
without running a build step.
