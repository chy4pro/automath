#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r49 ITEM A -- (BAND-EQ) on the odd half.  The obligation is SHARPENED from a
statement about a LEVEL to a statement about a POSITION, with an impossible middle range,
and r45's "54 out-of-family realisations" corrupt control is re-examined and CORRECTED.

Built on r45 (ledger sec 7.60) and r44's Theorem GAP1 (sec 7.59 b).  Every number below is
recomputed here; nothing is quoted from the ledger except as a `known(...)` reproduction.

------------------------------------------------------------------------------------------
THE SETTING (r44 Theorem GAP1, r45 (d)).  A joint state is a pair (A,B) of equal-length
sorted-decreasing lists walked in lockstep by the deterministic HH step.  A GAP-1 PARENT is
a UP2_1 joint state with p_B = p_A + 1: positionally B[i] = A[i] + delta_i with delta_0 = 1
and exactly one further index i0 >= 1 carrying delta_{i0} = 1.  Put d := A[0], c := A[d+1].
Theorem GAP1 (r44, PROVED) gives the outcome of the joint step:

    i0 <= d    : EQ iff A[i0] = c            (UNIT_DOWN impossible)
    i0 = d+1   : EQ always
    i0 >= d+2  : EQ iff c = u+1, UNIT_DOWN iff c >= u+2, OTHER iff c = u,  u := A[i0]

The BAND is the profile  A[1] = ... = A[d+1] = c  with  (d+2 = n  or  A[d+2] < c).
(BAND-EQ) (r45 (d)) is the surviving obligation: at every band-carrying gap-1 parent of a
head-block run, GAP1's EQ branch fires.  r45 left it MEASURED 100/100 in-family, with the
SAME configuration reaching UNIT_DOWN 54 times outside the family.

------------------------------------------------------------------------------------------
LEMMA BAND-POS (mine, NEW).  At a band-carrying gap-1 parent with d >= 1:

  (i)  i0 is NEVER in {2, ..., d+1}.
  (ii) i0 = 1  ==>  GAP1 gives EQ, unconditionally.
  (iii) i0 >= d+2  ==>  GAP1 gives EQ  IFF  A[i0] = c-1  IFF  (i0 = d+2 and A[d+2] = c-1).
  (iv) i0 > d+2   ==>  GAP1 gives UNIT_DOWN, always.

  Proof.
  (i) For 2 <= i0 <= d+1 the position i0-1 lies in [1, d] and is NOT raised, so
      B[i0-1] = A[i0-1] = c while B[i0] = A[i0] + 1 = c+1 > c, and B is not sorted. QED
      (The argument needs i0-1 >= 1: for i0 = 1 the predecessor IS raised, which is why
      i0 = 1 survives.  Position 0 gives B[0] = d+1 >= c+1 = B[1] since c <= d, so i0 = 1
      is always positionally admissible -- including when c = d.)
  (ii) i0 = 1 <= d, and GAP1's first row is EQ iff A[i0] = c; the band gives A[1] = c. QED
  (iii) GAP1's third row is EQ iff c = A[i0] + 1.  If A[i0] = c-1 then B sorted forces
      A[i0-1] >= A[i0] + 1 = c; but A[t] < c for every t >= d+2, so i0-1 <= d+1, i.e.
      i0 = d+2.  Conversely i0 = d+2 with A[d+2] = c-1 is the EQ case. QED
  (iv) i0 > d+2 gives A[i0] <= A[d+2] <= c-1, and A[i0] = c-1 is excluded by (iii), so
      A[i0] <= c-2, i.e. c >= u+2. QED

  ==> (BAND-EQ) IS NOW A POSITION STATEMENT:
      "at every band-carrying gap-1 parent of a head-block run, i0 = 1, or i0 = d+2 with
       A[d+2] = c-1."
  The middle range 2..d+1 is EXCLUDED BY SORTEDNESS ALONE, on every population.

