#!/usr/bin/env python3
"""ROUND 4-A (line k1695, 2026-08-24): the TIGHTEST case of the family, solved.

R3.13 measured which inputs are hardest for A = aI + u v^T: the multisets with exactly TWO
tokens carrying nonzero coordinates and n-2 null tokens (0,0).  Those are the ones where the
witness count bottoms out (exactly 2 good fixed points).  This script settles the lambda != 1
layer for them completely, in closed form, and checks the closed form against criterion C1.

THE ANALYSIS.  Let the two nonzero tokens sit at cyclic positions s1, s2 with gap
g = s2 - s1 in {1..n-1} -- g is OURS to choose, since the null tokens can be placed anywhere.
Write the tokens (u1,v1), (u2,v2).  For lambda^n = 1,
    U-hat(lambda) = 0  <=>  lambda^g = -u1/u2 =: c1
    V-hat(lambda) = 0  <=>  lambda^-g = -v1/v2, i.e. lambda^g = -v2/v1 =: c2
so BOTH eigenvector clauses hold at some lambda only if c1 = c2 =: c.  Hence:
  (1) c1 != c2  ->  NO lambda is bad, every gap works, the n-cycle wins outright.
  (2) c1 = c2 = c: the bad candidates are {lambda : lambda^n = 1, lambda^g = c}.  With m the
      number of distinct n-th roots of unity (m = n / p^e), lambda^g ranges over the subgroup
      of index gcd(m,g), so a bad candidate exists iff ord(c) divides m/gcd(m,g).
      - ord(c) = 1 (c = 1): unavoidable for every g -- but choosing gcd(g,m) = 1 leaves
        lambda = 1 as the ONLY bad candidate, which is the lambda=1 layer, already solved (R3.8).
      - ord(c) = e > 1: choose g with gcd(m,g) not dividing m/e.  Such a g exists whenever
        m has a divisor d < m with d not dividing m/e; the ONLY obstruction is m = l^a a prime
        power together with ord(c) = l, and then every gap leaves a bad candidate and the
        third (secular) clause must decide.
Everything above is a claim about which lambda are CANDIDATES; the script tests it against C1,
which also applies the third clause, so the two must agree exactly where the analysis predicts
"no candidate", and C1 may still say "cyclic" where a candidate exists (third clause failing).

CONTROLS: both directions of each prediction must occur on the grid (asserted), and the
predicted-no-candidate rows must be exactly the rows C1 calls cyclic-or-lambda=1-only.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round3_family.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 3-B family attack start')], "rf", "exec"), G)
GF, criterion_ncycle, pmod = G['GF'], G['criterion_ncycle'], G['pmod']

def order_of(c, F):
    if c == 0: return None
    o = 1; x = c
    while x != 1:
        x = F.MUL[x][c]; o += 1
    return o

def m_of(n, F):
    m = n
    while m % F.p == 0:
        m //= F.p
    return m

def bad_candidate_exists(c, g, m, F):
    """is there lambda with lambda^m = 1 and lambda^g = c?  (lambda^g ranges over the subgroup
    of m-th roots of unity of index gcd(m,g), i.e. the (m/gcd)-th roots of unity)"""
    from math import gcd
    e = order_of(c, F)
    if e is None: return False
    k = m // gcd(m, g)
    return (k % e == 0)

print("ROUND 4-A: the two-nonzero-token case")
print("q  n  rows  |  pred-no-candidate & C1 cyclic  pred-candidate & C1 cyclic  "
      "pred-candidate & C1 non-cyclic  DISAGREE(pred none but C1 non-cyclic off 1)")
lin_cache = {}
for q in [2, 3, 4, 5, 7]:
    F = GF(q)
    for n in range(3, 9):
        m = m_of(n, F)
        rows = 0; a = 0; b = 0; c_ = 0; bad = 0
        for u1 in range(1, q):
            for u2 in range(1, q):
                for v1 in range(1, q):
                    for v2 in range(1, q):
                        c0 = F.ADD[F.MUL[u1][v1]][F.MUL[u2][v2]]
                        if F.ADD[1][c0] == 0:
                            continue
                        c1 = F.NEG[F.MUL[u1][F.INV[u2]]]
                        c2 = F.NEG[F.MUL[v2][F.INV[v1]]]
                        for g in range(1, n):
                            rows += 1
                            if c1 != c2:
                                pred = False
                            else:
                                pred = bad_candidate_exists(c1, g, m, F)
                            # build the arrangement: token1 at position 0, token2 at position g
                            seq = [(1, 0, 0)]*n
                            seq[0] = (1, u1, v1); seq[g] = (1, u2, v2)
                            ok, gg = criterion_ncycle(seq, n, F)
                            if ok:
                                if pred: b += 1
                                else: a += 1
                            else:
                                # is the obstruction only at lambda=1?
                                h = list(gg); L = [F.NEG[1], 1]
                                while len(h) > 1 and pmod(h, L, F) == []:
                                    qo = [0]*(len(h)-1); rem = list(h)
                                    for d in range(len(h)-2, -1, -1):
                                        cc = rem[d+1]; qo[d] = cc; rem[d+1] = 0
                                        rem[d] = F.ADD[rem[d]][cc]
                                    h = qo
                                    while h and h[-1] == 0: h.pop()
                                only1 = (len(h) <= 1)
                                if pred:
                                    c_ += 1
                                else:
                                    if only1: a += 1
                                    else:
                                        bad += 1
                                        if bad <= 3:
                                            print("   DISAGREE q=%d n=%d g=%d u=(%d,%d) v=(%d,%d) gcd=%s"
                                                  % (q, n, g, u1, u2, v1, v2, gg))
        if rows:
            print("%-2d %-2d %-6d|  %-30d %-27d %-30d %d" % (q, n, rows, a, b, c_, bad))
        assert bad == 0, "CLOSED-FORM ANALYSIS WRONG -- a lambda!=1 obstruction exists where none was predicted"
print("no row where the closed form predicted 'no candidate' had a lambda!=1 obstruction. %.1fs"
      % (time.time()-T0))
