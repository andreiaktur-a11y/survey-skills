// Measure & Meaning — Employee Engagement & Retention SAMPLE report v2 (expanded, per-module viz)
// All data illustrative + synthetic. Fictional org: Northgate Components, Inc.
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, PageBreak,
  Footer, Header, PageNumber, TabStopType, LevelFormat, convertInchesToTwip,
} = require("docx");

// brand
const NAVY = "0B1F3A", TEAL = "0EA5A3", TEALI = "0B7472", CORAL = "FF6A5C",
      CORALI = "C7402F", SAGE = "7FA58F", PAPER = "F3F5F6", STONE = "E2E7EB";
const HEAD = "Poppins SemiBold", BODY = "Inter";

const img = (p, w, h) => new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 120, after: 60 },
  children: [new ImageRun({ type: "png", data: fs.readFileSync(p), transformation: { width: w, height: h } })],
});
const cap = (t) => new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { after: 200 },
  children: [new TextRun({ text: t + "  ·  Illustrative, synthetic data.", font: BODY, size: 17, italics: true, color: "5A6B7E" })],
});
const P = (t, o = {}) => new Paragraph({
  spacing: { after: o.after ?? 140, before: o.before ?? 0 },
  alignment: o.align,
  children: (Array.isArray(t) ? t : [{ text: t }]).map(r => new TextRun({
    font: BODY, size: o.size ?? 21, color: r.color ?? NAVY, bold: r.bold, italics: r.italics, text: r.text,
  })),
});
const H1 = (num, t) => new Paragraph({
  heading: HeadingLevel.HEADING_1, spacing: { before: 320, after: 160 },
  children: [
    new TextRun({ text: num + "  ", font: HEAD, size: 30, color: TEALI }),
    new TextRun({ text: t, font: HEAD, size: 30, color: NAVY }),
  ],
});
const H2 = (t) => new Paragraph({
  heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 120 },
  children: [new TextRun({ text: t, font: HEAD, size: 24, color: NAVY })],
});
const bullet = (t, ref = "bl") => new Paragraph({
  numbering: { reference: ref, level: 0 }, spacing: { after: 100 },
  children: (Array.isArray(t) ? t : [{ text: t }]).map(r => new TextRun({
    font: BODY, size: 21, color: r.color ?? NAVY, bold: r.bold, italics: r.italics, text: r.text,
  })),
});
const callout = (title, body, color = TEALI) => new Table({
  width: { size: 9360, type: WidthType.DXA }, columnWidths: [9360],
  borders: noBorders({ left: { style: BorderStyle.SINGLE, size: 18, color } }),
  rows: [new TableRow({ children: [new TableCell({
    width: { size: 9360, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: PAPER },
    margins: { top: 120, bottom: 120, left: 200, right: 160 },
    children: [
      new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: title, font: HEAD, size: 19, color })] }),
      ...(Array.isArray(body) ? body : [body]).map(b => new Paragraph({
        spacing: { after: 40 },
        children: (Array.isArray(b) ? b : [{ text: b }]).map(r => new TextRun({ font: BODY, size: 19, color: r.color ?? NAVY, bold: r.bold, italics: r.italics, text: r.text })),
      })),
    ],
  })] })],
});
function noBorders(overrides = {}) {
  const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  return { top: none, bottom: none, left: none, right: none, insideHorizontal: none, insideVertical: none, ...overrides };
}
// data table helper
function dataTable(headers, rows, widths, opts = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const mkCell = (txt, i, isHead, rowShade, bold, color) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: isHead ? NAVY : (rowShade ? PAPER : "FFFFFF") },
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    verticalAlign: "center",
    children: [new Paragraph({
      alignment: i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER,
      children: [new TextRun({
        text: String(txt), font: BODY, size: isHead ? 18 : 19,
        bold: isHead || bold, color: isHead ? "FFFFFF" : (color ?? NAVY),
      })],
    })],
  });
  return new Table({
    width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    borders: noBorders({ insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: STONE } }),
    rows: [
      new TableRow({ tableHeader: true, children: headers.map((h, i) => mkCell(h, i, true)) }),
      ...rows.map((r, ri) => new TableRow({
        children: r.cells.map((c, i) => mkCell(c, i, false, ri % 2 === 1, r.bold, r.colors ? r.colors[i] : undefined)),
      })),
    ],
  });
}
const spacer = (h = 120) => new Paragraph({ spacing: { after: h }, children: [] });

