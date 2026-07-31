# Tier B source items — verbatim text and transferability determinations

**Repo target:** `skills/domain-healthcare-cma/references/tier-b-source-items.md`
**Version:** 0.1 · 2026-07-28 · **Status:** draft — three determinations and six flags require owner sign-off before any questionnaire line is written.
**Governs:** every `-B-` slot in `references/module-framework-cx.md` v0.2 (framework §2.5, §3, §4, §5, §7, §8.2).
**Prepared with Claude · one task per session · principal-led · flag-first.**

> **File naming.** This file is an internal reference, not a deliverable, so framework §2.5 rule 1 ("the deliverable is not named …CAHPS…") does not strictly bind it. The neutral name is used anyway, because a file name propagates by accident into commit messages, directory listings and screenshots, and a neutral one costs nothing. The source *is* named in full inside the file, where it belongs — provenance requires precision, not euphemism. ⚑ **Flag F, owner:** confirm the naming convention so it can be applied to the rest of the reference layer.

---

## 0 · What this file is, and how it is used

`module-framework-cx.md` v0.2 carries **tier B slots, not tier B wording** (§2.5 rule 2). This file fills those slots with the exact published text, in both baseline languages, and records for each one a **determination**: transfers / transfers in part / does not transfer, with the ground stated.

Three rules govern reading it:

1. **A dropped item is recorded as dropped, not deleted.** §7 is the register. The provenance appendix must be able to show a reader comparing our instrument to the published measure set a *decision*, not an omission.
2. **The determination is the output, not the transcription.** Where a slot cannot be filled, the answer is an original tier A item (§2.5 rule 2), never a paraphrase of the source. That happened three times — see §5.3.
3. **This file is the only authorised route from source to questionnaire.** Once the two questionnaire blockers clear, `questionnaire-cx-member-experience.md` copies from here. It does not go back to the PDF, and it never works from memory.

---

## 1 · Source identification and version stamp

| Field | Value |
|---|---|
| Instrument | CAHPS® Home- and Community-Based Services Survey |
| Version | **1.0** |
| Population | Adult |
| Last updated (per source cover) | **January 19, 2017** |
| English source file | `CAHPSHcbs01192017SurvEng508` (canonical: `cahps-home-and-community-based-services-survey-10-english.pdf`) |
| Spanish source file | `CAHPSHcbs01192017SurvSpa508` (canonical: `cahps-home-and-community-based-services-survey-10-spanish.pdf`) |
| Developer / distributor | Centers for Medicare & Medicaid Services; distributed via Medicaid.gov. Trademark held by AHRQ. |
| Supporting document consulted | *Technical Assistance Guide for Administration of the HCBS CAHPS Survey* (CMS) |
| Administration mode as published | **Interviewer-administered only** — in person or by telephone |
| Core items | 69 |

**Currency check (2026-07-28).** AHRQ's HCBS survey page (content last reviewed January 2025) points to Medicaid.gov for the instrument and lists no successor version. The CAHPS Database accepts submissions for **"CAHPS Home and Community Based Services Survey 1.0"** and the 1.0-with-Employment-Module set only, and states that data from independently translated versions in other languages cannot be submitted. **Determination: 1.0 / 2017-01-19 is the current published version.** The uploaded PDFs match the canonical Medicaid.gov filenames referenced in the TA guide's Appendix B, so the chain from source to this file is clean.

> This currency check is **separate** from ROADMAP §5 item 4 (the SPA "Experience of Care" measure table, November 2017). Item 4 remains open and untouched by this session.

---

## 2 · What verbatim buys, and what it does not — ⚑ FLAG D, owner sign-off required

Framework §2.5 rule 2 states the rationale as: a tier B item used exactly as published "is comparable and attributable." **The first half of that does not survive contact with the source documentation, and the rule's rationale needs correcting even though the rule itself does not.**

Three findings, all from the source's own administration guidance:

1. **The instrument is validated only in its entirety.** The TA guide states that the survey has been validated for use in its entirety plus approved supplemental items, and **not in parts**, and that adding any question beyond the core survey and approved supplemental items removes the possibility of participating in the HCBS CAHPS Database. Our instrument is a subset plus a substantial tier A block. It is therefore outside validated use by construction.
2. **Trademark conditions confirm the same boundary from the other side.** The guide's condition for calling an instrument a CAHPS Survey is that the sponsor retains **all 69 core items** and does not modify or reorder questions or response options. We already decided not to use the name (D-CX-9); this simply confirms that the naming decision and the subsetting decision are the same decision.
3. **Mode.** The published instrument is interviewer-administered. D-CX-5 sets SMS/mail primary with phone fallback. Self-administration changes the measurement even when the words are identical — the vendor instructions are written for text read aloud, with emphasis, interviewer probing, and an `UNCLEAR RESPONSE` code that only an interviewer can assign. Identical wording in a different mode is not the same measurement.

**Proposed corrected rationale — for owner sign-off, not applied to the framework by Claude:**

> Verbatim use of a tier B item buys **attribution, format familiarity to the buyer, and freedom from the borrowed-paraphrase defect**. It does **not** buy comparability with published HCBS CAHPS results or database benchmarks, because the source is validated only in its entirety, because partial instruments cannot be submitted to the database, and because our mode differs from the published mode.

