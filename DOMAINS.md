# Domains

The skill set has **one domain-agnostic methodological core** and a thin **domain module** ("hat") per survey direction. The methodology (question quality, 3MC, TSE, design, review, translation, sampling, fielding, analysis, reporting) does **not** change with the domain — that's the whole point and the reason a new direction is cheap to add. Only the domain-specific knowledge varies, and it lives in one domain module.

The `survey-orchestrator` asks which direction a project is, then loads the matching domain module on top of the core.

## What stays in the core (never duplicated per domain)
`shared/question-quality.md`, `shared/3mc-considerations.md`, `shared/tse-framework.md`, and the `survey-*` skills. 3MC applies everywhere — HR teams and social-service caseloads are as multilingual/multicultural as CMA member populations.

## Domain-module contract
Every `domain-*` skill declares the same seven things, so adding a domain is *filling a template*, not redesigning:

1. **Scope** — who is surveyed; typical engagements.
2. **Construct domains** — the domain tags this direction adds to the instrument library.
3. **Instruments & sources** — typical validated instruments, each with a reuse tier (A/B/C) and provenance.
4. **Compliance & legal layer** — the rules and safeguards specific to this direction.
5. **Benchmarks** — what results are compared against.
6. **Sensitivities & population notes** — what's sensitive here; vulnerable-population and anonymity handling.
7. **Defaults** — typical mode, sampling, and reporting cadence.

## Roster
| Domain module | Status | Notes |
|---|---|---|
| `domain-healthcare-cma` | **built** | Health Home / CMA member-satisfaction. CAHPS/CG-CAHPS sources; HIPAA/PHI; satisfaction monitoring as good practice. |
| `domain-hr-employee` | **built** | Employee surveys (engagement, eNPS, wellbeing, exit). Confidentiality + small-group anonymity thresholds + labor law. |
| `domain-marketing` | **built** | Customer/brand research (CSAT, NPS, CES, brand health, pricing, segmentation). Consent/contactability: CAN-SPAM, TCPA (calls/SMS), GDPR-type. |
| `domain-legal` | **built** | Trademark/IP survey evidence (confusion, secondary meaning, genericness, dilution). Recognized formats; universe/control/double-blind; admissibility (Daubert/FRE 702; Rospatent). |
| `domain-social-survey` | **stub** | General sociological/social research of the public (attitudes, social conditions, civic studies). |
| `domain-public-opinion` | **future** | Politics / public opinion. Likely-voter & weighting models, strict non-partisanship and disclosure. Build when real. |

## Adding a new domain
Copy an existing `domain-*` skill, fill the seven contract sections for the new direction, add its construct domains to `shared/instrument-library/index.json`, and add a row above. The core is untouched.
