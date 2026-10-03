"""Vectorised version of q4lp.py (same relaxation; see that file for the block definitions)."""
import numpy as np, itertools, time, sys, pickle
from math import comb
from scipy.optimize import linprog
import scipy.sparse as sp
from q4enum import *

USE = set(sys.argv[1].split(",")) if len(sys.argv) > 1 else {"V", "VL", "E", "S"}
TAG = sys.argv[2] if len(sys.argv) > 2 else "run"
MAXOUT = int(sys.argv[3]) if len(sys.argv) > 3 else 60
TBUDGET = float(sys.argv[4]) if len(sys.argv) > 4 else 900.0
INNER = int(sys.argv[5]) if len(sys.argv) > 5 else 30
NADD = int(sys.argv[6]) if len(sys.argv) > 6 else 1500

P = pairs()
T = build_component_tables()
POP16 = np.array([bin(x).count("1") for x in range(1 << 16)])
TV = np.array([[ta, tb] for ta, tb, tm in T['V']]); TVm = np.array([tm for _, _, tm in T['V']])
TE_ = np.array([[ta, tb] for ta, tb, tm in T['E']]); TEm = np.array([tm for _, _, tm in T['E']])
TS = np.array([[ta, tb] for ta, tb, tm in T['S']]); TSm = np.array([tm for _, _, tm in T['S']])

pv_all = np.arange(1 << 16)
vb = np.array([(pv_all >> j) & 1 for j in range(4)])            # 4 x 65536
def sec(j, l): return (pv_all >> (4 + PIDX[(j, l)])) & 1
vq = {(j, l): vb[j] + 2 * vb[l] + 4 * sec(j, l) + 8 * sec(l, j) for (j, l) in ORD}
vdeg = vb.sum(0)
PERM4 = list(itertools.permutations(range(4)))
pe_all = np.arange(1 << 10)
es = pe_all & 1
et = [(pe_all >> (1 + 3 * k)) & 7 for k in range(3)]
def swp(t): return ((t >> 1) & 1) | ((t & 1) << 1) | (t & 4)
et_sw = [swp(t) for t in et]
PERM3 = list(itertools.permutations(range(3)))

def d4():
    gs = []
    for refl in (0, 1):
        for rot in range(4):
            if refl == 0:
                gs.append((lambda k, rot=rot: (k + rot) % 4, lambda k, rot=rot: (k + rot) % 4))
            else:
                gs.append((lambda k, rot=rot: (-k + rot) % 4, lambda k, rot=rot: (-k - 1 + rot) % 4))
    return gs
G8 = d4()
gr = np.zeros((8, 16), dtype=np.int64); gt = np.zeros((8, 256), dtype=np.int64)
for g, (cm, em) in enumerate(G8):
    for r in range(16):
        gr[g, r] = sum(((r >> k) & 1) << em(k) for k in range(4))
    for t in range(256):
        gt[g, t] = sum(((t >> k) & 1) << cm(k) for k in range(4)) | sum(((t >> (4 + k)) & 1) << (4 + em(k)) for k in range(4))

# per-vertex-pattern index lists (entries into flat V (18x18), VL (16x2x2))
V_idx = []; V_w = []
for (i, i2) in ORD:
    V_idx.append(vb[i] * 18 + vb[i2]); V_w.append(1 / (16 * 12))
for (j, l, i, i2) in PERM4:
    q = vq[(j, l)]
    V_idx.append(vb[i] * 18 + 2 + q); V_w.append(1 / (16 * 24))
    V_idx.append((2 + q) * 18 + vb[i]); V_w.append(1 / (16 * 24))
    V_idx.append((2 + q) * 18 + 2 + vq[(i, i2)]); V_w.append(1 / (16 * 24))
V_idx = np.array(V_idx); V_w = np.array(V_w)                     # 84 x 65536
VL_idx = np.array([vq[(j, l)] * 4 + vb[i] * 2 + vb[i2] for (j, l, i, i2) in PERM4])   # 24 x 65536
E_idx = []
for tt in (et, et_sw):
    for pr in PERM3:
        E_idx.append(es * 512 + tt[pr[0]] * 64 + tt[pr[1]] * 8 + tt[pr[2]])
