# Eval result — cma-build-bilingual

**Date:** 2026-06-22 → re-run 2026-07-01 · **Path:** healthcare-CMA · **Verdict: FAIL → PASS** (after seeding the library + filling 4 references)

Initial run failed on the two things that most need grounding — validated item wording and RU adaptation. Both now resolved.

## Per-criterion
| # | Criterion | Result | Why |
|---|---|---|---|
| 1 | Reuse validated CAHPS/CG-CAHPS items w/ provenance | **PASS** *(was FAIL)* | `instrument-library` now holds 20 tier-A CG-CAHPS items (13 core + 7 Coordination of Care) with full provenance; `validated-instruments.md` gives the reuse workflow. No invented wording. |
| 2 | 12 items map to CMA constructs | **PASS** | hat §2 + library `domain` tags cover access/communication/care_coordination/provider_rating/overall_satisfaction. |
| 3 | Flow / voice-friendly | **PASS** *(was PARTIAL)* | `instrument-flow.md` supplies order, routing, and the voice/phone-short rule. |
| 4 | RU = adaptation, not literal translation | **PASS** *(was FAIL)* | translation references supply TRAPD + equivalence; RU stored as `draft` (`verbatim_ok=false`), flagged for reconciliation — not passed off as validated. |
| 5 | CAHPS integrity caveat | **PASS** | hat §3 + library license notes. |
| 6 | No PHI; honest tier/provenance in library | **PASS** | banks carry tier A + provenance; RU honestly marked non-validated. |

## Resolved in this build
1. ~~`shared/instrument-library/` empty~~ — **DONE.** 20 tier-A CG-CAHPS items pulled from ahrq.gov (survey-measures + Coordination of Care), full provenance; RU draft flagged for TRAPD. Next library adds: ACS demographics, NHIS/BRFSS health-status.
2. ~~`adaptation-vs-translation.md`~~ — **DONE** (TRAPD, equivalence types).
3. ~~`team-and-process.md`~~ — **DONE** (roles, workflow, documentation).
4. ~~`instrument-flow.md`~~ — **DONE** (order, routing, voice-mode length).
5. ~~`validated-instruments.md`~~ — **DONE** (reuse workflow + tier rules).

## Residual (real-world, not stub gaps)
- **RU reconciliation:** the draft RU renderings must clear TRAPD (2nd translator + adjudication + cognitive pretest) before any client use.
- **Full field wording:** core item stems are AHRQ measure descriptions; confirm exact 6-month field wording + validated Spanish from the CG-CAHPS 3.0 instrument ZIP before fielding.
- Optional next: ~~ACS demographic + NHIS/BRFSS health-status banks~~ — **DONE.** Library now covers a full instrument: CG-CAHPS (experience, 20 items) + ACS demographics (8) + CDC HRQOL-4 health status (4) = 32 tier-A items.
