"""Q4 = Q3 x K2.  A C4-free subgraph of Q4 is (A,B,M): A,B C4-free in the two Q3 layers,
M = set of Q3-vertices whose vertical edge is present; the vertical squares force
M to be an independent set of the graph A&B (on the 8 vertices of Q3)."""
import numpy as np, itertools, sys
from cube import cube, c4free_masks

E3, eidx3, sq3 = cube(3)
L3 = np.array(c4free_masks(3), dtype=np.int64)
pc = np.array([bin(x).count("1") for x in range(1 << 12)])

# independent sets of each 12-bit edge set on 8 vertices
endmask = np.array([(1 << a) | (1 << b) for (a, b, _) in E3])
subsets = np.arange(256)
# for each subset S and edge e: edge inside S?
inside = np.array([[((S & m) == m) for m in endmask] for S in subsets])  # 256 x 12
insidemask = np.array([sum(1 << e for e in range(12) if inside[S, e]) for S in subsets])  # 256
indep_ok = lambda F: (insidemask & F) == 0  # vector over subsets
nind = np.zeros(1 << 12, dtype=np.int64); alpha = np.zeros(1 << 12, dtype=np.int64)
sizeS = np.array([bin(S).count("1") for S in subsets])
for F in range(1 << 12):
    ok = (insidemask & F) == 0
    nind[F] = ok.sum(); alpha[F] = sizeS[ok].max()

tot = 0; best = 0; nbest = 0
for A in L3:
    I = A & L3
    tot += nind[I].sum()
    val = pc[A] + pc[L3] + alpha[I]
    m = val.max()
    if m > best:
        best = m; nbest = 0
    if m == best:
        # count labelled extremal graphs = number of max-size independent sets achieving
        for B, Ii in zip(L3[val == best], I[val == best]):
            ok = (insidemask & Ii) == 0
            nbest += int((sizeS[ok] == alpha[Ii]).sum())
print("Q4: #C4-free subgraphs =", tot, " ex =", best, " #labelled extremal =", nbest)
