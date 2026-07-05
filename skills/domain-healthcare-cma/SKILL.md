---
name: domain-healthcare-cma
description: The healthcare / Health Home / Care Management Agency (CMA) domain module — the member-satisfaction "hat" on top of the methodological core. Supplies the construct domains, validated instruments (CAHPS/CG-CAHPS), compliance and HIPAA/PHI handling, benchmarks, and member-population sensitivities for healthcare surveys. Use whenever a survey concerns CMA members, patients, health-plan enrollees, member satisfaction, care coordination, or QMP-style satisfaction monitoring. Load this alongside the core survey skills; it does not replace them — design, sampling, analysis, etc. still come from the core.
---

# Domain: Healthcare / Health Home / CMA

The healthcare hat. Pair it with the methodological core (`survey-*` skills + `shared/`); this file supplies only what's healthcare-specific. Follows the domain-module contract in `../../DOMAINS.md`.

## 1. Scope
Member-satisfaction and experience surveys for Health Homes and Care Management Agencies: CMA members, patients, health-plan enrollees. Typical engagement: design or audit a satisfaction instrument, field it across the member population's languages, report results, evidence a monitoring obligation.

## 2. Construct domains
care_coordination, access, communication, provider_rating, shared_decision_making, overall_satisfaction, health_status, demographics, disenrollment_reason.

## 3. Instruments & sources
- **CAHPS / CG-CAHPS (AHRQ)** — tier A, public domain. The backbone. Pull current wording from ahrq.gov; record provenance. Caveat: deleting core items forfeits the CAHPS name and comparability.
- **ACS / Census** — tier A, for demographic items and official category mapping (ties to 3MC socio-demographic handling).
- **NHIS / BRFSS** — tier A, for health-status items.
- ARA's own validated instruments — proprietary_ARA, tier A.

## 4. Compliance & legal layer
See `references/compliance.md`. Key points: **HIPAA / PHI** — no member identifiers in the library or analysis artefacts; aggregate and de-identify. **QMP-style satisfaction monitoring** is a good-practice / contractual expectation, not (in this case) a specific written state policy — frame deliverables as the easiest way to evidence satisfaction monitoring, not as legal compliance. Coverage must reach **all member language groups** — a monitoring program that misses a language group is both a coverage gap and a credibility gap.

## 5. Benchmarks
CAHPS Database aggregate results (AHRQ) where comparable; prior waves for trend.

## 6. Sensitivities & population notes
Multilingual immigrant member population, so every survey here is effectively 3MC. Health, immigration, and family items can be sensitive and unevenly so across language groups (see `shared/question-quality.md` section 5). Voice mode common (Retell), so keep instruments short and routing clean.

## 7. Defaults
Mode: multilingual voice/phone + web fallback. Sampling: cover each language group with a minimum effective size. Reporting: per-wave, with a satisfaction-monitoring evidence package.

## References
- `references/compliance.md` — HIPAA/PHI handling and the satisfaction-monitoring evidence crosswalk.
