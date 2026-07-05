---
name: domain-hr-employee
description: The HR / employee-survey domain module — the "hat" on top of the methodological core for surveys of employees rather than healthcare members. Supplies engagement/wellbeing construct domains, typical instruments (eNPS, engagement), the confidentiality and small-group anonymity-threshold rules that employee surveys require, benchmarks, and workforce sensitivities. Use whenever a survey concerns employees, staff, engagement, eNPS, employee satisfaction, manager effectiveness, belonging, wellbeing, or exit/onboarding. Load alongside the core survey skills; design, sampling, analysis, etc. still come from the core.
---

# Domain: HR / Employee

The HR hat. Pair with the methodological core (`survey-*` + `shared/`); this file supplies only what's HR-specific. Follows the domain-module contract in `../../DOMAINS.md`.

## 1. Scope
Surveys of an organization's workforce: engagement, eNPS, satisfaction, manager effectiveness, belonging/inclusion, wellbeing/burnout, onboarding and exit. Typical engagement: design or audit an engagement instrument, field it across a multilingual workforce, report with safe small-group breakouts.

## 2. Construct domains
engagement, enablement, manager_effectiveness, belonging, intent_to_stay, wellbeing, overall_satisfaction, demographics.

## 3. Instruments & sources
- ARA's own instruments, incl. from *Социология управления: аналитический инструментарий* (Akhtyrsky, 2022) — proprietary_ARA, tier A (license: author-retained, confirm institutional terms).
- Public/academic engagement and wellbeing scales — tier B, with attribution; check each.
- Proprietary vendor batteries (e.g., Gallup Q12 and similar) — tier C: consult for coverage, never copy.

## 4. Compliance & legal layer
See `references/compliance.md`. Key points: **respondent confidentiality** is the core trust issue — employees must believe answers can't be traced to them. **Small-group anonymity threshold:** never report a breakout for a group smaller than N (commonly 5), or results can re-identify individuals. **Labor / data-protection law** varies by jurisdiction; for non-US staff, consider GDPR-type rules.

## 5. Benchmarks
Prior internal waves; published engagement norms where comparable (attribute; mind tier).

## 6. Sensitivities & population notes
Multilingual/multinational workforces are 3MC — apply the lens. Items on management, fairness, discrimination, and wellbeing are sensitive; fear of identification suppresses honesty, so anonymity design *is* measurement quality here.

## 7. Defaults
Mode: web/email primary; multilingual. Sampling: often a census of staff rather than a sample. Reporting: org-hierarchy breakouts subject to the anonymity threshold.

## References
- `references/compliance.md` — confidentiality, anonymity thresholds, labor/data-protection notes.
