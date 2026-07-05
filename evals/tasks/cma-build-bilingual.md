# Task: cma-build-bilingual

**Path:** healthcare-CMA. **Loads:** `survey-instrument-design` + references, `survey-translation-adaptation` + references, `shared/instrument-library`, `domain-healthcare-cma/SKILL.md`, `shared/{question-quality,3mc-considerations}`.

## Prompt
> Build a 12-item member-satisfaction survey for a CMA, in **English and Russian**, covering care coordination, access, communication, provider rating, and overall satisfaction, suitable for short voice/phone administration. Reuse validated items where possible and note provenance.

## Pass criteria
1. **Item sourcing** — reuse **validated CAHPS / CG-CAHPS (tier A, AHRQ)** items for the covered constructs, with provenance (source, retrieved date, attribution), rather than inventing wording.
2. **Construct coverage** — the 12 items map to the CMA construct domains (hat §2).
3. **Flow** — sensible order, screening, non-leading, voice-friendly length/routing.
4. **RU version = cross-cultural adaptation, not literal translation** — TRAPD-style process, adaptation decisions noted, measurement-equivalence awareness.
5. **CAHPS integrity caveat** — dropping/altering core CAHPS items forfeits the name/comparability.
6. **No PHI**; library entries stored with correct tier/provenance and `verbatim_ok` set honestly.

## What this stresses (where stubs bite)
- `shared/instrument-library/` — **empty** (no CAHPS/CG-CAHPS entries).
- `survey-instrument-design/references/validated-instruments.md` + `instrument-flow.md` — stubs.
- `survey-translation-adaptation/references/adaptation-vs-translation.md` + `team-and-process.md` — stubs.
