#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r47b -- THE CANDIDATE CERTIFICATE.

w61_r47_transfer.py reduced (DOM-MAJ) on this population from 572 open dominance pairs to
88 open TRANSFER EDGES, and measured that the 88 open edges are UNIFORM: each carries exactly
one inversion state, and at every one of them

        delta = max B - max A = 1,   g = sum B - sum A = 2,   slack g - 2 delta = 0,

with the L1 distance between the two states never exceeding 2 anywhere on those walks.  So the
open half of (DOM-MAJ) is not a spread-out residue at all: it is ONE configuration, sitting at
exactly the minimum gap that (STEP-GAP) permits.

That suggests a memoryless relation r46 did not try, because r46 never had the distance bound:

    D*  :=  { (A,B) :  A <| B ,  dist(A,B) <= 2 ,  sum B - sum A >= 2 (max B - max A) }

  * D* contains every transfer edge (dist 2, equal sums, A >= B in dominance so max A >= max B);
  * D* implies the (DOM-MAJ) conclusion sum A <= sum B (it is the m = infinity instance of <|);
  * so if D* is CLOSED under the joint step it is a CERTIFICATE for the transfer edges, and
    then -- by r47's connectivity census (2683/2683 dominance pairs chain-joined inside the
    terminating set) and transitivity of dominance on the mu's -- a certificate for ALL of
    (DOM-MAJ) on the population.

r46 refuted <| alone (1216 closure violations) and <| ^ (C2) (513).  (C2) is the third conjunct
here; the second, dist <= 2, is the new one.  Both corrupt controls below drop one conjunct and
must therefore FAIL, or the conjunct is decoration.

This file reports what it measures, including 0, and it re-runs the whole closure test on a
LARGER population (N <= 20) so that a clean result at N <= 16 cannot be an artefact of the size
that produced it (doctrine sec 111).

RULING CO': stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py.  sec 105: stepC, an
independent conjugate-coordinate implementation, is diffed against stepA on every step of every
trajectory in both populations.  No SAT, no solver.  Interpreter .venv/bin/python3.
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
    print("    [%s] %-90s hits=%d" % ("ok" if ok else "DEAD", name, hits))
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
            print("!! stepA vs stepC DISAGREEMENT on %s : %s %s" % (cur, nxt, alt))
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


def dist(a, b):
    n = max(len(a), len(b))
    A = list(a) + [0] * (n - len(a))
    B = list(b) + [0] * (n - len(b))
    return sum(abs(x - y) for x, y in zip(A, B))


def diffvec(a, b):
    n = max(len(a), len(b))
    A = list(a) + [0] * (n - len(a))
    B = list(b) + [0] * (n - len(b))
    return tuple(y - x for x, y in zip(A, B))


def shape(a, b):
    dv = [x for x in diffvec(a, b) if x != 0]
    if not dv:
        return "EQ"
    dvf = diffvec(a, b)
    pos = [i for i, x in enumerate(dvf) if x > 0]
    neg = [i for i, x in enumerate(dvf) if x < 0]
    if len(pos) == 1 and len(neg) == 1 and dvf[pos[0]] == 1 and dvf[neg[0]] == -1:
        return "TR" if neg[0] < pos[0] else "TR-ANOMALY"
    if not neg and len(pos) == 2 and all(dvf[i] == 1 for i in pos):
        return "TWO@%d,%d" % (pos[0], pos[1])
    if not neg and len(pos) == 1 and dvf[pos[0]] == 2:
        return "DBL@%d" % pos[0]
    return "OTHER"


def build(nmax, maxparts):
    P, A = {}, 0
    for N in range(1, nmax + 1):
        for p in parts(N):
            if len(p) <= maxparts:
                A += 1
                t = traj(p)
                if t is not None:
                    P[p] = t
    P[()] = [()]
    return P, A


def is_transfer(a, b):
    dv = diffvec(b, a)          # a - b, padded
    n = len(dv)
    if dv.count(1) != 1 or dv.count(-1) != 1 or dv.count(0) != n - 2:
        return False
    return dv.index(1) < dv.index(-1)


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


print("=" * 106)
print("w61 r47b -- the candidate CERTIFICATE  D* = <| ^ dist<=2 ^ (C2), and its closure")
print("=" * 106)


