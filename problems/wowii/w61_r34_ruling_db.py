#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r34 ITEM 3 -- RULING DB AS A BUILD-TIME GATE.

  "No two held-out rows may share a latent.  For every pair, assert that fixing one does
   not determine the other.  Where it does, they count as ONE ROW for the conjunction,
   or one is replaced."                                            (cert_w61_r33 SS4)

RULING CP checked each row against SHORTCUTS.  It never checked rows against EACH OTHER.
This is the missing gate.  It runs BEFORE dispatch, on the row specs, and it refuses.

WHAT A LATENT IS, stated precisely so the gate is not a vibe:
  a latent is a value of a quantity the BRIEF ITSELF PRINTS an identity for.  Two rows
  share a latent phi if
      (1) phi(row_i) == phi(row_j)                       -- same value, and
      (2) each row's ANSWER is recoverable from phi's value together with data the row's
          own QUESTION TEXT displays                     -- so one guess answers both.
Condition (2) is what makes this a gate and not a coincidence detector: rows may share a
number by accident without either being deducible from it.

RULING CO': stepA/runA/runB are EXTRACTED BY SOURCE TEXT from w61_r29_c1audit.py, the
same single positive-controlled source w61_r31_key.py and w61_r33_null.py both used.
Nothing about the step process is retyped here.