**Why this does not reverse D-CX-9.** The verbatim-or-nothing rule was never only about comparability; it is also the rule that stops us shipping lightly reworded CAHPS items, which is the genuinely bad outcome (no comparability *and* a paraphrase that reads as borrowed). The rule stands. What changes is what we may say about it — internally, and in the provenance appendix, and above all in front of a client. **A claim that our results are comparable to HCBS CAHPS benchmarks would now be a false claim** and belongs alongside the three prohibited claims in framework §0.1. ⚑ **Owner: add it as a fourth?**

**Second-order consequence, flagged not resolved:** if verbatim use does not buy comparability, the case for taking the tier B slot at `UNM-TRN` (ROADMAP §5 item 3) weakens materially, because comparability was the entire argument for it. See §5.5.

---

## 3 · Response scales — verbatim

Framework §2.1 flags the 0–10 anchor wording as the one thing not to reconstruct from memory. It is `SC-04` below. All scales are given as published; the trailing ellipsis, comma and question-mark placement are the source's own and are not normalised.

### 3.1 Missing-data codes — attached to every item

| Code | English | Spanish |
|---|---|---|
| -1 | `DON'T KNOW` | `NO SABE` |
| -2 | `REFUSED` | `SE NEGÓ A CONTESTAR` |
| -3 | `UNCLEAR RESPONSE` | `RESPUESTA POCO CLARA` |

The source defines `UNCLEAR` as the code for a response the interviewer cannot clarify even after minor probing. ⚑ **It has no meaning in a self-administered mode** — see §9 flag C.

### 3.2 `SC-01` — 4-point frequency (primary)

- **EN stem tail:** `Would you say . . .`
- **EN:** `1 Never,` · `2 Sometimes,` · `3 Usually, or` · `4 Always?`
- **ES stem tail:** `¿Diría que…?`
- **ES:** `1 Nunca,` · `2 A veces,` · `3 Casi siempre, o` · `4 Siempre?`

### 3.3 `SC-02` — alternate binary frequency (cognitive accommodation)

Reserved by the source for respondents who find `SC-01` cognitively challenging; administered as a **separate alternate version of the whole survey**, not as a per-item fallback.

- **EN:** `1 Mostly yes or` · `2 Mostly no?`
- **ES:** `1 En general, sí, o` · `2 En general, no?`

### 3.4 `SC-03` — Yes / No

- **EN:** `1 YES` · `2 NO` — with `3 DON'T NEED` where the item carries a need screen (Q50, Q52)
- **ES:** `1 SÍ` · `2 NO` — with `3 NO NECESITA`

### 3.5 `SC-04` — 0–10 global rating **(the anchor wording §2.1 flagged)**

Case-manager instance, from Q54, with the source's fills intact:

> **EN:** `Using any number from 0 to 10, where 0 is the worst help from {case manager} possible and 10 is the best help from {case manager} possible, what number would you use to rate the help you get from {case manager}?`
> Response: `__0 TO 10`

> **ES:** `¿Usando un número del 0 al 10, el 0 siendo la peor ayuda que recibe del {encargado de caso} posible y el 10 es la mejor ayuda que recibe del {encargado de caso} posible, ¿qué número usaría para calificar la ayuda que recibe del {encargado de caso}?`
> Response: `0 a 10`

**Determination on the anchor, and it matters.** The anchors are **not** a general "0 = worst possible, 10 = best possible" evaluation of the person. They are anchored on **"the worst / best help from {X} possible"**, and the question asks the respondent to rate **the help you get**, not the case manager. Framework §3 labels `RAT-B-01` "Global rating of the care manager (0–10)". **The verbatim item is a rating of the help received from the care manager.** ⚑ **Flag E:** the framework label must be corrected to match the item, because §9.2's dual-criterion decision turns on what the criterion actually measures — "rating of help received" and "rating of the person" are not the same construct, and the second is the one §2.2 spent three arguments keeping out of the product.

*(The ES rendering carries a doubled opening `¿` — one before `Usando` and one before `qué número`. This is in the published Spanish. It is reproduced, not corrected.)*

### 3.6 `SC-05` — alternate 5-point rating (accompanies `SC-04`)

- **EN:** `How would you rate the help you get from the {case manager}? Would you say . . .` → `1 Excellent,` · `2 Very good,` · `3 Good,` · `4 Fair, or` · `5 Poor?`
- **ES:** `¿Cómo calificaría la ayuda que recibe del {encargado de caso}? ¿Diría que es…?` → `1 Excelente,` · `2 Muy buena,` · `3 Buena,` · `4 Regular, o` · `5 Mala?`

### 3.7 `SC-06` — 4-point recommendation

- **EN:** `1 Definitely no,` · `2 Probably no,` · `3 Probably yes, or` · `4 Definitely yes?`
- **ES:** `1 Definitivamente no,` · `2 Probablemente no,` · `3 Probablemente sí, o` · `4 Definitivamente sí?`

### 3.8 `SC-07` — 4-point plan-content scale (Q56 only)

- **EN:** `1 None of the things that are important to you,` · `2 Some of the things that are important to you,` · `3 Most of the things that are important to you, or` · `4 All of the things that are important to you?`
- **ES:** `1 Ninguna de las cosas que son importantes para usted` · `2 Algunas de las cosas que son importantes para usted` · `3 La mayoría de las cosas que son importantes para usted` · `4 Todas las cosas que son importantes para usted`

*(In EN the options complete the stem sentence; in ES the stem is a standalone wh-question and the options are freestanding. This is a structural divergence in the published pair, not a transcription artefact. See §8.)*

