# Healthcare Compliance & Evidence (domain-specific)

**Version 0.2 · 2026-07-27.** Supersedes the v0.1 stub, whose central statement — that no written
state policy was found and that satisfaction monitoring should be framed as good practice rather
than obligation — was **superseded by the regulatory verification of 2026-07-23** (`ROADMAP.md` §4;
`module-framework-cx.md` §0).

This file is the compliance layer of the domain module (`../../DOMAINS.md`, contract item 4). It is
**not a legal opinion.** Two items on it are open with counsel and are marked ⚑; they are answered
before fieldwork, not after.

**Scope note.** §1 below is specific to **New York State** Health Homes. For a healthcare engagement
outside NYS, the obligation basis is re-verified from that state's own policy before any claim is
made — it is not assumed to be equivalent.

---

## 1. The obligation (NYS Health Home)

**NYSDOH HH0003, *Health Home Quality Management Program*, effective 2017-06-01, no recorded
revision.** A single programme-wide policy covering Health Homes serving adults and children; there
is no separate adult instrument. (The "Revised: September 2017" line on the HHSC web page is a page
footer, not a policy revision — the policy's own "Last revised" field is blank.)

What it establishes:

1. Health Homes must **collect, analyse and report data** measuring the effectiveness of care
   coordination, **including member satisfaction**, with content areas named explicitly: timeliness
   of appointments, ease of access to information, quality of communication with care managers.
2. **Member experience surveys are one permitted method** among several (chart reviews,
   complaint/incident reports).
3. Health Homes **must obtain feedback from members and family members and apply it to QMP
   processes** — an obligation, with the method left open.
4. Negative outcomes are addressed through a **Performance Improvement Plan**: root-cause analysis,
   measurable goals, timelines, possible sanctions.

**Framing rule.** The obligation is real and written; the *method* is not prescribed. A member
survey is therefore the most defensible way to discharge a stated obligation — not "the easiest way
to evidence good practice", and not a mandated instrument. Client-specific contractual expectations
from an LHH are mapped in §6 in addition to HH0003, never in place of it.

## 2. Claim discipline — prohibited statements

These are **prohibited in any client-facing document** and are checked by the QA layer
(`module-framework-cx.md` §0.1; `ROADMAP.md` §1, library-wide):

- ❌ **"Improves your redesignation score."** Redesignation Domain 2 (20% of the total) is computed
  from **CMART and Medicaid claims/encounters data only**. No survey-derived measure enters the
  score. A member survey is evidence of QMP compliance and an operational lever on the measures that
  *are* scored — nothing more.
- ❌ **"Required by NYSDOH."** The obligation is to obtain and apply member feedback. A survey is one
  permitted method, not a mandated instrument.
- ❌ **"Replaces / satisfies the state's CAHPS requirement."** The state's biennial CAHPS-based
  survey evaluates **Medicaid managed care plans**, not Health Homes, CMAs or care managers. Not to
  be confused with the voluntary electronic CMA survey sent before a redesignation review, which
  concerns the LHH's oversight of its network and is excluded from the final score.

**The defensible commercial statement is the narrow one:** the obligation exists, the method is
unspecified, and the state's own SPA measure framework names *Experience of Care* as a measure
category while populating it with none. ⚑ *Confirm no published version newer than November 2017
before this sentence goes into a client-facing document.*

## 3. Instrument IP

The HCBS CAHPS and CG-CAHPS surveys are **tier B**, not tier A (`SKILL.md` §3;
`module-framework-cx.md` §2.5). Compliance-relevant consequences:

- The deliverable is **never named** "…CAHPS…" — "CAHPS" is a registered AHRQ trademark, licensed
  only against AHRQ's own criteria. Attribution goes in the **provenance appendix** instead.
- Tier B items are **verbatim or not used**. A lightly reworded CAHPS item is the worst outcome
  available: no comparability, and phrasing that reads as borrowed.
- Every item in a codebook carries `ip_tier`, `wording_source`, and
  `concept_overlap_with_published_instrument`. Conceptual overlap in a tier A item is legitimate;
  borrowed phrasing in a tier A item is a defect, and this is where it is caught.

## 4. PHI and the business-associate structure

**Structure of record:** a **disclosure of PHI to a business associate for health care operations**
(quality assessment and improvement activities) under a **signed BAA**. It is explicitly **not a
HIPAA limited data set** — an LDS excludes telephone numbers, email addresses and street addresses,
which are precisely the fields fielding requires (`module-framework-cx.md` §10.3).

Standing safeguards:

- **Minimum necessary** applied to the field list — contact fields and nothing beyond the weighting
  attributes.
- **Contact fields physically segregated** from the analysis file, joined only by study ID.
- **Destruction of the contact file at fieldwork close**, with a written certificate to the LHH.
- **No direct identifier** ever enters the research record, the crosstab workbook, the instrument
  library, or any deliverable. Build and test on synthetic or de-identified data only.
- The contact list is held by the **LHH**; CMAs neither hold nor see the outbound list.

⚑ **Counsel review of this structure is required before any instrument text is written.** The mode
decision depends on it, and the mode determines the instrument's form — SMS, phone and mail are
three documents, not three layouts.

## 5. Respondent protection

- **Anonymity thresholds:** no breakout for any group of **N < 5**, with the complement check; **N ≥
  10** for within-agency subgroups. Suppressed cells print as "n/a (below reporting threshold)",
  never silently dropped.
- **Care-manager-level reporting is excluded by policy** and the exclusion is stated in the report,
  in the member-facing text, and in the engagement contract (`module-framework-cx.md` §2.2).
- **What the member is told** — in the invitation and at the start of a phone interview: who is
  asking, that the care manager will not see individual answers, that results are reported in group
  form only, and that participation does not affect services or eligibility. This text is fixed and
  is reproduced in the report's provenance appendix.
- **Physical-safety items are excluded** from every configuration. A **written disclosure and
  escalation protocol** is nonetheless required before fieldwork opens: what the interviewer says, to
  whom a disclosure goes at the LHH, within what window, and what the member is told will happen
  next. Interviewers are briefed on it; it is not left to judgment in the moment.
  ⚑ **Whether M&M's interviewers fall within any mandatory-reporting obligation in this configuration
  is a legal question, answered before the first call.**

## 6. Member-feedback evidence crosswalk

Map each element of the HH0003 obligation to the artefact that evidences it:

- [ ] Instrument covers the named content areas — timeliness of appointments, ease of access to
      information, quality of communication with care managers.
- [ ] **Independent administration** documented (the care manager was not the channel).
- [ ] Fielding coverage: languages fielded, and the **share of the roster excluded by instrument
      language**, printed as a coverage figure.
- [ ] Frame and route per agency (census or stratified sample), and **mode achieved per agency**.
- [ ] Response and screening funnel: N in frame → contacted → completed → after screening, by agency.
- [ ] Results reported at network and agency level, within suppression thresholds.
- [ ] **Feedback applied**: the action loop documented — what changed because of the results, and
      where a Performance Improvement Plan was triggered, movement against its stated goals.
- [ ] Client-specific contractual expectations from the LHH, if any, mapped here alongside the above.

**Coverage = credibility.** A feedback programme that misses a language group is both a coverage gap
and a credibility gap. Document per-group reach.
