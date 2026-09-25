#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r48b -- (WALK-SHAPE), the LAST obligation of (DOM-MAJ), reduced to one inequality.

r48 (companion file) proved (CHAIN).  What is left of (DOM-MAJ) is (WALK-SHAPE), which r47
stated as a shape census.  This file turns the joint walk into arithmetic and shows what
(WALK-SHAPE) actually is.

--------------------------------------------------------------------------------------------
THE TWO SHAPES.  Along the joint walk of a transfer edge every state (A,B) has
        c_m(B) - c_m(A) = one of
  (T)   the indicator of an interval [y+1, x-1]      (sum B = sum A;  B is A with one unit
                                                      moved DOWN from a part x to a part y)
  (U)   [m >= v1+1] + [m >= v2+1],  v1 <= v2        (sum B = sum A + 2;  B is A with two
                                                      units ADDED; a doubled unit on a part
                                                      of value v is the case (v1,v2)=(v,v+1))
Block [2] censuses that no other shape occurs.  In shape (U) write d := max A; then
        max B - max A  =  0 if v2 < d,   1 if v2 = d,   2 if v2 = d+1,
so an INVERSION state is exactly a (U) state with v2 = d, and r47's `A_j` is v1.

--------------------------------------------------------------------------------------------
LEMMA T-STEP (PROVED, mine).  Let (A,B) be a (T) state with max A = max B = d and both steps
legal.  Then hh(B) is hh(A) with one entry lowered by 1 and one entry raised by 1, the
lowered entry being the larger, so hh(A) >= hh(B) in dominance, sum hh A = sum hh B, and the
state stays in shape (T).  In particular max hh A >= max hh B.
  Proof.  Both steps delete a head of the same size d and lower the entries in positions
  1..d by one.  Writing B_t = A_t - [t=p] + [t=q] with 1 <= p < q, the two step outputs
  therefore differ, ENTRY BY ENTRY BEFORE SORTING, by exactly -[t=p] + [t=q].  The entry at
  p has value A_p - [p<=d] and the entry at q has value A_q - [q<=d]; since A_p >= A_q + 2
  (else B = A) the first exceeds the second in every one of the three admissible
  index cases, so the move is a unit transfer DOWNWARD and dominance follows.  QED

LEMMA T0-STEP (PROVED, mine).  Let (A,B) be a (T) state with max A = max B + 1 (the unit was
moved down OUT OF the head) and both steps legal.  Then the successor is a (U) state whose
two marks sit on the entries at old positions d and q, and its  v2 <= max hh A  --- i.e.
max hh B - max hh A <= 1: the FACTOR-TWO-violating case delta = 2 cannot be entered.
  Proof.  B = A - e_0 + e_q is a partition, so A_1 <= A_0 - 1 = d - 1, and if q = d then
  A_d + 1 <= A_{d-1}, hence A_d - 1 < A_1 - 1 <= max hh A.  A doubled mark can only arise at
  q = d, and it then sits on an entry strictly below max hh A, so it raises the maximum by at
  most 1.  A single mark raises an entry by 1 and so raises the maximum by at most 1.  QED

LEMMA U-EXACT (PROVED, mine -- the CONVERSE of r47's (INV-STEP')).  Let B = A + e_0 + e_j be
a partition (j >= 1), both steps legal, d := max A.  Then
        hh A  <|  hh B      IF AND ONLY IF      A_j <= A_{d+1}   (i.e. rho_{A_j}(A) >= d+1),
and in that case hh B is hh A with the entry at position d+1 lowered by one and the entry at
position j raised by one (equal partitions when j = d+1 or A_j = A_{d+1}).
  Proof.  Entry by entry before sorting, hh(B)_t - hh(A)_t = [t=j] - [t=d+1].  So hh B is
  hh A with the entry at d+1 (value A_{d+1}) lowered and the entry at j (value A_j - [j<=d])
  raised.  If j <= d this is a unit transfer UPWARD unless the two entries coincide as a
  multiset move, i.e. unless A_{d+1} = A_j; upward transfers strictly break <|.  If
  j = d+1 the two cancel.  If j >= d+2 then B sorted forces A_j + 1 <= A_{j-1} <= A_{d+1},
  so the move is downward.  QED   (r47 measured this hypothesis to be EXACT on its
  population with a corrupt control; the `only if` above makes that a theorem.)