### 3.9 Fills required from administrative data

The braces are **designated fills**, supplied by programme administrative data and overridden by the respondent's own term where they offer one. Filling them is specified use, not modification — the source's vendor instructions direct it explicitly, and the trademark condition prohibits modifying *questions and response options*, not populating fills.

| Fill | Set to |
|---|---|
| `{case manager}` / `{encargado de caso}` | Health Home programme term for the care manager, overridden by the member's own term |
| `{program-specific term for case manager services}` | Health Home term for care management |
| `{program-specific term for case-management services}` (Q55) / ES: `{término específico del encuestado para "servicios que presta un encargado de caso"}` | as above — ⚑ note the EN/ES divergence: EN says *program*-specific, ES says *respondent*-specific. Recorded, not reconciled. |
| `[program-specific term for "service plan"]` / `[término específico de cada programa que se refiere a un "plan de servicios"]` | Health Home plan-of-care term |

---

## 4 · Slot inventory and determination summary

| Slot | Framework § | Source item(s) | Determination |
|---|---|---|---|
| `RAT-B-01` | §3 | Q54 | **Transfers** |
| `RAT-B-02` | §3 | Q55 | **Transfers** |
| `CMH-B-01` | §4 | Q49 | **Transfers** |
| `CMH-B-02` | §4 | Q50 (screen) + Q51 | **Transfers in part** — screen carries HCBS content; base-rate risk |
| `CMH-B-03` | §4 | Q52 (screen) + Q53 | **Transfers in part** — screen contains non-fillable HCBS-specific text |
| `COM-B-01` | §5 | — | **Does not transfer — no source item exists** |
| `COM-B-02` | §5 | — | **Does not transfer — no source item exists** |
| `COM-B-03` | §5 | — | **Does not transfer — no source item exists** |
| `POC-B-01` | §7 | Q56 | **Transfers** |
| `POC-B-02` | §7 | Q58 | **Transfers** |
| `UNM-TRN` (conditional) | §8.2 | Q59 | **Transfers** — at a cost to module scale coherence; see §5.5 |
| *proposed* `CMH-B-00` | §4 | Q48 | **Recommended addition** — required as gate; owner decision |

**Count correction.** The session brief states "eleven fixed slots plus one conditional." The framework's own tables yield **ten fixed slots plus one conditional, eleven in total**. Minor, recorded because the slot count is quoted in the brief and will be quoted again.

**Result of the session:** 7 of 10 fixed slots fill from the source (2 of them only in part); 3 do not fill at all and convert to tier A; 1 conditional slot fills but with a documented methodological cost; 1 new slot is recommended.

---

## 5 · Slot entries

Every entry carries the six required fields: verbatim EN, verbatim response set, source location, verbatim ES, determination with ground, and the three codebook provenance fields.

### 5.1 Module RAT — global rating and recommendation

#### Section lead-in (required — the block is not administered without it)

- **EN section heading:** `YOUR CASE MANAGER`
- **EN lead-in:** `Now I would like to talk to you about your {case manager}, the person who helps make sure you have the services you need.`
- **ES section heading:** `Su encargado de caso`
- **ES lead-in:** `Ahora me gustaría hablarle de su {encargado de caso}, la persona que se asegura de que usted reciba los servicios que necesita.`

---

#### `RAT-B-01` — global rating of the help received from the care manager

- **Source location:** HCBS CAHPS 1.0, section *Your Case Manager*, **Q54**
- **Verbatim EN:** see `SC-04` §3.5 (the item *is* the scale stem)
- **Response set EN:** `__0 TO 10` · `-1 DON'T KNOW` · `-2 REFUSED` · `-3 UNCLEAR RESPONSE`; alternate version `SC-05`
- **Verbatim ES:** see `SC-04` §3.5
- **Response set ES:** `0 a 10` · `-1 NO SABE` · `-2 SE NEGÓ A CONTESTAR` · `-3 RESPUESTA POCO CLARA`; alternate version `SC-05`
- **Determination: transfers.** The item is anchored on the case manager, who is the Health Home care manager's direct structural counterpart, and the fills carry the programme's own term. Nothing in the wording presupposes paid in-home staff or personal-care tasks.
- **Carried caveat:** it measures the *help received*, not the person — see §3.5 flag E. This must be settled before §9.2 is signed off, because it is the proposed primary criterion.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q54)` · `concept_overlap_with_published_instrument: yes`

---

#### `RAT-B-02` — recommendation of the care manager

- **Source location:** Q55
- **Verbatim EN:** `Would you recommend the {case manager} who helps you to your family and friends if they needed {program-specific term for case-management services}? Would you say you would recommend the {case manager} . . .`
- **Response set EN:** `SC-06` + missing codes
- **Verbatim ES:** `¿Les recomendaría a sus familiares y amigos el {encargado de caso} que le ayuda a usted si ellos necesitaran {término específico del encuestado para "servicios que presta un encargado de caso"}? ¿Diría que les recomendaría el {encargado de caso}?`
- **Response set ES:** `SC-06` + missing codes
- **Determination: transfers.** Two fills, both settable from Health Home administrative data.
- **Note:** the conditional clause ("if they needed …") presupposes that care management is a service a friend could plausibly need. In a Health Home context that is true but the eligibility route is narrower than in HCBS; the item may read oddly to some members. Not a transferability failure — a cognitive-testing item. Recorded for the pretest protocol.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q55)` · `concept_overlap_with_published_instrument: yes`