// ============================== COVER ==============================
const cover = [
  new Paragraph({
    spacing: { before: 200, after: 60 },
    children: [new TextRun({ text: "MEASURE & MEANING RESEARCH", font: HEAD, size: 22, color: TEALI })],
  }),
  new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: TEAL } },
    spacing: { after: 480 }, children: [],
  }),
  new Paragraph({
    spacing: { after: 100 },
    children: [new TextRun({ text: "SAMPLE REPORT", font: HEAD, size: 20, color: CORALI })],
  }),
  new Paragraph({
    spacing: { after: 160 },
    children: [new TextRun({ text: "Employee Engagement & Retention Census", font: HEAD, size: 52, color: NAVY })],
  }),
  new Paragraph({
    spacing: { after: 520 },
    children: [new TextRun({
      text: "What predicts leaving — and which levers give the most retention per dollar. Annual census, all-employee population, Wave 1 baseline.",
      font: BODY, size: 26, color: "44546A",
    })],
  }),
  new Table({
    width: { size: 9360, type: WidthType.DXA }, columnWidths: [1900, 7460],
    borders: noBorders({ insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: STONE } }),
    rows: [
      ["Prepared for", "Northgate Components, Inc. — a fictional mid-size US manufacturer (illustrative)"],
      ["Prepared by", "Andrei Akhtyrskii, PhD — Measure & Meaning Research"],
      ["Fieldwork", "May 4 – May 22, 2026 (synthetic dates)"],
      ["Version", "Sample v2 · July 2026"],
    ].map(([k, v]) => new TableRow({
      children: [
        new TableCell({
          width: { size: 1900, type: WidthType.DXA }, margins: { top: 90, bottom: 90, left: 0, right: 110 },
          children: [new Paragraph({ children: [new TextRun({ text: k, font: HEAD, size: 19, color: TEALI })] })],
        }),
        new TableCell({
          width: { size: 7460, type: WidthType.DXA }, margins: { top: 90, bottom: 90, left: 110, right: 0 },
          children: [new Paragraph({ children: [new TextRun({ text: v, font: BODY, size: 20, color: NAVY })] })],
        }),
      ],
    })),
  }),
  spacer(500),
  callout("About this document", [
    [{ text: "This is a sample deliverable. ", bold: true },
     { text: "Every number, chart, organization name, and quotation in it is synthetic — generated to illustrate the structure, analysis standards, and decision framing of a Measure & Meaning employee census report. No real client data appear anywhere in this document." }],
    [{ text: "Instrumentation: all survey items referenced here are original Measure & Meaning formulations (IP tier A); provenance is documented in Appendix A." , italics: true }],
  ], CORALI),
];

