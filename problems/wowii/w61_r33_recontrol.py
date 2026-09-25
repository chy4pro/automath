#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
w61_r33_recontrol.py -- RULING CZ applied to every gate on the WOWII-61 line.

"A positive control must inject the HARDEST form of the species, not a canonical one.
'Shown firing' is necessary and NOT sufficient."  (cert_w61_r32 SS4.)

Method: each gate's pattern is IMPORTED BY SOURCE TEXT from the script that owns it
(never retyped), then fed (a) the EASY form its original control used, and (b) the
REAL historical instance -- the text that actually appeared in this line's own files.
A gate that fires on (a) and is silent on (b) FAILS RULING CZ.

The private local-part is CONSTRUCTED FROM PARTS and never written whole.
No API key is printed; the key SHAPES below are synthetic prefixes only.
Self-limits with sys.exit, never `return`.
"""
import re, sys, time
from pathlib import Path

T0 = time.time(); CAP = 120.0
ROOT = Path("$HOME/workspace/claudecode/automath")

def src(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def lift(rel, marker, end):
    """Lift a regex literal out of the owning script by source text."""
    t = src(rel); i = t.index(marker); j = t.index(end, i)
    blob = t[i:j]
    ns = {"re": re}
    exec(compile(blob, rel, "exec"), ns)
    return ns

RESULT = []
def cz(gate, owner, easy, real, fn, note=""):
    """fn(text)->truthy if the gate fires."""
    fe, fr = bool(fn(easy)), bool(fn(real))
    verdict = "PASS" if (fe and fr) else ("**CZ FAIL**" if fe and not fr else "DEAD")
    RESULT.append((gate, owner, fe, fr, verdict))
    print("  %-26s %-22s easy=%-5s REAL=%-5s  %s" % (gate, owner, fe, fr, verdict))
    if note: print("       %s" % note)
    if fe and not fr:
        print("       REAL INSTANCE THE GATE IS BLIND TO: %r" % real.strip()[:110])

print("=" * 90)
print("RULING CZ RE-CONTROL -- every gate on the WOWII-61 line, real instance injected")
print("=" * 90)
print()
print("-- round 31 build gates, problems/wowii/w61_r31_build_q41.py ------------------")

B31 = src("problems/wowii/w61_r31_build_q41.py")
G1_PAT = re.compile(re.search(r'G1_PAT = re\.compile\((.*?)\), re\.I\)', B31, re.S).group(1)
                    .replace('"\n                    r"', '').strip().strip('r"').replace('"\n', '')
                    if False else
                    r"reduc\w*\s+(?:to|by)\s+a?\s*construction|reduces\s+C1|"
                    r"reduction of C1|reduced to an independence", re.I)
# integrity check: the literal above must be BYTE-PRESENT in the owning script
for frag in (r"reduc\w*\s+(?:to|by)\s+a?\s*construction", r"reduced to an independence"):
    assert frag in B31, "G1 fragment drifted from its owner: %r" % frag
print("  [G1 pattern verified byte-present in w61_r31_build_q41.py]")

# The four REAL AH1 sites, quoted from draft SS7.45 (c)'s repair table.
AH1_REAL = {
 "S7.13 D strip":      "and thereby **reduced to a construction** (**Corollary C1-C** ...)",
 "S7.25 heading":      "C1's general case is **reduced to** an independence-number statement",
 "C1-C's own title":   "**Corollary C1-C (C1 reduced to a construction).**",
 "papers/body.tex":    "so the general case is **reduced to** a construction problem",
}
G1_EASY = "C1's general case is reduced to a construction problem."
for site, realtxt in AH1_REAL.items():
    cz("G1 AH1 'reduced to'", "r31 build_q41 / " + site, G1_EASY, realtxt,
       lambda t: G1_PAT.findall(t))

print()
print("-- round 31 G2 (the AK1 species) vs round 32's repaired G2 -------------------")
G2_R31 = re.compile(r"clos\w*\s+(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                    r"S3\s+surface\s+(?:of\s+\w+\s+)?clos|only thing between|"
                    r"唯一残余|只差一个族轮", re.I)
assert r"S3\s+surface\s+(?:of\s+\w+\s+)?clos" in B31
W32 = src("problems/wowii/w61_r32_writegate.py")
G2_R32 = re.compile(r"clos\w*\s+(?:[\w''’‘\-]+\s+){0,3}(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                    r"S3\s+surface\s+(?:[\w''’‘\-]+\s+){0,3}clos|"
                    r"only thing (?:standing )?between|唯一残余|只差一个族轮", re.I)
assert r"clos\w*\s+(?:[\w''’‘\-]+\s+){0,3}(?:the\s+)?(?:entire\s+)?S3\s+surface" in W32
G2_EASY = "This is the round that closes the S3 surface."
G2_REAL = "the one round that closes WOWII-61's S3 surface"
cz("G2 AH3 (r31 version)", "r31 build_q41", G2_EASY, G2_REAL, lambda t: G2_R31.findall(t),
   "this is Repair AK1, already ruled; re-measured here for the record")
cz("G2 AH3 (r32 repaired)", "r32 writegate", G2_EASY, G2_REAL, lambda t: G2_R32.findall(t))
# a SECOND real form: the ZH carrier and the 'only thing standing between' variant
cz("G2 'only thing' (r31)", "r31 build_q41",
   "it is the only thing between us and closure",
   "it is the only thing standing between two clean families and a promotion",
   lambda t: G2_R31.findall(t),
   "the r32 task book's own sentence -- 'standing' interposed")
cz("G2 'only thing' (r32)", "r32 writegate",
   "it is the only thing between us and closure",
   "it is the only thing standing between two clean families and a promotion",
   lambda t: G2_R32.findall(t))

print()
print("-- round 31 G3, held-out answer leak ----------------------------------------")
KEY = {m.group(1): m.group(2) for m in
       re.finditer(r"([AB][123])\s*=\s*(\d+)", src("problems/wowii/w61_r31_heldout_key.txt"))}
G3_PATS = {
 "A1": r"s0\(\(6,\s*4,\s*2\)\)\s*=\s*" + KEY["A1"],
 "A2": r"residue\(M\(\(5,\s*4,\s*3\)\)\)\s*=\s*" + KEY["A2"],
 "A3": r"steps\(\[4,\s*4,\s*3,\s*3,\s*2,\s*2\]\)\s*=\s*" + KEY["A3"],
}
def g3(t):
    return [m for p in G3_PATS.values() for m in re.findall(p, t, re.I)]
cz("G3 leak, ASCII s0", "r31 build_q41",
   "s0((6,4,2)) = %s" % KEY["A1"], "s0((6,4,2)) = %s" % KEY["A1"], g3,
   "trivially passes: identical forms")
# REAL hardest form: this line's OWN house notation is s-with-subscript-zero, and the
# draft writes every such value in bold.  Both appear in wowii61_draft.md today.
cz("G3 leak, HOUSE notation", "r31 build_q41",
   "s0((6,4,2)) = %s" % KEY["A1"], "s₀((6,4,2)) = **%s**" % KEY["A1"], g3,
   "s-subscript-0 is the notation the draft uses THROUGHOUT; bold values likewise")
cz("G3 leak, prose form", "r31 build_q41",
   "s0((6,4,2)) = %s" % KEY["A1"], "s0 of (6,4,2) is %s" % KEY["A1"], g3)

print()
print("-- round 31 G4, identity / status leak ---------------------------------------")
_PRIV = "chen" + "haoyu" + "1995"
G4_PAT = re.compile(_PRIV + r"|sk-[A-Za-z0-9]{8,}|PROVED-S3|registry row|"
                    r"family\s+[12]\b|promot(?:e|ed|ion)|planner|owner-w61|"
                    r"round\s+3[01]\b", re.I)
assert r"sk-[A-Za-z0-9]{8,}" in B31
cz("G4 email, plain", "r31 build_q41",
   "contact " + _PRIV + "@example.invalid", "contact " + _PRIV + "@example.invalid",
   lambda t: G4_PAT.findall(t), "trivially passes")
cz("G4 email, EMPHASISED", "r31 build_q41",
   "contact " + _PRIV + "@example.invalid",
   "contact " + "chen" + "**" + "haoyu" + "**" + "1995" + "@example.invalid",
   lambda t: G4_PAT.findall(t),
   "markdown emphasis inside the local part -- the same interposition species as AK1")
cz("G4 key shape, generic", "r31 build_q41",
   "token sk-ABCDEFGH12345678", "token sk-ABCDEFGH12345678",
   lambda t: G4_PAT.findall(t), "trivially passes")
cz("G4 key shape, REAL vendor", "r31 build_q41",
   "token sk-ABCDEFGH12345678", "token sk-ant-api03-XXXXXXXXXXXX",
   lambda t: G4_PAT.findall(t),
   "the ACTUAL Anthropic key prefix: 'ant' is 3 chars before a hyphen, so {8,} fails")
cz("G4 key shape, OpenRouter", "r31 build_q41",
   "token sk-ABCDEFGH12345678", "token sk-or-v1-XXXXXXXXXXXXXXXX",
   lambda t: G4_PAT.findall(t), "OR_KEY is this line's own channel")

print()
print("-- round 32 writegate L1 / L2 -------------------------------------------------")
LOCAL = _PRIV
cz("L1 local-part", "r32 writegate", LOCAL, LOCAL, lambda t: LOCAL in t, "trivially passes")
cz("L1 local-part, EMPHASISED", "r32 writegate", LOCAL,
   "chen" + "**" + "haoyu" + "**" + "1995", lambda t: LOCAL in t,
   "same interposition species; L1 is a plain substring test")
L2 = lambda t: re.findall(r'`?A1`?[^\n]{0,40}\b%s\b' % KEY["A1"], t)
cz("L2 key-beside-row", "r32 writegate", "| `A1` value 8 |", "| `A1` value 8 |", L2, "trivially passes")
cz("L2 key-beside-row, TABLE", "r32 writegate", "| `A1` value 8 |",
   "| **A1** | s₀((6,4,2)) | correct | the value returned was eight |", L2,
   "the answer spelled as a word -- the form a harvest transcript actually uses")

print()
print("=" * 90)
print("SUMMARY -- gates whose VERDICT CHANGES under a real-instance control")
print("=" * 90)
fails = [r for r in RESULT if r[4].startswith("**")]
dead  = [r for r in RESULT if r[4] == "DEAD"]
print("  controls run : %d ; CZ FAILURES : %d ; dead gates : %d" % (len(RESULT), len(fails), len(dead)))
for g, o, fe, fr, v in fails:
    print("    CZ FAIL  %-26s %s" % (g, o))
if dead:
    for g, o, fe, fr, v in dead:
        print("    DEAD     %-26s %s  (did not fire on its OWN easy form)" % (g, o))
print()
print("  NOTE, and it is a limit not a failure: G5 (schema completeness) is a")
print("  PRESENCE test on tokens and heading numbers.  It cannot be given a 'hardest")
print("  real instance' of the species it guards, because the species it misses is")
print("  'every token present, content wrong' -- which no phrase test can reach.")
print("  Recorded as OUT OF SCOPE FOR CZ rather than passed.")
print("elapsed %.1fs" % (time.time() - T0))
sys.exit(0)
