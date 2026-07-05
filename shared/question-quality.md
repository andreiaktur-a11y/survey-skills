# Question Quality (shared reference)

The single source of truth for what makes a survey question good. Three skills read this file and use it from different angles:
- **`survey-instrument-design`** applies these rules to *write* items.
- **`survey-instrument-review`** turns each section into *audit checks* (a violation is a finding; rate it with the severity rubric).
- **`instrument-library`** tags items by the question-type and scale-type vocabulary defined here.

Keep the rules here, not copied into each skill — design and review must judge by the *same* standard, or an audit becomes incoherent.

Pair with `3mc-considerations.md` and `tse-framework.md`: most of what follows reduces measurement error; the 3MC notes guard cross-group comparability.

---

## 0. The gate: every item must earn its place

Before wording anything, tie each item to a **research objective** — the thing you actually need to learn and the decision it informs. Then ask of the item in front of you: *why am I asking this?* If you can't name the objective it serves, cut it. This one discipline prevents bloated instruments, orphan items, and respondent fatigue, and it is the first thing a review should check: an item with no objective behind it is a finding, not a stylistic quibble.

This is the distinction between the *research question* (what you want to know) and the *survey question* (what you put to the respondent). They are not the same, and the craft is the disciplined translation between them.

---

## 1. Know what kind of question you're asking

The type drives both the dominant error to fear and the wording discipline to apply. The CCSG Questionnaire Design chapter lays out a useful taxonomy; synthesized:

- **Knowledge** — what the respondent knows or is aware of (facts, awareness of a program, understanding of a benefit). Risk: guessing; "don't know" handling matters.
- **Factual / autobiographical judgment** — recall of events, behaviors, or figures verifiable in principle against records (visits, calls, dates). Risk: recall error and telescoping (pulling distant events into the reference window). Anchor with a clear, bounded reference period.
- **Socio-demographic** — characteristics (age, language, insurance, household). In a multilingual population these often need **local categories mapped to a common standard** rather than one literal list.
- **Behavioral** — what people do or have done. Risk: social desirability and recall.
- **Attitudinal** — opinions, satisfaction, trust, perceptions. Only the respondent can supply these; nothing external validates them, so wording and scale carry the whole measurement. **Most culturally sensitive** type.
- **Intention / expectation** — future-oriented ("will you…", "what are the chances…"). Hard for respondents, and answered differently across cultures (subjective-probability responses vary with sense of control and with how uncertainty is expressed).

Practical use: a satisfaction survey is mostly *attitudinal* with some *factual* (did the contact happen, how often) and *demographic* items — so the bulk of your measurement risk sits in scale design and translation, not recall.

---

## 2. Wording rules (and the antipatterns)

Each rule removes a specific source of measurement error.

- **One idea per item.** Double-barreled questions ("Was your care manager friendly and helpful?") can't be answered cleanly when the parts diverge. Split them.
- **Neutral, not leading or loaded.** Don't presuppose or steer ("How much did our excellent staff help you?"). State the object plainly.
- **Concrete, not vague.** Replace fuzzy quantifiers ("often", "regularly") with anchored ones ("in the last 6 months, how many times…"). Vague terms mean different frequencies to different people.
- **Match the respondent's language and literacy.** No jargon, program acronyms, or clinical terms the member wouldn't use. Write at the population's reading level.
- **Bound the reference period** for any recall item, and keep it realistic for memory.
- **Mutually exclusive, exhaustive options** for closed items; no overlap, no gaps.
- **Translation-readiness.** Avoid idioms, culture-bound concepts, and phrasings that depend on the source language's structure. CCSG's stock failures: an item built on "city blocks" breaks where neighborhoods aren't organized that way; a literal rendering can shift meaning entirely (an innocent English "adventures" becoming "amorous adventures" in French). If an item can't survive a faithful translation, flag it for **adaptation** (hand to `survey-translation-adaptation`).

For review, each bullet is a pass/fail check against every item; severity depends on how much the defect distorts the measure.

---

## 3. Response scales

The scale is half the measurement for attitudinal items.