// ============================== 01 EXEC SUMMARY ==============================
const exec = [
  H1("01", "Executive summary"),
  P([{ text: "The decision this study supports: ", bold: true },
     { text: "voluntary turnover at Northgate rose from 14% to 21% in twelve months, concentrated in production roles. Leadership must decide where to spend a limited retention budget in FY-27. This census answers what actually predicts leaving — not what is loudest — and sequences the levers by cost." }]),
  bullet([{ text: "Engagement is uneven, not low. ", bold: true },
    { text: "The organization averages 65 on a 0–100 index, but Warehouse & Logistics (61) and Production (64) sit meaningfully below Engineering (74). The problem is concentrated, so the response should be too. (Fig. 1)" }]),
  bullet([{ text: "eNPS is −3 overall and −12 to −17 in the two frontline units ", bold: true },
    { text: "— the workforce is closer to warning peers off than recommending. Small-unit scores carry wide confidence intervals and are flagged as such. (Fig. 2)" }]),
  bullet([{ text: "Four conditions fall in the action zone ", bold: true },
    { text: "— high importance, low satisfaction: pay fairness, sustainable workload, career growth, and communication. Team relationships and safety are strengths to protect, not investment targets. (Fig. 3–4)" }]),
  bullet([{ text: "Burnout risk is demand-driven, not resilience-driven. ", bold: true },
    { text: "31% of the 3–7-year tenure band screens elevated; Production and Warehouse combine high demand with poor recovery. The fix is workload math — staffing, scheduling, overtime — not wellness programming. (Fig. 5–6)" }]),
  bullet([{ text: "The driver model reorders the priority list. ", bold: true },
    { text: "Stated importance puts pay and job security on top; the model of who actually intends to stay puts career growth first, with recognition, communication, and feedback — three low-cost levers — jointly explaining about 20% of retention variance. (Fig. 8–9)" }]),
  spacer(60),
  callout("Recommendation", [
    [{ text: "Sequence the retention budget in three tiers: " },
     { text: "(1) deploy the low-cost levers now — recognition practice, leadership communication rhythm, feedback clarity — in Production and Warehouse first; (2) fund the structural fixes — staffing-model review for sustainable workload and visible technical career paths; (3) commission a targeted pay-equity and market-benchmark study before making across-the-board pay moves. Re-measure with a 5-minute pulse in Q4 against this baseline.", bold: true }],
  ]),
];

// ============================== 02 BACKGROUND ==============================
const background = [
  H1("02", "Background and objectives"),
  P("Northgate Components employs approximately 1,240 people across two production sites and a headquarters office. Exit interviews and manager escalations pointed to workload and pay as the causes of rising turnover — but exit data describe leavers, are collected at the worst possible moment, and cannot rank causes. Leadership commissioned a full census to establish a defensible baseline before allocating the FY-27 retention budget."),
  P("The study was designed to resolve five questions, each mapped to a survey module:"),
  dataTable(["#", "Objective (question the analysis resolves)", "Module"], [
    { cells: ["1", "How engaged is the workforce, and where is engagement uneven?", "CORE"] },
    { cells: ["2", "Would employees recommend Northgate as a place to work — and what moves that?", "NPS"] },
    { cells: ["3", "Which working conditions matter most, and where do we under-deliver on what matters?", "GAP"] },
    { cells: ["4", "Where is burnout risk concentrated — and is it demand-driven or recovery-driven?", "BRN"] },
    { cells: ["5", "What actually predicts intent to stay, and which levers are cheapest per point of retention?", "STAY"] },
  ], [560, 6900, 1900]),
  spacer(),
  P([{ text: "Open-ended responses (module OPEN) cut across all five objectives and are reported in §4.5.", italics: true }]),
];

