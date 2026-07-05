# Adaptation vs. Translation

Literal translation is not enough for a survey. The goal is **measurement equivalence** — items that mean the same thing and measure the same construct across languages — not word-for-word correspondence. Apply with `../../../shared/3mc-considerations.md` (this is the 3MC core) and `../../../shared/question-quality.md`.

## The distinction
- **Translation** — render the source words in the target language.
- **Adaptation** — adjust wording, examples, and format so the *construct* and *response behaviour* transfer. Sometimes the best adaptation departs from the literal source (idioms, culturally specific referents, scale labels that don't map 1:1).
- Test: would a target-language respondent read the item the same way a source-language respondent does, and use the response scale the same way? If not, adapt.

## TRAPD (the working method)
A team-based process, not a solo translate-then-check:
- **T**ranslation — two or more independent parallel translations by qualified translators.
- **R**eview — translators + a survey methodologist review together.
- **A**djudication — a designated adjudicator decides the final version.
- **P**retesting — cognitive interviews / pilot with target-language respondents.
- **D**ocumentation — record every decision, alternative, and rationale (the audit trail).
Avoid back-translation as the *primary* check: it tests translator-to-translator fidelity, not whether target respondents understand the item. Use it only as a secondary diagnostic.

## Equivalence to watch
- **Semantic** — same meaning. **Conceptual** — the construct exists and is framed the same way. **Normative** — sensitivity/social-desirability differs by culture (health, immigration, family items land unevenly; see `question-quality.md` §5). **Measurement** — same scale behaviour; verify before pooling or comparing groups (analysis-side gate).
- Response scales: verbal labels (Never/Sometimes/Usually/Always) may not have equivalent-interval counterparts across languages — pretest them, don't assume.

## Provenance discipline
A validated source instrument stays tier-A **only in its validated languages**. A new-language rendering you produce is **draft / adapted, not validated** (`verbatim_ok=false`) until it clears TRAPD. Store it that way in `shared/instrument-library/` — never label a first-pass translation "validated". Where the official source already provides a validated target language (e.g., AHRQ Spanish CAHPS), prefer it over re-translating.
