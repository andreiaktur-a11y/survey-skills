# CONTINUE HERE (orientation for a new session)

This repo (`ara-survey-skills`) was built across a prior session. To resume: unzip, then **read `README.md`, `DOMAINS.md`, and `AGENTS.md` first** — they orient you fast.

## What this is
A private Claude skill set for ARA's survey consulting: methodological core + pluggable domain hats. Skill files in English (distributable artifact); working discussion in Russian.

## Current state (v1 — load-bearing COMPLETE; all 5 evals PASS)
13 skills (8 core + 5 domain), shared layer (question-quality, 3mc, tse, instrument-library, pricing-model), governance (DOMAINS.md, AGENTS.md), **evals/** (harness + 5 tasks run, all PASS).

**Eval status (all PASS):** `legal-rf-confusion-plan` · `cma-sample-plan` · `cma-build-bilingual` · `review-anonymized` · `analysis-comparability`. The two revenue paths (legal/RF, healthcare/CMA) plus the core review (entry product) and analysis tasks run end-to-end with no methodology improvised.

**Load-bearing references now all populated**, including this session's final four: `survey-instrument-review/references/severity-rubric.md`, `survey-analysis/references/core-analysis.md`, `survey-analysis/references/measurement-equivalence.md`, `survey-reporting/references/report-structure.md`.

**Populated this session:** `domain-legal/references/survey-formats.md` (Eveready/Squirt/Teflon/Thermos mechanics, control-stimulus design, triangle rule); `survey-sampling/references/sample-size-and-frames.md` (universal N/MOE/DEFF/per-group/frames/weighting + domain overlays — RF-legal geography stays in `admissibility.md`, referenced not duplicated); translation references (TRAPD) + `instrument-flow.md` + `validated-instruments.md`; **instrument-library seeded: 32 tier-A items / 4 banks** (CG-CAHPS core 13 + Coordination of Care 7, ACS demographics 8, CDC HRQOL-4 4) — full member-satisfaction instrument coverage (experience + demographics + health status), all with provenance from official sources. **RU renderings are draft forward translations (`verbatim_ok=false`), pending TRAPD reconciliation — do not field without it.**

**Also fixed:** legal SKILL.md §7 control-cell wording (RF ≠ US default); broken EXAMPLE-0001 library entry removed; README install instructions (single-skill zips break `../../shared/` refs — install whole repo as plugin or self-contained bundle); honest status wording.

## Working principles (carry these)
- **IP tiering A/B/C**: A = public-domain/own (use verbatim); B = attribution, synthesize-don't-copy (e.g., Sudman book, Babich-Batykov monograph); C = do not ingest (Qualtrics templates, vendor batteries). Build from official sources (Rospatent Guideline, SIP СП-21/15) as original synthesis.
- **No PHI / no respondent identifiers** anywhere; synthetic or de-identified only.
- **Confirm before building** new components; don't over-build (YAGNI).
- **Jurisdiction note (legal):** control *group* is OPTIONAL — standard in US confusion surveys, case-specific in RF (SIP requires control *questions*, not a control group).
- Human-in-the-loop; legal заключение needs expert signature.

## Open tasks (pick up here)
1. RF-legal agent pipeline end-to-end (orchestrator → methodology/design → analysis → report → quote), mapped to n8n + Claude API per AGENTS.md.
2. Original synthesis from "Профили потребителей" (Babich & Batykov, 2024 — tier B) → universe/profiling guide for legal + marketing.
3. Offline fieldwork contractor registry (from "Подрядчики офлайн вся Россия.xlsx") → survey-fielding (also serves the RF geography requirement).
4. ~~Populate instrument-library with real tier-A items~~ — **DONE** (32 items / 4 banks with provenance). Optional adds later: NHIS-specific items, disenrollment_reason.
5. Live test: run survey-instrument-review on a real anonymized questionnaire (ARA's entry product). Run remaining evals (`review-anonymized`, `analysis-comparability`) — they will expose which review/analysis stubs are load-bearing (`severity-rubric`, `core-analysis`, `measurement-equivalence`, `report-structure`).
6. **RU TRAPD reconciliation** of the library's draft translations (2nd translator → adjudication → cognitive pretest) before any client fielding; confirm full CG-CAHPS/ACS field wording from official PDFs.

## Intentional stubs (deliberate — do NOT fill without a real task hitting them)
Six remain, all correctly deferred under the eval-first discipline (no run has hit them):
- **Fielding:** `survey-fielding/references/mode-selection.md`, `voice-retell.md` — the voice/web stack decision waits for a concrete CMA client (PHI policy, budget, admin, languages). Platform *software* licensing (AGPL/GPL/MIT) doesn't touch our IP tiering, but never ingest platforms' bundled question libraries — item wording comes only from our instrument-library.
- **Unprioritized domains:** `domain-hr-employee/references/compliance.md`, `domain-marketing/references/{compliance,methods}.md` — HR and marketing are not current revenue paths.
- **Adequate-as-is:** `domain-healthcare-cma/references/compliance.md` — marked stub but its PHI + coverage content is sufficient for the CMA tasks that run; expand only for a full QMP evidence-package deliverable.

Fill any of these only when a client task or a new eval actually exercises it — not as bulk completion.
