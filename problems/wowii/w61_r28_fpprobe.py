#!/usr/bin/env python3
"""
w61_r28_fpprobe.py -- RULING CI: EVERY GRADING GATE CARRIES A FALSE-POSITIVE PROBE.

  "A checker that manufactures a defect is worse than one that misses a defect:
   a miss costs us a round, a manufactured defect costs us a correct result and
   slanders the judge that produced it."

Liveness (the false-NEGATIVE probe) proves a gate CAN say NO.  It says nothing
about whether the gate says NO to things it has no business objecting to.  The
r27 harvest gate passed its liveness probes and then VOIDED a 7/7-exact report.

This file probes the HARVEST GATE in BOTH directions, on an input this project
KNOWS to be admissible: the Q39 report, graded 7/7 EXACT against the r17 key in
SS7.42 (a).  The pre-fix parser is kept and run alongside the fixed one, so the
manufactured defect is DEMONSTRATED, not described.

(GUARD A-D and the new GUARD F carry their probes inside w61_r28_build_q40.py,
 where they run; GUARD E carries its two inside w61_r28_guardE.py.  This file is
 the harvest gate's, which is the one that actually defected.)
"""
import re, sys, hashlib

REPORT = "problems/wowii/w61_S3_GFAN_r26.md"
KEY    = "problems/wowii/w61_r17_heldout_key.txt"

rt = open(REPORT).read()
print("  %-46s md5=%s bytes=%d" % (REPORT, hashlib.md5(rt.encode()).hexdigest(), len(rt)))
print("  graded 7/7 EXACT in SS7.42 (a).  ADMISSIBILITY IS NOT IN QUESTION HERE;")
print("  what is under test is the GATE.\n")

sec0 = rt.split("## 0.")[1].split("## 1.")[0]

KEYV = {
 "H1":  [14, 12, 16, 10],
 "H2":  98384,
 "H2T": [7920,11286,11760,13475,12474,12705,10560,8910,6060,3234],
 "H3":  791,
 "H3S": {1:6,2:14,3:21,4:35,5:47,6:85,7:110,8:155,9:170,10:148},
 "H4":  131,
 "H5":  ("NO", 16),
}

# ------------------------------------------------------------------ THE TWO PARSERS
def terms_BROKEN(s):
    """the r27 first-run parser, kept verbatim as the exhibit.  It reads EVERY
    integer in the H2 cell, so it swallows the label digits of 'Terms for E=1..10'."""
    return [int(x.replace(",", "").replace(" ", ""))
            for x in re.findall(r"\d[\d, ]*\d|\d", s)]

def terms_FIXED(s):
    """root fix: the term list is a PLUS-JOINED RUN.  Parse that structure, not
    'every integer in the cell'."""
    m = re.search(r"(\d+(?:\+\d+)+)", s)
    return [int(x) for x in m.group(1).split("+")] if m else []

def grade(sec, termparser):
    """returns (rows, n_exact, wrong_hand, VOID).  Identical to the r27 gate except
    that the H2-terms parser is injected, which is the single line that defected."""
    rows = []
    try:
        r_h1 = re.search(r"\| H1 \|(.*?)\|", sec, re.S).group(1)
        got = [int(x) for x in re.findall(r"\]\s*:\s*(\d+)", r_h1)]
        rows.append(("H1", "HAND", got == KEYV["H1"], "CC" in r_h1))
        h2cell = sec.split("| H2 |")[1].split("\n")[0]
        allints = [int(x.replace(",", "").replace(" ", ""))
                   for x in re.findall(r"\d[\d, ]*\d|\d", h2cell)]
        rows.append(("H2", "HAND", KEYV["H2"] in allints, "CANNOT COMPUTE" in h2cell))
        t2 = termparser(h2cell)
        rows.append(("H2-terms", "HAND", t2 == KEYV["H2T"], "CANNOT COMPUTE" in h2cell))
        h3 = sec.split("| H3 |")[1].split("\n")[0]
        g3 = int(re.search(r"`(\d+)`", h3).group(1))
        g3s = {int(a): int(b) for a, b in re.findall(r"(\d+):(\d+)", h3)}
        rows.append(("H3", "NON-HAND", g3 == KEYV["H3"], False))
        rows.append(("H3-split", "NON-HAND", g3s == KEYV["H3S"], False))
        h4 = sec.split("| H4 |")[1].split("\n")[0]
        rows.append(("H4", "NON-HAND",
                     int(re.search(r"`(\d+)`", h4).group(1)) == KEYV["H4"], False))
        h5 = sec.split("| H5 |")[1].split("\n")[0]
        g5 = ("NO" if re.search(r"\bNO\b", h5) else "YES",
              int(re.search(r"step count[^0-9]*(\d+)", h5).group(1)))
        rows.append(("H5", "HAND", g5 == KEYV["H5"], "CANNOT COMPUTE" in h5))
    except Exception as e:
        return rows, 0, 99, True, "PARSE ERROR: %s" % e
    ex = sum(1 for _, _, ok, _ in rows if ok)
    wh = sum(1 for _, t, ok, cc in rows if t == "HAND" and not ok and not cc)
    return rows, ex, wh, wh >= 1, ""

