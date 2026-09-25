#!/usr/bin/env python3
"""
w61_r31_key.py -- held-out key for the SS7.25 two-family round (Q41/Q42).

SINGLE SOURCE OF TRUTH for the process implementations.  RULING (doctrine SS10):
"load-bearing predicates become ONE checked implementation, imported everywhere,
never re-typed."  stepA/runA/runB are therefore EXTRACTED FROM
problems/wowii/w61_r29_c1audit.py by source text and exec'd here -- not retyped.
If that file's definitions change, this script changes with them or dies.

Everything below prints its POPULATION before its verdict.
Every boolean predicate carries a POSITIVE control (an input on which it MUST
return True) as well as inputs on which it must return False -- a predicate whose
failure mode is "unconditionally False" is invisible to negative controls.

Self-limit: hard wall-clock cap; on overrun the script calls sys.exit(3).
"""
import sys, time, re, hashlib, itertools
from collections import Counter
from pathlib import Path

T0 = time.time()
CAP_S = 240.0
def tick(where):
    if time.time() - T0 > CAP_S:
        print("!! SELF-LIMIT %.0fs exceeded at %s -- exit(3)" % (CAP_S, where))
        sys.exit(3)

ROOT = Path("$HOME/workspace/claudecode/automath")
SRC  = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()
print("impl source : %s  md5 %s" % (SRC, hashlib.md5(text.encode()).hexdigest()))

# ---- extract the three implementation functions verbatim (no retyping) -------
def grab(name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---))" % re.escape(name),
                  text, re.S | re.M)
    assert m, "could not extract def %s from %s" % (name, SRC)
    return m.group(0)

BLOB = "\n".join(grab(n) for n in ("stepA", "runA", "runB"))
print("extracted   : %d chars of implementation source, %d defs"
      % (len(BLOB), BLOB.count("\ndef ") + 1))
ns = {"Counter": Counter, "sorted": sorted}
exec(compile(BLOB, str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]

# ---- the diffed front door: nothing downstream calls runA or runB directly ---
DIFFED = 0
def run(lst):
    """(steps, residue) or (None, None).  A and B diffed on EVERY call."""
    global DIFFED
    a, b = runA(list(lst)), runB(list(lst))
    if a != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (lst, a, b))
        sys.exit(2)
    DIFFED += 1
    return a

def M(lam):
    w = max(lam)
    return [w] * (w + 1) + list(lam)

def s0(lam):     return run(M(lam))[0]
def resid(lam):  return run(M(lam))[1]
def is_step_seq(lst): return run(lst)[0] is not None

def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield []
        return
    for p in range(min(n, mx), 0, -1):
        for rest in parts(n - p, p):
            yield [p] + rest

# ================================================================= PART 0
# POSITIVE CONTROLS.  Every predicate must be shown to return True somewhere.
print()
print("=" * 78)
print("PART 0  --  positive AND negative controls, before any key value is computed")
print("=" * 78)

CTRL = []
def ctl(tag, got, want):
    ok = (got == want)
    CTRL.append(ok)
    print("   %-46s got %-14s want %-14s  %s"
          % (tag, repr(got), repr(want), "OK" if ok else "** FAIL"))
    return ok

# is_step_seq -- POSITIVE control (must be True) and NEGATIVE controls
ctl("is_step_seq([2,2,2,2]) [POSITIVE ctrl]", is_step_seq([2, 2, 2, 2]), True)
ctl("is_step_seq(M([2,2]))  [POSITIVE ctrl]", is_step_seq(M([2, 2])), True)
ctl("is_step_seq([1,1,1])   [negative]",      is_step_seq([1, 1, 1]), False)
ctl("is_step_seq(M([3,2]))  [negative, odd]", is_step_seq(M([3, 2])), False)

# the process itself, against values the DRAFT already carries (not held out)
ctl("T(4)=steps([4]^6)      [Lemma C1-A]",  run([4] * 6)[0], 4)
ctl("T(6)=steps([6]^8)      [Lemma C1-A]",  run([6] * 8)[0], 6)
ctl("V(1)=steps([1]^4)      [Lemma C1-A']", run([1] * 4)[0], 2)
ctl("V(5)=steps([5]^8)      [Lemma C1-A']", run([5] * 8)[0], 6)
ctl("s0((2,1,1))            [SS7.25 (d)]",  s0([2, 1, 1]), 3)
ctl("s0((5,3)) = w+1        [Thm C1-2]",    s0([5, 3]), 6)
ctl("C1-B identity on (5,3)",
    s0([5, 3]) == (5 + 1 + 2) - resid([5, 3]), True)

# alpha, with its own positive control
def alpha(nv, adj):
    best = 0
    for S in range(1 << nv):
        bits = [i for i in range(nv) if S >> i & 1]
        if len(bits) <= best:
            continue
        ok = True
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if adj[bits[i]] >> bits[j] & 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = len(bits)
    return best

