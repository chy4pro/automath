#!/usr/bin/env python3
"""ROUND 6-Y: numerical checks of the Qwen K6-GC answer (registry R6.65), own code.
 (i) GC_3 in its strong form: for every A in GL(3,q), at least TWO permutations sigma make e_1 a
     Krylov-cyclic vector of A P_sigma (columns a_{sigma(1)}, a_{sigma(2)}, a_{sigma(3)}); exhaustive
     for q = 2, 3, 4, 5; also the Delta-lemma count (number of nonzero Delta(i;j,k)) distribution.
 (ii) the rank-one family A = I + gamma*J: n = 3 over F_5 with gamma = -2/3 = 1 (A = I + J): g = 2;
      n = 4 over F_7 with gamma = (omega-1)/4, omega = 2: gamma = 1/4 = 2 (A = I + 2J): g = 6."""
import sys, itertools, time
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']

def krylov_e1_count(A, n, F):
    ADD, MUL = F.ADD, F.MUL
    perms = list(itertools.permutations(range(n)))
    cnt = 0
    for s in perms:
        B = [[A[i][s[j]] for j in range(n)] for i in range(n)]
        v = [0]*n; v[0] = 1; kry = [v]
        for _ in range(n-1):
            w = [0]*n
            for i in range(n):
                acc = 0
                for j in range(n):
                    if B[i][j] and v[j]: acc = ADD[acc][MUL[B[i][j]][v[j]]]
                w[i] = acc
            v = w; kry.append(v)
        if rank_rows(kry, n, F) == n: cnt += 1
    return cnt

n = 3
for q in (2, 3, 4, 5):
    F = GF(q); hist = {}; tot = 0; worst = None
    for entries in itertools.product(range(q), repeat=9):
        A = [list(entries[r*3:(r+1)*3]) for r in range(3)]
        if rank_rows(A, 3, F) < 3: continue
        tot += 1
        c = krylov_e1_count(A, 3, F)
        hist[c] = hist.get(c, 0) + 1
        if worst is None or c < worst[0]: worst = (c, entries)
    print("(i) GL(3,%d): invertible=%d  #{sigma: e_1 Krylov-cyclic for A P_sigma} histogram=%s  MIN=%d (GC_3 strong form needs >= 2)  [%.0fs]"
          % (q, tot, sorted(hist.items()), min(hist), time.time()-T0))

# (ii) rank-one family
def g_of(A, n, F):
    perms = list(itertools.permutations(range(n)))
    return sum(1 for s in perms if cyclic(tuple(A[i][s[j]] for i in range(n) for j in range(n)), n, F))
F5 = GF(5); A = [[(1 if i == j else 0) + 1 for j in range(3)] for i in range(3)]
print("(ii) n=3, F_5, A = I + J (gamma = -2/3 = 1 mod 5): g =", g_of(A, 3, F5), " (claim 2)")
F7 = GF(7); A = [[((1 if i == j else 0) + 2) % 7 for j in range(4)] for i in range(4)]
print("(ii) n=4, F_7, A = I + 2J (gamma = (omega-1)/4 = 2, omega = 2): g =", g_of(A, 4, F7), " (claim 6)")
# control: a different gamma over F_7 should generally give more than 6
A = [[((1 if i == j else 0) + 1) % 7 for j in range(4)] for i in range(4)]
print("(ii) control n=4, F_7, A = I + J: g =", g_of(A, 4, F7))
print("done %.0fs" % (time.time()-T0))
