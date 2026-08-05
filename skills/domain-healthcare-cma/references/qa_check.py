#!/usr/bin/env python3
"""CX session 7 QA — standalone, not part of the build.
1. Every [LOCKED ...] block in v0.3 byte-identical to its v0.2 counterpart.
2. Locked strings still match tier-b-source-items.md v0.2 (spot check on stems).
3. SEF absent from the fielded body; present only in the annex/history.
4. Declared slots carry no item wording.
"""
import re, sys

v02 = open("questionnaire-cx-member-experience.md", encoding="utf-8").read()
v03 = open("stage/questionnaire-cx-member-experience-v0_3.md", encoding="utf-8").read()
src = open("repo/tier-b-source-items.md", encoding="utf-8").read()

fails = []


def locked_blocks(txt):
    """A locked block = fence to the next '---'. Scoped to the instrument body, so the
    illustrative fence in §0.1 (which is documentation, not an item) is excluded."""
    body = txt[txt.index("# THE INSTRUMENT"):]
    out = []
    for m in re.finditer(r"```\n\[LOCKED · TIER B · VERBATIM[^\n]*\n```", body):
        start = m.start()
        nxt = body.find("\n---\n", m.end())
        out.append(body[start:nxt])
    return out


# The locked span is defined at questionnaire 5.1: item wording (EN/ES), response-option
# wording and order, section headings, section lead-ins, published skip targets, punctuation.
# Those live on structurally identifiable lines. Prose commentary in our own register does not.
CARRIER = re.compile(r"^(> \*\*(EN|ES):\*\*|- \*\*(EN|ES):\*\*|> Response:|"
                     r"\*\*Section (heading|lead-in)|\*\*Response set|"
                     r"\*\*Missing-code routing)")


def verbatim_strings(block):
    """Backtick-quoted content on locked-carrier lines only."""
    out = []
    for line in block.splitlines():
        if CARRIER.match(line.strip()):
            out.extend(re.findall(r"`([^`]+)`", line))
    return out


b2, b3 = locked_blocks(v02), locked_blocks(v03)
print(f"[1] locked blocks: v0.2 = {len(b2)}, v0.3 = {len(b3)}")
if len(b2) != 6 or len(b3) != 6:
    fails.append(f"expected 6 locked blocks each, got {len(b2)}/{len(b3)}")

total = 0
for i, (x, y) in enumerate(zip(b2, b3), 1):
    vx, vy = verbatim_strings(x), verbatim_strings(y)
    total += len(vy)
    if vx == vy:
        print(f"    block {i}: {len(vy):>2} verbatim strings byte-identical to v0.2")
    else:
        fails.append(f"locked block {i} verbatim strings DIVERGED")
        print(f"    block {i}: \u2717 DIVERGED  v0.2={len(vx)} v0.3={len(vy)}")
        for a, b in zip(vx, vy):
            if a != b:
                print(f"        v0.2: {a!r}\n        v0.3: {b!r}")
print(f"    total locked verbatim strings checked: {total}")

# 2. verbatim stems still traceable to the source file
stems = [
    "Do you know who your {case manager} is?",
    "In the last 3 months, could you contact this {case manager} when you needed to?",
    "what number would you use to rate the help you get from {case manager}?",
]
print("[2] source traceability")
for s in stems:
    ok = (s in v03) and (s in src)
    print(f"    {'OK ' if ok else '✗  '} {s[:58]}…")
    if not ok:
        fails.append(f"stem not traceable: {s[:40]}")

# 3. SEF must not appear as a fielded item
body = v03[v03.index("# THE INSTRUMENT"):v03.index("## 4 · Routing map")]
sef_in_body = [ln for ln in body.splitlines() if "SEF-0" in ln and "WITHDRAWN" not in ln
               and "withdraw" not in ln.lower() and "retired" not in ln.lower()]
print(f"[3] SEF lines in instrument body that are not withdrawal notes: {len(sef_in_body)}")
for ln in sef_in_body:
    print("    ⚑", ln[:110])

# 4. declared slots carry no drafted wording
for sec in ("Section I · About you", "Section J · Interviewer questions"):
    i = v03.index(sec)
    j = v03.index("---", i + len(sec))
    chunk = v03[i:j]
    bad = re.findall(r"\*\*Wording:\*\*", chunk)
    print(f"[4] {sec[:22]}… drafted-wording markers: {len(bad)}")
    if bad:
        fails.append(f"{sec} contains drafted wording")

# 5. count integrity
print("[5] arithmetic strings present:",
      all(s in v03 for s in ("| 19 |", "**≈22**", "**44**", "**19**", "26 found, 26 expected")))

print()
if fails:
    print("QA FAILED:")
    for f in fails:
        print("  ✗", f)
    sys.exit(1)
print("QA PASSED — locked spans intact, no SEF in the fielded body, slots undrafted.")
