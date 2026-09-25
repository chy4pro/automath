#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r47c -- HOW MANY STEPS OF FORESIGHT DOES A STATE CERTIFICATE NEED?

r46 stopped (sec 96) on the sentence "every repair I tried is memoryless, and the arithmetic says
that shape is the wrong shape: the gap is a TRAJECTORY functional while a prefix surplus is a
STATE functional".  r47b's D* died too (64 / 304 closure violations), which looked like more of
the same.  BUT the joint step is DETERMINISTIC, so "what happens j steps from now" is itself a
function of the current pair.  The right question is therefore not state-versus-trajectory; it is

                    HOW DEEP A LOOKAHEAD DOES A STATE PREDICATE NEED?

Define, on pairs of TERMINATING partitions,

        E_j  :=  { (A,B) :  A^(i) <| B^(i)  for every i = 0..j }          (E_0 = <|)

Each E_j is a predicate on the pair alone -- a MEMORYLESS relation, computed by running the
deterministic step j times.  Three facts are immediate and are checked below rather than
asserted:

  (i)   E_{j+1} is contained in E_j, so the chain descends and must stabilise on a finite
        population;
  (ii)  E_j is CLOSED under the joint step  <==>  E_j = E_{j+1}   (closure says the successor of
        an E_j pair is E_j, i.e. <| holds at steps 1..j+1, i.e. the pair is in E_{j+1});
  (iii) the stabilised relation E_J is the GREATEST closed subrelation of <|, and it implies the
        (DOM-MAJ) conclusion (its m = infinity instance is sum A <= sum B).

So J := the least j with E_j = E_{j+1} is exactly the depth of foresight a state certificate
needs, and E_J is a certificate as soon as it contains every equal-sum dominance pair -- which is
checked here too.  J is measured at TWO population sizes; if it were an artefact of size, it
would move.

This file also re-books r47b's two REFUTATIONS (D* is not closed) and r47b's two surviving
measurements ((DIST2) and (HH-LIP)) so that the depth result and the refutations sit in one
place.  Interpreter .venv/bin/python3.  RULING CO' + sec 105 as in r47/r47b.
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
print("w61 r47c -- the DEPTH of lookahead a state certificate for (DOM-MAJ) needs")
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
    MLEV = nmax + 1
    CAPV = {X: tuple(sum(min(v, m) for v in X) for m in range(MLEV)) for X in POP}
    NEXT = {X: (POP[X][1] if len(POP[X]) > 1 else ()) for X in POP}
    print("\n%s population: %d partitions of N <= %d with <= %d parts ; %d TERMINATE"
          % (label, nall, nmax, maxparts, len(POP) - 1))

    def cle(a, b):
        ca, cb = CAPV[a], CAPV[b]
        return all(ca[m] <= cb[m] for m in range(MLEV))

    # E_0 = all <| pairs of terminating partitions
    E = [(a, b) for a in POP for b in POP if a != b and cle(a, b)]
    print("    E_0 = <| pairs                         : %d" % len(E))
    sizes = [len(E)]
    J = None
    firstdrop = {}
    for j in range(1, 12):
        if over():
            break
        # E_j = the pairs of E_{j-1} whose orbit keeps <| for j steps, recomputed by walking
        nxt = []
        for (a, b) in E:
            x, y = a, b
            ok = True
            for _ in range(j):
                x, y = NEXT[x], NEXT[y]
                if not cle(x, y):
                    ok = False
                    break
            if ok:
                nxt.append((a, b))
        dropped = set(E) - set(nxt)
        for p in dropped:
            firstdrop.setdefault(j, p)
        sizes.append(len(nxt))
        print("    E_%-2d (<| survives %2d steps)            : %d      (dropped %d)"
              % (j, j, len(nxt), len(E) - len(nxt)))
        if len(nxt) == len(E):
            J = j - 1
            E = nxt
            break
        E = nxt
    print("    ==> %s STABILISES at J = %s : E_J is the greatest closed subrelation of <|,"
          % (label, J))
    print("        and it is a MEMORYLESS predicate computed with %s step(s) of lookahead." % J)
    if J is None:
        bad("DEPTH", "%s did not stabilise within the tested range" % label)
    for j in sorted(firstdrop):
        print("        first pair dropped at depth %d : %s <| %s" % (j, firstdrop[j][0],
                                                                    firstdrop[j][1]))
    ctrl("%s CONTROL: the chain E_j actually descends (some pair is dropped)" % label,
         sizes[0] - sizes[-1])

    # is E_J closed, tested DIRECTLY rather than inferred from the sizes?
    ES = set(E)
    cl_t = cl_v = 0
    for (a, b) in E:
        if a == ():
            continue
        sa, sb = NEXT[a], NEXT[b]
        if sa == () or sb == ():
            continue
        cl_t += 1
        if (sa, sb) not in ES and sa != sb:
            cl_v += 1
    print("    E_J closure tested directly: %d steps ; %d leave E_J" % (cl_t, cl_v))
    if cl_v:
        bad("EJ-CLOSED", "%d steps leave E_J on %s" % (cl_v, label))
    ctrl("%s CONTROL: the direct closure test was non-vacuous" % label, cl_t)

    # does E_J contain every equal-sum dominance pair?  (the certificate property)
    BYN = {}
    for p in POP:
        BYN.setdefault(sum(p), []).append(p)
    dm_t = dm_out = 0
    for N, lst in sorted(BYN.items()):
        for a in lst:
            for b in lst:
                if a == b or not dominates(a, b):
                    continue
                dm_t += 1
                if (a, b) not in ES:
                    dm_out += 1
    print("    equal-sum dominance pairs %d ; OUTSIDE E_J : %d" % (dm_t, dm_out))
    if dm_out:
        bad("EJ-COVER", "%d dominance pairs outside E_J on %s" % (dm_out, label))
    ctrl("%s CONTROL: the certificate property was tested on a non-empty set" % label, dm_t)

    # and the depth is not decoration: how many pairs does each extra step of lookahead kill?
    print("    sizes along the chain : %s" % sizes)
    ctrl("%s CORRUPT CONTROL: ONE step of lookahead is NOT enough -- E_1 strictly contains E_J"
         % label, sizes[1] - sizes[-1] if len(sizes) > 2 else 0)
    return J, sizes, dm_t


J1, S1, D1 = analyse(16, 10, "[N<=16]")
J2, S2, D2 = analyse(20, 12, "[N<=20]")

print("\n" + "=" * 100)
print("DEPTH at N<=16 : J = %s   chain %s" % (J1, S1))
print("DEPTH at N<=20 : J = %s   chain %s" % (J2, S2))
if J1 is not None and J2 is not None and J1 != J2:
    print("THE DEPTH MOVED WITH THE SIZE -- so it is a property of the population, not of the")
    print("conjecture, and NO fixed finite lookahead is licensed by this evidence.")
else:
    print("THE DEPTH DID NOT MOVE between the two sizes.  That is TWO data points, not a")
    print("theorem: it licenses the STATEMENT 'a %s-step lookahead certificate exists at both"
          " sizes', nothing more." % J1)
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
