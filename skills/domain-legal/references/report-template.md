# Legal Survey Report Templates (domain-specific)

Original report templates for survey-as-evidence work. **Grounded in the SIP information note (СП-21/15) and standard methodology, deliberately NOT modeled on any sample заключение** — the organizing logic here is original (a defensibility-first structure), so it reads differently from typical market reports while covering everything a court checks.

Two variants below: **A** a litigation/registry expert opinion (заключение), **B** an academic/methodological report. Both are built for **automated filling**: text in `{{double_braces}}` is a variable; `{{#each list}}…{{/each}}` is a repeating block (Mustache/Handlebars convention, pairs with a Node + `docx` generator). The field schema at the end lists every variable.

Word every questionnaire item per `../../../shared/question-quality.md`; satisfy the criteria in `admissibility.md`.

---

## Variant A — Expert opinion / заключение (defensibility-first)

The signature move: the report's spine is the **compliance map** (§3), where each admissibility criterion is answered up front. The examples bury method in a parameters table; here it's the backbone, so an opposing expert sees defensibility immediately.

```
ЗАКЛЮЧЕНИЕ № {{report_no}}
от {{report_date}}

Эксперт/специалист: {{expert_name}}, {{expert_credentials}}
Организация: {{org_name}}
Подготовлено для: {{client_or_court}} (дело {{case_no}})

1. ПРАВОВОЙ ВОПРОС И ПРЕДМЕТ  [legal question & subject — SIP 2.4]
   1.1 Поставленный вопрос: {{legal_question}}
   1.2 Исследуемое обозначение (как зарегистрировано/заявлено): {{designation}}
   1.3 Товары/услуги (классы МКТУ): {{goods_services}}
   1.4 Юридически значимая дата: {{relevant_date}}
       (если ретроспектива — обоснование в §6.4)

2. КРАТКИЕ ВЫВОДЫ  [findings first — answer the question]
   {{#each findings}}
   - {{this.statement}} — {{this.figure}}% (доверит. интервал ±{{this.ci}}%,
     за вычетом контрольной группы: {{this.net}}%)
   {{/each}}

3. КАРТА СООТВЕТСТВИЯ МЕТОДОЛОГИИ ТРЕБОВАНИЯМ  ★ unique section
   [each SIP criterion → how satisfied → where proven]
   | Критерий (СП-21/15) | Как обеспечено | Раздел |
   |---|---|---|
   | Целевая аудитория / средний потребитель | {{cm_universe}} | §4.1 |
   | Репрезентативность (соц-дем + география + случайность) | {{cm_repr}} | §4.2–4.4 |
   | Объём выборки и погрешность | {{cm_size}} | §4.2 |
   | Скрининг релевантной аудитории | {{cm_screening}} | §5.1 |
   | Открытые до подсказок + контрольные вопросы | {{cm_qtypes}} | §5.2 |
   | Отсутствие наводящих формулировок | {{cm_leading}} | §5.2 |
   | Нейтральность стимульных материалов | {{cm_stimuli}} | §5.3 |
   | Предмет = обозначение в привязке к товарам | {{cm_subject}} | §1.2–1.3 |
   | Временные параметры | {{cm_temporal}} | §6.4 |

4. ЦЕЛЕВАЯ АУДИТОРИЯ И ВЫБОРКА  [SIP 2.2]
   4.1 Определение целевой аудитории: {{universe_def}}
   4.2 Объём {{n_total}}; погрешность ±{{moe}}% при 95%; обоснование размера: {{size_rationale}}
   4.3 Социально-демографическая структура:
       {{#each demographics}}- {{this.var}}: {{this.distribution}}{{/each}}
   4.4 География (распределение по РФ): {{#each regions}}{{this.name}} (n={{this.n}}); {{/each}}
   4.5 Случайность отбора: {{randomness_method}}

5. ИНСТРУМЕНТАРИЙ  [SIP 2.3]
   5.1 Скрининговые вопросы: {{#each screeners}}{{this.text}}; {{/each}}
   5.2 Последовательность: открытые без подсказок → с подсказками → контрольные.
       {{#each questions}}- [{{this.type}}] {{this.text}}{{/each}}
   5.3 Стимульные материалы: {{stimuli_description}} (нейтральность: {{stimuli_neutrality}})

6. ПОЛЕВОЙ ЭТАП
   6.1 Режим: {{mode}}   6.2 Сроки: {{field_dates}}
   6.3 Подрядчик/интервьюеры и инструкции: {{fielding_party}}; {{interviewer_instructions}}
   6.4 Временное обоснование (для ретроспективы): {{temporal_rationale}}
   6.5 Контроль качества / параданные: {{qc_notes}}

7. РЕЗУЛЬТАТЫ  [detailed; test vs. control]
   {{detailed_results}}

8. ОГРАНИЧЕНИЯ  [honest limitations — strengthens, not weakens]
   {{limitations}}

9. ПРИЛОЖЕНИЯ  [reproducibility — an opposing expert must be able to re-run]
   - Полная анкета · стимульные материалы (exhibits) · инструкции интервьюерам
   - Описание массива данных (обезличенного) · сведения о квалификации эксперта
```

---

## Completeness checklist — required elements of a RF заключение

