#!/usr/bin/env python3
"""ROUND 6-X: reproduce the two 'fresh finite evidence' claims of the K6-WIDE Pro answer (registry R6.63)
with own code, plus the good-count statistics behind its conjecture (GC_n): g(A) >= (n-1)!.
 (a) (OC_4) over GF(2): every A in GL(4,2) equals u H u^{-1} P^{-1} with u lower unitriangular,
     H invertible unreduced upper Hessenberg (H[i][j]=0 for i>j+1, H[j+1][j]!=0), P a permutation matrix
     — i.e. u^{-1} A P u is in the Coxeter cell.  Claim: the union has all 20160 elements.
 (b) g(A) = #{sigma : A P_sigma cyclic}: exhaustive minimum over GL(3,q), q=2,3,4,5, and GL(4,2)
     (claim: min = 6 = 3!, attained by 168 matrices); how many minimizers are monomial; GL(4,3) sample."""
import sys, itertools, time, random
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']

# ---------- (a) OC_4 over GF(2) ----------
n = 4
def mm2(X, Y):
    return tuple(tuple(sum(X[i][k] & Y[k][j] for k in range(n)) & 1 for j in range(n)) for i in range(n))
lows = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]
Us = []
for bits in itertools.product((0, 1), repeat=6):
    u = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for (i, j), b in zip(lows, bits): u[i][j] = b
    Us.append(tuple(map(tuple, u)))
def inv2(u):  # inverse of a lower unitriangular matrix over GF(2)
    v = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            v[i][j] = sum(u[i][k] & v[k][j] for k in range(j, i)) & 1
    return tuple(map(tuple, v))
F2 = GF(2)
Hs = []
frees = [(i, j) for i in range(n) for j in range(n) if i <= j]
for bits in itertools.product((0, 1), repeat=len(frees)):
    H = [[0]*n for _ in range(n)]
    for (i, j), b in zip(frees, bits): H[i][j] = b
    for j in range(n-1): H[j+1][j] = 1
    if rank_rows(H, n, F2) == n: Hs.append(tuple(map(tuple, H)))
perms = list(itertools.permutations(range(n)))
Pinv = []
for s in perms:  # P_s e_j = e_{s(j)}; P^{-1} = P^T
    P = tuple(tuple(1 if s[j] == i else 0 for j in range(n)) for i in range(n))
    Pinv.append(tuple(tuple(P[j][i] for j in range(n)) for i in range(n)))
seen = set()
for u in Us:
    ui = inv2(u)
    for H in Hs:
        M = mm2(mm2(u, H), ui)
        for Q in Pinv:
            seen.add(mm2(M, Q))
print("(a) OC_4 over GF(2): |U^-|=%d, invertible unreduced Hessenberg=%d, permutations=%d; union size=%d (|GL(4,2)|=20160)  [%.0fs]"
      % (len(Us), len(Hs), len(perms), len(seen), time.time()-T0))

# ---------- (b) good counts ----------
def gstats(n, q, sample=None, want_min_list=False):
    F = GF(q); perms = list(itertools.permutations(range(n)))
    rng = random.Random(1695)
    it = itertools.product(range(q), repeat=n*n) if sample is None else (tuple(rng.randrange(q) for _ in range(n*n)) for _ in range(sample))
    hist = {}; tot = 0; mins = []
    for entries in it:
        A = [list(entries[r*n:(r+1)*n]) for r in range(n)]
        if rank_rows(A, n, F) < n: continue
        tot += 1
        g = sum(1 for s in perms if cyclic(tuple(A[i][s[j]] for i in range(n) for j in range(n)), n, F))
        hist[g] = hist.get(g, 0) + 1
        if want_min_list: mins.append((g, entries))
    mn = min(hist)
    line = "(b) GL(%d,%d)%s: invertible=%d  min g=%d ((n-1)!=%d)  #minimizers=%d  g-histogram=%s  [%.0fs]" % (
        n, q, "" if sample is None else " sample %d" % sample, tot, mn, __import__("math").factorial(n-1), hist[mn], sorted(hist.items()), time.time()-T0)
    print(line)
    if want_min_list:
        minimizers = [e for g, e in mins if g == mn]
        def is_monomial(e):
            A = [e[r*n:(r+1)*n] for r in range(n)]
            return all(sum(1 for x in row if x) == 1 for row in A) and all(sum(1 for i in range(n) if A[i][j]) == 1 for j in range(n))
        mono = sum(1 for e in minimizers if is_monomial(e))
        # orbit structure under A -> Q A P (row & column permutations): count orbits
        orbits = set()
        for e in minimizers:
            A = [e[r*n:(r+1)*n] for r in range(n)]
            rep = min(tuple(A[s[i]][t[j]] for i in range(n) for j in range(n)) for s in perms for t in perms)
            orbits.add(rep)
        print("    minimizers: %d, monomial among them: %d, orbits under two-sided permutation: %d; representatives: %s" % (
            len(minimizers), mono, len(orbits), sorted(orbits)[:6]))

for q in (2, 3, 4, 5): gstats(3, q)
gstats(4, 2, want_min_list=True)
gstats(4, 3, sample=30000)
print("done %.0fs" % (time.time()-T0))
