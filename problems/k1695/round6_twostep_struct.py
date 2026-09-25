#!/usr/bin/env python3
"""ROUND 6-AD: structured (2Step)/(Mono) probe at n = 6 over GF(2) (registry R6.75): B = P_w + u v^T
(rank-one perturbations of permutation matrices, where the Pro counterexample M lives: M - P_? has low
rank) and B = P_w + u v^T + u' v'^T (rank two).  For each invertible sample and each i: is (B, i) a
kd-local maximum below 6?  If so: (Mono) decrease available?  (2Step) ascent available?  Own code."""
import sys, itertools, time, random
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows = G['GF'], G['rank_rows']
F = GF(2); n = 6
trans = [(a, b) for a in range(n) for b in range(a+1, n)]
def swapcols(B, a, b): return [[row[b] if j == a else (row[a] if j == b else row[j]) for j in range(n)] for row in B]
def matvec(B, v): return [sum(B[i][j] & v[j] for j in range(n)) & 1 for i in range(n)]
def kd(B, i):
    v = [0]*n; v[i] = 1; kry = [v]
    for _ in range(n-1): v = matvec(B, v); kry.append(v)
    return rank_rows(kry, n, F)
def probe(name, gen, N, cap):
    rng = random.Random(1695)
    tot = 0; locmax = 0; mono_fail = 0; two_fail = 0; ex = []
    for _ in range(N):
        if time.time() - T0 > cap: print("  cap"); break
        B = gen(rng)
        if rank_rows([r[:] for r in B], n, F) < n: continue
        tot += 1
        for i in range(n):
            k = kd(B, i)
            if k == n: continue
            nb = [kd(swapcols(B, a, b), i) for (a, b) in trans]
            if max(nb) > k: continue
            locmax += 1
            nu = sum(1 for x in nb if x == k); dec = False; asc = False
            for (a, b), x in zip(trans, nb):
                if x == k:
                    B2 = swapcols(B, a, b); nb2 = [kd(swapcols(B2, c, d), i) for (c, d) in trans]
                    if max(nb2) > k: asc = True
                    if sum(1 for y in nb2 if y == k) < nu: dec = True
            if not dec: mono_fail += 1
            if not asc:
                two_fail += 1
                if len(ex) < 3: ex.append((B, i, k))
    print("%s: invertible=%d  kd-local maxima=%d  (Mono) failures=%d  (2Step) failures=%d  [%.0fs]" % (name, tot, locmax, mono_fail, two_fail, time.time()-T0))
    for e in ex: print("   (2Step) FAILURE:", e)
def rank1(rng):
    w = list(range(n)); rng.shuffle(w)
    u = [rng.randrange(2) for _ in range(n)]; v = [rng.randrange(2) for _ in range(n)]
    return [[(1 if w[j] == i else 0) ^ (u[i] & v[j]) for j in range(n)] for i in range(n)]
def rank2(rng):
    B = rank1(rng); u = [rng.randrange(2) for _ in range(n)]; v = [rng.randrange(2) for _ in range(n)]
    return [[B[i][j] ^ (u[i] & v[j]) for j in range(n)] for i in range(n)]
probe("n=6 GF(2) P_w + u v^T", rank1, 30000, 400)
probe("n=6 GF(2) P_w + rank-2", rank2, 30000, 900)
print("done %.0fs" % (time.time()-T0))