// ============================== 03 METHOD ==============================
const method = [
  H1("03", "Method and sample"),
  H2("Design and instrument"),
  P("Anonymous online census of all employees; kiosk stations provided on production floors for employees without company email. Median completion time 13.4 minutes. The instrument combined six modules (CORE engagement, eNPS, importance × satisfaction matrix, burnout screen, retention intent, open-ended), 74 closed items plus three open-ends. All items are original Measure & Meaning formulations; item IDs, scales, and provenance are documented in Appendix A."),
  P([{ text: "Scales. " , bold: true },
     { text: "Agreement items use a 5-point Likert scale. Importance and satisfaction are each rated on 7-point, fully verbalized scales; satisfaction items offer an off-scale “Not applicable / no experience with this” option, excluded from means and reported as a coverage statistic (Appendix A explains the rationale). eNPS uses the canonical 0–10 scale." }]),
  H2("Sample and coverage"),
  dataTable(["Unit", "Invited", "Completed", "After screening", "Response rate", "MoE (95%)"], [
    { cells: ["Production", "648", "531", "512", "82%", "±2.0 pp"] },
    { cells: ["Warehouse & Logistics", "203", "174", "168", "86%", "±3.1 pp"] },
    { cells: ["Engineering", "108", "96", "94", "89%", "±3.6 pp"] },
    { cells: ["Sales & Customer Ops", "96", "83", "81", "86%", "±4.2 pp"] },
    { cells: ["Quality", "61", "54", "52", "89%", "±5.2 pp"] },
    { cells: ["Finance & Admin", "55", "48", "46", "87%", "±5.8 pp"] },
    { cells: ["IT", "31", "25", "24", "81%", "±9.5 pp"] },
    { cells: ["HR", "14", "11", "10", "79%", "±16.6 pp"] },
    { cells: ["Total", "1,216", "1,022", "987", "84%", "±1.3 pp"], bold: true },
  ], [2600, 1250, 1400, 1750, 1500, 1350]),
  cap("Exhibit 1. Achieved sample by unit"),
  P([{ text: "Weighting. ", bold: true },
     { text: "Results are weighted to payroll records by department × tenure band × role level to correct nonresponse skew (production shift workers responded at a lower rate than office staff). Weights range 0.71–1.58; the scheme is documented in Appendix C. All figures in this report are weighted unless labeled otherwise." }]),
  H2("Data-quality screening (applied before any analysis)"),
  P("Screening rules were pre-registered in the technical appendix and applied uniformly. This disclosure is standard in every Measure & Meaning report:"),
  dataTable(["Screen", "Rule", "Flagged", "Excluded"], [
    { cells: ["Speeding", "< ⅓ of median completion time flag; sustained < 2 s/item exclude", "41", "17"] },
    { cells: ["Straightlining", "Zero variance across ≥ 20 consecutive matrix items flag; + speeding exclude", "29", "11"] },
    { cells: ["Attention checks", "2 embedded items; one failure flag, two exclude", "23", "7"] },
    { cells: ["Kiosk proxy review", "Response-time clustering on shared devices reviewed manually", "6", "0"] },
    { cells: ["Total excluded (unique respondents)", "", "", "35 (3.4%)"], bold: true },
  ], [2300, 4750, 1100, 1300]),
  cap("Exhibit 2. Screening funnel: 1,022 completed → 987 analyzed"),
  callout("Anonymity threshold", [
    [{ text: "No result is reported for any group of fewer than 5 respondents. " , bold: true },
     { text: "Suppressed cells are shown as “n/a (below reporting threshold)” — never silently dropped. Open-ended quotations are paraphrased where verbatim wording could identify the author." }],
  ]),
];