------------------------------------------------------------------------------------------
WHAT THIS FILE DOES NOT DO.  It does not prove (BAND-EQ).  It removes one of the two ways
the obligation could have been stated and replaces r45's corrupt control with a corrected
one.  The residue is named in block [5] and is NOT closed.

RULING CO': stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py; Wp/Wm/head_of/
L_of/relation lifted BY SOURCE TEXT from w61_r39_monodd.py.  Nothing retyped.  No SAT, no
solver, no exhaustive search of an infeasible space -- every sweep is a census over a stated
finite population.  Interpreter: .venv/bin/python3 (pure Python; no sympy, no networkx).
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 240.0
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
SRC39 = ROOT / "problems/wowii/w61_r39_monodd.py"
text = SRC.read_text()
text39 = SRC39.read_text()


def grab(t, name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---|print|NMAX|absorb))" % re.escape(name),
                  t, re.S | re.M)
    assert m, name
    return m.group(0)


ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(text, n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]

DIFFED = 0
FAIL = []
CTRL = []
PARTIAL = False


def over():
    global PARTIAL
    if time.time() - T0 > LIMIT:
        PARTIAL = True
        return True
    return False


def ms(lst):
    return tuple(sorted(lst, reverse=True))


def run(lst):
    global DIFFED
    a, b = runA(list(lst)), runB(list(lst))
    if a != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (lst, a, b))
        sys.exit(2)
    DIFFED += 1
    return a


def res(lst):
    return run(lst)[1]


def step(lst):
    r = stepA(sorted(lst, reverse=True))
    if r == "TERMINAL" or r is None:
        return r
    return ms(r)


def bad(tag, detail):
    FAIL.append("%s  %s" % (tag, detail))
    print("   ** DEFECT %s  %s" % (tag, detail))


def ctrl(name, hits, must_fire=True):
    CTRL.append((name, hits, must_fire))
    ok = (hits > 0) if must_fire else True
    print("   [%s] %-78s hits=%d" % ("ok " if ok else "DEAD", name, hits))
    if must_fire and hits == 0:
        bad("DEAD CONTROL", name)


def known(name, got, want):
    tag = "ok " if got == want else "MISMATCH"
    print("   [%s] KNOWN VALUE %-58s got=%s want=%s" % (tag, name, got, want))
    if got != want:
        bad("KNOWN VALUE MISMATCH", "%s got=%s want=%s" % (name, got, want))


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


ns39 = {"ms": ms, "res": res, "sorted": sorted, "Counter": Counter}
exec(compile("\n".join(grab(text39, n) for n in ("Wp", "Wm", "head_of", "L_of", "relation")),
             str(SRC39), "exec"), ns39)
Wp, Wm, head_of, L_of, relation = (ns39["Wp"], ns39["Wm"], ns39["head_of"],
                                   ns39["L_of"], ns39["relation"])
FC = {}


def f(T):
    T = ms(T)
    if T not in FC:
        FC[T] = 2 if not T else res(L_of(T))
    return FC[T]


def joint_states(A0, B0, cap=90):
    a, b, k = A0, B0, 0
    out = []
    while k <= cap:
        out.append((a, b))
        if a == b:
            return out, "EQ"
        na, nb = step(list(a)), step(list(b))
        if na is None or nb is None:
            return out, "ABORT"
        if na == "TERMINAL" or nb == "TERMINAL":
            return out, "TERMINAL"
        a, b, k = na, nb, k + 1
    return out, "RUNAWAY"


print("=" * 100)
print("w61 r49 ITEM A -- (BAND-EQ): LEMMA BAND-POS, and r45's `54` corrected")
print("=" * 100)
print("interpreter: .venv/bin/python3 (pure Python, no sympy, no networkx)")

