#!/usr/bin/env python3
"""ROUND 6-AC: probe of the surviving conjecture (2Step) after the refutation of (Mono) (registry R6.73):
for every (B, i) with kd(B, i) < n that is a kd-local maximum (no column transposition raises kd), some
neutral transposition followed by some transposition raises kd.  Random invertible B over GF(2), n = 6
(and n = 7), own code; also records Phi'-local maxima (Mono failures) found along the way."""
import sys, itertools, time, random
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows = G['GF'], G['rank_rows']
F = GF(2)
def run(n, N, cap):
    rng = random.Random(1695 + n)
    trans = [(a, b) for a in range(n) for b in range(a+1, n)]
    def swapcols(B, a, b): return [[row[b] if j == a else (row[a] if j == b else row[j]) for j in range(n)] for row in B]
    def matvec(B, v): return [sum(B[i][j] & v[j] for j in range(n)) & 1 for i in range(n)]
    def kd(B, i):
        v = [0]*n; v[i] = 1; kry = [v]
        for _ in range(n-1): v = matvec(B, v); kry.append(v)
        return rank_rows(kry, n, F)
    tot = 0; locmax = 0; mono_fail = 0; twostep_fail = 0; examples = []
    for _ in range(N):
        if time.time() - T0 > cap: print("  cap reached"); break
        B = [[rng.randrange(2) for _ in range(n)] for _ in range(n)]
        if rank_rows([r[:] for r in B], n, F) < n: continue
        tot += 1
        for i in range(n):
            k = kd(B, i)
            if k == n: continue
            nb = [kd(swapcols(B, a, b), i) for (a, b) in trans]
            if max(nb) > k: continue
            locmax += 1
            nu = sum(1 for x in nb if x == k)
            dec = False; asc2 = False
            for (a, b), x in zip(trans, nb):
                if x == k:
                    B2 = swapcols(B, a, b)
                    nb2 = [kd(swapcols(B2, c, d), i) for (c, d) in trans]
                    if max(nb2) > k: asc2 = True
                    if sum(1 for y in nb2 if y == k) < nu: dec = True
            if not dec: mono_fail += 1
            if not asc2:
                twostep_fail += 1
                if len(examples) < 3: examples.append((B, i, k, nu))
    print("n=%d GF(2): invertible samples=%d  kd-local maxima (B,i)=%d  (Mono) failures=%d  (2Step) failures=%d  [%.0fs]" % (n, tot, locmax, mono_fail, twostep_fail, time.time()-T0))
    for ex in examples: print("   (2Step) failure example:", ex)
run(6, 20000, 500); run(7, 6000, 900)
print("done %.0fs" % (time.time()-T0))
