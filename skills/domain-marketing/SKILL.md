---
name: domain-marketing
description: The marketing-research domain module — the customer and brand survey hat on top of the methodological core. Supplies CSAT/NPS/CES, brand-health, concept-test, pricing, and segmentation construct domains, typical instruments with reuse tiers, the consent and contactability rules marketing outreach requires (CAN-SPAM, TCPA for calls and SMS, GDPR-type), benchmarks, and marketing-survey biases. Use whenever a survey concerns customers, prospects, brand, NPS, customer satisfaction, product or concept testing, pricing, or market segmentation. Load alongside the core survey skills; design, sampling, and analysis still come from the core.
---

# Domain: Marketing

The marketing hat. Pair with the methodological core (`survey-*` + `shared/`); this supplies only what's marketing-specific. Follows the contract in `../../DOMAINS.md`.

## 1. Scope
Customer and market research: satisfaction (CSAT), loyalty (NPS), effort (CES), brand awareness and health, concept/product testing, pricing research, segmentation, purchase intent.

## 2. Construct domains
csat, nps, ces, brand_awareness, brand_health, purchase_intent, price_sensitivity, segmentation, concept_test, overall_satisfaction, demographics.

## 3. Instruments & sources
- NPS / CSAT / CES — the metrics themselves are free to use; word items plainly (see `shared/question-quality.md`).
- Pricing methods — Van Westendorp price-sensitivity meter, Gabor-Granger — methods (not copyrightable); synthesize in references.
- Academic service-quality scales (e.g., SERVQUAL family) — tier B, attribute; check each.
- Proprietary vendor batteries — tier C: consult for coverage, never copy.
- ARA's own instruments — proprietary_ARA.

## 4. Compliance & legal layer
See `references/compliance.md`. **Outreach consent/contactability is the main legal surface:** US CAN-SPAM (email) and **TCPA** (calls, autodialed calls, and SMS — directly relevant to Retell voice/SMS fielding); GDPR-type consent for non-US contacts; panel and incentive rules. This reuses `survey-fielding`/Retell from the core but adds a stricter consent gate on top.

## 5. Benchmarks
Industry NPS/CSAT norms (attribute; mind tier); prior waves for trend.

## 6. Sensitivities & population notes
Low topic sensitivity, but high **selection bias** risk (only the delighted or the angry respond) and social-desirability in brand ratings. Multilingual customer bases are still 3MC.

## 7. Defaults
Mode: web/email and SMS; sample from the customer base or a panel. Reporting: metric trend + driver analysis.

## References
- `references/compliance.md` — CAN-SPAM, TCPA (calls/SMS), GDPR-type consent, panel/incentive rules.
- `references/methods.md` — NPS/CSAT/CES wording, pricing methods, segmentation.