---

### 5.2 Module CMH — care manager support ("Case manager is helpful")

**Composite composition — how it was derived, and a gap.** The TA guide names the eight core measure areas, including *Case manager is helpful*, but **neither uploaded source maps item numbers to measures or defines the top box per measure**. The mapping below is derived from the instrument's own section structure (the items sitting under *Your Case Manager*, excluding the gate, the two need screens, and the two rating items which belong to *Ratings of providers*). ⚑ **Flag G, new open item:** the authoritative measure specification — item composition and top-box definitions — is a document we do not hold. Framework §2.1's reporting rule ("the two most positive where the source measure defines it that way") cannot be applied to a tier B measure until we do. Obtain it before the codebook session.

---

#### `CMH-B-00` *(proposed — not in framework v0.2)* — knowledge of the care manager

- **Source location:** Q48
- **Verbatim EN:** `Do you know who your {case manager} is?`
- **Response set EN:** `1 YES` · `2 NO → GO TO Q56` · missing codes all `→ GO TO Q56`
- **Verbatim ES:** `¿Sabe quién es su {encargado de caso}?`
- **Response set ES:** `1 SÍ` · `2 NO → GO TO Q56` · missing codes all `→ GO TO Q56`
- **Determination: transfers — and is structurally required.** Q48 is the gate for the entire case-manager block: `RAT-B-01`, `RAT-B-02` and `CMH-B-01…03` are all administered behind it. Taking those five slots without their gate changes their denominators, which is the one modification the framework's own logic cannot tolerate.
- **It is also substantively worth having.** "Does the member know who their care manager is" is a first-order Health Home finding, actionable at agency level, and the LHH will read a low rate as an assignment or onboarding failure rather than a service-quality one.
- ⚑ **Owner decision:** adding a slot is a framework change (§4 table), not Claude's to make. Recommended: adopt as `CMH-B-00`, reported as a standalone rate, excluded from the composite.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q48)` · `concept_overlap_with_published_instrument: yes`

---

#### `CMH-B-01` — reachability

- **Source location:** Q49
- **Verbatim EN:** `In the last 3 months, could you contact this {case manager} when you needed to?`
- **Response set EN:** `SC-03` (`1 YES` · `2 NO`) + missing codes
- **Verbatim ES:** `En los últimos 3 meses, ¿Pudo comunicarse con este {encargado de caso} cuando necesitó hacerlo?`
- **Response set ES:** `SC-03` (`1 SÍ` · `2 NO`) + missing codes
- **Determination: transfers.** No HCBS-specific presupposition.
- ⚑ **Overlap to resolve at questionnaire drafting:** framework §6 `ACC-01` ("the member can reach the care manager when they need to", tier A, frequency) is the same construct on a different scale. Fielding both is redundant and will read as a repeat to a member on the phone. **One of them goes.** Recommended: keep `CMH-B-01` verbatim inside the composite and drop `ACC-01`, or keep both only if `ACC-01` is respecified to measure something `CMH-B-01` does not (e.g. time-to-response, which `ACC-02` already covers). Owner decision at drafting, flagged now so it is not discovered late.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q49)` · `concept_overlap_with_published_instrument: yes`

---

#### `CMH-B-02` — worked with the member on equipment

- **Source location:** Q51, screened by Q50
- **Verbatim EN — screen (Q50):** `Some people need to get equipment to help them, like wheelchairs or walkers, and other people need their equipment replaced or fixed. In the last 3 months, did you ask this {case manager} for help with getting or fixing equipment?`
  **Response set:** `1 YES` · `2 NO → GO TO Q52` · `3 DON'T NEED → GO TO Q52` · missing codes all `→ GO TO Q52`
- **Verbatim EN — item (Q51):** `In the last 3 months, did this {case manager} work with you when you asked for help with getting or fixing equipment?`
  **Response set:** `SC-03` + missing codes
- **Verbatim ES — screen (Q50):** `Algunas personas necesitan conseguir equipo, como sillas de ruedas o andadores, que les sirvan de ayuda y otras personas necesitan que el equipo que tienen sea remplazado o reparado. En los últimos 3 meses, ¿le pidió ayuda a este {encargado de caso} para conseguir o reparar un equipo?`
  **Response set:** `1 SÍ` · `2 NO → GO TO Q52` · `3 NO NECESITA→ GO TO Q52` · missing codes all `→ GO TO Q52`
- **Verbatim ES — item (Q51):** `En los últimos 3 meses, ¿Este {encargado de caso} colaboró con usted cuando le pidió ayuda para conseguir o reparar un equipo?`
- **Determination: transfers in part.** The item text transfers cleanly. Two problems sit with the pair:
  1. **Content fit.** Durable medical equipment is within a Health Home care manager's remit for some members, but it is an HCBS-shaped exemplar (wheelchairs, walkers) and will be a "don't need" for a large share of a Health Home roster — a population defined by chronic-condition eligibility, not by disability-related LTSS need.
  2. **Base rate and suppression.** The item is reported on the screened denominator only. At the planning target of ~100 completes per agency, a screen-in rate of even 15–20% puts the agency-level cell at 15–20, and any subgroup crossing trips the N ≥ 10 rule in framework §2.2 immediately. **This item will frequently be unreportable at agency level.**
