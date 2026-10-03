"""Enumeration of C4-free subgraphs of Q4 up to symmetry, as (A,B,M): Q4 = Q3 x K2 (bit 3 vertical).
A = Aut(Q3)-orbit representative, B = Stab(A)-orbit representative with orbit(B) >= orbit(A),
M = independent set of A&B.  Every C4-free Q4 graph is isomorphic to one of these.
Patterns: a pattern is an ordered list of Q4 edges; its value on a graph is the bit-vector of those edges.
Each pattern value = fA[A] | fB[B] | fM[M] (precomputed per component)."""
import numpy as np, itertools
from cube import cube, c4free_masks

E3, eidx3, sq3 = cube(3)
E4, eidx4, sq4 = cube(4)
L3 = np.array(c4free_masks(3), dtype=np.int64)
NL3 = len(L3)

def q3_auts():
    auts = []
    for p in itertools.permutations(range(3)):
        for flip in range(8):
            def f(v, p=p, flip=flip):
                w = 0
                for i in range(3):
                    if (v >> i) & 1: w |= 1 << p[i]
                return w ^ flip
            auts.append([f(v) for v in range(8)])
    return auts
AUT3 = q3_auts()
def edge_perm(vperm):
    out = []
    for (a, b, _) in E3:
        fa, fb = vperm[a], vperm[b]
        out.append(eidx3[(min(fa, fb), max(fa, fb))])
    return out
EP3 = [edge_perm(a) for a in AUT3]
# apply edge perms to all 4096 masks quickly
bits12 = (np.arange(4096)[:, None] >> np.arange(12)[None, :]) & 1
def apply_all(ep):
    w = np.zeros(4096, dtype=np.int64)
    for e in range(12):
        w |= bits12[:, e] << ep[e]
    return w
IMG = np.array([apply_all(ep) for ep in EP3])   # 48 x 4096
canon_all = IMG.min(axis=0)
orbit_reps = sorted(set(canon_all[L3].tolist()))
orbit_index = {c: i for i, c in enumerate(orbit_reps)}
oidx_L3 = np.array([orbit_index[canon_all[x]] for x in L3])
inL3 = np.full(4096, -1); inL3[L3] = np.arange(NL3)

def stab(a):
    return [g for g in range(48) if IMG[g, a] == a]

def pairs():
    """list of (A, array of B masks)"""
    out = []
    for a in orbit_reps:
        S = stab(a)
        ia = orbit_index[a]
        cand = L3[oidx_L3 >= ia]
        # Stab(a)-orbit reps of cand
        imgs = IMG[np.ix_(S, cand)]           # |S| x nc
        reps = np.unique(imgs.min(axis=0))
        out.append((a, reps))
    return out

# Q4 edge index of Q3 edge t in layer 0 / layer 1, and vertical edge at x
lay0 = [eidx4[(a, b)] for (a, b, _) in E3]
lay1 = [eidx4[(a + 8, b + 8)] for (a, b, _) in E3]
vert = [eidx4[(x, x + 8)] for x in range(8)]
endmask3 = [(1 << a) | (1 << b) for (a, b, _) in E3]
insidemask = np.array([sum(1 << e for e in range(12) if (S & endmask3[e]) == endmask3[e]) for S in range(256)])
bits8 = (np.arange(256)[:, None] >> np.arange(8)[None, :]) & 1

def comp_tables(pattern):
    """pattern: list of Q4 edge indices. returns fA[4096], fB[4096], fM[256] (int64)."""
    fA = np.zeros(4096, dtype=np.int64); fB = np.zeros(4096, dtype=np.int64); fM = np.zeros(256, dtype=np.int64)
    for pos, e in enumerate(pattern):
        if e in lay0:
            fA |= bits12[:, lay0.index(e)] << pos
        elif e in lay1:
            fB |= bits12[:, lay1.index(e)] << pos
        else:
            fM |= bits8[:, vert.index(e)] << pos
    return fA, fB, fM

