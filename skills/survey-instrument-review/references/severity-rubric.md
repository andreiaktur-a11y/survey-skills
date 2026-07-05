# Severity Rubric (instrument review)

How to classify findings when auditing a questionnaire or another party's survey. Pairs with `audit-checklist.md` (what to check) — this file is *how bad is each finding and what follows*. The value of a review is not the number of objections but their **weight**.

## Three levels
- **Critical** — a defect that invalidates the conclusions. The result cannot be trusted regardless of everything else. Examples: wrong universe (measured the wrong people); a leading key question that manufactures the finding; no control where the conclusion is inseparable from guessing; stimulus that misrepresents the mark at issue.
- **Major** — a systematic bias that does not automatically void the survey but requires explicit caveats and lowers evidentiary weight. Examples: geographic/demographic skew in the sample; an unbalanced scale or missing "don't know"; order effects on secondary questions; under-documented field procedures.
- **Minor** — a defect of documentation, presentation, or rigor that a critic would note but that does not move the conclusion. Examples: incomplete methods appendix, cosmetic wording issues, unreported minor exclusions.

## Decision rule
- **Any Critical finding** → the survey does not support its stated conclusion; say so plainly. One Critical outweighs many Minors.
- **Major findings without a Critical** → conclusions survive only with stated limitations; quantify direction of bias and who it favors where possible.
- **Only Minor findings** → methodology is sound; note the defects without overstating them (over-claiming on Minors destroys the reviewer's credibility — see `../../domain-legal/SKILL.md` neutrality).

## For each finding, record
Criterion violated (tie to `audit-checklist.md`), severity, the **mechanism of distortion** (how it biases the result and in whose favor), and the effect on the specific conclusion. Never assert a mechanism you can't explain.

## RF mapping
For RF reviews, this maps to Критические / Существенные / Замечания. Anchor criteria to the SIP information note (СП-21/15) and Rospatent methodological approaches (`../../domain-legal/references/admissibility.md`). The output is a written рецензия ranking findings by severity plus a conclusion on evidentiary force.
