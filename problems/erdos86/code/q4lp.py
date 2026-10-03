"""Q4-level relaxation by column generation + PSD cutting planes.
x = distribution on C4-free Q4 graphs (iso classes), mu = mixing measure of vertex densities.
Blocks:
 V : vertex root, flags = (bit of one direction | rooted-square config of an ordered direction pair) -> 18x18 PSD
 VL: vertex root, localising: for each rooted-square config c, 2x2 matrix over bits, PSD
 E : edge root (s = root edge status), flags = square type (bu,bv,btop) of one extra direction;
     third moments T^s[a,b,c]; for each s,c the 8x8 matrix T^s[.,.,c] PSD
 S : square root (config r), flags = prism type (4 vertical + 4 top edges) of one extra direction; 256x256 PSD per r
 H : degree histogram = int Bin(4,delta) dmu
"""
import numpy as np, itertools, time, sys, pickle
from math import comb
from scipy.optimize import linprog
import scipy.sparse as sp
from q4enum import *

USE = set(sys.argv[1].split(",")) if len(sys.argv) > 1 else {"V", "VL", "E", "S"}
TAG = sys.argv[2] if len(sys.argv) > 2 else "run"

P = pairs()
T = build_component_tables()
POP16 = np.array([bin(x).count("1") for x in range(1 << 16)])

# ---------------- per-pattern decoders ----------------
pv_all = np.arange(1 << 16)
vb = [(pv_all >> j) & 1 for j in range(4)]
def sec(j, l): return (pv_all >> (4 + PIDX[(j, l)])) & 1
vq = {(j, l): vb[j] + 2 * vb[l] + 4 * sec(j, l) + 8 * sec(l, j) for (j, l) in ORD}
vdeg = vb[0] + vb[1] + vb[2] + vb[3]
PERM4 = list(itertools.permutations(range(4)))

pe_all = np.arange(1 << 10)
es = pe_all & 1
et = [(pe_all >> (1 + 3 * k)) & 7 for k in range(3)]
def swp(t): return ((t >> 1) & 1) | ((t & 1) << 1) | (t & 4)
et_sw = [swp(t) for t in et]
PERM3 = list(itertools.permutations(range(3)))

# D4 action on 4-bit root config (bit k = r_k) and 8-bit type (bits 0-3 vertical V_k, 4-7 top t_k)
def d4():
    gs = []
    for refl in (0, 1):
        for rot in range(4):
            if refl == 0:
                cmap = lambda k, rot=rot: (k + rot) % 4
                emap = lambda k, rot=rot: (k + rot) % 4
            else:
                cmap = lambda k, rot=rot: (-k + rot) % 4
                emap = lambda k, rot=rot: (-k - 1 + rot) % 4
            gs.append((cmap, emap))
    return gs
G8 = d4()
gr = np.zeros((8, 16), dtype=np.int64); gt = np.zeros((8, 256), dtype=np.int64)
for g, (cm, em) in enumerate(G8):
    for r in range(16):
        gr[g, r] = sum(((r >> k) & 1) << em(k) for k in range(4))
    for t in range(256):
        gt[g, t] = sum(((t >> k) & 1) << cm(k) for k in range(4)) | sum(((t >> (4 + k)) & 1) << (4 + em(k)) for k in range(4))

# ---------------- column statistics ----------------
def col_patterns(a, b, m):
    pv = [int(ta[a] | tb[b] | tm[m]) for (ta, tb, tm) in T['V']]
    pe = [int(ta[a] | tb[b] | tm[m]) for (ta, tb, tm) in T['E']]
    ps = [int(ta[a] | tb[b] | tm[m]) for (ta, tb, tm) in T['S']]
    return pv, pe, ps