E_idx = np.array(E_idx)                                           # 12 x 1024
def S_entries(ps):
    r = ps & 15; t1 = (ps >> 4) & 255; t2 = (ps >> 12) & 255
    out = []
    for g in range(8):
        R, A_, B_ = gr[g][r], gt[g][t1], gt[g][t2]
        out.append(R * 65536 + A_ * 256 + B_); out.append(R * 65536 + B_ * 256 + A_)
    return np.stack(out, -1)                                      # (..., 16)

def batch_stats(ids):
    ids = np.array(ids); a, b, m = ids[:, 0], ids[:, 1], ids[:, 2]
    N = len(ids)
    pv = TV[:, 0][:, a].T | TV[:, 1][:, b].T | TVm[:, m].T       # N x 16
    pe = TE_[:, 0][:, a].T | TE_[:, 1][:, b].T | TEm[:, m].T     # N x 32
    ps = TS[:, 0][:, a].T | TS[:, 1][:, b].T | TSm[:, m].T       # N x 24
    rho = (pe & 1).sum(1) / 32.0
    H = np.zeros((N, 5)); np.add.at(H, (np.repeat(np.arange(N), 16), vdeg[pv].ravel()), 1 / 16)
    SV = np.zeros((N, 324))
    idx = V_idx[:, pv]                                            # 84 x N x 16
    np.add.at(SV, (np.broadcast_to(np.arange(N)[None, :, None], idx.shape).ravel(), idx.ravel()),
              np.broadcast_to(V_w[:, None, None], idx.shape).ravel())
    SVL = np.zeros((N, 64))
    idx = VL_idx[:, pv]
    np.add.at(SVL, (np.broadcast_to(np.arange(N)[None, :, None], idx.shape).ravel(), idx.ravel()), 1 / (16 * 24))
    SE = np.zeros((N, 1024))
    idx = E_idx[:, pe]
    np.add.at(SE, (np.broadcast_to(np.arange(N)[None, :, None], idx.shape).ravel(), idx.ravel()), 1 / (32 * 12))
    ent = S_entries(ps).reshape(N, -1)                            # N x 384
    SS = sp.csr_matrix((np.full(ent.size, 1 / (24 * 16)), (np.repeat(np.arange(N), ent.shape[1]), ent.ravel())),
                       shape=(N, 1 << 20))
    SS.sum_duplicates()
    return dict(rho=rho, H=H, SV=SV, SVL=SVL, SE=SE, SS=SS)

def cut_vector(cut):
    """returns (block, weight vector) so that coefficient = stats_block @ w"""
    k = cut[0]
    if k == 'V': return 'SV', np.outer(cut[1], cut[1]).ravel()
    if k == 'VL':
        w = np.zeros(64); w[cut[1] * 4:(cut[1] + 1) * 4] = np.outer(cut[2], cut[2]).ravel(); return 'SVL', w
    if k == 'E':
        w = np.zeros((2, 8, 8, 8)); w[cut[1], :, :, cut[2]] = np.outer(cut[3], cut[3]); return 'SE', w.ravel()
    if k == 'S':
        return 'SS', (cut[1], cut[2])
    if k == 'M2':
        w = np.zeros((2, 8, 8, 8)); w[cut[1]] = np.outer(cut[2], cut[2])[:, :, None]; return 'SE', w.ravel()

def coef_matrix(st, cuts):
    N = len(st['rho']); C = np.zeros((len(cuts), N))
    for t, cut in enumerate(cuts):
        blk, w = cut_vector(cut)
        if blk != 'SS':
            C[t] = st[blk] @ w
        else:
            r, v = w
            sub = st['SS'][:, r * 65536:(r + 1) * 65536]
            # coefficient = sum_{a,b} sub[(a,b)] v_a v_b
            coo = sub.tocoo()
            C[t] = np.bincount(coo.row, weights=coo.data * v[coo.col >> 8] * v[coo.col & 255], minlength=N)
    return C

def concat(s1, s2):
    if s1 is None: return s2
    return dict(rho=np.concatenate([s1['rho'], s2['rho']]), H=np.vstack([s1['H'], s2['H']]),
                SV=np.vstack([s1['SV'], s2['SV']]), SVL=np.vstack([s1['SVL'], s2['SVL']]),
                SE=np.vstack([s1['SE'], s2['SE']]), SS=sp.vstack([s1['SS'], s2['SS']]).tocsr())