- **Form:** rating (pick one position on an ordered scale), ranking (order a set), or frequency (how often). Match the form to the construct.
- **Balance:** equal positive and negative options around a clear midpoint. Unbalanced scales bias responses and, per a CCSG cross-cultural lesson, are especially fragile in translation — an inconsistently translated middle label like "fair" produced non-comparable distributions across countries.
- **Labeling:** label every point where feasible, not just the endpoints — fully labeled scales travel better across languages.
- **Points and midpoint:** decide the number of points and whether to offer a midpoint deliberately; document the choice.
- **Don't-know / not-applicable:** handle explicitly; its absence forces false answers, its presence can invite satisficing. Decide per item.
- **Consistency within a construct:** don't switch scale direction or length mid-construct.
- **Data type → analysis:** nominal vs. ordinal vs. interval/ratio determines what analysis is legitimate; coordinate with `survey-analysis` so the scale supports the intended statistics.

**3MC scale risks:** response styles differ systematically across cultural groups — acquiescence (a tendency toward "agree"/"yes") and extreme-response (favoring the endpoints) are documented to vary by group. Mitigate with balanced, fully labeled scales, and prefer construct-specific wording over generic agree/disagree where you can. Verify that translated labels carry **equivalent intensity**, not just dictionary-equivalent words.

---

## 4. Order and context

- **Priming:** earlier items shape later answers. Choose general-before-specific (or the reverse) on purpose, and hold the order constant across language versions — order effects appear to carry across cultures, so inconsistent ordering between versions injects comparison error.
- **Sensitive placement:** don't open cold with a sensitive item, and don't bury it where fatigue sets in.
- **Routing/filters:** keep skip logic clean; in interviewer or voice modes the routing must be unambiguous.

---

## 5. Sensitive and threatening questions

Sensitivity is **culturally variable** — an item that's routine in one group can be taboo in another (questions touching alcohol, family structure, immigration, income). CCSG is explicit that a topic innocuous in one culture may be offensive in another, so never assume neutrality across all your language groups.

- Reduce social-desirability pressure: normalize the behavior in the lead-in, allow self-administration for the most sensitive items, soften framing without leading. (For a small number of yes/no items, randomized-response techniques exist but are narrow in use.)
- For review: flag any item likely to be sensitive in *one* target group but not others. That asymmetry is both a nonresponse risk and a comparability risk — the groups effectively answer different questions.

---

## 6. Reuse before adapt, adapt before invent

Order of preference, because each step adds measurement risk (CCSG's three design strategies):

1. **Reuse** a validated item (search the instrument library; CAHPS/CG-CAHPS items come with known properties and existing translations).
2. **Adapt** an existing item when a literal version won't fit the population.
3. **Write new** only when nothing suitable exists — the most error-prone path, and the one that most needs pretesting.

Across languages this maps to three comparative approaches: **ask the same question and translate** (ASQT — standardizes the stimulus, but a close translation may not be culturally appropriate or even possible), **ask different questions** that tap the same underlying construct (ADQ — preserves meaning, but item-by-item comparison gets harder to justify), or a **mix**. The default for satisfaction work is mostly ASQT with targeted adaptation; the decision and its rationale belong in the documentation and run through `survey-translation-adaptation`.

---

## 7. Pretest — in every language, always

Questions aren't finished until they've been tested with real members. Cognitive interviewing surfaces inequivalence the design team can't see. Pretest each target language, not only the source — and note CCSG's point that even locales sharing the source language need a local review. The standing rule it quotes: if there are no resources to pilot, don't run the study. Make items as good as possible *before* pretesting (sections 0–6) so pretesting catches what nothing else could, rather than doing basic clean-up.

---

## How each consumer uses this file

- **Design:** sections 0–7 are the writing rules; produce items that already satisfy them.
- **Review:** convert each section into checks; cite the section a finding violates and rate it with `survey-instrument-review/references/severity-rubric.md`.
- **Instrument library:** tag every item with the §1 question type and the §3 scale form — that's the search vocabulary in `index.json`.

---

> Synthesized from the standard questionnaire-design canon (Sudman & Bradburn, *Asking Questions* / «Как правильно задавать вопросы», trans. Vinitskaya) and the CCSG Questionnaire Design and Study Design chapters (University of Michigan ISR, https://ccsg.isr.umich.edu/chapters/questionnaire-design/), tuned to healthcare member-satisfaction and 3MC contexts. Original synthesis — concepts paraphrased, not reproduced; consult the primary sources for full treatment and citations.
