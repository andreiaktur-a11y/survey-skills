# Member Experience Survey — Health Home care management

## Fielded questionnaire · v0.3 · documentation & freeze pass

**Repo target:** `skills/domain-healthcare-cma/references/questionnaire-cx-member-experience.md`
**Version:** 0.3 · 2026-08-05 · **Status:** ⏸ **FROZEN at v0.3** (CX session 7). Not fielded, not cognitively tested, not translated beyond the locked strings.
**Governed by:** `module-framework-cx.md` **v0.6** · **Locked strings sourced exclusively from** `tier-b-source-items.md` **v0.2**
**Configuration:** QMP evidence base (`D-CX-19`) · **Mode:** telephone interview, interviewer-administered (`D-CX-17`) · **Register:** mixed, biased to the standard (`D-CX-18`)
**Prepared with Claude · one task per session · principal-led · flag-first.**

> ⏸ **FREEZE NOTICE (`D-CX-26`, owner, 2026-08-05).** The CX domain is parked here while the Employee domain is finalised. **This file is the state to resume from.** Nothing below is abandoned: every unresolved question raised in the owner's second reading is written down as a numbered open item at §7 with its options and a recommendation, so the thaw session opens on a decision list rather than on a re-reading. **No open item was closed by assumption in order to tidy the freeze.**

> **All sample figures, thresholds, and organisation names in the Measure & Meaning library are illustrative + synthetic.** This file contains no data.

---

## 0 · How to read this file, and how to edit it

### 0.1 Two registers, never mixed

Every item is printed in exactly one of two forms.

```
[LOCKED · TIER B · VERBATIM — source Qnn — DO NOT EDIT]
```

```
[DRAFT · TIER A — editable]
```

**Why this matters more than it looks.** A locked item that reads awkwardly is exactly the kind of thing an editor improves. Improving it silently converts a tier B item into a lightly reworded CAHPS item — which `module-framework-cx.md` §2.5 identifies as the **worst** available outcome: no comparability *and* a paraphrase that reads as borrowed. The registers exist so that the edit pass cannot do that by accident.

**Locked means locked in both directions.** Not the wording, not the response options, not their order, not the punctuation, not the ellipses. The trailing `. . .` and the doubled Spanish `¿` are in the published source and are reproduced, not corrected.

### 0.2 What each editable item carries

| Field | What it is |
|---|---|
| **ID** | Stable across waves (§2.4). Revised wording gets a suffix (`CMH-01b`), never a new ID |
| **Construct** | What the item is for. **If an edit changes this, the edit is a framework change, not a wording change** |
| **Wording** | The first reading, delivered as drafted |
| **Clarification** | The single approved alternative phrasing (`O-CX-20`). Used only on the respondent's signal, never volunteered, never improvised |
| **Scale** | Response set and its provenance |
| **Routing** | Where the item sits in the skip logic |
| **Why worded this way** | The reasoning line. **Read this before editing the wording** |

**The reasoning line is the point of this format.** An edit pass without it produces wording changes that quietly change constructs — the item still reads well and no longer measures what the index needs.

### 0.3 What is not in this file, and why

| Absent | Reason |
|---|---|
| Introduction, consent and notice text | `O-CX-2` — stubs at §3, filled after counsel |
| Disclosure and escalation script (§8.4.1) | `O-CX-2` — stub at §3.4 |
| Spanish for tier A items | Deferred until the tier A wording survives cognitive testing — if v0.2 is followed by a v0.3, the translation waits again (session brief §3). TRAPD runs once, on settled text |
| Spanish for tier B items | **Present and locked.** That text is already final and cannot be edited anyway (`D-CX-12`) |
| Codebook | Needs `O-CX-6` (top-box definition for the 0–10 rating) |
| `GRV`, `RSP`, `COORD`, `LNG` modules | Not in the QMP configuration (§1 of the framework) |
| `SEF` module | **Withdrawn at v0.3** (`D-CX-24`). The dual criterion is declined; the three drafted items are held in the withdrawn annex at §9, not deleted, and their IDs are retired |
| *About you* — member characteristics | **Declared as Section I at v0.3, text absent** (`D-CX-25`). Tier B: verbatim or nothing, and the verbatim strings are not yet extracted into `tier-b-source-items.md`. A paraphrase here would be the exact defect §0.1 exists to prevent |
| *Interviewer questions* — post-interview observations | **Declared as Section J at v0.3, text absent** (`D-CX-25`). Same reason, plus an overlap with the fielding metadata we already record at §5.5 that has to be resolved before either is drafted (`O-CX-27`) |

---

## 1 · Item count against the budget

### 1.1 The arithmetic — counting units changed in this pass

The `UNM` rebuild (`D-CX-21`) replaces four fixed screen/item pairs with an **11-entry need checklist plus one follow-up item administered per flagged need**, so a single closed-item count no longer describes the interview. Three figures replace it.

| | Count |
|---|---|
| Closed bank items outside `UNM` — A 4 · CMH 3 · COM 4 · ACC 2 · POC 3 · `RAT-01` 1 · ENG 2 | 19 |
| `UNM` follow-up administrations, planning expectation (2–4 needs flagged) | +3 |
| **Administered closed items, expected case** | **≈22** |
| Administered closed items, theoretical maximum (all 11 needs flagged) | 30 |
| v0.2, for comparison | ≈25 |
| v0.1 fielded configuration, for comparison | 29 |

**Against the `D-CX-19` ceiling of 26: the expected case is now ≈22, four under it, and even the theoretical maximum sits at 30.** The maximum case exceeds the ceiling only for members with many flagged needs — who are exactly the members this instrument exists to hear from, and whose extra minutes buy the module's core content rather than overhead.

⚑ **The headroom is not spare capacity — it is the budget Section I is going to consume.** A standard *about you* block runs to roughly a dozen items. Four items of headroom against a dozen items of demand is the whole substance of `O-CX-27`: the question is not whether the block is worth having, it is which of its items are asked of the member and which are taken from the LHH file the BAA already covers. **Do not read ≈22 as room to add freely.**

