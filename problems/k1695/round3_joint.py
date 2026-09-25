#!/usr/bin/env python3
"""ROUND 3-H (line k1695): is the family obstruction SEPARABLE or JOINT?

R3.8 finished the lambda=1 layer for A = aI + u v^T.  The named gap is lambda != 1.  Before
attacking it, settle the question that decides the shape of the proof:

  (A) is there an arrangement with NO bad lambda at all?          (= the n-cycle works)
  (B) is there an arrangement with no bad lambda != 1?            (the lambda!=1 layer alone)
  (C) is there an arrangement with no bad lambda = 1?             (the lambda=1 layer alone)

If (B) and (C) always hold while (A) sometimes fails, the obstruction is JOINT: no arrangement
satisfies both layers at once, and the proof of T1 cannot be two independent steps.  If instead
(A) fails exactly when (B) or (C) fails, the layers are separable and the proof can be modular.
Criterion C1 gives the bad set as the roots of one gcd g; lambda=1 is bad iff (x-1) | g, and
some lambda != 1 is bad iff g still has a nonconstant part after dividing out every (x-1).
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round3_family.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 3-B family attack start')], "rf", "exec"), G)
GF, criterion_ncycle, pmod, distinct_cyclic_orders = (G['GF'], G['criterion_ncycle'], G['pmod'],
                                                      G['distinct_cyclic_orders'])

def layers(seq, n, F):
    """(bad_at_1, bad_away_from_1) for one arrangement."""
    ok, g = criterion_ncycle(list(seq), n, F)
    if ok:
        return (False, False)
    lin = [F.NEG[1], 1]                      # x - 1
    at1 = (pmod(g, lin, F) == [])
    h = list(g)
    while len(h) > 1 and pmod(h, lin, F) == []:
        # exact division by (x-1)
        qout = [0]*(len(h)-1); rem = list(h)
        for d in range(len(h)-2, -1, -1):
            c = rem[d+1]
            qout[d] = c
            rem[d+1] = 0
            rem[d] = F.ADD[rem[d]][c]        # subtract c*(x-1)*x^d  ->  rem[d] += c
        h = qout
        while h and h[-1] == 0:
            h.pop()
    away = (len(h) > 1)
    return (at1, away)

print("ROUND 3-H: separable or joint?")
print("q  n  multisets  A-fails(no n-cycle)  B-fails(no arr. clean off 1)  C-fails(no arr. clean at 1)  JOINT-ONLY")
for q in [2, 3, 4]:
    F = GF(q)
    syms = [(1, a, b) for a in range(q) for b in range(q)]
    for n in range(3, 8):
        if q == 3 and n > 6: break
        if q == 4 and n > 5: break
        tot = 0; Afail = 0; Bfail = 0; Cfail = 0; joint = 0; ex = None
        for tokens in itertools.combinations_with_replacement(syms, n):
            c0 = 0
            for t in tokens:
                c0 = F.ADD[c0][F.MUL[t[1]][t[2]]]
            if F.ADD[1][c0] == 0:
                continue
            tot += 1
            orders, _ = distinct_cyclic_orders(list(tokens), n, 200000)
            anyclean = False; anyclean1 = False; anycleanaway = False
            for s in orders:
                a1, aw = layers(s, n, F)
                if not a1 and not aw: anyclean = True
                if not a1: anyclean1 = True
                if not aw: anycleanaway = True
                if anyclean: break
            if not anyclean:
                Afail += 1
                if not anyclean1: Cfail += 1
                if not anycleanaway: Bfail += 1
                if anyclean1 and anycleanaway:
                    joint += 1
                    if ex is None: ex = tokens
        print("%-2d %-2d %-10d %-20d %-28d %-28d %d %s"
              % (q, n, tot, Afail, Bfail, Cfail, joint,
                 ("  e.g. %s" % (ex,)) if ex else ""))
print("%.1fs" % (time.time()-T0))