--------------------------------------------------------------------------------------------
THE MARK LAW (PROVED, mine).  In a (U) state with v2 < d (so both marks are on non-head
parts and both heads have size d) write rho_t := #{i >= 1 : A_i >= t}.  Using the conjugate
form of the step, conj(hh X)_t = min(rho_{t+1}, d) + max(rho_t - d, 0), a mark on value v
contributes +1 to conj(hh B) - conj(hh A) at t = v when rho_{v+1} < d and at t = v+1 when
rho_{v+1} >= d.  So the successor is again a (U) state and
        v  |-->  v - 1   if the part carrying the mark is decremented by the step,
        v  |-->  v       if it is not,
which is the obvious statement, now with an exact criterion.  Block [3] censuses it.

--------------------------------------------------------------------------------------------
WHAT REMAINS.  With T-STEP, T0-STEP, U-EXACT and (CHAIN) in hand, (DOM-MAJ) is equivalent to
        (U-INV)   at every (U) state of every transfer walk,  v1 <= A_{d+1}.
r47's own numbers say v1 in {0,1,2}; and v1 <= 1 is FREE (v1 = 0 is vacuous, and v1 = 1 is
exactly the LEGALITY of B's step, which forces rho_1(A) >= d+1 = max(A)+1).  So the entire
residual content of (DOM-MAJ) is the case v1 >= 2.  Blocks [4]/[5] measure it.

