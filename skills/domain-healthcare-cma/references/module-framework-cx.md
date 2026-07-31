# Measure & Meaning — CX Domain (Health Home Member Experience)

## Module Framework & Question Bank · v0.3

**Status:** owner sign-off of 2026-07-30 applied · **Repo target:** `skills/domain-healthcare-cma/references/module-framework-cx.md`

**Changelog v0.3 (supersedes v0.2; owner sign-off 2026-07-30, applied from `references/tier-b-source-items.md` v0.1):**

- **§2.5 rationale corrected — D-CX-10.** Verbatim use of a tier B item buys attribution, format familiarity and freedom from the borrowed-paraphrase defect. It does **not** buy comparability with published HCBS CAHPS results or the CAHPS Database. Grounds are in the source's own administration guidance. The verbatim-or-nothing rule itself is unchanged.
- **§0.1 fourth prohibited claim added** as the direct consequence: results are not comparable to HCBS CAHPS benchmarks.
- **§2.5 bright-line rule adopted — D-CX-11.** A slot whose item-by-item determination is an unqualified *transfers* is filled verbatim; a slot determined *transfers in part* becomes an original tier A item. **The tier B set is now closed at six items** and enumerated in §2.5.
- **§2.5 language rule — D-CX-12.** Official Spanish verbatim for tier B items; TRAPD applies to tier A only. All languages beyond EN/ES are tier A throughout.
- **§5 COM tier B slots struck — D-CX-13.** The source has no care-manager-referenced communication item at all; the module is rebuilt as four tier A items.
- **§3 `RAT-B-01` relabelled — D-CX-14.** The published item rates *the help received from* the care manager, not the care manager. §9.2 corrected accordingly.
- **§4 `CMH-B-00` added — D-CX-15.** Q48 is the gate for the whole care-manager block; taking the block without it changes five denominators.
- **§4 `CMH-B-02` dropped and `CMH-B-03` converted to tier A**; **§8.2 `UNM-TRN` resolved as tier A** — all three by the bright line, closing v0.2 §13.1 item 2.
- **§13 renumbered to stable `O-CX-n` IDs**, mapped to the ROADMAP §5 list so the two stop diverging. Header repo path corrected; §12 benchmarking note and §13.2 D-CX-6 cross-reference repaired.

**Changelog v0.2 (supersedes v0.1, same day):**

- **§9 rebuilt around `EXIT_TYPE`** (owner, 2026-07-23). Intent to leave plus a pre-registered reason item derives a four-type outcome, which restores engagement intent as an analysable outcome without treating it as a one-directional good. The two-sided-criterion objection in v0.1 is answered, not overruled — see §9.1.
- **§8.4 physical-safety items removed** (owner). Interviewer disclosure protocol retained as a separate requirement — §8.4.1.
- **§2.2 care-manager-level reporting resolved as excluded by policy**, with the measurement-validity and reliability arguments recorded; caseloads confirmed at 50–60 members per care manager, agencies at 300–6,000 members.
- **§10.1 census/sample threshold added** — agencies of 6,000 do not get a census.

**Vertical:** member experience for NYS Medicaid Health Home care management. **Buyer:** the Lead Health Home (LHH), not the individual Care Management Agency (CMA).

**All Measure & Meaning items in this document are original formulations (IP tier A). Items sourced from the HCBS CAHPS Survey are marked as tier B slots and their wording is deliberately NOT reproduced here — the verbatim text, in both baseline languages, lives in `references/tier-b-source-items.md` and is the only authorised route from source to questionnaire (§2.5). All sample figures, thresholds, and organisation names are illustrative + synthetic.**

**IP tier legend** (per standing rules):

- **A** — own/official: original synthesis, safe to publish and reuse.
- **B** — public/official/academic: used **verbatim with attribution** after a per-instrument licence check, or not used at all. Paraphrase of a tier B item is a **defect**, not a permitted option — see §2.5 rule 2. *(The standing library-wide legend still reads "paraphrase or verbatim"; for this instrument the narrower rule governs. Library-wide reconciliation is `O-CX-15`.)*
- **C** — proprietary vendor: never copied. Structural inspiration only.

---

## 0 · Regulatory basis (verified 2026-07-23)

