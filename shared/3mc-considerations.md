# 3MC Considerations (shared lens)

This file is the cross-cutting lens for **multinational, multicultural, or multiregional (3MC)** surveys. It is referenced by every skill in this set (design, review, translation/adaptation, sampling, fielding, analysis, reporting, compliance). Load it whenever the target population spans more than one language or culture — which, for immigrant-heavy member populations, is the default case rather than the exception.

## Why this applies even to a "single survey in a single state"

A survey is 3MC whenever its respondents differ in language or culture, regardless of geography. A member-satisfaction survey administered to a multilingual immigrant population (e.g., English, Spanish, Russian, French, Arabic, Bengali speakers in one service area) is functionally multicultural and multilingual. The same comparability problems that arise across countries arise across language groups within one program: an item that works in English may not measure the same construct, the same way, in Bengali.

## The core principle: do NOT apply "one size fits all"

The instinct to take an English instrument, translate it into N languages, and field it identically is the single most common and most damaging mistake. Strict standardization can actively *harm* comparability. The goal is the optimal balance between **local appropriateness** within each group and **cross-group comparability** of the resulting measures. Some elements should be standardized; others must be localized — and which is which is a deliberate decision, documented up front, not an afterthought.

## Language assignment is a design decision, not an operational detail

Decide which language each respondent is surveyed in *as part of the design*, from the beginning. For bilingual or bicultural respondents, the interview language can itself shift answers — especially on items tied to cultural norms (health, family, consumption-type attitudes), while demographic items are largely unaffected. Leaving language choice to an ad hoc, respondent-by-respondent decision introduces uncontrolled variation. Tie language assignment to survey goals and document the rule.

Offering additional languages can *reduce* representation bias by including groups who would otherwise be excluded — but it trades against potential measurement differences. Weigh both.

## Where 3MC error enters (map to TSE — see tse-framework.md)

Treat every group as potentially introducing its own error profile, and the *differences* between groups as **comparison error** — the conceptual error that threatens whether numbers from different groups can be compared at all. Watch especially:

- **Coverage / noncoverage:** excluding a language group at the sampling stage (no frame, no materials) silently drops part of the population.
- **Nonresponse:** excluding a group at the data-collection stage (no interviewer, no translated instrument) shows up as differential nonresponse.
- **Measurement:** an item may be valid in one language and not another (construct inequivalence), or a scale may be used differently across cultures (response-style differences such as acquiescence or extreme-response tendencies).
- **Adjustment / harmonization:** combining groups requires explicit input harmonization (common design) or output harmonization (reconciling after the fact).

## Practical checklist for any 3MC survey

1. Define the target population explicitly, including how each language/cultural group is handled. Name who is in and who is out, and at which stage.
2. Set the language-assignment rule before fielding; document it.
3. Decide per element what is standardized vs. localized, and record the rationale.
4. Use a structured translation/adaptation process (see `survey-translation-adaptation`), not literal translation.
5. Pretest in each language/culture, not just the source language (cognitive interviewing surfaces inequivalence).
6. At analysis, test for measurement equivalence before comparing groups (see `survey-analysis`).
7. Document everything: comparability rests on a clear audit trail of what was standardized, localized, and why.

## Quality framing

Run the whole lifecycle on a Plan–Do–Check–Act cadence: set quality standards, implement, measure indicators at each stage, correct, repeat. A single point of coordination ("who owns comparability across groups") is what keeps standards from drifting between groups — without it, each group's instrument and process quietly diverges.

> Methodology synthesized from the Cross-Cultural Survey Guidelines (CCSG, University of Michigan ISR) and the Total Survey Error literature. Paraphrased; consult the primary sources for full treatment and citations.
