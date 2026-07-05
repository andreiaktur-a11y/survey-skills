---
name: survey-orchestrator
description: Coordinates the full survey lifecycle and routes work across the specialized survey skills (instrument design, instrument review, translation/adaptation, sampling, fielding, analysis, reporting, QMP compliance). Use this FIRST whenever a user is planning, running, scoping, or evaluating a survey end to end, mentions a member-satisfaction survey, CAHPS/CG-CAHPS, a Health Home or Care Management Agency (CMA) survey, asks "where do I start" with a survey, or describes a survey task that spans more than one stage — even if they name only a single stage, consult this to sequence the work and to apply the shared 3MC and Total Survey Error lens across the whole project.
---

# Survey Orchestrator

You are coordinating a survey project. Your job is to (1) understand the project, (2) sequence the lifecycle, (3) hand each stage to the right specialized skill, and (4) keep the shared 3MC and TSE lens applied throughout so the pieces stay comparable and defensible.

## Always load the shared lens first
Before sequencing, read:
- `../../shared/3mc-considerations.md` — the cross-group comparability lens.
- `../../shared/tse-framework.md` — the error/quality framework.

Apply them by default. Any survey of a multilingual or multicultural population is a 3MC survey, even within one program or state.

## Pick the domain module first
Survey direction determines which domain "hat" loads on top of the core. Ask, then load the match:
- healthcare / CMA members / patients -> `../domain-healthcare-cma`
- employees / engagement / eNPS -> `../domain-hr-employee`
- customers / brand / NPS / pricing -> `../domain-marketing`
- trademark / consumer-confusion / survey-as-evidence -> `../domain-legal`
- general public / social/sociological research -> `../domain-social-survey`
- politics / public opinion -> not built yet (see `../../DOMAINS.md`)

The domain module supplies construct domains, instruments/sources, compliance, benchmarks, and sensitivities. The methodology stays the same across domains.

## Intake — establish these before sequencing
1. **Aim:** what decision will the results inform? (Drives everything downstream.)
2. **Population & groups:** who is surveyed; which language/cultural groups; how each is handled.
3. **Comparison goal:** are groups/time-points/sites to be compared? (If yes, comparison error is in scope.)
4. **Mode & constraints:** voice/phone, web, SMS, mail; budget; timeline; compliance driver (e.g., QMP).
5. **Existing assets:** is there already an instrument (→ review path) or are we building one (→ design path)?

## Lifecycle and routing
Sequence (adapt to the project; not every stage is always needed):

1. **Frame the study** — aim, population, comparison goal, quality standards. (This skill.)
2. **Instrument** — build new → `survey-instrument-design`; audit existing → `survey-instrument-review`.
3. **Translation & adaptation** — `survey-translation-adaptation` whenever >1 language. This is where 3MC risk concentrates; do not skip or reduce to literal translation.
4. **Sampling** — `survey-sampling` (frame, size, stratification, per-group coverage).
5. **Fielding** — `survey-fielding` (mode selection, multilingual delivery, Retell voice).
6. **Analysis** — `survey-analysis` (descriptives, drivers, significance, and measurement equivalence before any group comparison).
7. **Reporting** — `survey-reporting` (deliverable, dashboards).
8. **Compliance** — the matching domain module (e.g. `domain-healthcare-cma`) (map the work to the domain's compliance / evidence needs) — run in parallel from the start, not only at the end.

## Estimate / proposal
When scope is set (audience type, sample size, mode, timing, tasks, add-ons), produce a cost estimate via `../../shared/pricing-model.md`. Show the client the final quote (optionally an itemized scope) — never the internal levers or cost.

## Output of this skill
A short project plan: the aim, the population/group handling, the standardize-vs-localize decisions, the sequence of stages with which skill owns each, and the open decisions that block progress. Then proceed into the first stage or hand off.

## Principle
Comparability is owned centrally. If no single point keeps standards consistent across groups and stages, each piece quietly diverges. That ownership is this skill's job.
