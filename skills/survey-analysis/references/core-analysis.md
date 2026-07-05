# Core Analysis

Turning collected responses into defensible results. Domain-agnostic; overlays at the end. Apply weighting per `../../survey-sampling/references/sample-size-and-frames.md` §7 and equivalence gate per `measurement-equivalence.md` before comparing groups.

## Sequence
1. **Clean** — screen out ineligibles/speeders/straightliners; document exclusions and counts (unreported exclusions are a review finding).
2. **Weight** — apply design + nonresponse + calibration weights before any population estimate; report unweighted n, weighted base, and DEFF.
3. **Estimate with uncertainty** — every point estimate carries a margin of error / confidence interval on the **effective** sample size, not the raw n. A number without an interval is not a finding.
4. **Compare only where valid** — differences between groups need adequate n on both sides and a passed equivalence gate; report significance, but lead with effect size (a significant 1-point gap can be trivial).

## Common measures
- **Top-box / top-2-box** — share at the highest one/two scale points; the standard satisfaction/agreement summary. State which you used and keep it consistent.
- **Net score** — favorable minus unfavorable (e.g., promoters − detractors).
- **Composite** — mean of a validated item set (only when the set is validated as a scale; see `../../survey-instrument-design/references/validated-instruments.md`).
- **Driver analysis** — relate item ratings to an overall outcome (correlation/regression) to rank what matters; report it as association, never causation, and watch collinearity.

## Significance & multiplicity
Use the right test (proportions vs means; paired vs independent). With many subgroup comparisons, expect false positives — flag exploratory contrasts and don't headline an unadjusted lone "significant" result.

## Domain overlays
- **Legal — net confusion.** Report raw test, raw control, and **net = test − control** with the interval on the net figure (`../../domain-legal/references/survey-formats.md`). Thresholds are interpretive, not fixed cutoffs; counsel interprets. Show the sequence open→aided→control separately.
- **Healthcare/CMA.** Top-box per CG-CAHPS composite, by language group; report each group's n and coverage; never present a group below the reportable minimum without a caveat. No PHI in outputs.
- **HR.** Never report a cell below the small-group anonymity threshold even if statistically usable.