# =========================================================== 1. LEMMA BAND-POS, general
print("\n[1] LEMMA BAND-POS -- a census of EVERY band-carrying gap-1 configuration in a")
print("    stated finite population, at THREE sizes.  Predicted per the header:")
print("      i0 in {2..d+1}  IMPOSSIBLE ;  i0 = 1 -> EQ ;  i0 = d+2 -> EQ iff A[d+2]=c-1 ;")
print("      i0 > d+2 -> UNIT_DOWN.  Prediction is checked against relation(), which is")
print("    lifted by source text and knows nothing about the band.")

SIZES = [(13, 9, 3), (16, 10, 3), (20, 11, 2)]
SUMMARY = {}
for (NW, MP, ZP) in SIZES:
    if over():
        break
    POOL = [p for N in range(1, NW + 1) for p in parts(N) if len(p) <= MP]
    WZ = sorted(set(ms(list(A) + [0] * z) for A in POOL for z in range(0, ZP + 1)))
    pos = Counter()
    cross = Counter()
    mis = 0
    mid = 0
    nonEQ = []
    nband = 0
    for X in WZ:
        n, d = len(X), X[0]
        if d < 1 or d + 1 >= n:
            continue
        c = X[d + 1]
        if not (X[1] == c and (d + 2 >= n or X[d + 2] < c)):
            continue
        nA = step(list(X))
        if nA in ("TERMINAL", None):
            continue
        nband += 1
        for i0 in range(1, n):
            Bl = list(X)
            Bl[0] += 1
            Bl[i0] += 1
            B = ms(Bl)
            if len(B) != n or B[0] != X[0] + 1:
                continue
            dl = [B[i] - X[i] for i in range(n)]
            if not (all(t in (0, 1) for t in dl) and sum(dl) == 2 and dl[0] == 1):
                continue
            jj = [i for i in range(1, n) if dl[i] == 1]
            if len(jj) != 1:
                continue
            nB = step(list(B))
            if nB in ("TERMINAL", None):
                continue
            j0 = jj[0]
            u = X[j0] - (1 if j0 <= d else 0)
            r = relation(nA, nB)
            if 2 <= j0 <= d + 1:
                mid += 1
            key = ("i0=1" if j0 == 1 else "2<=i0<=d+1" if j0 <= d + 1
                   else "i0=d+2" if j0 == d + 2 else "i0>d+2")
            pos[key] += 1
            cross[(key, r)] += 1
            pred = "EQ" if (j0 == 1 or (j0 == d + 2 and d + 2 < n and X[d + 2] == c - 1)) \
                else "UNIT_DOWN"
            if pred != r:
                mis += 1
                if mis <= 3:
                    print("     MISPREDICTION A=%s B=%s i0=%d pred=%s got=%s" % (X, B, j0, pred, r))
            if r != "EQ":
                nonEQ.append((X, B, j0, d, c, u, r))
    print("    N<=%2d parts<=%2d zeros<=%d : |pop|=%-6d band states=%-4d configurations=%d"
          % (NW, MP, ZP, len(WZ), nband, sum(pos.values())))
    print("       i0 buckets                 : %s" % dict(sorted(pos.items())))
    print("       (bucket, relation)         : %s" % dict(sorted((str(k), v) for k, v in cross.items())))
    print("       BAND-POS mispredictions    : %d" % mis)
    print("       i0 landing in 2..d+1       : %d   (LEMMA BAND-POS (i): must be 0)" % mid)
    if mis:
        bad("BAND-POS", "N<=%d mispredictions=%d" % (NW, mis))
    if mid:
        bad("BAND-POS(i)", "N<=%d middle-range hits=%d" % (NW, mid))
    SUMMARY[NW] = (pos, cross, nonEQ, nband)

pos13, cross13, nonEQ13, nb13 = SUMMARY[13]
ctrl("CONTROL: the i0=1 bucket is non-empty (clause (ii) is exercised)", pos13["i0=1"])
ctrl("CONTROL: the i0=d+2 bucket is non-empty (clause (iii) is exercised)", pos13["i0=d+2"])
ctrl("CONTROL: the i0>d+2 bucket is non-empty (clause (iv) is exercised)", pos13["i0>d+2"])
ctrl("CORRUPT CONTROL: 'i0 in 2..d+1 occurs' -- must be DEAD, that is clause (i)",
     sum(v for (k, r), v in cross13.items() if k == "2<=i0<=d+1"), must_fire=False)
