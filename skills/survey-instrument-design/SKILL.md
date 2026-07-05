---
name: survey-instrument-design
description: Design survey questionnaires from scratch — question wording, response scales, item ordering, section flow, and selection of validated instruments such as CAHPS/CG-CAHPS. Use whenever a user wants to build, write, draft, or assemble a questionnaire or survey instrument, add items to measure a particular construct (satisfaction, access, care coordination, communication), or choose a response scale — especially for healthcare member-satisfaction or Health Home/CMA surveys. When the population is multilingual or multicultural, apply the shared 3MC lens so items survive translation and stay comparable across groups.
---

# Survey Instrument Design

Build a questionnaire that measures the intended constructs with minimal measurement error and that holds up across languages and cultures.

## Load first
- `../../shared/question-quality.md` — the authoring rules (what makes a good item/scale). This is the core craft reference.
- `../../shared/3mc-considerations.md` (if >1 language/culture).
- `../../shared/tse-framework.md` (measurement half is your target).
- `../../shared/instrument-library/index.json` — prefer reusing validated items over inventing new ones.

## Workflow
1. **Map constructs to aims.** List what must be measured and why each item earns its place. Cut items that don't serve the aim — every item costs respondent burden.
2. **Reuse before you write.** Search the instrument library by domain/language. Validated items (e.g., CAHPS/CG-CAHPS) come with known properties and translations; prefer them.
3. **Write any new items** per `../../shared/question-quality.md` §2 (one idea per item; neutral, concrete, translation-ready wording; no double-barreled/leading/loaded items or vague quantifiers).
4. **Choose scales** per `../../shared/question-quality.md` §3 (balance, labeling, point count, don't-know handling; keep scales consistent within a construct).
5. **Order and group** items to minimize context/priming effects; sensitive items placed deliberately.
6. **3MC pass:** for every item, ask whether the construct and the scale will mean the same thing in each target language/culture. Flag items that won't translate cleanly for adaptation (hand to `survey-translation-adaptation`).
7. **Plan pretesting:** cognitive interviewing in each language, not just the source.

## Output
A structured instrument: sections, items (with IDs that match the library), scales, routing/skip logic, and a short measurement rationale. Note which items are reused-validated vs. new-draft, and which were flagged for adaptation.

## References
- `../../shared/question-quality.md` — **canonical** wording, scale, ordering, and sensitivity rules (shared with review and the library; don't duplicate here).
- `references/validated-instruments.md` — using CAHPS/CG-CAHPS and the library.
- `references/instrument-flow.md` — design-specific: section structure, routing/skip logic, and item ordering decisions.