- ⚑ **Owner decision:** carry the pair verbatim (composite integrity, likely suppressed at agency level, reportable at network level), or drop `CMH-B-02` and let the composite run on two items. Dropping it changes the composite and forfeits the *Case manager is helpful* label — which, per §2, we could not claim comparability for anyway.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q50, Q51)` · `concept_overlap_with_published_instrument: yes`

---

#### `CMH-B-03` — worked with the member on service changes

- **Source location:** Q53, screened by Q52
- **Verbatim EN — screen (Q52):** `In the last 3 months, did you ask this {case manager} for help in getting any changes to your services, such as more help from {personal assistance/behavioral health staff and/or homemakers if applicable}, or for help with getting places or finding a job?`
  **Response set:** `1 YES` · `2 NO → GO TO 54` · `3 DON'T NEED → GO TO Q54` · missing codes all `→ GO TO Q54`
- **Verbatim EN — item (Q53):** `In the last 3 months, did this {case manager} work with you when you asked for help with getting other changes to your services?`
  **Response set:** `SC-03` + missing codes
- **Verbatim ES — screen (Q52):** `En los últimos 3 meses, ¿le pidió ayuda a este {encargado de caso} para hacer cambios en los servicios que recibe, como más ayuda de {el personal de salud mental/los auxiliares de cuidados personales y/o los ayudantes de oficios domésticos}, o para ir a lugares o buscar trabajo?`
- **Verbatim ES — item (Q53):** `En los últimos 3 meses, ¿este {encargado de caso} colaboró con usted cuando le pidió ayuda para hacer otros cambios en los servicios que recibe?`
- **Determination: transfers in part — and the fault is in the screen, not the item.** Q53 is population-neutral and transfers. Q52 does not, and this is the case where §2.5 rule 3 bites hardest:
  - The fill `{personal assistance/behavioral health staff and/or homemakers if applicable}` is a **designated fill** and can be set to Health Home service terms. Legitimate.
  - The clause **"or for help with getting places or finding a job" is not a fill.** It is fixed published text, and it names two HCBS service categories (medical transportation, employment supports) that are not Health Home care-management services. Under verbatim-or-nothing we may not delete it.
- ⚑ **Owner decision, three options, none free:**
  - **(a)** Field Q52 verbatim including the job clause. Preserves the published screen; reads as a non-sequitur to a Health Home member and risks confusing the screen-in decision, which corrupts Q53's denominator anyway.
  - **(b)** Replace the screen with an original tier A screen and keep Q53 verbatim. Clean administration; Q53's denominator no longer matches the published item, so what remains of the tier B claim is wording only.
  - **(c)** Drop the pair; write `CMH-B-03` as a tier A item.
  **Recommended: (b)**, on the ground that §2 already establishes we are not buying comparability — so a screen that a member can answer correctly is worth more than a screen that matches a benchmark we cannot use. Flagged, not applied.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q53); screen per owner decision` · `concept_overlap_with_published_instrument: yes`

---

### 5.3 Module COM — the determination this session was called to make

**`COM-B-01`, `COM-B-02`, `COM-B-03` cannot be filled. There is no care-manager-referenced item in the source composite.**

Framework §5 specifies "'Staff listen and communicate well' composite items, **care-manager-referenced subset only**", with the flag that the rest are dropped, not rewritten. The item-by-item check produces a result the framework anticipated in form but not in size: **the care-manager-referenced subset is empty.**

The source's communication items and their referents:

| Source item | Referent | Transfers? |
|---|---|---|
| Q28 — treated you with courtesy and respect | `{personal assistance/behavioral health staff}` | No |
| Q29 — explanations hard to understand because of accent | `{personal assistance/behavioral health staff}` | No |
| Q30 — treated you the way you wanted them to | `{personal assistance/behavioral health staff}` | No |
| Q31 — explained things in a way that was easy to understand | `{personal assistance/behavioral health staff}` | No |
| Q32 — listened carefully to you | `{personal assistance/behavioral health staff}` | No |
| Q33 — knew what kind of help you needed with everyday activities | `{personal assistance/behavioral health staff}` | No |
| Q34 — encouraged you to do things for yourself | `{personal assistance/behavioral health staff}` | No |
| Q41–Q45 — the same battery | `{homemakers}` | No |

The *Your Case Manager* section (Q48–Q55) contains a gate, two need-screened service items, one reachability item, and the two ratings. **It contains no communication item at all.** The published instrument does not ask whether the case manager listens, explains, or treats the member with respect. That is a real gap in the source, not an artefact of our reading of it.

**The route we explicitly reject.** Q32 could be re-pointed at the care manager by substituting the fill. It must not be. The braces at Q28–Q34 are populated from Q5/Q7/Q9 — the titles the member gives for **paid in-home staff** — not from Q12, which collects the case-manager title. Substituting across that boundary changes the item's population, which is a rewording in the sense §2.5 rule 2 exists to prevent: it would yield an item that looks published, is not, and carries a borrowed phrasing we could not defend in a provenance appendix. **If the item has to be reframed to fit, that is the signal to stop, not the licence to proceed.**

**Determination, for owner sign-off:**

> `COM-B-01…03` are struck as tier B slots. Framework §5's tier B row is replaced by original **tier A** items under §2.5 rule 2, joining the existing `COM-01`. The dropped source items are recorded in §7 and named in the provenance appendix so that a reader sees a determination rather than an omission.

**Consequences.** Framework §5's table and flag both need rewriting at the next content revision. The module goes from 3 tier B + 1 tier A to 0 tier B + 4 tier A, so the *content* of communication measurement in this instrument is now entirely ours to specify — a drafting task for the questionnaire session, not this one. On the positive side, this removes the one place where our instrument would have carried the source's weakest design feature for our purposes: a communication battery about people who are not the person we are measuring.

---

### 5.4 Module POC — "Choosing the services that matter to you"

#### Section lead-in

- **EN section heading:** `CHOOSING YOUR SERVICES` · **ES:** `La elección de sus servicios`
- The source supplies no lead-in sentence for this section in either language.

---

#### `POC-B-01` — plan content

- **Source location:** Q56
- **Verbatim EN:** `In the last 3 months, did your [program-specific term for "service plan"] include . . .`
  **Response set:** `SC-07`; `-1 DON'T KNOW → GO TO Q58` · `-2 REFUSED → GO TO Q58` · `-3 UNCLEAR RESPONSE → GO TO Q58`