Verified against NYSDOH policy **HH0003, *Health Home Quality Management Program***, effective 2017-06-01, **no recorded revision** (the "Revised: September 2017" line on the HHSC web page is a page footer, not a policy revision; the policy's own "Last revised" field is blank).

HH0003 is a **single programme-wide policy** covering Health Homes serving adults and children; the canonical PDF sits in the general Health Homes document path and the HHSC page links to that same file. There is no separate adult instrument.

What the policy establishes:

1. Health Homes must collect, analyse, and report data measuring the effectiveness of care coordination, **including member satisfaction**, with the content areas named explicitly: timeliness of appointments, ease of access to information, quality of communication with care managers.
2. **Member experience surveys** are listed as one permitted method among several (chart reviews, complaint/incident reports).
3. Health Homes **must obtain feedback from members and family members and apply it to QMP processes** — an obligation, with the method left open.
4. Negative outcomes are addressed through a **Performance Improvement Plan** with root-cause analysis, measurable goals, timelines, and possible sanctions.

### 0.1 Boundaries — mandatory claim discipline

These three statements are **prohibited** in any client-facing document, and are checked by the QA layer:

- ❌ *"Improves your redesignation score."* Redesignation **Domain 2 (Quality and Process Measures)** carries 20% of the total score (Quality 10%, Process 5%, prior redesignation result 5%) and is computed from **CMART and Medicaid claims/encounters data only**. No survey-derived measure enters the score. A member survey is evidence of QMP compliance and an operational lever on the measures that *are* scored — nothing more.
- ❌ *"Required by NYSDOH."* The obligation is to obtain and apply member feedback. A survey is one permitted method, not a mandated instrument.
- ❌ *"Replaces / satisfies the state's CAHPS requirement."* NYSDOH sponsors a biennial CAHPS-based member experience survey for adults enrolled in **Medicaid managed care plans**, used to compare **plans**. Its unit of evaluation is the plan; it says nothing about a Health Home, a CMA, or a care manager. Not to be confused either with the voluntary electronic **CMA survey** the Department sends before a redesignation review, which is about the LHH's oversight of its network and is explicitly excluded from the final score.
- ❌ *"Comparable to HCBS CAHPS benchmarks."* **(Added 2026-07-30, D-CX-10.)** The source instrument is validated in its entirety and not in parts; a sponsor that adds items beyond the core set and approved supplements cannot submit to the HCBS CAHPS Database; and our mode is not the published mode. Our instrument is a subset plus a substantial tier A block, fielded by SMS, mail and phone. Verbatim wording buys attribution and format familiarity — **it does not buy a benchmark.** The comparison this product offers is cross-agency within the network (§12).

**The defensible commercial statement is the narrow one:** the obligation exists, the method is unspecified, and the state's own SPA measure framework names *Experience of Care* as one of three measure categories while populating it with none. ⚑ *`O-CX-3`: the SPA measure table is dated November 2017; confirm no newer published version before this sentence goes into a client-facing document.*

---

## 1 · How modules combine: need → study design map

| Client need (trigger) | Modules | Target length | Primary deliverable focus |
|---|---|---|---|
| QMP evidence base / annual member feedback cycle | RAT + CMH + COM + ACC + POC + UNM + OPN | 10–12 min | Documented member feedback applied to QMP, with cross-agency comparison |
| Cross-CMA performance comparison for the LHH | RAT + CMH + COM + ACC + COORD + SEF | 10–12 min | Where agencies diverge, and on what |
| Pre-redesignation readiness | RAT + CMH + POC + GRV + UNM + OPN | 12–14 min | Documented QMP loop; Domain 1 evidence (not Domain 2 score) |
| Access & equity review | ACC + LNG + UNM + COORD + segmentation from roster | 8–10 min | Coverage and access gaps by language, programme, agency |
| Post-PIP verification | Modules matching the PIP's root cause + RAT | 6–8 min | Movement against the PIP's stated goals |

**Length budget.** The mode is SMS/mail with phone fallback (D-CX-5), so the budget is tighter than Employee: **20–26 closed items**, ≤ 10 minutes by phone. Segmentation is supplied by the roster, not asked (§9), which buys back 4–6 items relative to a self-administered design.

---

## 2 · Cross-cutting standards

### 2.1 Scales — HCBS CAHPS conventions adopted (D-CX-3)

The instrument follows the response formats used by the **CAHPS Home and Community-Based Services (HCBS) Survey**, because those are the formats this buyer's world reads, and because they are appropriate to a population where literacy varies, translation multiplies ambiguity, and long matrices are hostile over the phone.

- **Frequency items:** 4-point — Never · Sometimes · Usually · Always.
- **Occurrence / unmet-need items:** Yes · No.
- **Recommendation items:** 4-point — Definitely no · Probably no · Probably yes · Definitely yes.
- **Global ratings:** 0–10. *Anchor wording resolved: it is transcribed verbatim in both baseline languages at `tier-b-source-items.md` §3.5 and is pulled from there, never reconstructed from memory. Note that the published anchors run "the worst / best help from {care manager} possible" — they anchor on the help, not on the person (§3, D-CX-14).*
- **No agreement (Likert) matrices.** The Employee 7-point fully verbalized scale does **not** transfer. Layer 3 is rebuilt, and mixing an agreement matrix into a CAHPS-shaped instrument would produce an instrument that reads as neither.

**Reporting rule, stated once in §Method of every report:** all composites and items are reported as **top-box** (the most positive response option, or the two most positive where the source measure defines it that way), with the exact definition printed per measure. ⚑ *One residual dependency (`O-CX-6`): the source's own top-box definition for the 0–10 global rating is not stated in either uploaded source document, and §2.1 forbids supplying it from memory. Obtain the measure specification before the codebook session. Every other tier B item in the closed set is a single item on a scale whose most positive option is unambiguous, so this is one question, not a blocker.* Means are not reported for these items. A negatively worded item's top box is the response indicating the need *was* met — this is stated at the exhibit, not buried.

### 2.2 Anonymity & reporting thresholds (D-CX-6)

- **No breakout for any group of N < 5**, with the complement check (a suppressed cell must not be recoverable from the total minus the reported cells). Suppressed cells print as "n/a (below reporting threshold)", never silently dropped.
- **Within-agency subgroup breakouts require N ≥ 10**, not 5. Rationale: in a network where an agency is identifiable by name, agency × subgroup approaches individual identification faster than headcount alone suggests.
- **Care-manager-level reporting is excluded by policy** — stated explicitly in the report, in the member-facing text, and in the engagement contract.

**This is a choice, not a constraint, and the report argues it rather than asserting it.** Caseloads run 50–60 members per care manager, so at a realistic response rate a care-manager cell holds roughly 15–30 completes — technically reportable. Three arguments against reporting it anyway, in ascending order of force:

1. **Reliability.** Entity-level CAHPS reporting is built on far larger cells: in the measure developer's own testing, median entity-level responses ranged from about 85 to 123 per measure, and the developer's field test reports effective sample sizes running from roughly 70 for the weakest composite to 376 for the care-manager composite, against a **recommended target ESS of 400**. At n ≈ 20 on 4-point items, a care-manager-level top-box rate is dominated by sampling noise, and the difference between two care managers will usually be unreadable.

   **The same figures bear on the planning target (`O-CX-5`).** At ~100 completes per agency, ten agencies clear 400 comfortably at network level, but the care-manager-support composite is **not reliably reportable at agency level** — which is the level the LHH will want it at. This turns the per-agency completes question from a budget question into a design question: *what is reported at which level, and at what n.* It is answered before fieldwork is quoted, not after.
2. **Identification in practice.** An aggregate of 20 is not anonymity when the respondent pool is a named caseload and the member's circumstances are distinctive. Any crossing at all — language, programme, length of enrolment — closes the gap.
3. **Measurement validity, and this is the decisive one.** The instrument is sold on the promise that individual answers do not reach the care manager. Reporting at care-manager level does not literally break that promise, but members will not read it that way. Once a member believes an honest answer can damage a specific person they depend on, the honest answer stops arriving: top-box rates rise, variance collapses, and the instrument loses exactly the discriminating power the LHH is buying. **A performance-management instrument for individual staff and a QMP measurement instrument cannot be the same instrument.**

Where the LHH's real question is about staff performance, the answer is caseload-characteristic breakouts — by length of the member–care-manager relationship, by caseload size band, by supervisory unit where units are large enough — which locate the problem without naming a person. ⚑ *If the LHH insists on care-manager-level output, it is a contractually separate product with its own consent language and its own minimum-N rule, and the recommendation stands against it for v1.*
- Open-ended responses are paraphrased where verbatim text could identify the speaker. Programme and agency metadata attach to a quote only above threshold.

### 2.3 Data quality screening

Pre-registered in the technical appendix, applied before analysis. The Employee rule set does not transfer unchanged — there are no long matrices to straightline and no shared kiosks.

- **Interviewer-administered (phone):** call-attempt log, interview duration distribution, interviewer-level response-pattern review (an interviewer effect is a real threat when the instrument is short and the scale is 4-point).
- **Self-administered (SMS/web):** completion under 1/3 of median duration → flag; identical response across an entire module with no variance → flag; combined → exclude.
- **Proxy completion:** recorded as a variable, not silently allowed. Family/caregiver-assisted responses are reported as a rate and available as a breakout, because in this population assistance is common and is not a defect.
- Every report states: N in frame → N contacted → N completed → N after screening → screening rate, by agency.

### 2.4 Item ID convention

Stable IDs (`RAT-01`, `CMH-B-03`, `UNM-HOU`) used in the codebook, crosstab workbook, and the `{{braces}}` template. IDs never change meaning between waves; revised wording gets a suffix (`RAT-01b`). A `-B-` segment in the ID marks a **tier B** item (§2.5). **The set of `-B-` IDs is closed** — six items, enumerated in §2.5 — so a `-B-` ID outside that list appearing in the **codebook, questionnaire, crosstab workbook or template** is an error, and the QA layer checks for it. Retired `-B-` IDs (`CMH-B-02`, `CMH-B-03`, `COM-B-01…03`) survive in this framework's prose and in the provenance appendix as a record of decisions taken; they are never re-issued and never attach to a fielded item.

### 2.5 IP determination — HCBS CAHPS (D-CX-9, corrected and closed 2026-07-30)

**The HCBS CAHPS Survey is tier B, not tier C.** It was developed by CMS for voluntary use by state Medicaid programmes, received the CAHPS trademark in June 2016, and its 19 derived measures (7 composite + 12 single-item) received NQF endorsement in October 2016. Sponsors may administer it provided the questionnaire is administered independently and data are submitted to CAHPS specifications.

**Source of record.** CAHPS® Home- and Community-Based Services Survey, **version 1.0, adult, last updated 19 January 2017**, English and Spanish, distributed via Medicaid.gov; trademark held by AHRQ. Currency confirmed 2026-07-28: no successor version is published, and the CAHPS Database accepts 1.0 and 1.0-with-Employment-Module only. Verbatim text, both languages, is held in `references/tier-b-source-items.md`.

#### What verbatim use buys — corrected (D-CX-10, owner sign-off 2026-07-30)

v0.2 stated that a tier B item used exactly as published "is comparable and attributable." **The first half does not survive contact with the source's own administration guidance.** Three findings, each from the published TA guide:

1. The instrument is validated **in its entirety plus approved supplemental items, and not in parts.** Adding any question beyond the core set and approved supplements removes the possibility of submitting to the HCBS CAHPS Database.
2. The trademark condition confirms the same boundary from the other side: an instrument may be called a CAHPS Survey only if the sponsor retains **all 69 core items** without modifying or reordering questions or response options. The naming decision and the subsetting decision are therefore the same decision.
3. The published instrument is **interviewer-administered**; our mode is SMS/mail primary with phone fallback (D-CX-5). Identical wording in a different mode is not the same measurement — the vendor instructions assume text read aloud, interviewer probing, and an `UNCLEAR RESPONSE` code only an interviewer can assign.

Our instrument is a subset plus a substantial tier A block, fielded in a different mode. **It is outside validated use by construction.**

> **Corrected rationale of record.** Verbatim use of a tier B item buys **attribution, format familiarity to the buyer, and freedom from the borrowed-paraphrase defect.** It does **not** buy comparability with published HCBS CAHPS results or database benchmarks.

**This does not reverse the verbatim-or-nothing rule.** That rule was never only about comparability; it is also what stops us shipping lightly reworded CAHPS items, which remains the genuinely bad outcome — no comparability *and* a paraphrase that reads as borrowed. What changes is what may be said about it, internally, in the provenance appendix, and above all in front of a client: see §0.1, fourth prohibited claim.

#### The four governing constraints

1. **Trademark.** "CAHPS" is a registered trademark of AHRQ. An instrument may not carry the CAHPS name without AHRQ's permission, which is granted only against AHRQ's criteria for purpose, content, methodology, and development process. Our deliverable is therefore **not** named "…CAHPS…". Where tier B items are used, the instrument is attributed to the HCBS CAHPS Survey in the provenance appendix — which is what AHRQ recommends when a sponsor does not use the name.

2. **Verbatim or not at all.** A tier B item is either used **exactly as published** — in which case it is attributable and carries the buyer's expected format — or it is not used and an original tier A item takes its place. This document therefore carries **tier B slots, not tier B wording.** Exact text is pulled from `tier-b-source-items.md` at drafting.

3. **The bright line: "transfers" is kept, "transfers in part" is not (D-CX-11, owner sign-off 2026-07-30).** Transferability is checked **item by item, never block by block**, and the determination is recorded per slot. The rule applied to those determinations is now a rule, not a case-by-case judgment:

   - a slot whose determination is an unqualified **transfers** is filled **verbatim**;
   - a slot whose determination is **transfers in part** — because a screen, a denominator, a response scale or a fixed non-fillable clause would have to be altered to make it administrable — is **not** filled from the source. It becomes an original **tier A** item.

   **Ground.** After the correction above, every "in part" case was being paid for with a comparability we do not have. A verbatim item sitting behind a screen we wrote ourselves has a denominator that is not the published denominator, so what survives is **wording only** — the one form of tier B that buys nothing at all while still carrying the licence and provenance overhead. The rule is stated here rather than re-argued per item, because a rule survives between sessions and a series of individually reasonable outcomes does not.

4. **Language (D-CX-12, owner sign-off 2026-07-30).** For tier B slots the **official Spanish is used verbatim**; TRAPD (§8.5) applies to **tier A items only**. Our own reconciliation review still runs over the official Spanish as a documented quality check, never as a licence to amend it. Three grounds: a tier B item we translate ourselves is not the published item, so whatever verbatim buys, it buys per language; the source's own translation process was architecturally equivalent to ours (two independent forward translators, separate bilingual reconciliation); and the official Spanish is demonstrably an **adaptation rather than a translation** — it localises the reference language in several items and restructures one item from sentence-completion to wh-question — so we could not reproduce it by translating even if we tried.

   **Consequence for §8.5.** The CAHPS Database accepts only the official English and Spanish versions and excludes independently translated languages. **Every language beyond EN/ES is tier A throughout.** A bilingual instrument and a seven-language instrument are therefore not the same instrument with respect to tier B, and the coverage figure §8.5 requires must be read with that in mind.

#### The tier B set, closed

Six items. Any `-B-` ID outside this table appearing on a **fielded** item is an error (§2.4).

| Slot | Item | Source | Determination |
|---|---|---|---|
| `RAT-B-01` | Rating of the help received from the care manager (0–10) | Q54 | transfers |
| `RAT-B-02` | Recommendation of the care manager (4-point) | Q55 | transfers |
| `CMH-B-00` | Whether the member knows who their care manager is — **gate** | Q48 | transfers |
| `CMH-B-01` | Reachability (Yes/No) | Q49 | transfers |
| `POC-B-01` | Whether the plan contains what matters to the member (4-point) | Q56 | transfers |
| `POC-B-02` | Who the member would talk to in order to change the plan (multiple response) | Q58 | transfers |

**Converted to tier A by the bright line or by absence of a source item:** `CMH-B-02` (Q50+Q51 — dropped entirely, §4) · `CMH-B-03` → `CMH-03` (Q52+Q53 — the screen carries fixed non-fillable HCBS service content) · `UNM-TRN` (Q59 — a 4-point frequency item inside a Yes/No module, §8.2) · `COM-B-01…03` (no care-manager-referenced communication item exists in the source at all, §5).

**The dropped items are recorded, not deleted.** `tier-b-source-items.md` §7 is the register, and it is reproduced in the provenance appendix so that a reader comparing our instrument to the published measure set sees a **decision** rather than an omission.

#### Route from source to questionnaire

`tier-b-source-items.md` is the **only** authorised route. The questionnaire copies from it; it does not go back to the PDF, and it never works from memory. A tier B string appearing in any artefact without a matching entry in that file is a defect.

#### Reference-layer file naming (D-CX-16, owner sign-off 2026-07-30)

Internal reference files carry **neutral names** — the instrument is named in full *inside* the file, where provenance requires precision, and not in the filename, which propagates by accident into commit messages, directory listings and screenshots. Constraint 1 binds deliverable titles; this convention extends the same discipline to the reference layer at no cost.

**Codebook requirement.** Every item carries three fields: `ip_tier` (A/B), `wording_source` (original / HCBS CAHPS verbatim + item number), `concept_overlap_with_published_instrument` (yes/no). Tier A items with conceptual overlap are legitimate and expected; tier A items with borrowed phrasing are a defect and are caught here.

---

## 3 · Module RAT — Global ratings & recommendation (criterion layer)

**Decision question:** How do members rate the care management they receive, and would they recommend their care manager?

| ID | Item | Tier |
|---|---|---|
| RAT-B-01 | **Rating of the help received from the care manager (0–10)** | **B** |
| RAT-B-02 | Recommendation of the care manager to family and friends (4-point) | **B** |
| RAT-01 | Overall rating of the Health Home programme as a whole (0–10) | A |

**`RAT-B-01` measures the help received, not the person — D-CX-14 (owner sign-off 2026-07-30).** v0.2 labelled it "global rating of the care manager." The published item does not say that: its anchors run *the worst / best help from {care manager} possible*, and it asks the member to rate **the help you get**. The label is corrected because §9.2 turns on what the criterion actually measures, and "rating of help received" and "rating of the person" are different constructs.

**The correction cuts in our favour.** §2.2 excludes care-manager-level reporting on the ground that a performance-management instrument for individual staff and a QMP measurement instrument cannot be the same instrument. A criterion that rates *the help received* rather than *the care manager* is the consistent choice for that position — the relabel removes a tension in v0.2 rather than creating one.

`RAT-B-01` is the **primary criterion** for the driver model (§9.2). `RAT-01` separates the care manager from the programme — a distinction the LHH needs and the HCBS instrument does not make, because a member can be well served by a care manager inside a programme that is not delivering, and the LHH's levers differ in the two cases.

**Caveat disclosed:** global ratings are summary judgments, useful as criteria and as trend metrics, weak as diagnosis. Never reported without the composites that predict them.

---

## 4 · Module CMH — Care manager support

**Decision question:** Does the care manager actually help — with what, and where does help fall short?

| ID | Item | Tier |
|---|---|---|
| CMH-B-00 | Whether the member knows who their care manager is. (Yes/No) — **gate** | **B** |
| CMH-B-01 | Reachability: the member could contact the care manager when they needed to. (Yes/No) | **B** |
| CMH-01 | Follow-through: when the care manager says they will do something, it gets done. (frequency) | A |
| CMH-02 | The care manager knows the member's situation without needing it re-explained each time. (frequency) | A |
| CMH-03 | The care manager worked with the member when a change to their services was asked for. (Yes/No, behind an original need screen) — *wording to be drafted, `O-CX-11`* | A |

**`CMH-B-00` is the gate, and it is adopted as a slot in its own right (D-CX-15, owner sign-off 2026-07-30).** In the source, Q48 gates the entire care-manager block: both `RAT-B` items and the `CMH-B` items are administered behind it. Taking those slots without their gate changes five denominators, which is the one modification this framework's own logic cannot tolerate. It is also a first-order finding on its own — *does the member know who their care manager is* is actionable at agency level, and an LHH will read a low rate as an assignment or onboarding failure rather than a service-quality one. **Reported as a standalone rate; excluded from the composite.**

**`CMH-B-02` (help with getting or fixing equipment) is dropped.** It clears the bright line on wording but fails on fit and on base rate: durable medical equipment is an HCBS-shaped exemplar, it will be a "don't need" for a large share of a Health Home roster, and on the screened denominator at ~100 completes per agency the cell lands at 15–20 and trips the N ≥ 10 rule (§2.2) on any crossing at all. It would be **routinely unreportable at exactly the level the buyer wants.** Composite-label integrity was the only argument on the other side, and D-CX-10 prices that at zero.

⚑ **If the content is wanted, its place is `UNM`, not `CMH`** — as an original tier A unmet-need item with a proper need screen, where the module's whole logic already handles no-experience states correctly. Registered as `O-CX-12`, not adopted here.

**`CMH-03` replaces the tier B pair Q52+Q53.** The item text (Q53) is population-neutral and would have transferred; the screen (Q52) does not. Its clause *"or for help with getting places or finding a job"* is **fixed published text, not a fill**, and it names two HCBS service categories — medical transportation and employment supports — that are not Health Home care-management services. Verbatim-or-nothing forbids deleting it, and a member who cannot answer the screen correctly corrupts the item's denominator anyway. Under the bright line the whole pair converts to tier A.

**Composite composition.** The CMH composite is **`CMH-B-01` + `CMH-01` + `CMH-02` + `CMH-03`**, and it is **ours, not the source's** — the "Case manager is helpful" label is not claimed, and under D-CX-10 could not be. It mixes Yes/No and 4-point frequency items, which is admissible **only because reporting is top-box** (§2.1): every item reduces to a proportion, so the composite is the mean of item-level top-box rates with the composition printed at the exhibit. It is never reported as a scale mean.

`CMH-01` and `CMH-02` remain the two things members of care-managed programmes complain about that no source composite isolates: promises that do not close, and continuity lost to caseload churn. Both are actionable by the LHH at agency level.

---

## 5 · Module COM — Listening & communication

**Decision question:** Is communication working — in both directions?

**All tier B slots in this module are struck (D-CX-13, owner sign-off 2026-07-30). The module is entirely tier A.**

**Why.** v0.2 specified the source's "Staff listen and communicate well" composite, *care-manager-referenced subset only*, with the rest dropped rather than rewritten. The item-by-item check produced a result the framework anticipated in form but not in size: **the care-manager-referenced subset is empty.** Every communication item in the source (Q28–Q34, and the parallel battery at Q41–Q45) is anchored to paid in-home staff or homemakers. The *Your Case Manager* section contains a gate, two need-screened service items, one reachability item and two ratings — **and no communication item at all.** The published instrument never asks whether the case manager listens, explains, or treats the member with respect. That is a real gap in the source, not an artefact of our reading of it.

**The route explicitly rejected.** One item could be re-pointed at the care manager by substituting its fill. It must not be. Those braces are populated from the titles the member gives for **paid in-home staff**, not from the case-manager title collected elsewhere. Substituting across that boundary changes the item's population — a rewording in exactly the sense §2.5 rule 2 exists to prevent, yielding an item that looks published, is not, and carries a borrowed phrasing we could not defend in a provenance appendix. **If an item has to be reframed to fit, that is the signal to stop, not the licence to proceed.**

| ID | Item | Tier |
|---|---|---|
| COM-01 | Explanations are given in a way the member can act on, not just understand. (frequency) | A |
| COM-02 | *(slot)* The member is listened to — what they say is taken in, not worked around. (frequency) | A |
| COM-03 | *(slot)* Things are explained in terms the member understands. (frequency) | A |
| COM-04 | *(slot)* The member can tell the care manager when something is not working. (frequency) | A |

⚑ **`COM-02…04` are constructs, not wording — `O-CX-10`, drafted at the questionnaire session with owner sign-off.** Two constraints on that drafting, recorded now so they are not rediscovered late:

- **These are tier A items and must be written as original formulations.** The source's staff-referenced communication battery is the nearest available phrasing and is therefore the specific trap: reaching for it produces precisely the borrowed-paraphrase defect the codebook's `wording_source` field exists to catch.
- **`COM-04` is the item that delivers the module's stated decision question.** `COM-01/02/03` all run care manager → member. Whether a member feels able to say that something is not working runs the other way, and it is distinct from `GRV` (which asks about a formal problem, after the fact) and from `POC-03` (which is about choice between options). Without it the module measures one direction and claims two.

---

## 6 · Module ACC — Access & timeliness

**Decision question:** Can the member reach their care manager when it matters, and does contact happen at the promised frequency?

Directly aligned with the content areas HH0003 names (timeliness of appointments, ease of access to information).

| ID | Item | Tier |
|---|---|---|
| ACC-01 | The member can reach the care manager when they need to. (frequency) | A |
| ACC-02 | Time to a response after leaving a message. (banded categories) | A |
| ACC-03 | Contact happens as often as the member was told it would. (frequency) | A |
| ACC-04 | Help getting an appointment when one was needed. (Yes/No, with a "did not need one" screen) | A |

**Screening logic:** `ACC-04` is asked only of members who needed an appointment. A "no experience" state is never recoded as a negative — the Employee rule that no-experience ≠ dissatisfaction carries over intact as a **[BOILERPLATE — DO NOT EDIT]** invariant.

⚑ **`ACC-01` and `CMH-B-01` are the same construct on different scales — `O-CX-8`, resolved at drafting.** `ACC-01` is tier A and 4-point frequency; `CMH-B-01` is tier B, Yes/No, and verbatim. Fielding both is redundant and will read as a repeat to a member on the phone, so **one of them goes.** The trade is real in both directions: keeping `ACC-01` preserves gradation and keeps the ACC module on one scale; keeping `CMH-B-01` preserves the composite's only verbatim item and the shorter cognitive load of a binary. It is deferred rather than decided because the answer depends on the mode (`O-CX-2`) — gradation costs more by phone than by SMS. `ACC-02` (time to response) and `ACC-03` (promised contact frequency) are unaffected either way and are not substitutes for either.

---

---

## 7 · Module POC — Plan of Care participation & choice

**Decision question:** Is the plan of care the member's, or the agency's?

| ID | Item | Tier |
|---|---|---|
| POC-B-01 | Whether the plan contained what matters to the member. (4-point) | **B** |
| POC-B-02 | Who the member would talk to in order to change the plan. (multiple response) | **B** |
| POC-01 | The member knows what is in their plan of care. (Yes/No) | A |
| POC-02 | The member's own priorities are in the plan. (frequency) | A |
| POC-03 | The member was offered a real choice between options, not a single option presented. (frequency) | A |

This module is where the person-centred language of the programme becomes measurable, and it is the strongest QMP-facing content in the instrument. Both tier B slots transfer cleanly: the fills carry the Health Home plan-of-care term, and the constructs presuppose nothing about HCBS service receipt.

⚑ **`POC-02` and `POC-B-01` are close enough to require a stated distinction — `O-CX-9`, resolved at drafting.** Do not field both without one. The available distinction is that `POC-B-01` asks how much of what matters is *in* the plan (a coverage judgment, 4-point) while `POC-02` asks whether the member's priorities *get there* (a process judgment, frequency); if that distinction does not survive cognitive testing, `POC-02` goes.

⚑ **`POC-B-02` carries a mode caveat (`O-CX-7`).** It is an interviewer-coded multiple-response item whose unprompted "anyone else?" probe *is* part of its design. In SMS or mail it becomes a check-all-that-apply grid, which is a different instrument administering the same words. Not resolvable until the mode is fixed.

---

## 8 · Module COORD, UNM, GRV, RSP, LNG — service reality

### 8.1 COORD — Coordination across medical, behavioural health, and social services

| ID | Item | Tier |
|---|---|---|
| COORD-01 | Help connecting to medical care when needed. (Yes/No + screen) | A |
| COORD-02 | Help connecting to mental health or substance use services when needed. (Yes/No + screen) | A |
| COORD-03 | Providers involved in the member's care appear to know what the others are doing. (frequency) | A |

### 8.2 UNM — Unmet needs (social determinants)

Yes/No, top-box = need met. Asked with an explicit need screen; a member without the need is not counted as unmet.

`UNM-HOU` housing · `UNM-TRN` transportation to appointments · `UNM-FOD` food · `UNM-BEN` benefits and entitlements · `UNM-OTH` other unmet need (open follow-up). **All tier A.**

**`UNM-TRN` is resolved as the tier A item (owner sign-off 2026-07-30; closes v0.2 §13.1 item 2 and ROADMAP §5 item 3).** The source analogue (Q59) transfers on content — it presupposes nothing about who provides the transport, and it is the one source item in the whole set that measures an unmet need directly. It is declined anyway, on three costs the v0.2 flag did not price:

- it is a **4-point frequency item with no need screen**, so it would sit on a different scale from every other item in this module;
- the module could then not be reported as a single unmet-need count or index without a recode, and recoding a tier B item is exactly what §2.5 rule 2 forbids;
- *"never / sometimes"* is not the statement *"the need was unmet"* — a member with no medical appointments in the period still answers.

The argument for taking the slot was comparability, and after D-CX-10 there is none. Module coherence and a uniform top-box rule are worth more than a format familiarity of one item. **Do not field both.**

⚑ **`UNM-DME` — proposed, not adopted (`O-CX-12`).** If access to durable medical equipment is wanted as content (see §4), it belongs here as an original tier A item with a need screen, on the module's own Yes/No scale — not as a screened tier B pair inside `CMH`. Owner decision at drafting; it costs one item against the length budget.

### 8.3 GRV — Problems and their resolution

| ID | Item | Tier |
|---|---|---|
| GRV-01 | Had a problem with the programme or with an agency in the past 12 months. (Yes/No) | A |
| GRV-02 | If yes: the member knew how to raise it. (Yes/No) | A |
| GRV-03 | If yes: it was resolved. (Yes/No) | A |

This is the module that connects directly to the complaint/incident stream HH0003 already requires, and it is the one most likely to produce a finding the LHH acts on the same quarter.

### 8.4 RSP — Respect and safety

| ID | Item | Tier |
|---|---|---|
| RSP-01 | The member is treated with respect by programme staff. (frequency) | A |
| RSP-02 | The member's personal information is handled in a way they are comfortable with. (frequency) | A |

**Physical-safety items are excluded** (owner decision, 2026-07-23). The source instrument's harm items ("hit or hurt by staff" and equivalents) are not fielded in any configuration of this product. The exclusion is stated in the provenance appendix, so that a reader comparing the instrument to the HCBS CAHPS measure set sees a decision rather than an omission.

#### 8.4.1 Disclosure protocol — required regardless

Removing the item does not remove the event. In a phone-administered interview with a dependent population, a member may disclose harm, neglect, or acute risk spontaneously — most likely in the open-ends (§11) or in `GRV`. The engagement therefore carries a written protocol before fieldwork opens: what the interviewer says, to whom the disclosure goes at the LHH, within what window, and what the member is told will happen next. Interviewers are briefed on it and it is not left to judgment in the moment.

⚑ **`O-CX-2` — owner + counsel:** whether M&M's interviewers fall within any mandatory-reporting obligation in this configuration is a legal question, not a methodological one, and it is answered before the first call — not after a disclosure.

### 8.5 LNG — Language & cultural access (D-CX-7)

| ID | Item | Tier |
|---|---|---|
| LNG-01 | Contact happens in the member's preferred language. (frequency) | A |
| LNG-02 | An interpreter was available when needed. (Yes/No + screen) | A |
| LNG-03 | Written materials arrive in a language the member can read. (frequency) | A |

**Fielding rule, not a fixed language list.** The instrument is fielded in English and Spanish as baseline, plus whatever additional languages are needed to cover **95% of the roster**, determined per engagement from the frame. Reference set for this population, following the languages NYSDOH itself uses for Health Home instruments: Spanish, Chinese (simplified and traditional), Haitian Creole, Russian, Korean, French, Italian. Translation is part of the deliverable: forward translation by two independent translators, reconciliation, back-translation, and documented equivalence review. **The share of roster members excluded by instrument language is reported as a coverage figure in the sample section — not as a sentence in limitations.**

---

## 9 · Criterion variables and the driver model (D-CX-2)

**Decision question:** What actually predicts a member's rating of their care manager — and does the same thing predict the member's capacity to manage their own care?

### 9.1 `EXIT_TYPE` — engagement intent made analysable (owner, 2026-07-23)

Raw intent to stay is unusable here: Health Home care management is designed to move a member toward the point where the service is no longer needed, so disenrollment is frequently the **intended** outcome. A high intent-to-stay score is consistent with good care and with maintained dependence, and ranking drivers of a two-sided criterion produces a list the buyer cannot act on.

**The reason item resolves this.** Intent plus a pre-registered attribution yields a four-type outcome in which each type has a direction the LHH can act on. This is the member-side counterpart of the Employee `STAY_TYPE`, arrived at independently rather than transferred.

| ID | Item | Tier |
|---|---|---|
| ENG-01 | Expectation of still working with the programme six months from now. (4-point) | A |
| ENG-02 | If leaving is expected: the main reason. (pre-coded categories, one main + all-that-apply) | A |
| ENG-03 | If leaving is expected: whether the member expects to get this kind of help somewhere else. (Yes / No / Don't know) | A |

**`ENG-02` pre-coded categories** (fixed before fieldwork, never coded post hoc from open text):

`IND` no longer needs this kind of help — manages medical and social needs independently · `FAM` family or friends now provide the support · `ORG` another organisation provides it · `TRF` transferring to a different care management agency or Health Home · `INEFF` the help received was not useful · `CONT` could not reach or rely on the care manager · `ELIG` eligibility, coverage, or a move · `HLTH` health change · `OTH` other (open follow-up).

**Derivation rule, pre-registered:**

| Type | Definition | What it means to the LHH |
|---|---|---|
| **Graduating** | Expects to leave · reason ∈ {`IND`, `FAM`, `ORG`} | Programme goal achieved. A *high* rate here is good news, and is the finding claims data cannot produce. |
| **Disengaging** | Expects to leave · reason ∈ {`INEFF`, `CONT`, `TRF`} | Service failure. The rate, and its concentration by agency, is the headline. |
| **Constrained continuing** | Expects to stay · bottom-half `SEF` · one or more unmet needs in `UNM` | Continuation without progress toward independence — the member-side analogue of reluctant stayers. |
| **Committed continuing** | Expects to stay · everything else | Neither an alarm nor an achievement. |

`ELIG` and `HLTH` exits are counted and reported but are **outside the LHH's control**, so they are excluded from the Graduating/Disengaging split rather than assigned to one of them. `TRF` sits with Disengaging deliberately: within a network, a member moving between CMAs is a signal about the CMA being left, and the LHH is precisely the party that can act on it.

**Three cautions, stated in the report, not only here.**

1. **`ENG-02` is self-reported attribution, not ground truth,** and the bias runs in a known direction. In a dependent population interviewed by a stranger, "I can manage on my own" is the socially comfortable answer and "the help was not useful" is not. The reason item will therefore **over-count Graduating and under-count Disengaging** if read at face value.
2. **Triangulation is mandatory, and it is the analytic product.** A member coded `IND` who also sits in the bottom box on `CMH` and reports unmet needs in `UNM` is a **masked disengagement**, and the rate of that pattern is reported alongside the raw typology. This is where the divergence exhibit is earned — a real disagreement between what members say drives their exit and what their experience scores imply — rather than copied from the Employee template. Masked disengagement is an **aggregate analytic category and never an individual label**; no member is told, and no report says, that a member's stated reason was disbelieved.
3. **Cell sizes.** At the network level the typology is stable. At agency level, the leaving subset is a fraction of completes and the reason split fragments it further, so **`EXIT_TYPE` is reported by agency only where the leaving subset itself clears N ≥ 10** — otherwise agency-level output is limited to the intent item and the type distribution stays at network level.

**Wave-2 validation (recorded now, executed later).** The stated reason is prospective; the administrative record is actual. From wave 2, `EXIT_TYPE` is validated against realised disenrollment for the same members, which converts the typology from an attitude into a calibrated predictor and is the point at which it becomes genuinely defensible. ⚑ *`O-CX-4`: confirm with the LHH which disenrollment fields it actually holds and at what granularity before this is promised in a proposal.*

**Position in the model.** `EXIT_TYPE` is a **profiling outcome, not the driver-model criterion**: composites are compared across types descriptively and, where cell sizes permit, by multinomial model. The driver model keeps the two criteria in §9.2. Reason: a four-category outcome with an unequal and partly uncontrollable base does not support a ranked list of levers, which is what the driver section exists to produce.

### 9.2 Dual criterion, pre-registered

- **Primary criterion:** `RAT-B-01`, **rating of the help received from the care manager** (0–10). Two grounds, and v0.2 carried a third that has been removed: it is buyer-legible, and it is the conventional criterion for CAHPS-shaped driver analysis (composites → global rating). **v0.2 also claimed it was "comparable to the national database". That claim is false and is struck (D-CX-10, §2.5, §0.1).** The two surviving grounds are sufficient; the criterion does not depend on the deleted one.
- **Secondary criterion:** `SEF` index below — perceived capacity to manage one's own care and navigate services. Aligned with the programme's own stated goal, and non-redundant with the rating of the help received.

**Construct note, and it bears on the sign-off.** `RAT-B-01` rates *the help received*, not the care manager as a person (§3, D-CX-14). This is the reading that makes the dual criterion coherent: the primary criterion asks how well the service worked, the secondary asks what the member can now do, and neither is a judgment of an individual employee — which is what §2.2 requires of every measure in this instrument.

| ID | Item (module SEF) | Tier |
|---|---|---|
| SEF-01 | Confidence in knowing who to contact when a health problem comes up. (4-point) | A |
| SEF-02 | Confidence in managing appointments and medications day to day. (4-point) | A |
| SEF-03 | Confidence in getting help without waiting for the care manager to initiate it. (4-point) | A |

**Analysis standard.**

1. Bivariate first: composite top-box rates against each criterion, client-readable.
2. Then relative importance: dominance analysis or Shapley decomposition over the pre-registered predictor set, because composites are intercorrelated and raw associations over-credit redundant ones.
3. **Significance ≠ importance.** At census scale nearly everything reaches significance; the report ranks by effect size and shows stated-vs-derived comparison where a stated-importance item exists. Full matrices live in the appendix with a multiple-comparison note.
4. **Divergence between the two criteria is the analytical product** — the case where members rate a care manager highly while reporting low capacity to act independently is exactly the finding an LHH cannot get from claims data. It is reported as an exhibit plus prose, **never as a second ranked list**. If the two orderings do not diverge materially, the exhibit is omitted rather than padded.

**Structural caveat carried from Employee:** if an engagement has no criterion worth modelling, the driver section is **absent, not padded for symmetry**. The skeleton yields to the methodology, never the reverse.

⚑ **`O-CX-1` — owner sign-off required on §9 as a whole.** This is the substantive methodological choice of the domain, and it **blocks the questionnaire**. The two objections that stood against it in v0.2 are now answered: the criterion's label is correct (D-CX-14) and its false comparability ground is struck (D-CX-10). What remains open is the choice itself.

---

## 10 · Frame, weighting, and administration

### 10.1 Frame and segmentation (D-CX-4, D-CX-8)

Segmentation is **supplied by the frame, not asked of the member.** The LHH holds the enrolled-population roster; the study record carries a pseudonymous study ID plus roster attributes.

| Field | Source | Weighting cell |
|---|---|---|
| Agency (CMA) | roster | yes |
| Programme (adult / children / HARP / other) | roster | yes |
| Age band | roster | yes |
| Sex | roster | yes |
| Race / ethnicity | roster | yes ⚑ |
| Time enrolled in the programme | roster | no |
| Preferred language | roster | no (used for fielding) |
| Proxy/assisted completion | fieldwork | no |

⚑ **Race/ethnicity as a weighting variable requires a data-quality check before it is used.** Medicaid roster race and ethnicity fields are frequently incomplete or inconsistently coded. If missingness is material, the variable is reported descriptively and excluded from the weighting scheme, with that decision disclosed — a weight built on a 30%-missing variable is worse than no weight.

**Census or sample.** Agencies run from roughly 300 to 6,000 enrolled members, so a single rule does not fit the network. Standard: **census where the agency roster is at or below ~800 members; stratified probability sample above that**, stratified on programme × language, with a per-agency target of completes sufficient for stable agency-level top-box comparison (planning target ~100 completes per agency, consistent with the entity-level cell sizes CAHPS measures are built on). Mode and materials are identical across both routes so that census and sampled agencies remain comparable; which route each agency took is printed in the sample section.

**Weighting standard:** rim (raking) weighting to the **Health Home or agency enrolled population** on agency × programme × age × sex × race, conditional on frame quality. Nonresponse is analysed against roster attributes and printed as a table, not asserted as acceptable. Weight trimming bounds are disclosed in the codebook.

### 10.2 Administration (D-CX-5)

**Independent administration is the product, not a methodological nicety.** The instrument evaluates the care manager, and the care manager cannot be the channel through which it reaches the member.

- **Mode:** SMS and mail primary, **phone fallback**.
- **The phone fallback is not a minor mode.** Members with unstable housing, no reliable mobile, or low literacy fall through SMS and mail first — and they are not randomly distributed across agencies. Phone capacity is resourced multilingually from the outset, and the mode achieved is reported per agency, because a network where one agency's members answered by phone and another's by SMS has a comparability problem that must be visible.
- **Contact list:** held by the LHH and disclosed to M&M under a BAA (§10.3). CMAs neither hold nor see the outbound list.
- **What the member is told,** in the invitation and at the start of the phone interview: who is asking, that the care manager will not see individual answers, that results are reported in group form only, and that participation does not affect services or eligibility. This text is fixed and is reproduced in the report's provenance appendix.

### 10.3 PHI (D-CX-8 — decided (a), with a correction)

Owner decision: **M&M receives the contact data and administers directly.**

⚑ **Correction to the framing.** This cannot be structured as a HIPAA *limited data set*: an LDS excludes telephone numbers, email addresses, and street addresses — precisely the fields required to field by SMS, mail, and phone. The correct structure is a **disclosure of PHI to a business associate for health care operations** (quality assessment and improvement activities), under a signed BAA, with:

- **minimum necessary** applied to the field list — contact fields and nothing else beyond the weighting attributes;
- **contact fields physically segregated** from the analysis file, joined only by study ID;
- **destruction of the contact file at fieldwork close**, with a written certificate to the LHH;
- no direct identifier ever entering the research record, the crosstab workbook, or any deliverable.

⚑ **`O-CX-2` — counsel review required before any instrument text is written.** The mode decision depends on it, and per standing rules this is flagged, not resolved silently.

---

## 11 · Module OPN — Open-ended

| ID | Item |
|---|---|
| OPN-01 | What is the one thing that would most improve the help the member receives? |
| OPN-02 | What is working well that should not change? |
| OPN-03 | (need-specific slot, per engagement) |

**Standard:** thematic coding by two coders with adjudication; theme frequencies cross-tabbed by agency and programme; quotes only above the anonymity threshold and paraphrased where identifying. Phone-administered open-ends are recorded as interviewer-typed summaries, and that fact is disclosed — they are not verbatim and must not be presented as such.

---

## 12 · What transfers from the Employee domain

| Layer | Content | Status |
|---|---|---|
| **1 · Argument structure** | Decision-first summary → objectives → method → sample & coverage → results by objective → driver section → cost-sequenced actions → limitations → provenance appendix | **Carried** |
| **2 · Methodological invariants** | N < 5 suppression with complement check · significance ≠ importance · pre-registered screening · stated vs. derived importance · no external vendor benchmark databases · index rules disclosed · no-experience ≠ negative | **Carried as [BOILERPLATE — DO NOT EDIT]** |
| **3 · Domain content** | Items, modules, indices, criterion, model set, exhibits, `{{braces}}` schema | **Rebuilt.** `GAP_*`, `IDX_BRN`, `STAY_TYPE`, `SAT-00` do not transfer |

**Benchmarking note.** The standing refusal to use external vendor benchmark databases holds. The comparison this product offers is **cross-agency, within network** — which is the comparison the LHH can act on, and which no vendor database provides. **The HCBS CAHPS Database is not a deferred option — it is foreclosed by construction (D-CX-10, §2.5).** Submission requires the full core item set with no additions beyond approved supplemental items; our instrument is a subset plus a substantial tier A block, fielded in a non-published mode. v0.2 described this as "out of scope for v1", which implied a door that could be opened later. It cannot be opened without abandoning the tier A content that is the product. This is stated plainly rather than left as scope language, because the difference matters in front of a client.

---

## 13 · Flags & decisions

### 13.1 Open — stable IDs

**Numbering.** v0.2 numbered these positionally, and the ROADMAP §5 list numbered the same items differently — so a reference to "item 2" meant two things depending on which file the reader had open. IDs are now stable and never reused; the ROADMAP column is the mapping.

| ID | Open item | ROADMAP §5 | State |
|---|---|---|---|
| `O-CX-1` | **§9.2 dual criterion** — primary `RAT-B-01`, secondary `SEF`. `EXIT_TYPE` (§9.1) is settled; this is not. | 1 | **Blocks the questionnaire.** Both v0.2 objections cleared 2026-07-30 |
| `O-CX-2` | **Counsel review** of the §10.3 BAA structure and the §8.4.1 mandatory-reporting question | 2 | **Blocks the questionnaire** — mode determines the instrument's form |
| `O-CX-3` | **SPA measure table currency** — confirm no version newer than November 2017 before the "Experience of Care is empty" sentence is used with a client | 4 | Open |
| `O-CX-4` | **LHH disenrollment fields** and granularity, before wave-2 `EXIT_TYPE` validation is offered in a proposal | 5 | Open |
| `O-CX-5` | **Per-agency completes target.** Now a **design** question, not a budget one: what is reported at which level, and at what n (§2.2) | 6 | Open |
| `O-CX-6` | **Top-box definition for the 0–10 global rating** as the source defines it. Not stated in either uploaded source document; §2.1 forbids supplying it from memory | — | Open, narrow. Needed before the codebook session |
| `O-CX-7` | **Alternate scales and mode artefacts.** The source's cognitive-accommodation alternates are a separate version of the whole survey; `UNCLEAR RESPONSE` and the "anyone else?" probe have no self-administered meaning (§7) | — | **Blocked by `O-CX-2`** |
| `O-CX-8` | **`ACC-01` × `CMH-B-01`** — same construct, different scales. One goes (§6) | — | At questionnaire drafting |
| `O-CX-9` | **`POC-02` × `POC-B-01`** — stated distinction required, or `POC-02` goes (§7) | — | At questionnaire drafting |
| `O-CX-10` | **`COM-02…04` wording** — tier A originals, written without reaching for the source's staff battery (§5) | — | At questionnaire drafting |
| `O-CX-11` | **`CMH-03` wording and its need screen** — tier A original replacing Q52+Q53 (§4) | — | At questionnaire drafting |
| `O-CX-12` | **`UNM-DME`** — adopt an equipment-access unmet-need item, or leave the content out (§4, §8.2) | — | At questionnaire drafting |
| `O-CX-13` | **IP tier propagation.** `shared/instrument-library/index.json` and four instrument banks still carry `reuse_tier: "A"` on CAHPS-derived material | 7 | Open — mechanical, six files, its own session |
| `O-CX-14` | **CG-CAHPS retention** in the healthcare module, or retirement from it | 8 | Open |
| `O-CX-15` | **Tier legend.** Does "own/**official**" cover federal statistical instruments? Proposed reading: no — tier A is original synthesis only | 9 | Open. §2.5 already applies the narrow reading to this instrument |
| `O-CX-16` | **Automated voice** — confirm exclusion, or keep open | 11 | Open |
| `O-CX-17` | **"ARA" vs "Measure & Meaning"** across the skill library | 12 | Open — library-wide, not a CX decision |

**Closed 2026-07-30 and not carried forward:** v0.2 §13.1 item 2 / ROADMAP §5 item 3 (`UNM-TRN` → tier A, §8.2) · ROADMAP §5 item 10 (header repo path) · the seven flags raised in `tier-b-source-items.md` v0.1 §9, all of which are recorded as decisions below or as `O-CX-6` / `O-CX-7`.

### 13.2 Resolved (decisions log)

- **2026-07-23** Positioning: CX domain built as the Health Home member-experience vertical; buyer = Lead Health Home (owner).
- **2026-07-23** Three-layer transfer rule adopted (§12) (owner).
- **2026-07-23** **D-CX-3** Reporting convention = HCBS CAHPS response formats, top-box reporting, no agreement matrices (owner).
- **2026-07-23** **D-CX-4** Weighting frame = Health Home / agency enrolled population, rim weighting on agency × programme × age × sex × race, conditional on frame quality (owner).
- **2026-07-23** **D-CX-5** Mode = SMS/mail primary, phone fallback; independent administration; contact list held by LHH, not CMA (owner).
- **2026-07-23** **D-CX-6** Reporting units = network and agency; N < 5 suppression with complement check; N ≥ 10 for within-agency subgroups; **care-manager-level reporting excluded by policy** (owner + Claude). *(v0.2 printed this as "excluded pending confirmation of item 13.1.2" — a stale cross-reference to what was then the `UNM-TRN` flag. The exclusion was never conditional on it; corrected 2026-07-30.)*
- **2026-07-23** **D-CX-7** Language rule = EN + ES baseline plus coverage to 95% of roster; back-translation documented; language-exclusion rate printed as a coverage figure (owner).
- **2026-07-23** **D-CX-8** PHI route (a): M&M receives contact data under BAA and administers directly — structured as a health-care-operations disclosure, not a limited data set (owner, with correction).
- **2026-07-23** **D-CX-9** HCBS CAHPS classified **tier B**; verbatim-or-not-at-all rule; no "CAHPS" in the deliverable name; attribution in the provenance appendix; per-item transferability check (owner + Claude).
- **2026-07-23** Claim discipline §0.1 adopted: no redesignation-score claim, no "required" claim, no CAHPS-substitution claim (Claude, from verification).
- **2026-07-23** **`EXIT_TYPE` adopted** — intent plus pre-registered reason yields Graduating / Disengaging / Constrained continuing / Committed continuing; profiling outcome, not driver criterion; triangulated against experience composites, with masked disengagement as an aggregate category only (owner).
- **2026-07-23** **Physical-safety items excluded** from all configurations; disclosure protocol required regardless of item set (owner).
- **2026-07-23** **Care-manager-level reporting excluded by policy**, on reliability, identification, and measurement-validity grounds; caseload-characteristic breakouts offered instead. Caseloads: 50–60 members per care manager; agencies 300–6,000 members (owner + Claude).
- **2026-07-23** Census below ~800 roster members per agency, stratified sample above (Claude, from the caseload figures).
- **2026-07-28** Tier B source assembled: `references/tier-b-source-items.md` v0.1 — source version-stamped (HCBS CAHPS 1.0, 2017-01-19) and currency-checked, seven response scales and four fills transcribed verbatim in EN and ES, every slot determined item by item, dropped-items register built (Claude).
- **2026-07-30** **D-CX-10** **Verbatim rationale corrected.** Verbatim use buys attribution, format familiarity and freedom from the borrowed-paraphrase defect — **not** comparability with published results or the CAHPS Database. Grounds: the instrument is validated only in its entirety, partial instruments cannot be submitted to the database, and our mode is not the published mode. A fourth prohibited claim is added to §0.1; §9.2 and §12 corrected accordingly. The verbatim-or-nothing rule is unchanged (owner).
- **2026-07-30** **D-CX-11** **Bright line adopted.** Determination *transfers* → filled verbatim; determination *transfers in part* → original tier A item. **The tier B set is closed at six items** (§2.5). Adopted as a rule rather than as a series of item-level outcomes, because a rule survives between sessions. Consequences: `CMH-B-02` dropped, `CMH-B-03` → `CMH-03` tier A, `UNM-TRN` → tier A (owner).
- **2026-07-30** **D-CX-12** **Official Spanish verbatim** for tier B slots; TRAPD for tier A only; our reconciliation review runs as a quality check, never as a licence to amend. All languages beyond EN/ES are tier A throughout (owner).
- **2026-07-30** **D-CX-13** **`COM-B-01…03` struck.** The source contains no care-manager-referenced communication item; the subset is empty, not small. Module rebuilt as four tier A items; re-pointing a staff-referenced item at the care manager explicitly rejected (owner).
- **2026-07-30** **D-CX-14** **`RAT-B-01` relabelled** to "rating of the help received from the care manager" — the published anchors and stem rate the help, not the person. §9.2 corrected; the relabel is consistent with §2.2's exclusion of care-manager-level reporting (owner).
- **2026-07-30** **D-CX-15** **`CMH-B-00` adopted** (source Q48) as the gate for the whole care-manager block, reported as a standalone rate and excluded from the composite. Without it five denominators change (owner).
- **2026-07-30** **D-CX-16** **Reference-layer file naming**: internal reference files carry neutral names; the instrument is named in full inside the file, not in the filename (owner).

---

*Document owner: A. Akhtyrskii · Measure & Meaning Research · Prepared with Claude · v0.3 · 2026-07-30 · illustrative + synthetic · tier B source items reproduced verbatim from a publicly distributed CMS instrument, attributed in the provenance appendix, instrument name excluded from all deliverable titles.*