**Cut in this pass (owner's edit pass):** `ACC-04` and its screen (−2, content absorbed by `UNM-MED`) · `POC-01` (−1, closes `O-CX-22`) · `ENG-03` (−1, conditional path only) · `OPN-02` (open item, no closed-count effect).

### 1.2 What the interviewer actually asks

Item count is not question count, and on a telephone instrument question count is what costs money.

| | Count |
|---|---|
| Closed bank items | 19 |
| Need screens (`CMH-03s` + 11 `UNM` checklist entries) | 12 |
| `UNM` follow-up (`SC-10`), maximum administrations | 11 |
| Open-ended (`UNM-OTH`, `OPN-01`) | 2 |
| **Maximum-path administered questions** | **44** |
| Expected path — CM known, 3 needs flagged, expects to stay | ≈35 |
| **Minimum path** — no CM known, no needs flagged, expects to stay | **19** |
| Sections I and J | **not counted — declared, undrafted** (`D-CX-25`) |

Checklist entries are not full questions: **~8–10 seconds each** against ~20–25 for a standard item, because the stem is read once as a battery lead-in and each entry is a short phrase plus a Yes/No. Time-weighted, the expected path runs at roughly **29 standard-question equivalents — shorter than both v0.1's and v0.2's realistic path** — while the maximum path is longer precisely in the interviews with the most to report. The minimum path is 19 rather than v0.1's 17 because the checklist is unconditional: a member with no needs still hears all 11 entries, and that is by design — need prevalence is a denominator, not an assumption.

### 1.3 Time

Nominal **12 minutes**, planned against roughly **14 achieved** at v0.3 (`D-CX-19`); an interview where many needs flag can run to ~15, and that overage is accepted for the reason above. ⚑ **These figures do not include Sections I and J,** which are declared but undrafted; a dozen *about you* items at telephone pace is roughly **3–4 minutes**, which would put the expected interview back at or above v0.2's ~15. The time budget is therefore **not** freed by the `SEF` withdrawal — it is pre-committed, and `O-CX-27` is where it gets spent or saved. `D-CX-18`'s scripted clarification adds time wherever it fires and the clarification rate is not knowable before cognitive testing.

⚑ **If cognitive testing puts the achieved figure past 15 minutes for the typical member, the next cut is a module, not an item — and it is `COM`**, four tier A items whose content is entirely ours to re-scope. Recorded here and in framework §1 so the decision is not taken under field pressure.

### 1.4 The cut register, with what each cut costs

| Cut | Decision | Ground | Reversal cost |
|---|---|---|---|
| `ACC-01` | `O-CX-8`, ⚑ owner sign-off — stood through the edit pass without objection | Reporting is top-box, and the CMH composite is the mean of item-level top-box rates — so a 4-point item and a binary both reduce to a proportion before anything is computed. `CMH-B-01` measures the same construct, is verbatim, and sits behind the published gate | 1 item |
| `POC-02` | `O-CX-9`, ⚑ owner sign-off — stood through the edit pass without objection | The coverage/process distinction against `POC-B-01` will not survive the telephone: two adjacent items about whether the member's priorities are in the plan read as the same question twice | 1 item. `POC-03` carries the process side |
| `UNM-OTH` reclassified | `D-CX-19` | It was already an open follow-up in the framework; counting it as a closed item was an arithmetic error | none — it is still asked |
| `ACC-04` + `ACC-04s` | Owner's edit pass → `D-CX-21` | A member who arranged the appointment without asking for help had nowhere clean to land, and *help getting an appointment* is a need like the others. Content moves to the `UNM` checklist as `UNM-MED`, where the uptake stage separates never-raised from raised-and-failed | 2 questions. `UNM-MED` covers the content at checklist cost |
| `POC-01` | Owner, closes `O-CX-22` | `POC-B-01`'s `DON'T KNOW` rate carries plan knowledge, verbatim and at zero cost. The counter-argument (a `DK` and an explicit *no* are different admissions) was put and declined | 1 item |
| `ENG-03` | Owner's edit pass → `D-CX-23` | Never part of the `EXIT_TYPE` derivation rule. Cost: the *leaving into support* vs *leaving into nothing* distinction is now carried more coarsely by the `IND`/`FAM`/`ORG` reason codes | 1 conditional item |
| `OPN-02` | Owner's edit pass → `D-CX-23` | Section H runs on `OPN-01` alone; the improvement question does the decision work, the retention question was texture | 1 open item |
| `SEF-01`, `SEF-02`, `SEF-03` | Owner, 2026-08-05 → **`D-CX-24`**, closing `O-CX-1` | The dual criterion is declined. Cost, stated in full at §9 and in framework §9.2: the instrument now has **one** criterion, the divergence exhibit is withdrawn rather than reconstructed from a substitute, and `EXIT_TYPE`'s *Constrained continuing* type loses one of its two defining conditions (`O-CX-25`) | 3 items. Wording preserved verbatim in the withdrawn annex at §9; IDs retired and never re-issued (§5.3) |

---

## 2 · Administration — the interviewer layer is part of the instrument

In a telephone instrument the interviewer instructions **are** the instrument. Nothing below is a wrapper.

### 2.1 The register rule (`D-CX-18`)

| | **Tier B — the six locked items** | **Tier A — everything else** |
|---|---|---|
| First reading | Exactly as printed | Exactly as printed |
| Member does not understand | One **verbatim re-read** → then the source's own probing rules → then `UNCLEAR` | Read the item's **scripted clarification**, once |
| Interviewer may rephrase | **Never** | **Never** — clarification comes from this file, not from judgment |
| If still unresolved | `UNCLEAR` | `UNCLEAR` |

**Clarification use is logged per item.** The resulting per-item clarification rate is free comprehension diagnostics and the wave-2 rewrite signal. It is **reported, never adjusted for**: its correlation with respondent characteristics is a finding, not a nuisance parameter (framework §2.3).

**Register changes fall between blocks, never between items.** Section A runs four locked items contiguously; sections B, C, D, F, G, H are tier A throughout; section E has one register change, between E2 and E3.

### 2.2 Missing-data codes — attached to every item, tier A and tier B alike

| Code | English | Spanish |
|---|---|---|
| `-1` | DON'T KNOW | NO SABE |
| `-2` | REFUSED | SE NEGÓ A CONTESTAR |
| `-3` | UNCLEAR RESPONSE | RESPUESTA POCO CLARA |

`-3` is the code for a response the interviewer cannot clarify even after the permitted probing. **Adopted on every item, including tier A** (`O-CX-7`, framework §2.1): it is a missing-data code and not item wording, so adopting it on a tier A item is a fielding convention rather than borrowed phrasing. It is also what makes the clarification log interpretable — *clarification fired and the answer resolved* and *clarification fired and the answer did not resolve* are different findings, and without `-3` they collapse into one.

### 2.3 Response formats

| Ref | Format | Provenance |
|---|---|---|
| `SC-01` | `1 Never,` · `2 Sometimes,` · `3 Usually, or` · `4 Always?` · stem tail Would you say . . . | Source scale, adopted as the standing frequency convention (`D-CX-3`, framework §2.1) |
| `SC-03` | `1 YES` · `2 NO` | Source scale, adopted as the standing Yes/No convention |
| `SC-04` | 0–10, anchors **inside the locked item text at A3** | Locked. Never reconstructed |
| `SC-06` | `1 Definitely no,` · `2 Probably no,` · `3 Probably yes, or` · `4 Definitely yes?` | Source scale, adopted as the standing 4-point recommendation convention |
| `SC-07` | `1 None of the things that are important to you,` · `2 Some of the things that are important to you,` · `3 Most of the things that are important to you, or` · `4 All of the things that are important to you?` | Locked to `POC-B-01` only |
| `SC-08` | `1 Not at all confident,` · `2 A little confident,` · `3 Somewhat confident, or` · `4 Very confident?` | Original — registered in framework §2.1 at v0.5; top-box = `4 Very confident`. ⚑ **No item uses this format at v0.3** — `SEF` was its only consumer (`D-CX-24`). **Kept in the register, not deleted:** a registered format costs nothing, and deleting it would mean re-deriving and re-justifying an identical scale if a confidence item ever returns |
| `SC-09` | Banded time categories, printed at **D1** | Original — registered in framework §2.1 at v0.5; top-box = `1 Same day`; option `6` is a screen-in-item, excluded from the denominator; option `5` is substantive, not missing |
| `SC-10` | `1 Yes — and I got the help I needed` · `2 Yes — we are still working on it` · `3 Yes — but I did not get the help I needed` · `4 No — we have not worked on that together` | **New in v0.2** (`D-CX-21`) — registered in framework §2.1 at v0.5; top-box = `1`; option `2` is a separate in-progress rate, **never counted as unmet**; option `4` is an uptake signal that includes needs the member resolved without the programme, **never attributed as care-manager failure** |

**`O-CX-23` closed in this session.** `SC-08`, `SC-09` and the new `SC-10` are registered in framework §2.1 at v0.5, each with a stated top-box definition. The codebook session is unblocked on formats.

**On adopting source response formats for tier A items.** Applying `SC-01`, `SC-03` or `SC-06` to an item we wrote is **format reuse, not borrowed wording**: `D-CX-3` adopts these as the instrument's standing conventions precisely so the member is not asked to switch answer frames every few questions. The codebook's `wording_source` field records item wording; response format is governed separately (framework §2.1). A tier A item on a source-conventional scale is `wording_source: original`.

**Recall period.** Every retrospective item uses **the last 3 months**, matching the locked items. This is a design parameter, not borrowed wording, and it is uniform deliberately: a tier A item on a different recall window sitting next to a locked item on a 3-month window is a measurement defect that would show up as noise and be blamed on the members.

### 2.4 Fills — set from administrative data before fielding

| Fill | Set to | Appears in |
|---|---|---|
| `{case manager}` / `{encargado de caso}` | The Health Home programme's own term for the care manager, **overridden by the member's own term** where they offer one | Locked items — set exactly as the source directs |
| `{care manager}` | The same term, in tier A items | Tier A items |
| `{program-specific term for case-management services}` | The Health Home term for care management | A4 |
| `[program-specific term for "service plan"]` | The Health Home plan-of-care term | E1, E2 |
| `{service plan}` | The same term, in tier A items | E3 |
| `{agency name}` | The care management agency's own name, as members know it — from the LHH roster | `RAT-01`, `ENG-01`, `ENG-02` (`D-CX-22`). Members recognise the agency's name; many do not recognise *Health Home*, which is why the v0.1 fill `{Health Home programme}` is retired |
| `{need domain}` | The flagged checklist domain, in the member's-ear phrasing of the F0 read-aloud column | `UNM-*-W` (F1) |
| `{care manager name}` | ⚑ **PROPOSED, not adopted — `O-CX-26`.** The individual care manager's name, from the LHH roster. **Not a fill in any printed item at v0.3.** If adopted it is used by the interviewer under the sequence rule at §2.6, never inserted into a locked stem | §2.6 only |

⚑ **The EN/ES fill divergence at A4 is reproduced, not reconciled.** The English fill reads *program*-specific and the Spanish reads *respondent*-specific. Both are published. Recorded in `tier-b-source-items.md` §3.9.

⚑ **Two fill families, one term.** Locked items use the source's brace names; tier A items use `{care manager}`. They resolve to the same string. Kept visually distinct so that a fill map written against this file cannot silently alter a locked item's brace.

### 2.5 Excluded by decision — stated so a reader sees a decision, not an omission

| Excluded | Decision |
|---|---|
| The cognitive-accommodation **alternate version** of the survey (binary frequency, 5-point rating) | `O-CX-7`, framework §2.1. The source specifies it as a separate alternate version of the *whole* survey; ours is majority tier A, so it would have to be constructed, tested and translated as a second instrument. **The accommodation route in v0.1 is proxy and assisted completion**, recorded as a variable and reported as a rate |
| Physical-safety items | Owner, 2026-07-23. Excluded from every configuration. The §8.4.1 disclosure protocol is required regardless — removing the item does not remove the event |
| Automated conversational voice | `O-CX-16`, confirmed. §8.4.1 requires a protocol an automated agent cannot execute, and independent human administration is what the product sells |
| Care-manager-level output | `D-CX-6`. Stated to the member in §3, and in the report, and in the contract |

### 2.6 Making the member know who we mean — ⚑ **PROPOSED PROTOCOL, `O-CX-26`, not adopted**

**The problem, as put by the owner.** A member may not recognise *care manager*, may not recognise the agency as an organisation, and may not connect either to the person who actually rings them. In this population that is not inattention — it is the ordinary consequence of the conditions the programme enrols for. An instrument that asks about an entity the member cannot place returns affect and noise, and the noise gets attributed to the member.

**The source anticipates this and is worth quoting, because it settles the IP half of the question.** The administration guidance directs that programme-specific staff terms be inserted, that the interviewer be allowed to adopt the respondent's own word for the role, and that the state supply **agency names, staff titles, and staff names** for that purpose. **Populating a designated fill is specified use, not modification** (framework §2.5, `tier-b-source-items.md` §3.9). So identifying the person by name is not an IP problem. It is a measurement problem and a PHI problem, and those are the two that need deciding.

**The measurement problem, and why it is sharp.** **A1 is the gate, and its whole finding is whether the member knows who their care manager is** (`D-CX-15`: an LHH reads a low rate as an assignment or onboarding failure). **Saying the name before A1 destroys the item** — it converts *do you know who your care manager is* into *do you recognise this name I have just told you*, which is a different and much weaker measure, and it does so silently.

**Proposed sequence rule — the shape that solves the owner's problem without spending A1.**

1. **Before A1** the interviewer identifies **the agency by name and the role by description** — the organisation and *the person there who helps you arrange your care and services* — and no individual name is used.
2. **A1 is asked exactly as printed** and its answer is recorded before anything else happens.
3. **On `YES`,** the interviewer adopts the member's own word for the role for the rest of the interview, as the source's rule already directs.
4. **On `NO` — and only after the `NO` is recorded —** the interviewer may offer the name once as a recognition prompt. **Any recognition is recorded as a separate variable (`CM_NAME_RECOG`) and never overwrites A1.** This is the part that recovers what the owner is worried about losing: the member who knows Maria but not *my care manager* becomes visible in the data instead of vanishing behind a skip, and the LHH gets both numbers — *knows the role* and *knows the person* — which are different operational failures with different fixes.
5. If step 4 produces recognition, **the routing still follows A1**, because the 13 items behind the gate ask about a 3-month relationship, not about name recall. ⚑ This is the costly half of the rule and it is stated plainly rather than buried: a member who recognises the name still skips the block. Whether that is right is part of `O-CX-26`.

**The PHI problem, and it reaches outside this file.** Adding *care manager name* and *care manager title* per member expands the sample file beyond the minimum-necessary field list that `D-CX-17` narrowed to **telephone number plus mailing address** — and that narrowed list is precisely what framework §10.3 says is being put to counsel under `O-CX-2`. **So `O-CX-26` is not independent of `O-CX-2`: it changes the package counsel is asked to approve.** Deciding the protocol before the counsel package is assembled saves a second review; deciding it after means re-opening one. Recorded here so the sequencing is a choice and not an accident.

---

## 3 · Member-facing text — STUBS, pending `O-CX-2`

⚑ **Nothing in this section is drafted.** Framework §10.3 requires counsel review before member-facing text is written. `D-CX-17` sets the mode independently of the PHI route, so **item wording proceeds and this section waits** — that reading of the constraint is itself flagged for the owner at `O-CX-2`.

> **Where `O-CX-2` physically lives, since it was asked for (session 7).** The constraint itself is one line in `module-framework-cx.md` §10.3: *counsel review required before any instrument text is written*. The open item restating it sits twice in the framework — in the §13.1 open table and beside §10.3 — and once in `ROADMAP.md` §4. **There is no separate counsel document and no draft text anywhere; §3.1–§3.5 below are the whole of it, and they are five headings with requirements and no prose.** That is the reason it is hard to find: there is nothing to find yet. The decision needed is a single sentence — *does §10.3's constraint bind the item bank, or only the introduction, consent, disclosure and close language?* v0.1, v0.2 and v0.3 are all built on **only the latter**.

### 3.1 `[STUB — AWAITS O-CX-2]` Advance contact
Letter and/or text preceding the call. Must carry: who is asking; that this is not the agency; how the number was obtained; how to opt out.

### 3.2 `[STUB — AWAITS O-CX-2]` Interview introduction and notice
Must carry, before the first item: who is asking · that the {care manager} will not see individual answers · that results are reported in group form only, and **never at care-manager level** · that participation does not affect services or eligibility · expected length · that the member may stop at any point or skip any question.

### 3.3 `[STUB — AWAITS O-CX-2]` Proxy and assisted completion
Consent and recording rules where a family member or caregiver assists. Assistance is common in this population and **is not a defect** — it is recorded as a variable and reported as a rate (framework §2.3).

### 3.4 `[STUB — AWAITS O-CX-2]` Disclosure and escalation protocol (§8.4.1)
What the interviewer says on a spontaneous disclosure of harm, neglect or acute risk; to whom at the LHH it goes; within what window; what the member is told will happen next. **Most likely to fire in section H or at F5.** Interviewers are briefed on it; it is never left to judgment in the moment. Whether M&M's interviewers fall within a mandatory-reporting obligation is the legal half of `O-CX-2`.

### 3.5 `[STUB — AWAITS O-CX-2]` Close

---

# THE INSTRUMENT

---

## Section A · Your care manager — the locked block

⚑ **This section is administered contiguously and in this order** (`D-CX-18`). Four locked items, no tier A item inserted between them, no register change inside the section.

**`O-CX-21` closed → `D-CX-20` (owner, session 6): the criterion stays at question 3.** The gate requirement and the contiguity rule put `RAT-B-01` here — earlier than the source places it (Q54) and earlier than driver-analysis convention — and the owner kept it: an unprimed criterion is not inflated by consistency motive, and asking eight content questions before a global rating is the classic route to an R² that reflects questionnaire order rather than experience. The cost (a member rates on general affect) is accepted and watched in the pretest.

---

### A1 · `CMH-B-00` — gate

```
[LOCKED · TIER B · VERBATIM — source Q48 — DO NOT EDIT]
```

**Section heading (EN):** `YOUR CASE MANAGER`
**Section lead-in (EN):** `Now I would like to talk to you about your {case manager}, the person who helps make sure you have the services you need.`

**Section heading (ES):** `Su encargado de caso`
**Section lead-in (ES):** `Ahora me gustaría hablarle de su {encargado de caso}, la persona que se asegura de que usted reciba los servicios que necesita.`

> **EN:** `Do you know who your {case manager} is?`
> **ES:** `¿Sabe quién es su {encargado de caso}?`

**Response set (EN):** `1 YES` · `2 NO → GO TO Q56` · `→ GO TO Q56`
**Response set (ES):** `1 SÍ` · `2 NO → GO TO Q56` · `→ GO TO Q56`

**Routing.** `YES` → **A2**. `NO` or any missing code → **skip to E1**, which is the source's own skip target (its `GO TO Q56` is our `POC-B-01`). In our instrument that skip clears **A2, A3, A4 and all of sections B, C and D** — 13 questions — because every one of them is care-manager-referenced and unanswerable by a member who does not know who their care manager is.

**Reported as a standalone rate; excluded from the CMH composite** (`D-CX-15`). An LHH reads a low rate as an assignment or onboarding failure, not a service-quality one.

**Interviewer:** the lead-in is **required**. The block is not administered without it.

⚑ **"What if the answer is not a clean yes or no?" — asked at the owner's second reading, and already answered by the routing line above, but stated explicitly because it was not obvious from the file.** `DON'T KNOW` (`-1`), `REFUSED` (`-2`) and `UNCLEAR` (`-3`) **route with `NO`** — to E1. This is deliberate and it is the conservative direction: a member who cannot say whether they have a care manager is not a member who can rate one, and routing them into 13 care-manager items would manufacture data. The three codes are **reported separately from a substantive `NO`**, because *I do not have one* and *I do not know* are different findings for an LHH looking at onboarding.

⚑ **`O-CX-28` — the harder version of the same question, and it is genuinely open.** A member answers `YES` at A1 and it then emerges — at A2, or in section B — that there has been **no contact at all in 3 months**. The instrument has no back-out. **Recommendation: keep it that way, and do not add a contact screen.** Every item behind the gate is *in the last 3 months, how often …*, and `Never` is a substantive answer, not a missing one. A member with a care manager they have not heard from in three months is **the single most important member on the roster for an LHH to see**, and a screen would move exactly that member behind a skip and out of the denominators. The cost of keeping it, stated: some `Never` responses will be *no relationship* rather than *bad relationship*, and the two are not separable in the data. `A2` is what carries the distinction — see the note there. Owner's call at thaw.

---

### A2 · `CMH-B-01` — reachability

```
[LOCKED · TIER B · VERBATIM — source Q49 — DO NOT EDIT]
```

> **EN:** `In the last 3 months, could you contact this {case manager} when you needed to?`
> **ES:** `En los últimos 3 meses, ¿Pudo comunicarse con este {encargado de caso} cuando necesitó hacerlo?`

**Response set:** `SC-03` — `1 YES` · `2 NO` / `1 SÍ` · `2 NO` — plus missing codes.
**Routing.** Asked of all who clear A1. → **A3**.

**In the CMH composite.** This is the composite's only verbatim item, which is why `O-CX-8` was resolved by cutting `ACC-01` rather than this (§1.4).

⚑ **`O-CX-29` — "and if I never needed to contact them?" Raised at the owner's second reading. It is a real defect in the item as it will be fielded, and it cannot be fixed by editing.** The item is a locked Yes/No: a member who simply had no occasion to make contact has **no true option**. Pushed for an answer they give `YES` (nothing stopped me) or `NO` (I did not get hold of anyone) more or less at random, and either way a non-event is scored as a service outcome — inside the CMH composite.

**What may not be done:** adding a fifth printed option, or rewording. That converts a tier B item into a lightly-edited CAHPS item, which §0.1 identifies as the worst available outcome.

**Two admissible routes, for the owner at thaw.**

- **(a) Leave it.** Non-substantive answers land in `-3 UNCLEAR` after the source's own probing. Costs nothing to build. **Cost:** `-3` stops being a comprehension diagnostic on this item and becomes a mixture of *did not understand* and *did not apply*, which contaminates the §2.2 clarification log precisely where it is being used to decide wave-2 rewrites.
- **(b) Add a non-substantive interviewer code `-7 DID NOT NEED TO MAKE CONTACT`, never read aloud, excluded from the CMH denominator and reported as a rate.** This is the same logic §2.2 already uses to attach `-1`/`-2`/`-3` to locked items: a missing-data code is a fielding convention, not item wording. **Cost, and it is the reason this is flagged rather than applied:** it changes a composite denominator, and denominator changes are the one modification this framework's own logic treats as load-bearing (§A1, and `tier-b-source-items.md` §5.2 on why the gate could not be dropped). It must be settled **before the codebook**, not after.

**Recommendation: (b), with the denominator rule written into the codebook in the same commit.** Reason: under (a) the defect is still there, it is simply invisible and mislabelled. Under (b) it is measured. **This is a recommendation, not an applied change — nothing in v0.3 implements it.**

---

### A3 · `RAT-B-01` — rating of the help received from the care manager · **PRIMARY CRITERION**

```
[LOCKED · TIER B · VERBATIM — source Q54 — DO NOT EDIT]
```

> **EN:** `Using any number from 0 to 10, where 0 is the worst help from {case manager} possible and 10 is the best help from {case manager} possible, what number would you use to rate the help you get from {case manager}?`
> Response: `__0 TO 10`

> **ES:** `¿Usando un número del 0 al 10, el 0 siendo la peor ayuda que recibe del {encargado de caso} posible y el 10 es la mejor ayuda que recibe del {encargado de caso} posible, ¿qué número usaría para calificar la ayuda que recibe del {encargado de caso}?`
> Response: `0 a 10`

Plus missing codes. **Routing:** → **A4**.

⚑ **This item rates the help received, not the person** (`D-CX-14`). The anchors run *the worst / best help from {case manager} possible*. That reading is what keeps the instrument consistent with §2.2's exclusion of care-manager-level reporting — and **it carries more weight at v0.3 than it did at v0.2**: with the dual criterion declined (`D-CX-24`), this is the **only** criterion in the driver model, so the *help, not the person* reading is now the single thing standing between the model and a staff-rating reading of it — an instrument that rated the *person* would be a performance-management instrument for individual staff, which this one refuses to be.

⚑ **The Spanish carries a doubled opening `¿`** — one before *Usando*, one before *qué número*. **This is in the published Spanish. It is reproduced, not corrected.**

⚑ **`O-CX-6` is still open and lands here.** The source's own top-box definition for the 0–10 rating is not stated in either source document, and framework §2.1 forbids supplying it from memory. Needed before the codebook session, not before fielding.

---

### A4 · `RAT-B-02` — recommendation

```
[LOCKED · TIER B · VERBATIM — source Q55 — DO NOT EDIT]
```

> **EN:** `Would you recommend the {case manager} who helps you to your family and friends if they needed {program-specific term for case-management services}? Would you say you would recommend the {case manager} . . .`
> **ES:** `¿Les recomendaría a sus familiares y amigos el {encargado de caso} que le ayuda a usted si ellos necesitaran {término específico del encuestado para "servicios que presta un encargado de caso"}? ¿Diría que les recomendaría el {encargado de caso}?`

**Response set:** `SC-06` — `1 Definitely no,` · `2 Probably no,` · `3 Probably yes, or` · `4 Definitely yes?` / `1 Definitivamente no,` · `2 Probablemente no,` · `3 Probablemente sí, o` · `4 Definitivamente sí?` — plus missing codes.
**Routing.** → **B0**.

⚑ **Cognitive-testing item, recorded for the pretest protocol.** The conditional clause *"if they needed …"* presupposes that care management is a service a friend could plausibly need. True in a Health Home context, but the eligibility route is narrower than in HCBS, and the item may read oddly to some members. **This is not a transferability failure and it is not a licence to edit** — it is a note about what to watch in the pretest.

---

## Section B · Care manager support — tier A

Register changes here, at the block boundary. `CMH-01`, `CMH-02` and `CMH-03` join `CMH-B-01` in the CMH composite, which is **ours, not the source's** — the *Case manager is helpful* label is not claimed and under `D-CX-10` could not be.

---

### B0 · `CMH-03s` — need screen for `CMH-03`

```
[DRAFT · TIER A — editable]
```

- **ID:** `CMH-03s` · **Construct:** whether a service change was asked for at all — the denominator for `CMH-03`
- **Wording:** *In the last 3 months, did you ask your {care manager} for help changing any of the services or supports you get?*
- **Clarification:** *I mean any change at all — more of something, less of something, something different, or something new.*
- **Scale:** `SC-03` Yes/No + missing codes
- **Routing:** `YES` → **B3**. `NO` or missing → **skip to B1**
- **Why worded this way:** This screen exists because the published screen (Q52) could not be used. Its clause *"or for help with getting places or finding a job"* is fixed published text, not a fill, and it names two HCBS service categories that are not Health Home care-management services — so under verbatim-or-nothing it could neither be deleted nor sensibly read to a Health Home member (`D-CX-11`, framework §4). **This screen names nothing.** It lets the member define what counts as a change, which is the only way to get a denominator a member can place themselves in correctly. The clarification enumerates directions of change rather than categories of service, for the same reason.

---

### B1 · `CMH-01` — follow-through

```
[DRAFT · TIER A — editable]
```

- **ID:** `CMH-01` · **Construct:** reliability of commitments — when the care manager says they will do something, it gets done
- **Wording:** *In the last 3 months, when your {care manager} said they would do something, how often did it get done?*
- **Clarification:** *I mean the things they agreed to take care of for you — how often did those things get finished?*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** all who clear A1 → **B2**
- **Why worded this way:** This and `CMH-02` are the two things members of care-managed programmes complain about that no source composite isolates. Frequency rather than Yes/No because partial reliability is the normal state and the LHH's lever sits in the middle of the distribution, not at the tails — a binary would put four fifths of the network in one cell. Anchored on **the promise**, not on satisfaction, which is what makes it actionable at supervisory level: an agency can audit whether commitments close, and cannot audit whether members feel good.

---

### B2 · `CMH-02` — continuity

```
[DRAFT · TIER A — editable]
```

- **ID:** `CMH-02` · **Construct:** the care manager knows the member's situation without it being re-explained
- **Wording:** *In the last 3 months, how often did your {care manager} already know your situation, without you having to go over it again?*
- **Clarification:** *I mean whether you had to repeat your history, your health problems or your circumstances each time you spoke.*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** → **B0**
- **Why worded this way:** Isolates continuity lost to caseload churn and handoffs — an **agency-level staffing signal, not an individual one**, which matters because §2.2 excludes individual-level output. Worded **positively** (*already knew*) rather than negatively (*had to explain again*) so the whole frequency battery keeps one polarity: a mixed-polarity battery read aloud raises the error rate more than it buys in acquiescence control. Anchored on the member's own experience of repeating themselves, because staff turnover is the cause and the member cannot observe it.

---

### B3 · `CMH-03` — action on a requested service change

```
[DRAFT · TIER A — editable]
```

- **ID:** `CMH-03` · **Construct:** whether a requested change to services was acted on
- **Wording:** *In the last 3 months, when you asked for that change, did your {care manager} do something about it?*
- **Clarification:** *I mean whether anything happened after you asked — whether they took any step on it, even if the change did not end up happening.*
- **Scale:** `SC-03` Yes/No + missing codes
- **Routing:** asked only of `YES` at **B0** → **C1**
- **Why worded this way:** ⚑ **Read this one before editing it.** This item replaces the tier B pair Q52+Q53, and the trap is close. The framework's own construct label for `CMH-03` — *"the care manager **worked with** the member when a change to their services was asked for"* — echoes the published item's phrasing, and drafting to that label would have produced exactly the borrowed-paraphrase defect the `wording_source` field exists to catch. **The item is therefore deliberately not that item.** It measures whether **a step was taken**, which is narrower than collaboration, ours, and the thing an LHH can actually audit. The clarification carries the whole weight of separating **effort from outcome**: without it, a member whose requested change was reasonably refused answers `NO`, and the item silently becomes a measure of whether members get what they ask for.

---

## Section C · Communication — tier A throughout

**Every item in this module is original** (`D-CX-13`). The source contains **no care-manager-referenced communication item at all**: its whole communication battery is anchored to paid in-home staff and homemakers, and the *Your Case Manager* section has none. The subset was empty, not small.

⚑ **The specific drafting trap, recorded because it is the one that would actually happen.** The source's staff-referenced battery is the nearest available phrasing in existence for these constructs. Reaching for it — *listened carefully*, *explained things in a way that was easy to understand*, *treated you with courtesy and respect* — produces an item that looks published, is not, and carries borrowed phrasing indefensible in a provenance appendix. **All four items below are written from the construct, not from the source.** An edit that drifts back toward that phrasing reintroduces the defect.

**Order.** The module runs `COM-02` → `COM-03` → `COM-01` → `COM-04`: in, clarity, usability, out. That is the order the member experiences, not the order the IDs were assigned. **IDs are stable and do not renumber** (framework §2.4).

---

### C1 · `COM-02` — uptake

```
[DRAFT · TIER A — editable]
```

- **ID:** `COM-02` · **Construct:** what the member says is taken in, not worked around
- **Wording:** *In the last 3 months, how often did your {care manager} take what you told them into account when deciding what to do next?*
- **Clarification:** *I mean whether what you said actually made a difference to what happened, rather than being noted and set aside.*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** all who clear A1 → **C2**
- **Why worded this way:** Deliberately measures **uptake rather than attention**. *Did they listen to you* is answered generously by almost everyone and discriminates between agencies barely at all; *did what you said change what happened* is the version that separates them, and it is the version an LHH can act on. The clarification names the failure mode explicitly — *noted and set aside* — because that is the experience members describe and have no single word for.

---

### C2 · `COM-03` — clarity

```
[DRAFT · TIER A — editable]
```

- **ID:** `COM-03` · **Construct:** things are explained in terms the member understands
- **Wording:** *In the last 3 months, how often did your {care manager} explain things in words that made sense to you?*
- **Clarification:** *I mean whether you were left clear about what was being said, or left having to guess.*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** → **C3**
- **Why worded this way:** The comprehension half of the module. Worded on **the member's experience of clarity** rather than on a staff behaviour, because a member can report the first reliably and the second only by inference. Kept separate from `COM-01` because a member can understand an explanation perfectly and still not know what to do with it — and those two failures have different fixes, one in how staff talk and one in what they hand over.

---

### C3 · `COM-01` — actionability

```
[DRAFT · TIER A — editable]
```

- **ID:** `COM-01` · **Construct:** explanations the member can act on, not merely understand
- **Wording:** *In the last 3 months, how often did you know what to do next after your {care manager} explained something?*
- **Clarification:** *I mean whether you were clear about the next step — who to call, what to bring, when something would happen.*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** → **C4**
- **Why worded this way:** The item that distinguishes this module from a generic communication battery. **Comprehension is not the outcome the programme is paid for; a member acting on what they were told is.** Placed after `COM-03` so the two are answered in the order the member experiences them. The clarification is concrete on purpose — *who to call, what to bring, when* — because an abstract clarification of "actionable" would lead the answer, and a concrete one only anchors it.

---

### C4 · `COM-04` — the return direction

```
[DRAFT · TIER A — editable]
```

- **ID:** `COM-04` · **Construct:** the member can say when something is not working
- **Wording:** *In the last 3 months, how often did you feel able to tell your {care manager} when something was not working for you?*
- **Clarification:** *I mean whether you felt you could say so — not whether anything changed afterwards.*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** → **D1**
- **Why worded this way:** **This is the item that delivers the module's stated decision question.** `COM-01/02/03` all run care manager → member; this one runs the other way, and without it the module measures one direction and claims two. Distinct from `GRV` (a formal problem, after the fact — and `GRV` is not in this configuration) and from `POC-03` (choice between options). The clarification does the item's hardest work: **feeling able to speak** and **being acted on** collapse into one answer in members' minds, and only the first is what this item measures. `COM-02` measures the second.

---

## Section D · Access and timeliness — tier A

`ACC-01` is cut (§1.4); reachability is carried by the locked `A2`. **`ACC-04` and its screen are cut in the owner's edit pass** (`D-CX-21`): a member who arranged an appointment without ever asking for help had nowhere clean to land, and the content now lives in the `UNM` checklist as `UNM-MED` — where the uptake stage separates *never raised* from *raised and failed*. The module runs on `ACC-02` and `ACC-03`; HH0003's *timeliness of appointments* is carried by `UNM-MED` together with these two.

---

### D1 · `ACC-02` — time to a response

```
[DRAFT · TIER A — editable]
```

- **ID:** `ACC-02` · **Construct:** responsiveness, in time units
- **Wording:** *In the last 3 months, when you left a message for your {care manager}, how long did it usually take to hear back?*
- **Clarification:** *I mean a message of any kind — a voicemail, a text, or a message left with someone at the office.*
- **Scale:** `SC-09` — **original.** `1 Same day` · `2 The next day` · `3 Two or three days` · `4 Longer than three days` · `5 Usually did not hear back` · `6 Did not leave a message in the last 3 months` — plus missing codes
- **Routing:** all who clear A1 → **D2**
- **Why worded this way:** The **only** item in the instrument that measures responsiveness in time units rather than in frequency judgments, which is what makes it comparable across agencies whose caseload structures differ. `5 Usually did not hear back` is a **substantive category, not missing data**, and is reported as such. Option `6` carries the need screen **inside the item** rather than as a separate question — one question saved against a budget already 3 items over ceiling. ⚑ **The trade is real:** it depends on the member classifying themselves correctly, and the clarification is written to support that. **Pretest this specifically.**

---

### D2 · `ACC-03` — contact against what was promised

```
[DRAFT · TIER A — editable]
```

- **ID:** `ACC-03` · **Construct:** contact happens as often as the member was told it would
- **Wording:** *In the last 3 months, how often did your {care manager} contact you as often as they said they would?*
- **Clarification:** *I mean the arrangement you were given about how often you would hear from them — weekly, monthly, or however it was described.*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** → **E1**
- **Why worded this way:** HH0003 names **timeliness of contact** as a content area, and this measures it against a standard **the member was actually given** rather than against an unstated expectation — which is why it fails informatively in two directions. A low rate at an agency where members were promised weekly contact is a staffing problem; a low rate where nothing was ever promised is an onboarding problem, and it will announce itself in the clarification rate before it announces itself in the data. ⚑ **Cognitive-testing item:** a member who was never told a frequency has no basis to answer. The pretest determines whether that case needs its own screen or whether the clarification is sufficient.

---

## Section E · Plan of care

**Section heading (EN):** `CHOOSING YOUR SERVICES` · **(ES):** `La elección de sus servicios`
**The source supplies no lead-in sentence for this section in either language.** None is invented.

**Order.** The two locked items come first, then `POC-03`. With `POC-01` cut (`O-CX-22`, owner), the DK-priming argument that fixed the v0.1 order is moot, but the order stands: one register change, between E2 and E3, at the block boundary `D-CX-18` prefers. `POC-B-01`'s `DON'T KNOW` rate now carries plan knowledge alone, and the codebook records it as the measure `POC-01` used to duplicate.

---

### E1 · `POC-B-01` — plan content

```
[LOCKED · TIER B · VERBATIM — source Q56 — DO NOT EDIT]
```

> **EN:** `In the last 3 months, did your [program-specific term for "service plan"] include . . .`
> **ES:** `En los últimos 3 meses, ¿qué se incluyó en su [término específico de cada programa que se refiere a un "plan de servicios"]?`

**Response set:** `SC-07`
- **EN:** `1 None of the things that are important to you,` · `2 Some of the things that are important to you,` · `3 Most of the things that are important to you, or` · `4 All of the things that are important to you?`
- **ES:** `1 Ninguna de las cosas que son importantes para usted` · `2 Algunas de las cosas que son importantes para usted` · `3 La mayoría de las cosas que son importantes para usted` · `4 Todas las cosas que son importantes para usted`

**Missing-code routing (as published):** `-1 DON'T KNOW → GO TO Q58` · `-2 REFUSED → GO TO Q58` · `-3 UNCLEAR RESPONSE → GO TO Q58` — i.e. all three route to **E2**.
**Routing.** Answered → **E2**. This is the landing point for the `CMH-B-00` skip.

⚑ **EN and ES are structurally different here, and both are used as published.** In English the options complete the stem sentence; in Spanish the stem is a standalone wh-question and the options stand free. This is one of several places where the official Spanish is an **adaptation rather than a translation** — which is precisely why `D-CX-12` uses it verbatim instead of translating.

---

### E2 · `POC-B-02` — route to changing the plan

```
[LOCKED · TIER B · VERBATIM — source Q58 — DO NOT EDIT]
```

> **EN:** `In the last 3 months, who would you have talked to if you wanted to change your [program-specific term for "service plan"]? Anyone else? [INTERVIEWER MARKS ALL THAT APPLY]`
> **ES:** `En los últimos 3 meses, ¿con quién hubiera hablado si quisiera cambiar su [término específico de cada programa que se refiere a un "plan de servicios"]? ¿Hablaría con alguien más? [INTERVIEWER MARKS ALL THAT APPLY]`

**Response set (EN):** `1 CASE MANAGER` · `2 OTHER STAFF` · `3 FAMILY/FRIENDS` · `4 SOMEONE ELSE, PLEASE SPECIFY ___________________` — plus missing codes
**Response set (ES):** `1 ENCARGADO DE CASO` · `2 OTROS MIEMBROS DEL PERSONAL` · `3 FAMILIARES/ AMIGOS` · `4 ALGUIEN MÁS, ESPECIFIQUE` — plus missing codes

**Routing.** → **E3**.

**The unprompted probe is part of the item and is administered as published.** The mode caveat that stood against this item in framework v0.3 is struck (`D-CX-17`): interviewer-coded multiple response with an unprompted *"Anyone else?"* now works exactly as the source intends. The `4 SOMEONE ELSE` open capture is recorded verbatim.

---

### E3 · `POC-03` — real choice

```
[DRAFT · TIER A — editable]
```

- **ID:** `POC-03` · **Construct:** the member was offered a real choice between options, not a single option presented
- **Wording:** *In the last 3 months, when decisions were made about your services, how often were you given a choice between options?*
- **Clarification:** *I mean whether more than one possibility was put to you, rather than a single arrangement being presented as already decided.*
- **Scale:** `SC-01` frequency + missing codes
- **Routing:** → **F0**
- **Why worded this way:** This is where the programme's person-centred language becomes measurable. Deliberately asks about **options offered**, not about *feeling involved*: feeling involved is answered generously and discriminates poorly, while whether a second option was ever put on the table is a **concrete event** a member can recall and an agency can be held to. Distinct from `COM-04` (raising a problem) and from `POC-B-01` (what ended up in the plan). With `POC-02` and `POC-01` cut, this item carries the process side of the module on its own.

---

## Section F · Needs and help — tier A throughout · **rebuilt in this pass (`D-CX-21`)**

**What changed, and why.** v0.1 ran four screen/item pairs on *needed? → got it?*, and the owner's edit pass identified the defect precisely: **"did you get the help you needed" collapses three states an LHH must see separately.** A member whose need never entered joint work with the care manager answers `NO` — but that is an uptake gap, not a delivery failure, and counting it as unmet misattributes it. A member whose housing case is in active work answers `NO` too — because housing does not resolve inside one 3-month window — and counting *that* as unmet punishes exactly the agencies doing the slow work. The rebuilt module separates **need present → taken up together → resolved / in progress / not resolved**, with *never taken up* as its own reportable state.

**Structure:** an 11-domain **need checklist** (Yes/No screens, read as a battery) → **one uptake-and-outcome item per flagged domain** (`SC-10`) → the open catch-all. The domain list is the owner's, merged from 14 to 11 for the telephone; the definitions live in the clarifications, not in the read-aloud lines.

**Reporting, per domain:** need prevalence · share of flagged needs **not worked on together** — an outreach and assessment signal, **never attributed as care-manager failure**; the category includes needs the member resolved without the programme, and whether it needs splitting is a named pretest question · among needs worked on together: **resolved** (top-box) / **in progress** (separate rate, never counted unmet) / **not resolved**. The BOILERPLATE invariant holds and is strengthened: a no-experience state is never recoded as a negative, and a no-uptake state is never recoded as a delivery failure.

**Timeframe: the last 3 months, unchanged** — one recall window for the whole instrument. The owner's pass raised lengthening it for slow-moving needs; the `in progress` option is what makes 3 months workable instead, because active-but-unfinished work no longer reads as failure.

⚑ **`UNM-DME` (`O-CX-12`):** under the checklist, a durable-medical-equipment entry costs one line rather than a pair. Still the owner's call; register open.

---

### F0 · `UNM-*-N` — need checklist · 11 screens

```
[DRAFT · TIER A — editable]
```

**Interviewer lead-in (mandatory):** *People in this programme sometimes need help with different parts of life. I am going to read a short list. For each one, please tell me yes or no — was this something you needed help with in the last 3 months?*

Each entry: `SC-03` Yes/No + missing codes. `YES` flags the domain for **F1**. Entries are read in the order below — roughly from the most concrete to the most personal, ending on social connection.

| # | ID | Read aloud | Scripted clarification |
|---|---|---|---|
| 1 | `UNM-HOU-N` | *Your housing or your utilities?* | *I mean anything to do with where you live — rent, repairs, a landlord problem, needing somewhere to live, or keeping the electricity, gas, or phone on.* |
| 2 | `UNM-FOD-N` | *Getting enough food?* | *I mean having enough to eat — food running short, meals, or help applying for food assistance.* |
| 3 | `UNM-BEN-N` | *Benefits or coverage you are entitled to?* | *I mean things like Medicaid, SNAP, SSI, cash assistance, or disability — applying, renewing, or sorting out a problem.* |
| 4 | `UNM-MED-N` | *Getting medical care?* | *I mean finding a doctor or a specialist, or getting a medical appointment made.* |
| 5 | `UNM-MNT-N` | *Mental health care?* | *I mean finding a mental health provider or getting an appointment with one.* |
| 6 | `UNM-SUB-N` | *Treatment for alcohol or drug use?* | *I mean finding treatment or a provider — only if that is something you wanted help with.* |
| 7 | `UNM-MDM-N` | *Managing your medicines?* | *I mean keeping track of them, getting refills, or understanding how to take them.* |
| 8 | `UNM-TRN-N` | *Getting to your appointments?* | *I mean getting there and back — a ride, help with the fare, or arranging transport.* |
| 9 | `UNM-LGL-N` | *A legal or paperwork problem?* | *I mean things like a problem with a landlord, debt, protective services, or paperwork after being in jail or prison.* |
| 10 | `UNM-WRK-N` | *Work or school?* | *I mean finding a job, help with a resume, or finding or getting into an education or training program.* |
| 11 | `UNM-SOC-N` | *Feeling connected to other people?* | *I mean company and support — people to talk to, peer support, or things to do with others.* |

- **Routing:** after entry 11 → **F1**, for the first flagged domain in checklist order. No flags → **F2**.
- **Why built this way:** Screens name **situations, not services** — a member does not know which of their problems the programme classifies under which category (carried from v0.1). Merges, recorded: `HOU` absorbs utilities and household stability; `LGL` absorbs justice-system re-entry; `WRK` merges employment and education; **`MED` absorbs the cut `ACC-04`** (finding a doctor, getting an appointment made). The `FOD`/`BEN` boundary: `FOD` is *having* food, `BEN` is the paperwork — SNAP application lands in either and that is acceptable, because the follow-up, not the domain label, carries the finding. The sensitive entries (`MNT`, `SUB`) are deliberately the shortest read-alouds with the definitional weight in the clarification: every softening clause in a read-aloud raises, not lowers, the threshold to answering yes (carried from v0.1's food reasoning).
- ⚑ **§8.4.1 exposure begins here**, not only at the open items: the `LGL` clarification names protective services, and a spontaneous disclosure can arrive on any entry. The §3.4 protocol governs.

---

### F1 · `UNM-*-W` — worked on together, and what came of it · **one administration per flagged domain**

```
[DRAFT · TIER A — editable]
```

- **ID family:** `UNM-HOU-W` … `UNM-SOC-W` — one item definition, one variable per domain, administered once per flag in checklist order
- **Wording:** *You said you needed help with {need domain}. Have you and your {care manager} worked on that together?* **Read the options aloud.**
- **Scale:** `SC-10` — `1 Yes — and I got the help I needed` · `2 Yes — we are still working on it` · `3 Yes — but I did not get the help I needed` · `4 No — we have not worked on that together` — plus missing codes
- **Clarification:** *I mean whether it was ever taken up between you — you told them, or they asked, and something was agreed or tried. If it is moving but not finished, that is "still working on it"; if it was taken up and went nowhere, that is "did not get the help"; if it never became something you worked on together, that is "no".*
- **Routing:** next flagged domain → after the last, **F2**
- **Why worded this way:** ***Worked on together*, not *discussed*** — a passing mention that produced no agreement or step is not joint work, and the member should not be forced to score it as if it were. The four options are the module's construct: option `1` is the only top-box; option `2` is what makes a 3-month window compatible with needs that take longer than 3 months; option `3` is the only response that reads as a delivery failure; option `4` is heterogeneous **by design** — it holds never-raised, raised-but-not-taken-up, and self-resolved needs, and the report treats it as an uptake signal to investigate, never as a failure and never as an automatic excuse. Whether option `4` needs splitting is a **pretest question, recorded now**: if cognitive testing shows members reliably distinguish *I handled it myself* from *it never came up*, a wave-2 split is one option away. Polarity stays positive throughout — the collapse rejected at `O-CX-24` would have inverted it.

---

### F2 · `UNM-OTH` — open follow-up

```
[DRAFT · TIER A — editable]
```

- **ID:** `UNM-OTH` · **Not a closed item** (`D-CX-19`) — an open probe, counted as such
- **Wording:** *Was there anything else you needed help with in the last 3 months that you did not get?*
- **Interviewer probe** (not a clarification — §5.2): *Anything at all — it does not have to be something the programme normally handles.*
- **Recording:** interviewer-typed summary. `NOTHING` is a valid and expected entry.
- **Routing:** → **G1**
- **Why worded this way:** The catch-all that keeps the 11 pre-specified domains honest. Placed last so it does not cue the closed domains, and its probe widens beyond the programme's remit — an unmet need the programme does not handle is still a finding for an LHH deciding what to refer.
- ⚑ **§8.4.1 exposure.** This item and section H are where a spontaneous disclosure of harm, neglect or acute risk is most likely to arrive. The protocol at §3.4 governs, and it is briefed before the first call, not written after the first disclosure.

---

## Section G · Agency rating, capacity, and outlook

Reached by **everyone**, including members who answered `NO` at `CMH-B-00` — a member who does not know who their care manager is can still rate the agency, still report their own capacity, and still say whether they expect to stay.

---

### G1 · `RAT-01` — overall rating of the agency

```
[DRAFT · TIER A — editable]
```

- **ID:** `RAT-01` · **Construct:** rating of the care management agency overall, separated from the care manager (`D-CX-22`)
- **Wording:** *Using a number from 0 to 10, where 0 means {agency name} has not helped you at all and 10 means it has helped you as much as you could ask for — what number would you give {agency name} overall?*
- **Clarification:** *I mean the agency as a whole — the services, the programme, everything that comes with it — rather than the person you deal with.*
- **Scale:** 0–10 + missing codes
- **Routing:** all → **G2** *(`RAT-01` → `ENG-01`; the former G2–G4 are withdrawn, `D-CX-24`)*
- **Why worded this way:** **Anchored to the agency by name, not to "the Health Home programme" (`D-CX-22`, owner's edit pass):** members recognise the agency they deal with; many do not recognise *Health Home* at all, and an item rating an entity the member cannot place returns affect, not judgment. The construct shift is deliberate and recorded — v0.1 rated the programme; v0.2 rates the agency — and it lands the item exactly on the comparison the LHH buys, since cross-agency contrast is the product. The care-manager/agency separation carries the same logic the programme version did: a member can be well served by a care manager inside an agency that is not delivering, and the LHH's lever differs entirely in the two cases. **The cost, stated:** nothing in the instrument now rates the Health Home programme as such; if the LHH wants that construct, it is a new item, not a refill. Still anchored on **help received**, parallel in kind to the primary criterion at **A3** and placed far from it so the two 0–10 items do not read as the same question twice.
- ⚑ **QA rule, checked mechanically.** The anchor wording here is an **original formulation** and must remain distinct from the locked anchor at **A3**. An edit that drifts this toward *"where 0 is the worst … possible and 10 is the best … possible"* converts an original item into a paraphrase of a tier B item — the defect §2.5 exists to prevent. **A string-similarity check between G1 and A3 runs in the QA layer.**

---

### ~~G2–G4~~ · `SEF-01` … `SEF-03` — **WITHDRAWN** (`D-CX-24`, owner, 2026-08-05)

⚑ **`O-CX-1` is closed: the dual criterion is declined.** The three confidence items are **not administered**. Their drafted wording is preserved in the withdrawn annex at **§9** — not deleted, because a withdrawn item with its reasoning line intact is a cheap thing to reinstate and an expensive thing to re-derive. **The IDs `SEF-01`, `SEF-02`, `SEF-03` are retired and are never re-issued** (§5.3).

**What the withdrawal costs, stated here rather than only in the framework, because this is the file people read.**

1. **The instrument now has one criterion, not two.** Framework §9.2 collapses to a single-criterion driver model on `RAT-B-01`.
2. **The divergence exhibit is withdrawn, not substituted.** It was the case where members rate the help highly while reporting low capacity to act alone — the finding claims data cannot produce. There is no other capacity measure in the instrument, so it is **removed rather than reconstructed from a proxy**. Reconstructing it from `UNM` would be a different claim wearing the same exhibit's clothes.
3. **`EXIT_TYPE`'s *Constrained continuing* type loses one of its two defining conditions** — it was *expects to stay · bottom-half `SEF` · one or more unmet needs*. A provisional single-condition rule is in force so the framework is not left internally broken during the freeze; it is **`O-CX-25`** and it needs the owner's confirmation, not Claude's.

**What the withdrawal buys:** three items, roughly a minute of interview, and a criterion layer that no longer rests on an unanswered question. The expected case falls to ≈22 closed items (§1.1).

---

### G2 · `ENG-01` — expectation of continued enrolment  *(was G5)*

```
[DRAFT · TIER A — editable]
```

- **ID:** `ENG-01` · **Construct:** expectation of still working with the care management agency six months from now (`D-CX-22`)
- **Wording:** *Do you expect you will still be working with {agency name} six months from now?*
- **Clarification:** *I mean your best guess about whether you will still be getting this kind of help from them — not whether you want to.*
- **Scale:** `SC-06` — `1 Definitely no,` · `2 Probably no,` · `3 Probably yes, or` · `4 Definitely yes?` — plus missing codes
- **Routing:** `3 Probably yes` / `4 Definitely yes` or missing → **skip to H1**. `1 Definitely no` / `2 Probably no` → **G3**
- **Why worded this way:** Feeds `EXIT_TYPE` (framework §9.1). Worded as **expectation, not desire** — in this programme leaving is frequently the *intended* good outcome, and a "do you want to stay" item scores continued dependence as success; the clarification is where the two readings get pulled apart. **Anchored to the agency by name (`D-CX-22`), and the anchor repairs a blind spot:** under the v0.1 programme anchor, a member planning to transfer between CMAs answered *staying*, and the `TRF` reason code — which §9.1 deliberately assigns to Disengaging as a signal about the CMA being left — could never fire. Under the agency anchor, transfers surface. `EXIT_TYPE` remains a programme-level typology; the reason codes at **G6** separate agency exit from programme exit.

---

### G3 · `ENG-02` — reason · conditional  *(was G6)*

```
[DRAFT · TIER A — editable]
```

- **ID:** `ENG-02` · **Construct:** pre-registered attribution for an expected exit
- **Wording:** *What is the main reason you think you will not still be with {agency name}?*
  **Then:** *Is there any other reason?*
- **Clarification:** *I mean the main thing that will bring it to an end for you.*
- **Scale:** `[INTERVIEWER CODES TO LIST — DO NOT READ ALOUD]` · one **main** + all that apply:
  `IND` no longer needs this kind of help · `FAM` family or friends now provide it · `ORG` another organisation provides it · `TRF` moving to a different agency or Health Home · `INEFF` the help was not useful · `CONT` could not reach or rely on the care manager · `ELIG` eligibility, coverage, or a move · `HLTH` health change · `OTH` other *(open follow-up)*
- **Routing:** asked only of `1`/`2` at **G2** → **H1**
- **Why worded this way:** Categories are **fixed before fieldwork and never coded post hoc from open text** (framework §9.1), because `EXIT_TYPE`'s derivation rule is pre-registered and a post-hoc coding frame would let the typology be fitted to the data it is supposed to test. **Not read aloud**, for two reasons: nine options over the phone is expensive, and reading them cues `IND` — *"I can manage on my own"* is already the socially comfortable answer in a dependent population interviewed by a stranger.
- ⚑ **The known bias direction is handled analytically, not by the item.** This will **over-count Graduating and under-count Disengaging** if read at face value. Framework §9.1's mandatory triangulation against the experience composites is what catches it, and *masked disengagement* is an **aggregate analytic category, never an individual label.** No member is told, and no report says, that a stated reason was disbelieved. With the agency anchor at **G5**, `TRF` is now a reachable code rather than a dead one — see the note there.

---

## Section H · Open-ended

**Recording:** interviewer-typed summaries, **not verbatim.** That fact is disclosed in the report (framework §11) and they are never presented as quotations. Thematic coding by two coders with adjudication; quotes only above the anonymity threshold and paraphrased where identifying.

### H1 · `OPN-01`
- *What is the one thing that would most improve the help you get?*
- **Probe:** *Anything at all — big or small.*

**`OPN-02` (*what is working well*) is cut in the owner's edit pass (`D-CX-23`).** Section H runs on `OPN-01` alone: the improvement question does the decision work.

→ **§3.5 close (stub).**

⚑ **§8.4.1 exposure.** With `F2`, this is the most likely point of spontaneous disclosure. The §3.4 protocol governs.

---

## Section I · About you — **DECLARED SLOT, TEXT ABSENT** (`D-CX-25`)

```
[SLOT · TIER B · AWAITS VERBATIM EXTRACTION — DO NOT DRAFT]
```

**Owner's instruction, session 7:** add the source's *about you* block and the interviewer questions.
**Accepted in principle. Not drafted, and the reason is the same rule that governs Section A.**

`tier-b-source-items.md` v0.2 extracted the case-manager, plan-of-care and rating slots only. **The *about you* items were never extracted, and there is no verbatim text for them in the reference layer.** Under verbatim-or-nothing (framework §2.5) the choice here is between the published strings and nothing — and writing demographic items that *look like* the published ones from memory is the single defect the whole two-register apparatus exists to prevent. So the slot is declared and left empty.

**What has to happen before this section carries text** — the thaw precondition, in order:

1. **Extraction.** The source PDFs in the project are page images, not text, so the block has to be read off the pages and transcribed under the same byte-verification discipline as the six existing locked items, then added to `tier-b-source-items.md` as **v0.3** with a transferability determination per item. This is a session of its own.
2. **Scope decision — `O-CX-27`, and it is the real one.** Not *shall we add the block* but **which items are asked of the member at all.** The LHH's file already holds much of this and the BAA already covers a disclosure for health-care operations (§10.3): **date of birth, sex, and language of administration do not need to be asked** — asking a member to recite what the buyer already knows spends interview minutes and buys nothing. The items that **do** have to be self-reported are the ones where the administrative record is systematically worse than self-report, and in Medicaid data that is **race and ethnicity above all**, plus anything about the member's own circumstances the file cannot hold. ⚑ **The equity analysis is the reason this block exists** — without it the report cannot say whether experience differs by group, which is a standard the LHH will eventually be held to.
3. **Suppression check, and it is the constraint nobody expects.** Every demographic added is a breakdown dimension, and framework §2.2's `N ≥ 10` rule bites at agency level fast. At ~100 completes per agency a five-category variable produces cells that suppress on sight. **More demographics can therefore mean fewer reportable findings, not more** — so the block is specified against the breakdowns actually promised in the report, not collected for completeness.
4. **Placement.** Last, after Section H, per convention: sensitive and low-effort items go where breaking off costs the least.

⚑ **Budget consequence, already recorded at §1.1 and §1.3:** this block is what the `SEF` headroom is for. It is not free space.

---

## Section J · Interviewer questions — **DECLARED SLOT, TEXT ABSENT** (`D-CX-25`)

```
[SLOT · AWAITS SCOPE DECISION — DO NOT DRAFT]
```

Post-interview items completed by the interviewer, not asked of the member — who assisted, in what language, under what conditions.

⚑ **This one is not only an extraction problem — it is an overlap problem, and that is why it cannot be copied in without a decision.** §5.5 and framework §2.3 already require, as fielding metadata: interviewer identity on every completion, proxy and assisted-completion status recorded as a variable and reported as a rate, language of administration, achieved mode, and per-interviewer clarification and `UNCLEAR` rates. **A source interviewer block would duplicate part of that in different wording, with two fields meaning nearly the same thing and no rule for which one the report uses.** The decision at thaw (`O-CX-27`) is therefore: adopt the source block verbatim and **retire** the overlapping fielding fields, or keep our fielding metadata and take from the source only what it does not already cover. **Not both.**

Note that these items are **not member-facing**, so the register rules at §0.1 apply to their text but the cognitive-testing and translation obligations do not.

---

## 4 · Routing map

```
  §3.1  advance contact        [STUB]
  §3.2  introduction + notice  [STUB]
  §3.3  proxy/assisted consent [STUB]
    │
    ▼
  A1  CMH-B-00  gate  ──── NO / missing ──────────────────┐   (skips 13 questions)
    │ YES                                                 │
    ▼                                                     │
  A2  CMH-B-01   ▸ A3  RAT-B-01   ▸ A4  RAT-B-02          │
    │                                                     │
    ▼                                                     │
  B1  CMH-01  ▸ B2  CMH-02  ▸ B0  CMH-03s ──NO/missing──┐ │
    │                            │ YES                  │ │
    │                            ▼                      │ │
    │                          B3  CMH-03 ──────────────┤ │
    ▼                                                   │ │
  C1  COM-02 ▸ C2 COM-03 ▸ C3 COM-01 ▸ C4 COM-04  ◀─────┘ │
    │                                                     │
    ▼                                                     │
  D1  ACC-02  ▸ D2  ACC-03                                │
    │                                                     │
  E1  POC-B-01 ◀──────────────────────────────────────────┘
    │  (DK / REF / UNCLEAR → E2, as published)
    ▼
  E2  POC-B-02 ▸ E3  POC-03
    │
    ▼
  F0  UNM-*-N   need checklist, 11 entries, read as a battery
    │
    ├─ for each flagged domain, in checklist order:
    │      F1  UNM-*-W  (SC-10)
    │
    ▼
  F2  UNM-OTH  (open)
    │
    ▼
  G1  RAT-01                       [SEF-01…03 withdrawn, D-CX-24]
    │
    ▼
  G2  ENG-01 ──── 3 / 4 / missing ──────────────┐
    │ 1 / 2                                     │
    ▼                                           │
  G3  ENG-02                                    │
    │                                           │
    ▼                                           │
  H1  OPN-01  ◀─────────────────────────────────┘
    │
    ▼
  I   about you            [SLOT — declared, undrafted, D-CX-25]
    │
    ▼
  §3.5  close  [STUB]
    │
    ▼
  J   interviewer questions  [SLOT — post-interview, declared, undrafted, D-CX-25]
```

**Skip accounting**

| Path | Questions skipped |
|---|---|
| `CMH-B-00` = `NO` | 13 (A2–A4, B0–B3, C1–C4, D1–D2) |
| `CMH-03s` = `NO` | 1 |
| Each unflagged `UNM` checklist entry | 1 follow-up administration (×11 maximum) |
| `ENG-01` = probably/definitely yes | 1 |
| **Maximum path** (CM known, all 11 needs flagged, expects to leave) | **44 questions** |
| Expected path (CM known, 3 needs flagged, expects to stay) | **≈35 questions** |
| **Minimum path** (no CM known, no needs flagged, expects to stay) | **19 questions** |
| *All three figures exclude Sections I and J* | declared, undrafted (`D-CX-25`) |

---

## 5 · QA rules carried into the codebook and the pipeline

### 5.1 Locked strings

**Every locked string in this file is generated from `tier-b-source-items.md` v0.2 and checked byte-for-byte against it.** A mismatch is a **defect, not a variant.** The check is mechanical, its result is recorded at §6, and it re-runs on every revision of this file.

**Locked scope:** item wording (EN and ES), response-option wording and order, section headings, section lead-ins, published skip targets, and punctuation including the trailing `. . .` and the doubled Spanish `¿`.

### 5.2 Clarifications vs probes — a distinction the QA layer checks

| | Applies to | Rule |
|---|---|---|
| **Scripted clarification** | Every tier A **closed** item and every tier A **screen** | Exactly one, printed here, read only on the respondent's signal, never improvised. **Use is logged per item** |
| **Source probing rules** | The six locked items | One verbatim re-read, then the source's own rules, then `UNCLEAR`. **Never a clarification** |
| **Interviewer probe** | Open-ended items only (`UNM-OTH`, `OPN-01`) | A prompt to continue, not an alternative phrasing. Not logged as clarification |

**Checked:** one and only one clarification on every tier A closed item and screen — for **F0** the clarification column of the checklist table is the clarification bank, one per entry; for **F1** the single definition carries the single clarification for all administrations · **zero** clarifications on all six locked items · probes only on the two open items.

### 5.3 Item-ID integrity

- `-B-` IDs are a **closed set of six** (framework §2.4). Any `-B-` ID outside `RAT-B-01`, `RAT-B-02`, `CMH-B-00`, `CMH-B-01`, `POC-B-01`, `POC-B-02` appearing on a fielded item is an error. Retired IDs (`CMH-B-02`, `CMH-B-03`, `COM-B-01…03`) are never re-issued.
- **Retired tier A IDs, added at v0.3:** `SEF-01`, `SEF-02`, `SEF-03` (`D-CX-24`), alongside `ACC-01`, `ACC-04`, `POC-01`, `POC-02`, `ENG-03`, `OPN-02`. **A withdrawn item's ID is retired, not freed.** If `SEF` is ever reinstated it returns under its own IDs with its original wording from the §9 annex — which is the only way a later wave can tell reinstatement from a new item.
- IDs never change meaning between waves. **Revised wording gets a suffix** (`CMH-01b`), never a new ID and never a reused one. This applies to the owner's edit pass: an item rewritten in this pass and then fielded is `v0.1` wording under its existing ID; an item rewritten *after* a wave has fielded takes the suffix.
- Question labels (`A1`, `B3`, `F0`) are **positional and unstable by design** — they exist for this edit pass and are not carried into the codebook.

### 5.4 Original-wording checks

- **`RAT-01` (G1) against `RAT-B-01` (A3):** string-similarity check on the anchor phrasing. Drift toward the published anchors converts an original into a paraphrase of a tier B item.
- **Section C against the source's staff battery:** the four `COM` items are checked against the dropped source items recorded in `tier-b-source-items.md` §7. The nearest available phrasing for these constructs is the phrasing we must not use.
- **`CMH-03` (B3):** checked against Q53 *and* against the framework's own construct label for `CMH-03`, which itself echoes the published phrasing.
- Every item carries `ip_tier`, `wording_source`, `concept_overlap_with_published_instrument` in the codebook (framework §2.5). **Tier A items with conceptual overlap are legitimate and expected; tier A items with borrowed phrasing are a defect and are caught here.**

### 5.5 Fielding-layer checks

- Every fill in §2.4 resolved before fielding; **no unresolved brace reaches a member.**
- Fill maps are written against the two brace families separately; a map that rewrites a locked item's brace name is a defect.
- Interviewer identity recorded on every completion; clarification rate and `UNCLEAR` rate monitored **per interviewer during fielding**, not discovered in analysis (framework §2.3).
- Achieved mode, proxy/assisted rate, language of administration, and **telephone-coverage exclusion rate** recorded per agency and printed as coverage figures (framework §8.5, §10.2).

---

## 6 · Locked-string verification — result

| Check | Method | Result |
|---|---|---|
| All locked strings byte-identical to `tier-b-source-items.md` v0.2 | Per-line programmatic extraction of every verbatim string in the six `[LOCKED]` blocks (stems, response options, lead-ins, headings, published skip targets, EN and ES), byte-compared against the source file fetched from `survey-skills@main`. **No verbatim string was retyped in this revision** — the pass was applied around the locked blocks, never through them | ✅ **70 of 70 strings pass** *(v0.1 reported 91: the count fell because the check now excludes our own notation — scale IDs, item IDs — from the tally, not because any string changed)* |
| Owner's edit pass touched no locked item | All six locked blocks diffed against v0.1 | ✅ pass — byte-identical; no comment in the pass targeted a locked item |
| **v0.3 touched no locked item** | `qa_check.py`, run standalone: the six locked blocks located by fence, every verbatim string extracted from its **carrier line** (`EN:`/`ES:` stems, response-option lines, section headings and lead-ins, published missing-code skip targets) and byte-compared against v0.2 | ✅ **58 of 58 strings pass.** The session-7 changes are a withdrawal in section G, two declared slots after section H, and notes printed **beneath** the A1, A2 and A3 blocks in our own register. **No edit passed through a locked span** |
| ⚑ **Two extractors, two counts — reconcile before the codebook** | v0.2 reported **70** strings, v0.1 reported **91**, this run reports **58** | ⚑ **Not a content change — an extraction-rule change, three times running.** Every string that all three extractors agree is locked has been byte-identical throughout. But a QA figure that moves whenever the script is rewritten cannot be cited as evidence, which is the only thing it is for. **One extractor, fixed and committed, before the codebook session** — added to the thaw checklist |
| Declared slots carry no drafted text | Sections I and J scanned for item wording | ✅ pass — requirements and preconditions only; **zero item strings**, which is the point (`D-CX-25`) |
| Locked scope covers punctuation | Trailing `. . .` at A4, doubled Spanish `¿` at A3, `___________________` at E2, EN/ES structural divergence at E1 — all reproduced, none corrected | ✅ pass |
| Exactly one clarification per tier A closed item and screen | 15 inline (`CMH` 3 + `CMH-03s` + `COM` 4 + `ACC` 2 + `POC-03` + `UNM-*-W` definition + `RAT-01` + `ENG-01` + `ENG-02`) + 11 in the F0 checklist table = **26 expected for 26 definitions** *(−3: the withdrawn `SEF` clarifications live in the §9 annex and are excluded from the fielded count)* | ✅ **26 found, 26 expected** |
| Zero clarifications on the six locked items | Block-level scan of every `[LOCKED · TIER B · VERBATIM]` section | ✅ pass — 0 found |
| Open items carry probes, not clarifications | `UNM-OTH`, `OPN-01` | ✅ **2** probes, one per open item |
| `-B-` ID set closed at six | `RAT-B-01`, `RAT-B-02`, `CMH-B-00`, `CMH-B-01`, `POC-B-01`, `POC-B-02` — no other `-B-` ID on a fielded item (retired `CMH-B-02`/`CMH-B-03` appear in prose as history only) | ✅ pass |
| No `{Health Home programme}` fill survives | `D-CX-22` retired it | ✅ pass — replaced by `{agency name}` |

**Extraction is re-runnable.** The generator reads `tier-b-source-items.md` by section and line, emits a keyed string table, and renders this file from it. Re-running against a future version of the source file will fail loudly on any string that has moved or changed, rather than silently producing a stale instrument.

---

## 7 · Open items touching this file

| ID | State at v0.2 |
|---|---|
| `O-CX-1` | ✅ **CLOSED → `D-CX-24`** (owner, 2026-08-05). Dual criterion declined; `SEF` withdrawn (§9 annex). **Asked three times across sessions 5–7; answered at the second reading** |
| `O-CX-2` | **Open — counsel.** ⚑ **Re-surfaced at session 7 because the owner could not locate it.** Where it lives is now quoted at §3. **The whole decision is one sentence:** does framework §10.3's *no instrument text before counsel* bind the item bank, or only the introduction, consent, disclosure and close? All three versions are built on **only the latter**. ⚑ Now entangled with `O-CX-26`, which would change the PHI field list counsel is asked to approve |
| `O-CX-5` | **Open — per-agency completes.** Acute under a telephone census. Not resolvable in a drafting session |
| `O-CX-6` | **Open — top-box for the 0–10 rating.** Lands on A3 and G1. Needed before the codebook session |
| `O-CX-7` | ⚑ **Disposed of, sign-off pending** — stood through the edit pass without objection. `UNCLEAR` adopted (§2.2); alternate version excluded (§2.5) |
| `O-CX-8` | ⚑ **Resolved, sign-off pending** — `ACC-01` cut (§1.4); stood through the edit pass without objection |
| `O-CX-9` | ⚑ **Resolved, sign-off pending** — `POC-02` cut (§1.4); stood through the edit pass without objection |
| `O-CX-10` | ✅ **Closed by the edit pass** — `COM-02/03/04` reviewed without comment |
| `O-CX-11` | ✅ **Closed by the edit pass** — `CMH-03` and its screen reviewed without comment |
| `O-CX-12` | **Open** — under the F0 checklist a `UNM-DME` entry costs one line, not a pair. Owner's call |
| `O-CX-16` | **Disposed of** — automated voice excluded (§2.5) |
| `O-CX-20` | **Drafted** — 29 clarifications over 29 definitions (§6). Open until cognitive testing |
| `O-CX-21` | ✅ **Closed → `D-CX-20`** — criterion stays at question 3 (§A) |
| `O-CX-22` | ✅ **Closed** — `POC-01` cut (owner, §1.4) |
| `O-CX-23` | ✅ **Closed** — `SC-08`, `SC-09`, `SC-10` registered in framework §2.1 at v0.5, top-box definitions stated |
| `O-CX-24` | ✅ **Closed — superseded by `D-CX-21`.** The three-option collapse is off the table; the rebuilt module saves length by the checklist route without inverting polarity |
| `O-CX-25` | ⚑ **New at v0.3.** `EXIT_TYPE` *Constrained continuing* after the `SEF` withdrawal. **A provisional single-condition rule is in force** (expects to stay · one or more unmet needs, `SC-10` outcome `3`) so the framework is not internally broken during the freeze. **Provisional means provisional:** the type no longer carries *no progress toward independence*, only *continuation with unmet need*, and if that is not what the type is for it should be renamed or the four-type typology reduced to three. **Owner's decision, not Claude's** |
| `O-CX-26` | ⚑ **New at v0.3.** Identifying the care manager to the member — name vs. role description vs. programme term. Proposed sequence rule drafted at §2.6, **not adopted**. Touches A1's measurement value, adds `CM_NAME_RECOG`, and **expands the PHI field list `D-CX-17` narrowed** — so it feeds directly into the `O-CX-2` counsel package and is best decided **before** that package is assembled |
| `O-CX-27` | ⚑ **New at v0.3.** Scope of Sections I and J. **Not *whether* but *which*:** which member characteristics are asked versus taken from the LHH file under the existing BAA; and whether the source's interviewer block replaces or supplements the fielding metadata at §5.5 — **not both**. Blocked on a verbatim extraction into `tier-b-source-items.md` v0.3 |
| `O-CX-28` | ⚑ **New at v0.3.** A1 `YES` but no contact in 3 months — no back-out screen. **Recommendation: keep it that way**, `Never` is substantive and a screen would hide the most important members behind a skip (§A1) |
| `O-CX-29` | ⚑ **New at v0.3.** A2 has no *did not need to make contact* option and is locked. **Recommendation: non-substantive code `-7`, excluded from the CMH denominator, reported as a rate** (§A2). Changes a composite denominator, so it is settled **before** the codebook |
| — | ⚑ **Pretest register:** whether `SC-10` option `4` needs splitting (self-resolved vs never raised) — F1 · `ACC-02` self-classification on option `6` — D1 · `ACC-03` members never given a contact frequency — D2 · `RAT-B-02` conditional clause — A4 · A3 placement affect-rating watch — `D-CX-20` · **new at v0.3:** whether members can place *{agency name}* at all (`RAT-01`, `ENG-01`), which is the pretest that settles half of `O-CX-26` empirically rather than by argument |

---

## 8 · Change log

**v0.3 · 2026-08-05 · CX session 7 — documentation & freeze pass. ⏸ CX frozen after this version.**

- **`D-CX-24` — dual criterion declined, closing `O-CX-1` (owner).** `SEF-01…03` withdrawn to the §9 annex, IDs retired. Framework §9.2 collapses to a single criterion; the divergence exhibit is **withdrawn, not substituted**; `EXIT_TYPE`'s *Constrained continuing* runs on a **provisional** single condition pending `O-CX-25`.
- **`D-CX-25` — Sections I (*about you*) and J (*interviewer questions*) declared as slots (owner).** Accepted in principle, **text absent**: the verbatim strings are not in `tier-b-source-items.md` and verbatim-or-nothing forbids approximating them. Preconditions and the scope question written into both sections and into `O-CX-27`.
- **`D-CX-26` — CX frozen at v0.3** while Employee is finalised. Freeze notice at the head of this file; thaw preconditions in `session-brief-cx-07.md`.
- **Owner's second-reading questions written down rather than answered by assumption:** care-manager identification (`O-CX-26`, proposed protocol at §2.6, not adopted) · A1 non-substantive routing (answered inline — it routes with `NO`) · A1 `YES` with no contact (`O-CX-28`) · A2 with no *did not need to* option (`O-CX-29`) · `O-CX-2` re-surfaced with its physical location quoted at §3.
- Arithmetic regenerated: **19** closed bank items · expected **≈22** closed / **≈35** questions · maximum **44** · minimum **19** · ~12 nominal / ~14 achieved, **excluding Sections I and J**, which are pre-committed against the new headroom (§1.3).
- Clarification count **29 → 26** (the three `SEF` clarifications move to the annex with their items).
- ⚑ **Reading-copy defect found and recorded, not fixed here.** The Russian reading copy of v0.2 renders **A2** as a four-point frequency item about *how often the care manager helped when you asked*. **A2 is a locked Yes/No item about whether the member could make contact.** The reading copy is a retelling, not a translation, and it drifted on a locked item — the one place drift is least acceptable. **The working file is correct and was never affected.** The reading copy is superseded and is **regenerated from this file at thaw, mechanically**, not re-edited.
- Locked strings re-verified: **six blocks byte-identical to v0.2** (§6).

**v0.2 · 2026-08-02 · CX session 6 — owner's edit pass applied.**

- Every comment in the owner's pass classified (wording / construct / cut / question) and dispositioned; **no comment targeted a locked item**, so the six tier B strings are byte-identical to v0.1 and to `tier-b-source-items.md` v0.2 (§6).
- **`UNM` rebuilt (`D-CX-21`, construct change, framework §8.2 patched in the same session):** four *needed?→got it?* pairs replaced by an 11-domain need checklist plus one `SC-10` uptake-and-outcome item per flagged need; *in progress* and *not worked on together* separated from *unmet*; `ACC-04` pair cut and absorbed as `UNM-MED`. Supersedes `O-CX-24`.
- **Agency referent (`D-CX-22`, construct change, framework §3 and §9.1 patched):** `RAT-01`, `ENG-01`, `ENG-02` anchored to `{agency name}`; the `{Health Home programme}` fill retired; `TRF` becomes a reachable `EXIT_TYPE` reason code.
- **Cuts (`D-CX-23` + `O-CX-22`):** `POC-01`, `ENG-03`, `OPN-02` (owner). `D-CX-20`: criterion placement at question 3 confirmed, closing `O-CX-21`.
- **`O-CX-23` closed:** `SC-08`, `SC-09`, `SC-10` registered in framework §2.1 (v0.5) with top-box definitions.
- Arithmetic regenerated, not hand-edited: 22 closed bank items + `SC-10` per-flag administrations; expected case ≈25 closed / ≈38 questions; maximum 47; minimum 22; 12 min nominal / ~15 achieved.
- `O-CX-1` (`SEF` provisional) and `O-CX-2` remain open — both unanswered through the pass.

**v0.1 · 2026-08-02 · CX session 5.** First draft of the fielded instrument.

- Configuration: QMP evidence base (`D-CX-19`), 29 closed items, 38 maximum-path questions, 12 min nominal / ~15 achieved.
- Six locked tier B items generated from `tier-b-source-items.md` v0.2 — EN and ES, byte-verified (§6). No verbatim string was retyped at any point; all were extracted programmatically from the source file.
- Twenty-three tier A items and six screens drafted as original formulations, each with one scripted clarification (`O-CX-20`) and a reasoning line.
- Cuts applied: `ACC-01` (`O-CX-8`), `POC-02` (`O-CX-9`), `UNM-OTH` reclassified as an open follow-up (`D-CX-19`).
- Member-facing text held as stubs pending `O-CX-2`.
- Spanish present and locked on tier B items only; tier A Spanish deferred until the owner's edits settle.

---

## 9 · Withdrawn-item annex — `SEF-01` … `SEF-03` (`D-CX-24`)

**Held, not deleted.** These three items are not administered and are not in any count in this file. Their wording and reasoning lines are preserved verbatim as drafted at v0.2 so that reinstatement is a decision rather than a re-derivation, and so that a later wave can distinguish a reinstated item from a new one. **Their IDs are retired** (§5.3) and are re-used only by these items.

**Scale for all three:** `SC-08` — `1 Not at all confident,` · `2 A little confident,` · `3 Somewhat confident, or` · `4 Very confident?` + missing codes. Registered in framework §2.1; **no fielded item uses it at v0.3** (§2.3).

**`SEF-01`** · *Construct:* confidence in knowing the route in when something goes wrong · *Wording:* How confident are you that you know who to contact when a health problem comes up? · *Clarification:* I mean if something happened this week — would you know who to call first? · *Reasoning:* measures capacity rather than satisfaction, taking the most concrete part of capacity — knowing the route in — which a member can answer without self-assessment bias swamping it; the clarification makes it a specific hypothetical rather than a general self-rating.

**`SEF-02`** · *Construct:* day-to-day self-management · *Wording:* How confident are you that you can keep on top of your appointments and your medicines day to day? · *Clarification:* I mean managing them yourself — remembering them, getting to them, keeping the prescriptions going. · *Reasoning:* the part of capacity that persists after the programme ends; worded as confidence rather than behaviour because self-reported behaviour over three months is unreliable in this population.

**`SEF-03`** · *Construct:* capacity to initiate, not only to receive · *Wording:* How confident are you that you could get help you needed without waiting for your {care manager} to get in touch first? · *Clarification:* I mean starting it yourself — reaching out, rather than waiting to be contacted. · *Reasoning:* the item that made `SEF` non-redundant with the care-manager composite — a member can be superbly served and still be entirely dependent on the care manager initiating everything, which is the *constrained continuing* pattern in framework §9.1.

⚑ **Read `SEF-03` before any future decision to reinstate.** It is the reason `O-CX-25` exists: with `SEF` gone, *constrained continuing* has no measure of the pattern it was named for.

---

*Document owner: A. Akhtyrskii · Measure & Meaning Research · Prepared with Claude · v0.3 · 2026-08-05 · ⏸ frozen, not fielded · tier B items reproduced verbatim from a publicly distributed CMS instrument, attributed in the provenance appendix, instrument name excluded from all deliverable titles · illustrative + synthetic.*
