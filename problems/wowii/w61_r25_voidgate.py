#!/usr/bin/env python3
"""owner-w61 round 25 -- Q38 VOID GATE, run BLIND (Section 0 rows only; no prose read).

RULING AS: print the population before the verdict.  Both sides of every row are
printed in full FIRST; verdicts are computed only after the print.
Grading is EXACT MATCH against problems/wowii/w61_r17_heldout_key.txt (written r17,
untouched since; md5 recorded below).
"""
import hashlib, re, sys

REPORT = "problems/wowii/w61_S3_GFAN_r24.md"
KEY    = "problems/wowii/w61_r17_heldout_key.txt"

def md5(p):
    return hashlib.md5(open(p,'rb').read()).hexdigest()

print("=== ARTIFACTS ===")
for p in (REPORT, KEY):
    print(f"  {p}  md5={md5(p)}  bytes={len(open(p,'rb').read())}")

# ---- the key, transcribed from the r17 key file (values only) ----
KEY_H1 = {"[12,6,4]":14, "[9,7,3,3]":12, "[14,5,2,1]":16, "[8,8,6]":10}
KEY_H2 = 98384
KEY_H2_TERMS = [7920,11286,11760,13475,12474,12705,10560,8910,6060,3234]
KEY_H3 = 791
KEY_H3_SPLIT = [6,14,21,35,47,85,110,155,170,148]
KEY_H4 = 131
KEY_H5 = ("NO", 16)

# ---- guard: the transcription above must actually be IN the key file ----
kt = open(KEY).read()
guard = []
for pat in ["s0([12+6+4]) = 14","s0([9+7+3+3]) = 12","s0([14+5+2+1]) = 16",
            "s0([8+8+6]) = 10","S(11) = sum_{E=1}^{10} (11-E) p(E) p(22-E) = 98384",
            "E>=1 survivors at nu = 11 : 791",
            "{1: 6, 2: 14, 3: 21, 4: 35, 5: 47, 6: 85, 7: 110, 8: 155, 9: 170, 10: 148}",
            "s0(lambda) = 13} = 131","clears in exactly L = 13 steps?  NO   (actual step count 16)"]:
    guard.append((pat in kt, pat))
print("\n=== TRANSCRIPTION GUARD (every graded value must appear verbatim in the key file) ===")
for ok, pat in guard:
    print(("  OK   " if ok else "  MISS ") + pat)
assert all(ok for ok,_ in guard), "transcription guard FAILED -- gate is not gradeable"

# ---- the report's Section 0 rows, extracted verbatim, printed before grading ----
rows = {}
for line in open(REPORT):
    m = re.match(r"\|\s*(H[1-5])\s*\|(.*)", line)
    if m:
        rows[m.group(1)] = m.group(2).rstrip()
print("\n=== REPORT SECTION 0, VERBATIM (%d rows found) ===" % len(rows))
for k in sorted(rows):
    print(f"  {k} | {rows[k]}")
assert set(rows) == {"H1","H2","H3","H4","H5"}, "not all five held-out rows present"

def nums(s):
    return [int(x.replace(",","").replace("_","")) for x in re.findall(r"\d[\d,_]*", s)]

print("\n=== GRADING (exact match) ===")
res = {}

# H1: the four values, in the order the key lists them, must all be present as pairs
h1 = rows["H1"]
got1 = re.findall(r"\[\s*12\s*,\s*6\s*,\s*4\s*\]\s*(?:→|->|-->)\s*`?\s*(\d+)", h1) \
     + re.findall(r"\[\s*9\s*,\s*7\s*,\s*3\s*,\s*3\s*\]\s*(?:→|->|-->)\s*`?\s*(\d+)", h1) \
     + re.findall(r"\[\s*14\s*,\s*5\s*,\s*2\s*,\s*1\s*\]\s*(?:→|->|-->)\s*`?\s*(\d+)", h1) \
     + re.findall(r"\[\s*8\s*,\s*8\s*,\s*6\s*\]\s*(?:→|->|-->)\s*`?\s*(\d+)", h1)
want1 = [14,12,16,10]
print(f"  H1 [HAND]  key={want1}  report={[int(x) for x in got1]}")
res["H1"] = ([int(x) for x in got1] == want1)

# H2
g2 = nums(rows["H2"])
print(f"  H2 [HAND]  key value={KEY_H2}  key terms={KEY_H2_TERMS}")
print(f"             report numbers={g2}")
res["H2"] = (KEY_H2 in g2) and all(t in g2 for t in KEY_H2_TERMS)

# H3
# CHECKER DEFECT FOUND AND FIXED IN-ROUND (r25): nums() strips ',' as a thousands
# separator, so the ten-entry split "[6,14,21,...]" collapsed into ONE integer and the
# row graded MISMATCH on a correct answer.  Noisy-and-safe (RULING BL) -- it cost a
# re-scope, not a promotion -- but it is a real miscalibration and is recorded, not
# quietly patched.  The split is now parsed from its own bracketed list, comma-preserved.
h3 = rows["H3"]
g3 = nums(h3)
brackets = re.findall(r"\[([0-9,\s]+)\]", h3)
splits = [[int(x) for x in b.replace(" ","").split(",") if x] for b in brackets]
print(f"  H3 [NON-HAND]  key value={KEY_H3}  key split={KEY_H3_SPLIT}")
print(f"                 report bracketed lists={splits}")
print(f"                 report scalars={[n for n in g3 if n < 10**6]}")
split_ok = KEY_H3_SPLIT in splits
value_ok = KEY_H3 in g3
res["H3"] = value_ok and split_ok
print(f"                 value_ok={value_ok}  ten-entry split exact={split_ok}")

# H4
g4 = nums(rows["H4"])
print(f"  H4 [NON-HAND]  key={KEY_H4}  report numbers={g4}")
res["H4"] = (KEY_H4 in g4)

# H5
h5 = rows["H5"]
said_no = re.search(r"\bNO\b", h5) is not None
said_yes = re.search(r"\bYES\b", h5) is not None
g5 = nums(h5)
print(f"  H5 [HAND]  key=('NO', 16)   report: NO={said_no} YES={said_yes} numbers={g5}")
res["H5"] = said_no and (not said_yes) and (16 in g5)

# CANNOT COMPUTE hatch usage
hatch = {k: ("CANNOT COMPUTE" in rows[k].upper()) for k in rows}
print(f"\n  hatch 'CANNOT COMPUTE' used on: {[k for k,v in hatch.items() if v]}")

print("\n=== VERDICT (computed only now) ===")
for k in ["H1","H2","H3","H4","H5"]:
    print(f"  {k}: {'EXACT' if res[k] else 'MISMATCH'}")
hand = ["H1","H2","H5"]; comp = ["H3","H4"]
hand_wrong = [k for k in hand if not res[k] and not hatch[k]]
comp_wrong = [k for k in comp if not res[k] and not hatch[k]]
print(f"\n  HAND rows wrong (any ⟹ VOID): {hand_wrong or 'none'}")
print(f"  COMPUTATIONAL rows wrong (both wrong, hatch unused ⟹ VOID): {comp_wrong or 'none'}")
void = bool(hand_wrong) or (len(comp_wrong) == 2)
print(f"\n  VOID GATE: {'VOID' if void else 'PASS'}   score {sum(res.values())}/5 exact")
