---
name: survey-fielding
description: Plan and run data collection — choose the mode(s) (voice/phone incl. IVR and AI voice, web, SMS, mail, face-to-face), decide single-mode vs. mixed-mode, deliver the survey in multiple languages, and set up AI voice calling (e.g., Retell). Use whenever a user asks how to administer or send out a survey, which mode to use, how to reach respondents in different languages, how to run phone or voice surveys, how to boost response rates, or how to wire up automated calling. Apply the shared 3MC lens because mode and language interact with comparability.
---

# Survey Fielding

Get the instrument to respondents and responses back, with mode and language choices that don't wreck comparability.

## Load first
- `../../shared/3mc-considerations.md` — mode and language assignment are 3MC design decisions.
- `../../shared/tse-framework.md` — mode affects measurement and nonresponse.

## Workflow
1. **Mode selection** (`references/mode-selection.md`): match mode to population, frame, questionnaire length/complexity, sensitivity, and budget. There is no single best mode — choose on time/cost/error tradeoffs.
2. **Mixed-mode decision:** mixed-mode can cut cost and nonresponse but adds mode effects and harmonization burden — and, across groups, can confound mode with culture. Decide deliberately; if comparing groups, prefer holding mode constant or measuring the mode effect.
3. **Language delivery:** apply the language-assignment rule from design (not ad hoc). Ensure every targeted language has a working instrument and a capable interviewer/voice.
4. **AI voice setup** (`references/voice-retell.md`): Retell configuration, per-language voices/prompts, latency and handoff, capturing paradata (call outcomes, timing) for quality control.
5. **Paradata:** capture contact attempts, outcomes, timings — needed for nonresponse analysis and QC.

## Output
A fielding plan: mode(s) and the mixed-mode decision with rationale, per-language delivery setup, contact protocol, and the paradata to capture. For voice, the Retell configuration outline.

## References
- `references/mode-selection.md` — mode tradeoffs and the mixed-mode decision.
- `references/voice-retell.md` — AI voice calling setup and multilingual delivery.