naive = sum(v for (k, r), v in cross13.items() if k in ("i0=d+2", "i0>d+2") and r != "EQ")
ctrl("CORRUPT CONTROL: the naive rule 'i0>=d+2 => EQ' mispredicts", naive)
known("N<=13 EQ configurations (r45's 336)",
      sum(v for (k, r), v in cross13.items() if r == "EQ"), 336)
known("N<=13 UNIT_DOWN configurations (r45's 54)",
      sum(v for (k, r), v in cross13.items() if r == "UNIT_DOWN"), 54)

# ==================================================== 2. THE FAMILY: P1, P2, the 100 parents
print("\n[2] THE FAMILY.  P1/P2 rebuilt, band-carrying gap-1 parents located, and each one")
print("    classified by LEMMA BAND-POS's trichotomy.")
NMAX = 18
S1 = []
S2rec = []
for N in range(1, NMAX + 1):
    if over():
        break
    for T in parts(N):
        if sum(T) % 2:
            pass
        else:
            continue
        for i in range(len(T)):
            U = list(T)
            U[i] += 1
            U = ms(U)
            isS1 = not (i == 0 or T[i] == T[0])
            a, b = f(T), f(U)
            if a is None or b is None:
                continue
            if isS1 and sum(T) <= 14:
                S1.append((ms(L_of(T)), ms(L_of(U))))
            if not isS1:
                S2rec.append((T[0], ms(T[1:])))
CT = sorted(set(S2rec))
known("P1 size", len(S1), 709)
known("P2 size", len(CT), 686)
P2 = []
for (c, tl) in CT:
    L = ms(Wm(c) + list(tl))
    Lp = ms(Wp(c + 1) + list(tl))
    L1 = step(list(Lp))
    if L1 in ("TERMINAL", None):
        continue
    P2.append((L, L1))

fam = []
fam_tag = Counter()
for tag, POP in (("P1", S1), ("P2", P2)):
    if over():
        break
    for (A0, B0) in POP:
        st, ex = joint_states(A0, B0)
        for idx, (a, b) in enumerate(st):
            n, d = len(a), a[0]
            if not (sum(b) - sum(a) == 2 and a != b and len(a) == len(b) and b[0] == a[0] + 1):
                continue
            if d + 1 >= n:
                continue
            dl = [b[i] - a[i] for i in range(n)]
            ii = [i for i in range(1, n) if dl[i] == 1]
            if len(ii) != 1:
                continue
            c = a[d + 1]
            if not (a[1] == c and (d + 2 >= n or a[d + 2] < c)):
                continue
            fam.append((tag, a, b, ii[0], d, c, idx))
            fam_tag[tag] += 1
known("family band-carrying gap-1 parents (r45's 100)", len(fam), 100)
print("    which population they come from      : %s" % dict(fam_tag))
fpos = Counter("i0=1" if r[3] == 1 else "2<=i0<=d+1" if r[3] <= r[4] + 1 else
               "i0=d+2" if r[3] == r[4] + 2 else "i0>d+2" for r in fam)
print("    LEMMA BAND-POS bucket                : %s" % dict(sorted(fpos.items())))
print("    c = d ?                              : %s"
      % dict(Counter("c=d" if r[5] == r[4] else "c<d" for r in fam)))
print("    A[d+2] = c-1 ?                       : %s"
      % dict(Counter("A[d+2]=c-1" if r[4] + 2 < len(r[1]) and r[1][r[4] + 2] == r[5] - 1
                     else "other" for r in fam)))
print("    #max(A) = d+2 ?                      : %s"
      % dict(Counter("m=d+2" if r[1].count(r[4]) == r[4] + 2 else "other" for r in fam)))
