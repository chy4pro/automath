#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r48c -- THE CERTIFICATE R, AND ITS CLOSURE.  Every case of the proof, one block each.

r47 left (DOM-MAJ) resting on (WALK-SHAPE) + (CHAIN).  w61_r48_chain.py proves (CHAIN).
This file exhibits an EXPLICIT MEMORYLESS relation R on pairs of partitions, proves it is
closed under the joint HH step, and thereby proves (DOM-MAJ) on transfer edges -- which is
(WALK-SHAPE)'s entire job.

--------------------------------------------------------------------------------------------
THE SHAPES.  For a pair (A,B) put P_m := c_m(B) - c_m(A), where c_m(X) = sum_i min(X_i, m).
  (EQ)  A = B.
  (T)   P is the indicator of an interval [y+1, x-1]:  B is A with ONE unit moved DOWN from a
        part of size x to a part of size y  (sum B = sum A).
  (U)   P_m = [m >= v1+1] + [m >= v2+1] with v1 <= v2:  B is A with TWO units ADDED, to parts
        of sizes v1 and v2  (sum B = sum A + 2).  A doubled unit on one part of size v is the
        case (v1,v2) = (v,v+1).  If v1 >= 1 then A HAS a part of size exactly v1.
Write d := max A.  In shape (U), max B - max A = 0 / 1 / 2 according as v2 < d / v2 = d /
v2 = d+1.

        R  :=  { (A,B) : (EQ) }
             u { (A,B) : (T) }
             u { (A,B) : (U) and v2 <= d and v1 <= A_{d+1} }.

The (T) clause carries NO dominance hypothesis: shape (T) has P_m >= 0 with P_infinity = 0,
which IS A >= B.  My first draft of R wrote `and A >= B in dominance` there; block [4] runs
the drop as a corrupt control, it finds ZERO closure violations, and block [4t] then checks
the redundancy directly.  The conjunct is deleted from R by that run, not by assertion.

R is MEMORYLESS (a predicate on the pair alone), it CONTAINS every transfer edge (block [1]),
and it IMPLIES sum A <= sum B (block [2]).  Note  v1 <= A_{d+1}  is exactly r47's
rho_{v1}(A) >= max(A)+1.

--------------------------------------------------------------------------------------------
THEOREM R-CLOSED (PROVED, mine).  If (A,B) in R and A is not terminal (so both steps are
legal whenever A, B are graphic), then (hh A, hh B) in R.

Case EQ.  The step is deterministic.  QED

Case T, max A = max B  (block [3a]).  A copy of the head of size d is deleted on both sides
and positions 1..d are lowered by one on both sides, so entry by entry BEFORE SORTING
hh(B)_t - hh(A)_t = -[t=p] + [t=q] with 1 <= p < q.  The entries carrying those changes have
values A_p - [p<=d] and A_q - [q<=d]; B sorted gives A_p - 1 >= A_q + 1, so in each of the
three admissible index cases the lowered entry exceeds the raised one by at least 1.  A move
of one unit from a strictly larger entry to a smaller one leaves the multiset alone (gap 1)
or strictly lowers it in dominance (gap >= 2).  Hence shape (T) or (EQ) with hh A >= hh B. QED

Case T, max A = max B + 1  (block [3b]).  Then B = A - e_0 + e_q with A_1 <= d-1, and
hh(B)_t - hh(A)_t = [t=d] + [t=q], a (U) state whose marks sit on the entries of hh A at
positions d and q, of values m_d := A_d - 1 and m_q := A_q - [q<=d].
 * v2 <= d' := max hh A = max(A_1 - 1, A_{d+1}):  m_d <= A_1 - 1; if q <= d then
   m_q <= A_1 - 1; if q > d then m_q <= A_{d+1}; and in the doubled case q = d, B sorted
   forces A_d + 1 <= A_{d-1} <= A_1, so the doubled value A_d <= A_1 - 1.
 * v1 <= A'_{d'+1}:  v1 <= m_d = A_d - 1, and hh A has the d entries A_1-1 >= ... >= A_d-1,
   all >= A_d - 1.  Since A_1 <= d-1 we get d' <= d-1.  If A_d = 1 then v1 <= A_d - 1 = 0 and
   the conclusion is trivial, so assume A_d >= 2, where those d entries are all POSITIVE and
   therefore really are entries of the partition hh A.  If d' <= d-2 they already put
   A'_{d'+1} >= A_d - 1.  If d' = d-1 then A_{d+1} = d-1, which with A_1 <= d-1 forces
   A_1 = ... = A_{d+1} = d-1, so hh A also holds the tail entry A_{d+1} = d-1 >= A_d - 1 and
   there are d+1 = d'+2 entries >= A_d - 1.  QED
   [The proviso A_d >= 2 is MY OWN SCOPING DEFECT, caught by this run and repaired BY RUNNING:
   block [3s] states the count claim FIRST without it, that statement FAILS, and a further
   line checks that EVERY failure has A_d = 1 -- exactly the case the conclusion does not
   need.  Both the failing count and the corrected count are printed, neither is deleted.]

