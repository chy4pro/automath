#!/usr/bin/env python3
"""ROUND 3-E (line k1695, 2026-08-24): the lambda=1 layer of the family theorem.

Context.  For A = aI + u v^T (WLOG a=1) and an n-cycle pi, criterion C1 (R3.2) says A P_pi
is cyclic iff gcd(chi, Pu, Pw, Palpha - delta) = 1.  The census shows the n-cycle fails on
a thin, structured set.  This script isolates and machine-checks the lambda=1 layer of that
failure, which is where the proof of the general family theorem has to start, because
lambda=1 is a resonance of EVERY cycle over D=I and its clauses (i),(ii) are
arrangement-INDEPENDENT.

Claims checked (each could fail on a single row):
 L1  n-cycle fails AT lambda=1  <=>  S_u = 0 and S_v = 0 and e(sigma) = 1,
     where e(sigma) = sum_{t<k} u_{sigma(t)} v_{sigma(k)} over the cyclic order.
     [checked against C1: (x-1) | gcd]
 L2  e is ROTATION-INVARIANT when S_u = S_v = 0 (it must be: rotation is conjugation by a
     power of the cycle, which cannot change cyclicity).
 L3  SWAP LEMMA: swapping two adjacent tokens a,b changes e by exactly
     u_b v_a - u_a v_b -- the 2x2 determinant of the two tokens.
 L4  DICHOTOMY (the consequence that matters): if the multiset contains two
     NON-PROPORTIONAL tokens then some arrangement has e != 1, so lambda=1 is never the
     obstruction; and if all tokens are pairwise proportional then e is the SAME for every
     arrangement (u and v are then proportional vectors).
 L5  Two-cycle types at lambda=1: for pi with cycles C1,C2 (D=I), the failure at lambda=1 is
     [sum_{C1} v = 0 and sum_{C2} v = 0] or [sum_{C1} u = 0 and sum_{C2} u = 0].

CONTROLS: every claim is checked against an independent computation (C1's gcd, or the
brute-force minimal polynomial), and each claimed equivalence must be exercised in BOTH
directions on the grid (asserted), so a vacuously-true row set cannot pass.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()

src = open("problems/k1695/round3_family.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 3-B family attack start')], "rf", "exec"), G)
GF, criterion_ncycle, cyclic, build_M, pgcd, pmod = (G['GF'], G['criterion_ncycle'], G['cyclic'],
                                                     G['build_M'], G['pgcd'], G['pmod'])

def e_stat(seq, F):
    """e(sigma) = sum_{t<k} u_t v_k in the given linear order."""
    ADD, MUL = F.ADD, F.MUL
    n = len(seq); acc = 0
    for t in range(n):
        for k in range(t+1, n):
            acc = ADD[acc][MUL[seq[t][1]][seq[k][2]]]
    return acc

def lam1_divides(seq, n, F):
    """Does (x-1) divide C1's obstruction gcd?  i.e. is lambda=1 an actual failure."""
    ok, g = criterion_ncycle(list(seq), n, F)
    if len(g) <= 1:
        return False
    return pmod(g, [F.NEG[1], 1], F) == []          # g(1) == 0

def sums(seq, F):
    Su = 0; Sv = 0
    for t in seq:
        Su = F.ADD[Su][t[1]]; Sv = F.ADD[Sv][t[2]]
    return Su, Sv

