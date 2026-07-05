# Instrument Flow

How items are ordered, routed, and framed into a coherent questionnaire. Item wording lives in `../../../shared/question-quality.md`; this file is about sequence and structure. For legal surveys, order is also an admissibility issue (`../../domain-legal/references/admissibility.md`: open before aided).

## Order
- **Screeners / eligibility first** — admit the right respondents without revealing the survey's aim (esp. legal).
- **Easy, engaging, non-threatening items early** — build rapport before harder or sensitive content.
- **Group by topic**, move general → specific within a topic. For attitude/confusion work, **open/unaided before aided/closed** so early items don't cue later answers.
- **Sensitive items late** (health, income, immigration, demographics) — after rapport, before fatigue ends the session. Demographics typically last unless needed for routing.
- **Overall rating placement:** ask the global rating (e.g., provider 0–10) before drilling into specific complaints, so it isn't anchored by just-recalled negatives.

## Routing / skips
- Gate low-frequency or conditional items behind a filter question (e.g., "did you see a specialist?" → specialist items).
- Keep skip logic explicit and testable; every path must terminate cleanly. Follow the source instrument's own skip instructions when reusing validated items (see the placement notes in library banks).
- Minimize respondent-visible branching in self-administered modes; handle it programmatically.

## Length & mode
- Match length to mode and population: **voice/phone (common for CMA) must be short with clean routing** — no long option lists read aloud; prefer ≤4-point verbal scales and yes/no gates. Split-load or defer low-priority items rather than bloat.
- Keep response scales consistent within a block so respondents aren't re-learning the scale each item.
- 3MC: verify flow works in **every** language version — skip logic, scale direction, and sensitive-item placement can shift across cultures (`../../../shared/3mc-considerations.md`).

## Reuse assembly
When building from validated banks: keep each source composite's core items together and intact (dropping CAHPS core items forfeits the name/comparability), respect documented placement/skip rules, and note where a supplemental set attaches to the core.