- **Verbatim ES:** `En los últimos 3 meses, ¿qué se incluyó en su [término específico de cada programa que se refiere a un "plan de servicios"]?`
  **Response set:** `SC-07`; missing codes all `→ GO TO Q58`
- **Determination: transfers.** The fill carries the Health Home plan-of-care term. The construct — whether the member's own priorities are in the plan — is the strongest QMP-facing content in the instrument (framework §7) and is population-neutral.
- **Note:** EN and ES differ structurally (sentence-completion vs wh-question, §3.8). Both are published; both are used as published. This is one of several places where the official Spanish is an *adaptation*, not a translation — see §8.
- ⚑ **Overlap:** framework §7 `POC-02` (tier A, "the member's own priorities are in the plan", frequency) is close to this item. Resolve at drafting; do not field both without a stated distinction.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q56)` · `concept_overlap_with_published_instrument: yes`

---

#### `POC-B-02` — route to changing the plan

- **Source location:** Q58
- **Verbatim EN:** `In the last 3 months, who would you have talked to if you wanted to change your [program-specific term for "service plan"]? Anyone else? [INTERVIEWER MARKS ALL THAT APPLY]`
  **Response set:** `1 CASE MANAGER` · `2 OTHER STAFF` · `3 FAMILY/FRIENDS` · `4 SOMEONE ELSE, PLEASE SPECIFY ___________________` + missing codes
- **Verbatim ES:** `En los últimos 3 meses, ¿con quién hubiera hablado si quisiera cambiar su [término específico de cada programa que se refiere a un "plan de servicios"]? ¿Hablaría con alguien más? [INTERVIEWER MARKS ALL THAT APPLY]`
  **Response set:** `1 ENCARGADO DE CASO` · `2 OTROS MIEMBROS DEL PERSONAL` · `3 FAMILIARES/ AMIGOS` · `4 ALGUIEN MÁS, ESPECIFIQUE` + missing codes
- **Determination: transfers**, with one mode caveat. The response options are population-neutral. But the item is an interviewer-coded multiple-response item with an unprompted "Anyone else?" probe — the probe is the item's design, and it does not exist in a self-administered form. In SMS/mail this becomes a check-all-that-apply grid, which is a different instrument. See flag C.
- `ip_tier: B` · `wording_source: HCBS CAHPS 1.0 verbatim (Q58)` · `concept_overlap_with_published_instrument: yes`

---

#### Q57 — dropped

- **Verbatim EN:** `In the last 3 months, did you feel {personal assistance/behavioral health staff} knew what's on your [program-specific term for "service plan"], including the things that are important to you?`
- **Determination: does not transfer.** Referenced to paid in-home staff. There is no Health Home counterpart within the item, and re-pointing it at the care manager would be the same substitution rejected in §5.3. Recorded in §7.

---

### 5.5 `UNM-TRN` — the conditional slot, now costed

- **Source location:** Q59, section *Transportation*
- **EN section heading:** `TRANSPORTATION` · **EN lead-in:** `The next questions ask about how you get to places in your community.`
- **ES section heading:** `Transporte` · **ES lead-in:** `El tema de las siguientes preguntas es cómo va usted a sitios de su comunidad.`
- **Verbatim EN:** `Medical appointments include seeing a doctor, a dentist, a therapist, or someone else who takes care of your health. In the last 3 months, how often did you have a way to get to your medical appointments? Would you say . . .`
  **Response set:** `SC-01` + missing codes; alternate version `SC-02`
- **Verbatim ES:** `Entre las citas médicas se incluye ir a ver al doctor, al dentista, al terapeuta o a otra persona que se encargue del cuidado de su salud. En los últimos 3 meses, ¿con qué frecuencia tuvo forma de llegar a sus citas médicas? ¿Diría que...?`
  **Response set:** `SC-01` + missing codes; alternate version `SC-02`
- **Determination: transfers.** The item presupposes nothing about who provides the transport. It is population-neutral and it is the one source item in the whole set that measures an unmet need directly.
- **The cost, which is what ROADMAP §5 item 3 was missing.** Framework §8.2 specifies the entire UNM module as **Yes/No, top-box = need met, with an explicit need screen**. Q59 is a **4-point frequency item with no need screen**. Taking the tier B slot therefore means:
  - one item in the UNM module sits on a different scale from `UNM-HOU`, `UNM-FOD`, `UNM-BEN`;
  - the module cannot be reported as a single unmet-need count or index without a stated recode, and a recode of a tier B item is exactly what §2.5 forbids;
  - "never / sometimes" is not the same statement as "the need was unmet", because a member with no medical appointments in the period still answers.