Case U, v2 = d  (block [3c], = LEMMA U-EXACT).  B = A + e_0 + e_j is a partition, and
hh(B)_t - hh(A)_t = [t=j] - [t=d+1]: hh B is hh A with the entry at d+1 (value A_{d+1})
lowered and the entry at j (value A_j - [j<=d]) raised.  If j >= d+2 then B sorted gives
A_j + 1 <= A_{j-1} <= A_{d+1}, a DOWNWARD move; if j = d+1 the two cancel; if j <= d then
A_j <= A_{d+1} is the hypothesis and forces A_j = A_{d+1}, where the move again leaves the
multiset alone.  Hence shape (T) or (EQ) with hh A >= hh B.
CONVERSELY if j <= d and A_j > A_{d+1} the move is UPWARD and <| fails, so the hypothesis is
not merely sufficient: it is EXACT.  QED

Case U, v2 < d  (block [3d]).  Both heads have size d and both marked parts are non-head
parts, so rho_t(B) = rho_t(A) + [t=v1+1] + [t=v2+1] for rho_t(X) := #{i>=1 : X_i >= t}.  The
conjugate form of the step, conj(hh X)_t = min(rho_{t+1}, d) + max(rho_t - d, 0), turns a
single mark on a part of size v into a single mark on a part of size
        v - 1  if rho_{v+1} < d   (the part is inside the block of d entries the step lowers)
        v      if rho_{v+1} >= d  (it is not),