def col_stats(a, b, m):
    pv, pe, ps = col_patterns(a, b, m)
    st = {}
    st['rho'] = sum(p & 1 for p in pe) / 32.0
    h = np.zeros(5)
    for p in pv: h[vdeg[p]] += 1 / 16
    st['h'] = h
    MV = np.zeros((18, 18)); MVL = np.zeros((16, 2, 2))
    for p in pv:
        bits = [(p >> j) & 1 for j in range(4)]
        q = {(j, l): int(vq[(j, l)][p]) for (j, l) in ORD}
        for (i, i2) in ORD:
            MV[bits[i], bits[i2]] += 1 / (16 * 12)
        for (j, l, i, i2) in PERM4:
            MV[bits[i], 2 + q[(j, l)]] += 1 / (16 * 24)
            MV[2 + q[(j, l)], bits[i]] += 1 / (16 * 24)
            MV[2 + q[(j, l)], 2 + q[(i, i2)]] += 1 / (16 * 24)
            MVL[q[(j, l)], bits[i], bits[i2]] += 1 / (16 * 24)
    st['V'] = MV; st['VL'] = MVL
    TE = np.zeros((2, 8, 8, 8))
    for p in pe:
        s = p & 1
        ts = [(p >> (1 + 3 * k)) & 7 for k in range(3)]
        for tt in (ts, [swp(t) for t in ts]):
            for pr in PERM3:
                TE[s, tt[pr[0]], tt[pr[1]], tt[pr[2]]] += 1 / (32 * 12)
    st['E'] = TE
    rows = []
    for p in ps:
        r = p & 15; t1 = (p >> 4) & 255; t2 = (p >> 12) & 255
        for g in range(8):
            R, A_, B_ = gr[g, r], gt[g, t1], gt[g, t2]
            rows.append((R, A_, B_)); rows.append((R, B_, A_))
    rows = np.array(rows)
    key = rows[:, 0] * 65536 + rows[:, 1] * 256 + rows[:, 2]
    uk, cnt = np.unique(key, return_counts=True)
    st['S'] = (uk, cnt / (24 * 16))
    return st

# ---------------- cut coefficient for a column ----------------
def cut_coef(st, cut):
    kind = cut[0]
    if kind == 'V':
        v = cut[1]; return v @ st['V'] @ v
    if kind == 'VL':
        c, v = cut[1], cut[2]; return v @ st['VL'][c] @ v
    if kind == 'E':
        s, c, v = cut[1], cut[2], cut[3]; return v @ st['E'][s][:, :, c] @ v
    if kind == 'S':
        r, v = cut[1], cut[2]
        uk, w = st['S']
        sel = (uk >> 16) == r
        return float((w[sel] * v[(uk[sel] >> 8) & 255] * v[uk[sel] & 255]).sum())

# ---------------- aggregated moments at x ----------------
def moments(cols, x):
    MV = np.zeros((18, 18)); MVL = np.zeros((16, 2, 2)); TE = np.zeros((2, 8, 8, 8)); MS = np.zeros((16, 256, 256))
    for st, xv in zip(cols, x):
        if xv <= 1e-12: continue
        MV += xv * st['V']; MVL += xv * st['VL']; TE += xv * st['E']
        uk, w = st['S']
        np.add.at(MS, (uk >> 16, (uk >> 8) & 255, uk & 255), xv * w)
    return MV, MVL, TE, MS

def new_cuts(x, cols, tol=1e-9, maxper=3):
    MV, MVL, TE, MS = moments(cols, x)
    cuts = []; worst = 0.0
    def neg(M):
        w, V = np.linalg.eigh(M)
        return [(w[i], V[:, i]) for i in range(min(maxper, len(w))) if w[i] < -tol]
    if "V" in USE:
        for w, v in neg(MV): cuts.append(('V', v)); worst = min(worst, w)
    if "VL" in USE:
        for c in range(16):
            for w, v in neg(MVL[c]): cuts.append(('VL', c, v)); worst = min(worst, w)
    if "E" in USE:
        for s in range(2):
            for c in range(8):
                for w, v in neg(TE[s][:, :, c]): cuts.append(('E', s, c, v)); worst = min(worst, w)
    if "S" in USE:
        for r in range(16):
            M = MS[r]
            idx = np.where(np.abs(M).sum(1) > 0)[0]
            if len(idx) == 0: continue
            for w, v in neg(M[np.ix_(idx, idx)]):
                vf = np.zeros(256); vf[idx] = v
                cuts.append(('S', r, vf)); worst = min(worst, w)
    return cuts, worst

