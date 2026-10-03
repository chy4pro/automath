"""Fractional relaxation: maximize lambda such that there is a probability vector p on
{0..M} with nu = p*p*rev(p) >= lambda/(M+1) on target indices 0..M.
(nu index j corresponds to value j, range -M..2M.)
"""
import numpy as np, sys
from scipy.optimize import minimize

def nu_of(p):
    M = len(p) - 1
    q = np.convolve(p, p)              # indices 0..2M
    r = np.convolve(q, p[::-1])        # index i <-> value i - M ; range -M..2M
    return r

def solve(M, seed, iters=4000, beta0=50.0):
    rng = np.random.default_rng(seed)
    x = rng.normal(size=M + 1) * 0.5
    # softmax parametrization, maximize soft-min via LSE
    return _run(M,x,iters,beta0)

def obj(x, beta):
    M = len(x)-1
    if True:
        p = np.exp(x - x.max()); p /= p.sum()
        r = nu_of(p)
        tgt = r[M:2 * M + 1] * (M + 1)
        m = tgt.min()
        w = np.exp(-beta * (tgt - m)); s = w.sum()
        val = m - np.log(s) / beta
        # gradient of val wrt tgt = w/s
        g_t = w / s * (M + 1)
        # d r[M+j] / d p : r = p*p*rev(p)
        G = np.zeros(3 * M + 1); G[M:2 * M + 1] = g_t
        # r(v) = sum_{a,b,c} p_a p_b p_c [a+b-c = v]  (value index v, array index v+M)
        # dval/dp_a = 2*sum_{b,c} p_b p_c G(a+b-c) - ... + sum_{a,b} p_a p_b G(a+b-c) for c
        # compute via correlations
        q = np.convolve(p, p)  # a+b
        # term for c: sum_{a,b} p_a p_b G(a+b-c+M)  -> correlate q with G
        # index: value a+b-c, array idx a+b-c+M. For c in 0..M: sum_s q[s] G[s - c + M]
        gc = np.array([np.dot(q, G[M - c:M - c + 2 * M + 1]) for c in range(M + 1)])
        # term for a: 2*sum_{b,c} p_b p_c G(a+b-c+M)
        # d = b - c ranges -M..M ; pd = correlate
        pd = np.convolve(p, p[::-1])  # index d+M
        ga = np.array([2 * np.dot(pd, G[a:a + 2 * M + 1]) for a in range(M + 1)])
        gp = ga + gc
        gx = p * (gp - np.dot(gp, p))
        return -val, -gx
def _run(M,x,iters,beta0):
    beta = beta0
    for stage in range(6):
        res = minimize(obj, x, args=(beta,), jac=True, method='L-BFGS-B',
                       options={'maxiter': iters})
        x = res.x
        beta *= 3
    p = np.exp(x - x.max()); p /= p.sum()
    r = nu_of(p)
    lam = r[M:2 * M + 1].min() * (M + 1)
    return lam, p

if __name__ == '__main__':
    M = int(sys.argv[1]); nseeds = int(sys.argv[2])
    best = (0, None)
    for s in range(nseeds):
        lam, p = solve(M, s)
        if lam > best[0]:
            best = (lam, p)
        print(s, round(lam, 5), flush=True)
    lam, p = best
    print('BEST', lam)
    np.save(f'best_p_{M}.npy', p)
    np.set_printoptions(precision=4, suppress=True, linewidth=150)
    print(p)