// ============================== 04 RESULTS ==============================
const results = [
  H1("04", "Results by objective"),
  H2("4.1 · Engagement: uneven, and concentrated where turnover is (CORE)"),
  P([{ text: "The engagement index (mean of six agreement items, rescaled 0–100) averages 65.4 weighted. " },
     { text: "The story is not the average but the spread: ", bold: true },
     { text: "Engineering (74) and the smaller office functions sit comfortably above it, while Warehouse & Logistics (61) and Production (64) — 69% of headcount and the locus of the turnover increase — sit below." }]),
  img("figs/fig1_core.png", 620, 302),
  cap("Fig. 1. Engagement index by unit vs. organization average (weighted, n=987)"),
  P([{ text: "Reading note: ", italics: true },
     { text: "the index is a formative composite for tracking and comparison, not a clinical measure; wave-over-wave comparison requires identical wording and comparable fielding windows.", italics: true }]),

  H2("4.2 · Willingness to recommend: eNPS −3, dragged by the frontline (NPS)"),
  P("Employee Net Promoter Score is % promoters (9–10) minus % detractors (0–6) on the 0–10 recommendation scale. The organization scores −3: for every promoter there is slightly more than one detractor."),
  img("figs/fig2_enps.png", 620, 319),
  cap("Fig. 2. Promoter / passive / detractor shares and eNPS by unit (weighted)"),
  P([{ text: "Two disclosures we make in every report. ", bold: true },
     { text: "First, the mean score (6.4) is reported only as a secondary statistic — the mean and the index can move in opposite directions (detractors softening from 2 to 5 raises the mean and leaves eNPS unchanged), and any divergence is explained, not hidden. Second, small segments produce unstable eNPS: a 24-person unit moves ±8 points on one changed answer, which is why every segment score carries a confidence interval." }]),

  H2("4.3 · What matters vs. what we deliver: the gap map (GAP)"),
  P("Each of 18 working conditions was rated twice — importance when choosing an employer, and satisfaction in the current role (7-point scales; “not applicable” available on satisfaction and excluded from means). Plotting the two against each other separates what to fix from what to protect. Quadrant boundaries are the within-survey medians, not scale midpoints — this is disclosed because it affects interpretation: quadrants describe relative position in this workforce, this wave."),
  img("figs/fig3_gap_quadrant.png", 560, 436),
  cap("Fig. 3. Importance × satisfaction, 18 conditions (weighted means; codes in Appendix A)"),
  P([{ text: "Four conditions land in the action zone: " , bold: true },
     { text: "pay fairness (PAY), sustainable workload (WKL), career growth (GRW), and communication & information (COM). Voice & participation (VOI) and recognition (REC) sit just outside it with below-median satisfaction. Team relationships (TEA), workplace safety (SAF), and the manager relationship (MGR) are strengths — the recommendation section treats them as assets to protect, not targets for new spending." }]),
  img("figs/fig4_gap_rank.png", 620, 419),
  cap("Fig. 4. Gap score (importance − satisfaction), ranked; gaps ≥ 1.3 highlighted"),
  P([{ text: "Coverage note: ", bold: true },
     { text: "8% of respondents selected “not applicable” on the benefits satisfaction item (mostly employees under 90 days, not yet benefits-eligible) and 3% on learning & development. These responses are excluded from the means above and reported here rather than recoded to the midpoint." }]),

  H2("4.4 · Burnout risk: demand-driven, concentrated mid-tenure (BRN)"),
  P("The burnout module is an organizational risk screen — six items covering exhaustion, recovery, disengagement, and sustainability — reported only at segment level. It is not a clinical assessment and produces no individual feedback. Respondents are assigned to low / moderate / elevated tiers by pre-set cutpoints on the summed score (cutpoint logic in Appendix A)."),
  img("figs/fig5_brn_tiers.png", 570, 285),
  cap("Fig. 5. Burnout risk tiers by tenure band (weighted)"),
  P([{ text: "Risk peaks at 3–7 years of tenure (31% elevated), not among newcomers — " , bold: true },
     { text: "the employees who carry the most institutional knowledge and are most expensive to replace. By unit, elevated-tier share ranges from 12% (Finance & Admin) to 29% (Production); the night-shift Quality cell (n=4) is n/a (below reporting threshold)." }]),
  P("The screen separates two mechanisms: demand (energy depletion, unsustainable workload) and recovery (whether normal rest restores capacity). Units in the lower-right of Fig. 6 need structural workload intervention; resilience or wellness programming does not fix a staffing-model problem."),
  img("figs/fig6_brn_2x2.png", 540, 413),
  cap("Fig. 6. Demand load vs. recovery adequacy by unit (bubble size = n)"),

  H2("4.5 · What employees say in their own words (OPEN)"),
  P("Three open-ended items were coded thematically by two coders with adjudication (94% initial agreement). Themes are cross-tabulated by promoter class — what detractors want changed, and what promoters insist must not change:"),
  img("figs/fig9_open_themes.png", 620, 335),
  cap("Fig. 7. Theme frequency among detractors vs. promoters (multi-code; “keep” themes from OPN-02)"),
  P([{ text: "Two paraphrased responses illustrate the dominant pair of themes " },
     { text: "(paraphrased to protect anonymity; role metadata shown only where the cell exceeds the reporting threshold):", italics: true }]),
  callout("From the open-ended responses (paraphrased, synthetic)", [
    [{ text: "“We keep being asked to cover extra shifts because positions stay unfilled — the overtime pay is fine, the pace is not.” ", italics: true }, { text: " — Production, 3–7 yrs" }],
    [{ text: "“Whatever changes, don’t break the crews. The team is why people stay as long as they do.” ", italics: true }, { text: " — Warehouse & Logistics, 7+ yrs" }],
  ], SAGE.replace("#", "") === SAGE ? SAGE : SAGE),
];

