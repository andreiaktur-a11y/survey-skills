---
name: survey-sampling
description: Design the sample for a survey — define the target population, choose a sampling frame, decide the sampling approach (probability vs. other), compute sample size and effective sample size accounting for design effects, and plan stratification and per-group coverage. Use whenever a user asks how many respondents they need, how to draw a sample, how to handle response rates, how to ensure each language/cultural group is adequately covered, or how to weight results. Apply the shared 3MC lens so coverage and nonresponse don't silently drop language groups.
---

# Survey Sampling

Get a sample that supports the intended estimates and comparisons at acceptable cost, without quietly excluding groups.

## Load first
- `../../shared/3mc-considerations.md` — coverage/nonresponse differ by group.
- `../../shared/tse-framework.md` — sampling lives in the representation half.
- Census/frame data available in the project (e.g., `/mnt/project/USA_census`) for population structure and weighting targets.

## Workflow
1. **Target population.** Define precisely, including how each language/cultural group is included or excluded — and at which stage. Excluding a group at the frame stage is coverage error; at the field stage, nonresponse error. Make this a choice, not an accident.
2. **Frame.** Identify the frame; assess its coverage of each group. Different groups may need different frames or stages.
3. **Approach.** Probability where feasible; document deviations. For comparison goals, set a **minimum effective sample size per group**, not just an overall N, to account for design effects.
   - *Optional control cell (legal):* a test/control design adds a second arm to net out baseline noise/guessing — standard in US confusion surveys, optional/case-specific in RF (the SIP note requires control *questions*, not a control *group*). If used, size both arms; account for the extra cost (`shared/pricing-model.md`).
4. **Size.** Compute N from the precision needed on the key estimate(s) and expected response rate; inflate for design effect and per-group breakouts.
5. **Stratify** by the groups you must compare or represent.
6. **Weighting plan.** Specify how you'll adjust for unequal selection and nonresponse (note adjustment error).

## Output
A sampling plan: target population and group handling, frame(s), approach, overall and per-group sample sizes with assumptions, stratification, and the weighting plan. Use `scripts/` for size calculations once added.

## References
- `references/sample-size-and-frames.md` — formulas, design effects, per-group sizing, frame assessment.