print("    exact A-shape [d]^{d+2}[d-1]^r + tail: %s"
      % dict(Counter("yes" if (r[1].count(r[4]) == r[4] + 2 and r[4] + 2 < len(r[1])
                               and r[1][r[4] + 2] == r[4] - 1) else "no" for r in fam)))
ctrl("CONTROL: family band parents exist", len(fam))
ctrl("CORRUPT CONTROL: 'some family band parent has i0=1' -- DEAD, they all use i0=d+2",
     fpos.get("i0=1", 0), must_fire=False)

# ======================================== 3. r45's `54`, RE-EXAMINED AND CORRECTED
print("\n[3] r45's `54` OUT-OF-FAMILY REALISATIONS, RE-EXAMINED.  r45 booked them as the")
print("    corrupt control showing (BAND-EQ) is a genuine FAMILY fact.  Item (a): are they")
print("    54 tests, and do they test what r45 said they test?")
UD13 = nonEQ13
print("    enumeration slots at N<=13                    : %d" % len(UD13))
print("    DISTINCT (A,B) pairs among them               : %d"
      % len(set((r[0], r[1]) for r in UD13)))
strip13 = set((tuple(x for x in r[0] if x > 0), tuple(x for x in r[1] if x > 0)) for r in UD13)
print("    DISTINCT pairs after deleting padded zeros    : %d" % len(strip13))
uvals13 = Counter(r[5] for r in UD13)
print("    the raised level u over those slots           : %s" % dict(sorted(uvals13.items())))
print("    slots whose raised entry IS a padded zero     : %d of %d"
      % (sum(1 for r in UD13 if r[0][r[2]] == 0), len(UD13)))
for a, b in sorted(strip13):
    print("       A*=%-30s B*=%-32s  parts %d -> %d" % (str(a), str(b), len(a), len(b)))
ctrl("CONTROL: r45's 54 slots were reproduced", len(UD13))
ctrl("CORRUPT CONTROL: 'some N<=13 failure has u>=1' -- DEAD; every one is a padded zero",
     sum(1 for r in UD13 if r[5] >= 1), must_fire=False)
print()
print("    THE SAME QUESTION AT LARGER SIZES -- direction fixed before reading (item d):")
print("    I predicted, in writing, that failures with u>=1 WOULD appear above N=13, on the")
print("    hand-built witness A=(3,3,3,3,3,1).  Both halves of that prediction are checked.")
for NW in (13, 16, 20):
    if NW not in SUMMARY:
        continue
    ud = SUMMARY[NW][2]
    st = set((tuple(x for x in r[0] if x > 0), tuple(x for x in r[1] if x > 0)) for r in ud)
    print("      N<=%2d : non-EQ slots=%-4d distinct (A,B)=%-4d stripped=%-3d  u>=1 slots=%d"
          % (NW, len(ud), len(set((r[0], r[1]) for r in ud)), len(st),
             sum(1 for r in ud if r[5] >= 1)))
u1 = [r for r in SUMMARY[20][2] if r[5] >= 1] if 20 in SUMMARY else []
ctrl("CONTROL: failures with u>=1 (NOT padding artefacts) exist above N=13", len(u1))
if u1:
    sm = min(u1, key=lambda r: (sum(r[0]), r[0]))
    print("    smallest u>=1 witness : A=%s B=%s i0=%d d=%d c=%d u=%d rel=%s"
          % (sm[0], sm[1], sm[2], sm[3], sm[4], sm[5], sm[6]))
    hand = (3, 3, 3, 3, 3, 1)
    print("    hand-built witness A=(3,3,3,3,3,1) present in the u>=1 set : %s"
          % any(tuple(x for x in r[0] if x > 0) == hand for r in u1))

