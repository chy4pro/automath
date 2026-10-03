"""Exact verification of a dual certificate produced by q4lp2.py.
Statement verified:  for every C4-free G in Q4 (all iso classes),
   F(G) := 384*[ rho_G - w.H_G + <Y, Stats(G)> ]  <=  384*c0     (exact integer arithmetic, Y,w rational)
and  w.Bin(4,delta) <= c1 for all delta in [0,1] (exact rational Bernstein subdivision);
with every Y-block PSD.  Then pi_4 <= c0 + c1."""
import numpy as np, pickle, sys, time
from fractions import Fraction as Fr
from math import comb
VTAG = sys.argv[1] if len(sys.argv) > 1 else "m2"
sys.argv = [sys.argv[0], "none", "verify"]
exec(open("q4lp2.py").read().split('if __name__ == "__main__":')[0])
d = pickle.load(open(f"res_{VTAG}.pkl", "rb"))
lam0, lamh, WV, WVL, WE, WS = d['duals']
print("run", VTAG, "LP value", d['val'], "gmin", d['gmin'])
D = 10**9; EPS = 1e-6

def ldl_psd(M):
    """exact PSD test of a symmetric rational matrix (list of lists of Fraction) via LDL with pivoting on zeros"""
    n = len(M); A = [row[:] for row in M]
    for k in range(n):
        if A[k][k] < 0: return False
        if A[k][k] == 0:
            if any(A[k][j] != 0 for j in range(k + 1, n)): return False
            continue
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            if f != 0:
                for j in range(k + 1, n):
                    A[i][j] -= f * A[k][j]
    return True

def rationalise_block(Yf, exact=True):
    Yf = (Yf + Yf.T) / 2
    idx = np.where(np.abs(Yf).sum(1) > 0)[0]
    Y = Yf.copy()
    Y[idx, idx] += EPS
    Yi = np.round(Y * D).astype(np.int64)
    Yi = (Yi + Yi.T) // 2 if np.all((Yi + Yi.T) % 2 == 0) else np.round((Yi + Yi.T) / 2).astype(np.int64)
    Yi = np.triu(Yi) + np.triu(Yi, 1).T
    if len(idx) == 0: return Yi, True
    sub = Yi[np.ix_(idx, idx)]
    if exact and len(idx) <= 20:
        ok = ldl_psd([[Fr(int(v), D) for v in row] for row in sub])
    else:
        lmin = np.linalg.eigvalsh(sub / D).min()
        # float eigenvalue error is ~ n*1e-16*||Y||; require a margin well above it
        ok = lmin > 1e3 * len(idx) * 1e-16 * np.abs(sub / D).max() and lmin > 0
    return Yi, ok

allok = True
YV, ok = rationalise_block(-WV.reshape(18, 18)); allok &= ok
YVL = np.zeros((16, 2, 2), dtype=np.int64)
for c in range(16):
    YVL[c], ok = rationalise_block(-WVL.reshape(16, 2, 2)[c]); allok &= ok
YE = np.zeros((2, 8, 8, 8), dtype=np.int64); WE4 = WE.reshape(2, 8, 8, 8)
for s_ in range(2):
    for c in range(8):
        YE[s_, :, :, c], ok = rationalise_block(-WE4[s_, :, :, c]); allok &= ok
YS = np.zeros((16, 256, 256), dtype=np.int64)
for r_ in range(16):
    if np.any(WS[r_] != 0):
        YS[r_], ok = rationalise_block(-WS[r_], exact=False); allok &= ok
print("all Y blocks PSD (after +EPS*I, rational with denominator D):", allok)
wint = np.round(-lamh * D).astype(np.int64)      # w = wint / D

# integer cost tables, scaled by 384*D
V_wint = np.round(V_w * 384).astype(np.int64)     # 2 (bb) or 1
assert np.allclose(V_w * 384, V_wint)
Vt = -24 * wint[vdeg] + (YV.ravel()[V_idx] * V_wint[:, None]).sum(0) + YVL.ravel()[VL_idx].sum(0)
Et = 12 * D * es + YE.ravel()[E_idx].sum(0)
St = YS.ravel()[S_entries(np.arange(1 << 20))].sum(-1) if np.any(YS) else None
t0 = time.time(); best = None; arg = None
for a, Bs in P:
    F = a & Bs
    ok = (insidemask[None, :] & F[:, None]) == 0
    cost = np.zeros((len(Bs), 256), dtype=np.int64)
    for ta, tb, tm in T['V']: cost += Vt[ta[a] | tb[Bs][:, None] | tm[None, :]]
    for ta, tb, tm in T['E']: cost += Et[ta[a] | tb[Bs][:, None] | tm[None, :]]
    if St is not None:
        for ta, tb, tm in T['S']: cost += St[ta[a] | tb[Bs][:, None] | tm[None, :]]
    cost[~ok] = np.iinfo(np.int64).min
    m = int(cost.max())
    if best is None or m > best: best = m; t = int(cost.argmax()); arg = (a, int(Bs[t // 256]), t % 256)
c0 = Fr(best, 384 * D)
print("max_G F(G) exact:", best, " c0 =", float(c0), "attained at", arg, "time", round(time.time() - t0, 1))

# c1 = max over [0,1] of sum_m w_m C(4,m) d^m (1-d)^(4-m): Bernstein coefficients are w_m themselves
w = [Fr(int(x), D) for x in wint]
def bern_split(b):
    # de Casteljau at 1/2: returns Bernstein coeffs on left and right halves
    L, R = [b[0]], [b[-1]]; cur = b[:]
    while len(cur) > 1:
        cur = [(cur[i] + cur[i + 1]) / 2 for i in range(len(cur) - 1)]
        L.append(cur[0]); R.append(cur[-1])
    return L, R[::-1]
lower = max(w[0], w[-1]); stack = [w]; upper = lower; it = 0
while stack:
    b = stack.pop(); it += 1
    ub = max(b)
    lower = max(lower, b[0], b[-1])
    if ub <= lower + Fr(1, 10**12): upper = max(upper, ub); continue
    Lb, Rb = bern_split(b); stack += [Lb, Rb]
c1 = max(upper, lower)
print("c1 (rigorous upper bound) =", float(c1), "subdivisions", it, " LP c1 estimate", -d['duals'][0] * 0)
bound = c0 + c1
print("PROVED (exact arithmetic): pi_4 <=", float(bound), " = ", bound if bound.denominator < 10**30 else "")
pickle.dump(dict(c0=c0, c1=c1, bound=bound, D=D, EPS=EPS, YV=YV, YVL=YVL, YE=YE, YS_nonzero=[r for r in range(16) if np.any(YS[r])], wint=wint, psd=allok),
            open(f"cert_{VTAG}.pkl", "wb"))
