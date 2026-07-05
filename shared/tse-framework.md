# Total Survey Error (TSE) framework (shared lens)

TSE is the organizing framework for evaluating *and designing* surveys. Use it as a blueprint at the design stage and as a diagnostic grid at the review/analysis stage. It pairs with `3mc-considerations.md`: TSE names the error sources; the 3MC lens adds the cross-group "comparison error" that sits on top of them.

## The idea in one line

Quality = minimizing the **mean squared error** of the statistics you care about = reducing **variance** (random error) + **bias** (systematic error), subject to **cost**. Error is statistic-specific: a survey has many items and parameters, and the error profile differs across them, so reason per estimate, not about "the survey" as a monolith.

## The two halves

**A. Representation** — can you generalize from your sample to the target population?
- **Coverage error** — does the frame include everyone in the target population? (3MC: excluded language groups.)
- **Sampling error** — variability from sampling a subset; controlled by design and effective sample size.
- **Nonresponse error** — do non-responders differ from responders? (3MC: differential by group, mode, language.)
- **Adjustment error** — error introduced by weighting/post-stratification.

**B. Measurement** — do the questions measure the intended construct?
- **Validity** — does the item capture the construct at all?
- **Measurement error** — respondent, interviewer, instrument, or mode effects on the answer.
- **Processing error** — coding, editing, data-entry, transformation errors.

Each half ends in a **survey statistic** with its own error profile.

## What 3MC adds

- **Comparison error** — error introduced at each component *and in aggregate* when comparing across groups; the thing that determines whether group-to-group differences are real or artefacts.
- **Harmonization** — input harmonization (common design up front) and output harmonization (reconciling outputs afterward) are the levers for reducing comparison error.
- **Constraints** — cost, respondent burden, professionalism, and ethics bound every choice and frequently bind harder across groups.

## Using TSE in this skill set

- **Design / sampling / fielding:** for each major decision, ask which error component it moves and at what cost; prefer choices that reduce comparison error across groups.
- **Review (audit):** walk an existing instrument and protocol through every component above as a checklist; a finding is "this design leaves component X uncontrolled for group Y."
- **Analysis:** before comparing groups, rule out that an observed difference is measurement or mode artefact rather than a true difference.
- **Reporting:** state the dominant remaining error sources and their likely direction; never present comparisons as clean if comparison error is uncontrolled.

> Synthesized from the Total Survey Error literature and the CCSG adaptation of TSE for 3MC surveys. Paraphrased; consult primary sources for the formal treatment.
