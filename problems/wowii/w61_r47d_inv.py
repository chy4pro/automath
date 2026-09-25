#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r47d -- THE INVERSION STEP, DERIVED AND THEN TESTED.

r47/r47b measured that along the joint walk of a TRANSFER EDGE every inversion state (the only
place Theorem CAP-STEP-MONO does not reach) has delta = 1 and g = 2 and L1 distance 2 -- 88 of
them at N <= 16, 395 at N <= 20, with no exceptions.  An L1 distance of 2 together with a sum
gap of 2 forces  B = A + e_i + e_j  (two coordinates raised by one) or  B = A + 2 e_i, and
delta = 1 forces the raised coordinate to include the head.  So an inversion state is

        B = A + e_0 + e_j ,   for some j >= 1.

DERIVATION (mine).  Write d := max A, so max B = d + 1, and rho_{m+1} := #{i >= 1 : A_i >= m+1}.
By (CAP-STEP) applied to each side, and using
        c_m(B) = c_m(A) + [m >= d+1] + [m >= A_j + 1],
        rho_{m+1}(B) = rho_{m+1} + [A_j = m],
one gets, for every m,

        c_m(hh B) - c_m(hh A)  =  [m >= A_j + 1] - 1 + BR_m,
        BR_m := min(rho_{m+1} + [A_j = m], d+1) - min(rho_{m+1}, d)  in {0,1},

and BR_m = 1 exactly when rho_{m+1} >= d+1 or A_j = m.  Hence

  * m >= A_j + 1  ==>  the difference is BR_m >= 0                                  (free)
  * m  = A_j      ==>  BR_m = 1, difference 0                                       (free)
  * m <  A_j      ==>  the difference is BR_m - 1, so <| survives ONLY IF
                       rho_{m+1}(A) >= d + 1.

Since A is sorted, A_1 >= ... >= A_j >= m+1 for every m < A_j, so rho_{m+1} >= j, and j >= d+1
is SUFFICIENT.  And when A_j = 0 the third case is EMPTY, so:

  LEMMA (INV-STEP) (PROVED, mine).  If B = A + e_0 + e_j with A_j = 0 -- i.e. B is A with its
  head raised by one and a new part of size 1 appended -- and both HH steps are legal, then
  hh A <| hh B.  (No hypothesis on <|, on the sums, or on the maxima.)

  Proof: the case split above; the only case that can fail is m < A_j, which is empty. QED

That lemma is exactly the shape of the smallest inversion this line has been carrying since r46:
(3,2,2,1) vs (2,2,2,2) reaches (1,1) vs (2,1,1) at k = 1, and (2,1,1) = (1,1) + e_0 + a new 1.

THIS FILE ASKS THE ONE QUESTION THAT DECIDES WHETHER THE LEMMA COVERS THE WHOLE RESIDUE:
is A_j = 0 at EVERY inversion state of EVERY transfer walk, or only at some?  It reports the
answer either way, together with (i) the lemma censused on its own general population, (ii) the
corrupt control A_j >= 1 which the derivation predicts CAN fail, and (iii) the same two counts
at N <= 20.  Interpreter .venv/bin/python3.  RULING CO' + sec 105 as in r47/r47b/r47c.
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 420.0
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()


def grab(t, name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---|print|NMAX|absorb))" % re.escape(name),
                  t, re.S | re.M)
    assert m, name
    return m.group(0)


ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(text, n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]

DIFFED = DIFFC = 0
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
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append((name, hits, ok))
    print("    [%s] %-88s hits=%d" % ("ok" if ok else "DEAD", name, hits))
    if not ok:
        bad("CONTROL-DEAD", name)


def norm(x):
    return tuple(sorted([v for v in x if v > 0], reverse=True))


def step(X):
    r = stepA(list(X))
    if r == "TERMINAL":
        return ()
    if r is None:
        return None
    return norm(r)


def conj(X):
    return tuple(sum(1 for v in X if v >= t) for t in range(1, (X[0] if X else 0) + 1))


def unconj(xi):
    if not xi:
        return ()
    return tuple(sum(1 for z in xi if z >= i) for i in range(1, xi[0] + 1))


def stepC(X):
    if not X:
        return ()
    xi = conj(X)
    d = len(xi)
    if xi[0] - 1 < d:
        return None
    eta = [z - 1 for z in xi]
    while eta and eta[-1] == 0:
        eta.pop()
    out = []
    for t in range(1, len(eta) + 1):
        nxt = eta[t] if t < len(eta) else 0
        out.append(min(nxt, d) + max(eta[t - 1] - d, 0))
    while out and out[-1] == 0:
        out.pop()
    return unconj(tuple(out))