# ---------------- master LP ----------------
GRID = np.linspace(0, 1, 401)
BIN = np.array([[comb(4, j) * d**j * (1 - d)**(4 - j) for j in range(5)] for d in GRID])

def solve_master(cols, cuts, coef):
    nG = len(cols); nq = len(GRID)
    c = np.zeros(nG + nq); c[:nG] = -np.array([st['rho'] for st in cols])
    Aeq = np.zeros((7, nG + nq)); beq = np.zeros(7)
    Aeq[0, :nG] = 1; beq[0] = 1
    Aeq[1, nG:] = 1; beq[1] = 1
    H = np.array([st['h'] for st in cols])
    Aeq[2:7, :nG] = H.T; Aeq[2:7, nG:] = -BIN.T
    if cuts:
        Aub = np.zeros((len(cuts), nG + nq)); Aub[:, :nG] = -coef[:, :nG]
        r = linprog(c, A_ub=sp.csr_matrix(Aub), b_ub=np.zeros(len(cuts)), A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    else:
        r = linprog(c, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    return r

# ---------------- pricing ----------------
def pricing_tables(r, cuts, coef):
    lam_eq = r.eqlin.marginals
    lam_ub = r.ineqlin.marginals if cuts else np.zeros(0)
    lam0 = lam_eq[0]; lamh = lam_eq[2:7]
    WV = np.zeros((18, 18)); WVL = np.zeros((16, 2, 2)); WE = np.zeros((2, 8, 8, 8)); WS = np.zeros((16, 256, 256))
    for lam, cut in zip(lam_ub, cuts):
        if abs(lam) < 1e-15: continue
        k = cut[0]
        if k == 'V': WV += lam * np.outer(cut[1], cut[1])
        elif k == 'VL': WVL[cut[1]] += lam * np.outer(cut[2], cut[2])
        elif k == 'E': WE[cut[1], :, :, cut[2]] += lam * np.outer(cut[3], cut[3])
        elif k == 'S': WS[cut[1]] += lam * np.outer(cut[2], cut[2])
    # reduced cost = -rho - lam0 - lamh.h + sum lam_k a_k   (a_k = cut coefficient, cut row is -a_k x <= 0, so + lam*a)
    # careful: row is (-a_k) x <= 0, reduced = c - A^T lam = -rho - lam0 - lamh.h - sum lam_k (-a_k)
    Vt = -lamh[vdeg] / 16.0
    acc = np.zeros(1 << 16)
    for (i, i2) in ORD: acc += WV[vb[i], vb[i2]] / 12
    for (j, l, i, i2) in PERM4:
        q = vq[(j, l)]
        acc += 2 * WV[vb[i], 2 + q] / 24
        acc += WV[2 + q, 2 + vq[(i, i2)]] / 24
        acc += WVL[q, vb[i], vb[i2]] / 24
    Vt += acc / 16.0
    Et = -es / 32.0
    acc = np.zeros(1 << 10)
    for tt in (et, et_sw):
        for pr in PERM3:
            acc += WE[es, tt[pr[0]], tt[pr[1]], tt[pr[2]]] / 12
    Et += acc / 32.0
    St = None
    if np.any(WS != 0):
        ps_all = np.arange(1 << 20)
        rr = ps_all & 15; t1 = (ps_all >> 4) & 255; t2 = (ps_all >> 12) & 255
        St = np.zeros(1 << 20)
        for g in range(8):
            R, A_, B_ = gr[g][rr], gt[g][t1], gt[g][t2]
            St += WS[R, A_, B_] + WS[R, B_, A_]
        St /= (24 * 16)
    return -lam0, Vt, Et, St

def price(const, Vt, Et, St, K=300):
    best = []
    for a, Bs in P:
        F = a & Bs
        ok = (insidemask[None, :] & F[:, None]) == 0
        cost = np.full((len(Bs), 256), const)
        for ta, tb, tm in T['V']:
            cost += Vt[ta[a] | tb[Bs][:, None] | tm[None, :]]
        for ta, tb, tm in T['E']:
            cost += Et[ta[a] | tb[Bs][:, None] | tm[None, :]]
        if St is not None:
            for ta, tb, tm in T['S']:
                cost += St[ta[a] | tb[Bs][:, None] | tm[None, :]]
        cost[~ok] = np.inf
        flat = cost.ravel()
        kk = min(K, flat.size)
        idx = np.argpartition(flat, kk - 1)[:kk]
        for t in idx:
            if flat[t] < -1e-9:
                best.append((flat[t], a, int(Bs[t // 256]), int(t % 256)))
    best.sort()
    return best

if __name__ == "__main__":
    t0 = time.time()
    # seed columns: one graph per degree histogram
    fA, fB, fM = T['mask']
    seen = {}; cols = []; keys = set(); colids = []
    star = [sum(1 << E(v, v ^ (1 << j)) for j in range(4)) for v in range(16)]
    for a, Bs in P:
        F = a & Bs
        ok = (insidemask[None, :] & F[:, None]) == 0
        mask = fA[a] | fB[Bs][:, None] | fM[None, :]
        code = np.zeros(mask.shape, dtype=np.int64)
        for v in range(16):
            mv = mask & star[v]
            code += 17 ** (POP16[mv & 0xFFFF] + POP16[mv >> 16])
        code[~ok] = -1
        u, first = np.unique(code.ravel(), return_index=True)
        for cd, t in zip(u.tolist(), first.tolist()):
            if cd >= 0 and cd not in seen:
                seen[cd] = (a, int(Bs[t // 256]), int(t % 256))
    for cd, (a, b, m) in seen.items():
        cols.append(col_stats(a, b, m)); keys.add((a, b, m)); colids.append((a, b, m))
    print("seed columns", len(cols), time.time() - t0, flush=True)
    cuts = []; coef = np.zeros((0, len(cols)))
    history = []
    for outer in range(60):
        for inner in range(40):
            r = solve_master(cols, cuts, coef)
            x = r.x[:len(cols)]
            nc, worst = new_cuts(x, cols)
            if not nc: break
            newrows = np.array([[cut_coef(st, cut) for st in cols] for cut in nc])
            coef = np.vstack([coef, newrows]) if len(cuts) else newrows
            cuts += nc
        val = -r.fun
        const, Vt, Et, St = pricing_tables(r, cuts, coef)
        best = price(const, Vt, Et, St)
        minrc = best[0][0] if best else 0.0
        history.append((val, minrc))
        print(f"outer {outer}: LP {val:.6f} worst_eig {worst:.2e} cols {len(cols)} cuts {len(cuts)} min_rc {minrc:.3e} t {time.time()-t0:.0f}s", flush=True)
        if not best or minrc > -1e-7:
            break
        added = 0
        for rc, a, b, m in best[:400]:
            if (a, b, m) in keys: continue
            st = col_stats(a, b, m); cols.append(st); keys.add((a, b, m)); colids.append((a, b, m)); added += 1
            nr = np.array([cut_coef(st, cut) for cut in cuts])
            coef = np.hstack([coef, nr[:, None]]) if len(cuts) else coef
        # prune cuts with zero dual and slack (keep size manageable)
        if len(cuts) > 3000:
            lam = r.ineqlin.marginals
            keep = np.where(np.abs(lam) > 1e-12)[0]
            cuts = [cuts[i] for i in keep]; coef = coef[keep]
    pickle.dump(dict(history=history, cols=len(cols), cuts=cuts, val=val, x=r.x, USE=USE,
                     colids=colids), open(f"res_{TAG}.pkl", "wb"))
    print("FINAL", USE, val, "minrc", minrc)