// ============================== 05 DRIVERS ==============================
const drivers = [
  H1("05", "Driver analysis: what actually predicts staying"),
  P([{ text: "This section is the differentiator of the report. " , bold: true },
     { text: "Sections 4.1–4.3 describe the workforce; this section models it. The criterion is intent to stay (STY-01, “I expect to still be working at this organization twelve months from now”), validated against overall satisfaction (SAT-00) as a secondary criterion." }]),
  P("The analysis proceeds in two disclosed steps. First, transparent bivariate rank correlations between each condition and intent to stay — readable by any stakeholder. Second, because the predictors are intercorrelated (pay fairness correlates with recognition; workload with schedule fit), raw correlations over-credit redundant drivers. A Shapley-value decomposition allocates the model’s explained variance fairly across correlated predictors."),
  img("figs/fig7_stay_drivers.png", 620, 385),
  cap("Fig. 8. Share of explained variance in intent to stay, with cost-to-address tags (model R² = 0.47)"),
  callout("Significance ≠ importance", [
    [{ text: "At census scale (n=987), nearly every correlation is statistically significant — significance is a function of sample size, not practical relevance. " },
     { text: "This report therefore ranks drivers by effect size and never presents unadjusted significance matrices in client-facing sections; the full matrix, with a multiple-comparison note, lives in Appendix D.", bold: true }],
  ]),
  P([{ text: "Stated vs. derived importance disagree — and the disagreement is the finding. " , bold: true },
     { text: "Asked directly, employees rank pay, safety, and job security highest. Modeled against actual intent to stay, career growth moves from 7th to 1st, and job security falls from 3rd to 7th — security matters enormously in the abstract but does not differentiate stayers from leavers at Northgate, where layoffs are not a live fear. Both rankings are shown because the divergence is informative, not an error:" }]),
  img("figs/fig8_stated_derived.png", 560, 384),
  cap("Fig. 9. Stated importance rank vs. model-derived driver rank (top 10)"),
  P([{ text: "The retention-per-dollar reading: " , bold: true },
     { text: "recognition, communication, and feedback jointly account for roughly 20% of explained variance and are the cheapest levers on the board — process and management-practice changes, not budget lines. Career growth and workload are structural and mid-cost. Pay is a real driver but the most expensive lever per point; it warrants a targeted equity study, not an across-the-board adjustment on this evidence." }]),
];

// ============================== 06 ACTIONS ==============================
const actions = [
  H1("06", "Recommended actions"),
  P("Sequenced by expected retention impact per dollar, using the driver model (Fig. 8), the gap map (Fig. 3), and the burnout mechanism split (Fig. 6). Each action names its evidence."),
  H2("Now — low-cost levers (this quarter)"),
  bullet([{ text: "Stand up a structured recognition practice in Production and Warehouse ", bold: true }, { text: "(REC: 8.3% of driver variance, largest low-cost lever; detractor theme #6). Manager-led, specific, weekly cadence — not an awards program." }]),
  bullet([{ text: "Fix the leadership communication rhythm ", bold: true }, { text: "(COM: action-zone gap −1.4; 6.9% of variance; detractor theme #4). Monthly all-hands with a standing “what changed and why” segment; shift-start briefings on the floor." }]),
  bullet([{ text: "Make evaluation criteria explicit ", bold: true }, { text: "(FDK: 5.2% of variance). Every employee should be able to answer “how is my work judged and what would improve it.”" }]),
  H2("Next — structural fixes (2–3 quarters)"),
  bullet([{ text: "Commission the staffing-model review for Production and Warehouse ", bold: true }, { text: "(WKL: action zone, 11.8% of variance; burnout is demand-driven in exactly these units — Fig. 6; staffing is detractor theme #2). Target: reduce sustained overtime dependence, not add resilience training." }]),
  bullet([{ text: "Publish technical career paths ", bold: true }, { text: "(GRW: #1 derived driver at 16.2%; action zone). Dual-ladder design so growth does not require leaving the tools or the site." }]),
  H2("Then — evidence before spending (before FY-27 budget close)"),
  bullet([{ text: "Run a targeted pay-equity and market-benchmark study ", bold: true }, { text: "(PAY: #2 driver, widest gap at −2.3, and the most expensive lever). The census shows pay fairness perception is a problem; it cannot show whether the fix is levels, structure, or transparency. Do not make across-the-board moves on perception data alone." }]),
  bullet([{ text: "Protect the strengths: ", bold: true }, { text: "team cohesion and safety practice are the top “do not change” themes among promoters. Any reorganization of crews should be tested against this finding." }]),
  spacer(),
  callout("Measurement follow-up", [
    [{ text: "Re-field a 5-minute pulse (CORE-short + eNPS + one open-end) in Q4 2026 against this baseline. Identical wording, comparable fielding window. Movement of ±3 index points at org level is within noise; read direction at unit level." }],
  ]),
];