def _cyc(n):
    adj = [0] * n
    for i in range(n):
        j = (i + 1) % n
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    return adj

def _cliq(n):
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj

ctl("alpha(K_5)             [POSITIVE ctrl, must be 1]", alpha(5, _cliq(5)), 1)
ctl("alpha(C_5)             [POSITIVE ctrl, must be 2]", alpha(5, _cyc(5)), 2)
ctl("alpha(C_6)                                       ", alpha(6, _cyc(6)), 3)
ctl("alpha(empty on 4)      [POSITIVE ctrl, must be 4]", alpha(4, [0] * 4), 4)

def min_alpha(seq):
    """min over ALL labelled realizations of `seq` of alpha(G); None if none."""
    nv = len(seq)
    tgt = sorted(seq, reverse=True)
    pairs = [(i, j) for i in range(nv) for j in range(i + 1, nv)]
    best = None
    seen = 0
    for mask in range(1 << len(pairs)):
        adj = [0] * nv
        for b, (i, j) in enumerate(pairs):
            if mask >> b & 1:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
        deg = sorted((bin(a).count("1") for a in adj), reverse=True)
        if deg != tgt:
            continue
        seen += 1
        a = alpha(nv, adj)
        if best is None or a < best:
            best = a
        if best == 1:
            break
    return best, seen

# min_alpha positive controls: a sequence whose ONLY realization is K_4, and one
# whose realizations are all edgeless.
ctl("min_alpha([3,3,3,3])   [POSITIVE ctrl, K_4 -> 1]", min_alpha([3, 3, 3, 3])[0], 1)
ctl("min_alpha([0,0,0])     [POSITIVE ctrl, -> 3]",     min_alpha([0, 0, 0])[0], 3)
ctl("min_alpha([2,2,2])     [C_3 -> 1]",                min_alpha([2, 2, 2])[0], 1)
# NEGATIVE control: a non-graphical sequence has NO realization -> None
# NOTE (own-instrument defect, recorded not smoothed): this control was FIRST WRITTEN
# with want=2 and FAILED.  The implementation was right and MY EXPECTATION was wrong --
# [3,1,1,1] is the star K_{1,3}, whose unique realization has alpha = 3 (the three
# leaves), not 2.  Kept here at its corrected value, with the incident on the record,
# because a control that cannot fail is not a control and this one demonstrably can.
ctl("min_alpha([3,1,1,1]) = star K_{1,3} -> 3",         min_alpha([3, 1, 1, 1])[0], 3)
ctl("min_alpha([1,1,1]) non-graphical -> None",         min_alpha([1, 1, 1])[0], None)
# the published Observation C1-E row, as an in-draft positive control
ce = min_alpha(M([3, 1]))
ctl("min_alpha(M((3,1))) = 3  [Obs C1-E, 180 realizations]", ce[0], 3)
ctl("realization count for M((3,1)) = 180",                  ce[1], 180)

print()
print("   controls run : %d ; passed : %d" % (len(CTRL), sum(CTRL)))
if not all(CTRL):
    print("!! a control failed -- NO key is produced.  exit(2)")
    sys.exit(2)
tick("part0")

# ================================================================= PART 1
# IMPL A/B diff on a declared population, BEFORE any key value is trusted.
print()
print("=" * 78)
print("PART 1  --  two-implementation diff on a declared population")
print("=" * 78)
pop = []
for n in range(1, 17):
    for lam in parts(n):
        pop.append(M(lam))
for w in range(0, 26):
    pop.append([w] * (w + 2))
    pop.append([w] * (w + 3))
print("   population : %d lists (every M(lambda) for n<=16, plus both proof shapes w<=25)"
      % len(pop))
for L in pop:
    run(L)
print("   A/B calls diffed so far : %d ; disagreements : 0 (any would have exited 2)"
      % DIFFED)
tick("part1")

# ================================================================= PART 2
# THE KEY.  Population printed for every row before its value.
print()
print("=" * 78)
print("PART 2  --  held-out key rows")
print("=" * 78)
KEY = {}

# ---- ROW-DETERMINATION AUDIT (RULING CP) runs FIRST: a row the brief pins to a
# ---- single value is STRUCK BEFORE DISPATCH, not graded and then excused.
print("   ROW-DETERMINATION AUDIT (RULING CP) -- struck rows are named, not hidden:")
print("      STRUCK  s0((7,4,1))          : = 8 = w+1, which is exactly what Theorem")
print("              C1-2's k=2 value and the (2,1,1) worked example both suggest.")
print("              A judge guessing 'w+1' scores it correct. Grades nothing. STRUCK.")
print("      STRUCK  min_alpha(M((6,2)))  : Observation C1-G pins it to >= 3 outright")
print("              (w+2=8 > 3c=6). The brief DETERMINES the interesting half. STRUCK.")
print("      STRUCK  T(w), V(c), any k<=2 s0 : pinned by Lemma C1-A / C1-A' / Thm C1-2.")
print("      KEPT    the six rows below, each with its shortcut value printed beside it.")
print()

