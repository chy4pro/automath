#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r50 -- (MON) IN FULL, as a corollary of r48's THEOREM R-CLOSED.

r49 proved (RH) = the LOWER bound of (MON)'s EVEN half, and measured that it covers only
821 of 1 507 even-sum instances (219 identical lists, 467 "not same length/sum").  This
file closes the whole of (MON): both bounds, both parities, and the 467.

--------------------------------------------------------------------------------------
SET-UP (r38, sec 7.53).  W+(c) = c^3 (c-1)^c ,  W-(c) = c^2 (c-1)^{c+1}   -- both of
LENGTH c+3, and sum W+ = sum W- + 1.  For a partition T with T_0 = c,
        L(T) := ms( W^eps(c) u T[1:] ),   eps = '+' iff sum(T) is EVEN,
        f(T) := residue(L(T)) = len(L(T)) - s(L(T)),   s = #Havel-Hakimi steps.
(MON):  f(T) - f(T + e_i) in {0,1}  for every partition T and every part index i.
(MON) is the single open input of r38's THEOREM C1-V (C1-S + (MON) ==> C1-M).

--------------------------------------------------------------------------------------
THEOREM STEP-GAP-1 (PROVED, mine -- corollary of r48's THEOREM R-CLOSED).
    (A,B) in R, A and B both graphic  ==>  s(B) - s(A) in {0,1}.

  Proof.  Induction on s(A).
  BASE  A = ().  Then d := max A = 0 and A_{d+1} = 0.  (EQ) gives B = ().  (T) is
    impossible: it moves a unit out of a part of size x >= 2 and A has none.  (U) needs
    v2 <= d = 0 and v1 <= A_{d+1} = 0, so v1 = v2 = 0 and B is A with two units added at
    part-size 0, i.e. B = (1,1).  So B in {(), (1,1)} and s(B) in {0,1} = {s(A), s(A)+1}.
  STEP  A != ().  R implies sum A <= sum B, so B != ().  Both steps are legal (both
    graphic), so THEOREM R-CLOSED gives (hh A, hh B) in R, with hh A, hh B graphic.  By
    induction s(hh B) - s(hh A) in {0,1}; add 1 to each of s(A), s(B).  QED

  Note the lower bound s(B) >= s(A) is the same three-line argument as r49's (RH); the
  UPPER bound is what is new, and it is the terminal state that supplies it.

--------------------------------------------------------------------------------------
THE FOUR CASES OF (MON).  Write c = T_0, tail = T[1:], t = the raised value T_i.
Case (1), the raise does NOT change the max (t <= c-1):  U[1:] = tail with t -> t+1, and
len L' = len L.
  (1a) sum T EVEN.  L = ms(W+(c) u tail), L' = ms(W-(c) u tail').  W-(c) is W+(c) with one
       c lowered to c-1, so L' = L with one unit moved from a part of size c to a part of
       size t.  t = c-1 -> the two changes cancel, (EQ).  t <= c-2 -> a (T) state.  Both
       lie in R with NO side condition.  STEP-GAP-1 and len L' = len L give (MON).
  (1b) sum T ODD.   L = ms(W-(c) u tail), L' = ms(W+(c) u tail').  W+(c) is W-(c) with one
       (c-1) raised to c, so L' = L with TWO units added, at part-sizes v1 = t and
       v2 = c-1 (t <= c-1).  In R:  v2 = c-1 <= c = d;  and W-(c) puts c+3 entries >= c-1
       into L, so L_0..L_{c+2} >= c-1, in particular L_{d+1} = L_{c+1} >= c-1 >= v1.
       ** THIS IS WHAT THE HEAD BLOCK IS FOR. **  (UP2) -- the same "raise two by 1"
       statement without a head block -- is FALSE (r38 [5], 97 counterexamples), and the
       only conjunct of R it can break is v1 <= A_{d+1}: block [3] checks that.
