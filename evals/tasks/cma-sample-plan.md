# Task: cma-sample-plan

**Path:** healthcare-CMA. **Loads:** `survey-sampling` + `references/sample-size-and-frames.md`, `domain-healthcare-cma/SKILL.md` + `references/compliance.md`, `shared/{3mc-considerations,tse-framework}`.

## Prompt
> A Care Management Agency has ~1,200 Health Home members across 5 language groups and must evidence member-satisfaction monitoring. Produce a **sample-size and fielding plan**: how many to survey overall and per language group, how to handle the finite roster, mode, weighting, and how the plan evidences per-group coverage. De-identified only.

## Pass criteria
1. **Clarify 1,200** = finite roster (population), and apply **FPC**; distinguish roster size vs. target completes.
2. **Per-group sizing** — size for the smallest reportable language cell (~100), not just the total; unequal groups → oversample small ones or census very small ones; both sides of any comparison adequately powered.
3. **DEFF / weighting** — weight to roster margins; note DEFF inflates required n.
4. **Frame = de-identified roster; no PHI** in the frame or artefacts.
5. **Mode** — multilingual voice/phone + web fallback; each language group actually reachable.
6. **Coverage = credibility** — paradata / per-group reach record as the monitoring evidence.
7. Flags that concrete per-language allocation needs the **actual roster language distribution** (real-world input, not guessed).

## What this stresses
`sample-size-and-frames.md` (FPC, per-group minimums, DEFF, finite-roster overlay) and the CMA compliance/coverage layer.