- **And the benefit has shrunk.** The argument for taking the slot was comparability. Per §2, we do not have comparability. What remains is format familiarity — real but small.
- ⚑ **Recommendation for the owner's decision (ROADMAP §5 item 3): take the tier A item.** `UNM-TRN` as an original Yes/No item with a need screen keeps the module coherent, keeps the top-box rule uniform, and gives up a comparability we cannot claim. **Do not field both** (framework §8.2). Flagged, not decided.
- `ip_tier: B if adopted` · `wording_source: HCBS CAHPS 1.0 verbatim (Q59) if adopted` · `concept_overlap_with_published_instrument: yes`

#### Q60, Q61, Q62 — dropped

The remaining transportation items ask whether the member used a van or other transportation service, whether they could get in and out of the ride easily, and how often the ride arrived on time. **Do not transfer:** all three presuppose a programme-provided or brokered transport benefit, which is not a Health Home care-management service. Recorded in §7.

---

## 6 · Composite-level determination: the staff-reliability composites

Framework §2.5 rule 3 states that the staff-reliability composites "largely do not transfer." **The item-by-item check upgrades "largely" to "entirely."** Recorded here explicitly so that it is not re-opened at each engagement.

| Source block | Items | Referent | Determination |
|---|---|---|---|
| *Getting needed services from personal assistant and behavioral health staff* | Q13–Q27 | paid in-home staff | Does not transfer |
| *How well personal assistant and behavioral health staff communicate with and treat you* | Q28–Q36 | paid in-home staff | Does not transfer (Q35, Q36 are the staff ratings, not the case-manager ratings) |
| *Getting needed services from homemakers* | Q37–Q40 | homemakers | Does not transfer |
| *How well homemakers communicate with and treat you* | Q41–Q47 | homemakers | Does not transfer |

**Ground, stated once:** every item in these blocks is anchored to a person who is paid to come into the member's home and perform personal-care, behavioural-health or household tasks. A Health Home care manager does none of these things. The items are not merely a poor fit — they describe a service the respondent does not receive from the entity we are measuring, and a member who does receive such services receives them from a different agency entirely, outside the LHH's scope.

**Consequence:** the reliability construct that matters in care management — does the care manager do what they said they would, and do they have to be told the situation again each time — has no tier B source. Framework §4 already answers this with `CMH-01` and `CMH-02` as tier A items. That decision is confirmed by this check rather than merely assumed.

---

## 7 · Dropped-items register

For the provenance appendix. Each entry shows a decision.

| Source item(s) | Content | Ground for dropping |
|---|---|---|
| Q1–Q3, CSQPASS | Cognitive screening | Screening apparatus for an interviewer-administered LTSS instrument; our frame and mode differ |
| Q4–Q12 | Service-type identification | Identifies HCBS service types not present in Health Home care management |
| Q13–Q27 | Getting needed services from paid in-home staff | Presupposes personal-care service receipt |
| Q28–Q36 | Staff communication and staff ratings | Referenced to paid in-home staff, not the care manager (§5.3) |
| Q37–Q47 | Homemaker service, communication, ratings | Presupposes homemaker service receipt |
| Q57 | Whether staff knew the service plan | Referenced to paid in-home staff (§5.4) |
| Q60–Q62 | Transport service, accessibility, punctuality | Presupposes a programme transport benefit (§5.5) |
| Q63–Q64 | Emergency contact; someone to talk to if hurt | **Owner decision, 2026-07-23:** physical-safety items excluded from every configuration (framework §8.4) |
| Q65–Q73 | Harm by staff: money/possessions, verbal, physical; resolution | **Owner decision, 2026-07-23:** excluded from every configuration. Disclosure protocol required regardless (framework §8.4.1) |
| Q74–Q81 | Community inclusion and empowerment | Out of scope for a care-management member-experience instrument at v1 |
| Q82–Q96 | Demographics, health status, household | Supplied by the roster (framework §9), not asked — buys back 4–6 items against the length budget |
| Q97–Q102 | Interviewer post-interview items | Mode-specific; our proxy-completion variable (framework §2.3) is specified independently |

---

## 8 · The Spanish determination — ⚑ FLAG A, owner sign-off

**Proposed rule:** for tier B slots the **official Spanish is used verbatim**; TRAPD applies to tier A items only; our reconciliation review still runs over the official Spanish as a documented quality check, never as a licence to amend it.

**Recommend adoption.** Three grounds, the third of which is new from this session:

1. **Symmetry with §2.5 rule 2.** A tier B item we translate ourselves is not the published item. Whatever verbatim use buys, it buys per language, and a TRAPD rendering forfeits it exactly the way a reworded English item does.
2. **The source's own process was equivalent to ours.** The TA guide describes the Spanish version as produced by two independent forward translators with a separate bilingual reviewer reconciling them against the English — the same architecture `survey-translation-adaptation` specifies. Re-running our own TRAPD over it would not improve it; it would only produce a different, unattributable string.
3. **The official Spanish is an adaptation, not a translation, and this is visible in the text.** Three instances found in this session's transcription: Q92 asks in English about a language other than **English** at home and in Spanish about a language other than **Spanish**; Q29/Q42 ask about staff speaking **English** in the EN version and **español** in the ES version; Q56 is a sentence-completion item in English and a wh-question in Spanish. These are deliberate localisation decisions embedded in the published instrument. **We could not reproduce them by translating, because they are not translations** — which settles the question: either take the official Spanish as published, or write the item ourselves in both languages as tier A.

