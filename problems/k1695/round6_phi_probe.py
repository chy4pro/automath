#!/usr/bin/env python3
"""ROUND 6-Q: independent probe of the potential Phi' = (kd, -nu) (registry R6.45), my own code.
For every B in GL(n,q) (B = A P_sigma; every (A,sigma) pair is some B, so it suffices to scan B) and
every index i with kd(B,i) < n and no transposition tau with kd(B P_tau, i) > kd(B,i)  [a kd-local
maximum], check that some NEUTRAL tau (kd unchanged) has nu(B P_tau, i) < nu(B, i), where nu = number
of neutral transpositions.  Print the (nu, min nu') pairs and any violation.  Light: GL(3,4), GL(4,2)
exhaustively; GL(3,5) if time permits (cap 20 min)."""
import sys, itertools, time
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time(); CAP = 1200
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows = G['GF'], G['rank_rows']

def run(n, q):
    F = GF(q); ADD, MUL = F.ADD, F.MUL
    trans = [(a, b) for a in range(n) for b in range(a+1, n)]
    def swapcols(B, a, b):
        return [[row[b] if j == a else (row[a] if j == b else row[j]) for j in range(n)] for row in B]
    def matvec(B, v):
        out = [0]*n
        for i in range(n):
            acc = 0
            for j in range(n):
                if B[i][j] and v[j]: acc = ADD[acc][MUL[B[i][j]][v[j]]]
            out[i] = acc
        return out
    def kd(B, i):
        v = [0]*n; v[i] = 1; kry = [v]
        for _ in range(n-1):
            v = matvec(B, v); kry.append(v)
        return rank_rows(kry, n, F)
    def kd_nu(B, i):
        k = kd(B, i); nb = [kd(swapcols(B, a, b), i) for (a, b) in trans]
        return k, nb
    tot = 0; locmax = 0; viol = 0; pairs = {}; examples = []
    for entries in itertools.product(range(q), repeat=n*n):
        if time.time() - T0 > CAP:
            print("  CAP reached in GL(%d,%d) after %d matrices" % (n, q, tot)); break
        B = [list(entries[r*n:(r+1)*n]) for r in range(n)]
        if rank_rows(B, n, F) < n: continue
        tot += 1
        for i in range(n):
            k, nb = kd_nu(B, i)
            if k == n or max(nb) > k: continue
            locmax += 1
            nu = sum(1 for x in nb if x == k)
            best = None
            for (a, b), x in zip(trans, nb):
                if x == k:
                    B2 = swapcols(B, a, b); k2, nb2 = kd_nu(B2, i)
                    nu2 = sum(1 for y in nb2 if y == k2)
                    if best is None or nu2 < best: best = nu2
            pairs[(nu, best)] = pairs.get((nu, best), 0) + 1
            if best is None or best >= nu:
                viol += 1
                if len(examples) < 3: examples.append((B, i, k, nu, best))
    print("GL(%d,%d): invertible=%d  kd-local maxima (B,i)=%d  (nu, min nu' over neutral nbrs) -> count: %s  VIOLATIONS of (Mono)=%d  [%.0fs]"
          % (n, q, tot, locmax, sorted(pairs.items()), viol, time.time()-T0))
    for ex in examples: print("   violation example:", ex)

print("ROUND 6-Q: Phi' = (kd, -nu) monotonicity probe (own code)")
run(3, 4); run(4, 2); run(3, 5)
print("done %.0fs" % (time.time()-T0))