def subset(s, keep):
    return dict(rho=s['rho'][keep], H=s['H'][keep], SV=s['SV'][keep], SVL=s['SVL'][keep], SE=s['SE'][keep], SS=s['SS'][keep])

def new_cuts(st, x, tol=1e-9, maxper=4):
    MV = (x @ st['SV']).reshape(18, 18); MVL = (x @ st['SVL']).reshape(16, 2, 2); TEn = (x @ st['SE']).reshape(2, 8, 8, 8)
    MS = (st['SS'].T @ x).reshape(16, 256, 256)
    cuts = []; worst = 0.0
    def neg(M):
        idx = np.where(np.abs(M).sum(1) > 1e-14)[0]
        if len(idx) == 0: return []
        w, V = np.linalg.eigh(M[np.ix_(idx, idx)])
        out = []
        for i in range(min(maxper, len(w))):
            if w[i] < -tol:
                vf = np.zeros(len(M)); vf[idx] = V[:, i]; out.append((w[i], vf))
        return out
    if "V" in USE:
        for w, v in neg(MV): cuts.append(('V', v)); worst = min(worst, w)
    if "VL" in USE:
        for c in range(16):
            for w, v in neg(MVL[c]): cuts.append(('VL', c, v)); worst = min(worst, w)
    if "E" in USE:
        for s in range(2):
            for c in range(8):
                for w, v in neg(TEn[s][:, :, c]): cuts.append(('E', s, c, v)); worst = min(worst, w)
    if "M2" in USE:
        for s_ in range(2):
            for w, v in neg(TEn[s_].sum(2)): cuts.append(('M2', s_, v)); worst = min(worst, w)
    if "S" in USE:
        for r in range(16):
            for w, v in neg(MS[r]): cuts.append(('S', r, v)); worst = min(worst, w)
    return cuts, worst

GRID = np.linspace(0, 1, 801)
BIN = np.array([[comb(4, j) * d**j * (1 - d)**(4 - j) for j in range(5)] for d in GRID])