def traj(X):
    global DIFFED, DIFFC
    out = [X]
    cur = X
    for _ in range(400):
        nxt = step(cur)
        alt = stepC(cur)
        DIFFC += 1
        if nxt != alt:
            print("!! stepA vs stepC DISAGREEMENT on %s" % (cur,))
            sys.exit(2)
        if nxt is None:
            return None
        out.append(nxt)
        if nxt == ():
            a, b = runA(list(X)), runB(list(X))
            if a != b:
                print("!! runA vs runB DISAGREEMENT on %s" % (X,))
                sys.exit(2)
            DIFFED += 1
            return out
        cur = nxt
    return None


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


def MX(X):
    return X[0] if X else 0


def diffvec(a, b, L):
    A = list(a) + [0] * (L - len(a))
    B = list(b) + [0] * (L - len(b))
    return tuple(y - x for x, y in zip(A, B))


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


def is_transfer(a, b, L):
    dv = diffvec(b, a, L)
    if dv.count(1) != 1 or dv.count(-1) != 1 or dv.count(0) != L - 2:
        return False
    return dv.index(1) < dv.index(-1)


print("=" * 100)
print("w61 r47d -- LEMMA (INV-STEP), and whether it covers every inversion of every transfer walk")
print("=" * 100)


def analyse(nmax, maxparts, label):
    POP = {}
    nall = 0
    for N in range(1, nmax + 1):
        for p in parts(N):
            if len(p) <= maxparts:
                nall += 1
                t = traj(p)
                if t is not None:
                    POP[p] = t
    POP[()] = [()]
    L = maxparts + 2
    MLEV = nmax + 1
    CAPV = {X: tuple(sum(min(v, m) for v in X) for m in range(MLEV)) for X in POP}
    NEXT = {X: (POP[X][1] if len(POP[X]) > 1 else ()) for X in POP}
    print("\n%s population: %d partitions of N <= %d with <= %d parts ; %d TERMINATE"
          % (label, nall, nmax, maxparts, len(POP) - 1))

    def cle(a, b):
        ca, cb = CAPV[a], CAPV[b]
        return all(ca[m] <= cb[m] for m in range(MLEV))

    # ---------------------------------------------- (1) the inversion states, shape by shape
    BYN = {}
    for p in POP:
        BYN.setdefault(sum(p), []).append(p)
    TE = []
    for N, lst in sorted(BYN.items()):
        for a in lst:
            for b in lst:
                if a != b and dominates(a, b) and is_transfer(a, b, L):
                    TE.append((a, b))
    shapes = Counter()
    aj_hist = Counter()
    inv = 0
    exbad = None
    for (a0, b0) in TE:
        a, b = a0, b0
        for _ in range(60):
            if MX(a) < MX(b):
                inv += 1
                dv = diffvec(a, b, L)
                pos = [i for i, x in enumerate(dv) if x != 0]
                key = tuple((i, dv[i]) for i in pos)
                shapes[key] += 1
                if len(pos) == 2 and dv[pos[0]] == 1 and dv[pos[1]] == 1 and pos[0] == 0:
                    j = pos[1]
                    aj = (a[j] if j < len(a) else 0)
                    aj_hist[aj] += 1
                    if aj != 0 and exbad is None:
                        exbad = (a, b, j, aj)
                else:
                    aj_hist["OTHER-SHAPE"] += 1
                    if exbad is None:
                        exbad = (a, b, None, None)
            na, nb = NEXT[a], NEXT[b]
            if na == () or nb == ():
                break
            a, b = na, nb
    print("    transfer edges %d ; INVERSION STATES %d" % (len(TE), inv))
    print("    inversion shapes (index, increment) : %s" % dict(shapes))
    print("    A_j at the SECOND raised coordinate : %s" % dict(aj_hist))
    print("    ==> every inversion has the (INV-STEP) shape A_j = 0 : %s"
          % (list(aj_hist.keys()) == [0]))
    if list(aj_hist.keys()) != [0]:
        print("    first inversion NOT of that shape : %s" % (exbad,))
    ctrl("%s CONTROL: inversion states exist on transfer walks" % label, inv)

    # ---------------------------------------------- (2) LEMMA (INV-STEP) censused on its own
    # population: every A whose step is legal, B := A with head+1 and a new part 1 appended.
    lt = lv = 0
    for A in POP:
        if A == () or over():
            continue
        B = norm([A[0] + 1] + list(A[1:]) + [1])
        if B not in POP:
            sB = step(B)
        else:
            sB = NEXT[B]
        if sB is None:
            continue
        sA = NEXT[A]
        lt += 1
        M = max(MX(sA), MX(sB)) + 1
        if not all(sum(min(v, m) for v in sA) <= sum(min(v, m) for v in sB) for m in range(M + 1)):
            lv += 1
    print("\n    LEMMA (INV-STEP) censused: %d instances ; VIOLATIONS %d" % (lt, lv))
    if lv:
        bad("INV-STEP", "%d violations on %s" % (lv, label))
    ctrl("%s CONTROL: (INV-STEP) was tested where it could fail" % label, lt)

    # corrupt control: the SAME construction with the second unit landing on a POSITIVE part
    ct = cv = 0
    cex = None
    for A in POP:
        if A == () or over():
            continue
        for j in range(1, len(A)):
            B = norm([A[0] + 1] + [A[i] + (1 if i == j else 0) for i in range(1, len(A))])
            if MX(B) != A[0] + 1:
                continue
            sB = NEXT[B] if B in POP else step(B)
            if sB is None:
                continue
            sA = NEXT[A]
            ct += 1
            M = max(MX(sA), MX(sB)) + 1
            if not all(sum(min(v, m) for v in sA) <= sum(min(v, m) for v in sB)
                       for m in range(M + 1)):
                cv += 1
                if cex is None:
                    cex = (A, B, j)
    print("    CORRUPT CONTROL (second unit on a POSITIVE part, A_j >= 1): %d instances ;"
          " %d FAIL   e.g. %s" % (ct, cv, cex))
    ctrl("%s CORRUPT CONTROL: the hypothesis A_j = 0 is load-bearing -- dropping it breaks <|"
         % label, cv)

    # ---------------------------------------------- (3) the assembled certification
    cert = 0
    thm = ivs = 0
    for (a0, b0) in TE:
        a, b = a0, b0
        ok = True
        for _ in range(60):
            if MX(a) >= MX(b):
                if not cle(a, b):
                    ok = False
                    break
                thm += 1
            else:
                dv = diffvec(a, b, L)
                pos = [i for i, x in enumerate(dv) if x != 0]
                shape_ok = (len(pos) == 2 and pos[0] == 0 and dv[0] == 1 and dv[pos[1]] == 1
                            and (a[pos[1]] if pos[1] < len(a) else 0) == 0)
                if not shape_ok:
                    ok = False
                    break
                ivs += 1
            na, nb = NEXT[a], NEXT[b]
            if na == () or nb == ():
                break
            a, b = na, nb
        cert += ok
    print("\n    ASSEMBLED: transfer edges every step of which is closed by CAP-STEP-MONO (max"
          " order) or by (INV-STEP) (the A_j = 0 shape) : %d of %d" % (cert, len(TE)))
    print("    steps closed by CAP-STEP-MONO %d ; steps closed by (INV-STEP) %d" % (thm, ivs))
    print("    (this is the NARROW hypothesis A_j = 0 that the header of this file states.  It")
    print("     is MY OWN SCOPING DEFECT, caught by this run: the derivation in the header shows")
    print("     the only case that can fail is 1 <= m < A_j, and m = 0 is free by the LEGALITY")
    print("     of B's step, so the correct hypothesis is  rho_{A_j}(A) >= max(A) + 1, which is")
    print("     VACUOUS for A_j <= 1.  The narrow count is printed rather than deleted; block")
    print("     (2b)/(3b) below run the corrected statement.)")
    ctrl("%s CONTROL: (INV-STEP) is doing work CAP-STEP-MONO cannot" % label, ivs)

    # ------------------------------------------ (2b) THE CORRECTED LEMMA, censused on its own
    # (INV-STEP') B = A + e_0 + e_j, and either A_j <= 1, or rho_{A_j}(A) >= max(A)+1.
    def rho(A, t):
        return sum(1 for i, v in enumerate(A) if i >= 1 and v >= t)

    def hyp(A, j):
        aj = A[j] if j < len(A) else 0
        if aj <= 1:
            return True
        return rho(A, aj) >= A[0] + 1

    bt = bv = 0
    bex = None
    for A in POP:
        if A == () or over():
            continue
        for j in range(1, len(A) + 1):
            base = list(A) + [0]
            if j >= len(base):
                continue
            cand = list(base)
            cand[0] += 1
            cand[j] += 1
            B = norm(cand)
            if sorted(cand, reverse=True) != cand:
                continue                      # not a sorted-coordinate raise
            if MX(B) != A[0] + 1 or not hyp(A, j):
                continue
            sB = NEXT[B] if B in POP else step(B)
            if sB is None:
                continue
            sA = NEXT[A]
            bt += 1
            M = max(MX(sA), MX(sB)) + 1
            if not all(sum(min(v, m) for v in sA) <= sum(min(v, m) for v in sB)
                       for m in range(M + 1)):
                bv += 1
                if bex is None:
                    bex = (A, B, j)
    print("\n    (2b) LEMMA (INV-STEP') with the CORRECT hypothesis rho_{A_j}(A) >= max(A)+1")
    print("         (vacuous when A_j <= 1): %d instances ; VIOLATIONS %d   %s" % (bt, bv, bex))
    if bv:
        bad("INV-STEP-PRIME", "%d violations on %s" % (bv, label))
    ctrl("%s CONTROL: (INV-STEP') was tested where it could fail" % label, bt)

    # corrupt control: the same construction with the hypothesis DROPPED
    dt = dv2 = 0
    dex = None
    for A in POP:
        if A == () or over():
            continue
        for j in range(1, len(A) + 1):
            base = list(A) + [0]
            if j >= len(base):
                continue
            cand = list(base)
            cand[0] += 1
            cand[j] += 1
            if sorted(cand, reverse=True) != cand:
                continue
            B = norm(cand)
            if MX(B) != A[0] + 1 or hyp(A, j):
                continue
            sB = NEXT[B] if B in POP else step(B)
            if sB is None:
                continue
            sA = NEXT[A]
            dt += 1
            M = max(MX(sA), MX(sB)) + 1
            if not all(sum(min(v, m) for v in sA) <= sum(min(v, m) for v in sB)
                       for m in range(M + 1)):
                dv2 += 1
                if dex is None:
                    dex = (A, B, j)
    print("    CORRUPT CONTROL: the SAME shape with the hypothesis FAILING: %d instances ;"
          " %d break <|   e.g. %s" % (dt, dv2, dex))
    ctrl("%s CORRUPT CONTROL: rho_{A_j}(A) >= max(A)+1 is load-bearing" % label, dv2)

    # ------------------------------------------ (3b) THE CORRECTED ASSEMBLY
    cert2 = 0
    thm2 = ivs2 = 0
    uncov = []
    for (a0, b0) in TE:
        a, b = a0, b0
        ok = True
        for _ in range(60):
            if MX(a) >= MX(b):
                if not cle(a, b):
                    ok = False
                    break
                thm2 += 1
            else:
                dv = diffvec(a, b, L)
                pos = [i for i, x in enumerate(dv) if x != 0]
                good = (len(pos) == 2 and pos[0] == 0 and dv[0] == 1 and dv[pos[1]] == 1
                        and hyp(a, pos[1]))
                if not good:
                    ok = False
                    uncov.append((a0, b0, a, b))
                    break
                ivs2 += 1
            na, nb = NEXT[a], NEXT[b]
            if na == () or nb == ():
                break
            a, b = na, nb
        cert2 += ok
    print("\n    (3b) ASSEMBLED with the CORRECT hypothesis: transfer edges every step of which")
    print("         is closed by CAP-STEP-MONO or by (INV-STEP') : %d of %d" % (cert2, len(TE)))
    print("         steps by CAP-STEP-MONO %d ; steps by (INV-STEP') %d ; uncovered edges %d"
          % (thm2, ivs2, len(TE) - cert2))
    if uncov:
        print("         first uncovered state : edge %s -> %s at %s vs %s" % uncov[0])
    ctrl("%s CONTROL: (INV-STEP') carries inversion steps" % label, ivs2)
    return len(TE), inv, cert2


a16 = analyse(16, 10, "[N<=16]")
a20 = analyse(20, 12, "[N<=20]")

print("\n" + "=" * 100)
print("N<=16 : %d transfer edges, %d inversions, %d certified by the two lemmas" % a16)
print("N<=20 : %d transfer edges, %d inversions, %d certified by the two lemmas" % a20)
el = time.time() - T0
print("ELAPSED %.2f s / %.0f s ; PARTIAL=%s ; runA/runB diffed %d ; stepA/stepC diffed %d"
      % (el, LIMIT, PARTIAL, DIFFED, DIFFC))
good = sum(1 for _, _, ok in CTRL if ok)
print("CONTROLS %d/%d firing ; DEFECTS %d" % (good, len(CTRL), len(FAIL)))
for f in FAIL:
    print("   DEFECT: %s" % f)
print("EXIT=%d   (script's own FLAG line; the process exit code is 0)"
      % (1 if (FAIL or PARTIAL) else 0))
sys.exit(0)
