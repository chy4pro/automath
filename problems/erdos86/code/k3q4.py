"""Q3 edge-root PSD relaxation (as k3edge.py) coupled with the Q4 degree-histogram constraint
through the common vertex-density mixing measure mu."""
import numpy as np, sys
from math import comb
from scipy.optimize import linprog
exec(open("k3edge.py").read().split("grid = 1001")[0])     # reuse Q3 statistics: L, Hs, Mlin, edges_cnt
H4 = np.load("H4.npy") / 16.0
COUPLE = len(sys.argv) < 2 or sys.argv[1] != "nocouple"
grid = 1001; ds = np.linspace(0, 1, grid)
B3 = np.array([[comb(3, j) * d**j * (1 - d)**(3 - j) for j in range(4)] for d in ds])
B4 = np.array([[comb(4, j) * d**j * (1 - d)**(4 - j) for j in range(5)] for d in ds])
n3, n4 = nG, len(H4)
def solve(cuts):
    nv = n3 + n4 + grid
    Aeq = []; beq = []
    for j in range(4):
        row = np.zeros(nv); row[:n3] = Hs[:, j]; row[n3 + n4:] = -B3[:, j]; Aeq.append(row); beq.append(0)
    if COUPLE:
        for j in range(5):
            row = np.zeros(nv); row[n3:n3 + n4] = H4[:, j]; row[n3 + n4:] = -B4[:, j]; Aeq.append(row); beq.append(0)
    for sl in (slice(0, n3), slice(n3, n3 + n4), slice(n3 + n4, nv)):
        row = np.zeros(nv); row[sl] = 1; Aeq.append(row); beq.append(1)
    Aub = []; bub = []
    for (s, vec) in cuts:
        row = np.zeros(nv); row[:n3] = -np.einsum('gpq,p,q->g', Mlin[:, s], vec, vec); Aub.append(row); bub.append(0)
    c = np.zeros(nv); c[:n3] = -edges_cnt
    return linprog(c, A_ub=np.array(Aub) if Aub else None, b_ub=np.array(bub) if bub else None,
                   A_eq=np.array(Aeq), b_eq=np.array(beq), bounds=(0, None), method="highs")
cuts = []; last = 1
for it in range(80):
    r = solve(cuts); xg = r.x[:n3]; worst = 0
    for s in (0, 1):
        M = np.einsum('g,gpq->pq', xg, Mlin[:, s]); w, V = np.linalg.eigh(M)
        for i in range(T):
            if w[i] < -1e-10: cuts.append((s, V[:, i].copy())); worst = min(worst, w[i])
    if it % 10 == 0: print(it, -r.fun, worst, len(cuts), flush=True)
    if worst > -1e-10 or abs(last + r.fun) < 1e-9 and it > 20: break
    last = -r.fun
print("coupled" if COUPLE else "uncoupled", "bound:", -r.fun)
mu = r.x[n3 + n4:]; print("mu support:", [(round(ds[i], 4), round(mu[i], 4)) for i in range(grid) if mu[i] > 1e-6])