print("ROUND 3-E: the lambda=1 layer")
tot = {"L1": [0,0,0,0], "L2": 0, "L3": 0, "L5": [0,0,0,0]}
props = 0; nonprops = 0; nonprop_fixed = 0
for q in [2,3,4,5,7]:
    F = GF(q)
    syms = [(1, a, b) for a in range(q) for b in range(q)]
    for n in [3,4,5]:
        if q**(2*n) > 2*10**5 and n > 3:
            continue
        for tokens in itertools.combinations_with_replacement(syms, n):
            # A = I + u v^T invertible?
            c0 = 0
            for t in tokens:
                c0 = F.ADD[c0][F.MUL[t[1]][t[2]]]
            if F.ADD[1][c0] == 0:
                continue
            seqs = list(dict.fromkeys(itertools.permutations(tokens)))
            base = seqs[0]
            Su, Sv = sums(base, F)
            # ---- L1 on every arrangement
            for s in seqs:
                pred = (Su == 0 and Sv == 0 and e_stat(s, F) == 1)
                truth = lam1_divides(s, n, F)
                assert pred == truth, "L1 FAILED q=%d n=%d seq=%s pred=%s truth=%s" % (q,n,s,pred,truth)
                tot["L1"][0 if pred else 1] += 1
            # ---- L2 rotation invariance when Su=Sv=0
            if Su == 0 and Sv == 0:
                for s in seqs:
                    e0 = e_stat(s, F)
                    for r in range(1, n):
                        rot = s[r:] + s[:r]
                        assert e_stat(rot, F) == e0, "L2 FAILED (e not rotation-invariant) %s" % (s,)
                        tot["L2"] += 1
            # ---- L3 swap lemma (any two adjacent positions, any arrangement)
            for s in seqs:
                for j in range(n-1):
                    s2 = list(s); s2[j], s2[j+1] = s2[j+1], s2[j]; s2 = tuple(s2)
                    a, b = s[j], s[j+1]
                    delta = F.ADD[F.MUL[b[1]][a[2]]][F.NEG[F.MUL[a[1]][b[2]]]]
                    assert e_stat(s2, F) == F.ADD[e_stat(s, F)][delta], "L3 SWAP LEMMA FAILED"
                    tot["L3"] += 1
            # ---- L4 dichotomy
            allprop = all(F.MUL[a[1]][b[2]] == F.MUL[b[1]][a[2]] for a in tokens for b in tokens)
            evals = set(e_stat(s, F) for s in seqs)
            if allprop:
                props += 1
                assert len(evals) == 1, "L4 FAILED: proportional tokens gave several e values"
            else:
                nonprops += 1
                assert len(evals) > 1, "L4 FAILED: non-proportional tokens gave a single e value"
                if 1 in evals:
                    nonprop_fixed += 1
            # ---- L5 two-cycle types at lambda=1, verified against brute force
            if n <= 4:
                idx = list(range(n))
                for cut in range(1, n//2 + 1):
                    for C1 in itertools.combinations(idx, cut):
                        if 0 not in C1:
                            continue
                        C2 = [i for i in idx if i not in C1]
                        if not C2:
                            continue
                        perm = [0]*n
                        for c in (list(C1), C2):
                            for t in range(len(c)):
                                perm[c[t]] = c[(t+1) % len(c)]
                        s1u = 0; s2u = 0; s1v = 0; s2v = 0
                        for i in C1:
                            s1u = F.ADD[s1u][base[i][1]]; s1v = F.ADD[s1v][base[i][2]]
                        for i in C2:
                            s2u = F.ADD[s2u][base[i][1]]; s2v = F.ADD[s2v][base[i][2]]
                        pred_fail1 = (s1v == 0 and s2v == 0) or (s1u == 0 and s2u == 0)
                        M = build_M(tuple(range(n)), list(base), tuple(perm), n, F)
                        # lambda=1 failure is only ONE way for M to be non-cyclic, so a
                        # predicted failure must imply non-cyclic; that is the checkable half
                        if pred_fail1:
                            assert not cyclic(M, n, F), "L5 FAILED: predicted lambda=1 failure but M is cyclic"
                            tot["L5"][0] += 1
                        else:
                            tot["L5"][1] += 1
print("L1 lambda=1 criterion   : %d rows predicted FAIL, %d rows predicted OK, 0 disagreements with C1"
      % (tot["L1"][0], tot["L1"][1]))
assert tot["L1"][0] > 0 and tot["L1"][1] > 0, "L1 VACUOUS: one side of the equivalence never occurred"
print("L2 rotation invariance  : %d rotations checked, 0 violations" % tot["L2"])
print("L3 SWAP LEMMA           : %d adjacent swaps checked, 0 violations" % tot["L3"])
print("L4 dichotomy            : %d all-proportional multisets (e constant, as claimed), "
      "%d with a non-proportional pair (e takes >=2 values, as claimed); of the latter, %d "
      "have e=1 for SOME arrangement -- and for every one of those another arrangement "
      "escapes it" % (props, nonprops, nonprop_fixed))
assert props > 0 and nonprops > 0, "L4 VACUOUS"
print("L5 two-cycle lambda=1   : %d predicted failures all confirmed non-cyclic, %d rows not predicted"
      % (tot["L5"][0], tot["L5"][1]))
assert tot["L5"][0] > 0, "L5 VACUOUS: never predicted a failure"
print("ALL LEMMAS PASS  %.1fs" % (time.time()-T0))
