#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r34 WRITE-TIME gate on SS7.49.  Every pattern is LIFTED BY SOURCE TEXT from the
script that owns it and asserted byte-present there (RULING CO'):
  L1, G2, G4'  <- w61_r33_writegate.py     G1', G3'  <- w61_r34_gates.py
Each is shown firing on its REAL historical instance in the same run (RULING CZ), and
each control is MINIMAL-PAIRED where its instance carries more than one species -- the
new refinement from w61_r34_gates.py.  Diagnostics are REDACTED.  Population before
verdict.  Self-limits with sys.exit, never `return`."""
import re, sys
from pathlib import Path
ROOT = Path("$HOME/workspace/claudecode/automath")
D = ROOT / "notes/proofs/wowii61_draft.md"
W33 = (ROOT / "problems/wowii/w61_r33_writegate.py").read_text(encoding="utf-8")
W34 = (ROOT / "problems/wowii/w61_r34_gates.py").read_text(encoding="utf-8")
MARK = "<!-- RETRACTED-QUOTE -->"

def lift(text, start, end, owner):
    i = text.index(start); j = text.index(end, i)
    ns = {"re": re}; exec(compile(text[i:j], owner, "exec"), ns); return ns
n33 = lift(W33, "LOOSE = re.compile(", "sec = open(", "w61_r33_writegate.py")
L1, G2, G4 = n33["LOOSE"], n33["G2"], n33["G4"]
n34 = lift(W34, '_M = r"[\\s*_`~]{0,6}"', "\nR1a =", "w61_r34_gates.py")
G1 = n34["G1_NEW"]
assert "sk-(?:[A-Za-z0-9]+-){0,3}[A-Za-z0-9]{8,}" in W33 and "G1_NEW = re.compile(" in W34

sec = D.read_text(encoding="utf-8")
sec = sec[sec.index("## §7.49"):]
_P = re.compile(r"chen[\W_]{0,4}haoyu[\W_]{0,4}1995", re.I)
red = lambda s: _P.sub("<PRIVATE-LOCAL-PART>", s)
print("=== w61 r34 write gate on §7.49 (population BEFORE verdict) ===")
print("  §7.49 chars %d, lines %d" % (len(sec), sec.count("\n")))
bad = 0
for nm, pat in (("L1 private local-part", L1), ("G4' key shape", G4), ("G1' AH1 over-read", G1)):
    n = len(pat.findall(sec)); print("  %-24s %d" % (nm, n)); bad += n
    for h in pat.findall(sec)[:4]: print("      %r" % red(str(h))[:80])
raw = [(i, l) for i, l in enumerate(sec.split("\n"), 1) if G2.search(l)]
car = [h for h in raw if MARK not in h[1]]
print("  %-24s raw=%d marked=%d CARRIERS=%d" % ("G2 AH3 closure", len(raw), len(raw)-len(car), len(car)))
for i, l in car: print("      +%-4d CARRIER %r" % (i, red(l.strip())[:88]))
bad += len(car)
print("  POSITIVE CONTROLS, REAL instances, MINIMAL-PAIRED where two species co-occur:")
c1 = "chen" + "**" + "haoyu" + "**" + "1995"
c2 = "this is the round that closes WOWII-61's S3 surface"
c2b = "it is now the only statement standing between WOWII-61 and a promotion"
c3 = "sk-ant-api03-" + "X" * 12
c4 = "so the general case is **reduced to** a construction problem"
f = {"L1(emphasis)": bool(L1.search(sec + c1)) and not bool(L1.search(sec)),
     "G2(possessive,bare)": bool(G2.search(c2)) and MARK not in c2,
     "G4'(sk-ant)": bool(G4.search(sec + " " + c3)),
     "G1'(md interposition)": bool(G1.search(c4))}
for k, v in f.items(): print("      %-24s %s" % (k, v))
print("      G2 MINIMAL PAIR on 'only statement standing between' -> fires=%s" % bool(G2.search(c2b)))
print("        DECLARED, NOT HIDDEN: G2 is BLIND to that construction. It is the referent")
print("        species and no regex reaches it. §7.49 (e) says so; the gate does not")
print("        pretend otherwise, and this line is why the gate's CLEAN is not a class claim.")
if not all(f.values()):
    print("A GATE COULD NOT BE SHOWN FIRING ON ITS REAL INSTANCE -- refusing to certify"); sys.exit(2)
print("  DECLARED: §7.49 states that round 31's A rows all had residue 2. Via Prop C1-B")
print("  that DETERMINES the A-row answers. §7.49 therefore carries held-out key content")
print("  on exactly the same footing as §7.48 and MUST NEVER BE PASTED INTO A BRIEF.")
print("VERDICT:", "CLEAN" if bad == 0 else "DIRTY bad=%d" % bad)
sys.exit(0 if bad == 0 else 2)
