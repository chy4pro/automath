#!/usr/bin/env python3
"""ROUND 6-M: verify K6-N4m's odd-characteristic all-six-fail input over GF(7) with my oracle."""
import sys, itertools
sys.stdout.reconfigure(line_buffering=True)
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']
F = GF(7); n = 4
A = [[2,3,4,6],[3,2,6,4],[4,6,2,3],[6,4,3,2]]
AmI = [[F.ADD[A[i][j]][F.NEG[1] if i == j else 0] for j in range(n)] for i in range(n)]
print("rank(A)=%d rank(A-I)=%d row sums=%s" % (rank_rows(A, n, F), rank_rows(AmI, n, F),
      [sum(r) % 7 for r in A]))
def ctype(s):
    seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))
by = {}
for s in itertools.permutations(range(n)):
    M = tuple(A[i][s[j]] for i in range(n) for j in range(n))
    by.setdefault(ctype(s), []).append((s, cyclic(M, n, F)))
for t in sorted(by):
    good = [s for (s, ok) in by[t] if ok]
    print("  type %s: %d of %d cyclic; witnesses %s" % (t, len(good), len(by[t]), good[:6]))
# eigenvalues in GF(7): rank(A - mu I)
print("nullity(A - mu) for mu in GF(7):", {mu: n - rank_rows([[F.ADD[A[i][j]][F.NEG[mu] if i == j else 0] for j in range(n)] for i in range(n)], n, F) for mu in range(7)})
