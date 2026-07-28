---
name: domain-healthcare-cma
description: The healthcare / Health Home / Care Management Agency (CMA) domain module — the member-experience "hat" on top of the methodological core. Supplies the construct domains, instrument sources and their reuse tiers (HCBS CAHPS and CG-CAHPS are tier B, not tier A), the HIPAA/PHI and business-associate handling, benchmarks, and member-population sensitivities for healthcare surveys. Use whenever a survey concerns Health Home or CMA members, patients, health-plan enrollees, member experience or satisfaction, care coordination, or the member-feedback obligation under a Health Home Quality Management Program. Load alongside the core survey skills; it does not replace them — design, sampling, analysis, etc. still come from the core.
---

# Domain: Healthcare / Health Home / CMA

The healthcare hat. Pair it with the methodological core (`survey-*` skills + `shared/`); this file
supplies only what is healthcare-specific. Follows the domain-module contract in `../../DOMAINS.md`.

**Version 0.2 · reconciled 2026-07-27 against `references/module-framework-cx.md` v0.2.**

> **Precedence.** This file is the routing layer: what an agent needs to know before it opens
> anything else. For the **NYS Medicaid Health Home member-experience vertical**,
> `references/module-framework-cx.md` is **normative** — items, scales, thresholds, criterion,
> frame, administration and claim discipline are settled there, and every section below points at
> the framework section that carries the argument. **Where the two disagree, the framework governs
> and this file is corrected.** Do not restate framework methodology here; point at it.

## 1. Scope

Member-experience and satisfaction surveys for Health Homes and Care Management Agencies: CMA
members, patients, health-plan enrollees. Typical engagement: design or audit a member-experience
instrument, field it across the member population's languages, report results, and evidence the
member-feedback obligation.

**Worked-out vertical (v1):** member experience for **NYS Medicaid Health Home care management**.
The **buyer is the Lead Health Home (LHH)**, not the individual CMA — the obligation and the budget
sit at the LHH, and one engagement covers the whole CMA network. **Reporting units are the network
and the agency. Care-manager-level reporting is excluded by policy** (framework §2.2) — a
performance-management instrument for individual staff and a quality-measurement instrument cannot
be the same instrument.

## 2. Construct domains

`care_coordination` · `access` · `communication` · `care_manager_support` · `provider_rating` ·
`shared_decision_making` · `unmet_needs` · `grievance_resolution` · `respect` · `language_access` ·
`self_efficacy` · `engagement_intent` · `overall_satisfaction` · `health_status` · `demographics`.

`engagement_intent` supersedes the earlier `disenrollment_reason` tag: intent plus a pre-registered
reason item derives `EXIT_TYPE` (framework §9.1), because in this programme disenrollment is
frequently the *intended* outcome and a bare reason field is not analysable. ⚑ *The tag vocabulary
in `shared/instrument-library/index.json` still lists `disenrollment_reason` and none of the new
tags — a shared-layer edit, flagged for authorisation, not made here.*

## 3. Instruments & sources

- **HCBS CAHPS Survey (CMS/AHRQ)** — **tier B**. The structural and response-format reference for
  the Health Home vertical (framework §2.1, §2.5). Governing rules: the deliverable is **not** named
  "…CAHPS…" (registered AHRQ trademark); tier B items are used **verbatim or not at all**, so the
  framework carries **tier B slots, not tier B wording**, with exact text pulled from the source at
  fielding; transferability is checked **item by item, never block by block**; attribution goes in
  the provenance appendix. A `-B-` segment in an item ID marks a tier B slot.
- **CG-CAHPS 3.0 (AHRQ)** — **tier B**, same governing rules. Retained for general
  patient/clinician-visit experience work. ⚑ *It is **not** the reference for the Health Home
  vertical: it measures experience of clinician and group visits, not a member's relationship with a
  care manager. Owner decision pending on whether it stays in this module at all (see flag F-3).*
- **ACS / Census** (demographics and official category mapping), **NHIS / BRFSS / CDC HRQOL-4**
  (health status) — **tier B** proposed: public instruments, attribute and check each. ⚑ *The
  standing legend reads "A = own/official"; whether "official" covers federal statistical
  instruments is genuinely ambiguous and is flagged (F-4). Tier B is the safe reading and costs only
  attribution.*
- **Measure & Meaning's own original formulations** — **tier A**. Original synthesis only; an item
  with borrowed phrasing is a tier A defect, caught by the codebook's `wording_source` field.
- **Proprietary vendor batteries** — **tier C**: consult for coverage, never copied.

⚑ **Known defect, not yet corrected:** all four banks in `shared/instrument-library/` (CG-CAHPS core,
CG-CAHPS coordination of care, ACS demographics, CDC HRQOL-4) carry `reuse_tier: "A"`. Under the
determination above they are tier B. Until corrected, do not rely on the library's tier field for
these banks — rely on this section. See flag F-2.

## 4. Compliance & legal layer

See `references/compliance.md`, which is normative for this section's detail.