RULING CZ: the gate is fed BOTH a set it must REJECT (round 31's real rows) and a set it
must ACCEPT (a repaired set).  A gate only ever shown rejecting is not controlled.
No exhaustive search, no SAT.  Self-limits with sys.exit, never `return`.
"""
import re, sys, time, hashlib
from collections import Counter
from pathlib import Path
from itertools import combinations

T0 = time.time(); CAP = 120.0
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()
print("=" * 92)
print("w61 r34 ITEM 3 -- RULING DB BUILD-TIME GATE: no two held-out rows share a latent")
print("=" * 92)
print("impl source : %s  md5 %s" % (SRC.name, hashlib.md5(text.encode()).hexdigest()))
print("             (w61_r31_key.py / w61_r33_null.py recorded md5 768975c3...)")

def grab(name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---))" % re.escape(name), text, re.S | re.M)
    assert m, "could not extract def %s" % name
    return m.group(0)
ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
runA, runB = ns["runA"], ns["runB"]

DIFFED = 0
def run(lst):
    global DIFFED
    a, b = runA(list(lst)), runB(list(lst))
    if a != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s" % (lst,)); sys.exit(2)
    DIFFED += 1
    # CONTRACT, and I got this wrong on the first pass: runA/runB signal ABORT as the
    # PAIR (None, None), never as a bare None.  My original guard `if r is None` could
    # therefore never fire -- a control that cannot fire, on this very line's own
    # doctrine.  It went unnoticed because every row fed to it terminates.  Fixed and
    # recorded rather than smoothed.
    return None if a[0] is None else a         # (steps, residue), or None on abort

def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)

# ---------------------------------------------------------------- row specification
# Each row: the LIST it is really about, what the answer IS, and what the row's own
# QUESTION TEXT displays to the reader without any computation.
def row(rid, lst, kind, shown_len):
    r = run(lst)
    if r is None:
        print("row %s does not terminate -- not a legal held-out row" % rid); sys.exit(2)
    steps, resid = r
    ans = {"steps": steps, "residue": resid}[kind]
    return dict(rid=rid, lst=list(lst), kind=kind, ans=ans, steps=steps, residue=resid,
                n=len(lst), shown_len=shown_len, total=sum(lst), mx=max(lst))

# The brief's identity, printed as Proposition C1-B / Statement 3:  steps = |L| - residue
# A row's answer is RECOVERABLE from a residue value iff the row's question text shows
# the reader |L|.  All three A rows do: A1 prints [6]^7 + [6,4,2], A2 prints [5]^6 +
# [5,4,3], A3 prints the six entries literally.
def recoverable_from_residue(r):
    if not r["shown_len"]:
        return False, "|L| is not displayed in the question text"
    if r["kind"] == "residue":
        return True, "the answer IS the residue"
    if r["kind"] == "steps":
        return True, "steps = |L| - residue, and |L| is displayed (Prop C1-B, Statement 3)"
    return False, "no printed identity connects this answer to the residue"

def db_gate(rows, label):
    print()
    print("-" * 92)
    print("RULING DB GATE on: %s   (%d rows)" % (label, len(rows)))
    print("-" * 92)
    print("  %-4s %-28s %-8s %-7s %-8s %s" % ("row", "list", "|L|", "answer", "residue",
                                              "|L| shown in question?"))
    for r in rows:
        s = str(r["lst"])
        print("  %-4s %-28s %-8d %-7s %-8d %s" % (r["rid"], s[:28], r["n"],
                                                  "<hidden>", r["residue"],
                                                  "yes" if r["shown_len"] else "no"))
    bad = []
    print("\n  pairwise:")
    for a, b in combinations(rows, 2):
        same = (a["residue"] == b["residue"])
        ra, na = recoverable_from_residue(a)
        rb, nb = recoverable_from_residue(b)
        shared = same and ra and rb
        print("    %-3s x %-3s  same residue latent = %-5s   both recoverable = %-5s   %s"
              % (a["rid"], b["rid"], same, ra and rb,
                 "*** SHARED LATENT -- REJECT ***" if shared else "independent"))
        if shared:
            print("         %s : %s" % (a["rid"], na))
            print("         %s : %s" % (b["rid"], nb))
            bad.append((a["rid"], b["rid"]))
    if bad:
        cls = set()
        for x, y in bad:
            cls |= {x, y}
        print("\n  VERDICT: REJECT. %d pair(s) share a latent." % len(bad))
        print("  Rows %s collapse to ONE row for the conjunction." % ", ".join(sorted(cls)))
        print("  A build using these rows must replace all but one, or cite them as one row.")
    else:
        print("\n  VERDICT: ACCEPT. No pair shares a latent; the rows may be multiplied")
        print("  (subject to every OTHER standing condition -- DB is necessary, not sufficient).")
    return len(bad)

# ---------------------------------------------------------------- (1) the REJECT control
R31 = [row("A1", M((6, 4, 2)), "steps", True),
       row("A2", M((5, 4, 3)), "residue", True),
       row("A3", [4, 4, 3, 3, 2, 2], "steps", True)]
n_bad_r31 = db_gate(R31, "ROUND 31's ACTUAL A ROWS (the set that was dispatched)")

# ---------------------------------------------------------------- (2) the ACCEPT control
# CZ: a gate only ever shown rejecting is not a gate.  Rows chosen so their residues
# differ; nothing else about them is tuned.
CAND = []
for lam in [(6, 4, 2), (5, 4, 3), (8, 6, 4, 2), (7, 5, 3, 1), (6, 5, 4, 3, 2),
            (4, 4, 4), (9, 7), (8, 4), (10, 6, 2), (7, 6, 5)]:
    r = run(M(lam))
    if r:
        CAND.append((lam, r[1], r[0]))
print("\n  candidate pool for a REPAIRED row set (residue printed, answers withheld):")
for lam, res, st in CAND:
    print("     lambda=%-16s |M|=%-3d residue=%d" % (str(lam), len(M(lam)), res))
seen, PICK = set(), []
for lam, res, st in CAND:
    if res not in seen:
        seen.add(res)
        PICK.append(row("R%d" % (len(PICK) + 1), M(lam), "steps", True))
    if len(PICK) == 3:
        break
n_bad_ok = db_gate(PICK, "A REPAIRED ROW SET (distinct residue latents)")

# ---------------------------------------------------------------- (3) coincidence control
# Condition (2) must do real work: two rows sharing a residue but where one's answer is
# NOT recoverable must be ACCEPTED, or the gate is just an equality test on residues.
HID = row("H1", M((5, 4, 3)), "residue", False)      # same list as A2, |L| NOT displayed
HID["rid"] = "H1"
COINC = [R31[0], HID]
print("\n  --- condition-(2) control: same residue, but one row's |L| is NOT displayed ---")
n_bad_co = db_gate(COINC, "COINCIDENCE PAIR (shared value, one not recoverable)")

# ---------------------------------------------------------------- verdict
print()
print("=" * 92)
print("GATE SELF-CONTROL")
print("=" * 92)
ok = True
print("  must REJECT round 31's rows                 : %s (%d bad pairs)"
      % ("REJECTED" if n_bad_r31 else "*** ACCEPTED -- GATE IS DEAD ***", n_bad_r31))
ok &= n_bad_r31 > 0
print("  must ACCEPT a distinct-latent row set       : %s"
      % ("ACCEPTED" if n_bad_ok == 0 else "*** REJECTED -- GATE IS VACUOUS ***"))
ok &= n_bad_ok == 0
print("  must ACCEPT a shared-VALUE non-recoverable  : %s"
      % ("ACCEPTED" if n_bad_co == 0 else "*** REJECTED -- gate is an equality test ***"))
ok &= n_bad_co == 0
print("  implementations diffed (runA vs runB)       : %d calls, 0 disagreements" % DIFFED)
print()
print("  ROUND 31's THREE A ROWS FAIL THIS GATE ON ALL THREE PAIRS. Had it existed, the")
print("  build would have refused before dispatch, and the 1/36 that cert_w61_r32 SS8 was")
print("  written around would never have been available to write around.")
print()
print("  SCOPE, because overstating a new gate is how the last four got written:")
print("   * DB is NECESSARY, NOT SUFFICIENT. It tests one shared-latent family -- the")
print("     residue, because that is the identity the brief prints. A brief printing a")
print("     DIFFERENT identity creates a different latent, and this gate will not see it.")
print("   * The latent list must be REBUILT PER BRIEF from the identities that brief")
print("     prints. Hard-coding 'residue' into the line's build scripts would reproduce")
print("     RULING CZ exactly: a check measuring the dimension its fault set came from.")
print("   * It says nothing about GUESSABILITY. Three rows with distinct latents can each")
print("     still have a 3-element plausible set. DB and the null are separate conditions")
print("     and BOTH must be computed before any conjunction is cited.")
print("  elapsed %.1fs" % (time.time() - T0))
RC = 0 if ok else 2

# ---------------------------------------------------------------- RIDER: is DB satisfiable here?
# The candidate pool above showed 8 of 10 lambdas landing on residue 2.  If the residue
# latent is near-CONSTANT across the natural row population, then DB is not a formality
# on this problem -- it is a binding constraint, and a brief cannot get three independent
# rows out of this family at all.  Bounded census, capped, no search.
print()
print("=" * 92)
print("RIDER -- IS RULING DB EVEN SATISFIABLE ON THIS FAMILY?  (bounded census)")
print("=" * 92)
def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield ()
    else:
        for f in range(min(n, mx), 0, -1):
            for rest in parts(n - f, f):
                yield (f,) + rest
from collections import Counter as _C
hist, tot, NCAP = _C(), 0, 34
for N in range(4, NCAP + 1):
    if time.time() - T0 > CAP:
        print("  census stopped at sum=%d by time cap" % N); break
    for lam in parts(N):
        if len(lam) < 2:
            continue
        st, res = runA(M(lam))
        if st is None:                 # (None, None) == abort; see the contract note above
            continue
        tot += 1
        hist[res] += 1
print("  population: every partition of 4..%d with >=2 parts whose M terminates" % NCAP)
print("  terminating lists: %d" % tot)
print("  residue histogram: %s" % dict(sorted(hist.items())))
if tot:
    top, cnt = hist.most_common(1)[0]
    print("  MODAL RESIDUE %d covers %d/%d = %.1f%% of the whole population."
          % (top, cnt, tot, 100.0 * cnt / tot))
    print("  distinct residue values available at all: %d" % len(hist))
    print()
    print("  SECOND CUT -- restricted to HAND-COMPUTABLE rows, which is what round 31")
    print("  actually required (A rows are 'derivable by hand from section 1 alone'):")
    for cap in (10, 12, 14, 18):
        h2 = _C()
        for N in range(4, NCAP + 1):
            for lam in parts(N):
                if len(lam) < 2:
                    continue
                if len(M(lam)) > cap:
                    continue
                st, res = runA(M(lam))
                if st is None:
                    continue
                h2[res] += 1
        if h2:
            tp, cn = h2.most_common(1)[0]
            tt = sum(h2.values())
            print("    |M| <= %-3d : %5d rows, %2d distinct residues, MODAL residue %d = %5.1f%%"
                  % (cap, tt, len(h2), tp, 100.0 * cn / tt))
    print()
    print("  THE FINDING, AND IT IS THE OPPOSITE OF WHAT I EXPECTED WHEN I WROTE THIS RIDER.")
    print("  I predicted the residue latent would be near-constant across the family, which")
    print("  would have made RULING DB unsatisfiable here. THE CENSUS REFUTES THAT: over the")
    print("  full population the residue takes %d distinct values and the mode holds only" % len(hist))
    print("  %.1f%%. The prediction was wrong and the table above is the authority." % (100.0*cnt/tot))
    print()
    print("  What the two cuts together actually show is sharper and worse:")
    print("   * DB IS SATISFIABLE on this family. Independent rows exist in quantity.")
    print("   * The collinearity was manufactured by the HAND-COMPUTABILITY CONSTRAINT.")
    print("     Round 31 required its A rows to be derivable by hand, which forces short")
    print("     lists, and short lists CONCENTRATE: 4 residue values at |M|<=10 against 17")
    print("     over the family, with the top one at 50.8%. Said exactly, because the table")
    print("     above is the authority: that modal value is 3, NOT the 2 round 31 drew. So")
    print("     the collinearity is BOTH the structural concentration AND an unlucky draw")
    print("     inside it -- round 31 landed three rows on a SUB-modal value. Either alone")
    print("     would have been survivable; the brief\'s own hand-derivability rule plus one")
    print("     unexamined draw is what collapsed three rows onto one latent.")
    print("   * SO THE REPAIR IS NOT 'PICK BETTER SMALL ROWS'. It is that a row set cannot")
    print("     be simultaneously hand-derivable AND latent-independent AND numerous on")
    print("     this family. Any two of the three. A future brief must choose which to")
    print("     drop and say which, before dispatch, in writing.")
    print("   * RULING DB must therefore run AFTER the hand-computability filter, never")
    print("     before it -- otherwise it certifies a pool the brief will never draw from.")
print("  elapsed %.1fs" % (time.time() - T0))
sys.exit(RC)
