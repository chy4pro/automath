#!/usr/bin/env python3
"""ROUND 6-N: the Klein-four group-algebra family at n = 4.
A_f = sum_{g in V4} f(g) P_g, i.e. A[i][j] = f(i xor j) (V4 acting regularly on {0,1,2,3}).
For q in {2,3,4,5,7,9,11,13}: scan ALL f with A_f invertible; for each, count the sigma in S_4 with
A_f P_sigma cyclic, split by cycle type; report the minimum and the members attaining it, and whether
any member defeats all of S_4 (that would be a counterexample to 16.95).
Also the circulant (Z_4) family A[i][j] = f((j - i) mod 4) for comparison.  Exact tables; light."""
import sys, itertools, time
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']
n = 4
perms = list(itertools.permutations(range(n)))
def ctype(s):
    seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))
types = {s: ctype(s) for s in perms}
for fam in ("V4", "Z4"):
    for q in (2, 3, 4, 5, 7, 9, 11, 13):
        F = GF(q)
        tot = 0; minimum = None; worst = []; zero = 0; hist_min_by_type = None
        for f in itertools.product(range(q), repeat=4):
            if fam == "V4":
                A = [[f[i ^ j] for j in range(n)] for i in range(n)]
            else:
                A = [[f[(j - i) % n] for j in range(n)] for i in range(n)]
            if rank_rows(A, n, F) < n: continue
            tot += 1
            good = {}
            for s in perms:
                M = tuple(A[i][s[j]] for i in range(n) for j in range(n))
                if cyclic(M, n, F):
                    good[types[s]] = good.get(types[s], 0) + 1
            ng = sum(good.values())
            if ng == 0:
                zero += 1
                print("  *** ALL 24 FAIL: family=%s q=%d f=%s ***" % (fam, q, f))
            if minimum is None or ng < minimum:
                minimum = ng; worst = [(f, dict(sorted(good.items())))]
            elif ng == minimum and len(worst) < 3:
                worst.append((f, dict(sorted(good.items()))))
        print("%s family over GF(%d): invertible members=%d  all-fail=%d  min #good sigma=%s  examples=%s  [%.1fs]"
              % (fam, q, tot, zero, minimum, worst, time.time()-T0))
print("done")
