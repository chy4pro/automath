#!/usr/bin/env python3
"""ROUND 6-E (line k1695): the TIGHTEST instances of (T_m) — where a proof must do its work.

For every m x (m+1) matrix R of rank m (up to column order), count the witnesses (j, tau): column j
and ordering tau of the others such that R[:,j] is a cyclic vector of R[:,!=j] P_tau.  Also record,
per column j, whether ANY tau works ("j is a usable pivot column") and compare with kappa_j != 0
(kappa = the kernel vector of R; kappa_j != 0 iff the other m columns are independent).
Print the minimum witness count and the matrices attaining it.  Light compute, exact tables.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, controllable = G['GF'], G['rank_rows'], G['controllable']

def vec_of_int(x, m, q):
    v = []
    for _ in range(m):
        v.append(x % q); x //= q
    return v

def kernel_vec(cols, m, F):
    """kernel vector of the m x (m+1) matrix with the given columns (1-dim kernel)"""
    rows = [[cols[j][i] for j in range(m+1)] for i in range(m)]
    ADD, MUL, NEG, INV = F.ADD, F.MUL, F.NEG, F.INV
    R = [list(r) for r in rows]; piv = []; r = 0
    for c in range(m+1):
        p = next((i for i in range(r, len(R)) if R[i][c]), None)
        if p is None: continue
        R[r], R[p] = R[p], R[r]
        iv = INV[R[r][c]]; R[r] = [MUL[x][iv] for x in R[r]]
        for i in range(len(R)):
            if i != r and R[i][c]:
                Mnf = MUL[NEG[R[i][c]]]
                R[i] = [ADD[R[i][t]][Mnf[R[r][t]]] for t in range(m+1)]
        piv.append(c); r += 1
        if r == m: break
    free = [c for c in range(m+1) if c not in piv][0]
    k = [0]*(m+1); k[free] = 1
    for i, pc in enumerate(piv):
        k[pc] = NEG[R[i][free]]
    return k

print("ROUND 6-E: tightest (T_m) instances")
for (m, q) in [(2, 2), (2, 3), (3, 2), (3, 3), (4, 2), (2, 5), (3, 4)]:
    F = GF(q)
    vecs = [vec_of_int(x, m, q) for x in range(q**m)]
    tot = 0; hist = {}; worst = []
    pivot_vs_kappa = {"usable&kappa!=0": 0, "usable&kappa==0": 0, "unusable&kappa!=0": 0, "unusable&kappa==0": 0}
    for comb in itertools.combinations_with_replacement(range(q**m), m+1):
        cols = [vecs[x] for x in comb]
        if rank_rows([[cols[j][i] for j in range(m+1)] for i in range(m)], m+1, F) < m:
            continue
        tot += 1
        kap = kernel_vec(cols, m, F)
        nwit = 0
        for j in range(m+1):
            b = cols[j]; others = [cols[t] for t in range(m+1) if t != j]
            nj = 0
            for tau in itertools.permutations(range(m)):
                if controllable([others[tau[l]] for l in range(m)], m, b, F): nj += 1
            nwit += nj
            key = ("usable" if nj else "unusable") + "&" + ("kappa!=0" if kap[j] else "kappa==0")
            pivot_vs_kappa[key] += 1
        hist[nwit] = hist.get(nwit, 0) + 1
        worst.append((nwit, comb))
    worst.sort()
    mn = worst[0][0]
    print("(T_%d)/GF(%d): matrices=%d  min #witnesses=%d (attained by %d)  histogram head=%s  pivot-usable vs kappa: %s  [%.1fs]"
          % (m, q, tot, mn, hist[mn], sorted(hist.items())[:6], pivot_vs_kappa, time.time()-T0))
    for (nw, comb) in worst[:4]:
        print("     #wit=%d columns=%s" % (nw, [vecs[x] for x in comb]))
print("done")
