#!/usr/bin/env python3
"""ROUND 6-Z: tests for the K6-GC2 answer (registry R6.66), own code.
 (a) low-rank form of (GC_4) and the 'derangement conjecture': for A = I + U W^T (rank <= 2) over F_q,
     invertible, sample: min g(A) (conjecture >= 6) and max number of BAD derangements among the 9
     (conjecture <= 3); q = 3, 5, 7 (20000 samples each) and exhaustive rank-1 over F_3.
 (b) I + gamma*J over F_7 with 1 + 4 gamma = omega = 2 (gamma = 2): bad derangements should be exactly the
     three double transpositions.
 (c) the 'kill a 4-cycle' family over F_5 (i = 2): P = P_(1234), E = 4(I + 2P + 4P^2 + 3P^3) (projection
     onto the -i eigenspace), A = I + (beta-1)E with beta = i = 2, i.e. A = I + E: g(A) and its bad set
     (claim: identity, P, P^2, P^3 bad; g not below 6)."""
import sys, itertools, time, random
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']
n = 4
perms = list(itertools.permutations(range(n)))
def ctype(s):
    seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))
derang = [s for s in perms if all(s[i] != i for i in range(n))]
def good_set(A, F):
    return [s for s in perms if cyclic(tuple(A[i][s[j]] for i in range(n) for j in range(n)), n, F)]

def sample_lowrank(q, N, rank=2):
    F = GF(q); ADD, MUL = F.ADD, F.MUL
    rng = random.Random(1695 + q)
    ming = None; maxbad = 0; tot = 0; hist = {}
    for _ in range(N):
        U = [[rng.randrange(q) for _ in range(rank)] for _ in range(n)]
        W = [[rng.randrange(q) for _ in range(rank)] for _ in range(n)]
        A = [[(1 if i == j else 0) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                acc = A[i][j]
                for k in range(rank): acc = ADD[acc][MUL[U[i][k]][W[j][k]]]
                A[i][j] = acc
        if rank_rows(A, n, F) < n: continue
        tot += 1
        gs = good_set(A, F); g = len(gs)
        hist[g] = hist.get(g, 0) + 1
        bad_der = sum(1 for s in derang if s not in gs)
        if ming is None or g < ming: ming = g
        maxbad = max(maxbad, bad_der)
    print("(a) F_%d, A = I + U W^T rank<=%d, %d invertible samples: min g = %d, max #bad derangements = %d (conj <= 3); g-histogram low end %s  [%.0fs]"
          % (q, rank, tot, ming, maxbad, sorted(hist.items())[:5], time.time()-T0))

for q in (3, 5, 7): sample_lowrank(q, 20000)
sample_lowrank(3, 20000, rank=1)

F7 = GF(7)
A = [[((1 if i == j else 0) + 2) % 7 for j in range(n)] for i in range(n)]
gs = good_set(A, F7)
print("(b) F_7, I + 2J: g = %d; bad derangements = %s" % (len(gs), [(s, ctype(s)) for s in derang if s not in gs]))

F5 = GF(5); ADD, MUL = F5.ADD, F5.MUL
sig = (1, 2, 3, 0)  # sigma = (1234) in 0-based: 0->1->2->3->0 ; P e_j = e_{sigma(j)}
P = [[1 if sig[j] == i else 0 for j in range(n)] for i in range(n)]
def mm(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(n)) % 5 for j in range(n)] for i in range(n)]
I4 = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
P2 = mm(P, P); P3 = mm(P2, P)
E = [[(4*(I4[i][j] + 2*P[i][j] + 4*P2[i][j] + 3*P3[i][j])) % 5 for j in range(n)] for i in range(n)]
E2 = mm(E, E)
print("(c) E idempotent:", E2 == E, " rank E =", rank_rows([row[:] for row in E], n, F5))
A = [[(I4[i][j] + E[i][j]) % 5 for j in range(n)] for i in range(n)]
gs = good_set(A, F5)
bad = [s for s in perms if s not in gs]
print("(c) F_5, A = I + E (beta = i = 2): g = %d; bad permutations = %s" % (len(gs), [(s, ctype(s)) for s in bad]))
print("done %.0fs" % (time.time()-T0))
