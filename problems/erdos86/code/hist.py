"""Achievable degree histograms of C4-free subgraphs of Q3 and Q4, and the LP
   max rho s.t.  sum_h lam_h h/2^k = int Bin(k,delta) dmu(delta),  rho = int delta dmu."""
import numpy as np, itertools
from scipy.optimize import linprog
from cube import cube, c4free_masks

E3, eidx3, sq3 = cube(3)
L3 = np.array(c4free_masks(3), dtype=np.int64)
pc = np.array([bin(x).count("1") for x in range(1 << 12)])

def autQ3_edge_perms():
    perms = []
    for p in itertools.permutations(range(3)):
        for flip in range(8):
            def f(v):
                w = 0
                for i in range(3):
                    if (v >> i) & 1: w |= 1 << p[i]
                return w ^ flip
            perm = []
            for (a, b, _) in E3:
                fa, fb = f(a), f(b)
                perm.append(eidx3[(min(fa, fb), max(fa, fb))])
            perms.append(perm)
    return perms
P3 = autQ3_edge_perms()
def apply(perm, x):
    y = 0
    for e in range(12):
        if (x >> e) & 1: y |= 1 << perm[e]
    return y
canon = {}
reps = []
for x in L3:
    x = int(x)
    c = min(apply(p, x) for p in P3)
    if c not in canon:
        canon[c] = 1; reps.append(c)
print("Q3 C4-free orbits under Aut(Q3):", len(reps))

# degrees in Q3 of each edge mask
deg3 = np.zeros((1 << 12, 8), dtype=np.int64)
for t, (a, b, _) in enumerate(E3):
    bit = (np.arange(1 << 12) >> t) & 1
    deg3[:, a] += bit; deg3[:, b] += bit
endmask = [(1 << a) | (1 << b) for (a, b, _) in E3]
insidemask = np.array([sum(1 << e for e in range(12) if (S & endmask[e]) == endmask[e]) for S in range(256)])
mbit = np.array([[(S >> x) & 1 for x in range(8)] for S in range(256)])

def hist_code(degs, base=17):
    return (base ** degs).sum(axis=-1)

# Q3 histograms
H3 = set()
for x in L3:
    H3.add(tuple(np.bincount(deg3[x], minlength=4)))
H3 = np.array(sorted(H3))
print("Q3 distinct degree histograms:", len(H3))

# Q4 histograms
codes = set()
pow17 = 17 ** np.arange(5)
for A in reps:
    dA = deg3[A]                         # 8
    dB = deg3[L3]                        # nB x 8
    ok = (insidemask[None, :] & (A & L3)[:, None]) == 0   # nB x 256
    c = pow17[dA[None, None, :] + mbit[None, :, :]].sum(-1) + pow17[dB[:, None, :] + mbit[None, :, :]].sum(-1)
    codes.update(np.unique(c[ok]).tolist())
H4 = []
for c in codes:
    h = []
    for d in range(5):
        h.append(c % 17); c //= 17
    H4.append(h)
H4 = np.array(sorted(H4))
print("Q4 distinct degree histograms:", len(H4))
np.save("H3.npy", H3); np.save("H4.npy", H4)

from math import comb
def lp(H, k, grid=2001):
    ds = np.linspace(0, 1, grid)
    B = np.array([[comb(k, m) * d**m * (1 - d)**(k - m) for m in range(k + 1)] for d in ds])  # grid x (k+1)
    nh = len(H); nq = grid
    # variables lam (nh), q (nq)
    Aeq = np.zeros((k + 3, nh + nq)); beq = np.zeros(k + 3)
    Aeq[:k + 1, :nh] = (H / 2**k).T
    Aeq[:k + 1, nh:] = -B.T
    Aeq[k + 1, :nh] = 1; beq[k + 1] = 1
    Aeq[k + 2, nh:] = 1; beq[k + 2] = 1
    cobj = np.zeros(nh + nq); cobj[nh:] = -ds
    r = linprog(cobj, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    q = r.x[nh:]
    supp = [(round(ds[i], 4), round(q[i], 4)) for i in range(nq) if q[i] > 1e-7]
    lam = r.x[:nh]
    hs = [(tuple(H[i]), round(lam[i], 4)) for i in range(nh) if lam[i] > 1e-7]
    return -r.fun, supp, hs, r

for k, H in ((3, H3), (4, H4)):
    val, supp, hs, r = lp(H, k)
    print(f"k={k}: LP bound {val:.6f}; delta support {supp}; histograms {hs}")
