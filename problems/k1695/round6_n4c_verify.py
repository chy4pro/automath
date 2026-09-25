#!/usr/bin/env python3
"""ROUND 6-I (line k1695): re-verify K6-N4c's two GF(4) stratum-(a) matrices for which it claims
ALL SIX transpositions fail (encoding 2 = alpha, 3 = alpha+1 in GF(4) = F2[alpha]/(alpha^2+alpha+1)),
with my own oracle; report which permutations work, by cycle type.  Also confirm rank(A - I) = 2 and
the case classification (charpoly of S via A's charpoly = x^2 (x^2 - tr x + e2))."""
import sys, itertools
sys.stdout.reconfigure(line_buffering=True)
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']
F = GF(4)
# my GF(4) from round3_family: elements 0..3 with index = a0 + 2*a1 for a0 + a1*alpha, IRRED (2,2) = [1,1,1]
# so 2 = alpha, 3 = 1 + alpha : same encoding as the report's
assert F.MUL[2][2] == 3 and F.ADD[2][3] == 1, "GF(4) encoding differs from the report's"

def ctype(s):
    n = len(s); seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))

def AP(A, s, n):
    # (A P_s)[i][j] = A[i][s(j)]
    return tuple(A[i][s[j]] for i in range(n) for j in range(n))

mats = {
 "beta-rat": [[3,2,0,1],[0,1,0,0],[2,2,1,2],[0,0,0,2]],
 "gamma":    [[1,0,0,0],[3,0,2,0],[3,2,0,0],[0,3,3,1]],
}
for name, A in mats.items():
    n = 4
    AmI = [[F.ADD[A[i][j]][F.NEG[1] if i == j else 0] for j in range(n)] for i in range(n)]
    print("%s: rank(A)=%d rank(A-I)=%d" % (name, rank_rows(A, n, F), rank_rows(AmI, n, F)))
    by_type = {}
    for s in itertools.permutations(range(n)):
        ok = cyclic(AP(A, s, n), n, F)
        by_type.setdefault(ctype(s), []).append((s, ok))
    for t in sorted(by_type):
        good = [s for (s, ok) in by_type[t] if ok]
        print("   type %s: %d of %d cyclic; witnesses %s" % (t, len(good), len(by_type[t]), good[:4]))
print("done")
