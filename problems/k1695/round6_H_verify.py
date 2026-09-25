#!/usr/bin/env python3
"""ROUND 6-L: re-verify K6-H's smallest local maximum with my own Krylov-rank code.
A = [[1,2,1],[2,1,1],[1,0,0]] over GF(4) (2 = alpha, 3 = alpha+1), sigma = id, i = 2:
claim kd = 2, every transposition neighbour kd = 2, and (0,1) then (0,2) reaches kd = 3."""
import sys, itertools
sys.stdout.reconfigure(line_buffering=True)
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows = G['GF'], G['rank_rows']
F = GF(4); assert F.MUL[2][2] == 3
n = 3
A = [[1,2,1],[2,1,1],[1,0,0]]
def AP(A, s):   # (A P_s)[i][j] = A[i][s(j)]
    return [[A[i][s[j]] for j in range(n)] for i in range(n)]
def matvec(M, v):
    out = [0]*n
    for i in range(n):
        acc = 0
        for j in range(n):
            if M[i][j] and v[j]: acc = F.ADD[acc][F.MUL[M[i][j]][v[j]]]
        out[i] = acc
    return out
def kd(M, i):
    v = [0]*n; v[i] = 1
    kry = [v]
    for _ in range(n-1):
        v = matvec(M, v); kry.append(v)
    return rank_rows(kry, n, F)
def compose(s, t):   # (s o t)(x) = s(t(x)); sigma tau means apply tau first in the column-swap sense: A P_sigma P_tau
    return tuple(s[t[x]] for x in range(n))
ident = (0,1,2)
i = 2
print("rank(A) =", rank_rows(A, n, F))
print("kd(A, id, i=2) =", kd(AP(A, ident), i))
trans = {(0,1):(1,0,2), (0,2):(2,1,0), (1,2):(0,2,1)}
for name, t in trans.items():
    print("  neighbour tau=%s: kd = %d" % (name, kd(AP(A, compose(ident, t)), i)))
two = compose(compose(ident, trans[(0,1)]), trans[(0,2)])
print("two-step (0,1) then (0,2): sigma =", two, " kd =", kd(AP(A, two), i))
# also: is there ANY sigma with kd = 3 for this A and i=2? and for other i?
best = {j: max(kd(AP(A, s), j) for s in itertools.permutations(range(n))) for j in range(n)}
print("max kd over all sigma, per index i:", best)
