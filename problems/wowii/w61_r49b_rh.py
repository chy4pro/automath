#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r49 ITEM B -- (PIVOT-MAJ) and (RH) are COROLLARIES of r48's proved (DOM-MAJ).

r48 (ledger sec 7.63) proved (DOM-MAJ).  r45 sec 7.60 (g) had MEASURED (PIVOT-MAJ) and
(DOM-MAJ) to be equivalent; r48's own ledger line records (PIVOT-MAJ) as "not re-run" and
lists (RH) as UNTOUCHED.  This file draws the deduction that was left on the table and
RUNS it (sec 81: no load-bearing assertion before its run).

------------------------------------------------------------------------------------------
> COROLLARY PIVOT-MAJ.  Let pi be graphic and pi' = pi - e_i + e_j with pi_i >= pi_j + 2.
> Then p(pi) >= p(pi') in dominance, where p(X) is the Havel-Hakimi pivot sequence.
>
> Proof.  (pi, pi') is ONE transfer edge: equal sums, equal length, one unit moved DOWN.
> In the language of sec 7.63 (c) it is a (T) state, and R := (EQ) u (T) u (U){...}
> contains every (T) state with no side condition.  THEOREM R-CLOSED (r48, PROVED) says R
> is closed under the joint HH step whenever both steps are legal -- which they are, pi
> being graphic and pi' being graphic by DOWN-SET (= Ruch-Gutman 1979, CITED not claimed;
> so r43's hypothesis "pi' also terminating" is REDUNDANT, and that redundancy is measured
> below).  Every R state satisfies sum A <= sum B, so sum pi^(k) <= sum pi'^(k) for every
> k.  By (PIV-SUM)/(MU) the k-th prefix sum of p(X) is (sum X - sum X^(k))/2, so the prefix
> sums of p(pi) dominate those of p(pi'), i.e. p(pi) >= p(pi').  QED
>
> NOTE ON WHAT THE PROOF USES.  Only the SINGLE-EDGE case of r48 is used: NOT (CHAIN), and
> therefore not Ruch-Gutman except for the (redundant) graphicness of pi'.

> COROLLARY RH.  With pi, pi' as above, s(pi) <= s(pi'), equivalently residue(pi') <=
> residue(pi) -- the statement (RH).
>
> Proof.  p(pi) and p(pi') are partitions of the same integer sum(pi)/2 ((PIV-SUM)).  For
> partitions of one integer a >= b implies a* <= b* (conjugation reverses dominance), and
> a*_1 = #parts(a); so #parts p(pi) <= #parts p(pi'), i.e. s(pi) <= s(pi').  pi and pi'
> have the same length n and residue = n - s, so residue(pi') <= residue(pi).  QED

WHAT IS NOT CLAIMED.  (DOM-MAJ) is NOT novelty-cleared (planner ruling
cert_w61_r48_litcheck.md sec 4), so nothing here goes outward as new.  (RH)'s own S1 lookup
(sec 7.55 b) returned NOT FOUND with a named gap (Triesch 1996, paywalled, unverified).
Block [4] measures EXACTLY how much of (MON)'s even half this closes and how much it does
not: (RH) gives f(U) <= f(T), it does NOT give (MON)'s upper half f(T) - f(U) <= 1.

RULING 105: this file shares NO LINE with w61_r29_c1audit.py or w61_r43_gap.py.  The HH
walk is Counter-based and written here; graphicness is cross-checked by Erdos-Gallai;
dominance and conjugation are written here.  No SAT, no solver, no exhaustive search.
Interpreter: .venv/bin/python3 (pure Python; no sympy, no networkx).
"""
import sys, time
from collections import Counter

T0 = time.time()
LIMIT = 300.0
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
    print("   [%s] %-76s hits=%d" % ("ok " if ok else "DEAD", name, hits))
    if must_fire and hits == 0:
        bad("DEAD CONTROL", name)


def known(name, got, want):
    tag = "ok " if got == want else "MISMATCH"
    print("   [%s] KNOWN VALUE %-56s got=%s want=%s" % (tag, name, got, want))
    if got != want:
        bad("KNOWN VALUE MISMATCH", "%s got=%s want=%s" % (name, got, want))


# ------------------------------------------------------------------ independent HH walk
def hh_walk(seq):
    """Counter-based Havel-Hakimi.  Returns (pivot tuple, steps, residue) or None if the
    sequence is NOT graphic.  Written here; shares no line with the r29 list implementation."""
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
        # TWO PASSES.  Choosing and decrementing in ONE pass re-picks the entries the pass
        # has just lowered -- my first version did exactly that and blocks [0] and [3]
        # caught it (10 oracle disagreements, 3 spurious DOWN-SET failures).  Kept as a
        # comment because the defect is disclosed in the ledger, not deleted.
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


def erdos_gallai(seq):
    """independent graphicness oracle."""
    s = sorted((x for x in seq), reverse=True)
    if any(x < 0 for x in s):
        return False
    tot = sum(s)
    if tot % 2:
        return False
    n = len(s)
    for k in range(1, n + 1):
        lhs = sum(s[:k])
        rhs = k * (k - 1) + sum(min(x, k) for x in s[k:])
        if lhs > rhs:
            return False
    return True


def dominates(a, b):
    """a >= b in dominance: prefix sums of a are >= those of b (equal totals assumed)."""
    la, lb = list(a), list(b)
    m = max(len(la), len(lb))
    la = la + [0] * (m - len(la))
    lb = lb + [0] * (m - len(lb))
    pa = pb = 0
    for x, y in zip(la, lb):
        pa += x
        pb += y
        if pa < pb:
            return False
    return True


def conj(a):
    """conjugate partition."""
    if not a:
        return ()
    mx = max(a)
    return tuple(sum(1 for x in a if x >= t) for t in range(1, mx + 1))


def ms(l):
    return tuple(sorted(l, reverse=True))


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


print("=" * 100)
print("w61 r49 ITEM B -- (PIVOT-MAJ) and (RH) as COROLLARIES of the proved (DOM-MAJ)")
print("=" * 100)
print("interpreter: .venv/bin/python3 (pure Python, no sympy, no networkx)")

# ================================================== 0. the two oracles must agree
print("\n[0] TWO INDEPENDENT GRAPHICNESS ORACLES, AGREEMENT FIRST (sec 105).")
ORACLE_N = 6 * 3
agree = disagree = ngraphic = 0
for N in range(1, ORACLE_N + 1):
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
print("    partitions of N<=%d tested : %d ; agreements %d ; DISAGREEMENTS %d"
      % (ORACLE_N, agree + disagree, agree, disagree))
print("    of which graphic           : %d" % ngraphic)
if disagree:
    bad("ORACLES", "%d disagreements" % disagree)
ctrl("CONTROL: the population contains NON-graphic partitions too", agree + disagree - ngraphic)

# ================================================== 1. conjugation reverses dominance
print("\n[1] THE CONJUGATION STEP OF COROLLARY RH, CHECKED AS A STANDALONE FACT:")
print("    for partitions a,b of one integer,  a >= b  ==>  a* <= b*  ==>  #parts(a) <= #parts(b).")
cj_ok = cj_bad = 0
np_ok = np_bad = 0
LOOSE_N = 6 * 2
loose = 0
for N in range(2, 15):
    P = list(parts(N))
    for a in P:
        for b in P:
            if not dominates(a, b):
                continue
            if dominates(conj(b), conj(a)):
                cj_ok += 1
            else:
                cj_bad += 1
            if len(a) <= len(b):
                np_ok += 1
            else:
                np_bad += 1
    if over():
        break
for N in range(2, LOOSE_N + 1):
    P = list(parts(N))
    for a in P:
        for b in P:
            if len(a) <= len(b) and not dominates(a, b):
                loose += 1
print("    dominance pairs tested        : %d ; a* <= b* holds %d, FAILS %d"
      % (cj_ok + cj_bad, cj_ok, cj_bad))
print("    #parts(a) <= #parts(b)        : holds %d, FAILS %d" % (np_ok, np_bad))
print("    fewer-or-equal parts WITHOUT dominance (N<=%d) : %d" % (LOOSE_N, loose))
if cj_bad or np_bad:
    bad("CONJUGATION", "cj_bad=%d np_bad=%d" % (cj_bad, np_bad))
ctrl("CORRUPT CONTROL: fewer parts does NOT imply dominance -- the step is real work", loose)
known("fewer-or-equal parts without dominance (r43's 1458)", loose, 1458)

# ================================================== 2. (PIVOT-MAJ) on r43's P3 and P4
print("\n[2] (PIVOT-MAJ) AND (RH) ON r43's TWO POPULATIONS, RECOMPUTED HERE.")
print("    P3: every partition pi of N in [2,16] that is graphic, every pi' = pi - e_i + e_j")
print("        with pi_i >= pi_j + 2 that is graphic.   P4: the DISJOINT range N in [17,20].")


def sweep(lo, hi):
    pop = 0
    rh_ok = rh_bad = 0
    mj_ok = mj_bad = 0
    rev_rh_bad = rev_mj_bad = 0
    contain_ok = contain_bad = 0
    redundant = 0
    distinct = set()
    ce = []
    for N in range(lo, hi + 1):
        if over():
            break
        for pi in parts(N):
            W = hh_walk(list(pi))
            if W is None:
                continue
            pv, s_pi, r_pi = W
            n = len(pi)
            for i in range(n):
                for j in range(n):
                    if i == j or pi[i] < pi[j] + 2:
                        continue
                    u = list(pi)
                    u[i] -= 1
                    u[j] += 1
                    u = ms(u)
                    if min(u) < 0:
                        continue
                    U = hh_walk(list(u))
                    if U is None:
                        continue
                    redundant += 1
                    pu, s_u, r_u = U
                    pop += 1
                    distinct.add((ms(pi), u))
                    # the (DOM-MAJ) hypothesis: equal sums, comparable, both graphic
                    if (sum(pi) == sum(u) and dominates(ms(pi), u)
                            and erdos_gallai(list(pi)) and erdos_gallai(list(u))):
                        contain_ok += 1
                    else:
                        contain_bad += 1
                    if s_pi <= s_u:
                        rh_ok += 1
                    else:
                        rh_bad += 1
                        if len(ce) < 4:
                            ce.append(("RH", pi, u, s_pi, s_u))
                    if r_u > r_pi:
                        rh_bad += 0
                    if dominates(pv, pu):
                        mj_ok += 1
                    else:
                        mj_bad += 1
                        if len(ce) < 4:
                            ce.append(("MAJ", pi, u, pv, pu))
                    # reversed (RH) is the claim s(pi') <= s(pi); it FAILS where s(pi) < s(pi').
                    # My first version wrote the condition backwards and the r43 known value
                    # 873 caught it (it printed 0).  Repaired by running.
                    if s_pi < s_u:
                        rev_rh_bad += 1
                    if not dominates(pu, pv):
                        rev_mj_bad += 1
    return (pop, rh_ok, rh_bad, mj_ok, mj_bad, rev_rh_bad, rev_mj_bad,
            contain_ok, contain_bad, len(distinct), ce)


for (lo, hi, tag) in ((2, 16, "P3"), (17, 20, "P4"), (21, 23, "P5-HELDOUT")):
    (pop, rh_ok, rh_bad, mj_ok, mj_bad, rrb, rmb, cok, cbad, nd, ce) = sweep(lo, hi)
    print("    %s  N in [%d,%d]" % (tag, lo, hi))
    print("       pairs in population (i,j slots)          : %d   distinct (pi,pi') : %d" % (pop, nd))
    print("       (RH)        s(pi) <= s(pi')              : holds %d, FAILS %d" % (rh_ok, rh_bad))
    print("       (PIVOT-MAJ) p(pi) >= p(pi')              : holds %d, FAILS %d" % (mj_ok, mj_bad))
    print("       EVERY pair meets the (DOM-MAJ) hypothesis: yes %d, no %d" % (cok, cbad))
    print("       CORRUPT reversed (RH)  s(pi') < s(pi)    : fails %d" % rrb)
    print("       CORRUPT reversed maj   p(pi') >= p(pi)   : fails %d" % rmb)
    for z in ce:
        print("       COUNTEREXAMPLE %s" % (z,))
    if rh_bad or mj_bad or cbad:
        bad(tag, "rh_bad=%d mj_bad=%d containment_bad=%d" % (rh_bad, mj_bad, cbad))
    if tag == "P3":
        known("P3 population size (r43's 1324)", pop, 1324)
        known("P3 reversed (RH) failures (r43's 873)", rrb, 873)
        known("P3 reversed majorization failures (r43's 1072)", rmb, 1072)
        ctrl("CORRUPT CONTROL: the reversed (RH) really fails on P3", rrb)
        ctrl("CORRUPT CONTROL: the reversed majorization really fails on P3", rmb)
        ctrl("CONTROL: P3 is non-empty", pop)
    elif tag == "P4":
        known("P4 population size (r43's 5006)", pop, 5006)
        ctrl("CONTROL: P4 (disjoint range) is non-empty", pop)
    else:
        ctrl("CONTROL: P5, a THIRD disjoint range never used by r43, is non-empty (sec 111)", pop)
        ctrl("CORRUPT CONTROL: the reversed majorization fails on P5 too", rmb)

# ============================ 3. is "pi' also graphic" a redundant hypothesis?
print("\n[3] IS r43's HYPOTHESIS 'pi ALSO TERMINATES' REDUNDANT?  DOWN-SET (= Ruch-Gutman")
print("    1979, CITED not claimed) says yes.  Counted here rather than assumed:")
dropped = kept = 0
for N in range(2, 17):
    if over():
        break
    for pi in parts(N):
        if hh_walk(list(pi)) is None:
            continue
        n = len(pi)
        for i in range(n):
            for j in range(n):
                if i == j or pi[i] < pi[j] + 2:
                    continue
                u = ms([pi[t] - (t == i) + (t == j) for t in range(n)])
                if min(u) < 0:
                    continue
                if hh_walk(list(u)) is None:
                    dropped += 1
                else:
                    kept += 1
print("    pi graphic + unit transfer down : pi' graphic %d times, NON-graphic %d times"
      % (kept, dropped))
if dropped:
    bad("DOWN-SET", "%d transfers left the graphic set" % dropped)
up_left = 0
for N in range(2, 15):
    if over():
        break
    for pi in parts(N):
        if hh_walk(list(pi)) is None:
            continue
        n = len(pi)
        for i in range(n):
            for j in range(n):
                if i == j or pi[i] < pi[j] + 2:
                    continue
                # the UPWARD move: take from the small part, give to the large one
                v = ms([pi[t] + (t == i) - (t == j) for t in range(n)])
                if min(v) < 0:
                    continue
                if hh_walk(list(v)) is None:
                    up_left += 1
ctrl("CORRUPT CONTROL: run the SAME move UPWARD and it DOES leave the graphic set", up_left)

# ============================ 4. exactly how much of (MON)'s even half this closes
print("\n[4] WHAT THIS DOES AND DOES NOT GIVE (MON) (item (b)).  (MON) is")
print("    f(T) - f(T+e_i) in {0,1} with f(T) = residue(L(T)).  For sum(T) EVEN the pair")
print("    (L(T), L(T+e_i)) is claimed by r38 [5] to be a unit transfer DOWN.  Item (a):")
print("    checked, not assumed -- how many even-sum instances ACTUALLY satisfy it?")


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
        return None
    W = hh_walk(list(L))
    return None if W is None else W[2]


cov = Counter()
lower_ok = lower_bad = 0
upper_ok = upper_bad = 0
for N in range(1, 15):
    if over():
        break
    for T in parts(N):
        if sum(T) % 2:
            continue
        a = f_of(T)
        if a is None:
            continue
        for i in range(len(T)):
            U = ms([T[t] + (t == i) for t in range(len(T))])
            b = f_of(U)
            if b is None:
                continue
            L, Lp = ms(L_of(T)), ms(L_of(U))
            if len(L) != len(Lp) or sum(L) != sum(Lp):
                cov["not same length/sum"] += 1
            elif dominates(L, Lp) and L != Lp:
                cov["a genuine transfer DOWN -- (RH) applies"] += 1
            elif L == Lp:
                cov["identical lists"] += 1
            else:
                cov["NOT a transfer down -- (RH) does NOT apply"] += 1
            if a - b >= 0:
                lower_ok += 1
            else:
                lower_bad += 1
            if a - b <= 1:
                upper_ok += 1
            else:
                upper_bad += 1
print("    even-sum (MON) instances, coverage by (RH): %s" % dict(sorted(cov.items())))
print("    (MON) LOWER half  f(T) - f(U) >= 0 : holds %d, fails %d   <-- this is what (RH) gives"
      % (lower_ok, lower_bad))
print("    (MON) UPPER half  f(T) - f(U) <= 1 : holds %d, fails %d   <-- NOT given by (RH)"
      % (upper_ok, upper_bad))
ctrl("CONTROL: even-sum (MON) instances that (RH) does NOT cover exist",
     cov.get("NOT a transfer down -- (RH) does NOT apply", 0)
     + cov.get("not same length/sum", 0))

print("\n[5] WHAT IS NOT CLOSED.")
print("    (DOM-MAJ) is NOT novelty-cleared; nothing here is claimed NEW or goes outward.")
print("    (MON)'s UPPER half, (MON)'s ODD half, (S2), C1-W, (PERSIST-NARROW), (GAP1-OK),")
print("    (BAND-EQ), (F2-FREE) are all untouched by this file.  The conjecture is NOT closed.")

print("\n" + "=" * 100)
print("CONTROLS %d, all fired: %s" % (len(CTRL), all(h > 0 for _, h, mf in CTRL if mf)))
print("DEFECTS  %d" % len(FAIL))
for x in FAIL:
    print("   " + x)
print("PARTIAL=%s  elapsed %.2fs  (internal limit %.0fs)" % (PARTIAL, time.time() - T0, LIMIT))
print("=" * 100)
sys.exit(1 if FAIL else 0)