def analyse(nmax, maxparts, label, deep):
    global DIFFED, DIFFC
    POP, nall = build(nmax, maxparts)
    MLEV = nmax + 1
    CAPV = {X: tuple(sum(min(v, m) for v in X) for m in range(MLEV)) for X in POP}
    NEXT = {X: (POP[X][1] if len(POP[X]) > 1 else ()) for X in POP}
    PAD = {X: tuple(X) + (0,) * (maxparts - len(X)) for X in POP}

    def dst(a, b):
        return sum(abs(x - y) for x, y in zip(PAD[a], PAD[b]))

    def cle(a, b):
        ca, cb = CAPV[a], CAPV[b]
        return all(ca[m] <= cb[m] for m in range(MLEV))

    def C2(a, b):
        return (sum(b) - sum(a)) >= 2 * (MX(b) - MX(a))

    print("\n%s population: %d partitions of N <= %d with <= %d parts ; %d TERMINATE"
          % (label, nall, nmax, maxparts, len(POP) - 1))

    # ---- the three relations
    def R_cle(a, b):
        return cle(a, b)

    def R_cle_c2(a, b):
        return cle(a, b) and C2(a, b)

    def R_cle_d2(a, b):
        return cle(a, b) and dst(a, b) <= 2

    def R_star(a, b):
        return cle(a, b) and dst(a, b) <= 2 and C2(a, b)

    def closure(pred, name):
        t = v = 0
        ex = None
        for a in POP:
            if over():
                break
            if a == ():
                continue
            sa = NEXT[a]
            for b in POP:
                if b == () or not pred(a, b):
                    continue
                t += 1
                sb = NEXT[b]
                if not pred(sa, sb):
                    v += 1
                    if ex is None or (sum(a) + sum(b)) < (sum(ex[0]) + sum(ex[1])):
                        ex = (a, b, sa, sb)
        print("    %-34s pairs %7d ; CLOSURE VIOLATIONS %6d   smallest %s"
              % (name, t, v, ex))
        return t, v

    t0, v0 = closure(R_cle, "<| alone")
    t1, v1 = closure(R_cle_c2, "<| ^ (C2)")
    t2, v2 = closure(R_cle_d2, "<| ^ dist<=2")
    t3, v3 = closure(R_star, "D* = <| ^ dist<=2 ^ (C2)")
    ctrl("%s CORRUPT CONTROL: dropping dist<=2 breaks closure, so it is load-bearing" % label, v1)
    ctrl("%s CORRUPT CONTROL: dropping (C2) breaks closure, so it is load-bearing" % label, v2)
    ctrl("%s CONTROL: D* is non-empty on this population" % label, t3)
    print("    ==> D* closure violations on %s : %d" % (label, v3))

    # ---- does D* contain every transfer edge?
    TE = []
    BYN = {}
    for p in POP:
        BYN.setdefault(sum(p), []).append(p)
    for N, lst in sorted(BYN.items()):
        for a in lst:
            for b in lst:
                if a != b and dominates(a, b) and is_transfer(a, b):
                    TE.append((a, b))
    miss = sum(1 for (a, b) in TE if not R_star(a, b))
    print("    transfer edges inside the terminating set : %d ; NOT in D* : %d" % (len(TE), miss))
    if miss:
        bad("D*-COVER", "%d transfer edges are outside D*" % miss)
    ctrl("%s CONTROL: the transfer-edge population is non-empty" % label, len(TE))

    if not deep:
        return v3

    # ---- shapes along the transfer walks
    print("\n    SHAPES of the padded difference B^(k) - A^(k) along all %d transfer walks:"
          % len(TE))
    sh = Counter()
    dmax = 0
    ginv = Counter()
    for (a0, b0) in TE:
        a, b = a0, b0
        for _ in range(60):
            sh[shape(a, b)] += 1
            dmax = max(dmax, dst(a, b))
            if MX(a) < MX(b):
                ginv[(MX(b) - MX(a), sum(b) - sum(a))] += 1
            na, nb = NEXT[a], NEXT[b]
            if na == () or nb == ():
                break
            a, b = na, nb
    print("    %s" % dict(sh))
    print("    max L1 distance anywhere on a transfer walk : %d" % dmax)
    print("    (delta, g) at inversion states of transfer walks : %s" % dict(ginv))
    if dmax > 2:
        bad("DIST2", "L1 distance %d > 2 on a transfer walk" % dmax)
    ctrl("%s CONTROL: transfer walks were actually walked" % label, sum(sh.values()))

    # ---- (HH-LIP): does one step ever push dist above 2 from inside D*?
    lip_t = lip_v = 0
    lex = None
    for a in POP:
        if over():
            break
        if a == ():
            continue
        sa = NEXT[a]
        for b in POP:
            if b == () or not R_star(a, b):
                continue
            lip_t += 1
            sb = NEXT[b]
            if dst(sa, sb) > 2:
                lip_v += 1
                if lex is None:
                    lex = (a, b, sa, sb)
    print("\n    (HH-LIP) from inside D*, dist(hh a, hh b) <= 2 : %d instances, %d violations %s"
          % (lip_t, lip_v, lex))
    ctrl("%s CONTROL: (HH-LIP) was tested on a non-empty set" % label, lip_t)

    # ---- THE ASSEMBLED INDUCTION, run as a certification and counted
    print("\n    THE ASSEMBLED ARGUMENT, executed as a certification of every transfer edge:")
    print("    invariant D*; at each state either max A >= max B (CAP-STEP-MONO closes the step)")
    print("    or the state is an inversion, and then D* must carry it.  Count what each does.")
    cert_ok = cert_bad = 0
    by_thm = by_inv = 0
    for (a0, b0) in TE:
        a, b = a0, b0
        ok = True
        for _ in range(60):
            if not R_star(a, b):
                ok = False
                break
            if MX(a) >= MX(b):
                by_thm += 1
            else:
                by_inv += 1
            na, nb = NEXT[a], NEXT[b]
            if na == () or nb == ():
                if not cle(na, nb):
                    ok = False
                break
            a, b = na, nb
        cert_ok += ok
        cert_bad += (not ok)
    print("    transfer edges certified end-to-end by D* : %d of %d   (failures %d)"
          % (cert_ok, len(TE), cert_bad))
    print("    steps closed by CAP-STEP-MONO (max A >= max B) : %d" % by_thm)
    print("    steps closed only by the D* invariant (inversions) : %d" % by_inv)
    if cert_bad:
        bad("CERT", "%d transfer edges not certified" % cert_bad)
    ctrl("%s CONTROL: the inversion branch is actually exercised, so D* is doing work"
         " CAP-STEP-MONO cannot" % label, by_inv)

    # ---- and then the whole conjecture, through the reduction only
    print("\n    (DOM-MAJ) re-derived through the reduction ONLY: chain each dominance pair down")
    print("    transfer edges and compose.  Any failure here breaks the reduction, not the data.")
    down = {}
    for (a, b) in TE:
        down.setdefault(a, []).append(b)
    dm_t = dm_bad = 0
    for N, lst in sorted(BYN.items()):
        if over():
            break
        reach = {}
        for a in lst:
            s = set()
            st = [a]
            while st:
                u = st.pop()
                for v in down.get(u, ()):
                    if v not in s:
                        s.add(v)
                        st.append(v)
            reach[a] = s
        for a in lst:
            for b in lst:
                if a == b or not dominates(a, b):
                    continue
                dm_t += 1
                if b not in reach[a]:
                    dm_bad += 1
    print("    dominance pairs %d ; NOT reachable by a chain of certified transfer edges : %d"
          % (dm_t, dm_bad))
    if dm_bad:
        bad("REDUCTION", "%d dominance pairs not chain-joined" % dm_bad)
    ctrl("%s CONTROL: the reduction was exercised on a non-empty set" % label, dm_t)
    return v3


v_small = analyse(16, 10, "[N<=16]", True)
print("\n" + "-" * 106)
print("SECOND POPULATION -- the same closure test at a LARGER size, so that a clean result at")
print("N <= 16 cannot be an artefact of the size that produced it (doctrine sec 111).")
v_big = analyse(20, 12, "[N<=20]", True)

print("\n" + "=" * 106)
el = time.time() - T0
print("ELAPSED %.2f s / %.0f s internal limit ; PARTIAL=%s ; runA/runB diffed %d ;"
      " stepA/stepC diffed %d" % (el, LIMIT, PARTIAL, DIFFED, DIFFC))
good = sum(1 for _, _, ok in CTRL if ok)
print("CONTROLS %d/%d firing ; DEFECTS %d" % (good, len(CTRL), len(FAIL)))
for f in FAIL:
    print("   DEFECT: %s" % f)
print("D* closure violations : N<=16 -> %s ; N<=20 -> %s" % (v_small, v_big))
print("EXIT=%d   (script's own FLAG line; the process exit code is 0)"
      % (1 if (FAIL or PARTIAL) else 0))
sys.exit(0)