# ============================================ 4. TWO CONJECTURES OF MINE, BOTH REFUTED
print("\n[4] TWO CANDIDATE FAMILY INVARIANTS OF MINE, BOTH REFUTED BY THIS RUN (booked, not")
print("    deleted).  (N1): A[m] = A[0]-1 at every joint state, m := #max(A).")
print("    (N2): the two raised positions are {m,m+1} (equal pivots) or {0,m} (gap step).")
n1 = Counter()
n2 = Counter()
ex1 = []
ex2 = []
for tag, POP in (("P1", S1), ("P2", P2)):
    if over():
        break
    for (A0, B0) in POP:
        st, ex = joint_states(A0, B0)
        for (a, b) in st:
            if a == b or len(b) != len(a):
                continue
            n, d = len(a), a[0]
            m = a.count(d)
            if m < n:
                n1["A[m]=d-1" if a[m] == d - 1 else "A[m]<=d-2"] += 1
                if a[m] < d - 1 and len(ex1) < 2:
                    ex1.append((tag, a, b))
            else:
                n1["m=n"] += 1
            dl = [b[i] - a[i] for i in range(n)]
            if not (all(t in (0, 1) for t in dl) and sum(dl) == 2):
                n2["not a positional 2-raise"] += 1
                continue
            rr = tuple(i for i in range(n) if dl[i] == 1)
            gap = (b[0] == a[0] + 1)
            lab = "{m,m+1}" if rr == (m, m + 1) else "{0,m}" if rr == (0, m) else "OTHER"
            n2[("gap1" if gap else "eqpiv", lab)] += 1
            if lab == "OTHER" and len(ex2) < 2:
                ex2.append((tag, a, b, rr, m))
print("    (N1) : %s" % dict(sorted(n1.items())))
print("    (N2) : %s" % dict(sorted((str(k), v) for k, v in n2.items())))
for e in ex1:
    print("      (N1) REFUTED, witness: %s" % (e,))
for e in ex2:
    print("      (N2) REFUTED, witness: %s" % (e,))
ctrl("REFUTATION: (N1) fails somewhere on the family", n1.get("A[m]<=d-2", 0))
ctrl("REFUTATION: (N2) fails somewhere on the family",
     sum(v for k, v in n2.items() if isinstance(k, tuple) and k[1] == "OTHER"))

# =========================================================== 5. WHAT IS NOT CLOSED
print("\n[5] WHAT THIS RUN FAILS TO CLOSE (item (b)).")
print("    (BAND-EQ) is NOT proved.  After LEMMA BAND-POS the residue is exactly:")
print("      at every band-carrying gap-1 parent of a head-block run, either i0 = 1, or")
print("      i0 = d+2 AND A[d+2] = c-1.")
print("    Measured on the family: %d of %d parents take the i0=d+2, A[d+2]=c-1 branch;" % (
    sum(1 for r in fam if r[3] == r[4] + 2 and r[4] + 2 < len(r[1]) and r[1][r[4] + 2] == r[5] - 1),
    len(fam)))
print("    %d take the i0=1 branch.  Neither branch is PROVED to be the one the family takes."
      % sum(1 for r in fam if r[3] == 1))
print("    LEMMA BAND-POS is a general lemma and does NOT use any family hypothesis, so it")
print("    cannot distinguish the family from the u>=1 counterexamples found in block [3].")
print("    (F2-FREE), (GAP1-OK), (PERSIST-NARROW), (MON), (S2), C1-W are untouched here.")

print("\n" + "=" * 100)
print("CONTROLS %d, all fired: %s" % (len(CTRL), all(h > 0 for _, h, mf in CTRL if mf)))
print("DEFECTS  %d" % len(FAIL))
for x in FAIL:
    print("   " + x)
print("diffed runA/runB calls: %d, disagreements: 0" % DIFFED)
print("PARTIAL=%s  elapsed %.2fs  (internal limit %.0fs)" % (PARTIAL, time.time() - T0, LIMIT))
print("=" * 100)
sys.exit(1 if FAIL else 0)
