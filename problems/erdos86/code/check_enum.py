import numpy as np, time
from q4enum import *
P = pairs()
T = build_component_tables()
fA, fB, fM = T['mask']
POP = np.array([bin(x).count("1") for x in range(1 << 16)])
star = [sum(1 << E(v, v ^ (1 << j)) for j in range(4)) for v in range(16)]
H = set(); best = 0; n = 0
t = time.time()
for a, Bs in P:
    F = a & Bs
    ok = (insidemask[None, :] & F[:, None]) == 0
    mask = (fA[a] | fB[Bs][:, None] | fM[None, :])[ok]
    n += len(mask)
    ec = POP[mask & 0xFFFF] + POP[mask >> 16]
    best = max(best, ec.max())
    code = np.zeros(len(mask), dtype=np.int64)
    for v in range(16):
        dv = POP[(mask & star[v]) & 0xFFFF] + POP[(mask & star[v]) >> 16]
        code += 17 ** dv
    H.update(np.unique(code).tolist())
print("graphs", n, "max edges", best, "distinct hist", len(H), time.time() - t)
H4 = np.load("H4.npy")
H4codes = set(int(sum(h[d] * 17**d for d in range(5))) for h in H4)
print("same histogram set as before:", H4codes == H)
# timing of one gather op
rng = np.random.default_rng(0); ts = rng.random(1 << 20)
idx = rng.integers(0, 1 << 20, size=10**7)
t = time.time(); s = ts[idx]; print("1e7 random gathers:", time.time() - t)
