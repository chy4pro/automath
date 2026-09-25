#!/usr/bin/env python3
"""owner-w61 round 25 -- RULING BK retroactive brief audit, MECHANICAL half.

One question, mechanised: *what in this document answers a joint for the judge before
the judge reads anything?*  A status word attached to an imported statement answers
J-IMPORT; a status word attached to a TARGET statement answers the round.

RULING AS: the whole population is printed BEFORE any verdict.
RULING BL: err NOISY.  The vocabulary is deliberately over-broad; every hit is printed
with its line and adjudicated by hand in the ledger, not suppressed by the script.
RULING S: this check's own coverage is stated -- it tests OCCURRENCE of a status
vocabulary, not derivability, and it cannot see a leak phrased without these words.
"""
import re, glob, os, hashlib

# the promotion-scoring population, named explicitly with what each brief bought
POP = [
 ("prompts/w61_S3_GFAN_qwen.md",  "Q25",  "rows R-20, R-21, R-22 (family 1)"),
 ("prompts/w61_S3_GFAN_sol.md",   "Q33",  "rows R-20, R-21 (family 2)"),
 ("prompts/w61_S3_GFAN_r14.md",   "Q34",  "row R-22 (family 3)"),
 ("prompts/w61_S3_GFAN_r14b.md",  "Q34b", "row R-22 (family 2, Meta)"),
 ("prompts/w61_S3_GFAN_r15.md",   "Q35",  "row R-23 (family 1)"),
 ("prompts/w61_S3_GFAN_r20.md",   "Q37",  "row R-23 (family 2)"),
]
# non-promotion briefs of the same family, swept too (noisy side)
ALSO = [("prompts/w61_S3_GFAN_r18.md","Q36","no promotion (no family 2 that round)"),
        ("prompts/w61_S3_GFAN_r24.md","Q38","IN FLIGHT this round")]

VOCAB = [
 ("STATUS-CERT",  r"\bcertified\b|\bcertification\b"),
 ("STATUS-PROVED",r"PROVED-S3|\bproved\b(?![ -]in place)|\bestablished elsewhere\b"),
 ("STATUS-FAM",   r"two (independent )?families|second family|independent families|clean round"),
 ("STATUS-VER",   r"independently verified|already verified|verified elsewhere|owner-certified"),
 ("STATUS-JUDGE", r"\bjudges?\b.{0,30}\b(certified|clean|passed)|passed .{0,20}(gate|review)"),
 ("STATUS-SETTLED",r"\bsettled\b|\bclosed\b(?![ -]form)|no longer (open|in doubt)|not in doubt"),
]

print("=== POPULATION, PRINTED BEFORE ANY VERDICT (RULING AS) ===")
def stamp(p):
    b=open(p,'rb').read(); return f"{len(b):>7}B md5={hashlib.md5(b).hexdigest()[:8]}"
print("  -- promotion-scoring briefs (the audit RULING BK ordered) --")
for p,q,what in POP: print(f"    {q:<5} {p:<34} {stamp(p)}  bought: {what}")
print("  -- same family, no promotion (swept anyway, noisy side) --")
for p,q,what in ALSO: print(f"    {q:<5} {p:<34} {stamp(p)}  {what}")

print("\n=== CHECK LIVENESS (V7): the vocabulary must fire on a known planted leak ===")
planted = "Do not referee the imports' own proofs -- they are separately certified."
lit = [(n,pat) for n,pat in VOCAB if re.search(pat, planted, re.I)]
print(f"  planted sentence: {planted!r}")
print(f"  classes that fire: {[n for n,_ in lit]}   -> check CAN fail: {bool(lit)}")
assert lit, "V7 FAILED: the vocabulary does not fire on the known r14 leak"

print("\n=== ALL HITS, VERBATIM, EVERY BRIEF (no filtering) ===")
tally = {}
for p,q,what in POP+ALSO:
    txt = open(p, encoding='utf-8', errors='replace').read().splitlines()
    hits = []
    for i,line in enumerate(txt,1):
        for name,pat in VOCAB:
            if re.search(pat, line, re.I):
                hits.append((i,name,line.strip()))
                break
    tally[q] = len(hits)
    print(f"\n--- {q}  {p}  ({len(hits)} hit lines)")
    for i,name,line in hits:
        print(f"    {i:>5} [{name}] {line[:190]}")

print("\n=== TALLY (verdict computed only now) ===")
for p,q,what in POP+ALSO:
    print(f"  {q:<5} {tally[q]:>3} hit lines   {what}")
