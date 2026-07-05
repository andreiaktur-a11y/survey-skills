# Eval result — cma-sample-plan

**Date:** 2026-06-22 · **Path:** healthcare-CMA · **Verdict: PASS**

Validates that the just-populated `sample-size-and-frames.md` serves the CMA path through its overlay. No methodology improvised.

## Per-criterion
| # | Criterion | Result | Source |
|---|---|---|---|
| 1 | Finite roster + FPC; roster vs completes | **PASS** | `sample-size-and-frames.md` §1 (FPC) + CMA overlay (roster = finite frame). |
| 2 | Per-group minimums, oversample/census small groups | **PASS** | §4 (smallest reportable cell ~100) + §4 3MC link. |
| 3 | DEFF / weighting to roster margins | **PASS** | §3 + §7. |
| 4 | De-identified frame, no PHI | **PASS** | CMA overlay + `compliance.md` (HIPAA/PHI). |
| 5 | Multilingual voice/web, each group reachable | **PASS** | hat §7 defaults. |
| 6 | Coverage = credibility (per-group paradata) | **PASS** | `compliance.md` coverage section + evidence crosswalk. |
| 7 | Flags need for real roster language distribution | **PASS** *(agent asks / states assumption)* | Real-world input gap, not a stub gap. |

## Notes
- `compliance.md` is marked "stub" but its PHI + coverage content is **adequate for sampling** — not load-bearing-missing here.
- Worked example the plan should produce (illustrative, p=0.5, 95%): overall ±5% on a 1,200 roster → n₀≈385, FPC → ≈292 completes; per-language ±5% is infeasible for small groups → census them and report with wider CI + a coverage note. This falls out of the populated file without improvisation.

**Conclusion:** CMA **sampling** side is covered. The CMA gap is on the **instrument** side — see `cma-build-bilingual`.
