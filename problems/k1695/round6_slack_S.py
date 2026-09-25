#!/usr/bin/env python3
"""ROUND 6-D (line k1695): SLACK of the (S)-certificate on GL(4,2) and GL(3,q).

For each A count the number of pairs (i, sigma) with e_i a cyclic vector of A P_sigma, and the
number of sigma with A P_sigma cyclic at all.  The matrices with the FEWEST (S)-witnesses are where
a proof of (S) must do its work; print them with their structure (rank(A - lambda I) profile).
Light compute, exact tables.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, controllable, cyclic = G['GF'], G['rank_rows'], G['controllable'], G['cyclic']

def matmul_cols(Acols, Pcols, n, F):
    """columns of A*P given columns of A and columns of P (each col a list)"""
    ADD, MUL = F.ADD, F.MUL
    out = []
    for pc in Pcols:
        v = [0]*n
        for j, x in enumerate(pc):
            if x:
                Mx = MUL[x]; c = Acols[j]
                for i in range(n):
                    if c[i]: v[i] = ADD[v[i]][Mx[c[i]]]
        out.append(v)
    return out

print("ROUND 6-D: slack of the (S) certificate")
for (n, q) in [(3, 2), (3, 3), (4, 2), (3, 4)]:
    F = GF(q)
    perms = list(itertools.permutations(range(n)))
    Pcols = {s: [[1 if s[j] == i else 0 for i in range(n)] for j in range(n)] for s in perms}
    hist = {}; worst = []; tot = 0
    for entries in itertools.product(range(q), repeat=n*n):
        rows = [list(entries[i*n:(i+1)*n]) for i in range(n)]
        if rank_rows(rows, n, F) < n: continue
        tot += 1
        Acols = [[rows[i][j] for i in range(n)] for j in range(n)]
        nS = 0; nC = 0
        for s in perms:
            Mc = matmul_cols(Acols, Pcols[s], n, F)
            Mflat = tuple(Mc[j][i] for i in range(n) for j in range(n))
            if cyclic(Mflat, n, F):
                nC += 1
                for i in range(n):
                    e = [0]*n; e[i] = 1
                    if controllable(Mc, n, e, F): nS += 1
        hist[nS] = hist.get(nS, 0) + 1
        if len(worst) < 400:
            worst.append((nS, nC, entries))
        else:
            worst.sort();
            if nS < worst[-1][0]:
                worst[-1] = (nS, nC, entries)
    worst.sort()
    print("GL(%d,%d): |GL|=%d  histogram of #(i,sigma) (S)-witnesses (min first): %s" % (n, q, tot, sorted(hist.items())[:8]))
    print("   worst 6 (nS, #cyclic sigma, A rows):")
    for (nS, nC, e) in worst[:6]:
        rows = [e[i*n:(i+1)*n] for i in range(n)]
        # rank profile: rank(A - lam I) for lam in GF(q)
        prof = []
        for lam in range(q):
            M = [list(r) for r in rows]
            for i in range(n): M[i][i] = F.ADD[M[i][i]][F.NEG[lam]]
            prof.append(rank_rows(M, n, F))
        print("     nS=%d nC=%d rows=%s rank(A-lam) for lam in GF(q)=%s" % (nS, nC, rows, prof))
    print("   [%.1fs]" % (time.time()-T0))
print("done")
