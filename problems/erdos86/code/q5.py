"""ex(Q5,C4) by Q5 = Q4 x K2:  a C4-free subgraph is (A,B,M), A,B C4-free in Q4, M independent in A&B.
|G| = |A|+|B|+|M|.  57 edges would need |A|+|B| - nu(A&B) >= 41, and nu >= |A&B|/4 >= (|A|+|B|-32)/4,
so |A|+|B| >= 44 and |A|,|B| >= 20.  We enumerate all labelled C4-free Q4 graphs with >= 20 edges,
take A among Aut(Q4)-orbit representatives of the larger class, B over all labelled graphs, and compute
alpha(A&B) exactly (16-vertex bipartite graph)."""
import numpy as np, itertools, time
from cube import cube, c4free_masks
E3, eidx3, sq3 = cube(3); E4, eidx4, sq4 = cube(4)
L3 = np.array(c4free_masks(3), dtype=np.int64)
pc12 = np.array([bin(x).count("1") for x in range(1 << 12)])
endmask3 = [(1 << a) | (1 << b) for (a, b, _) in E3]
insidemask = np.array([sum(1 << e for e in range(12) if (S & endmask3[e]) == endmask3[e]) for S in range(256)])
sizeS = np.array([bin(S).count("1") for S in range(256)])
bits12 = (np.arange(4096)[:, None] >> np.arange(12)[None, :]) & 1
bits8 = (np.arange(256)[:, None] >> np.arange(8)[None, :]) & 1
lay0 = [eidx4[(a, b)] for (a, b, _) in E3]; lay1 = [eidx4[(a + 8, b + 8)] for (a, b, _) in E3]
vert = [eidx4[(x, x + 8)] for x in range(8)]
fA = (bits12 << np.array(lay0)).sum(1); fB = (bits12 << np.array(lay1)).sum(1); fM = (bits8 << np.array(vert)).sum(1)

t0 = time.time()
masks = {k: [] for k in range(20, 25)}
for A in L3:
    I = A & L3
    base = pc12[A] + pc12[L3]
    for k in range(9):
        need = 20 - base   # need |M| >= need
        ok = (insidemask[None, :] & I[:, None]) == 0
        sel = ok & (sizeS[None, :] + base[:, None] >= 20)
        break
    ib, im = np.where(sel)
    mm = fA[A] | fB[L3[ib]] | fM[im]
    ecount = base[ib] + sizeS[im]
    for k in range(20, 25):
        masks[k].append(mm[ecount == k])
masks = {k: np.concatenate(v) for k, v in masks.items()}
print({k: len(v) for k, v in masks.items()}, "t", round(time.time() - t0, 1))

# Aut(Q4) on edges
auts = []
for p in itertools.permutations(range(4)):
    for flip in range(16):
        f = lambda v, p=p, flip=flip: sum(((v >> i) & 1) << p[i] for i in range(4)) ^ flip
        auts.append([eidx4[(min(f(a), f(b)), max(f(a), f(b)))] for (a, b, _) in E4])
auts = np.array(auts)  # 384 x 32
def canon(ms):
    bits = (ms[:, None] >> np.arange(32)[None, :]) & 1
    best = None
    for perm in auts:
        img = (bits << perm[None, :]).sum(1)
        best = img if best is None else np.minimum(best, img)
    return best
reps = {k: np.unique(canon(masks[k])) for k in (22, 23, 24)}
print("orbit reps:", {k: len(v) for k, v in reps.items()}, "t", round(time.time() - t0, 1))

# alpha of A&B: bipartite, X = even vertices. N(S) for S subset of X via neighbour masks over Y.
X = [v for v in range(16) if bin(v).count("1") % 2 == 0]; Y = [v for v in range(16) if bin(v).count("1") % 2 == 1]
ypos = {v: i for i, v in enumerate(Y)}
# for each edge index e: (x-index, y-bit)
exy = []
for (a, b, _) in E4:
    x, y = (a, b) if a in X else (b, a)
    exy.append((X.index(x), 1 << ypos[y]))
def alpha(H):
    """H: array of 32-bit edge masks; returns independence numbers."""
    nb = np.zeros((len(H), 8), dtype=np.int64)
    for e, (xi, yb) in enumerate(exy):
        nb[:, xi] |= ((H >> e) & 1) * yb
    NS = np.zeros((len(H), 256), dtype=np.int64)
    for S in range(1, 256):
        low = (S & -S).bit_length() - 1
        NS[:, S] = NS[:, S & (S - 1)] | nb[:, low]
    popc8 = sizeS
    return (sizeS[None, :] + 8 - popc8[NS]).max(1)

best = 0; n56 = 0; ex56 = None
cases = [(24, b) for b in (20, 21, 22, 23, 24)] + [(23, b) for b in (21, 22, 23)] + [(22, 22)]
for ka, kb in cases:
    for A in reps[ka]:
        Bs = masks[kb]
        for chunk in range(0, len(Bs), 200000):
            Bc = Bs[chunk:chunk + 200000]
            al = alpha(A & Bc)
            tot = ka + kb + al
            m = tot.max()
            if m > best: best = m
            if m >= 56 and ex56 is None:
                ex56 = (int(A), int(Bc[np.argmax(tot)]))
    print("case", ka, kb, "max so far", best, "t", round(time.time() - t0, 1), flush=True)
print("max |A|+|B|+alpha(A&B) over pairs with |A|+|B|>=44:", best)
print("example 56-edge pair (A,B masks):", ex56)
