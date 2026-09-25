#!/usr/bin/env python3
"""ROUND 3-G (line k1695): HOW CLOSE IS THE FAMILY TO A COUNTEREXAMPLE?

The census says every rank-one-over-monomial matrix has a good permutation.  That is not the
question that matters for refutation.  The question is the SLACK: on the hardest multisets,
how many witnesses are there?  If the minimum witness count is falling toward 1 as n grows,
a counterexample is plausibly just past the window; if it stays comfortably above 1, it is not.
(Round 2 already found one such trap: "most permutations work" was TRUE at small n and the
density in fact decays like log n / n.  Measure, do not extrapolate.)

For every token multiset with NO good n-cycle, count how many fixed points f give a good
(n-1,1) permutation, and how many (n-1,1) permutations are good in total.  Report the minima.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round3_family.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 3-B family attack start')], "rf", "exec"), G)
GF, criterion_ncycle, cyclic, build_M, distinct_cyclic_orders = (
    G['GF'], G['criterion_ncycle'], G['cyclic'], G['build_M'], G['distinct_cyclic_orders'])

def n1_perms(n):
    out = []
    for f in range(n):
        rest = [i for i in range(n) if i != f]
        head, tail = rest[0], rest[1:]
        for pr in itertools.permutations(tail):
            cyc = (head,) + pr
            s = [0]*n; s[f] = f
            for t in range(len(cyc)):
                s[cyc[t]] = cyc[(t+1) % len(cyc)]
            out.append((f, tuple(s)))
    return out

print("ROUND 3-G: witness slack on the hardest multisets")
print("n  q  multisets  no-n-cycle  | min #good f  min #good (n-1,1) perms  (out of n and n*(n-2)!)")
for q in [2, 3]:
    F = GF(q)
    syms = [(1, a, b) for a in range(q) for b in range(q)]
    for n in range(3, 10):
        if q == 3 and n > 7:
            break
        NP = n1_perms(n)
        hard = 0; tot = 0
        min_f = None; min_p = None
        for tokens in itertools.combinations_with_replacement(syms, n):
            c0 = 0
            for t in tokens:
                c0 = F.ADD[c0][F.MUL[t[1]][t[2]]]
            if F.ADD[1][c0] == 0:
                continue
            tot += 1
            orders, capped = distinct_cyclic_orders(list(tokens), n, 100000)
            if any(criterion_ncycle(list(s), n, F)[0] for s in orders):
                continue
            hard += 1
            good_f = set(); good_p = 0
            for (f, s) in NP:
                if cyclic(build_M(tuple(range(n)), list(tokens), s, n, F), n, F):
                    good_f.add(f); good_p += 1
            assert good_p > 0, "*** NO (n-1,1) WITNESS -- check all n! : tokens=%s q=%d ***" % (tokens, q)
            if min_f is None or len(good_f) < min_f:
                min_f = len(good_f); argmin_f = tokens
            if min_p is None or good_p < min_p:
                min_p = good_p
        print("%-2d %-2d %-10d %-11d | %-12s %s   %s" % (n, q, tot, hard,
              min_f if min_f is not None else "-", min_p if min_p is not None else "-",
              ("tightest: %s" % (argmin_f,)) if min_f is not None else ""))
print("%.1fs" % (time.time()-T0))
