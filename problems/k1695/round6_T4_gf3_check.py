#!/usr/bin/env python3
"""ROUND 6-H (line k1695): verify the spark-reported (T_4) FAILURES over GF(3) with independent code,
and test what survives for the completed 5x5 matrices: (S') at the deleted row, (S) at any row,
and 16.95 itself.  Exact tables (GF from round3_family via round6_controllable)."""
import sys, time, itertools, re
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, controllable, cyclic, T_test = G['GF'], G['rank_rows'], G['controllable'], G['cyclic'], G['T_test']
F = GF(3); q = 3

# parse FAIL_T blocks from the spark log
txt = open("engine/harvest/k1695_r6_S/logs/cell4.log").read()
blocks = re.findall(r"FAIL_T cell=T4_GF3\n((?:  \[[0-9,]+\]\n){4})", txt)
mats = []
for b in blocks:
    rows = [list(map(int, r.strip()[1:-1].split(","))) for r in b.strip().split("\n")]
    mats.append(rows)
print("spark FAIL_T blocks parsed: %d" % len(mats))

def matmul_cols(Acols, Pcols, n):
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

confirmed = 0; refuted = 0
S_any_holds = 0; S_any_fails = 0; k1695_fails = 0
perms5 = list(itertools.permutations(range(5)))
Pcols5 = {s: [[1 if s[j] == i else 0 for i in range(5)] for j in range(5)] for s in perms5}
examples = []
for rows in mats[:200]:
    m = 4
    cols = [[rows[i][j] for i in range(m)] for j in range(5)]
    assert rank_rows(rows, 5, F) == 4
    w = T_test(cols, m, F)
    if w is not None:
        refuted += 1; continue
    confirmed += 1
    # complete to 5x5 invertible A = [R; y] with y = the kernel-complement: try all y in GF(3)^5 until invertible
    for y in itertools.product(range(q), repeat=5):
        A = rows + [list(y)]
        if rank_rows(A, 5, F) == 5: break
    Acols = [[A[i][j] for i in range(5)] for j in range(5)]
    # (S') at i=4 must FAIL (consistency), (S) at some i?, 16.95?
    nS_by_i = [0]*5; nC = 0
    for s in perms5:
        Mc = matmul_cols(Acols, Pcols5[s], 5)
        Mflat = tuple(Mc[j][i] for i in range(5) for j in range(5))
        if cyclic(Mflat, 5, F):
            nC += 1
            for i in range(5):
                e = [0]*5; e[i] = 1
                if controllable(Mc, 5, e, F): nS_by_i[i] += 1
    assert nS_by_i[4] == 0, "(S') at the deleted row should fail if (T_4) fails: %s" % (nS_by_i,)
    if any(nS_by_i[i] for i in range(4)): S_any_holds += 1
    else: S_any_fails += 1
    if nC == 0: k1695_fails += 1
    if len(examples) < 3: examples.append((rows, list(y), nS_by_i, nC))
print("(T_4)/GF(3) spark failures re-tested with independent code: confirmed=%d refuted=%d (of first %d)" % (confirmed, refuted, min(200, len(mats))))
print("for the completed 5x5 A: (S) holds at some other row in %d, fails at ALL rows in %d; 16.95 fails in %d" % (S_any_holds, S_any_fails, k1695_fails))
for (rows, y, nS, nC) in examples:
    print("  R=%s  completing row=%s  #(S)-witnesses by row i=%s  #cyclic sigma=%d" % (rows, y, nS, nC))
print("[%.1fs]" % (time.time()-T0))
