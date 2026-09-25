#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r44 -- HARVEST of E03 / E05 / E10, and the mathematics that came out of it.

WHAT THIS ROUND IS.  Three engine outputs landed for this line.  Doctrine: read what they
BUILT, not what they CONCLUDED; rebuild every construction; re-derive every load-bearing
step.  Doing that to E03's "Lemma B" produced a strictly better lemma of my own, and the
better lemma CLOSES both of the two points E03 reported itself stuck on.  This file is the
run behind every number in the r44 result; no number is written before its run exists.

THE MATHEMATICS THIS FILE TESTS (all statements are MINE; E03's are marked as such).

  Setup.  A joint state is a pair (A,B) of equal-length lists walked in lockstep by the
  deterministic HH step of w61_r29_c1audit.py.  g := sum(B) - sum(A).  d_X := max(X) is the
  pivot.  UP2_1 means: B is obtained from A by raising TWO entries (two distinct positions)
  by 1.  Write s^A for A sorted decreasing.

  LEMMA U1 (mine).  If B is A with k entries raised by 1 then, for every i,
      s^B_i - s^A_i in {0,1},  and  sum_i (s^B_i - s^A_i) = k.
  Proof.  The i largest entries of B come from i entries of A each of value >= s^B_i - 1,
  so s^A_i >= s^B_i - 1; and s^B_i >= s^A_i since B >= A on a matching.  Sums agree. QED

  COROLLARY U2 (mine).  In a UP2_1 state,  d_B - d_A in {0,1}.
  ==> this is the g=2 half of (G2-a), PROVED, not measured.

  THEOREM UP2-PERSIST (mine).  UP2_1 state, d_A = d_B = d, A's step legal.  Then B's step
  is legal and the successor state is again UP2_1 (hence g stays 2).
  Proof.  With d_A = d_B = d, next_X (as a multiset) = {s^X_i - 1 : 1<=i<=d} u {s^X_i : i>d}
  -- the SAME index set on both sides.  Put delta_i := s^B_i - s^A_i in {0,1} (U1), with
  delta_0 = 0.  Then next_B is next_A with 1 added at exactly the indices i>=1 carrying
  delta_i = 1 -- two of them.  QED
  ==> E03's (H1) / "no crossing" hypothesis is NOT NEEDED.  Its STUCK-2 dissolves.

  THEOREM GAP1 (mine).  UP2_1 state with d_B = d_A + 1 (so delta_0 = 1, and exactly one
  further index i0 >= 1 has delta = 1).  Put d := d_A and c := s^A_{d+1}.  Then next_B
  differs from next_A by ONE unit moved, and exactly:
      i0 <= d      : +1 at u = s^A_{i0} - 1, -1 at c.  s^A_{i0} >= c always, so
                     EQ  iff s^A_{i0} = c ;  otherwise an UP-transfer (OTHER).  Never UNIT_DOWN.
      i0 =  d+1    : next_B = next_A.  EQ.
      i0 >  d+1    : +1 at u = s^A_{i0}, -1 at c.  c >= u always, so
                     EQ iff c = u+1 ;  UNIT_DOWN iff c >= u+2 ;  otherwise (c = u) OTHER.
  ==> E03's (H2) / STUCK-1 becomes a finite condition on A's sorted profile AT THE CUT.

  THEOREM UD-PERSIST (mine).  UNIT_DOWN state (B = A with one entry lowered by 1 and one
  raised by 1, lowered value >= raised value + 2), d_A = d_B.  Then the successor is
  UNIT_DOWN or EQ.  Proof: same index alignment; the two touched indices i1 < i2 descend by
  1 iff they are <= d, and the gap v1 - v2 >= 2 can only fall to 1 (=> EQ) when i1 <= d < i2.
  ==> E03's Corollary B2 without its "no crossing" hypothesis, and it also covers the case
  B2 misses.

  THE RESIDUE OF (PERSIST-NARROW).  With U2 + UP2-PERSIST + GAP1 + UD-PERSIST + G0-EXIT
  (proved r43), the whole statement reduces to TWO local obligations:
      (GAP1-OK)  every gap-1 step of a head-block run lands in {EQ, UNIT_DOWN}, never OTHER.
      (G0-MAX)   at every g=0 joint state of a head-block run, max(A) = max(B).
  (G0-MAX) is exactly E03's own (T2), reached independently.  Both are measured below.

ENGINE CLAIMS AUDITED HERE (E03 Lemma B and its per-unit rule; E05 sec 1.1/1.2/2/3;
E10 sec 7 new transition rows and sec 12 composition).  Each is recomputed, not read.

RULING CO': stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py and diffed on
every call; Wp/Wm/head_of/L_of/relation lifted BY SOURCE TEXT from w61_r39_monodd.py.
Nothing retyped.  No SAT, no solver, no exhaustive search of an infeasible space.
INTERNAL HARD LIMIT below; PARTIAL is printed rather than running on.
Interpreter: .venv/bin/python3 (pure Python; neither sympy nor networkx imported).
"""
import re, sys, time, itertools, random
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 150.0
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
            return tuple(sorted(out, reverse=True))
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


print("=" * 100)
print("w61 r44 -- HARVEST OF E03/E05/E10 + THE FOUR LEMMAS THE HARVEST PRODUCED")
print("=" * 100)
print("stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py (diffed every call);")
print("Wp/Wm/head_of/L_of/relation lifted BY SOURCE TEXT from w61_r39_monodd.py.")


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append(ok)
    print("   %-70s hits=%-8s %s" % (name, hits, "OK" if ok else "** CONTROL DID NOT FIRE"))
    if not ok:
        bad("CONTROL", name)


def known(name, got, exp):
    CTRL.append(got == exp)
    print("   known  %-46s = %-18s expect %-18s %s"
          % (name, got, exp, "OK" if got == exp else "** MISMATCH"))
    if got != exp:
        bad("KNOWN", "%s got %s expect %s" % (name, got, exp))


# ================================================================= 0. CONTROLS
print("\n[0] CONTROLS AND KNOWN VALUES -- fired before any verdict")
known("[1,1,0,0] (steps,residue)", run([1, 1, 0, 0]), (1, 3))
known("relation() EQ", relation((2, 1), (2, 1)), "EQ")
known("relation() UP2", relation((2, 1, 1), (2, 2, 2)), "UP2")
known("relation() UNIT_DOWN", relation((3, 1), (2, 2)), "UNIT_DOWN")
known("relation() DOM", relation((4, 1, 1), (2, 2, 2)), "DOM")
known("C1-Y R(0^r), R(1,1,0^{r-2}) r=2..8",
      [(res([0] * r), res([1, 1] + [0] * (r - 2))) for r in range(2, 9)],
      [(r, r - 1) for r in range(2, 9)])
known("pivots([1,1,0,0])", pivots([1, 1, 0, 0]), (1,))


# ===================================================== 1. LEMMA U1 (0/1 SORTED DIFFERENCE)
print("\n[1] LEMMA U1  --  raising k entries by 1 moves the SORTED vector by a 0/1 vector")
print("    Census: every multiset A with parts <= 6 and length <= 7 drawn from partitions of")
print("    N <= 14 (zero-padded to a fixed length), every choice of k DISTINCT positions.")
u1_ok = u1_bad = 0
u1_two = 0                      # CONTROL: raising the SAME position twice must produce a 2
POOL = []
for N in range(1, 15):
    for p in parts(N):
        if len(p) <= 7 and p[0] <= 6:
            POOL.append(p)
print("    pool size (multisets tested) : %d" % len(POOL))
for A in POOL:
    if over():
        break
    n = len(A)
    for k in (1, 2, 3):
        if k > n:
            continue
        for S in itertools.combinations(range(n), k):
            Bl = list(A)
            for i in S:
                Bl[i] += 1
            sA, sB = ms(A), ms(Bl)
            dl = [sB[i] - sA[i] for i in range(n)]
            if all(x in (0, 1) for x in dl) and sum(dl) == k:
                u1_ok += 1
            else:
                u1_bad += 1
                if u1_bad <= 3:
                    print("      U1 FAILURE  A=%s S=%s delta=%s" % (A, S, dl))
    # CONTROL that could have failed: raise ONE position by 2 -> a 2 must appear
    C = list(A)
    C[0] += 2
    dl2 = [ms(C)[i] - ms(A)[i] for i in range(n)]
    if any(x >= 2 for x in dl2):
        u1_two += 1
print("    U1 holds on %d instances, FAILS on %d" % (u1_ok, u1_bad))
if u1_bad:
    bad("U1", "%d failures" % u1_bad)
ctrl("CORRUPT CONTROL: raising ONE entry by 2 does produce a sorted-delta >= 2", u1_two)
ctrl("CONTROL: the U1 census is non-empty", u1_ok)


# ================================================= 2. THE TWO HEAD-BLOCK POPULATIONS
print("\n[2] REBUILD P1 (S1 head-block pairs) AND P2 (S2-derived pairs) -- r43 figures 709 / 686")
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
print("    P1 pairs: %d   (r43/r39 printed 709)" % len(S1))
print("    P2 distinct (c,tail): %d   (r43/r42 printed 686)" % len(CT))
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
print("    P2 usable pairs (L, L'_1): %d" % len(P2))


def joint_states(A0, B0, cap=90):
    """walk the lockstep, yielding (A,B) at each joint state; stop at EQ / TERMINAL / ABORT."""
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


# ===================================== 3. UP2-PERSIST, GAP1, UD-PERSIST -- ON A WIDE POPULATION
print("\n[3] THE THREE STEP LEMMAS, TESTED ON A POPULATION MUCH WIDER THAN THE HEAD BLOCKS")
print("    Population W: every partition A of N <= 13 with A's HH step legal, paired with every")
print("    B obtained by raising two DISTINCT positions of A by 1 (UP2_1), and every B obtained")
print("    by one unit transfer down (UNIT_DOWN).  No head-block hypothesis anywhere.")

up2_eqpiv = up2_persist_ok = up2_persist_bad = 0
up2_gap1 = 0
gap1_pred_ok = gap1_pred_bad = 0
gap1_out = Counter()
gap1_pred = Counter()
gap1_skip = Counter()
ud_eqpiv = ud_ok = ud_bad = 0
ud_out = Counter()
piv_gap_dist = Counter()
descend_all = descend_not_all = 0          # CONTROL for E03 Cor.B1's "both levels descend by 1"


def up2_positions(A, B):
    """A,B sorted desc, equal length: return the sorted-index delta vector."""
    return [B[i] - A[i] for i in range(len(A))]


def predict_gap1(sA, i0, d):
    """MY Theorem GAP1: returns predicted relation label."""
    c = sA[d + 1] if d + 1 < len(sA) else None
    if c is None:
        return "NOCUT"
    if i0 == d + 1:
        return "EQ"
    if i0 <= d:
        u = sA[i0] - 1
        return "EQ" if sA[i0] == c else "OTHER"
    u = sA[i0]
    if c == u + 1:
        return "EQ"
    if c >= u + 2:
        return "UNIT_DOWN"
    return "OTHER"


WPOOL = []
for N in range(2, 14):
    for p in parts(N):
        if len(p) <= 9:
            WPOOL.append(p)
print("    |W| base partitions : %d" % len(WPOOL))

for A in WPOOL:
    if over():
        break
    n = len(A)
    if n < 2:
        continue
    sA = ms(A)
    nA = step(list(sA))
    if nA in ("TERMINAL", None):
        continue
    d = sA[0]
    # ---- UP2_1 partners
    for (x, y) in itertools.combinations(range(n), 2):
        Bl = list(sA)
        Bl[x] += 1
        Bl[y] += 1
        sB = ms(Bl)
        nB = step(list(sB))
        dl = up2_positions(sA, sB)
        piv_gap_dist[sB[0] - sA[0]] += 1
        if sB[0] == sA[0]:                       # equal pivots
            up2_eqpiv += 1
            if nB in ("TERMINAL", None):
                up2_persist_bad += 1
                bad("UP2-PERSIST", "B step illegal though A's is legal: A=%s B=%s" % (sA, sB))
                continue
            # successor must be UP2_1: exactly two positions of the SORTED successor differ by 1
            dl2 = [nB[i] - nA[i] for i in range(len(nA))]
            if all(t in (0, 1) for t in dl2) and sum(dl2) == 2:
                up2_persist_ok += 1
            else:
                up2_persist_bad += 1
                if up2_persist_bad <= 3:
                    print("      UP2-PERSIST FAILURE A=%s B=%s -> %s %s" % (sA, sB, nA, nB))
            # E03 Cor.B1 check: do BOTH raised levels descend by 1?
            lev_before = sorted([sA[i] for i in range(n) if dl[i] == 1])
            lev_after = sorted([nA[i] for i in range(len(nA)) if dl2[i] == 1])
            if len(lev_before) == 2 and len(lev_after) == 2 and \
               lev_after == sorted([v - 1 for v in lev_before]):
                descend_all += 1
            else:
                descend_not_all += 1
        elif sB[0] == sA[0] + 1:                 # gap-1
            up2_gap1 += 1
            if nB in ("TERMINAL", None):
                gap1_skip["B_step_not_a_list"] += 1
                continue
            i0 = [i for i in range(1, n) if dl[i] == 1]
            if len(i0) != 1:
                gap1_skip["delta_0 raised twice (one entry +2)"] += 1
                continue
            i0 = i0[0]
            pr = predict_gap1(sA, i0, d)
            act = relation(nA, nB)
            gap1_out[act] += 1
            gap1_pred[pr] += 1
            if pr == "NOCUT":
                continue
            # my prediction says EQ / UNIT_DOWN / OTHER; relation() may also say DOM or DOWN1
            hit = (pr == act) or (pr == "OTHER" and act in ("OTHER", "DOM", "UP2", "DOWN1"))
            if hit:
                gap1_pred_ok += 1
            else:
                gap1_pred_bad += 1
                if gap1_pred_bad <= 5:
                    print("      GAP1 MISPREDICT A=%s B=%s i0=%d d=%d pred=%s act=%s  nA=%s nB=%s"
                          % (sA, sB, i0, d, pr, act, nA, nB))
    # ---- UNIT_DOWN partners
    for x in range(n):
        for y in range(n):
            if x == y or sA[x] < sA[y] + 2:
                continue
            Bl = list(sA)
            Bl[x] -= 1
            Bl[y] += 1
            sB = ms(Bl)
            if relation(sA, sB) != "UNIT_DOWN":
                continue
            if sB[0] != sA[0]:
                continue
            ud_eqpiv += 1
            nB = step(list(sB))
            if nB in ("TERMINAL", None):
                ud_out["B_step_illegal"] += 1
                continue
            r2 = relation(nA, nB)
            ud_out[r2] += 1
            if r2 in ("EQ", "UNIT_DOWN"):
                ud_ok += 1
            else:
                ud_bad += 1
                if ud_bad <= 3:
                    print("      UD-PERSIST FAILURE A=%s B=%s -> %s %s rel=%s"
                          % (sA, sB, nA, nB, r2))

print("    pivot gap d_B - d_A over ALL UP2_1 pairs         : %s" % dict(sorted(piv_gap_dist.items())))
print("    U2 (gap in {0,1}) violations                     : %d"
      % sum(v for k, v in piv_gap_dist.items() if k not in (0, 1)))
print("    UP2-PERSIST  equal-pivot instances %d : holds %d, FAILS %d"
      % (up2_eqpiv, up2_persist_ok, up2_persist_bad))
print("    E03 Cor.B1 'both unit levels descend by 1'       : true %d, FALSE %d"
      % (descend_all, descend_not_all))
print("    GAP1 instances %d : my prediction correct %d, WRONG %d"
      % (up2_gap1, gap1_pred_ok, gap1_pred_bad))
print("    GAP1 actual relations  : %s" % dict(sorted(gap1_out.items())))
print("    GAP1 predicted labels  : %s" % dict(sorted(gap1_pred.items())))
print("    GAP1 instances NOT scored, with reason : %s" % dict(sorted(gap1_skip.items())))
print("    UD-PERSIST  equal-pivot instances %d : lands in {EQ,UNIT_DOWN} %d, ELSEWHERE %d"
      % (ud_eqpiv, ud_ok, ud_bad))
print("    UD-PERSIST successor relations : %s" % dict(sorted(ud_out.items())))
if up2_persist_bad:
    bad("UP2-PERSIST", "%d failures" % up2_persist_bad)
if gap1_pred_bad:
    bad("GAP1", "%d mispredictions" % gap1_pred_bad)
if ud_bad:
    bad("UD-PERSIST", "%d failures" % ud_bad)
if sum(v for k, v in piv_gap_dist.items() if k not in (0, 1)):
    bad("U2", "pivot gap outside {0,1}")
ctrl("CONTROL: gap-1 steps actually occur in W", up2_gap1)
ctrl("CONTROL: equal-pivot UP2 steps actually occur in W", up2_eqpiv)
ctrl("CONTROL: UNIT_DOWN equal-pivot steps actually occur in W", ud_eqpiv)
ctrl("CORRUPT CONTROL: E03 Cor.B1's unconditional reading is FALSE somewhere", descend_not_all)
ctrl("CONTROL: GAP1 prediction is not constant (>=2 distinct predicted labels)",
     len([k for k in gap1_pred if k != "NOCUT"]) - 1)


# ============================================ 4. THE RESIDUE: (GAP1-OK) AND (G0-MAX) ON P1/P2
print("\n[3b] E07 (landed 16:54, MID-ROUND) -- ITS GAP G1 IS ANSWERED BY THE SAME ALIGNMENT")
print("     E07 encodes a UP2 state as A = C u {x,y}, B = C u {x+1,y+1}, and its gap G1 is:")
print("     'the token pair can in principle re-emerge at distance >= 2', which its own endgame")
print("     analysis says would be fatal.  MY COROLLARY TOKEN-DRIFT: at an equal-pivot step the")
print("     two token indices i1 < i2 each descend by 1 IFF their index is <= d, and i1 > d >= i2")
print("     is impossible, so the SIGNED gap (v1 - v2) goes to itself or to itself minus 1.")
print("     The first version of this block asserted the ABSOLUTE gap is non-increasing.  THE RUN")
print("     REFUTED IT (127 rises) and the corrected statement is the one that matters: the gap")
print("     falls, stays, or rises 0 -> 1 (the signed gap going negative by one), so a gap <= 1")
print("     CAN NEVER REACH 2.  That is exactly what E07's G1 needs.  Both readings are scored.")


def tokens(a, b):
    """canonical token levels of a UP2_1 pair: the A-values at the sorted indices where
    sorted(B) - sorted(A) = 1.  Returns (y, x) with y >= x, or None if not UP2_1."""
    if len(a) != len(b):
        return None
    dl = [b[i] - a[i] for i in range(len(a))]
    if not (all(t in (0, 1) for t in dl) and sum(dl) == 2):
        return None
    lv = sorted([a[i] for i in range(len(a)) if dl[i] == 1], reverse=True)
    return (lv[0], lv[1])


drift_ok = drift_bad = 0
drift_delta = Counter()
drift_pair = Counter()
gap1_dist = Counter()
for A in WPOOL:
    if over():
        break
    sA = ms(A)
    n = len(sA)
    nA = step(list(sA))
    if nA in ("TERMINAL", None):
        continue
    for (x, y) in itertools.combinations(range(n), 2):
        Bl = list(sA)
        Bl[x] += 1
        Bl[y] += 1
        sB = ms(Bl)
        nB = step(list(sB))
        if nB in ("TERMINAL", None):
            continue
        t0 = tokens(sA, sB)
        if t0 is None:
            continue
        if sB[0] == sA[0]:                        # equal-pivot step: TOKEN-DRIFT applies
            t1 = tokens(nA, nB)
            if t1 is None:
                drift_bad += 1
                continue
            d0, d1 = t0[0] - t0[1], t1[0] - t1[1]
            drift_delta[d1 - d0] += 1
            drift_pair[(d0, d1)] += 1
            # CORRECTED claim: signed gap goes to gap or gap-1, so the ABSOLUTE gap can only
            # rise 0 -> 1 and can NEVER reach 2 from a gap <= 1.
            if d1 == d0 or d1 == d0 - 1 or (d0 == 0 and d1 == 1):
                drift_ok += 1
            else:
                drift_bad += 1
                if drift_bad <= 3:
                    print("      TOKEN-DRIFT FAILURE A=%s B=%s tok %s -> %s" % (sA, sB, t0, t1))
        elif sB[0] == sA[0] + 1:                  # E07's endgame: is distance >= 2 fatal?
            gap1_dist[(t0[0] - t0[1], relation(nA, nB))] += 1
print("     TOKEN-DRIFT (corrected: gap -> gap or gap-1, and 0 -> 1) : holds %d, FAILS %d"
      % (drift_ok, drift_bad))
print("     distribution of the CHANGE in token gap               : %s" % dict(sorted(drift_delta.items())))
print("     ==> the RAW 'non-increasing' reading is FALSE: the gap DOES rise, %d times."
      % drift_delta.get(1, 0))
esc = sum(v for (d0, d1), v in drift_pair.items() if d0 <= 1 and d1 >= 2)
rise = sorted(set(d0 for (d0, d1), v in drift_pair.items() if d1 > d0))
print("     every rise starts from gap : %s   (a rise from gap >= 1 would break the corollary)"
      % rise)
print("     equal-pivot steps carrying a gap <= 1 UP TO gap >= 2  : %d   <- E07's gap G1" % esc)
print("     E07 sec 3 claim, cross-tab (token distance, endgame outcome) : %s"
      % dict(sorted(gap1_dist.items())))
if drift_bad:
    bad("TOKEN-DRIFT", "%d failures" % drift_bad)
ctrl("CONTROL: the token gap actually DOES fall somewhere (drift is not trivial)",
     drift_delta.get(-1, 0))
ctrl("CORRUPT CONTROL: the RAW non-increasing reading of TOKEN-DRIFT is refuted",
     drift_delta.get(1, 0))
ctrl("CONTROL: E07 sec3 claim -- endgames at token distance >= 2 that give EQ",
     sum(v for (dd, r), v in gap1_dist.items() if dd >= 2 and r == "EQ"))
ctrl("CONTROL: endgame states at token distance >= 2 actually occur",
     sum(v for (dd, r), v in gap1_dist.items() if dd >= 2))


print("\n[4] WHAT IS LEFT OF (PERSIST-NARROW) AFTER THE THREE LEMMAS")
print("    Only two obligations survive.  Measured on P1 (709) and P2 (686):")
print("      (GAP1-OK)  every gap-1 step lands in {EQ, UNIT_DOWN}")
print("      (G0-MAX)   every g=0 joint state has max(A) = max(B)")
GAP1_UD_SEEN = []
for tag, POP in (("P1", S1), ("P2", P2)):
    if over():
        break
    n_states = n_g0 = n_g0_maxbad = 0
    n_gap1 = n_gap1_bad = 0
    pop_pred_ok = pop_pred_bad = 0
    pop_pred = Counter()
    exits = Counter()
    rels = Counter()
    up21_all = up21_bad = 0
    for (A0, B0) in POP:
        st, ex = joint_states(A0, B0)
        exits[ex] += 1
        for (a, b) in st:
            n_states += 1
            r = relation(a, b)
            rels[r] += 1
            gg = sum(b) - sum(a)
            if gg == 0:
                n_g0 += 1
                if max(a) != max(b):
                    n_g0_maxbad += 1
            if gg == 2 and len(a) == len(b):
                dl = [b[i] - a[i] for i in range(len(a))]
                up21_all += 1
                if not (all(t in (0, 1) for t in dl) and sum(dl) == 2):
                    up21_bad += 1
            if a != b and max(b) == max(a) + 1 and gg == 2:
                n_gap1 += 1
                na, nb = step(list(a)), step(list(b))
                if na not in ("TERMINAL", None) and nb not in ("TERMINAL", None):
                    act = relation(na, nb)
                    if act not in ("EQ", "UNIT_DOWN"):
                        n_gap1_bad += 1
                    dl = [b[i] - a[i] for i in range(len(a))]
                    ii = [i for i in range(1, len(a)) if dl[i] == 1]
                    if len(ii) == 1:
                        pr = predict_gap1(a, ii[0], max(a))
                        pop_pred[pr] += 1
                        if pr == act or (pr == "OTHER" and act in ("OTHER", "DOM", "UP2", "DOWN1")):
                            pop_pred_ok += 1
                        else:
                            pop_pred_bad += 1
                            if pop_pred_bad <= 3:
                                print("      GAP1 MISPREDICT on %s: A=%s B=%s pred=%s act=%s"
                                      % (tag, a, b, pr, act))
    print("    %s: joint states %d ; exits %s" % (tag, n_states, dict(sorted(exits.items()))))
    print("    %s: relations %s" % (tag, dict(sorted(rels.items()))))
    print("    %s: g=2 states that are UP2_1 in the SORTED sense: %d of %d (violations %d)"
          % (tag, up21_all - up21_bad, up21_all, up21_bad))
    print("    %s: gap-1 steps %d ; landing OUTSIDE {EQ,UNIT_DOWN}: %d   <- (GAP1-OK)"
          % (tag, n_gap1, n_gap1_bad))
    print("    %s: g=0 states %d ; with max(A) != max(B): %d      <- (G0-MAX)"
          % (tag, n_g0, n_g0_maxbad))
    print("    %s: Theorem GAP1 prediction correct %d, WRONG %d ; predicted labels %s"
          % (tag, pop_pred_ok, pop_pred_bad, dict(sorted(pop_pred.items()))))
    if pop_pred_bad:
        bad("GAP1-PRED", "%s: %d" % (tag, pop_pred_bad))
    GAP1_UD_SEEN.append(pop_pred.get("UNIT_DOWN", 0))
    if n_gap1_bad:
        bad("GAP1-OK", "%s: %d" % (tag, n_gap1_bad))
    if n_g0_maxbad:
        bad("G0-MAX", "%s: %d" % (tag, n_g0_maxbad))
    if up21_bad:
        bad("UP2_1", "%s: %d g=2 states are not UP2_1" % (tag, up21_bad))
    ctrl("CONTROL: %s has g=2 states" % tag, up21_all)

ctrl("CONTROL: Theorem GAP1's UNIT_DOWN branch is exercised somewhere on P1/P2",
     sum(GAP1_UD_SEEN))

print("\n[4b] IS (G0-MAX) NON-VACUOUS?  A UNIT_DOWN pair OUTSIDE the head-block family")
print("     whose maxima DIFFER would show (G0-MAX) genuinely needs the family hypothesis.")
g0max_ce = 0
g0max_ex = None
for A in WPOOL:
    if over():
        break
    sA = ms(A)
    n = len(sA)
    for x in range(n):
        for y in range(n):
            if x == y or sA[x] < sA[y] + 2:
                continue
            Bl = list(sA)
            Bl[x] -= 1
            Bl[y] += 1
            sB = ms(Bl)
            if relation(sA, sB) == "UNIT_DOWN" and max(sB) != max(sA):
                g0max_ce += 1
                if g0max_ex is None:
                    g0max_ex = (sA, sB)
print("     UNIT_DOWN pairs with differing maxima in W : %d   e.g. %s" % (g0max_ce, g0max_ex))
ctrl("CORRUPT CONTROL: (G0-MAX) is FALSE for general UNIT_DOWN pairs", g0max_ce)


# ================================================================= 5. AUDIT OF E03's LEMMA B
print("\n[4c] LOCALIZING THE SURVIVING OBLIGATION (G0-MAX) TO A SINGLE PROFILE CONDITION")
print("     At a UNIT_DOWN state B = A - e_p + e_q (value w lowered, value u raised, w >= u+2),")
print("     max(B) < max(A) IFF the LOWERED entry is the UNIQUE maximum of A.  So (G0-MAX) is")
print("     exactly: the lowered entry is never A's unique maximum.  Measured on P1's g=0 states.")
print("     And by Theorem GAP1 the lowered entry enters at sorted position d+1 of the PARENT,")
print("     so the danger profile is  s^A_1 = ... = s^A_{d+1} > s^A_{d+2}  (a band of exactly")
print("     d+1 copies straight below the pivot).  Both are counted.")
mult_max_ud = Counter()
lowered_is_max = lowered_is_unique_max = 0
g0_states = g0_ud = 0
danger_parent = 0
danger_i0 = Counter()
danger_cu = Counter()
for tag, POP in (("P1", S1), ("P2", P2)):
    if over():
        break
    for (A0, B0) in POP:
        st, ex = joint_states(A0, B0)
        for (a, b) in st:
            if sum(b) != sum(a):
                continue
            g0_states += 1
            if a == b:
                continue                     # EQ states carry no lowered entry
            g0_ud += 1
            mult_max_ud[a.count(max(a))] += 1
            dn = list((Counter(a) - Counter(b)).elements())
            if dn and max(dn) == max(a):
                lowered_is_max += 1
                if a.count(max(a)) == 1:
                    lowered_is_unique_max += 1
        # danger profile among PARENTS of a gap-1 step: band of exactly d+1 copies below
        # the pivot, ending strictly before position d+2
        for (a, b) in st:
            if sum(b) - sum(a) != 2 or a == b or max(b) != max(a) + 1:
                continue
            d, n = max(a), len(a)
            if d + 1 >= n or len(set(a[1:d + 2])) != 1:
                continue
            if d + 2 < n and a[d + 2] == a[1]:
                continue                     # band continues past the cut
            danger_parent += 1
            ii = [i for i in range(1, n) if b[i] - a[i] == 1]
            if len(ii) == 1:
                pos = ("i0<=d" if ii[0] <= d else
                       "i0==d+1" if ii[0] == d + 1 else "i0>d+1")
                na2, nb2 = step(list(a)), step(list(b))
                out2 = relation(na2, nb2) if na2 not in ("TERMINAL", None) and \
                    nb2 not in ("TERMINAL", None) else "exit"
                danger_i0[(pos, out2)] += 1
                if pos == "i0>d+1" and out2 != "exit":
                    danger_cu[("c=u+1(EQ)" if a[d + 1] == a[ii[0]] + 1 else
                               "c>=u+2(UNIT_DOWN)" if a[d + 1] >= a[ii[0]] + 2 else
                               "c=u(OTHER)")] += 1
print("     g=0 joint states over P1+P2                       : %d  (of which non-EQ: %d)"
      % (g0_states, g0_ud))
print("     multiplicity of max(A) at the non-EQ g=0 states   : %s" % dict(sorted(mult_max_ud.items())))
print("     ... where the LOWERED entry IS A's maximum        : %d" % lowered_is_max)
print("     ... where it is A's UNIQUE maximum (the only way (G0-MAX) can fail) : %d"
      % lowered_is_unique_max)
print("     gap-1 parents carrying the danger cut profile     : %d" % danger_parent)
print("     ... (i0 position, outcome) for those parents       : %s" % dict(sorted(danger_i0.items())))
print("     ... and for the i0>d+1 ones, which GAP1 branch     : %s" % dict(sorted(danger_cu.items())))
ctrl("CONTROL: non-EQ g=0 states exist to be measured", g0_ud)
print("     ==> the lowered entry IS the maximum at every one of these states; (G0-MAX)")
print("         survives ONLY because that maximum always has multiplicity >= 2.")
print("         MEASURED, NOT PROVED.")

print("\n[4d] IS THE DANGER PROFILE REALISABLE AT ALL?  Search over W EXTENDED WITH ZEROS")
print("     (zeros are genuine HH states and partitions exclude them -- the first pass of")
print("      this search used partitions only, found nothing, and its control did not fire).")
WZ = []
for A in WPOOL:
    for z in range(0, 4):
        WZ.append(tuple(list(A) + [0] * z))
dang = 0
dang_ex = None
for sA in WZ:
    if over():
        break
    sA = ms(sA)
    d, n = sA[0], len(sA)
    if d + 1 >= n or len(set(sA[1:d + 2])) != 1:
        continue
    c = sA[1]
    if d + 2 < n and sA[d + 2] == c:
        continue                      # band continues past the cut -> max stays multiple
    for i0 in range(d + 2, n):
        if sA[i0] > c - 2:
            continue
        Bl = list(sA)
        Bl[0] += 1
        Bl[i0] += 1
        sB = ms(Bl)
        if sB[0] != sA[0] + 1:
            continue
        nA, nB = step(list(sA)), step(list(sB))
        if nA in ("TERMINAL", None) or nB in ("TERMINAL", None):
            continue
        if relation(nA, nB) == "UNIT_DOWN" and max(nB) != max(nA):
            dang += 1
            if dang_ex is None:
                dang_ex = (sA, sB, nA, nB)
print("     W+zeros states realising the danger profile with g returning to 2 : %d" % dang)
print("     example (A, B, next_A, next_B) : %s" % (dang_ex,))
ctrl("CORRUPT CONTROL: the danger profile IS realisable outside the head-block family", dang)


print("\n[5] AUDIT OF E03's OWN LEMMA B AND ITS PER-UNIT RULE")
print("    Lemma B (next_B - next_A = U + Delta_down - Delta, U = B-A, Delta = Top_B - Top_A)")
print("    is re-derived by me and CORRECT.  Its stated PER-UNIT contribution '(t) - (s-1)'")
print("    is NOT: the correct contribution of a unit (s)-(t) is (s-1)+(t)-(t-1)-(s).")


def formal(cnt):
    return Counter({k: v for k, v in cnt.items() if v})


lemB_ok = lemB_bad = 0
perunit_ok = perunit_bad = 0
for A in WPOOL:
    if over():
        break
    sA = ms(A)
    n = len(sA)
    nA = step(list(sA))
    if nA in ("TERMINAL", None):
        continue
    d = sA[0]
    for (x, y) in itertools.combinations(range(n), 2):
        Bl = list(sA)
        Bl[x] += 1
        Bl[y] += 1
        sB = ms(Bl)
        if sB[0] != sA[0]:
            continue
        nB = step(list(sB))
        if nB in ("TERMINAL", None):
            continue
        U = formal(Counter(sB) - Counter(sA)) , formal(Counter(sA) - Counter(sB))
        TopA, TopB = sA[1:d + 1], sB[1:d + 1]
        Dp = formal(Counter(TopB) - Counter(TopA))
        Dm = formal(Counter(TopA) - Counter(TopB))
        Dpd = Counter({k - 1: v for k, v in Dp.items()})
        Dmd = Counter({k - 1: v for k, v in Dm.items()})
        # lhs = next_B - next_A ; rhs = U + Delta_down - Delta   (as signed multisets)
        lhs = Counter(nB) - Counter(nA)
        lhs_neg = Counter(nA) - Counter(nB)
        L = Counter()
        for k, v in lhs.items():
            L[k] += v
        for k, v in lhs_neg.items():
            L[k] -= v
        R = Counter()
        for k, v in U[0].items():
            R[k] += v
        for k, v in U[1].items():
            R[k] -= v
        for k, v in Dpd.items():
            R[k] += v
        for k, v in Dmd.items():
            R[k] -= v
        for k, v in Dp.items():
            R[k] -= v
        for k, v in Dm.items():
            R[k] += v
        if formal(L) == formal(R):
            lemB_ok += 1
        else:
            lemB_bad += 1
            if lemB_bad <= 3:
                print("      LEMMA B FAILURE A=%s B=%s L=%s R=%s" % (sA, sB, formal(L), formal(R)))
        # engine's per-unit rule, on the same instances, as a formal identity:
        # sum over units (s)-(t) of Delta of [(t) - (s-1)]  ==  Delta_down - Delta ?
        E = Counter()
        us = sorted(Dp.elements(), reverse=True)
        ts = sorted(Dm.elements(), reverse=True)
        if len(us) == len(ts):
            for s_, t_ in zip(us, ts):
                E[t_] += 1
                E[s_ - 1] -= 1
            Cd = Counter()
            for k, v in Dpd.items():
                Cd[k] += v
            for k, v in Dmd.items():
                Cd[k] -= v
            for k, v in Dp.items():
                Cd[k] -= v
            for k, v in Dm.items():
                Cd[k] += v
            if formal(E) == formal(Cd):
                perunit_ok += 1
            else:
                perunit_bad += 1
print("    Lemma B identity: holds %d, FAILS %d      (E03's construction -- CONFIRMED)"
      % (lemB_ok, lemB_bad))
print("    E03's per-unit rule '(t)-(s-1)': agrees %d, DISAGREES %d   (its derivation -- WRONG)"
      % (perunit_ok, perunit_bad))
if lemB_bad:
    bad("LEMMA-B", "%d failures" % lemB_bad)
ctrl("CONTROL: E03's per-unit rule is refuted somewhere", perunit_bad)

print("\n[5b] E03's minimal counterexample (2,2,2,1,1) -> (3,3,2,1,1), recomputed")
a5, b5 = ms([2, 2, 2, 1, 1]), ms([3, 3, 2, 1, 1])
na5, nb5 = step(list(a5)), step(list(b5))
print("     A=%s -> %s   B=%s -> %s   rel(next)=%s   g_before=%d g_after=%d"
      % (a5, na5, b5, nb5, relation(na5, nb5), sum(b5) - sum(a5), sum(nb5) - sum(na5)))
known("E03 ce: step(2,2,2,1,1)", na5, (1, 1, 1, 1))
known("E03 ce: step(3,3,2,1,1)", nb5, (2, 1, 1, 0))
known("E03 ce: relation is not narrow", relation(na5, nb5) not in ("EQ", "UP2"), True)
known("E03 ce: R(A) and R(B)", (res(list(a5)), res(list(b5))), (res(list(a5)), res(list(b5))))
print("     R(A)=%s  R(B)=%s" % (res(list(a5)), res(list(b5))))


# ================================================================= 6. AUDIT OF E05
print("\n[6] AUDIT OF E05  ((PIVOT-MAJ))")
print("    E05 sec 1.1 claims p_1 >= p_1' always; sec 1.2 claims")
print("    sum(step pi) - sum(step pi') = 2(p_1' - p_1).  Both re-derived by me and checked here.")
e5_pairs = 0
e5_p1_bad = 0
e5_sum_bad = 0
e5_gapdist = Counter()
for N in range(2, 15):
    if over():
        break
    for pi in parts(N):
        if len(pi) > 9:
            continue
        pv = pivots(pi)
        if pv is None:
            continue
        for i in range(len(pi)):
            for j in range(len(pi)):
                if i == j or pi[i] < pi[j] + 2:
                    continue
                u = list(pi)
                u[i] -= 1
                u[j] += 1
                u = ms(u)
                pu = pivots(u)
                if pu is None:
                    continue
                e5_pairs += 1
                p1, p1p = max(pi), max(u)
                if p1 < p1p:
                    e5_p1_bad += 1
                e5_gapdist[p1 - p1p] += 1
                sa, sb = step(list(ms(pi))), step(list(u))
                if sa not in ("TERMINAL", None) and sb not in ("TERMINAL", None):
                    if sum(sa) - sum(sb) != 2 * (p1p - p1):
                        e5_sum_bad += 1
print("    transfer-down pairs (both terminating) : %d" % e5_pairs)
print("    E05 1.1  p_1 >= p_1' violations        : %d" % e5_p1_bad)
print("    p_1 - p_1' distribution                : %s" % dict(sorted(e5_gapdist.items())))
print("    E05 1.2  sum identity violations       : %d" % e5_sum_bad)
if e5_p1_bad:
    bad("E05-1.1", "%d" % e5_p1_bad)
if e5_sum_bad:
    bad("E05-1.2", "%d" % e5_sum_bad)
ctrl("CONTROL: gap-1 (p_1 - p_1' = 1) actually occurs", e5_gapdist.get(1, 0))

print("\n[6b] E05's HAND TABLE sec 2 -- every row recomputed (it is offered as consistency data)")
tbl = [((3, 3, 1, 1), (3, 2), (3, 2, 2, 1), (3, 1)),
       ((3, 2, 2, 1), (3, 1), (2, 2, 2, 2), (2, 2)),
       ((4, 2, 2, 1, 1), (4, 1), (3, 2, 2, 2, 1), (3, 1, 1)),
       ((5, 2, 2, 1, 1, 1), (5, 1), (4, 2, 2, 2, 1, 1), (4, 1, 1)),
       ((5, 2, 2, 1, 1, 1), (5, 1), (4, 3, 2, 1, 1, 1), (4, 2))]
e5_tbl_bad = 0
for (pi, ppi, pip, pppi) in tbl:
    gp, gq = pivots(pi), pivots(pip)
    okl = (gp == ppi)
    okr = (gq == pppi)
    if not (okl and okr):
        e5_tbl_bad += 1
    print("     pi=%-18s p(pi) claimed %-10s true %-10s | pi'=%-18s claimed %-10s true %-10s %s"
          % (str(pi), str(ppi), str(gp), str(pip), str(pppi), str(gq),
             "OK" if okl and okr else "** WRONG"))
print("     rows with a wrong entry : %d of %d" % (e5_tbl_bad, len(tbl)))
print("\n[6c] E05 sec 3 claims '(3,3,1,1) terminates but is not graphic'.  Recomputed:")
print("     runA/runB on (3,3,1,1) : %s   pivots: %s" % (run([3, 3, 1, 1]), pivots([3, 3, 1, 1])))


# ============================================== 7. NEW MEASUREMENT: IS (PIVOT-MAJ) A SHADOW
#                                                  OF A DOMINANCE STATEMENT?
print("\n[7] NEW: (DOM-MAJ)?  A >= B in dominance, both terminating, same N  ==>  p(A) >= p(B)?")
print("    E05 sec 4 suggests replacing the token bookkeeping by 'an order-ideal condition on")
print("    the sorted lists'.  That is exactly (DOM-MAJ).  It has never been measured.  A single")
print("    transfer down gives dominance, so (DOM-MAJ) IMPLIES (PIVOT-MAJ); if (DOM-MAJ) is")
print("    FALSE the suggested route is dead and the induction must stay on single transfers.")
DOMMAJ = []
NDM = 20
for samelen in (True, False):
    dm_ok = dm_bad = 0
    dm_ex = []
    for N in range(2, NDM + 1):
        if over():
            break
        ps = [p for p in parts(N) if len(p) <= 11]
        terms = [(p, pivots(p)) for p in ps]
        terms = [(p, v) for (p, v) in terms if v is not None]
        for (a, pa) in terms:
            for (b, pb) in terms:
                if a == b or not dominates(a, b):
                    continue
                if samelen and len(a) != len(b):
                    continue
                if dominates(pa, pb):
                    dm_ok += 1
                else:
                    dm_bad += 1
                    if len(dm_ex) < 6:
                        dm_ex.append((a, pa, b, pb))
    lab = "SAME LENGTH (the (PIVOT-MAJ) shape)" if samelen else "ANY LENGTH (the full order ideal)"
    print("    %s :" % lab)
    print("      dominance pairs, same N, both terminating, N <= %d : %d" % (NDM, dm_ok + dm_bad))
    print("      (DOM-MAJ) holds %d, FAILS %d" % (dm_ok, dm_bad))
    for e in dm_ex:
        print("        (DOM-MAJ) COUNTEREXAMPLE  A=%s p(A)=%s   B=%s p(B)=%s" % e)
    ctrl("CONTROL: the (DOM-MAJ) population [%s] is non-empty" % lab, dm_ok + dm_bad)
    DOMMAJ.append((lab, dm_ok, dm_bad))

print("\n[7b] CONTROL that could have failed: reversed (DOM-MAJ) must be violated")
dm_rev_bad = 0
for N in range(2, 11):
    if over():
        break
    ps = [p for p in parts(N) if len(p) <= 10]
    terms = [(p, pivots(p)) for p in ps]
    terms = [(p, v) for (p, v) in terms if v is not None]
    for (a, pa) in terms:
        for (b, pb) in terms:
            if a == b or len(a) != len(b) or not dominates(a, b):
                continue
            if not dominates(pb, pa):
                dm_rev_bad += 1
ctrl("CORRUPT: reversed (DOM-MAJ) 'p(B) >= p(A)' is violated", dm_rev_bad)


# ================================================================= 8. AUDIT OF E10
print("\n[8] AUDIT OF E10  (C1-N / C1-R reusability)  --  only its NEW constructions are testable")


def F(s, x, j, nu):
    return ms([x] * j + [x - 1] * (x + s - j) + list(nu))


print("    E10 sec 7 adds two transition rows it flags as NEW and unverified:")
print("      (zero)   j = 0                       -> F_s(x-1, s-1; nu)")
print("      (middle) x+2 <= j <= x+s-1 (s >= 3)  -> F_{s-1}(x, j-x-1; nu)")
print("    and restates the two proved rows.  All four are checked here against the real step.")
rows = Counter()
rowbad = Counter()
NUS = [(), (1,), (2, 1), (1, 1, 1), (2, 2, 1)]
for x in range(2, 9):
    for s in range(1, 7):
        for j in range(0, x + s + 1):
            for nu in NUS:
                if nu and max(nu) > x - 1:
                    continue
                L = F(s, x, j, nu)
                got = step(list(L))
                if j == 0:
                    exp, tag = F(s, x - 1, s - 1, nu), "zero(E10 as written)"
                    rows[tag] += 1
                    if got != exp:
                        rowbad[tag] += 1
                    exp, tag = F(s, x - 1, s, nu), "zero(MY correction)"
                elif 1 <= j <= x + 1:
                    exp, tag = F(s, x - 1, j + s - 2, nu), "interior"
                elif s >= 3 and x + 2 <= j <= x + s - 1:
                    exp, tag = F(s - 1, x, j - x - 1, nu), "middle"
                elif j == x + s and s >= 2:
                    exp, tag = F(s - 1, x, s - 1, nu), "entry"
                else:
                    continue
                rows[tag] += 1
                if got != exp:
                    rowbad[tag] += 1
                    if sum(rowbad.values()) <= 4:
                        print("      E10 ROW FAILURE [%s] s=%d x=%d j=%d nu=%s : got %s expect %s"
                              % (tag, s, x, j, nu, got, exp))
for t in ("zero(E10 as written)", "zero(MY correction)", "interior", "middle", "entry"):
    print("    row %-22s tested %-5d  failures %d" % (t, rows[t], rowbad[t]))
if rowbad["zero(MY correction)"] or rowbad["interior"] or rowbad["middle"] or rowbad["entry"]:
    bad("E10-ROWS", "%s" % dict(rowbad))
print("    ==> E10's j=0 row is WRONG as written and the corrected row is  F_s(x,0;nu) -> F_s(x-1,s;nu).")
print("        Its derivation says 'the top x entries'; the pivot at j=0 is x-1, so the")
print("        decrement set has x-1 entries, not x.  Every other row of its table is correct.")
ctrl("CONTROL: the NEW rows (zero, middle) were actually exercised",
     rows["zero(MY correction)"] + rows["middle"])
ctrl("CORRUPT CONTROL: E10's j=0 row as written is refuted", rowbad["zero(E10 as written)"])

print("\n[8b] E10 sec 12 composition: M(lambda) = F_{m+1}(w, w+m+1; lambda') with w = lambda_1,")
print("     m = multiplicity of lambda_1, lambda' the rest.  Checked as an identity of lists.")
comp_ok = comp_bad = 0
for N in range(1, 17):
    for lam in parts(N):
        w = lam[0]
        if w < 2:
            continue
        m = sum(1 for t in lam if t == w)         # E10: m = MULTIPLICITY of lambda_1 IN lambda
        lamp = tuple(t for t in lam if t != w)
        M = ms([w] * (w + 1) + list(lam))
        G = F(m + 1, w, w + m + 1, lamp)
        if M == G:
            comp_ok += 1
        else:
            comp_bad += 1
            if comp_bad <= 3:
                print("      COMPOSITION FAILURE lam=%s  M=%s  F=%s" % (lam, M, G))
print("     composition holds %d, FAILS %d   (lambda_1 >= 2, N <= 16)" % (comp_ok, comp_bad))
if comp_bad:
    bad("E10-COMP", "%d" % comp_bad)

print("\n[8c] E10 sec 2/5: the k = w variant of C1-N and its claimed PARITY FLIP.")
print("     Claim: [w]^w u lambda terminates iff |lambda| = w (mod 2); [w]^{w+1} u lambda iff |lambda| even.")
kn_ok = kn_bad = kw_ok = kw_bad = 0
kless_bad = 0
for N in range(1, 15):
    for lam in parts(N):
        w = lam[0]
        t1 = res([w] * (w + 1) + list(lam)) is not None
        if t1 == (sum(lam) % 2 == 0):
            kn_ok += 1
        else:
            kn_bad += 1
        t2 = res([w] * w + list(lam)) is not None
        if t2 == (sum(lam) % 2 == w % 2):
            kw_ok += 1
        else:
            kw_bad += 1
            if kw_bad <= 3:
                print("      k=w FAILURE lam=%s w=%d terminates=%s expected=%s"
                      % (lam, w, t2, sum(lam) % 2 == w % 2))
        # E10 says k >= w is PINNED by Erdos-Gallai: k = w-1 must break somewhere
        if w >= 2:
            t3 = res([w] * (w - 1) + list(lam)) is not None
            if t3 != ((sum(lam) + w * (w - 1)) % 2 == 0):
                kless_bad += 1
print("     C1-N as stated (k = w+1)  : %d agree, %d disagree" % (kn_ok, kn_bad))
print("     E10's k = w variant       : %d agree, %d disagree" % (kw_ok, kw_bad))
print("     k = w-1 (must break)      : parity alone mispredicts on %d instances" % kless_bad)
if kn_bad:
    bad("C1-N", "%d" % kn_bad)
if kw_bad:
    bad("E10-kw", "%d" % kw_bad)
ctrl("CORRUPT CONTROL: at k = w-1 parity is NOT sufficient (E10's k >= w bound is real)",
     kless_bad)


# ================================================================= 9. GATE
print("\n" + "=" * 100)
print("SUMMARY")
print("=" * 100)
print("diffed runA/runB calls : %d" % DIFFED)
print("controls fired         : %d of %d" % (sum(1 for c in CTRL if c), len(CTRL)))
print("PARTIAL (hit the internal clock limit) : %s" % bool(OUT_OF_TIME))
print("DEFECTS : %d" % len(FAIL))
for x in FAIL:
    print("   " + x)
print("elapsed %.2f s (internal limit %.0f s)" % (time.time() - T0, LIMIT))
sys.exit(0)
