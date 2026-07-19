#!/usr/bin/env python3
"""Generate the machine-readable codebook for the M&M Employee Census instrument.
Source of truth: questionnaire-employee-census.md v0.1 + codebook-employee-census.md v0.1.
Output: codebook-employee-census-v0_1.csv (one row per variable)."""

import csv

AGREE5 = "1=Strongly disagree;2=Disagree;3=Neither agree nor disagree;4=Agree;5=Strongly agree"
SAT5 = "1=Very dissatisfied;2=Dissatisfied;3=Neither satisfied nor dissatisfied;4=Satisfied;5=Very satisfied"
IMP7 = ("1=Not at all important;2=Slightly important;3=Somewhat important;4=Moderately important;"
        "5=Important;6=Very important;7=Extremely important")
SAT7 = ("1=Very dissatisfied;2=Dissatisfied;3=Somewhat dissatisfied;4=Neither satisfied nor dissatisfied;"
        "5=Somewhat satisfied;6=Satisfied;7=Very satisfied;99=Not applicable (off-scale)")
NPS11 = "0=Not at all likely;...;10=Extremely likely"

COLS = ["variable_id", "block", "item_text", "response_type", "scale", "value_labels",
        "missing_codes", "reverse_keyed", "index_membership", "notes"]

rows = []


def add(vid, block, text, rtype, scale, labels, missing="blank=skipped",
        rev="no", idx="", notes=""):
    rows.append(dict(zip(COLS, [vid, block, text, rtype, scale, labels, missing, rev, idx, notes])))


# --- Block A ---
add("SAT-00", "A_anchor", "Overall, how satisfied or dissatisfied are you with [Organization] as an employer?",
    "single", "SAT-5", SAT5, idx="criterion_secondary",
    notes="Asked before the GAP matrix; headline trend metric")

# --- Block B: CORE ---
core = [
    "Most days, my work gives me more energy than it takes.",
    "I am proud to tell people where I work.",
    "My work gives me a real sense of accomplishment.",
    "When my team needs extra effort, I am willing to give it.",
    "I can see a future for myself at this organization.",
    "I care about what this organization is trying to achieve.",
]
for i, t in enumerate(core, 1):
    add(f"ENG-{i:02d}", "B_core", t, "single", "AGREE-5", AGREE5, idx="IDX_ENG",
        notes="Item order fixed across waves")

# --- Block C: NPS ---
add("NPS-01", "C_nps",
    "How likely are you to recommend [Organization] as a place to work to a friend or colleague?",
    "single", "NPS-11", NPS11, idx="ENPS;NPS_CLASS",
    notes="0-10 only; cutoffs 9-10 promoter / 0-6 detractor defined on this scale")
add("NPS-02", "C_nps", "What is the main reason for your score?", "open_text", "", "",
    notes="Thematic coding; cross-tabbed by promoter class")

# --- Block D: GAP ---
GAP = [
    ("PAY", "Pay fairness", "My total pay reflects my skills and what I contribute."),
    ("REC", "Recognition", "Good work here gets noticed and acknowledged."),
    ("MGR", "Manager relationship", "I can work with my direct manager openly and without friction."),
    ("GRW", "Career growth", "There is a realistic path to grow my career here."),
    ("LRN", "Learning & development", "I can build new professional skills through my work, including formal training and development programs."),
    ("FLX", "Schedule fit", "My work schedule fits my life - hours, predictability, and the flexibility available to me."),
    ("WKL", "Sustainable workload", "My workload is one I can sustain long-term without burning out."),
    ("BEN", "Benefits & social support", "The benefits package (health, retirement, family support) works for my real life."),
    ("MNG", "Meaningful work", "My work contributes to something I consider worthwhile."),
    ("AUT", "Autonomy", "I can decide how to do my own work."),
    ("TEA", "Team relationships", "I work with people I trust and enjoy working with."),
    ("SEC", "Job security", "I am confident in this organization's stability and future."),
    ("RES", "Tools & resources", "I have the tools, equipment, and resources I need to get my work done."),
    ("VOI", "Voice & participation", "My ideas can actually influence decisions in my area, and leaders are willing to hear them."),
    ("CRS", "Support in difficult situations", "If I run into a difficult situation - at work or in life - this organization will help me through it."),
    ("SAF", "Workplace safety", "I feel safe and protected while doing my job."),
    ("COM", "Communication & information", "I get the information I need about what is happening in the organization and how it affects me."),
    ("FDK", "Feedback", "I know how my work is evaluated and what I can do to improve."),
]
for code, cat, text in GAP:
    add(f"GAP-{code}-I", "D_gap", f"[{cat}] IMPORTANCE: {text}", "single", "IMP-7", IMP7,
        idx=f"GAP_{code};IMP_MED", notes="No N/A option offered on importance")
    add(f"GAP-{code}-S", "D_gap", f"[{cat}] SATISFACTION: {text}", "single", "SAT-7", SAT7,
        missing="blank=skipped;99=not applicable", idx=f"GAP_{code};COV_{code};SAT_MED;driver_predictor",
        notes="99 excluded from means, reported as coverage %; NEVER recoded to midpoint")
