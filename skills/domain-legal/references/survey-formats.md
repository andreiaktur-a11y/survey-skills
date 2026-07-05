# Trademark Survey Formats (domain-specific)

The recognized survey **formats** (methods) for evidentiary trademark work, operationalized so design can build from them without improvising. Formats answer *how the stimulus is shown and what is asked*; the construct→indicator→threshold mapping lives in `constructs-and-indicators.md`, and universe/sample/wording/stimulus rules live in `admissibility.md`. Use all three together.

> **Provenance & IP.** These are named, long-standing methodological formats from trademark-survey practice (the format names trace to US case law; the techniques are professional standard practice — **methods, not protected expression**). Written here as **original synthesis**, not copied from any treatise or vendor template. Word every item per `../../../shared/question-quality.md` and the neutrality/sequence rules in `admissibility.md`. **Not legal advice** — confirm format choice and exact construction with counsel and against current Daubert/FRE-702 (US) or Rospatent-SIP (RF) practice.

## How to use
1. Identify the construct (`constructs-and-indicators.md`) → 2. pick the matching format below → 3. screen to the universe (`admissibility.md`) → 4. sequence **open → aided → control** → 5. set threshold logic with counsel → 6. document stimulus, instructions, and scoring in `report-template.md`.

---

## Likelihood of confusion

### Eveready — strong / well-known senior mark
**When:** the senior mark is strong and familiar, so respondents can hold it in memory without it being shown alongside the junior sign.
**Stimulus:** show **only the junior (defendant's) sign** in a realistic context. The senior mark is *not* displayed — recall is from memory, which is what makes the design probative.
**Sequence:**
- *Open/unaided:* "Who do you think puts out this product? / What company?" — then "What makes you say that?" (capture verbatim, no prompting).
- *Aided (only if needed):* affiliation/connection/approval probes ("Do you think the maker of this needs permission from, or is connected with, any other company?").
- *Control questions* to check the answer wasn't externally cued.
**Scoring:** confusion = share naming the senior mark / its owner (or asserting affiliation/sponsorship) as the source, on the open question first. Spontaneous (unaided) attribution carries the most weight.
**Pitfalls:** showing both marks together turns Eveready into a side-by-side comparison and inflates "confusion"; don't. Keep the affiliation probe non-leading.

### Squirt — weaker / less-known mark, marketplace proximity
**When:** the senior mark isn't strong enough for pure memory recall, or the marks genuinely co-appear in the market.
**Stimulus:** a **line-up / array**: the junior sign embedded among the senior mark and neutral others, mimicking shelf/market exposure — not an isolated two-way comparison.
**Sequence:** brief realistic exposure → open source/affiliation question → aided affiliation probe → control.
**Control & scoring:** run a **control stimulus** (see Control-stimulus design) and report **net confusion = test − control**. The control absorbs baseline guessing and demand effects; the *net* figure is the evidence, not the raw test percentage.
**Pitfalls:** an artificial side-by-side that no consumer would encounter; a control too dissimilar (under-corrects) or too similar (over-corrects) to the test stimulus.

---

## Genericness

### Teflon — classification ("brand name vs. common name")
**Stimulus/sequence:**
- *Calibration:* teach the brand/common distinction with neutral, uncontested examples (a known brand and a known common term), and confirm the respondent grasps it.
- *Test:* present a randomized list mixing clear brand names, clear common names, and the contested term; for each, ask "brand name or common name?" with a "don't know" option.
**Scoring:** the share classifying the **contested term as a common name** indicates genericness; the calibration items validate that the respondent understood the task (drop respondents who misclassify the anchors).
**Pitfalls:** weak/biased calibration; an unbalanced list that signals the "expected" answer; omitting "don't know."

### Thermos — elicitation ("what would you ask for?")
**Sequence:** open question — to buy/obtain the product, **what would you ask for?** — recorded verbatim, no list.
**Scoring:** the share spontaneously using the contested term as the **product name** (rather than as one brand among options) indicates genericness.
**Pitfalls:** prompting the term; failing to distinguish "I'd ask for [term]" as a category vs. as a preferred brand — probe to separate the two.

---

## Secondary meaning / acquired distinctiveness
**Goal:** show the designation points to **one source** for the relevant consumers (now, or as of a date).
**Design:** unaided association ("when you see this, what — if anything — comes to mind?" → "does it bring to mind any particular company; which?"), then aided single-vs-multiple-source attribution ("put out by one company, or more than one, or no opinion?").
**Scoring:** secondary meaning is supported by a high share associating the designation with **a single source**; absence is shown by dispersion across many producers or "no opinion." For an "as of a date" claim, anchor questions to that date and assess the fieldwork-vs-relevant-date gap (`admissibility.md` → temporal).

## Dilution / fame
**Goal:** establish the senior mark's **fame/recognition** among the general (not just niche) consuming public, and—where relevant—blurring/tarnishment.
**Design:** unaided then aided recognition tied to the goods, fielded with adequate geographic spread; for blurring, probe whether the junior use brings the famous mark to mind and whether it weakens the one-to-one association.
**Scoring:** recognition level against the case-appropriate benchmark (treat as a reference point, not a fixed cutoff — counsel interprets). Fame is a high bar: broad-public recognition, not category-only.

## Control-stimulus design
The control isolates the contested element by **removing or swapping just that element** while holding everything else constant, so that test − control attributes confusion to the element at issue rather than to format, category cues, or guessing.
- Change **only** the disputed feature (the similar word/figure); keep layout, category, and presentation identical.
- Too-dissimilar control → under-corrects (overstates confusion); too-similar control → over-corrects (hides real confusion). Pretest the control's plausibility.
- Report raw test, raw control, and **net**; describe exactly how the control was constructed.

---

## RF: правило треугольника (triangle rule) — сходство до степени смешения
A triangulation technique used in RF court surveys to separate *actual confusion* from mere surface similarity: the respondent's perception is probed across the disputed sign, the senior mark, and a control comparison, so baseline guessing/association is netted out and genuine source-confusion is isolated. Sequence open (spontaneous source) → aided (perceived sameness of source/affiliation) → control. Net confusion = test − control.
> Exact mechanics vary by practitioner and case — confirm the specific construction against current Rospatent/SIP practice before relying on it. Standard method (not protected expression); word per `../../../shared/question-quality.md` and `admissibility.md`.

## Jurisdiction note — control group
Eveready/Squirt are **US** formats built on a **test/control** design (a control cell nets out baseline noise) — conventional and expected by US courts. **RF** practice (and the SIP note) requires control **questions** inside a single survey, plus the open→aided→control sequence and the triangle rule — a control **group** is **optional**, used case-by-case when it strengthens probativeness, not a default. Don't apply the US control-cell default to RF cases automatically.

## Library entries
Store each format's question pattern in `shared/instrument-library/` as `source: other`, `reuse_tier: A` (method/standard), `verbatim_ok: false` (store the standard pattern, adapt wording per case). No PHI.
