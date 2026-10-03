import numpy as np, time
from q4enum import *
P = pairs(); T = build_component_tables()
fA, fB, fM = T['mask']
rng = np.random.default_rng(1)
bad = 0
for trial in range(300):
    a, Bs = P[rng.integers(len(P))]
    b = Bs[rng.integers(len(Bs))]
    okM = [m for m in range(256) if (insidemask[m] & a & b) == 0]
    m = okM[rng.integers(len(okM))]
    mask = int(fA[a] | fB[b] | fM[m])
    for key, PATS in (('V', VPAT), ('E', EPAT), ('S', SPAT)):
        for (ta, tb, tm), pat in zip(T[key], PATS):
            val = int(ta[a] | tb[b] | tm[m])
            direct = sum(((mask >> e) & 1) << pos for pos, e in enumerate(pat))
            bad += val != direct
print("pattern mismatches:", bad)
a, Bs = P[50]
print(len(Bs), max(len(b) for _, b in P))
t = time.time()
idx = T['S'][3][0][a] | T['S'][3][1][Bs][:, None] | T['S'][3][2][None, :]
print(idx.shape, idx.max(), time.time() - t)