add("GAP_ORDER", "D_gap", "Realized randomized display order of the 18 categories", "paradata", "", "",
    notes="Comma-separated codes; required to test order effects between waves")

# --- Block E: BRN ---
brn = [
    ("BRN-01", "By the end of a typical workday, I have little energy left for anything else.", "no"),
    ("BRN-02", "Evenings, weekends, and vacations are enough for me to recover from work.", "yes"),
    ("BRN-03", "I find it harder to get interested in my work than I used to.", "no"),
    ("BRN-04", "My current workload is sustainable for the long term.", "yes"),
    ("BRN-05", "I feel increasingly detached from what happens in this organization.", "no"),
    ("BRN-06", "In the past month, work stress has affected my sleep or health.", "no"),
]
for vid, text, rev in brn:
    add(vid, "E_brn", text, "single", "AGREE-5", AGREE5, rev=rev, idx="IDX_BRN;BRN_TIER;driver_predictor",
        notes="Reversal applied at scoring only (x_r = 6 - x); scale never flipped on screen"
        if rev == "yes" else "Aggregate reporting only, N>=5")

# --- Block F: STAY ---
add("STY-01", "F_stay", "I expect to still be working at this organization twelve months from now.",
    "single", "AGREE-5", AGREE5, idx="criterion_primary", notes="Primary criterion for the driver model")
add("STY-02", "F_stay", "In the past six months, I have seriously considered leaving.",
    "single", "AGREE-5", AGREE5, notes="Reported separately; not summed with STY-01")
add("STY-03", "F_stay", "Which best describes your current plans?", "single", "categorical",
    "1=Planning to stay;2=Open to outside offers;3=Actively looking;98=Prefer not to say",
    missing="blank=skipped;98=prefer not to say",
    notes="Only item with an explicit refusal option; refusal rate reported")

# --- Block G: OPEN ---
add("OPN-01", "G_open",
    "What is the single most important thing this organization could change to make it a better place to work?",
    "open_text", "", "", notes="Dual-coder thematic coding with adjudication")
add("OPN-02", "G_open", "What should this organization be careful NOT to change?", "open_text", "", "",
    notes="Source of 'keep' themes")
add("OPN-03", "G_open", "(need-specific slot; omitted in standard census)", "open_text", "", "",
    missing=".n=not fielded", notes="Activated per engagement")

# --- Block H: segmentation ---
add("SEG-TEN", "H_segmentation", "How long have you worked at [Organization]?", "single", "categorical",
    "1=Less than 1 year;2=1-2 years;3=3-6 years;4=7 years or more",
    missing="blank=skipped", idx="weighting_cell",
    notes="Non-overlapping by construction (owner decision 2026-07-19); HRIS extract must be re-banded to match")
add("SEG-FUN", "H_segmentation", "Which best describes your area?", "single", "categorical",
    "client-specific; mirrors HRIS department list;98=Prefer not to say",
    missing="blank=skipped;98=prefer not to say", idx="weighting_cell",
    notes="Must match HRIS exactly or weighting cannot be executed as specified")