**Consequence for §3.9 fills:** the ES fill instruction at Q55 says *respondent*-specific where EN says *program*-specific. Reproduced as published; the fill is set from the same administrative source in both languages, and the divergence is noted in the provenance appendix rather than harmonised.

**Related, and it is not a Spanish question:** the CAHPS Database accepts only the official English and Spanish versions and explicitly excludes independently translated languages. Framework §8.5 requires coverage to 95% of roster, which for a NYS Health Home roster means Chinese, Haitian Creole, Russian and others. **Those languages will be tier A throughout** — there is no official version to be verbatim about — so a bilingual instrument and a seven-language instrument are not the same instrument with respect to tier B. Recorded here; it will matter when §8.5's coverage figure is specified.

---

## 9 · Flags for owner sign-off

| # | Flag | Where |
|---|---|---|
| **A** | **Spanish = tier B question, not translation question.** Official Spanish verbatim for tier B slots; TRAPD for tier A only. **Recommend adopt.** | §8 |
| **B** | **Slots with no usable source text become tier A.** Materialised at COM — all three slots. **Requires sign-off; it changes framework §5.** | §5.3 |
| **C** | **The alternate scales and the mode.** The source's `SC-02`/`SC-05` alternates are an interviewer-administered accommodation delivered as a separate version of the whole survey; `UNCLEAR RESPONSE` and the "Anyone else?" probe have no self-administered meaning. Framework §2.1 does not mention any of this. Decide: carry the alternates in the phone version only, or exclude them and state it. Not decidable until the mode blocker clears. | §3.3, §3.1, §5.4 |
| **D** | **Corrected rationale for verbatim use** — attribution and format, not comparability; plus proposed fourth prohibited claim ("comparable to CAHPS benchmarks"). | §2 |
| **E** | **`RAT-B-01` is a rating of *help received*, not of the care manager.** Framework §3 label to be corrected; bears directly on the §9.2 criterion decision. | §3.5 |
| **F** | **Naming convention for reference-layer files.** | header |
| **G** | **The measure specification is a document we do not hold.** Item-to-composite mapping and per-measure top-box definitions are in neither uploaded source. Framework §2.1's top-box rule cannot be applied to tier B measures until obtained. **New open item.** | §5.2 |

**Additional finding for ROADMAP §5 item 6 (per-agency completes target), not a flag but a hard input.** The TA guide reports effective sample sizes from the field test ranging from **70 completes for the *Choosing the Services That Matter to You* composite to 376 for the *Case Manager Is Helpful* composite**, with **400 as the recommended target ESS**. Our planning figure is ~100 per agency. The composite the instrument is built around is the one requiring 376. This does not invalidate the design — at network level, ten agencies at 100 clears 400 comfortably — but it means **the `CMH` composite is not reliably reportable at agency level at the current planning target**, which is the level the LHH will want it at. It strengthens framework §2.2's reliability argument, and it turns item 6 from a budget question into a design question: what is reported at which level, and at what n. Recommend it is answered before the fieldwork budget is quoted.

---

## 10 · Consequences for other artefacts (proposed, not applied)

| Artefact | Change |
|---|---|
| `module-framework-cx.md` §5 | Tier B row struck; `COM-B-01…03` → tier A items; flag resolved |
| `module-framework-cx.md` §3 | `RAT-B-01` label corrected to "rating of the help received from the care manager" |
| `module-framework-cx.md` §4 | `CMH-B-00` added if flag adopted; `CMH-B-02`/`-03` screen decisions recorded |
| `module-framework-cx.md` §2.1 | Alternate scales addressed; top-box rule qualified pending flag G |
| `module-framework-cx.md` §2.5 | Rationale corrected per flag D |
| `module-framework-cx.md` §0.1 | Fourth prohibited claim, if adopted |
| `module-framework-cx.md` §8.2 | `UNM-TRN` recommendation recorded |
| `module-framework-cx.md` IP tier legend | Legend reads "paraphrase **or** verbatim use with attribution" — contradicts §2.5 rule 2 for this instrument. Correct at next revision |
| `module-framework-cx.md` header | Still names `skills/domain-cx-member-experience/…` — ROADMAP §5 item 10, unchanged |
| Codebook (future) | `ip_tier`, `wording_source`, `concept_overlap_with_published_instrument` populated from §5 of this file |
| Provenance appendix (future) | §7 register + §8 Spanish note + attribution to the HCBS CAHPS Survey, with no instrument name in the deliverable title |

---

## 11 · Change log

**v0.1 · 2026-07-28 —** Created. Source version-stamped and currency-checked. Seven response scales and four fills transcribed verbatim in both baseline languages. Eleven slots determined: seven fill (two in part), three struck to tier A, one conditional filled with a costed recommendation, one new slot proposed. Staff-reliability and staff-communication composites determined non-transferring at block level with the item-by-item evidence recorded. Dropped-items register built. Seven flags raised for owner sign-off; one hard input supplied to ROADMAP §5 item 6.

---

*Document owner: A. Akhtyrskii · Measure & Meaning Research · prepared with Claude · illustrative + synthetic where examples appear · source items reproduced verbatim from a publicly distributed CMS instrument, attributed in the provenance appendix, instrument name excluded from all deliverable titles.*