// ============================== 07 LIMITATIONS ==============================
const limitations = [
  H1("07", "Limitations"),
  bullet("Cross-sectional design: the driver model identifies predictive association at one point in time, not proven causation. The Q4 pulse and Wave 2 census will test whether movement on the levers precedes movement in intent to stay."),
  bullet("Intent to stay is a proxy for retention. It is the strongest survey-measurable predictor of voluntary turnover, but linkage to actual exit records (a Wave 2 option, subject to the anonymity protocol) would strengthen the model."),
  bullet("Self-report burnout screen: tiers indicate where organizational intervention should be prioritized; they are not diagnoses and are never reported below segment level."),
  bullet("Stated importance reflects what employees can and will articulate; derived importance reflects statistical association. Both are shown; neither is treated as ground truth alone."),
  bullet("Small units (IT n=24, HR n=10) carry wide intervals; their scores are directional. One cell (night-shift Quality, n=4) is suppressed under the reporting threshold."),
  bullet("First wave: no internal trend exists yet. External benchmarks are not used — cross-vendor benchmark databases differ in items, scales, and populations, and comparisons against them are not defensible. The baseline standard here is internal comparison across units and waves."),
];

// ============================== APPENDIX ==============================
const appendix = [
  H1("A–D", "Appendices"),
  H2("Appendix A · Instrument provenance and scales (summary)"),
  P("All items fielded in this study are original Measure & Meaning formulations (IP tier A). The engagement, burnout, and importance–satisfaction spaces are occupied by well-known proprietary and academic instruments (e.g., Gallup Q12 — proprietary; UWES, OLBI — academic with license terms; MBI, PCQ — proprietary via Mind Garden). No wording from any of these instruments is used; where a construct space is shared, structural inspiration is acknowledged generically. The full item bank with stable IDs (ENG-01…06, NPS-01/02, SAT-00, GAP-xxx-I/S ×18, BRN-01…06, STY-01…03, OPN-01…03) is maintained in the engagement codebook."),
  dataTable(["Module", "Items", "Scale", "Index rule (disclosed)"], [
    { cells: ["CORE", "6", "5-pt agreement", "Mean of 6, rescaled 0–100"] },
    { cells: ["NPS", "1 + open", "0–10 canonical", "% promoters − % detractors; mean secondary"] },
    { cells: ["GAP", "18 × 2 + SAT-00", "7-pt verbalized; N/A off-scale on satisfaction", "Quadrants at within-survey medians; gap = I − S"] },
    { cells: ["BRN", "6 (2 reverse-keyed)", "5-pt agreement", "Tiers by pre-set cutpoints on summed score"] },
    { cells: ["STAY", "3", "5-pt / categorical", "STY-01 criterion; Shapley decomposition"] },
    { cells: ["OPEN", "3", "open text", "Dual-coder thematic coding, adjudicated"] },
  ], [1100, 1750, 3350, 3160]),
  spacer(),
  P([{ text: "Why 7-point verbalized scales for the GAP matrix: ", bold: true },
     { text: "satisfaction is bipolar — a neutral state is a real position, and forcing a direction manufactures signal; importance is unipolar — the fully labeled midpoint (“moderately important”) is a level, not an escape hatch. An odd scale also yields a stable within-survey median, which defines the quadrant boundaries; on an even scale those boundaries fall between categories and drift between waves. Midpoint share is monitored as a satisficing indicator alongside straightlining." }]),
  H2("Appendix B · Screening rules (pre-registered)"),
  P("Speeders: completion < ⅓ of median → flag; sustained < 2 s per item → exclude. Straightliners: zero variance across ≥ 20 consecutive matrix items → flag; combined with speeding → exclude. Attention checks: one per ~50 items (“For data quality purposes, please select ‘Agree’”); one failure → flag, two → exclude. Shared kiosk devices: identical device signatures acceptable by design; response-time clustering reviewed for proxy completion. Funnel: 1,022 → 987 (3.4% excluded), reported by segment in Exhibit 2."),
  H2("Appendix C · Weighting"),
  P("Rim weighting to payroll records on department × tenure band × role level. Category sets mirror HRIS categories by design, which is what makes payroll weighting possible. Weight range 0.71–1.58; design effect 1.06; effective n = 931. Unweighted results available in the crosstab workbook."),
  H2("Appendix D · Statistical notes"),
  P("Driver model: OLS on standardized predictors, criterion STY-01; R² = 0.47; Shapley decomposition over the 14-predictor set (10 shown, remainder pooled). Full bivariate matrix with Holm-adjusted p-values in the crosstab workbook — omitted from the body per the significance ≠ importance standard. eNPS intervals: Wald 95% on the promoter–detractor difference. Suppression: all cells n < 5."),
  spacer(300),
  new Paragraph({
    border: { top: { style: BorderStyle.SINGLE, size: 6, color: STONE } },
    spacing: { before: 120, after: 0 },
    children: [new TextRun({
      text: "Measure & Meaning Research · measuremeaning.com · This sample report contains only illustrative, synthetic data and a fictional organization.",
      font: BODY, size: 17, color: "5A6B7E",
    })],
  }),
];