so the successor is again a (U) state -- THE MARK LAW.  Write d' := max hh A =
max(A_1 - 1, A_{d+1}) and z := v1' the new lower mark.
 * v2' <= d'.  The part carrying v2 has size v2, so A_1 >= v2; if the mark does not move then
   rho_{v2+1} >= d >= 1 gives A_1 >= v2+1.  Either way d' >= A_1 - 1 >= v2'.
 * v1' <= A'_{d'+1}, i.e. #{entries of hh A >= z} >= d'+2.  If z = 0 it is trivial.  Else
   every non-head part of A of size >= v1 yields an entry of hh A of size >= v1 - 1, and when
   the mark did NOT move (rho_{v1+1} >= d) the d lowered entries are all >= v1+1, so parts of
   size exactly v1 survive untouched and the same count works at level v1.  Either way
        #{entries of hh A >= z}  >=  rho_{v1}(A)  >=  d+1,
   the last step being the hypothesis v1 <= A_{d+1}.  Now d' <= d always, and d' = d forces
   A_{d+1} = d, i.e. A = (d^k, others) with k >= d+2; then
   hh A = (d^{k-1-d}, (d-1)^d, others) and, since z <= v2 < d, the count is
   k-1 + #{others >= z} >= (d+1) + 1 = d'+2 because A carries a part of size exactly
   v1 < d, which is one of the `others`.  If d' <= d-1 then d'+2 <= d+1 and the bound
   rho_{v1} >= d+1 already suffices.  QED

--------------------------------------------------------------------------------------------
COROLLARY (DOM-MAJ).  For an equal-sum dominance pair (A,B) of graphic partitions,
mu(A) >= mu(B) in dominance.
  Proof.  By (CHAIN) (w61_r48_chain.py) it is enough to treat a single transfer edge, since
  mu-dominance is transitive and mu(X) is a partition of sum(X)/2 by (MU) (r47).  A transfer
  edge lies in R; R is closed and implies sum A <= sum B; so sum A^{(k)} <= sum B^{(k)} for
  every k, which is exactly mu(A) >= mu(B).  QED

--------------------------------------------------------------------------------------------
sec 90 / sec 104 -- WHAT COULD HAVE COME OUT THE OTHER WAY.
 * R's two (U) conjuncts are each DROPPED in block [4]; each drop must produce closure
   violations, or the conjunct was decoration.  Both do.  The `A >= B` I first wrote into the
   (T) clause is dropped there too and changes NOTHING -- that is how it was found redundant
   and removed from R, with block [4t] checking the implication directly.
 * The (U) hypothesis is NOT implied by graphicness: block [5] exhibits pairs (A,B) both
   GRAPHIC with B = A + e_0 + e_j and A_j > A_{d+1}.  So R is a strictly smaller relation
   than "both graphic", and its closure is a real restriction, not a tautology.
 * r47's own D* was refuted by exactly this kind of test; block [3] runs the same test on R.

RULING CO': stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py; the conjugate
implementation stepC lifted BY SOURCE TEXT from w61_r47_transfer.py and diffed against stepA
on every call.  No SAT, no solver, no exhaustive search.  Interpreter .venv/bin/python3.
"""
import re
import sys
import time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 600.0
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
SRC2 = ROOT / "problems/wowii/w61_r47_transfer.py"


def grab(t, name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---|print|NMAX|absorb|T0|MLEV))"
                  % re.escape(name), t, re.S | re.M)
    assert m, name
    return m.group(0)


ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(SRC.read_text(), n) for n in ("stepA", "runA", "runB")),
             str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]
ns2 = {}
exec(compile("\n".join(grab(SRC2.read_text(), n) for n in ("conj", "unconj", "stepC")),
             str(SRC2), "exec"), ns2)
stepC = ns2["stepC"]

FAIL = []
CTRL = []
PARTIAL = False
DIFFC = 0


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
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append((name, hits, ok))
    print("    [%s] %-82s hits=%d" % ("ok" if ok else "DEAD", name, hits))
    if not ok:
        bad("CONTROL-DEAD", name)


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


def norm(x):
    return tuple(sorted([v for v in x if v > 0], reverse=True))


def step(X):
    """HH step; () terminal, None illegal.  DIFFED against the conjugate implementation."""
    global DIFFC
    r = stepA(list(X))
    out = () if r == "TERMINAL" else (None if r is None else norm(r))
    alt = stepC(X)
    DIFFC += 1
    if out != alt:
        print("!! stepA vs stepC DISAGREEMENT on %s : %s %s" % (X, out, alt))
        sys.exit(2)
    return out


def terminates(X):
    cur = X
    for _ in range(500):
        n = step(cur)
        if n is None:
            return False
        if n == ():
            return True
        cur = n
    return False


def MX(X):
    return X[0] if X else 0


def AT(X, i):
    return X[i] if i < len(X) else 0


def dominates(a, b):
    L = max(len(a), len(b))
    A = list(a) + [0] * (L - len(a))
    B = list(b) + [0] * (L - len(b))
    sa = sb = 0
    for x, y in zip(A, B):
        sa += x
        sb += y
        if sb > sa:
            return False
    return True


def is_transfer(a, b):
    L = max(len(a), len(b))
    A = list(a) + [0] * (L - len(a))
    B = list(b) + [0] * (L - len(b))
    d = [y - x for x, y in zip(A, B)]
    if d.count(-1) != 1 or d.count(1) != 1 or d.count(0) != L - 2:
        return False
    return d.index(-1) < d.index(1)


print("=" * 100)
print("w61 r48c -- the certificate R, its closure case by case, and (DOM-MAJ).")
print("=" * 100)


def run(NMAX, label, want_pairs=None, want_edges=None):
    print("\n" + "-" * 100)
    MLEV = NMAX + 3
    GR = []
    for N in range(1, NMAX + 1):
        for p in parts(N):
            if terminates(p):
                GR.append(p)
    GR.append(())
    CV = {X: tuple(sum(min(v, m) for v in X) for m in range(MLEV)) for X in GR}
    NXT = {X: (step(X) if X else ()) for X in GR}
    print("%s  graphic partitions of N <= %d (no cap on parts) : %d" % (label, NMAX, len(GR) - 1))

    def classify(A, B):
        p = tuple(y - x for x, y in zip(CV[A], CV[B]))
        g = sum(B) - sum(A)
        if p[0] != 0:
            return ("OTHER",)
        if g == 0:
            if A == B:
                return ("EQ",)
            one = [m for m in range(MLEV) if p[m] == 1]
            if set(p) <= {0, 1} and one and one == list(range(one[0], one[-1] + 1)) \
                    and p[MLEV - 1] == 0:
                return ("T", one[-1] + 1, one[0] - 1)
            return ("OTHER",)
        if g == 2 and set(p) <= {0, 1, 2} and p[MLEV - 1] == 2 \
                and all(p[m] <= p[m + 1] for m in range(MLEV - 1)):
            v1 = min(m for m in range(MLEV) if p[m] >= 1) - 1
            v2 = min(m for m in range(MLEV) if p[m] == 2) - 1
            return ("U", v1, v2)
        return ("OTHER",)

    def inR(A, B, use_v1=True, use_v2=True, use_dom=False):
        c = classify(A, B)
        if c[0] == "EQ":
            return True
        if c[0] == "T":
            # use_dom=True reinstates my FIRST DRAFT of R, which carried `and A >= B`;
            # block [4] shows the conjunct is redundant, so R itself does not use it.
            return dominates(A, B) if use_dom else True
        if c[0] == "U":
            d = MX(A)
            okv1 = (c[1] <= AT(A, d + 1)) if use_v1 else True
            okv2 = (c[2] <= d) if use_v2 else True
            return okv1 and okv2
        return False

    # ------------------------------------------------------------------ [1] R covers the edges
    BYN = {}
    for X in GR:
        BYN.setdefault(sum(X), []).append(X)
    TE = []
    for N, lst in sorted(BYN.items()):
        for a in lst:
            for b in lst:
                if a != b and dominates(a, b) and is_transfer(a, b):
                    TE.append((a, b))
    miss = sum(1 for (a, b) in TE if not inR(a, b))
    print("    [1] transfer edges of graphic partitions : %d ; NOT in R : %d" % (len(TE), miss))
    if miss:
        bad("R-COVER", "%s %d" % (label, miss))
    ctrl("%s CONTROL: there are transfer edges to cover" % label, len(TE))
    if want_edges is not None and len(TE) != want_edges:
        print("        (edge count differs from the r47 window, which capped the parts: %d)"
              % want_edges)

    # ------------------------------------------------- [2] R implies sum A <= sum B, and R-set
    RPAIRS = []
    bad_sum = 0
    for A in GR:
        if over():
            break
        for B in GR:
            g = sum(B) - sum(A)
            if g not in (0, 2):
                continue
            if not inR(A, B):
                continue
            RPAIRS.append((A, B))
            if sum(A) > sum(B):
                bad_sum += 1
    print("    [2] pairs in R : %d ; of them with sum A > sum B : %d" % (len(RPAIRS), bad_sum))
    if bad_sum:
        bad("R-SUM", "%s %d" % (label, bad_sum))
    ctrl("%s CONTROL: R is a non-empty relation" % label, len(RPAIRS))

    # -------------------------------------------------------- [3] CLOSURE, ONE BLOCK PER CASE
    cases = Counter()
    viol = Counter()
    ex = {}
    unclassified = 0
    sub_bad = Counter()
    sub_t = Counter()
    for (A, B) in RPAIRS:
        if A == ():
            continue
        c = classify(A, B)
        na, nb = NXT[A], NXT[B]
        if na is None or nb is None:
            bad("ILLEGAL-STEP", "%s %s" % (A, B))
            continue
        d = MX(A)
        if c[0] == "EQ":
            key = "EQ"
        elif c[0] == "T" and MX(A) == MX(B):
            key = "T-flat"
        elif c[0] == "T" and MX(A) == MX(B) + 1:
            key = "T-head"
        elif c[0] == "U" and c[2] == d:
            key = "U-inv"
        elif c[0] == "U" and c[2] < d:
            key = "U-flat"
        else:
            unclassified += 1
            key = "UNCLASSIFIED"
        cases[key] += 1
        if not inR(na, nb):
            viol[key] += 1
            if key not in ex:
                ex[key] = (A, B, c, na, nb, classify(na, nb))
        # ---- the individual sub-claims the proof of each case rests on
        cn = classify(na, nb)
        if key == "T-flat":
            sub_t["T-flat: successor is (T) or (EQ) with hh A >= hh B"] += 1
            if not (cn[0] in ("T", "EQ") and dominates(na, nb)):
                sub_bad["T-flat: successor is (T) or (EQ) with hh A >= hh B"] += 1
        if key == "T-head":
            dp = MX(na)
            sub_t["T-head: A_1 <= d-1"] += 1
            if not AT(A, 1) <= d - 1:
                sub_bad["T-head: A_1 <= d-1"] += 1
            sub_t["T-head: d' <= d-1"] += 1
            if not dp <= d - 1:
                sub_bad["T-head: d' <= d-1"] += 1
            sub_t["T-head: successor is (U)"] += 1
            if cn[0] != "U":
                sub_bad["T-head: successor is (U)"] += 1
            else:
                sub_t["T-head: v1' <= A_d - 1"] += 1
                if not cn[1] <= AT(A, d) - 1:
                    sub_bad["T-head: v1' <= A_d - 1"] += 1
                # MY OWN MIS-SCOPING, kept and printed: the count claim is stated first
                # WITHOUT the proviso A_d >= 2 and fails; every failure has A_d = 1, where
                # v1' <= A_d - 1 = 0 makes the conclusion trivial.
                sub_t["T-head: #{hh A >= A_d-1} >= d'+2   (MIS-SCOPED, no proviso)"] += 1
                if not sum(1 for v in na if v >= AT(A, d) - 1) >= dp + 2:
                    sub_bad["T-head: #{hh A >= A_d-1} >= d'+2   (MIS-SCOPED, no proviso)"] += 1
                    if AT(A, d) != 1:
                        sub_bad["T-head: EVERY mis-scoped failure has A_d = 1"] += 1
                    sub_t["T-head: EVERY mis-scoped failure has A_d = 1"] += 1
                if AT(A, d) >= 2:
                    sub_t["T-head: #{hh A >= A_d-1} >= d'+2   given A_d >= 2 (CORRECTED)"] += 1
                    if not sum(1 for v in na if v >= AT(A, d) - 1) >= dp + 2:
                        sub_bad["T-head: #{hh A >= A_d-1} >= d'+2   given A_d >= 2 (CORRECTED)"] += 1
        if key == "U-inv":
            sub_t["U-inv: successor is (T) or (EQ) with hh A >= hh B"] += 1
            if not (cn[0] in ("T", "EQ") and dominates(na, nb)):
                sub_bad["U-inv: successor is (T) or (EQ) with hh A >= hh B"] += 1
        if key == "U-flat":
            rho = [0] * (MLEV + 2)
            for t in range(1, MLEV + 2):
                rho[t - 1] = sum(1 for i in range(1, len(A)) if A[i] >= t)
            RHO = lambda t: (rho[t - 1] if 1 <= t <= MLEV + 1 else 0)
            sub_t["U-flat: successor is (U)"] += 1
            if cn[0] != "U":
                sub_bad["U-flat: successor is (U)"] += 1
            else:
                dp = MX(na)
                sub_t["U-flat: MARK LAW predicts the new marks"] += 1
                pred = tuple(sorted(v - (1 if RHO(v + 1) < d else 0) for v in (c[1], c[2])))
                if c[1] != c[2] and pred != (cn[1], cn[2]):
                    sub_bad["U-flat: MARK LAW predicts the new marks"] += 1
                sub_t["U-flat: rho_{v1}(A) >= d+1"] += 1
                if c[1] >= 1 and not RHO(c[1]) >= d + 1:
                    sub_bad["U-flat: rho_{v1}(A) >= d+1"] += 1
                sub_t["U-flat: #{hh A >= v1'} >= d'+2"] += 1
                if cn[1] >= 1 and not sum(1 for v in na if v >= cn[1]) >= dp + 2:
                    sub_bad["U-flat: #{hh A >= v1'} >= d'+2"] += 1
                sub_t["U-flat: d' = d only when A_{d+1} = d"] += 1
                if dp == d and AT(A, d + 1) != d:
                    sub_bad["U-flat: d' = d only when A_{d+1} = d"] += 1
                sub_t["U-flat: v1 >= 1 implies A has a part of size exactly v1"] += 1
                if c[1] >= 1 and c[1] not in A:
                    sub_bad["U-flat: v1 >= 1 implies A has a part of size exactly v1"] += 1
    print("    [3] CLOSURE of R, by case (each is a place the theorem could fail):")
    tot_v = 0
    for k in ("EQ", "T-flat", "T-head", "U-inv", "U-flat", "UNCLASSIFIED"):
        print("        %-14s instances %7d   closure violations %d   %s"
              % (k, cases.get(k, 0), viol.get(k, 0), ex.get(k, "")))
        tot_v += viol.get(k, 0)
        if viol.get(k, 0):
            bad("R-CLOSURE-" + k, "%s %d %s" % (label, viol[k], ex.get(k)))
    if unclassified:
        bad("R-CASES-NOT-EXHAUSTIVE", "%s %d" % (label, unclassified))
    print("        TOTAL closure violations : %d" % tot_v)
    for k in ("EQ", "T-flat", "T-head", "U-inv", "U-flat"):
        ctrl("%s CONTROL: closure case %s is non-empty" % (label, k), cases.get(k, 0))
    print("    [3s] the sub-claims the case proofs rest on:")
    for k in sorted(sub_t):
        print("        %-62s tested %6d  failures %d" % (k, sub_t[k], sub_bad.get(k, 0)))
        if sub_bad.get(k, 0) and "MIS-SCOPED" not in k:
            bad("SUBCLAIM", "%s %s %d" % (label, k, sub_bad[k]))

    # ------------------------------------------------------- [4] EACH CONJUNCT OF R, DROPPED
    print("    [4] CORRUPT CONTROLS: drop one conjunct of R and re-test closure.")
    for tag, kw in (("drop  v1 <= A_{d+1}", dict(use_v1=False)),
                    ("drop  v2 <= max A", dict(use_v2=False)),
                    ("drop  A >= B on (T)", dict(use_dom=False))):
        t = v = 0
        exc = None
        for A in GR:
            if over():
                break
            if A == ():
                continue
            for B in GR:
                if sum(B) - sum(A) not in (0, 2):
                    continue
                if not inR(A, B, **kw):
                    continue
                t += 1
                na, nb = NXT[A], NXT[B]
                if na is None or nb is None:
                    continue
                if not inR(na, nb, **kw):
                    v += 1
                    if exc is None:
                        exc = (A, B)
        print("        %-22s : pairs %6d  closure violations %5d   e.g. %s" % (tag, t, v, exc))
        if "A >= B" in tag:
            # THIS control is DEAD by construction, and the reason is block [4t]: the (T)
            # shape already implies A >= B, so there is nothing to drop.  Recorded as a
            # REDUNDANCY, not as a live conjunct.
            ctrl("%s CONTROL: reinstating my first draft's `A >= B` on (T) changes nothing "
                 "-- it is redundant" % label, v, must_fire=False)
        else:
            ctrl("%s CORRUPT CONTROL: %s BREAKS closure" % (label, tag), v)

    # ------------------------------- [4t] why that control is dead: (T) shape IMPLIES A >= B
    tsh = tnd = 0
    for A in GR:
        if over():
            break
        for B in GR:
            if sum(B) != sum(A):
                continue
            if classify(A, B)[0] != "T":
                continue
            tsh += 1
            if not dominates(A, B):
                tnd += 1
    print("    [4t] (T)-shaped pairs : %d ; of them NOT satisfying A >= B : %d" % (tsh, tnd))
    if tnd:
        bad("T-IMPLIES-DOM", "%s %d" % (label, tnd))
    ctrl("%s CONTROL: there are (T)-shaped pairs to test the redundancy on" % label, tsh)

    # --------------------------------------------- [5] the hypothesis is NOT implied by graphic
    st_t = st_bad = 0
    st_ex = None
    for A in GR:
        if A == () or over():
            continue
        d = MX(A)
        L = list(A)
        for j in range(1, len(L) + 1):
            Bl = [d + 1] + L[1:] + [0]
            if j >= len(Bl):
                continue
            Bl[j] += 1
            if Bl != sorted(Bl, reverse=True):
                continue
            B = norm(Bl)
            if sum(B) > NMAX or B not in CV:
                continue
            st_t += 1
            if AT(A, j) > AT(A, d + 1):
                st_bad += 1
                if st_ex is None:
                    st_ex = (A, B, j, AT(A, j), AT(A, d + 1))
    print("    [5] (A,B) BOTH GRAPHIC with B = A + e_0 + e_j : %d ; of them with A_j > A_{d+1}"
          " (so NOT in R) : %d" % (st_t, st_bad))
    print("        e.g. %s" % (st_ex,))
    ctrl("%s CONTROL: graphicness ALONE does not give the (U) hypothesis -- R is strictly "
         "smaller" % label, st_bad)

    # ---------------------------------------------------------------- [6] (DOM-MAJ), end to end
    MU = {}
    for X in GR:
        m = []
        cur = X
        while cur != ():
            m.append(MX(cur))
            cur = NXT[cur]
        MU[X] = tuple(m)
    dm_t = dm_bad = 0
    dm_ex = None
    walk_t = walk_bad = 0
    for N, lst in sorted(BYN.items()):
        if over():
            break
        for A in lst:
            for B in lst:
                if A == B or not dominates(A, B):
                    continue
                dm_t += 1
                if not dominates(MU[A], MU[B]):
                    dm_bad += 1
                    if dm_ex is None:
                        dm_ex = (A, B, MU[A], MU[B])
    for (a0, b0) in TE:
        a, b = a0, b0
        for _ in range(80):
            walk_t += 1
            if not inR(a, b):
                walk_bad += 1
            if a == ():
                break
            a, b = NXT[a], NXT[b]
    print("    [6] equal-sum dominance pairs of graphic partitions : %d ; (DOM-MAJ) FAILURES %d"
          "   e.g. %s" % (dm_t, dm_bad, dm_ex))
    print("        joint states on transfer walks : %d ; states OUTSIDE R : %d"
          % (walk_t, walk_bad))
    if dm_bad:
        bad("DOM-MAJ", "%s %d %s" % (label, dm_bad, dm_ex))
    if walk_bad:
        bad("WALK-IN-R", "%s %d" % (label, walk_bad))
    ctrl("%s CONTROL: (DOM-MAJ) was tested on a non-empty population" % label, dm_t)
    if want_pairs is not None and dm_t != want_pairs:
        print("        (differs from r47's windowed count %d, which capped the parts)"
              % want_pairs)
    return dict(pairs=dm_t, rpairs=len(RPAIRS), viol=tot_v, edges=len(TE))


a = run(16, "[N<=16]")
b = run(20, "[N<=20]")
c = run(22, "[N<=22]")

print("\n" + "=" * 100)
print("sec 111: THREE sizes.  |R| = %d / %d / %d ; closure violations %d / %d / %d ; "
      "dominance pairs %d / %d / %d"
      % (a["rpairs"], b["rpairs"], c["rpairs"], a["viol"], b["viol"], c["viol"],
         a["pairs"], b["pairs"], c["pairs"]))
ok = sum(1 for _, _, o in CTRL if o)
print("stepA vs stepC (conjugate coordinates) diffed calls : %d , 0 disagreements" % DIFFC)
print("ELAPSED %.2f s / %.0f s internal limit ; PARTIAL=%s" % (time.time() - T0, LIMIT, PARTIAL))
print("CONTROLS %d/%d firing ; DEFECTS %d" % (ok, len(CTRL), len(FAIL)))
for f in FAIL:
    print("   DEFECT: %s" % f)
print("=" * 100)
sys.exit(1 if FAIL or PARTIAL else 0)