def solve_master(st, C):
    nG = len(st['rho']); nq = len(GRID)
    c = np.zeros(nG + nq); c[:nG] = -st['rho']
    Aeq = np.zeros((7, nG + nq)); beq = np.zeros(7)
    Aeq[0, :nG] = 1; beq[0] = 1; Aeq[1, nG:] = 1; beq[1] = 1
    Aeq[2:7, :nG] = st['H'].T; Aeq[2:7, nG:] = -BIN.T
    if len(C):
        Aub = sp.hstack([sp.csr_matrix(-C), sp.csr_matrix((len(C), nq))]).tocsr()
        return linprog(c, A_ub=Aub, b_ub=np.zeros(len(C)), A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    return linprog(c, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")

def pricing_tables(r, cuts):
    lam_eq = r.eqlin.marginals; lam_ub = r.ineqlin.marginals if cuts else np.zeros(0)
    lam0 = lam_eq[0]; lamh = lam_eq[2:7]
    WV = np.zeros(324); WVL = np.zeros(64); WE = np.zeros(1024); WS = np.zeros((16, 256, 256))
    for lam, cut in zip(lam_ub, cuts):
        if abs(lam) < 1e-15: continue
        blk, w = cut_vector(cut)
        if blk == 'SV': WV += lam * w
        elif blk == 'SVL': WVL += lam * w
        elif blk == 'SE': WE += lam * w
        else: WS[w[0]] += lam * np.outer(w[1], w[1])
    # reduced cost(G) = -rho - lam0 - lamh.H + sum_k lam_k * coef_k(G)
    Vt = -lamh[vdeg] / 16.0 + (WV[V_idx] * V_w[:, None]).sum(0) + WVL[VL_idx].sum(0) / (16 * 24)
    Et = -es / 32.0 + WE[E_idx].sum(0) / (32 * 12)
    St = None
    if np.any(WS != 0):
        St = WS.ravel()[S_entries(np.arange(1 << 20))].sum(-1) / (24 * 16)
    return -lam0, Vt, Et, St, (lam0, lamh, WV, WVL, WE, WS)

def price(const, Vt, Et, St, K=40):
    best = []; gmin = np.inf
    for a, Bs in P:
        F = a & Bs
        ok = (insidemask[None, :] & F[:, None]) == 0
        cost = np.full((len(Bs), 256), const)
        for ta, tb, tm in T['V']: cost += Vt[ta[a] | tb[Bs][:, None] | tm[None, :]]
        for ta, tb, tm in T['E']: cost += Et[ta[a] | tb[Bs][:, None] | tm[None, :]]
        if St is not None:
            for ta, tb, tm in T['S']: cost += St[ta[a] | tb[Bs][:, None] | tm[None, :]]
        cost[~ok] = np.inf
        flat = cost.ravel(); gmin = min(gmin, flat.min())
        kk = min(K, flat.size)
        idx = np.argpartition(flat, kk - 1)[:kk]
        for t in idx:
            if flat[t] < -1e-9: best.append((flat[t], a, int(Bs[t // 256]), int(t % 256)))
    best.sort()
    return best, gmin

if __name__ == "__main__":
    t0 = time.time()
    fA, fB, fM = T['mask']
    star = [sum(1 << E(v, v ^ (1 << j)) for j in range(4)) for v in range(16)]
    seen = {}
    for a, Bs in P:
        F = a & Bs
        ok = (insidemask[None, :] & F[:, None]) == 0
        mask = fA[a] | fB[Bs][:, None] | fM[None, :]
        code = np.zeros(mask.shape, dtype=np.int64)
        for v in range(16):
            mv = mask & star[v]; code += 17 ** (POP16[mv & 0xFFFF] + POP16[mv >> 16])
        code[~ok] = -1
        u, first = np.unique(code.ravel(), return_index=True)
        for cd, t in zip(u.tolist(), first.tolist()):
            if cd >= 0 and cd not in seen: seen[cd] = (a, int(Bs[t // 256]), int(t % 256))
    colids = list(seen.values()); keys = set(colids)
    st = batch_stats(colids)
    cuts = []; C = np.zeros((0, len(colids)))
    print("seed", len(colids), time.time() - t0, flush=True)
    history = []
    for outer in range(MAXOUT):
        for inner in range(INNER):
            r = solve_master(st, C)
            x = r.x[:len(colids)]
            nc, worst = new_cuts(st, x)
            if not nc: break
            C = np.vstack([C, coef_matrix(st, nc)]); cuts += nc
        val = -r.fun
        const, Vt, Et, St, duals = pricing_tables(r, cuts)
        best, gmin = price(const, Vt, Et, St)
        history.append((val, gmin, len(colids), len(cuts)))
        print(f"outer {outer}: LP {val:.6f} worst {worst:.1e} cols {len(colids)} cuts {len(cuts)} min_rc {gmin:.3e} t {time.time()-t0:.0f}s", flush=True)
        if gmin > -1e-7 or time.time() - t0 > TBUDGET:
            break
        newids = [(a, b, m) for rc, a, b, m in best[:NADD] if (a, b, m) not in keys]
        if newids:
            sn = batch_stats(newids)
            Cn = coef_matrix(sn, cuts) if cuts else np.zeros((0, len(newids)))
            st = concat(st, sn); C = np.hstack([C, Cn]); colids += newids; keys.update(newids)
        # prune (reduced costs computed with the duals of the last solve, before pruning cuts)
        lam = r.ineqlin.marginals if len(cuts) else np.zeros(0)
        if len(colids) > 8000:
            rcc = -st['rho'] - r.eqlin.marginals[0] - st['H'] @ r.eqlin.marginals[2:7]
            if len(lam): rcc = rcc + lam @ C
            xs = np.concatenate([x, np.zeros(len(colids) - len(x))])
            order = np.argsort(rcc)
            keep = np.sort(np.union1d(np.where(xs > 1e-12)[0], order[:6000]))
            st = subset(st, keep); C = C[:, keep]; colids = [colids[i] for i in keep]; keys = set(colids)
        if len(cuts) > 400:
            keepc = np.where(np.abs(lam) > 1e-13)[0]
            cuts = [cuts[i] for i in keepc]; C = C[keepc]
    pickle.dump(dict(history=history, cuts=cuts, val=val, x=r.x, colids=colids, USE=USE, duals=duals, gmin=gmin),
                open(f"res_{TAG}.pkl", "wb"))
    print("FINAL", sorted(USE), "LP", val, "min reduced cost over ALL Q4 graphs", gmin, flush=True)
