#!/usr/bin/env python3
"""ROUND 6-C (line k1695): the WEIGHTED form (W_m) that the deflation of (T_m) lands in.

(W_m)(R, v): R is m x (m+1) of rank m, v in F^m. Statement: there is an ordering tau of ALL m+1
columns such that, with M = R[:, tau(1..m)] (first m columns in that order) and
u = R w where w_{tau(l)} = v_l (l <= m), w_{tau(m+1)} = 1  (i.e. u = sum_l v_l c_{tau(l)} + c_{tau(m+1)}),
the pair (M, u) is controllable (u is a cyclic vector of M).
v = 0 is exactly (T_m).  The deflation identity turns (T_m) at a pivot into (W_{m-1}) with a
specific v, so (W_m) for ALL v would be an induction-closed statement.  Measure it.
Exact table arithmetic; light compute.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, matvec_cols, controllable = G['GF'], G['rank_rows'], G['matvec_cols'], G['controllable']

def vec_of_int(x, m, q):
    v = []
    for _ in range(m):
        v.append(x % q); x //= q
    return v

def W_test(cols, m, v, F):
    """returns a witness ordering or None"""
    for tau in itertools.permutations(range(m+1)):
        M = [cols[tau[l]] for l in range(m)]
        u = list(cols[tau[m]])
        for l in range(m):
            if v[l]:
                c = cols[tau[l]]; Mv = F.MUL[v[l]]
                for i in range(m):
                    if c[i]: u[i] = F.ADD[u[i]][Mv[c[i]]]
        if controllable(M, m, u, F):
            return tau
    return None

print("ROUND 6-C: weighted statement (W_m)(R, v) for all R (rank m, up to column order) and all v")
for (m, q) in [(2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (2, 5), (4, 2)]:
    F = GF(q)
    vecs = [vec_of_int(x, m, q) for x in range(q**m)]
    tot = 0; fails = 0; fail_v = {}; examples = []
    tot_pairs = 0
    for comb in itertools.combinations_with_replacement(range(q**m), m+1):
        cols = [vecs[x] for x in comb]
        if rank_rows([[cols[j][i] for j in range(m+1)] for i in range(m)], m+1, F) < m:
            continue
        tot += 1
        for v in vecs:
            tot_pairs += 1
            if W_test(cols, m, v, F) is None:
                fails += 1
                key = tuple(v); fail_v[key] = fail_v.get(key, 0) + 1
                if len(examples) < 4: examples.append((comb, tuple(v)))
    print("(W_%d) over GF(%d): matrices=%d  (R,v) pairs=%d  FAILURES=%d  failures by v=%s  examples=%s  [%.1fs]"
          % (m, q, tot, tot_pairs, fails, sorted(fail_v.items()), examples, time.time()-T0))
print("done %.1fs" % (time.time()-T0))
