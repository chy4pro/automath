"""k=3 relaxation: x = distribution over C4-free Q3 (labelled, symmetrised via orbits).
 Constraints: (V) degree histogram = Bin(3,delta) mixture;
              (E) edge-rooted second moments M^s (8x8, types of the 2 squares through the root edge)
                  must be PSD (cutting planes) and >= 0 (automatic).
"""
import numpy as np, itertools
from math import comb
from scipy.optimize import linprog
from cube import cube, c4free_masks

k = 3
E, eidx, sq = cube(k)
L = c4free_masks(k)
m = len(E)
# per graph statistics
def stats(x):
    D = [set() for _ in range(1 << k)]
    for t, (a, b, i) in enumerate(E):
        if (x >> t) & 1:
            D[a].add(i); D[b].add(i)
    hist = np.bincount([len(d) for d in D], minlength=k + 1)
    # edge-root: for each edge (u lower, v upper, dir i), for each other direction j: type
    prof = []
    for t, (u, v, i) in enumerate(E):
        s = (x >> t) & 1
        types = []
        for j in range(k):
            if j == i: continue
            u2, v2 = u ^ (1 << j), v ^ (1 << j)
            bu = 1 if j in D[u] else 0
            bv = 1 if j in D[v] else 0
            bt = 1 if i in D[u2] else 0
            types.append(bu + 2 * bv + 4 * bt)
        prof.append((s, types))
    return hist, prof

T = 8
nG = len(L)
Hs = np.zeros((nG, k + 1))
Mlin = np.zeros((nG, 2, T, T))   # contribution to M^s
for g, x in enumerate(L):
    h, prof = stats(x)
    Hs[g] = h / 2**k
    for s, types in prof:
        a, b = types
        # symmetrise u<->v: type bu+2bv+4bt -> bv+2bu+4bt
        sw = lambda t: ((t >> 1) & 1) | ((t & 1) << 1) | (t & 4)
        for (p, q) in ((a, b), (sw(a), sw(b))):
            Mlin[g, s, p, q] += 0.25 / m
            Mlin[g, s, q, p] += 0.25 / m
edges_cnt = np.array([bin(x).count("1") for x in L]) / m

grid = 1001
ds = np.linspace(0, 1, grid)
Bm = np.array([[comb(k, j) * d**j * (1 - d)**(k - j) for j in range(k + 1)] for d in ds])

def solve(cuts, use_edge=True):
    nv = nG + grid
    Aeq = []; beq = []
    for j in range(k + 1):
        row = np.zeros(nv); row[:nG] = Hs[:, j]; row[nG:] = -Bm[:, j]; Aeq.append(row); beq.append(0)
    row = np.zeros(nv); row[:nG] = 1; Aeq.append(row); beq.append(1)
    row = np.zeros(nv); row[nG:] = 1; Aeq.append(row); beq.append(1)
    Aub = []; bub = []
    for (s, vec) in cuts:   # vec^T M^s vec >= 0  ->  -sum_g x_g vec^T Mlin vec <= 0
        row = np.zeros(nv)
        row[:nG] = -np.einsum('gpq,p,q->g', Mlin[:, s], vec, vec)
        Aub.append(row); bub.append(0)
    c = np.zeros(nv); c[:nG] = -edges_cnt
    r = linprog(c, A_ub=np.array(Aub) if Aub else None, b_ub=np.array(bub) if bub else None,
                A_eq=np.array(Aeq), b_eq=np.array(beq), bounds=(0, None), method="highs")
    return r

cuts = []
for it in range(200):
    r = solve(cuts)
    xg = r.x[:nG]
    worst = 0
    for s in (0, 1):
        M = np.einsum('g,gpq->pq', xg, Mlin[:, s])
        w, V = np.linalg.eigh(M)
        for idx in range(T):
            if w[idx] < -1e-9:
                cuts.append((s, V[:, idx].copy())); worst = min(worst, w[idx])
    if it % 10 == 0 or worst > -1e-9:
        print(it, -r.fun, worst, len(cuts))
    if worst > -1e-9:
        break
print("k=3 vertex+edge-root(PSD) bound:", -r.fun)