What a real, court-accepted заключение contains (genre/Rospatent-driven elements — use to verify any variant is complete; this is a checklist of *elements*, not borrowed wording):
- Титул: № and date, **УТВЕРЖДАЮ** block with the signatory's credentials.
- **Оглавление.**
- **Задачи, поставленные перед специалистами**, with an explicit **task ↔ questionnaire-item crosswalk** (each research task mapped to the anketa questions that answer it).
- **Основные выводы** in legal-conclusion phrasing (e.g., "присутствуют/отсутствуют социологические признаки широкой известности / различительной способности / ассоциации").
- **Параметры исследования** as a table: *Параметр · Краткое описание · Методическое обоснование* (method; objectivity safeguards; sample size; age/sex/education/occupation/income distributions; критерии отбора; география).
- **Проверка соответствия справке СИП** — table mapping each SIP thesis → "соответствует" + where shown (this is the §3 compliance map; real practice confirms it).
- **Результаты** with diagrams, split **«на настоящее время» vs «на даты в прошлом»** when retrospection matters (mirrors the SIP temporal requirement).
- **Приложения:** «Методика исследования», full anketa, stimulus exhibits, de-identified dataset description, signatory credentials.

## Variant A2 — Conventional заключение layout (court-familiar)

Same content as Variant A, but ordered the way courts/Rospatent expect to read it — for when familiarity beats novelty. Original boilerplate; automation-ready.

```
ЗАКЛЮЧЕНИЕ № {{report_no}} от {{report_date}}      УТВЕРЖДАЮ: {{signatory_block}}
ОГЛАВЛЕНИЕ {{toc}}

1. ЗАДАЧИ И ИХ СООТНЕСЕНИЕ С АНКЕТНЫМИ ВОПРОСАМИ
   {{#each tasks}}- Задача: {{this.task}} → вопросы: {{this.questions}}{{/each}}

2. ОСНОВНЫЕ ВЫВОДЫ
   {{#each findings}}- {{this.legal_phrasing}} ({{this.figure}}%, ±{{this.ci}}%; нетто {{this.net}}%){{/each}}

3. ПАРАМЕТРЫ ИССЛЕДОВАНИЯ   | Параметр | Краткое описание | Методическое обоснование |
   {{#each parameters}}| {{this.name}} | {{this.desc}} | {{this.rationale}} |{{/each}}
   (метод; объективность; объём {{n_total}}; возраст/пол/образование/занятость/доход; критерии отбора; география по РФ)

4. ПРОВЕРКА СООТВЕТСТВИЯ СПРАВКЕ СИП (СП-21/15)
   {{#each sip_theses}}| {{this.thesis}} | {{this.status}} | {{this.where}} |{{/each}}

5. РЕЗУЛЬТАТЫ  (диаграммы; разбивка «на настоящее время» / «на даты в прошлом»)
   {{detailed_results}}

6. ПРИЛОЖЕНИЯ: методика, анкета, стимульные материалы, описание массива, квалификация подписанта
```

Adds variables to the schema: signatory_block, toc, tasks[]{task, questions}, findings[].legal_phrasing, parameters[]{name, desc, rationale}, sip_theses[]{thesis, status, where}.

---

## Variant B — Academic / methodological report

For peer/scholarly audiences, grant deliverables, or publication. IMRaD-style — distinct in tone and structure from the заключение (no "УТВЕРЖДАЮ", no compliance map; instead theory, contribution, validity).

```
{{title}}
Аннотация / Abstract: {{abstract}}

1. Исследовательский вопрос и контекст: {{research_question}}; {{theoretical_framing}}
2. Методология: дизайн {{design}}; выборка {{sampling}}; инструмент {{instrument}};
   {{#if multilingual}}3MC: эквивалентность по языковым группам — {{equivalence_note}}{{/if}}
3. Результаты: {{results}} (таблицы/рисунки; значимость с учётом дизайна)
4. Обсуждение: {{discussion}} (сопоставление с литературой/бенчмарками)
5. Ограничения и валидность: {{validity}}
6. Выводы и вклад: {{contribution}}
Приложения / доступность данных: {{appendices}}
```

---

## Automation field schema

Generate from the structured project record (the orchestrator/analysis output), then render with a Node + `docx` pipeline. Groups:

- **case:** report_no, report_date, expert_name, expert_credentials, org_name, client_or_court, case_no
- **subject:** legal_question, designation, goods_services, relevant_date
- **findings[]:** statement, figure, ci, net
- **compliance_map:** cm_universe, cm_repr, cm_size, cm_screening, cm_qtypes, cm_leading, cm_stimuli, cm_subject, cm_temporal
- **sample:** universe_def, n_total, moe, size_rationale, demographics[]{var, distribution}, regions[]{name, n}, randomness_method
- **instrument:** screeners[]{text}, questions[]{type, text}, stimuli_description, stimuli_neutrality
- **fielding:** mode, field_dates, fielding_party, interviewer_instructions, temporal_rationale, qc_notes
- **results/limits:** detailed_results, limitations
- **academic (variant B):** title, abstract, research_question, theoretical_framing, design, sampling, instrument, multilingual, equivalence_note, results, discussion, validity, contribution, appendices

## Notes
- The compliance map (§3) is the differentiator and the automation anchor — every `cm_*` field is also an admissibility self-check; if one can't be filled, the survey isn't defensible yet.
- Keep PHI/respondent identifiers out; appendices describe the de-identified dataset, not the raw data.
- Original structure; do not paste layout/wording from sample заключения (third-party authored works). The completeness checklist and Variant A2 ordering were derived as *genre elements* (cross-checked against a real заключение) — element-level facts, not borrowed expression. Real practice confirms the SIP-compliance table (§3 / §4 of A2), so the compliance-map design is best practice, not idiosyncratic.
