# Eval results — review-anonymized & analysis-comparability

**Date:** 2026-07-04 · **Paths:** core (review, analysis)

## review-anonymized — Verdict: FAIL → PASS
Task: audit an anonymized member-satisfaction questionnaire → findings.
- Initial: `audit-checklist.md` populated (what to check), but `severity-rubric.md` was a stub → the agent could list issues but not rank them Critical/Major/Minor, and the "value = weight not count" logic was missing. **FAIL.**
- After filling `severity-rubric.md` (three levels + decision rule + mechanism-of-distortion requirement + RF mapping to Критические/Существенные/Замечания): findings are ranked, one Critical correctly outweighs many Minors, neutrality preserved. **PASS.**
- This is the entry product (рецензия) — now load-bearing-complete end to end.

## analysis-comparability — Verdict: FAIL → PASS
Task: decide whether language groups are comparable before pooling.
- Initial: `core-analysis.md` and `measurement-equivalence.md` were stubs → the agent would pool language groups without the equivalence gate (a Major methodological error), and had no top-box/net/driver method or net-confusion computation. **FAIL.**
- After filling both: the equivalence gate is explicit (scalar needed to compare means/top-box; metric for drivers; disaggregate when untested), core measures + weighting + significance are grounded, and the legal net-confusion overlay (test − control with interval on the net) is present. **PASS.**

## Net effect
All four evals on the two revenue paths (legal/RF, healthcare/CMA) plus the core review and analysis tasks now PASS end-to-end. Remaining stubs are intentional (see CONTINUE.md deferred list) and hit by none of these tasks.