RULING CO': stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py; the conjugate
implementation stepC lifted BY SOURCE TEXT from w61_r47_transfer.py (sec 105) and diffed
against stepA on every step of every walk.  No SAT, no solver, no exhaustive search.
Interpreter: .venv/bin/python3 (pure Python).
"""
import re
import sys
import time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 300.0
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
    print("    [%s] %-84s hits=%d" % ("ok" if ok else "DEAD", name, hits))
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
    """the HH step, DIFFED against the conjugate implementation on every call."""
    global DIFFC
    r = stepA(list(X))
    out = () if r == "TERMINAL" else (None if r is None else norm(r))
    alt = stepC(X)
    DIFFC += 1
    if out != alt:
        print("!! stepA vs stepC DISAGREEMENT on %s : %s %s" % (X, out, alt))
        sys.exit(2)
    return out


def MX(X):
    return X[0] if X else 0


def pad(a, L):
    return list(a) + [0] * (L - len(a))


def dominates(a, b):
    L = max(len(a), len(b))
    A, B = pad(a, L), pad(b, L)
    sa = sb = 0
    for x, y in zip(A, B):
        sa += x
        sb += y
        if sb > sa:
            return False
    return True


def is_transfer(a, b):
    L = max(len(a), len(b))
    A, B = pad(a, L), pad(b, L)
    d = [y - x for x, y in zip(A, B)]
    if d.count(-1) != 1 or d.count(1) != 1 or d.count(0) != L - 2:
        return False
    return d.index(-1) < d.index(1)


V1GE2 = []
print("=" * 100)
print("w61 r48b -- the joint walk as arithmetic: T-STEP, T0-STEP, U-EXACT, the mark law,")
print("            and (WALK-SHAPE) reduced to ONE inequality (U-INV).")
print("=" * 100)


def build(nmax, maxparts, label):
    POP = {}
    for N in range(1, nmax + 1):
        for p in parts(N):
            if len(p) <= maxparts:
                cur, ok = p, True
                for _ in range(400):
                    nx = step(cur)
                    if nx is None:
                        ok = False
                        break
                    if nx == ():
                        break
                    cur = nx
                if ok:
                    POP[p] = True
    POP[()] = True
    return POP


def cprof(A, B, MLEV):
    """c_m(B) - c_m(A) for m = 0 .. MLEV-1."""
    return tuple(sum(min(v, m) for v in B) - sum(min(v, m) for v in A) for m in range(MLEV))


def classify(A, B, MLEV):
    """returns ('EQ',) | ('T', x, y) | ('U', v1, v2) | ('OTHER', profile).

    (T): c_m(B) - c_m(A) is the indicator of an interval [y+1, x-1]: B is A with one unit
         moved DOWN from a part of size x to a part of size y.
    (U): c_m(B) - c_m(A) = [m >= v1+1] + [m >= v2+1]: B is A with two units ADDED."""
    p = cprof(A, B, MLEV)
    g = sum(B) - sum(A)
    if p[0] != 0:
        return ("OTHER", p)
    if g == 0:
        if A == B:
            return ("EQ",)
        onepos = [m for m in range(MLEV) if p[m] == 1]
        if set(p) <= {0, 1} and onepos and onepos == list(range(onepos[0], onepos[-1] + 1)) \
                and p[MLEV - 1] == 0:
            return ("T", onepos[-1] + 1, onepos[0] - 1)      # x = top+1 , y = bottom-1
        return ("OTHER", p)
    if g == 2 and set(p) <= {0, 1, 2} and p[MLEV - 1] == 2 \
            and all(p[m] <= p[m + 1] for m in range(MLEV - 1)):
        v1 = min(m for m in range(MLEV) if p[m] >= 1) - 1
        v2 = min(m for m in range(MLEV) if p[m] == 2) - 1
        return ("U", v1, v2)
    return ("OTHER", p)


def analyse(nmax, maxparts, label, want_term=None, want_edges=None, want_inv=None):
    print("\n" + "-" * 100)
    POP = build(nmax, maxparts, label)
    MLEV = nmax + 2
    NEXT = {}
    for X in POP:
        NEXT[X] = step(X) if X != () else ()
    BYN = {}
    for p in POP:
        BYN.setdefault(sum(p), []).append(p)
    TE = []
    for N, lst in sorted(BYN.items()):
        for a in lst:
            for b in lst:
                if a != b and dominates(a, b) and is_transfer(a, b):
                    TE.append((a, b))
    print("%s  partitions of N <= %d with <= %d parts that TERMINATE : %d ; transfer edges : %d"
          % (label, nmax, maxparts, len(POP) - 1, len(TE)))
    if want_term is not None and len(POP) - 1 != want_term:
        bad("REPRO-TERM", "%s %d vs %d" % (label, len(POP) - 1, want_term))
    if want_edges is not None and len(TE) != want_edges:
        bad("REPRO-EDGES", "%s %d vs %d" % (label, len(TE), want_edges))

    # ------------------------------------------------- [2] the shape census over every state
    shapes = Counter()
    other_shapes = 0
    other_ex = None
    states = 0
    inv = 0
    uinv_ok = uinv_bad = 0
    uinv_ex = None
    v1_hist = Counter()
    v1_at_inv = Counter()
    ustates = 0
    delta2 = 0
    ucap_bad = 0
    tstep_t = tstep_bad = 0
    t0_t = t0_bad = 0
    uu_t = uu_bad = 0
    marklaw_t = marklaw_bad = 0
    marklaw_ex = None
    for (a0, b0) in TE:
        a, b = a0, b0
        for _ in range(80):
            states += 1
            cl = classify(a, b, MLEV)
            shapes[cl[0]] += 1
            if cl[0] == "OTHER":
                other_shapes += 1
                if other_ex is None:
                    other_ex = (a, b, cl)
            d = MX(a)
            if cl[0] == "U":
                ustates += 1
                v1, v2 = cl[1], cl[2]
                v1_hist[v1] += 1
                if v2 > d:
                    delta2 += 1
                # THE inequality (U-INV): v1 <= A_{d+1}
                adp1 = a[d + 1] if d + 1 < len(a) else 0
                if v1 <= adp1:
                    uinv_ok += 1
                else:
                    uinv_bad += 1
                    if uinv_ex is None:
                        uinv_ex = (a, b, v1, adp1)
                if v2 == d:
                    inv += 1
                    v1_at_inv[v1] += 1
                    if v1 > adp1:
                        ucap_bad += 1
            na, nb = NEXT[a], NEXT[b]
            if na == () or nb == ():
                break
            # --------------- the three step lemmas, checked on the state we are leaving
            if cl[0] == "T" and MX(a) == MX(b):
                tstep_t += 1
                cn = classify(na, nb, MLEV)
                if not (dominates(na, nb) and sum(na) == sum(nb)
                        and cn[0] in ("T", "EQ") and MX(na) >= MX(nb)):
                    tstep_bad += 1
            if cl[0] == "T" and MX(a) == MX(b) + 1:
                t0_t += 1
                cn = classify(na, nb, MLEV)
                if cn[0] != "U" or cn[2] > MX(na):
                    t0_bad += 1
            if cl[0] == "U" and cl[2] < MX(a):
                uu_t += 1
                cn = classify(na, nb, MLEV)
                if cn[0] != "U":
                    uu_bad += 1
                else:
                    # THE MARK LAW: v |-> v - [rho_{v+1} < d]
                    rho = lambda t: sum(1 for i in range(1, len(a)) if a[i] >= t)
                    pred = tuple(sorted(v - (1 if rho(v + 1) < d else 0)
                                        for v in (cl[1], cl[2])))
                    marklaw_t += 1
                    if pred != (cn[1], cn[2]) and cl[1] != cl[2]:
                        marklaw_bad += 1
                        if marklaw_ex is None:
                            marklaw_ex = (a, b, cl, cn, pred)
            a, b = na, nb
    print("    joint states on transfer walks : %d ; shapes %s" % (states, dict(shapes)))
    print("    states of NO admissible shape : %d   e.g. %s" % (other_shapes, other_ex))
    if other_shapes:
        bad("SHAPE", "%s %d %s" % (label, other_shapes, other_ex))
    ctrl("%s CONTROL: transfer walks visit states" % label, states)
    print("    (U) states %d ; of them INVERSIONS (v2 = max A) %d ; with v2 > max A (delta=2) %d"
          % (ustates, inv, delta2))
    if want_inv is not None and inv != want_inv:
        bad("REPRO-INV", "%s %d vs %d" % (label, inv, want_inv))
    print("    v1 over ALL (U) states     : %s" % dict(v1_hist))
    print("    v1 at the INVERSION states : %s" % dict(v1_at_inv))
    print("    (U-INV)  v1 <= A_{d+1} : holds %d , FAILS %d   e.g. %s"
          % (uinv_ok, uinv_bad, uinv_ex))
    if uinv_bad:
        bad("U-INV", "%s %d %s" % (label, uinv_bad, uinv_ex))
    if ucap_bad:
        bad("WALK-SHAPE", "%s %d" % (label, ucap_bad))
    if delta2:
        bad("DELTA2", "%s %d" % (label, delta2))
    print("    LEMMA T-STEP  instances %d , failures %d" % (tstep_t, tstep_bad))
    print("    LEMMA T0-STEP instances %d , failures %d" % (t0_t, t0_bad))
    print("    (U)->(U) steps %d , failures %d ; MARK LAW instances %d , failures %d  e.g. %s"
          % (uu_t, uu_bad, marklaw_t, marklaw_bad, marklaw_ex))
    for got, tag in ((tstep_bad, "T-STEP"), (t0_bad, "T0-STEP"), (uu_bad, "U-TO-U"),
                     (marklaw_bad, "MARK-LAW")):
        if got:
            bad(tag, "%s %d" % (label, got))
    ctrl("%s CONTROL: (U) states occur" % label, ustates)
    ctrl("%s CONTROL: LEMMA T-STEP was exercised" % label, tstep_t)
    ctrl("%s CONTROL: LEMMA T0-STEP was exercised" % label, t0_t)
    ctrl("%s CONTROL: (U)->(U) propagation was exercised" % label, uu_t)
    # MY OWN MIS-DECLARED CONTROL, kept and repaired BY RUNNING: I first wrote this control
    # with must_fire=False, i.e. I predicted the v1 >= 2 case would be EMPTY.  It is empty at
    # N <= 16 and NON-EMPTY at N <= 20 and N <= 24.  A single-size census would have licensed
    # the wrong sentence; the count is reported and the sec 111 line below carries all three.
    V1GE2.append(sum(c for v, c in v1_at_inv.items() if v >= 2))
    print("    v1 >= 2 inversions (the ONLY case in which (U-INV) is not free) : %d"
          % V1GE2[-1])

    # ------------------------------------------- [5] LEMMA U-EXACT, both directions, censused
    ue_t = ue_if = ue_onlyif = 0
    ue_yes = ue_no = 0
    ue_ex = None
    for A in POP:
        if A == () or over():
            continue
        d = MX(A)
        L = list(A)
        for j in range(1, len(L) + 1):
            Bl = [d + 1] + L[1:] + [0]
            if j >= len(Bl):
                continue
            Bl[j] += 1
            if list(Bl) != sorted(Bl, reverse=True):
                continue
            B = norm(Bl)
            sB = step(B)
            sA = step(A)
            if sB is None or sA is None:
                continue
            ue_t += 1
            aj = L[j] if j < len(L) else 0
            adp1 = L[d + 1] if d + 1 < len(L) else 0
            hyp = (aj <= adp1)
            concl = all(sum(min(v, m) for v in sA) <= sum(min(v, m) for v in sB)
                        for m in range(MLEV))
            if hyp:
                ue_yes += 1
                if not concl:
                    ue_if += 1
                    if ue_ex is None:
                        ue_ex = ("IF", A, B, j)
            else:
                ue_no += 1
                if concl:
                    ue_onlyif += 1
                    if ue_ex is None:
                        ue_ex = ("ONLYIF", A, B, j)
    print("    LEMMA U-EXACT: instances %d  (hypothesis TRUE %d , FALSE %d)"
          % (ue_t, ue_yes, ue_no))
    print("      'if'      failures (hyp holds, <| breaks)     : %d" % ue_if)
    print("      'only if' failures (hyp fails, <| survives)   : %d   e.g. %s"
          % (ue_onlyif, ue_ex))
    if ue_if or ue_onlyif:
        bad("U-EXACT", "%s %d/%d %s" % (label, ue_if, ue_onlyif, ue_ex))
    ctrl("%s CONTROL: U-EXACT tested where the hypothesis HOLDS" % label, ue_yes)
    ctrl("%s CORRUPT CONTROL: U-EXACT tested where the hypothesis FAILS -- and <| breaks at "
         "every one of them" % label, ue_no)
    return dict(term=len(POP) - 1, edges=len(TE), states=states, ustates=ustates, inv=inv,
                uinv_bad=uinv_bad, v1inv=dict(v1_at_inv))


r16 = analyse(16, 10, "[N<=16]", want_term=181, want_edges=567, want_inv=88)
r20 = analyse(20, 12, "[N<=20]", want_term=531, want_edges=2233, want_inv=395)
r24 = analyse(24, 14, "[N<=24]")

print("\n" + "=" * 100)
print("sec 111: THREE sizes now, not two.  inversion states %d / %d / %d ; (U-INV) failures "
      "%d / %d / %d" % (r16["inv"], r20["inv"], r24["inv"],
                        r16["uinv_bad"], r20["uinv_bad"], r24["uinv_bad"]))
print("v1 at inversions, by size : %s | %s | %s" % (r16["v1inv"], r20["v1inv"], r24["v1inv"]))
print("v1 >= 2 inversions by size : %s  -- EMPTY at the smallest size and non-empty after it"
      % (V1GE2,))
ctrl("CONTROL: the v1 >= 2 case, which I first predicted to be empty, is NOT empty once the "
     "population grows", sum(V1GE2))
ok = sum(1 for _, _, o in CTRL if o)
print("stepA vs stepC (conjugate coordinates) diffed calls : %d , 0 disagreements" % DIFFC)
print("ELAPSED %.2f s / %.0f s internal limit ; PARTIAL=%s" % (time.time() - T0, LIMIT, PARTIAL))
print("CONTROLS %d/%d firing ; DEFECTS %d" % (ok, len(CTRL), len(FAIL)))
for f in FAIL:
    print("   DEFECT: %s" % f)
print("=" * 100)
sys.exit(1 if FAIL or PARTIAL else 0)
