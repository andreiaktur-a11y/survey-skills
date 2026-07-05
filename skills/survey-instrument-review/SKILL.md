---
name: survey-instrument-review
description: Audit an EXISTING questionnaire and produce a findings report with severity ratings — covering question-wording defects, response-scale problems, ordering/context effects, coverage of the intended constructs, QMP-readiness, and cross-cultural/translation equivalence. Use this whenever a user hands over a survey, questionnaire, or instrument and asks whether it is good, wants it reviewed, critiqued, audited, QA'd, or "checked," asks whether it will satisfy QMP, or asks whether it holds up across multiple languages or cultures. This is distinct from building one from scratch (use survey-instrument-design for that); review evaluates something that already exists.
---

# Survey Instrument Review (Audit)

Take an existing instrument and systematically find what's wrong with it, how badly, and how to fix it. This is an evaluative task with a fixed deliverable — a findings report — and it is an excellent low-friction entry engagement (audit first, redesign later).

## Load first
- `../../shared/tse-framework.md` — walk the instrument through every error component.
- `../../shared/3mc-considerations.md` — if the instrument is or will be multilingual.
- `references/audit-checklist.md` and `references/severity-rubric.md`.

## Workflow
1. **Establish intent.** What is the instrument supposed to measure, for whom, in which languages, and against which standard (e.g., QMP)? An audit without a stated purpose can't judge fitness for use.
2. **Construct coverage.** Do the items actually cover the intended constructs? Flag gaps and items that measure nothing the aim needs.
3. **Item-level pass.** Run every item through the wording/scale checklist: double-barreled, leading, loaded, ambiguous, mismatched or unbalanced scales, inconsistent scales within a construct, problematic don't-know handling.
4. **Structure pass.** Ordering, context/priming, placement of sensitive items, routing logic.
5. **3MC pass.** For multilingual instruments: construct equivalence across languages, literal-translation artefacts, culturally non-equivalent items, response-style risks, language-assignment rule.
6. **Compliance pass.** Map coverage to the relevant standard (hand specifics to `domain-healthcare-cma`).
7. **Rate and prioritize.** Assign each finding a severity (`references/severity-rubric.md`) and a concrete fix.

## Output — ALWAYS use this structure
```
# Instrument Audit: [name]
## Summary (fitness-for-use verdict in 2-3 sentences)
## Findings (each: location · issue · severity · recommended fix)
   - Critical
   - Major
   - Minor
## Construct coverage gaps
## 3MC / cross-language risks (if applicable)
## Recommended next steps
```

## References
- `references/audit-checklist.md` — the full pass-by-pass checklist.
- `references/severity-rubric.md` — what counts as Critical/Major/Minor.