# ---- A1 (hand) : s0((6,4,2)) -- k=3, and the w+1 shortcut is WRONG here
lam = [6, 4, 2]
print("   A1 population : the single list M((6,4,2)) = [6]^7 + [6,4,2], %d entries"
      % len(M(lam)))
KEY["A1"] = s0(lam)
sc = max(lam) + 1
print("      A1  s0((6,4,2)) = %s   shortcut 'w+1' = %s -> %s"
      % (KEY["A1"], sc, "COINCIDES, ROW IS WEAK" if KEY["A1"] == sc else "differs, row discriminates"))
assert KEY["A1"] != sc, "A1 coincides with the shortcut -- strike it"

# ---- A2 (hand) : residue(M((5,4,3)))
lam = [5, 4, 3]
print("   A2 population : the single list M((5,4,3)) = [5]^6 + [5,4,3], %d entries"
      % len(M(lam)))
KEY["A2"] = resid(lam)
print("      A2  residue(M((5,4,3))) = %s   shortcuts 'k' = %s and 'k+1' = %s -> %s"
      % (KEY["A2"], len(lam), len(lam) + 1,
         "differs from both, row discriminates"
         if KEY["A2"] not in (len(lam), len(lam) + 1) else "COINCIDES, ROW IS WEAK"))
assert KEY["A2"] not in (len(lam), len(lam) + 1), "A2 coincides with a shortcut"

# ---- A3 (hand) : an explicit list that is NOT of the M(lambda) shape
L3 = [4, 4, 3, 3, 2, 2]
print("   A3 population : the single explicit list %s (not of the M(lambda) shape,"
      " so no statement in the brief speaks to it)" % L3)
KEY["A3"] = run(L3)[0]
print("      A3  steps([4,4,3,3,2,2]) = %s   (residue %s)" % (KEY["A3"], run(L3)[1]))

# ---- B1 (computational) : min alpha over ALL realizations of M((2,2,1,1))
lam = [2, 2, 1, 1]
seq = M(lam)
print("   B1 population : ALL labelled graphs on %d vertices (2^%d masks), filtered to"
      " realizations of M((2,2,1,1)) = %s"
      % (len(seq), len(seq) * (len(seq) - 1) // 2, sorted(seq, reverse=True)))
b1, cnt = min_alpha(seq)
KEY["B1"] = b1
print("      B1  min_alpha = %s over %d realizations ; shortcut 'k' = %s -> %s"
      % (b1, cnt, len(lam),
         "differs, row discriminates" if b1 != len(lam) else "COINCIDES, ROW IS WEAK"))
assert b1 != len(lam), "B1 coincides with the shortcut"
print("          (k = 4 here, so this row also refutes the reading that C1-C's"
      " hypothesis is tight; nothing in the brief states this value)")

# ---- B2 (computational) : #{lambda |- 20, k>=2, residue(M) = k}
n = 20
tot = hit = 0
for lam in parts(n):
    if len(lam) < 2:
        continue
    r = resid(lam)
    if r is None:
        continue
    tot += 1
    if r == len(lam):
        hit += 1
print("   B2 population : %d partitions of %d with k>=2 and a terminating process" % (tot, n))
KEY["B2"] = hit
print("      B2  #{residue = k} = %s" % hit)
tick("B2")

# ---- B3 (computational) : #{lambda |- 22, k>=2, s0 = lambda_1 + 2}
n = 22
tot = hit = 0
for lam in parts(n):
    if len(lam) < 2:
        continue
    v = s0(lam)
    if v is None:
        continue
    tot += 1
    if v == max(lam) + 2:
        hit += 1
print("   B3 population : %d partitions of %d with k>=2 and a terminating process" % (tot, n))
KEY["B3"] = hit
print("      B3  #{s0 = lambda_1 + 2} = %s" % hit)
tick("B3")

print()
print("   A/B calls diffed in total : %d ; disagreements : 0" % DIFFED)

# ================================================================= PART 3
print()
print("=" * 78)
print("PART 3  --  key written")
print("=" * 78)
OUTK = ROOT / "problems/wowii/w61_r31_heldout_key.txt"
lines = ["# HELD-OUT KEY -- w61 round 31, SS7.25 two-family round (Q41 Qwen / Q42 Gemini)",
         "# Written %s.  NOT to appear in any brief." % time.strftime("%Y-%m-%d %H:%M"),
         ""]
for k in ("A1", "A2", "A3", "B1", "B2", "B3"):
    lines.append("%s = %s" % (k, KEY[k]))
OUTK.write_text("\n".join(lines) + "\n")
print("   wrote %s" % OUTK)
for k in ("A1", "A2", "A3", "B1", "B2", "B3"):
    print("      %s = %s" % (k, KEY[k]))
print()
print("elapsed %.1fs" % (time.time() - T0))