- **The obligation is written policy, not merely good practice.** NYSDOH **HH0003, *Health Home
  Quality Management Program***, effective 2017-06-01, no recorded revision, requires Health Homes
  to collect, analyse and report data on care-coordination effectiveness **including member
  satisfaction**, and to **obtain feedback from members and family and apply it** to QMP processes.
  Member experience surveys are **one permitted method among several** — the obligation is real, the
  method is unspecified (framework §0).
- **Claim discipline (mandatory, checked by the QA layer, framework §0.1).** Never claim a survey
  improves the redesignation score (Domain 2 is computed from CMART and Medicaid claims/encounters
  only); never describe a permitted method as mandated ("required by NYSDOH"); never imply the
  deliverable substitutes for the state's CAHPS-based managed-care plan survey.
- **HIPAA / PHI.** No member identifier enters the instrument library, an analysis artefact, a
  crosstab workbook, or any deliverable; build and test on synthetic or de-identified data only.
  Contact data for fielding are received **under a signed BAA as a health-care-operations
  disclosure — explicitly not a limited data set** (framework §10.3). ⚑ *Counsel review pending
  before any instrument text is written.*
- **Disclosure protocol.** Physical-safety items are excluded from every configuration, and a
  written disclosure and escalation protocol is required regardless — removing the item does not
  remove the event (framework §8.4, §8.4.1). ⚑ *Mandatory-reporting exposure is a legal question,
  answered before the first call.*
- **Language coverage.** English and Spanish baseline plus whatever covers **95% of the roster**,
  determined per engagement from the frame; the share of members excluded by instrument language is
  printed as a **coverage figure in the sample section**, not buried in limitations (framework §8.5).

## 5. Benchmarks

**Cross-agency, within network** — the comparison the LHH can act on, and the one no vendor database
provides. Prior waves for trend. **No external vendor benchmark databases** (standing rule). Public
national aggregates, including the **HCBS CAHPS Database**, are a **separate owner decision with its
own submission and specification requirements — out of scope for v1** (framework §12).

## 6. Sensitivities & population notes

- Multilingual member population, so every survey here is effectively **3MC** (`shared/3mc-considerations.md`).
- **Dependent population.** The member depends on the person the survey evaluates. This is the reason
  care-manager-level reporting is excluded and the reason independent administration is the product,
  not a nicety: once a member believes an honest answer can damage someone they rely on, the honest
  answer stops arriving and the instrument loses its discriminating power (framework §2.2, §10.2).
- Health, immigration, and family items are sensitive and unevenly so across language groups
  (`shared/question-quality.md` §5).
- **Proxy / family-assisted completion is common and is not a defect** — it is recorded as a
  variable, reported as a rate, and available as a breakout (framework §2.3).
- Open-ended responses are paraphrased where verbatim text could identify the speaker; agency and
  programme metadata attach to a quote only above threshold.
- **No people-photography** in any deliverable for this domain (standing rule; it matters more than
  usual with this population).

## 7. Defaults

- **Mode:** **SMS and mail primary, phone fallback** — and the phone fallback is resourced
  multilingually from the outset, because the members who fall through SMS and mail are not randomly
  distributed across agencies. The **mode achieved is reported per agency**. Phone is
  **interviewer-administered**: §2.3 screening assumes interviewer effects and §8.4.1 assumes a
  briefed human. ⚑ *Automated voice is therefore not a default in this vertical; if it is ever
  proposed, §8.4.1 has to be answered first (see flag F-5, and `survey-fielding/references/` for the
  stack decision, which is not a domain-module matter).*
- **Independent administration:** the contact list is held by the LHH and disclosed to M&M under the
  BAA; CMAs neither hold nor see the outbound list.
- **Sampling:** **census where the agency roster is ≤ ~800 members, stratified probability sample
  above**, stratified on programme × language; planning target ~100 completes per agency. Mode and
  materials identical across both routes; which route each agency took is printed in the sample
  section. ⚑ *The ~100 figure is methodological, not costed.*
- **Instrument budget:** 20–26 closed items, ≤ 10 minutes by phone; segmentation comes from the
  roster, not from asked items.
- **Reporting:** per wave, at network and agency level. **N < 5 suppression with the complement
  check; N ≥ 10 for within-agency subgroups.** Composites reported as **top-box**, never as means.

## References

- `references/module-framework-cx.md` — **normative for the Health Home vertical**: modules, item
  bank, scales, thresholds, `EXIT_TYPE`, driver model, frame, administration, claim discipline.
- `references/compliance.md` — HH0003 basis, PHI/BAA structure, claim discipline, evidence crosswalk.
- Core, not duplicated here: `shared/question-quality.md`, `shared/3mc-considerations.md`,
  `shared/tse-framework.md`, `shared/instrument-library/`, and the `survey-*` skills.

*Not yet built for this domain (Report Library): questionnaire, codebook, report template, sample
report. Both are blocked on the two open items in `ROADMAP.md` §5.*