// ============================== DOC ==============================
const doc = new Document({
  numbering: {
    config: [{
      reference: "bl",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "—", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 240 } }, run: { color: TEALI } },
      }],
    }],
  },
  styles: {
    default: { document: { run: { font: BODY, size: 21, color: NAVY } } },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1180, bottom: 1080, left: 1440, right: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: STONE } },
          children: [
            new TextRun({ text: "MEASURE & MEANING RESEARCH", font: HEAD, size: 14, color: TEALI }),
            new TextRun({ text: "\tSAMPLE — illustrative, synthetic data", font: BODY, size: 14, color: CORALI }),
          ],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
          children: [
            new TextRun({ text: "Employee Engagement & Retention Census · Sample v2", font: BODY, size: 14, color: "5A6B7E" }),
            new TextRun({ text: "\t", font: BODY, size: 14 }),
            new TextRun({ children: [PageNumber.CURRENT], font: BODY, size: 14, color: "5A6B7E" }),
          ],
        })],
      }),
    },
    children: [
      ...cover,
      new Paragraph({ children: [new PageBreak()] }),
      ...exec,
      new Paragraph({ children: [new PageBreak()] }),
      ...background,
      ...method,
      new Paragraph({ children: [new PageBreak()] }),
      ...results,
      new Paragraph({ children: [new PageBreak()] }),
      ...drivers,
      new Paragraph({ children: [new PageBreak()] }),
      ...actions,
      ...limitations,
      new Paragraph({ children: [new PageBreak()] }),
      ...appendix,
    ],
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync("Employee_Engagement_Retention_SAMPLE_v2.docx", b);
  console.log("written", b.length);
});
