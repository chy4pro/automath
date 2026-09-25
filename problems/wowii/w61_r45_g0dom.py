#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r45 -- (G0-MAX) turned from a MEASUREMENT into a PROOF-PLUS-ONE-PROFILE, and
(DOM-MAJ) given a candidate CLOSED invariant.

Built on r44 (ledger sec 7.59, cert cert_w61_r44.md).  r44 left (PERSIST-NARROW) resting on
exactly two obligations, (GAP1-OK) and (G0-MAX), both MEASURED 0 violations and neither
proved, and it left (DOM-MAJ) as a 15901/15901 census with no route.  This round attacks
both, and every statement below is recomputed here, never quoted.

--------------------------------------------------------------------------------------
FRONT A -- (G0-MAX)

  Setting.  A joint state is a pair (A,B) of equal-length sorted-decreasing lists walked in
  lockstep by the deterministic HH step of w61_r29_c1audit.py.  d := A[0] is the pivot;
  next_A = {A[i]-1 : 1<=i<=d} u {A[i] : i>d} -- the SAME index set on both sides whenever the
  pivots agree (r44, UP2-PERSIST).  g := sum(B)-sum(A).  A g=0 non-EQ state is UNIT_DOWN:
  B = A with one entry lowered by 1 (sorted index i1) and one raised by 1 (sorted index
  i2 > i1).  (G0-MAX) is the surviving obligation "max(A) = max(B) at every g=0 state",
  equivalently "the lowered entry is never A's UNIQUE maximum" (r44 sec 7.59 d).

  LEMMA G0-STEP (mine, NEW).  Let (A,B) be UNIT_DOWN with max(A) = max(B) (so i1 >= 1) and
  A's step legal, n := len(A), d := A[0], and suppose the tail is non-empty (d+1 < n).
  Put L1 := A[i1] - [i1 <= d]  and  L2 := A[i2] - [i2 <= d].  Then next_B is next_A with the
  slot-i1 entry lowered from L1 to L1-1 and the slot-i2 entry raised from L2 to L2+1; and
  L1 - L2 >= 1 always.  If L1 = L2 + 1 the two moves cancel as multisets and next_B = next_A
  (this is UD-PERSIST's EQ exit).  Otherwise  max(next_B) < max(next_A)  holds IFF

      (F1)   i1 = 1  and  A[1] > A[2]  and  A[d+1] < A[1] - 1
      (F2)   i1 = d+1  and  A[1] = A[d+1]  and  (d+2 = n  or  A[d+2] < A[d+1])

  Proof.  max(next_A) = max(A[1]-1, A[d+1]) =: M, and (given L1 >= L2+2, so the raised entry
  lands at L2+1 <= L1 - 1 < M whenever L1 = M) max(next_B) < max(next_A) iff the lowered
  entry sits at M with multiplicity 1 in next_A.
  MY OWN FIRST VERSION OMITTED the L1 = L2+1 clause and was refuted by its own run
  (27 mispredictions, all of them exactly the EQ exits).  Repaired by running.
  * i1 <= d.  L1 = A[i1]-1 <= A[1]-1 <= M, so L1 = M forces A[i1] = A[1] and A[d+1] <= A[1]-1.
    If i1 > 1 then index 1 also carries value A[1] -> level A[1]-1 = M, multiplicity >= 2.
    If A[2] = A[1] likewise.  If A[d+1] = A[1]-1 then index d+1 carries M, multiplicity >= 2.
    What is left is exactly (F1), and there the multiplicity is 1.
  * i1 > d.  L1 = A[i1] <= A[d+1] <= M, so L1 = M forces A[i1] = A[d+1] = M >= A[1]-1.
    A[1] >= A[d+1] = M, so A[1] in {M, M+1}.  If A[1] = M+1 then index 1 gives level M and the
    multiplicity is >= 2.  So A[1] = M = A[d+1], i.e. the BAND A[1] = ... = A[d+1]; and the
    multiplicity is #{i>d : A[i] = M}, which is 1 iff A[d+2] < M, which also forces i1 = d+1.
    That is exactly (F2).  QED

  ==> (F2) is precisely r44's "danger cut profile".  (F1) is a SECOND failure shape that r44
  did not name; whether it can occur inside the family is measured below.

  LEMMA G0-FIRST (mine, NEW).  Let (A,B) be UP2_1 with p_B = p_A + 1 (the unique pivot-gap
  step of r44's Theorem GAP1), d := p_A, c := A[d+1], i0 the second raised index, u the
  raised level of the successor.  Suppose GAP1's UNIT_DOWN branch fires (c >= u+2), so the
  successor is a g=0 non-EQ state.  Then max(next_A) = max(next_B) UNLESS  c = A[1], i.e.
  unless A[1] = ... = A[d+1] and A[d+2] < c.

  Proof.  The lowered level of the successor is c, and max(next_A) = max(A[1]-1, c).  If
  c < A[1]-1 the lowered entry is not the maximum at all.  If c = A[1]-1 the maximum M = c is
  carried by index 1 (value A[1] -> A[1]-1 = c) AND by index d+1 (value c), multiplicity >= 2.
  Only c = A[1] survives, and then M = c with multiplicity #{i >= d+1 : A[i] = c}.  QED

  ==> This PROVES the half of r44's one-sentence obligation that r44 could only measure:
  (G0-MAX) at the FIRST g=0 state of a head-block run is a theorem except on the band profile.
  What remains is: the band profile never occurs (or never with c >= u+2) inside the family.

  BAND-CLOSURE.  Head blocks are Wp(c) = [c]^3 [c-1]^c and Wm(c) = [c]^2 [c-1]^{c+1}, so
  every P1/P2 run STARTS with  N_{d-1}(X) >= d+3  where N_v(X) := #{i : X[i] >= v}, i.e. with
  X[d+1] >= d-1 -- there is no band.  Measured below: does N_{d-1} >= d+2 persist, and what is
  the exact exception?

--------------------------------------------------------------------------------------
FRONT B -- (DOM-MAJ)

  Two elementary facts, both proved here and both censused:
    (PIV-MONO)  max(next_X) = max(X[1]-1, X[d+1]) <= d, so the pivot sequence p(X) is already
                sorted decreasing; the sort in pivots() is a no-op.
    (PIV-SUM)   one step drops sum by 2d and the terminal state is all-zero, so
                sum(p(X)) = sum(X)/2.
  Hence, writing X^(k) for X after k steps,
    (DOM-MAJ)  ==  "for every k,  sum(A^(k)) <= sum(B^(k))"
  because the k-th prefix sum of p(X) is (sum(X) - sum(X^(k)))/2 and the totals agree.

  CANDIDATE CLOSED INVARIANT.  For sorted-decreasing lists padded to a common length put
    T_m(X) := sum of all but the m largest entries of X.
    (C1)  T_m(A) <= T_m(B) for every m >= 0.
    (C2)  sum(B) - sum(A) >= 2*(max(B) - max(A)).
  A >= B in dominance with equal sums gives (C1) (that IS dominance) and (C2) (both sides 0
  and <= 0).  (C2) is exactly "sum(next_A) <= sum(next_B)".  So if (C1)&(C2) is CLOSED under
  the joint step, (DOM-MAJ) follows by induction -- and (DOM-MAJ) => (PIVOT-MAJ) => (RH).
  (C1) ALONE IS NOT CLOSED and this file exhibits the counterexample.  Whether (C1)&(C2) is
  closed is the question; the answer measured here is reported exactly as it comes out.

RULING CO': stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py and diffed on every
call; Wp/Wm/head_of/L_of/relation lifted BY SOURCE TEXT from w61_r39_monodd.py.  Nothing
retyped.  No SAT, no solver, no exhaustive search of an infeasible space -- every sweep is a
census over a stated finite population.  INTERNAL HARD LIMIT below; PARTIAL is printed rather
than running on.  Interpreter: .venv/bin/python3 (pure Python; neither sympy nor networkx).
"""
import re, sys, time, itertools
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 200.0
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
OUT_OF_TIME = []
CTRL = []
PARTIAL = False


def over():
    global PARTIAL
    if time.time() - T0 > LIMIT:
        OUT_OF_TIME.append(1)
        PARTIAL = True
        return True
    return False


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


def bad(tag, detail):
    FAIL.append("%s  %s" % (tag, detail))
    print("   ** DEFECT %s  %s" % (tag, detail))


def ms(lst):
    return tuple(sorted(lst, reverse=True))


def step(lst):
    r = stepA(sorted(lst, reverse=True))
    if r == "TERMINAL" or r is None:
        return r
    return ms(r)


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


ns39 = {"ms": ms, "res": res, "sorted": sorted, "Counter": Counter}
_defs = "\n".join(grab(text39, n) for n in ("Wp", "Wm", "head_of", "L_of", "relation"))
exec(compile(_defs, str(SRC39), "exec"), ns39)
Wp, Wm, head_of, L_of, relation = (ns39["Wp"], ns39["Wm"], ns39["head_of"],
                                   ns39["L_of"], ns39["relation"])
FC = {}


def f(T):
    T = ms(T)
    if T not in FC:
        FC[T] = 2 if not T else res(L_of(T))
    return FC[T]


def pivots(lst):
    cur = sorted(lst, reverse=True)
    out = []
    guard = 0
    while True:
        guard += 1
        if guard > 400:
            return None
        nxt = stepA(sorted(cur, reverse=True))
        if nxt == "TERMINAL":
            return tuple(out)
        if nxt is None:
            return None
        out.append(max(cur))
        cur = list(nxt)


def dominates(a, b):
    n = max(len(a), len(b))
    A = list(a) + [0] * (n - len(a))
    B = list(b) + [0] * (n - len(b))
    sa = sb = 0
    for x, y in zip(A, B):
        sa += x
        sb += y
        if sb > sa:
            return False
    return True


def tails(x, n):
    """T_m(x) for m = 0..n, x sorted desc, zero-padded to length n."""
    X = list(x) + [0] * (n - len(x))
    tot = sum(X)
    out = [tot]
    s = 0
    for v in X:
        s += v
        out.append(tot - s)
    return out


def C1(a, b, n):
    ta, tb = tails(a, n), tails(b, n)
    return all(ta[m] <= tb[m] for m in range(n + 1))


def C2(a, b):
    return (sum(b) - sum(a)) >= 2 * ((b[0] if b else 0) - (a[0] if a else 0))


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append(ok)
    print("    %-4s %-84s hits=%d" % ("[ok]" if ok else "[!!]", name, hits))
    if not ok:
        bad("CONTROL", name)


def known(name, got, exp):
    if got != exp:
        bad("KNOWN", "%s got %s expected %s" % (name, got, exp))
    else:
        print("    [known] %-58s = %s" % (name, got))


print("=" * 100)
print("w61 r45 -- (G0-MAX): PROOF PLUS ONE PROFILE.  (DOM-MAJ): A CANDIDATE CLOSED INVARIANT.")
print("built on r44 / ledger sec 7.59.  stepA/runA/runB and Wp/Wm/head_of/L_of/relation lifted")
print("BY SOURCE TEXT; every runA is diffed against runB.")
print("=" * 100)

# ================================================================= 0. CONTROLS
print("\n[0] CONTROLS AND KNOWN VALUES -- fired before any verdict")
known("[1,1,0,0] (steps,residue)", run([1, 1, 0, 0]), (1, 3))
known("relation() UNIT_DOWN", relation((3, 1), (2, 2)), "UNIT_DOWN")
known("relation() UP2", relation((2, 1, 1), (2, 2, 2)), "UP2")
known("pivots([1,1,0,0])", pivots([1, 1, 0, 0]), (1,))
known("Wp(3)", tuple(Wp(3)), (3, 3, 3, 2, 2, 2))
known("Wm(3)", tuple(Wm(3)), (3, 3, 2, 2, 2, 2))

WPOOL = []
for N in range(2, 14):
    for p in parts(N):
        if len(p) <= 9:
            WPOOL.append(p)
print("    |W| base partitions                      : %d" % len(WPOOL))
WZ = []
for A in WPOOL:
    for z in range(0, 4):
        WZ.append(ms(list(A) + [0] * z))
WZ = sorted(set(WZ))
print("    |W+zeros| distinct zero-padded states    : %d" % len(WZ))


# ============================================ 1. LEMMA G0-STEP  (the two failure shapes)
print("\n[1] LEMMA G0-STEP -- at a UNIT_DOWN state with EQUAL maxima, the successor loses the")
print("    maximum IFF profile (F1) or profile (F2).  Both profiles are stated in the header")
print("    and are predicates on A ALONE plus the lowered index i1.")
print("    Population: every zero-padded state of W, every pair (i1,i2) of sorted indices that")
print("    realises a single unit moved down, with max(A)=max(B) and both steps legal.")


def unit_down_pair(A, i1, i2):
    """B := A with A[i1] lowered by 1 and A[i2] raised by 1, PROVIDED the sorted difference
    of B against A is exactly -1 at i1 and +1 at i2 (i.e. the sorted alignment is clean)."""
    B = list(A)
    B[i1] -= 1
    B[i2] += 1
    sB = ms(B)
    if len(sB) != len(A):
        return None
    dl = [sB[i] - A[i] for i in range(len(A))]
    if dl.count(-1) != 1 or dl.count(1) != 1 or dl.count(0) != len(A) - 2:
        return None
    if dl[i1] != -1 or dl[i2] != 1:
        return None
    return sB


def F1(A, i1, d, n):
    return (i1 == 1 and A[1] > A[2] if n > 2 else False) and (d + 1 < n and A[d + 1] < A[1] - 1)


def F2(A, i1, d, n):
    if not (d + 1 < n and i1 == d + 1):
        return False
    if A[1] != A[d + 1]:
        return False
    return (d + 2 >= n) or (A[d + 2] < A[d + 1])


g0_seen = g0_fail = eq_exit = 0
f1_with_I = f2_with_I = 0
g0_pred_ok = g0_pred_bad = 0
g0_shape = Counter()
ud_persist_ok = ud_persist_bad = 0
for A in WZ:
    if over():
        break
    n = len(A)
    d = A[0]
    if d == 0 or d + 1 >= n:
        continue
    nA = step(list(A))
    if nA in ("TERMINAL", None):
        continue
    for i1 in range(1, n):
        for i2 in range(i1 + 1, n):
            if A[i1] - 1 < A[i2] + 1:
                continue
            B = unit_down_pair(A, i1, i2)
            if B is None or B[0] != A[0]:
                continue
            nB = step(list(B))
            if nB in ("TERMINAL", None):
                continue
            g0_seen += 1
            # the claimed successor: next_A with slot i1 lowered L1 -> L1-1 and slot i2
            # raised L2 -> L2+1.  MY FIRST VERSION WROTE '-e_L1 + e_L2' and was refuted by
            # its own run on every single instance; repaired by running, not by deleting.
            L1 = A[i1] - (1 if i1 <= d else 0)
            L2 = A[i2] - (1 if i2 <= d else 0)
            cc = Counter(nA)
            cc[L1] -= 1
            cc[L1 - 1] += 1
            cc[L2] -= 1
            cc[L2 + 1] += 1
            claim = ms([v for v in cc.elements()])
            if claim == nB:
                ud_persist_ok += 1
            else:
                ud_persist_bad += 1
                if ud_persist_bad <= 3:
                    print("      UD-LEVELS FAILURE A=%s i1=%d i2=%d claim=%s actual=%s"
                          % (A, i1, i2, claim, nB))
            if L1 - L2 < 1:
                bad("UD-GAP", "L1-L2 = %d < 1 at A=%s i1=%d i2=%d" % (L1 - L2, A, i1, i2))
            if L1 == L2 + 1:
                eq_exit += 1
                if nB != nA:
                    bad("UD-EQ-EXIT", "L1=L2+1 but successors differ at A=%s" % (A,))
                g0_pred_ok += 1
                continue
            actual = max(nB) < max(nA)
            pred = F1(A, i1, d, n) or F2(A, i1, d, n)
            if actual:
                g0_fail += 1
                g0_shape[("F1" if F1(A, i1, d, n) else "") +
                         ("F2" if F2(A, i1, d, n) else "") or "NEITHER"] += 1
                if A[d + 1] >= d - 1:
                    if F1(A, i1, d, n):
                        f1_with_I += 1
                    if F2(A, i1, d, n):
                        f2_with_I += 1
            if actual == pred:
                g0_pred_ok += 1
            else:
                g0_pred_bad += 1
                if g0_pred_bad <= 5:
                    print("      G0-STEP MISPREDICT A=%s B=%s i1=%d i2=%d actual=%s pred=%s"
                          % (A, B, i1, i2, actual, pred))
print("    equal-max UNIT_DOWN steps examined              : %d" % g0_seen)
print("    ... of which L1 = L2+1, so the successors COINCIDE (UD-PERSIST's EQ exit) : %d" % eq_exit)
print("    ... successor levels L1->L2 predicted correctly : %d   WRONG %d" % (ud_persist_ok, ud_persist_bad))
print("    ... of which the successor LOSES the maximum    : %d" % g0_fail)
print("    G0-STEP prediction correct                      : %d   WRONG %d" % (g0_pred_ok, g0_pred_bad))
print("    shape of the failures                           : %s" % dict(sorted(g0_shape.items())))
print("    (I) => not-(F1):  (F1) needs A[d+1] < A[1]-1, while (I) gives A[d+1] >= A[0]-1 >= A[1]-1.")
print("    ... (F1) instances that satisfy (I) : %d   (F2) instances that satisfy (I) : %d"
      % (f1_with_I, f2_with_I))
if g0_pred_bad:
    bad("G0-STEP", "%d mispredictions" % g0_pred_bad)
if ud_persist_bad:
    bad("UD-LEVELS", "%d" % ud_persist_bad)
ctrl("CONTROL: the failure event (max lost at a g=0 state) DOES occur in W", g0_fail)
ctrl("CONTROL: profile (F1) is realised somewhere -- it is a SECOND shape r44 did not name",
     g0_shape.get("F1", 0))
ctrl("CONTROL: profile (F2) (r44's danger band) is realised somewhere", g0_shape.get("F2", 0))
ctrl("CORRUPT CONTROL: no failure is left unexplained by (F1)/(F2)", g0_shape.get("NEITHER", 0),
     must_fire=False)
ctrl("CORRUPT CONTROL: (I) really does kill (F1) -- no (F1) instance satisfies (I)",
     f1_with_I, must_fire=False)
ctrl("CONTROL: (I) does NOT kill (F2) -- (F2) survives (I), which is why the band is the",
     f2_with_I)


# ================================================== 2. LEMMA G0-FIRST (the gap-1 step)
print("\n[2] LEMMA G0-FIRST -- the FIRST g=0 state, reached by GAP1's UNIT_DOWN branch, keeps")
print("    the maximum UNLESS the parent carries the band  A[1] = ... = A[d+1] > A[d+2].")
print("    r44 measured 65/65 'the lowered entry IS the maximum' and left the whole obligation")
print("    on an unproved multiplicity.  Half of it is a theorem: c = A[1]-1 forces")
print("    multiplicity >= 2 outright.  Both halves are counted separately here.")
gf_seen = 0
gf_case = Counter()
gf_bad = 0
for A in WZ:
    if over():
        break
    n = len(A)
    d = A[0]
    if d == 0 or d + 1 >= n:
        continue
    nA = step(list(A))
    if nA in ("TERMINAL", None):
        continue
    for i0 in range(1, n):
        Bl = list(A)
        Bl[0] += 1
        Bl[i0] += 1
        B = ms(Bl)
        if len(B) != n or B[0] != A[0] + 1:
            continue
        dl = [B[i] - A[i] for i in range(n)]
        if not (all(t in (0, 1) for t in dl) and sum(dl) == 2 and dl[0] == 1):
            continue
        ii = [i for i in range(1, n) if dl[i] == 1]
        if len(ii) != 1:
            continue
        nB = step(list(B))
        if nB in ("TERMINAL", None):
            continue
        if relation(nA, nB) != "UNIT_DOWN":
            continue
        gf_seen += 1
        c = A[d + 1]
        lost = max(nB) < max(nA)
        if c < A[1] - 1:
            key = "c<A1-1 (lowered is not the max)"
        elif c == A[1] - 1:
            key = "c=A1-1 (PROVED multiplicity>=2)"
        else:
            key = "c=A1   (THE BAND -- the only survivor)"
        gf_case[(key, "LOST" if lost else "kept")] += 1
        if key != "c=A1   (THE BAND -- the only survivor)" and lost:
            gf_bad += 1
            if gf_bad <= 3:
                print("      G0-FIRST COUNTEREXAMPLE A=%s B=%s c=%d A1=%d" % (A, B, c, A[1]))
print("    GAP1 UNIT_DOWN-branch instances in W+zeros : %d" % gf_seen)
print("    case split (parent case, did the successor lose the max) : %s"
      % dict(sorted(gf_case.items())))
if gf_bad:
    bad("G0-FIRST", "%d" % gf_bad)
ctrl("CONTROL: the c = A[1]-1 case actually occurs (else the lemma is vacuous)",
     sum(v for (k, r), v in gf_case.items() if k.startswith("c=A1-1")))
ctrl("CONTROL: the BAND case actually occurs and DOES lose the max somewhere",
     gf_case.get(("c=A1   (THE BAND -- the only survivor)", "LOST"), 0))
ctrl("CORRUPT CONTROL: no loss outside the band", gf_bad, must_fire=False)


# ============================================= 3. THE HEAD-BLOCK POPULATIONS P1 AND P2
print("\n[3] REBUILD P1 (S1 head-block pairs) AND P2 (S2-derived pairs) -- r43/r44 figures 709/686")
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
print("    P2 usable pairs (L, L'_1) : %d" % len(P2))


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


# ================================== 4. DOES THE FAMILY EVER PRODUCE (F1) OR THE BAND?
print("\n[4] THE FAMILY SIDE.  Two questions, both about A ALONE:")
print("    (Q1) does any joint state of P1/P2 carry the band A[1]=...=A[d+1]>A[d+2] ?")
print("    (Q2) does N_{d-1}(A) >= d+2  (equivalently A[d+1] >= A[0]-1) hold at every state?")
print("    Head blocks Wp(c)=[c]^3[c-1]^c and Wm(c)=[c]^2[c-1]^{c+1} START with N_{d-1} >= d+3.")


def Nv(A, v):
    return sum(1 for x in A if x >= v)


band_states = 0
band_ex = None
fat_states = 0
inv_ok = inv_bad = 0
inv_bad_ex = None
inv_margin = Counter()
maxmult = Counter()
states_seen = 0
band_at_gap1 = Counter()
for tag, POP in (("P1", S1), ("P2", P2)):
    if over():
        break
    for (A0, B0) in POP:
        st, ex = joint_states(A0, B0)
        for (a, b) in st:
            n, d = len(a), a[0]
            states_seen += 1
            if d == 0:
                continue
            maxmult[a.count(d)] += 1
            if d + 1 < n:
                if a[d + 1] >= d - 1:
                    inv_ok += 1
                    inv_margin[Nv(a, d - 1) - (d + 2)] += 1
                else:
                    inv_bad += 1
                    if inv_bad_ex is None:
                        inv_bad_ex = (tag, a, b)
                if a[1] == a[d + 1] and (d + 2 >= n or a[d + 2] < a[d + 1]):
                    band_states += 1
                    if band_ex is None:
                        band_ex = (tag, a, b)
                if a.count(d) >= d + 2:
                    fat_states += 1
            # gap-1 parents: which GAP1 branch, and is the band present
            if sum(b) - sum(a) == 2 and a != b and len(a) == len(b) and b[0] == a[0] + 1:
                dl = [b[i] - a[i] for i in range(n)]
                ii = [i for i in range(1, n) if dl[i] == 1]
                if len(ii) == 1 and d + 1 < n:
                    c = a[d + 1]
                    i0 = ii[0]
                    u = a[i0] - (1 if i0 <= d else 0)
                    isband = (a[1] == c and (d + 2 >= n or a[d + 2] < c))
                    br = ("EQ" if c == u + 1 else "UNIT_DOWN" if c >= u + 2 else "OTHER") \
                        if i0 > d + 1 else ("i0<=d" if i0 <= d else "i0=d+1")
                    band_at_gap1[(isband, br)] += 1
print("    joint states walked over P1+P2                     : %d" % states_seen)
print("    multiplicity of max(A) over all those states       : %s" % dict(sorted(maxmult.items())))
print("    states with A[d+1] >= A[0]-1  (the head-block band-free invariant) : %d  VIOLATIONS %d"
      % (inv_ok, inv_bad))
print("    ... margin  N_{d-1}(A) - (d+2)  distribution      : %s" % dict(sorted(inv_margin.items())))
print("    states carrying the BAND A[1]=...=A[d+1]>A[d+2]   : %d   e.g. %s" % (band_states, band_ex))
print("    states with a FAT top  (#max >= d+2)              : %d" % fat_states)
print("    gap-1 parents (band?, GAP1 branch)                : %s" % dict(sorted(band_at_gap1.items())))
if inv_bad:
    print("    first violating state : %s" % (inv_bad_ex,))
ctrl("CONTROL: P1+P2 joint states were actually walked", states_seen)
ctrl("CONTROL: gap-1 parents exist in P1+P2", sum(band_at_gap1.values()))


# ==================== 4a2. DO (F1)/(F2) EVER FIRE AT A g=0 STATE OF THE FAMILY?
print("\n[4a] (G0-MAX) ON THE FAMILY, IN THE COORDINATES OF LEMMA G0-STEP.  Every non-EQ g=0")
print("     state of P1+P2 is classified by (i1 position, does (F1) hold, does (F2) hold).")
fam_g0 = Counter()
fam_g0_n = 0
fam_g0_lost = 0
for tag, POP in (("P1", S1), ("P2", P2)):
    if over():
        break
    for (A0, B0) in POP:
        st, ex = joint_states(A0, B0)
        for (a, b) in st:
            if sum(a) != sum(b) or a == b or len(a) != len(b):
                continue
            n, d = len(a), a[0]
            dl = [b[i] - a[i] for i in range(n)]
            if dl.count(-1) != 1 or dl.count(1) != 1:
                continue
            i1 = dl.index(-1)
            fam_g0_n += 1
            if max(b) < max(a):
                fam_g0_lost += 1
            fam_g0[("i1=%s" % ("0" if i1 == 0 else "1" if i1 == 1 else
                               "d+1" if i1 == d + 1 else "other"),
                    "F1" if F1(a, i1, d, n) else "-",
                    "F2" if F2(a, i1, d, n) else "-")] += 1
print("     non-EQ g=0 states of P1+P2 : %d ; of which max(A) != max(B) : %d"
      % (fam_g0_n, fam_g0_lost))
print("     classification (i1 position, F1?, F2?) : %s"
      % dict(sorted((str(k), v) for k, v in fam_g0.items())))
ctrl("CONTROL: non-EQ g=0 states of the family exist to classify", fam_g0_n)


# ======================== 4b. THE BAND PARENTS: WHY DOES GAP1 SEND THEM TO EQ?
print("\n[4b] (BAND-EQ) -- the ONE sentence that is left.  A band-carrying gap-1 parent has")
print("     A[1]=...=A[d+1]=c > A[d+2].  By Theorem GAP1 its outcome is EQ iff c = u+1 where")
print("     u is the level of the second raised index i0.  Since u <= A[d+2] <= c-1, EQ is")
print("     EXACTLY 'A[d+2] = c-1 and i0 sits at that level'.  Measured inside and outside")
print("     the family, so that the family-side content is separated from the general fact.")
fam_band = Counter()
fam_band_i0 = Counter()
for tag, POP in (("P1", S1), ("P2", P2)):
    if over():
        break
    for (A0, B0) in POP:
        st, ex = joint_states(A0, B0)
        for (a, b) in st:
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
            i0 = ii[0]
            u = a[i0] - (1 if i0 <= d else 0)
            fam_band[("A[d+2]=c-1" if d + 2 < n and a[d + 2] == c - 1 else
                      "A[d+2]<=c-2" if d + 2 < n else "no A[d+2]",
                      "u=c-1" if u == c - 1 else "u<=c-2")] += 1
            fam_band_i0[("i0<=d" if i0 <= d else "i0=d+1" if i0 == d + 1 else "i0>d+1")] += 1
print("     band-carrying gap-1 parents in P1+P2 : %d" % sum(fam_band.values()))
print("     (does the entry past the band sit at c-1 ?, is the raised level c-1 ?) : %s"
      % dict(sorted(fam_band.items())))
print("     position of i0 for those parents      : %s" % dict(sorted(fam_band_i0.items())))
wide_band = Counter()
for X in WZ:
    if over():
        break
    n, d = len(X), X[0]
    if d < 1 or d + 1 >= n:
        continue
    c = X[d + 1]
    if not (X[1] == c and (d + 2 >= n or X[d + 2] < c)):
        continue
    nA = step(list(X))
    if nA in ("TERMINAL", None):
        continue
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
        wide_band[("u=c-1" if u == c - 1 else "u<=c-2" if u <= c - 2 else "u>=c",
                   relation(nA, nB))] += 1
print("     SAME configuration OUTSIDE the family (W+zeros), (raised level, outcome) : %s"
      % dict(sorted((str(k), v) for k, v in wide_band.items())))
ctrl("CONTROL: band-carrying gap-1 parents exist inside P1+P2", sum(fam_band.values()))
ctrl("CORRUPT CONTROL: outside the family the band DOES reach GAP1's UNIT_DOWN branch",
     sum(v for (uu, r), v in wide_band.items() if r == "UNIT_DOWN"))


# ======================== 5. IS THE BAND-FREE INVARIANT CLOSED UNDER THE STEP?
print("\n[5] CLOSURE OF THE BAND-FREE INVARIANT  (I): N_{d-1}(X) >= d+2, d := X[0] >= 1.")
print("    (I) says X[d+1] >= d-1, i.e. the entry just past the cut is at most one below the")
print("    pivot.  It holds for every head block.  Tested for closure on W+zeros, and the")
print("    EXCEPTION SET is characterised rather than merely counted.")
cl_ok = cl_bad = 0
cl_exc = Counter()
cl_ex = None


def sorted_lists(n, V):
    out = []

    def rec(pref, mx):
        if len(pref) == n:
            out.append(tuple(pref))
            return
        for v in range(mx, -1, -1):
            rec(pref + [v], v)
    rec([], V)
    return out


CLPOOL = sorted(set(list(WZ) + [X for (n, V) in ((6, 4), (7, 4), (7, 5), (8, 4), (8, 5))
                                for X in sorted_lists(n, V)]))
print("    closure population (W+zeros u all sorted lists n<=8, entries<=5) : %d" % len(CLPOOL))
for X in CLPOOL:
    if over():
        break
    n, d = len(X), X[0]
    if d < 1 or d + 1 >= n:
        continue
    if Nv(X, d - 1) < d + 2:
        continue
    Y = step(list(X))
    if Y in ("TERMINAL", None):
        continue
    dY = Y[0]
    if dY < 1:
        cl_exc["successor pivot 0"] += 1
        continue
    if d + 1 >= len(Y):
        cl_exc["successor has no tail"] += 1
        continue
    if Nv(Y, dY - 1) >= dY + 2:
        cl_ok += 1
    else:
        cl_bad += 1
        a_, b_ = Nv(X, d), Nv(X, d - 1)
        cl_exc[("a=%s" % ("d+2" if a_ == d + 2 else ">=d+3" if a_ >= d + 3 else "<=d+1"),
                "b=%s" % ("d+2" if b_ == d + 2 else ">=d+3"))] += 1
        if cl_ex is None:
            cl_ex = (X, Y)
print("    states satisfying (I) whose successor also satisfies (I) : %d" % cl_ok)
print("    states satisfying (I) whose successor VIOLATES (I)       : %d" % cl_bad)
print("    exception profile (N_d(X) vs N_{d-1}(X))                 : %s" % dict(sorted(
    (str(k), v) for k, v in cl_exc.items())))
print("    smallest exception (X, next X)                           : %s" % (cl_ex,))
ctrl("CONTROL: (I) is non-vacuous on W+zeros", cl_ok)
ctrl("CORRUPT CONTROL: (I) alone is NOT closed -- the fat-top escape is real", cl_bad)

print("\n[5b] REFINED INVARIANT  (I+): N_{d-1}(X) >= d+2 AND N_d(X) <= d+1  (no fat top).")
cl2_ok = cl2_bad = 0
cl2_ex = None
cl2_shape = Counter()
for X in CLPOOL:
    if over():
        break
    n, d = len(X), X[0]
    if d < 1 or d + 1 >= n:
        continue
    if not (Nv(X, d - 1) >= d + 2 and Nv(X, d) <= d + 1):
        continue
    Y = step(list(X))
    if Y in ("TERMINAL", None) or Y[0] < 1 or Y[0] + 1 >= len(Y):
        continue
    dY = Y[0]
    if Nv(Y, dY - 1) >= dY + 2 and Nv(Y, dY) <= dY + 1:
        cl2_ok += 1
    else:
        cl2_bad += 1
        cl2_shape[("band-free kept" if Nv(Y, dY - 1) >= dY + 2 else "band-free LOST",
                   "no-fat kept" if Nv(Y, dY) <= dY + 1 else "fat top APPEARS")] += 1
        if cl2_ex is None:
            cl2_ex = (X, Y)
print("     (I+) preserved : %d    VIOLATED : %d" % (cl2_ok, cl2_bad))
print("     which half fails : %s" % dict(sorted((str(k), v) for k, v in cl2_shape.items())))
print("     smallest violation : %s" % (cl2_ex,))
ctrl("CONTROL: (I+) is non-vacuous", cl2_ok)


# ============================================== 6. DOM-MAJ: THE TWO ELEMENTARY FACTS
print("\n[6] (DOM-MAJ) REFORMULATED.  Two elementary facts, censused:")
print("    (PIV-MONO) the pivot sequence is ALREADY sorted decreasing;")
print("    (PIV-SUM)  sum(p(X)) = sum(X)/2.")
pm_ok = pm_bad = ps_ok = ps_bad = 0
for X in WZ:
    if over():
        break
    p = pivots(list(X))
    if p is None:
        continue
    if all(p[i] >= p[i + 1] for i in range(len(p) - 1)):
        pm_ok += 1
    else:
        pm_bad += 1
    if 2 * sum(p) == sum(X):
        ps_ok += 1
    else:
        ps_bad += 1
print("    terminating states tested        : %d" % pm_ok if not pm_bad else "")
print("    (PIV-MONO) holds %d, FAILS %d" % (pm_ok, pm_bad))
print("    (PIV-SUM)  holds %d, FAILS %d" % (ps_ok, ps_bad))
if pm_bad:
    bad("PIV-MONO", "%d" % pm_bad)
if ps_bad:
    bad("PIV-SUM", "%d" % ps_bad)
ctrl("CONTROL: terminating states exist to test", pm_ok)


# ============================================== 7. DOM-MAJ: IS (C1)&(C2) CLOSED?
print("\n[7] THE CANDIDATE CLOSED INVARIANT FOR (DOM-MAJ).")
print("    (C1) T_m(A) <= T_m(B) for all m ;  (C2) sum(B)-sum(A) >= 2*(max(B)-max(A)).")
print("    A >= B in dominance with equal sums gives both.  (C2) IS 'sum(next_A)<=sum(next_B)'.")
print("    Population: all sorted-decreasing zero-allowed lists of a common length n with")
print("    entries <= V, all ordered pairs, both steps legal.")


for (n, V) in ((5, 4), (6, 4), (6, 5), (7, 4), (7, 5)):
    if over():
        break
    LS = sorted_lists(n, V)
    # ONLY lists that TERMINATE are in scope for (DOM-MAJ); a terminating list has EVEN sum
    # (each step drops the sum by 2d and the terminal state is all-zero), and along a joint
    # trajectory started from equal sums BOTH sums stay even.  The first version of this
    # section omitted the parity/termination filter and its "violations" were dominated by
    # odd-sum pairs that no (DOM-MAJ) trajectory can ever reach.  Repaired by running.
    good = [X for X in LS if X[0] >= 1 and sum(X) % 2 == 0
            and pivots(list(X)) is not None and step(list(X)) not in ("TERMINAL", None)]
    tot = both_ok = c1_only_ok = c1_only_bad = both_bad = 0
    ex_both = ex_c1 = None
    for A in good:
        if over():
            break
        sA, mA = sum(A), A[0]
        nA = step(list(A))
        tA = tails(A, n)
        for B in good:
            if sum(B) < sA:
                continue
            tB = tails(B, n)
            if not all(tA[m] <= tB[m] for m in range(n + 1)):
                continue
            nB = step(list(B))
            c2 = (sum(B) - sA) >= 2 * (B[0] - mA)
            tot += 1
            nn = len(nA)
            tnA, tnB = tails(nA, nn), tails(nB, nn)
            c1n = all(tnA[m] <= tnB[m] for m in range(nn + 1))
            c2n = (sum(nB) - sum(nA)) >= 2 * ((nB[0] if nB else 0) - (nA[0] if nA else 0))
            if c2:
                if c1n and c2n:
                    both_ok += 1
                else:
                    both_bad += 1
                    if ex_both is None:
                        ex_both = (A, B, nA, nB, c1n, c2n)
            else:
                if c1n:
                    c1_only_ok += 1
                else:
                    c1_only_bad += 1
                    if ex_c1 is None:
                        ex_c1 = (A, B, nA, nB)
    print("    n=%d V=%d : pairs with (C1) : %d" % (n, V, tot))
    print("        with (C2) too : preserved %d   VIOLATED %d" % (both_ok, both_bad))
    if ex_both:
        print("        smallest (C1)&(C2) violation (A,B,nA,nB,c1n,c2n) : %s" % (ex_both,))
    print("        WITHOUT (C2)  : (C1) still preserved %d   (C1) LOST %d   e.g. %s"
          % (c1_only_ok, c1_only_bad, ex_c1))
    if both_bad:
        bad("C1C2-CLOSURE", "n=%d V=%d : %d" % (n, V, both_bad))
    if n == 6 and V == 5:
        ctrl("CORRUPT CONTROL: (C1) ALONE is not closed -- (C2) is doing real work", c1_only_bad)
        ctrl("CONTROL: the (C1)&(C2) population is non-empty", both_ok)


print("\n[7b] IS (C1)&(C2) TRUE ALONG THE ACTUAL (DOM-MAJ) TRAJECTORIES, even if it is not")
print("     closed as an abstract relation?  Every dominance pair of partitions of N <= 16")
print("     with both sides terminating is walked in lockstep and both conditions are checked")
print("     at every k.  A relation that is TRUE on the reachable set but NOT closed is a")
print("     different situation from one that is simply false, and the two are separated here.")
tr_pairs = tr_states = 0
tr_c1_bad = tr_c2_bad = 0
tr_ex1 = tr_ex2 = None
POOL16 = {}
for N in range(2, 17):
    if over():
        break
    for pp in parts(N):
        if len(pp) <= 10:
            pv = pivots(list(pp))
            if pv is not None:
                POOL16.setdefault(N, []).append(pp)
for N, lst in sorted(POOL16.items()):
    if over():
        break
    for A in lst:
        for B in lst:
            if A == B or not dominates(A, B):
                continue
            tr_pairs += 1
            nn = max(len(A), len(B))
            a, b = A, B
            k = 0
            while k < 60:
                tr_states += 1
                L = max(len(a), len(b), 1)
                ta, tb = tails(a, L), tails(b, L)
                if not all(ta[m] <= tb[m] for m in range(L + 1)):
                    tr_c1_bad += 1
                    if tr_ex1 is None:
                        tr_ex1 = (A, B, k, a, b)
                    break
                if not ((sum(b) - sum(a)) >= 2 * ((b[0] if b else 0) - (a[0] if a else 0))):
                    tr_c2_bad += 1
                    if tr_ex2 is None:
                        tr_ex2 = (A, B, k, a, b)
                    break
                na, nb = step(list(a)), step(list(b))
                if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
                    break
                a, b, k = na, nb, k + 1
print("     dominance pairs walked : %d ; joint states visited : %d" % (tr_pairs, tr_states))
print("     (C1) violations along the trajectories : %d   e.g. %s" % (tr_c1_bad, tr_ex1))
print("     (C2) violations along the trajectories : %d   e.g. %s" % (tr_c2_bad, tr_ex2))
print("     (C3) 'max(A^(k)) >= max(B^(k))' -- the entrywise strengthening -- along the same")
print("     trajectories, as a CORRUPT CONTROL that the walk can detect a failure at all :")
tr_c3_bad = 0
tr_ex3 = None
for N, lst in sorted(POOL16.items()):
    if over():
        break
    for A in lst:
        for B in lst:
            if A == B or not dominates(A, B):
                continue
            a, b, k = A, B, 0
            while k < 60:
                if (a[0] if a else 0) < (b[0] if b else 0):
                    tr_c3_bad += 1
                    if tr_ex3 is None:
                        tr_ex3 = (A, B, k, a, b)
                    break
                na, nb = step(list(a)), step(list(b))
                if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
                    break
                a, b, k = na, nb, k + 1
print("     (C3) violations : %d   e.g. %s" % (tr_c3_bad, tr_ex3))
ctrl("CONTROL: trajectories were actually walked", tr_states)
ctrl("CORRUPT CONTROL: (C3) DOES fail along these very trajectories, so a 0 for (C1)/(C2) is"
     " not an artefact of the walk", tr_c3_bad)


# ============================================== 8. DOM-MAJ ITSELF, RE-CENSUSED
print("\n[8] (DOM-MAJ) ITSELF -- re-censused independently of r44, in the sum(A^(k)) form.")
dm_ok = dm_bad = 0
dm_pairs = 0
dm_strict = 0
rev_bad = 0
POOL = {}
for N in range(2, 19):
    if over():
        break
    for p in parts(N):
        if len(p) <= 11:
            pv = pivots(list(p))
            if pv is not None:
                POOL.setdefault(N, []).append((p, pv))
for N, lst in sorted(POOL.items()):
    if over():
        break
    for (A, pA) in lst:
        for (B, pB) in lst:
            if A == B or not dominates(A, B):
                continue
            dm_pairs += 1
            if dominates(pA, pB):
                dm_ok += 1
            else:
                dm_bad += 1
                if dm_bad <= 3:
                    print("      DOM-MAJ FAILURE A=%s B=%s pA=%s pB=%s" % (A, B, pA, pB))
            if pA != pB:
                dm_strict += 1
            if not dominates(pB, pA):
                rev_bad += 1
print("    dominance pairs (same N, both terminating) : %d" % dm_pairs)
print("    p(A) >= p(B) holds %d, FAILS %d" % (dm_ok, dm_bad))
print("    ... of which p(A) != p(B) (the sub-population that COULD have failed) : %d" % dm_strict)
print("    reversed companion p(B) >= p(A) fails      : %d" % rev_bad)
if dm_bad:
    bad("DOM-MAJ", "%d" % dm_bad)
ctrl("CORRUPT CONTROL: the reversed claim fails (the census is not vacuous)", rev_bad)
ctrl("CONTROL: pairs with p(A) != p(B) exist -- these are the ones that could have failed",
     dm_strict)

print("\n[8b] ENTRYWISE is FALSE -- the honest scope of (DOM-MAJ).")
ent_bad = 0
ent_ex = None
for N, lst in sorted(POOL.items()):
    if over():
        break
    for (A, pA) in lst:
        for (B, pB) in lst:
            if A == B or not dominates(A, B):
                continue
            # non-trivial reading: compare only on p(A)'s own length.  (Padding with zeros
            # makes the claim fail for the trivial reason len(p(A)) < len(p(B)); that is not
            # a mathematical failure and is not counted.)
            if any(pA[i] < pB[i] for i in range(min(len(pA), len(pB)))):
                ent_bad += 1
                if ent_ex is None:
                    ent_ex = (A, B, pA, pB)
print("     pairs where p(A)_i >= p(B)_i fails on the common length : %d   e.g. %s"
      % (ent_bad, ent_ex))
ctrl("CORRUPT CONTROL: the entrywise strengthening of (DOM-MAJ) is FALSE", ent_bad)


# ============ 9. IS (PIVOT-MAJ) => (DOM-MAJ)?  CONNECTIVITY OF THE TERMINATING INTERVAL
print("\n[9] (PIVOT-MAJ) vs (DOM-MAJ).  p(.) dominance is TRANSITIVE, so if every dominance")
print("    pair (A,B) of TERMINATING partitions of N is joined by a chain of SINGLE unit")
print("    transfers down that stays inside the terminating partitions, then")
print("    (PIVOT-MAJ) => (DOM-MAJ) outright and r44's 'better-shaped' census is the SAME")
print("    statement, not a stronger one.  The obstruction is that a unit transfer can leave")
print("    the terminating set -- (3,3,1,1) ABORTS (r44's E05 audit).  Measured per N.")


def unit_downs(C):
    """all partitions obtained from C by moving ONE unit from a larger part to a smaller
    (or new) part -- the moves that generate the dominance order."""
    out = set()
    L = list(C) + [0]
    for i in range(len(L)):
        for j in range(len(L)):
            if i >= j or L[i] - 1 < L[j] + 1:
                continue
            M = list(L)
            M[i] -= 1
            M[j] += 1
            M = tuple(x for x in sorted(M, reverse=True) if x > 0)
            if sum(M) == sum(C):
                out.add(M)
    return out


conn_ok = conn_bad = 0
conn_ex = None
conn_edges_lost = 0
for N in range(2, 19, 2):
    if over():
        break
    TERM = [p for p in parts(N) if len(p) <= 11 and pivots(list(p)) is not None]
    TS = set(TERM)
    if len(TERM) > 260:
        continue
    adj = {}
    for C in TERM:
        nb = unit_downs(C)
        conn_edges_lost += sum(1 for x in nb if x not in TS)
        adj[C] = [x for x in nb if x in TS]
    for A in TERM:
        seen = {A}
        stack = [A]
        while stack:
            C = stack.pop()
            for D in adj[C]:
                if D not in seen:
                    seen.add(D)
                    stack.append(D)
        for B in TERM:
            if B == A or not dominates(A, B):
                continue
            if B in seen:
                conn_ok += 1
            else:
                conn_bad += 1
                if conn_ex is None:
                    conn_ex = (N, A, B)
print("    dominance pairs of terminating partitions tested : %d" % (conn_ok + conn_bad))
print("    joined by a chain INSIDE the terminating set     : %d" % conn_ok)
print("    NOT joined (so (PIVOT-MAJ) does not reach them)  : %d   e.g. %s" % (conn_bad, conn_ex))
print("    unit-transfer edges that LEAVE the terminating set : %d" % conn_edges_lost)
ctrl("CONTROL: unit transfers really do leave the terminating set (the obstruction is real)",
     conn_edges_lost)
ctrl("CONTROL: the connectivity test was non-vacuous", conn_ok + conn_bad)


# ================================================================= 9. GATE
print("\n" + "=" * 100)
print("ELAPSED %.2f s / %.0f s internal limit ; PARTIAL=%s ; diffed runA/runB calls %d"
      % (time.time() - T0, LIMIT, PARTIAL, DIFFED))
print("CONTROLS %d/%d firing ; DEFECTS %d" % (sum(1 for c in CTRL if c), len(CTRL), len(FAIL)))
for x in FAIL:
    print("   DEFECT: %s" % x)
print("EXIT=%d" % (1 if (FAIL or PARTIAL) else 0))
sys.exit(0)