def full_mask_tables():
    fA = np.zeros(4096, dtype=np.int64); fB = np.zeros(4096, dtype=np.int64); fM = np.zeros(256, dtype=np.int64)
    for t in range(12):
        fA |= bits12[:, t] << lay0[t]
        fB |= bits12[:, t] << lay1[t]
    for x in range(8):
        fM |= bits8[:, x] << vert[x]
    return fA, fB, fM

def E(a, b):
    return eidx4[(min(a, b), max(a, b))]

# ---------- pattern definitions ----------
# (V) vertex patterns: 4 star bits (dir j at bit j) + 12 second-level bits: for ordered (j,l), j!=l: edge (v^ej, v^ej^el) at bit 4+PIDX[(j,l)]
ORD = [(j, l) for j in range(4) for l in range(4) if j != l]
PIDX = {p: i for i, p in enumerate(ORD)}
VPAT = []
for v in range(16):
    pat = [E(v, v ^ (1 << j)) for j in range(4)]
    pat += [E(v ^ (1 << j), v ^ (1 << j) ^ (1 << l)) for (j, l) in ORD]
    VPAT.append(pat)
# (Ed) edge patterns: s, then for each other dir j (increasing): bu, bv, bt
EPAT = []
for (u, v, i) in E4:
    pat = [E(u, v)]
    for j in range(4):
        if j == i: continue
        pat += [E(u, u ^ (1 << j)), E(v, v ^ (1 << j)), E(u ^ (1 << j), v ^ (1 << j))]
    EPAT.append(pat)
# (S) square patterns: corners c0=u, c1=u+ei, c2=u+ei+ej, c3=u+ej ; root edges r_k=(c_k,c_{k+1});
# for extra dirs l<m: 4 vertical bits (c_k, c_k+e_l), then 4 top bits (c_k+e_l, c_{k+1}+e_l)
SPAT = []
for u in range(16):
    for i in range(4):
        for j in range(i + 1, 4):
            if (u >> i) & 1 or (u >> j) & 1: continue
            c = [u, u ^ (1 << i), u ^ (1 << i) ^ (1 << j), u ^ (1 << j)]
            pat = [E(c[k], c[(k + 1) % 4]) for k in range(4)]
            for l in range(4):
                if l in (i, j): continue
                pat += [E(c[k], c[k] ^ (1 << l)) for k in range(4)]
                pat += [E(c[k] ^ (1 << l), c[(k + 1) % 4] ^ (1 << l)) for k in range(4)]
            SPAT.append(pat)
assert len(VPAT) == 16 and len(EPAT) == 32 and len(SPAT) == 24

def build_component_tables():
    T = {}
    T['V'] = [comp_tables(p) for p in VPAT]
    T['E'] = [comp_tables(p) for p in EPAT]
    T['S'] = [comp_tables(p) for p in SPAT]
    T['mask'] = full_mask_tables()
    return T

if __name__ == "__main__":
    import time
    t0 = time.time()
    P = pairs()
    npairs = sum(len(b) for _, b in P)
    tot = 0
    for a, Bs in P:
        F = a & Bs
        ok = (insidemask[None, :] & F[:, None]) == 0
        tot += ok.sum()
    print("pairs", npairs, "graphs (A,B,M)", tot, "time", time.time() - t0)
    T = build_component_tables()
    print("tables built", time.time() - t0)
    # timing test of a pricing pass with random tables
    rng = np.random.default_rng(0)
    tv = rng.random(1 << 16); te = rng.random(1 << 10); ts = rng.random(1 << 20)
    t1 = time.time(); best = -1e9
    for a, Bs in P:
        F = a & Bs
        ok = (insidemask[None, :] & F[:, None]) == 0
        cost = np.zeros((len(Bs), 256))
        for key, tab in (('V', tv), ('E', te), ('S', ts)):
            for fA, fB, fM in T[key]:
                idx = fA[a] | fB[Bs][:, None] | fM[None, :]
                cost += tab[idx]
        cost[~ok] = -np.inf
        best = max(best, cost.max())
    print("pricing pass time", time.time() - t1)
