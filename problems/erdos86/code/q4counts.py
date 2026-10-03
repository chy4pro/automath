import numpy as np
from cube import cube, c4free_masks
E3, eidx3, sq3 = cube(3)
L3 = np.array(c4free_masks(3), dtype=np.int64)
pc = np.array([bin(x).count("1") for x in range(1 << 12)])
endmask = [(1 << a) | (1 << b) for (a, b, _) in E3]
insidemask = np.array([sum(1 << e for e in range(12) if (S & endmask[e]) == endmask[e]) for S in range(256)])
sizeS = np.array([bin(S).count("1") for S in range(256)])
# indpoly[F][k] = # independent sets of size k in graph F
indpoly = np.zeros((4096, 9), dtype=np.int64)
for F in range(4096):
    ok = (insidemask & F) == 0
    indpoly[F] = np.bincount(sizeS[ok], minlength=9)
cnt = np.zeros(33, dtype=np.int64)
for A in L3:
    I = A & L3
    base = pc[A] + pc[L3]
    for k in range(9):
        np.add.at(cnt, base + k, indpoly[I, k])
print({e: int(c) for e, c in enumerate(cnt) if c})
print("total", cnt.sum(), " with >=20 edges:", cnt[20:].sum())