Case (2), the raise DOES change the max (t = c):  then U = T - {c} + {c+1} and
U[1:] = T - {c} = tail EXACTLY, so L' = ms(W^{-eps}(c+1) u tail) and len L' = len L + 1,
whence  f(T) - f(T') = s(L') - s(L) - 1,  and (MON) asks s(L') - s(L) in {1,2}.
  Write tail = c^a (c-1)^b u rest with rest <= c-2.
  (2a) sum T EVEN.  L = c^{3+a} (c-1)^{c+b} u rest, L' = (c+1)^2 c^{c+2+a} (c-1)^b u rest.
       One HH step on L' deletes a (c+1) and lowers the largest c+1 of what is left --
       the remaining (c+1) and c of the c's, never reaching rest since 1+(c+2+a) >= c+1:
       hh(L') = c^{1} c^{2+a} (c-1)^{c} (c-1)^b u rest = L.   ** hh(L') = L EXACTLY. **
       So s(L') = s(L) + 1 and f(T) - f(T') = 0.
  (2b) sum T ODD.   L = c^{2+a} (c-1)^{c+1+b} u rest, L' = (c+1)^3 c^{c+1+a} (c-1)^b u rest.
       One HH step on L' deletes a (c+1) and lowers 2 entries of (c+1) plus c-1 entries of
       c:  hh(L') = c^{4+a} (c-1)^{c-1+b} u rest = L with TWO (c-1)'s raised to c.  That is
       a (U) state with v1 = v2 = c-1 <= c = d and v1 = c-1 <= L_{c+1} (L holds
       2+a+c+1+b >= c+3 entries >= c-1), so it is in R.  STEP-GAP-1 gives
       s(hh L') - s(L) in {0,1}, hence s(L') - s(L) in {1,2}, hence f(T) - f(T') in {0,1}.
  COROLLARY MON (PROVED).  f(T) - f(T + e_i) in {0,1} for every T and every i.  QED

WHAT IS NOT CLAIMED.  (DOM-MAJ) is NOT novelty-cleared (planner ruling
cert_w61_r48_litcheck.md), so neither is STEP-GAP-1 nor (MON).  Nothing goes outward.
C1-S / C1-U / C1-V are r38's, owner-claimed and uncertified; this file re-runs C1-V's
consequence but does not re-prove C1-S.  (BAND-EQ), (S2), C1-W, (PERSIST-NARROW),
(GAP1-OK), (F2-FREE) are untouched.  WOWII-61 IS NOT CLOSED.

--------------------------------------------------------------------------------------
DIRECTION FIXED IN WRITING BEFORE THE RUN (dispatch item (d)).  Predictions:
  P1  Case (2a): hh(L') = L on EVERY instance, so delta = f(T) - f(T') = 0 on every one of
      them -- the histogram on case (2a) is {0: all}, with NO 1's.
  P2  Case (2b): delta takes BOTH values 0 and 1.
  P3  Of r38's 97 general (UP2) counterexamples, ZERO are in R, and the conjunct that
      fails is v1 <= A_{d+1} in ALL 97 -- never v2 <= d, which cannot fail when two
      distinct existing entries are raised (v2 <= max A = d always).
  P4  Case (1a) splits into (EQ) when t = c-1 and (T) when t <= c-2, with BOTH non-empty.
  P5  The terminal set of R at A = () is exactly {(), (1,1)}.
  P6  Dropping v1 <= A_{d+1} from R breaks STEP-GAP-1 (s-gap >= 2 occurs); dropping
      v2 <= d breaks it too.
  P7  L(T) is graphic for EVERY partition T (r38's block [3] calls f with no None guard,
      so it must be -- this is a check of r38, not of me).

RULING 105 / 81.  hh_walk is lifted BY SOURCE TEXT from w61_r49b_rh.py (itself sharing no
line with the r29 walk); hh_walk2 is a second, list-based walk written here and DIFFED
against it on every call.  Graphicness is cross-checked by Erdos-Gallai.  No SAT, no
solver, no local exhaustive search.  Interpreter: .venv/bin/python3.
"""
import sys, time
from collections import Counter

T0 = time.time()
LIMIT = 420.0
FAIL = []
CTRL = []
PARTIAL = False


def over():
    global PARTIAL
    if time.time() - T0 > LIMIT:
        PARTIAL = True
        return True
    return False


def bad(tag, detail):
    FAIL.append("%s  %s" % (tag, detail))
    print("   ** DEFECT %s  %s" % (tag, detail))


def ctrl(name, hits, must_fire=True):
    CTRL.append((name, hits, must_fire))
    ok = (hits > 0) if must_fire else True
    print("   [%s] %-74s hits=%d" % ("ok " if ok else "DEAD", name, hits))
    if must_fire and hits == 0:
        bad("DEAD CONTROL", name)


def known(name, got, want):
    tag = "ok " if got == want else "MISMATCH"
    print("   [%s] KNOWN VALUE %-54s got=%s want=%s" % (tag, name, got, want))
    if got != want:
        bad("KNOWN VALUE MISMATCH", "%s got=%s want=%s" % (name, got, want))


# ------------------------------------------------------------------ HH walk, impl A
# lifted BY SOURCE TEXT from problems/wowii/w61_r49b_rh.py (r49 ITEM B).
def hh_walk(seq):
    """Counter-based Havel-Hakimi.  Returns (pivot tuple, steps, residue) or None if the
    sequence is NOT graphic."""
    n = len(seq)
    cnt = Counter()
    for x in seq:
        if x < 0:
            return None
        if x:
            cnt[x] += 1
    pivs = []
    while cnt:
        d = max(cnt)
        cnt[d] -= 1
        if not cnt[d]:
            del cnt[d]
        need = d
        if need > sum(cnt.values()):
            return None
        picks = []
        for v in sorted(cnt, reverse=True):
            if not need:
                break
            take = cnt[v] if cnt[v] < need else need
            picks.append((v, take))
            need -= take
        for v, take in picks:
            cnt[v] -= take
            if not cnt[v]:
                del cnt[v]
        for v, take in picks:
            if v > 1:
                cnt[v - 1] += take
        pivs.append(d)
    return tuple(pivs), len(pivs), n - len(pivs)


# ------------------------------------------------------------------ HH walk, impl B
def hh_walk2(seq):
    """second, INDEPENDENT, list-based walk.  Returns (steps, residue) or None."""
    n = len(seq)
    for x in seq:
        if x < 0:
            return None
    a = sorted([x for x in seq if x], reverse=True)
    steps = 0
    while a:
        d = a[0]
        rest = a[1:]
        if d > len(rest):
            return None
        for t in range(d):
            rest[t] -= 1
        a = sorted([x for x in rest if x], reverse=True)
        steps += 1
    return steps, n - steps


DIFFED = 0


def walk(seq):
    """(steps, residue) or None; ABORTS if the two implementations disagree."""
    global DIFFED
    a = hh_walk(list(seq))
    b = hh_walk2(list(seq))
    ra = None if a is None else (a[1], a[2])
    if ra != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (list(seq), ra, b))
        sys.exit(2)
    DIFFED += 1
    return b


def hh_one(A):
    """ONE HH step on the multiset of positive parts.  Returns a sorted tuple, or None."""
    a = sorted([x for x in A if x], reverse=True)
    if not a:
        return ()
    d = a[0]
    rest = a[1:]
    if d > len(rest):
        return None
    for t in range(d):
        rest[t] -= 1
    return tuple(sorted([x for x in rest if x], reverse=True))


def erdos_gallai(seq):
    s = sorted((x for x in seq), reverse=True)
    if any(x < 0 for x in s):
        return False
    if sum(s) % 2:
        return False
    n = len(s)
    for k in range(1, n + 1):
        lhs = sum(s[:k])
        rhs = k * (k - 1) + sum(min(x, k) for x in s[k:])
        if lhs > rhs:
            return False
    return True


def ms(l):
    return tuple(sorted(l, reverse=True))


def pos(l):
    return tuple(sorted([x for x in l if x], reverse=True))


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


# ------------------------------------------------------------------ the c_m shape, r48 (c)
def shape(A, B):
    """(kind, v1_or_x, v2_or_y) for the c_m profile P_m = c_m(B) - c_m(A).
       'EQ'  P == 0
       'T'   P is the indicator of an interval [y+1, x-1]   -> ('T', x, y)
       'U'   P = [m>=v1+1] + [m>=v2+1], v1 <= v2            -> ('U', v1, v2)
       else 'OTHER'."""
    A = pos(A)
    B = pos(B)
    M = max([0] + list(A) + list(B)) + 1
    P = [sum(min(x, m) for x in B) - sum(min(x, m) for x in A) for m in range(M + 1)]
    if all(p == 0 for p in P):
        return ("EQ", None, None)
    if P[-1] == 0 and all(p in (0, 1) for p in P):
        idx = [m for m, p in enumerate(P) if p == 1]
        if idx == list(range(idx[0], idx[-1] + 1)):
            return ("T", idx[-1] + 1, idx[0] - 1)
    if P[-1] == 2 and all(0 <= p <= 2 for p in P):
        one = [m for m, p in enumerate(P) if p >= 1]
        two = [m for m, p in enumerate(P) if p >= 2]
        if one and two:
            v1, v2 = one[0] - 1, two[0] - 1
            if v1 <= v2 and all(
                    P[m] == (1 if m >= v1 + 1 else 0) + (1 if m >= v2 + 1 else 0)
                    for m in range(M + 1)):
                return ("U", v1, v2)
    return ("OTHER", None, None)


def at(A, i):
    A = pos(A)
    return A[i] if i < len(A) else 0


def in_R(A, B, drop_v1=False, drop_v2=False):
    k, u, v = shape(A, B)
    if k in ("EQ", "T"):
        return True
    if k == "U":
        d = at(A, 0)
        c1 = drop_v1 or (u <= at(A, d + 1))
        c2 = drop_v2 or (v <= d)
        return c1 and c2
    return False


print("=" * 100)
print("w61 r50 -- (MON) IN FULL as a corollary of r48's R-CLOSED:  THEOREM STEP-GAP-1")
print("           plus a FOUR-CASE decomposition that covers the 467 r49 could not reach")
print("=" * 100)
print("interpreter: .venv/bin/python3 (pure Python, no sympy, no networkx)")

# ================================================== [0] CONTROLS AND KNOWN VALUES FIRST
print("\n[0] CONTROLS AND KNOWN VALUES, BEFORE ANY RESULT (sec 148).")

agree = disagree = ngraphic = 0
for N in range(1, 19):
    for p in parts(N):
        w = hh_walk(list(p))
        eg = erdos_gallai(list(p))
        if (w is not None) == eg:
            agree += 1
        else:
            disagree += 1
            if disagree <= 3:
                print("     ORACLE DISAGREEMENT %s hh=%s eg=%s" % (p, w is not None, eg))
        if eg:
            ngraphic += 1
        walk(list(p))
print("    two graphicness oracles on partitions of N<=18 : %d tested, %d agree, %d DISAGREE"
      % (agree + disagree, agree, disagree))
if disagree:
    bad("ORACLES", "%d disagreements" % disagree)
known("r49 [0] oracle population", agree + disagree, 1596)
known("r49 [0] graphic among them", ngraphic, 360)
ctrl("CONTROL: the population contains NON-graphic partitions too",
     agree + disagree - ngraphic)


def Wp(c):
    return [c] * 3 + [c - 1] * c


def Wm(c):
    return [c] * 2 + [c - 1] * (c + 1)


def L_of(T):
    T = ms(T)
    if not T:
        return None
    c = T[0]
    return (Wp(c) if sum(T) % 2 == 0 else Wm(c)) + list(T[1:])


def f_of(T):
    L = L_of(T)
    if L is None:
        return 2
    w = walk(L)
    return None if w is None else w[1]


# r38 Lemma C1-U, as a known value
c1u_bad = 0
for m in range(0, 31):
    if f_of(tuple([1] * m)) != (m + 1) // 2 + 2:
        c1u_bad += 1
known("r38 Lem C1-U  f(1^m) = ceil(m/2)+2 for m=0..30, failures", c1u_bad, 0)

# P7: L(T) graphic for every T
nongraphic_L = 0
nL = 0
for N in range(1, 23):
    for T in parts(N):
        nL += 1
        if walk(L_of(T)) is None:
            nongraphic_L += 1
print("    P7  L(T) built for %d partitions T (sum<=22); NON-graphic L(T): %d"
      % (nL, nongraphic_L))
if nongraphic_L:
    bad("P7", "L(T) not always graphic -- r38 block [3] would have crashed")

# r38 block [3]: the (MON) census itself
hist_mon = Counter()
viol_mon = []
for N in range(1, 23):
    for T in parts(N):
        for i in range(len(T)):
            Tp = list(T)
            Tp[i] += 1
            d = f_of(T) - f_of(ms(Tp))
            hist_mon[d] += 1
            if d < 0:
                viol_mon.append((T, ms(Tp)))
known("r38 [3] (MON) population, sum(T)<=22", sum(hist_mon.values()), 31766)
known("r38 [3] (MON) delta histogram {0}", hist_mon[0], 28288)
known("r38 [3] (MON) delta histogram {1}", hist_mon[1], 3478)
print("    (MON) delta histogram, full: %s ; delta<0 : %d"
      % (dict(sorted(hist_mon.items())), len(viol_mon)))
ctrl("CORRUPT: 'f(T) - f(T+e_i) in {0}' is violated", hist_mon[1])
if len(hist_mon) > 2:
    bad("MON", "delta outside {0,1}: %s" % dict(sorted(hist_mon.items())))


# r38 block [5]: (RH) and (UP2) sweeps, distinct pairs
def sweep(gen, nmax=16):
    ok = set()
    bd = set()
    for N in range(2, nmax + 1):
        for L in parts(N):
            w = walk(list(L))
            if w is None:
                continue
            r = w[1]
            for Lp in gen(L):
                Lp = ms(Lp)
                if min(Lp) < 0:
                    continue
                w2 = walk(list(Lp))
                if w2 is None:
                    continue
                (ok if w2[1] <= r else bd).add((L, Lp, r, w2[1]))
    return ok, bd


def rh_gen(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if i != j and L[i] - 1 >= L[j] + 1:
                Lp = list(L)
                Lp[i] -= 1
                Lp[j] += 1
                yield Lp


def up2_gen(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            Lp = list(L)
            Lp[i] += 1
            Lp[j] += 1
            yield Lp


rh_ok, rh_bad = sweep(rh_gen)
up_ok, up_bad = sweep(up2_gen)
known("r38 [5] (RH)  distinct ok", len(rh_ok), 284)
known("r38 [5] (RH)  distinct VIOLATIONS", len(rh_bad), 0)
known("r38 [5] (UP2) distinct ok", len(up_ok), 635)
known("r38 [5] (UP2) distinct VIOLATIONS", len(up_bad), 97)
ctrl("(UP2) general form is REFUTED (r38)", len(up_bad))
print("    diffed HH calls so far: %d, disagreements 0 (any would have exited 2)" % DIFFED)

# ================================================== [1] THEOREM STEP-GAP-1
print("\n[1] THEOREM STEP-GAP-1 :  (A,B) in R, both graphic  ==>  s(B) - s(A) in {0,1}.")
print("    The BASE of the induction, checked first: which B can stand opposite A = () in R?")

NTERM = 4 * 3
term = set()
for N in range(0, NTERM + 1):
    for B in parts(N):
        if in_R((), B):
            term.add(B)
print("    P5  {B : ((),B) in R} over all partitions of N<=%d : %s" % (NTERM, sorted(term)))
if term != {(), (1, 1)}:
    bad("P5", "terminal set is %s, not {(), (1,1)}" % sorted(term))
ctrl("CONTROL: partitions of N<=%d that are NOT admissible opposite ()" % NTERM,
     sum(1 for N in range(0, NTERM + 1) for B in parts(N)) - len(term))

# 1a. all-pairs sweep -- unbiased, catches a shape misclassification
print("    [1a] ALL-PAIRS sweep: every (A,B) of graphic partitions with sum B - sum A in")
print("         {0,2}, classified by shape, then STEP-GAP-1 checked on the R members.")
NP = 16
G = {}
for N in range(0, NP + 3):
    G[N] = [p for p in parts(N) if walk(list(p)) is not None]
S = {}
for N in G:
    for p in G[N]:
        S[p] = walk(list(p))[0]
shape_hist = Counter()
rpairs = 0
gap_hist = Counter()
gap_bad = []
out_hist = Counter()
for N in range(0, NP + 1):
    if over():
        break
    for A in G[N]:
        for M2 in (N, N + 2):
            if M2 not in G:
                continue
            for B in G[M2]:
                k, u, v = shape(A, B)
                shape_hist[k] += 1
                if in_R(A, B):
                    rpairs += 1
                    g = S[B] - S[A]
                    gap_hist[g] += 1
                    if g not in (0, 1):
                        gap_bad.append((A, B, g))
                else:
                    out_hist[S[B] - S[A]] += 1
print("         population %d ordered pairs; shape histogram %s"
      % (sum(shape_hist.values()), dict(sorted(shape_hist.items()))))
print("         in R: %d ; s(B)-s(A) histogram %s ; OUTSIDE {0,1}: %d"
      % (rpairs, dict(sorted(gap_hist.items())), len(gap_bad)))
if gap_bad:
    bad("STEP-GAP-1", "%d failures, e.g. %s" % (len(gap_bad), gap_bad[:3]))
ctrl("CONTROL: pairs NOT in R with s-gap outside {0,1} exist (the theorem has content)",
     sum(n for g, n in out_hist.items() if g not in (0, 1)))
print("         (for reference, the OUTSIDE-R s-gap histogram is %s)"
      % dict(sorted(out_hist.items())))

# 1b. corrupt R's, each conjunct dropped
print("    [1b] CORRUPT CONTROLS on R itself (P6).")
for tagname, dv1, dv2 in (("drop v1 <= A_{d+1}", True, False),
                          ("drop v2 <= max A", False, True)):
    hits = 0
    smallest = None
    for N in range(0, NP + 1):
        for A in G[N]:
            for M2 in (N, N + 2):
                if M2 not in G:
                    continue
                for B in G[M2]:
                    if in_R(A, B):
                        continue
                    if in_R(A, B, drop_v1=dv1, drop_v2=dv2):
                        if S[B] - S[A] not in (0, 1):
                            hits += 1
                            if smallest is None:
                                smallest = (A, B, S[B] - S[A])
    ctrl("CORRUPT R (%s): STEP-GAP-1 then FAILS" % tagname, hits)
    if smallest:
        print("         smallest witness A=%s B=%s gap=%d" % smallest)

# 1c. R-closure, re-verified here on my own implementation
print("    [1c] R-CLOSURE re-verified on THIS implementation (r48's THEOREM R-CLOSED).")
for NP2 in (14, 18):
    if over():
        break
    GG = {}
    for N in range(0, NP2 + 3):
        GG[N] = [p for p in parts(N) if walk(list(p)) is not None]
    tot = viols = 0
    for N in range(0, NP2 + 1):
        for A in GG[N]:
            if not A:
                continue
            for M2 in (N, N + 2):
                if M2 not in GG:
                    continue
                for B in GG[M2]:
                    if not in_R(A, B):
                        continue
                    hA, hB = hh_one(A), hh_one(B)
                    if hA is None or hB is None:
                        continue
                    tot += 1
                    if not in_R(hA, hB):
                        viols += 1
    print("         N<=%d : %d R-states stepped, closure violations %d" % (NP2, tot, viols))
    if viols:
        bad("R-CLOSED", "%d closure violations at N<=%d" % (viols, NP2))

# 1d. R implies sum A <= sum B (the other half of the induction), and a SECOND, larger
#     population built by a DIFFERENT generator: B is constructed from A, not enumerated.
print("    [1d] 'R ==> sum A <= sum B' and STEP-GAP-1 on a CONSTRUCTIVELY generated")
print("         population (B built from A by the three shapes, not enumerated).")
sum_bad = 0
cons_n = 0
cons_gap = Counter()
cons_bad = []
for N in range(0, 23):
    if over():
        break
    for A in parts(N):
        if walk(list(A)) is None:
            continue
        sA = walk(list(A))[0]
        cand = set([A])
        pad = list(A) + [0, 0]
        n = len(pad)
        for i in range(n):
            for j in range(n):
                if i != j and pad[i] - 1 >= pad[j] + 1:
                    v = list(pad)
                    v[i] -= 1
                    v[j] += 1
                    cand.add(pos(v))
            for j in range(i, n):
                v = list(pad)
                v[i] += 1
                v[j] += 1
                cand.add(pos(v))
        for B in cand:
            if not in_R(A, B):
                continue
            if sum(B) - sum(A) not in (0, 2):
                sum_bad += 1
            wB = walk(list(B))
            if wB is None:
                continue
            cons_n += 1
            g = wB[0] - sA
            cons_gap[g] += 1
            if g not in (0, 1):
                cons_bad.append((A, B, g))
print("         constructive R-pairs with both graphic: %d ; s-gap histogram %s"
      % (cons_n, dict(sorted(cons_gap.items()))))
print("         'R ==> sum B - sum A in {0,2}' failures: %d" % sum_bad)
if cons_bad or sum_bad:
    bad("STEP-GAP-1/sum", "%d gap failures, %d sum failures" % (len(cons_bad), sum_bad))
ctrl("CONTROL: the constructive population is larger than the all-pairs one",
     max(0, cons_n - rpairs))

# ================================================== [2] THE FOUR CASES OF (MON)
print("\n[2] THE FOUR-CASE DECOMPOSITION.  Every (T,i) is classified BEFORE its delta is")
print("    read, and the structural claim of its case is checked on it.")


def classify(T, i):
    """returns (case, dict of facts)."""
    T = ms(T)
    c = T[0]
    t = T[i]
    U = ms([T[k] + (k == i) for k in range(len(T))])
    L, Lp = ms(L_of(T)), ms(L_of(U))
    ev = (sum(T) % 2 == 0)
    d = dict(c=c, t=t, L=L, Lp=Lp, U=U,
             lenL=len(L_of(T)), lenLp=len(L_of(U)))
    if t < c:
        return ("1a" if ev else "1b"), d
    return ("2a" if ev else "2b"), d


case_hist = Counter()
struct_bad = Counter()
delta_by_case = {}
shape_by_case = {}
NMAX = 22
for N in range(1, NMAX + 1):
    if over():
        break
    for T in parts(N):
        for i in range(len(T)):
            cs, D = classify(T, i)
            case_hist[cs] += 1
            L, Lp, c, t = D["L"], D["Lp"], D["c"], D["t"]
            delta = f_of(T) - f_of(D["U"])
            delta_by_case.setdefault(cs, Counter())[delta] += 1
            if cs in ("1a", "1b"):
                if D["lenL"] != D["lenLp"]:
                    struct_bad[cs + ":length"] += 1
                k, u, v = shape(L, Lp)
                shape_by_case.setdefault(cs, Counter())[k] += 1
                if not in_R(L, Lp):
                    struct_bad[cs + ":not in R"] += 1
                if cs == "1a":
                    if t == c - 1 and k != "EQ":
                        struct_bad["1a:t=c-1 not EQ"] += 1
                    if t <= c - 2 and not (k == "T" and u == c and v == t):
                        struct_bad["1a:t<=c-2 not T(c,t)"] += 1
                else:
                    if not (k == "U" and u == min(t, c - 1) and v == max(t, c - 1)):
                        struct_bad["1b:not U(t,c-1)"] += 1
                    if at(L, 0) != c:
                        struct_bad["1b:max L != c"] += 1
                    if at(L, at(L, 0) + 1) < c - 1:
                        struct_bad["1b:L_{d+1} < c-1"] += 1
                wL, wLp = walk(list(L_of(T))), walk(list(L_of(D["U"])))
                if wL is not None and wLp is not None:
                    if (wLp[0] - wL[0]) not in (0, 1):
                        struct_bad[cs + ":s-gap outside {0,1}"] += 1
            else:
                if D["lenLp"] != D["lenL"] + 1:
                    struct_bad[cs + ":length not +1"] += 1
                hLp = hh_one(Lp)
                if hLp is None:
                    struct_bad[cs + ":L' not steppable"] += 1
                    continue
                if cs == "2a":
                    if hLp != pos(L):
                        struct_bad["2a:hh(L') != L"] += 1
                else:
                    k, u, v = shape(L, hLp)
                    shape_by_case.setdefault(cs, Counter())[k] += 1
                    if not (k == "U" and u == c - 1 and v == c - 1):
                        struct_bad["2b:shape(L,hh L') != U(c-1,c-1)"] += 1
                    if at(L, 0) != c:
                        struct_bad["2b:max L != c"] += 1
                    if at(L, at(L, 0) + 1) < c - 1:
                        struct_bad["2b:L_{d+1} < c-1"] += 1
                    if not in_R(L, hLp):
                        struct_bad["2b:(L, hh L') not in R"] += 1
                wL, wLp = walk(list(L_of(T))), walk(list(L_of(D["U"])))
                if wL is not None and wLp is not None:
                    if (wLp[0] - wL[0]) not in (1, 2):
                        struct_bad[cs + ":s-gap outside {1,2}"] += 1
print("    case histogram over sum(T)<=%d : %s" % (NMAX, dict(sorted(case_hist.items()))))
print("    STRUCTURAL FAILURES (every one is a defect in the proof above): %s"
      % (dict(sorted(struct_bad.items())) if struct_bad else "NONE"))
if struct_bad:
    bad("FOUR-CASE", str(dict(struct_bad)))
for cs in sorted(delta_by_case):
    print("    case %s : delta histogram %s ; shapes %s"
          % (cs, dict(sorted(delta_by_case[cs].items())),
             dict(sorted(shape_by_case.get(cs, Counter()).items())) or "-"))
# P1 / P2 / P4
p1 = delta_by_case.get("2a", Counter())
print("    P1  case (2a) delta is identically 0 : %s" % (set(p1) == {0}))
if set(p1) != {0}:
    bad("P1", "case 2a histogram %s" % dict(p1))
p2 = delta_by_case.get("2b", Counter())
print("    P2  case (2b) takes both values      : %s" % (set(p2) == {0, 1}))
if set(p2) != {0, 1}:
    bad("P2", "case 2b histogram %s" % dict(p2))
sh1a = shape_by_case.get("1a", Counter())
print("    P4  case (1a) shapes                 : %s" % dict(sorted(sh1a.items())))
if set(sh1a) != {"EQ", "T"}:
    bad("P4", "case 1a shapes %s" % dict(sh1a))
ctrl("CONTROL: case (1a) really does contain both EQ and T", min(sh1a["EQ"], sh1a["T"]))
ctrl("CONTROL: the max-raising cases (2a)+(2b) are non-empty",
     case_hist["2a"] + case_hist["2b"])

# THE TIE TO r49's OWN THREE NUMBERS.  r49 block [4] swept sum(T) even, N in [1,14] and
# split by (L,L') into 821 "genuine transfer DOWN", 219 "identical lists", 467 "not same
# length/sum".  Those three ARE case (1a)-with-(T), case (1a)-with-(EQ) and case (2a).
r49tie = Counter()
for N in range(1, 15):
    for T in parts(N):
        if sum(T) % 2:
            continue
        for i in range(len(T)):
            cs, D = classify(T, i)
            if cs == "2a":
                r49tie["not same length/sum"] += 1
            else:
                r49tie[shape(D["L"], D["Lp"])[0]] += 1
known("r49 [4] 'a genuine transfer DOWN' == case (1a), shape (T)", r49tie["T"], 821)
known("r49 [4] 'identical lists'         == case (1a), shape (EQ)", r49tie["EQ"], 219)
known("r49 [4] 'not same length/sum'     == case (2a)", r49tie["not same length/sum"], 467)
known("r49 [4] even-sum (MON) population", sum(r49tie.values()), 1507)

# corrupt controls on the two case-(2) identities
print("    CORRUPT CONTROLS on the case-(2) identities.")
c4 = c5 = 0
for N in range(1, 15):
    for T in parts(N):
        for i in range(len(T)):
            cs, D = classify(T, i)
            if cs == "2a":
                wrong = ms(Wp(D["c"] + 1) + list(D["U"][1:]))
                h = hh_one(wrong)
                if h != pos(D["L"]):
                    c4 += 1
            elif cs == "2b":
                if hh_one(D["Lp"]) != pos(D["L"]):
                    c5 += 1
ctrl("CORRUPT: case (2a) with W+(c+1) instead of W-(c+1) -- hh(L') != L", c4)
ctrl("CORRUPT: case (2b) does NOT satisfy hh(L') = L (it needs STEP-GAP-1)", c5)

# ================================================== [3] why (UP2) is false without a head block
print("\n[3] P3 -- r38's 97 general (UP2) counterexamples, against R.")
in_r = 0
fail_v1 = fail_v2 = fail_both = other_shape = 0
for (L, Lp, r, rp) in up_bad:
    if in_R(L, Lp):
        in_r += 1
    k, u, v = shape(L, Lp)
    if k != "U":
        other_shape += 1
        continue
    d = at(L, 0)
    b1 = u > at(L, d + 1)
    b2 = v > d
    if b1 and b2:
        fail_both += 1
    elif b1:
        fail_v1 += 1
    elif b2:
        fail_v2 += 1
print("    of the %d (UP2) counterexamples: in R = %d ; shape not (U) = %d"
      % (len(up_bad), in_r, other_shape))
print("    failing conjunct: v1 <= A_{d+1} only = %d ; v2 <= d only = %d ; both = %d"
      % (fail_v1, fail_v2, fail_both))
if in_r:
    bad("P3", "%d (UP2) counterexamples lie in R -- STEP-GAP-1 would be false" % in_r)
if fail_v2 or fail_both:
    print("    ** P3's second half is WRONG as predicted: v2 <= d DOES fail somewhere.")
ctrl("P3: the failing conjunct is v1 <= A_{d+1}", fail_v1)
# and the head block repairs it
rep = 0
for (L, Lp, r, rp) in up_bad:
    c = L[0]
    L2 = ms(list(L) + Wm(c))
    if at(L2, at(L2, 0) + 1) >= c - 1:
        rep += 1
ctrl("the head block W-(c) restores L_{d+1} >= c-1 on those same lists", rep)

# ================================================== [4] the consequence for C1-M
print("\n[4] WHAT (MON) NOW BUYS.  r38's THEOREM C1-V is  C1-S + (MON) ==> C1-M, and it")
print("    uses only the LOWER half:  T >= 1^m componentwise, so f(T) <= f(1^m) =")
print("    ceil(m/2)+2 by Lemma C1-U.  The ladder and the consequence, re-run here:")
lad_bad = ineq_bad = ntest = 0
for N in range(1, 21):
    if over():
        break
    for T in parts(N):
        m = len(T)
        cur = [1] * m
        okpath = True
        for i in range(m):
            while cur[i] < T[i]:
                cur[i] += 1
                if any(cur[a] < cur[a + 1] for a in range(m - 1)):
                    okpath = False
        if not okpath or tuple(cur) != tuple(T):
            lad_bad += 1
        ntest += 1
        if f_of(T) > f_of(tuple([1] * m)):
            ineq_bad += 1
print("    ladder 1^m -> T stays sorted: %d partitions, failures %d" % (ntest, lad_bad))
print("    f(T) <= f(1^m) = ceil(m/2)+2 : failures %d" % ineq_bad)
if lad_bad or ineq_bad:
    bad("C1-V", "ladder %d, inequality %d" % (lad_bad, ineq_bad))
ctrl("CONTROL: f(T) < f(1^m) STRICTLY somewhere (the bound is not an identity)",
     sum(1 for N in range(1, 15) for T in parts(N) if f_of(T) < f_of(tuple([1] * len(T)))))

# ================================================== [5] held-out range
HO_LO, HO_HI = NMAX + 1, NMAX + 4
print("\n[5] HELD OUT -- the four-case decomposition on sum(T) in [%d,%d], a range r38's"
      % (HO_LO, HO_HI))
print("    (MON) census never used.")
ho_case = Counter()
ho_bad = Counter()
ho_delta = Counter()
for N in range(HO_LO, HO_HI + 1):
    if over():
        break
    for T in parts(N):
        for i in range(len(T)):
            cs, D = classify(T, i)
            ho_case[cs] += 1
            ho_delta[f_of(T) - f_of(D["U"])] += 1
            L, Lp, c, t = D["L"], D["Lp"], D["c"], D["t"]
            if cs in ("1a", "1b"):
                if not in_R(L, Lp) or D["lenL"] != D["lenLp"]:
                    ho_bad[cs] += 1
            elif cs == "2a":
                if hh_one(Lp) != pos(L) or D["lenLp"] != D["lenL"] + 1:
                    ho_bad[cs] += 1
            else:
                h = hh_one(Lp)
                if h is None or not in_R(L, h) or shape(L, h) != ("U", c - 1, c - 1):
                    ho_bad[cs] += 1
print("    held-out cases %s ; structural failures %s ; delta histogram %s"
      % (dict(sorted(ho_case.items())),
         dict(sorted(ho_bad.items())) if ho_bad else "NONE",
         dict(sorted(ho_delta.items()))))
if ho_bad:
    bad("HELD-OUT", str(dict(ho_bad)))
if set(ho_delta) - {0, 1}:
    bad("HELD-OUT MON", str(dict(ho_delta)))

# ================================================== [6] what is NOT closed
print("\n[6] WHAT IS NOT CLOSED.")
print("    (DOM-MAJ) is NOT novelty-cleared, so neither is STEP-GAP-1 nor (MON).")
print("    C1-S, C1-U, C1-V are r38's, owner-claimed and UNCERTIFIED; this file re-runs")
print("    C1-V's consequence but does not re-prove C1-S.")
print("    (BAND-EQ), (S2), C1-W, (PERSIST-NARROW), (GAP1-OK), (F2-FREE) UNTOUCHED here.")
print("    THE CONJECTURE (WOWII, line %d) IS NOT CLOSED." % (60 + 1))

print("\n" + "=" * 100)
print("SELF-AUDIT")
print("  diffed HH calls : %d  (any disagreement would have exited 2)" % DIFFED)
print("  controls        : %d declared, %d firing"
      % (len(CTRL), sum(1 for _, h, mf in CTRL if (h > 0) or not mf)))
for n, h, mf in CTRL:
    if mf and h == 0:
        print("    DEAD: %s" % n)
print("  defects         : %d" % len(FAIL))
for x in FAIL:
    print("    - %s" % x)
print("  PARTIAL         : %s" % PARTIAL)
print("  elapsed         : %.1fs" % (time.time() - T0))
print("=" * 100)
sys.exit(1 if FAIL else 0)