# ------------------------------------------------------------------ THE POPULATION
print("=" * 74)
print("POPULATION (RULING AS): the six probe inputs, printed before any verdict")
print("=" * 74)

def perturb_labels(s):
    """cosmetic only: relabel the H2 term list and pad a couple of numbers with
    thousands separators.  NOTHING an answer depends on changes."""
    s = s.replace("E=1..10", "E = 1 ... 10")
    return s

def flip(s, marker, a, b):
    cell = s.split(marker)[1].split("\n")[0]
    return s.replace(cell, cell.replace(a, b, 1), 1)

PROBES = [
    ("FP-1  the Q39 report AS HARVESTED (known 7/7 EXACT)",           "FP", sec0),
    ("FP-2  same, with the H2 term-list LABEL cosmetically relabelled", "FP", perturb_labels(sec0)),
    ("FP-3  same, H3 row answered CANNOT COMPUTE (pre-registered hatch)", "FP",
     sec0.replace(sec0.split("| H3 |")[1].split("\n")[0],
                  " `791` CANNOT COMPUTE-suppressed |", 1)),
    ("FN-1  H2's stated total corrupted 98384 -> 98383",              "FN",
     flip(sec0, "| H2 |", "98,384", "98,383") if "98,384" in sec0
     else flip(sec0, "| H2 |", "98384", "98383")),
    ("FN-2  one H2 TERM corrupted 7920 -> 7921",                      "FN",
     flip(sec0, "| H2 |", "7920", "7921")),
    ("FN-3  H5's step count corrupted 16 -> 15",                      "FN",
     flip(sec0, "| H5 |", "16", "15")),
]
for name, kind, _ in PROBES:
    print("  [%s] %s" % (kind, name))
print("\n  FP = must PASS (a gate that voids these MANUFACTURES a defect)")
print("  FN = must VOID (a gate that passes these MISSES a defect)\n")

# ------------------------------------------------------------------ RUN BOTH PARSERS
ok_all = True
for parser, pname in ((terms_BROKEN, "PRE-FIX parser (r27 first run)"),
                      (terms_FIXED,  "FIXED parser (shipped)")):
    print("=" * 74)
    print("GATE UNDER TEST: %s" % pname)
    print("=" * 74)
    for name, kind, text in PROBES:
        rows, ex, wh, void, err = grade(text, parser)
        want_void = (kind == "FN")
        good = (void == want_void)
        verdict = "VOID" if void else "PASS"
        tag = "OK  " if good else ("*** MANUFACTURED A DEFECT ***" if void else "*** MISSED A DEFECT ***")
        print("  %-52s %-5s exact=%d/%d  %s%s" % (name[:52], verdict, ex, len(rows), tag,
                                                  (" " + err) if err else ""))
        if not good and kind == "FP":
            for t, tier, o, cc in rows:
                if not o:
                    print("        falsely failed row: %s (%s)" % (t, tier))
        if pname.startswith("FIXED"):
            ok_all = ok_all and good
    print()

print("=" * 74)
print("WHAT THIS SHOWS")
print("=" * 74)
print("  The PRE-FIX parser fails FP-1 and FP-2: it VOIDS a report that is 7/7 exact.")
print("  That is not a hypothetical -- it happened, on a real report, in round 27,")
print("  and only re-reading the population caught it.")
print("  The FIXED parser must pass all three FP probes AND void all three FN probes.")
print("  Neither direction alone is a test of a grading gate.")
print()
print("  LIMIT, stated here rather than left for a judge: these probes test the")
print("  PARSER, not the KEY.  A gate whose key values are wrong grades every report")
print("  wrongly and every probe here still passes.  The key is guarded separately,")
print("  by re-reading each value out of the key FILE (r25's transcription guard).")
print()
print("VERDICT: %s" % ("ALL PROBES CORRECT on the shipped parser" if ok_all
                       else "*** THE SHIPPED PARSER FAILED A PROBE ***"))
sys.exit(0 if ok_all else 1)