add("SEG-ROL", "H_segmentation", "Which best describes your role level?", "single", "categorical",
    "1=Individual contributor;2=Team lead/supervisor;3=Manager;4=Senior leadership;98=Prefer not to say",
    missing="blank=skipped;98=prefer not to say", idx="weighting_cell")
add("SEG-SIT", "H_segmentation", "Which site do you work at most of the time?", "single", "categorical",
    "client-specific;98=Prefer not to say", missing="blank=skipped;98=prefer not to say")
add("SEG-AGE", "H_segmentation", "Which age group are you in?", "single", "categorical",
    "1=Under 25;2=25-34;3=35-44;4=45-54;5=55 or older;98=Prefer not to say",
    missing="blank=skipped;98=prefer not to say")
add("SEG-CAR", "H_segmentation", "Do you regularly care for children or another dependent?", "single",
    "categorical", "1=Yes;2=No;98=Prefer not to say", missing=".n=not fielded", notes="Optional per engagement")
add("SEG-EDU", "H_segmentation", "What is the highest level of education you have completed?", "single",
    "categorical", "client-specific;98=Prefer not to say", missing=".n=not fielded",
    notes="Optional per engagement")

# --- quality / paradata ---
add("AC-01", "quality", "Attention check (GAP screen 2, satisfaction column)", "single", "SAT-7", SAT7,
    notes="Pass = 'Satisfied' (6). One failure flags; two exclude")
add("AC-02", "quality", "Attention check (BRN matrix, row 4)", "single", "AGREE-5", AGREE5,
    notes="Pass = 'Agree' (4). One failure flags; two exclude")
add("T_TOTAL", "paradata", "Total completion time", "numeric", "seconds", "",
    notes="Speeder screen: < 1/3 of sample median flags")
add("T_BLOCK_*", "paradata", "Page-level time per screen", "numeric", "seconds", "",
    notes="Sustained < 2 s per item excludes")
add("DEVICE", "paradata", "Device type", "single", "categorical", "1=desktop;2=mobile;3=tablet;4=kiosk",
    notes="Kiosk duplicates expected by design; never used for identification")
add("SOURCE", "paradata", "Invitation channel", "single", "categorical", "1=link;2=QR;3=kiosk")

# --- derived ---
derived = [
    ("IDX_ENG", "Engagement index, 0-100", "(mean(ENG-01..06) - 1) / 4 * 100", "Computed if >=4 of 6 answered"),
    ("IDX_BRN", "Burnout index, 6-30", "sum(BRN-01, BRN-02r, BRN-03, BRN-04r, BRN-05, BRN-06)", "Computed if >=5 of 6 answered"),
    ("BRN_TIER", "Burnout risk tier", "6-13=Low;14-21=Moderate;22-30=Elevated", "Pre-set cutpoints, not sample terciles; disclosed"),
    ("NPS_CLASS", "Promoter class", "0-6=Detractor;7-8=Passive;9-10=Promoter", ""),
    ("ENPS", "Employee Net Promoter Score, pp", "%Promoters - %Detractors", "Mean of NPS-01 is a secondary statistic only"),
    ("GAP_<CODE>", "Gap score per category", "mean(GAP-<CODE>-I) - mean(GAP-<CODE>-S)", "Satisfaction mean excludes 99"),
    ("COV_<CODE>", "Coverage per category", "% answering 99 on GAP-<CODE>-S", "Reported with every satisfaction mean"),
    ("IMP_MED", "Within-survey median importance", "median of the 18 importance means", "Defines GAP quadrant boundary; recomputed each wave"),
    ("SAT_MED", "Within-survey median satisfaction", "median of the 18 satisfaction means", "Defines GAP quadrant boundary; recomputed each wave"),
    ("WT", "Payroll weight", "rim weighting on department x tenure x role", "Trimmed 0.4-2.5; design effect reported"),
]
for vid, text, formula, note in derived:
    add(vid, "derived", text, "derived", "", formula, missing="", notes=note)

with open("codebook-employee-census-v0_1.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    w.writerows(rows)

print(f"wrote {len(rows)} variable rows")
fielded = [r for r in rows if r["block"] not in ("derived", "paradata")
           and r["response_type"] in ("single",)]
print("fielded closed items:", len(fielded))
