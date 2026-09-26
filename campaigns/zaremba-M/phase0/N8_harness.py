#!/usr/bin/env python3
"""N8 numerics harness (Zaremba campaign, phase 0).

Operators on functions f : P^1(F_p) -> R, points indexed 0..p-1 (finite) and p (= infinity).
Conventions: 1/0 = inf, 1/inf = 0, inf + a = inf.

 T1_N f(x) = (1/N)   sum_{c=1..N}          f( 1/(x+2c) - 2c )          Shkredov 2603.14116v2 Lemma 14, eq. (32)
                                                                        (= MMS 2212.14646 Lemma 4, eq. (14)-(15))
 T2_N f(x) = (1/N^2) sum_{h,h'=1..N}       f( 1/(x+h) - h' )           Shkredov Lemma 15, eq. (33), with S=[N]x[N],
                                                                        g x = 1/x  (the two-parameter family used in
                                                                        the proof of Corollary 16, eq. (35))
 T2e_N f(x)= (1/N^2) sum_{h,h'=1..N}       f( 1/(x+2h) - 2h' )         even-step variant (lives in <u^2, J> = Z*Z/2)

For sets A,B in F_p:  #{(a,b,c): (a+2c)(b+2c)=1} = N <1_B, T1 1_A>  (b = g_c a, g_c an involution)
                      #{(alpha,beta,a,b): 1/(alpha+a) = beta+b} = N^2 <1_B, T2 1_A>.
All three operators are real symmetric (T1: average of involution permutations; T2 = U J U^*,
U = (1/N) sum_h shift_h) and doubly stochastic, so sigma_max on mean-zero functions = max |eigenvalue|
on 1^perp. Every value computed by Lanczos/power iteration is a Rayleigh-Ritz value, hence a LOWER bound
for the true max over the spectrum's edge (up to floating point); the dense check gives the exact value.

Usage:
  python N8_harness.py selftest
  python N8_harness.py sparse  <p> <kind> <N1,N2,...>      kind in T1,T2,T2e
  python N8_harness.py dense   <p> <kind> <N1,N2,...>
  python N8_harness.py free    <N1,N2,...>                 free-model value for T2 / T2e (S-transform)
  python N8_harness.py randperm <n> <N1,...>               random-involution model for T2 (checks 'free')
Output: one JSON object per line on stdout.
"""
import sys, json, time, math
import numpy as np

# ---------------------------------------------------------------- arithmetic
def is_prime(n):
    if n < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0: return n == q
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True

def prim_root(p):
    m, fac, q = p - 1, [], 2
    while q * q <= m:
        if m % q == 0:
            fac.append(q)
            while m % q == 0: m //= q
        q += 1
    if m > 1: fac.append(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac): return g

def inverse_table(p):
    """inv[x] = x^{-1} mod p for x=1..p-1 (inv[0]=0 unused); built from powers of a primitive root."""
    g = prim_root(p); n = p - 1; B = int(math.isqrt(n)) + 1
    small = np.empty(B, dtype=np.int64); small[0] = 1
    for k in range(1, B): small[k] = small[k - 1] * g % p
    gB = pow(g, B, p); nb = n // B + 1
    big = np.empty(nb, dtype=np.int64); big[0] = 1
    for i in range(1, nb): big[i] = big[i - 1] * gB % p
    pw = ((big[:, None] * small[None, :]) % p).ravel()[:n]          # pw[k] = g^k
    inv = np.zeros(p, dtype=np.int64)
    inv[pw] = pw[(-np.arange(n)) % n]
    x = np.arange(1, p, dtype=np.int64)
    assert np.all((x * inv[1:]) % p == 1), "inverse table failed"
    return inv

# ---------------------------------------------------------------- sparse operators (length p+1 vectors)
class Ops:
    def __init__(self, p):
        assert is_prime(p) and p > 2
        self.p = p; self.n = p + 1
        self.inv = inverse_table(p)
        J = np.empty(p + 1, dtype=np.int64)
        J[1:p] = self.inv[1:]; J[0] = p; J[p] = 0
        self.J = J                                   # (Jf)(z) = f(1/z) = f[J[z]]
        x = np.arange(p, dtype=np.int64)
        self.m2 = (2 * x) % p                        # y -> 2y
        self.mhalf = (x * ((p + 1) // 2)) % p        # x -> x/2
        self.perms = None

    # (U+ f)(x) = (1/N) sum_{h=1..N} f(x+h),  (U- f)(y) = (1/N) sum_{h=1..N} f(y-h); infinity fixed
    def uplus(self, f, N):
        p = self.p; out = np.empty_like(f)
        ext = np.concatenate(([0.0], f[:p], f[:N + 1]))
        cs = np.cumsum(ext)                           # cs[k] = sum ext[1..k] = sum f-ext[0..k-1]
        i = np.arange(p)
        out[:p] = (cs[i + N + 1] - cs[i + 1]) / N      # f[x+1..x+N]
        out[p] = f[p]; return out
    def uminus(self, f, N):
        p = self.p; out = np.empty_like(f)
        ext = np.concatenate(([0.0], f[p - N:p], f[:p]))  # ext[1+k] = f[(k-N) mod p]
        cs = np.cumsum(ext)
        i = np.arange(p)
        out[:p] = (cs[i + N] - cs[i]) / N              # f[x-N..x-1]
        out[p] = f[p]; return out
    def _step2(self, fn, f, N):
        p = self.p; g = np.empty_like(f)
        g[:p] = f[self.m2]; g[p] = f[p]               # F(y) = f(2y)
        o = fn(g, N); out = np.empty_like(f)
        out[:p] = o[self.mhalf]; out[p] = o[p]; return out

    def T2(self, f, N, step=1):
        if step == 1:
            g = self.uminus(f, N); g = g[self.J]; return self.uplus(g, N)
        g = self._step2(self.uminus, f, N); g = g[self.J]; return self._step2(self.uplus, g, N)

    def build_T1(self, Nmax):
        p = self.p; x = np.arange(p, dtype=np.int64)
        P = np.empty((Nmax, p + 1), dtype=np.int32)
        for c in range(1, Nmax + 1):
            s = (x + 2 * c) % p
            y = np.where(s == 0, p, (self.inv[s] - 2 * c) % p)
            P[c - 1, :p] = y; P[c - 1, p] = (-2 * c) % p
        self.perms = P
    def T1(self, f, N):
        P = self.perms; out = f[P[0]].copy()
        for c in range(1, N): out += f[P[c]]
        return out / N

    def op(self, kind, N):
        if kind == 'T1':
            if self.perms is None or self.perms.shape[0] < N: self.build_T1(N)
            A = lambda f: self.T1(f, N)
        elif kind == 'T2': A = lambda f: self.T2(f, N, 1)
        elif kind == 'T2e': A = lambda f: self.T2(f, N, 2)
        else: raise ValueError(kind)
        def A0(f):                                    # restriction to mean-zero functions
            g = f - f.mean(); o = A(g); return o - o.mean()
        return A0

def lanczos_edges(A0, n, seed=0, tol=1e-9, ncv=40):
    from scipy.sparse.linalg import LinearOperator, eigsh
    L = LinearOperator((n, n), matvec=A0, dtype=np.float64)
    rng = np.random.default_rng(seed); v0 = rng.standard_normal(n); v0 -= v0.mean()
    cnt = [0]
    def mv(f): cnt[0] += 1; return A0(f)
    L = LinearOperator((n, n), matvec=mv, dtype=np.float64)
    la = eigsh(L, k=1, which='LA', v0=v0, tol=tol, ncv=ncv, return_eigenvectors=False)[0]
    sa = eigsh(L, k=1, which='SA', v0=v0, tol=tol, ncv=ncv, return_eigenvectors=False)[0]
    return float(la), float(sa), cnt[0]

def power_iter(A0, n, iters, seed=1):
    """power iteration on A0^2 ; returns sqrt of Rayleigh quotient <f,A0^2 f>/<f,f> (a lower bound)."""
    rng = np.random.default_rng(seed); f = rng.standard_normal(n); f -= f.mean(); f /= np.linalg.norm(f)
    hist = []
    for it in range(1, iters + 1):
        g = A0(A0(f)); r = float(f @ g); nf = np.linalg.norm(g); f = g / nf
        if it in (25, 50, 100, 200, 400, 800): hist.append((it, math.sqrt(max(r, 0.0))))
    return math.sqrt(max(r, 0.0)), hist

# ---------------------------------------------------------------- dense, independent construction
def dense(p, kind, N):
    """Build the (p+1)x(p+1) matrix entry by entry from the definition with Python integers."""
    INF = p
    def add(a, b):   return INF if a == INF else (a + b) % p
    def recip(a):    return 0 if a == INF else (INF if a % p == 0 else pow(a, -1, p))
    M = np.zeros((p + 1, p + 1))
    for x in range(p + 1):
        if kind == 'T1':
            for c in range(1, N + 1):
                M[x, add(recip(add(x, 2 * c)), -2 * c)] += 1.0 / N
        else:
            s = 1 if kind == 'T2' else 2
            for h in range(1, N + 1):
                r = recip(add(x, s * h))
                for h2 in range(1, N + 1):
                    M[x, add(r, -s * h2)] += 1.0 / N ** 2
    n = p + 1
    assert np.allclose(M.sum(0), 1) and np.allclose(M.sum(1), 1)
    Q = np.eye(n) - np.ones((n, n)) / n
    M0 = Q @ M @ Q
    sv = np.linalg.svd(M0, compute_uv=False)
    ev = np.linalg.eigvalsh((M0 + M0.T) / 2)
    return dict(sym_err=float(np.abs(M - M.T).max()), sigma_svd=float(sv[0]), sigma2_svd=float(sv[1]),
                lam_max=float(ev[-1]), lam_min=float(ev[1] if abs(ev[0]) < 1e-12 else ev[0]))

# ---------------------------------------------------------------- free-model value for T2 / T2e
def fejer_grid(N, M=1 << 22):
    th = (np.arange(M) + 0.5) * (np.pi / M)          # midpoint rule on (0, pi); F is even
    F = (np.sin(N * th / 2) / (N * np.sin(th / 2))) ** 2
    return F
def free_edge(F):
    """sup supp(mu (x) mu) for mu = law of F (free multiplicative convolution, S-transform).
    chi_nu(z) = chi_mu(z)^2 (1+z)/z; parametrize by w = chi_mu(z) in (0,1): z = psi_mu(w).
    Edge x+ = 1 / max_w  w^2 (1+psi(w))/psi(w)."""
    def f(t):
        w = 1 - math.exp(-t); ps = float(np.mean(w * F / (1 - w * F)))
        return w * w * (1 + ps) / ps
    # golden section on t = -log(1-w)
    a, b = 1e-3, 40.0
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a); fc, fd = f(c), f(d)
    for _ in range(90):
        if fc > fd: b, d, fd = d, c, fc; c = b - g * (b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + g * (b - a); fd = f(d)
    best = max(fc, fd); t = (a + b) / 2
    return 1.0 / best, 1 - math.exp(-t)

def selftest():
    # free_edge on two free projections of trace alpha: known edge 4 alpha(1-alpha)
    for al in (0.1, 0.25, 0.4):
        F = np.zeros(100000); F[:int(al * 100000)] = 1.0
        # atoms at 1 make psi finite at w->1-; restrict the search to w<1 (t<=40 fine)
        e, _ = free_edge(F)
        print(json.dumps(dict(test='free_edge_projections', alpha=al, got=e, expect=4 * al * (1 - al))))
    # inverse table / operator consistency vs dense for small p
    for p in (101, 211):
        O = Ops(p)
        for kind in ('T1', 'T2', 'T2e'):
            N = 5; A = O.op(kind, N)
            D = np.zeros((p + 1, p + 1))
            for i in range(p + 1):
                e = np.zeros(p + 1); e[i] = 1; D[:, i] = A(e)
            n = p + 1; Q = np.eye(n) - np.ones((n, n)) / n
            INF = p
            # rebuild independently
            Md = None
            d = dense(p, kind, N)
            s = np.linalg.svd(D, compute_uv=False)[0]
            print(json.dumps(dict(test='sparse_vs_dense', p=p, kind=kind, N=N, sparse=float(s), dense=d['sigma_svd'])))

def main():
    mode = sys.argv[1]
    if mode == 'selftest': selftest(); return
    if mode == 'free':
        for N in map(int, sys.argv[2].split(',')):
            t = time.time(); e, w = free_edge(fejer_grid(N))
            print(json.dumps(dict(mode='free', N=N, sigma_free_T2=math.sqrt(e), wstar=w,
                                  kesten=2 * math.sqrt(N - 1) / N if N > 1 else 1.0, secs=round(time.time() - t, 2))), flush=True)
        return
    if mode == 'randperm':
        n = int(sys.argv[2]); rng = np.random.default_rng(12345)
        perm = rng.permutation(n); Jr = np.empty(n, dtype=np.int64)
        Jr[perm[0::2]] = perm[1::2]; Jr[perm[1::2]] = perm[0::2]    # fixed-point-free involution
        for N in map(int, sys.argv[3].split(',')):
            def up(f):
                ext = np.concatenate(([0.0], f, f[:N + 1])); cs = np.cumsum(ext); i = np.arange(n)
                return (cs[i + N + 1] - cs[i + 1]) / N
            def um(f):
                ext = np.concatenate(([0.0], f[n - N:], f)); cs = np.cumsum(ext); i = np.arange(n)
                return (cs[i + N] - cs[i]) / N
            def A0(f):
                g = f - f.mean(); o = up(um(g)[Jr]); return o - o.mean()
            t = time.time(); la, sa, mv = lanczos_edges(A0, n)
            print(json.dumps(dict(mode='randperm', n=n, N=N, lam_max=la, lam_min=sa, matvecs=mv,
                                  secs=round(time.time() - t, 1))), flush=True)
        return
    p = int(sys.argv[2]); kind = sys.argv[3]; Ns = list(map(int, sys.argv[4].split(',')))
    piters = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    if mode == 'dense':
        for N in Ns:
            t = time.time(); d = dense(p, kind, N)
            d.update(mode='dense', p=p, kind=kind, N=N, secs=round(time.time() - t, 1))
            print(json.dumps(d), flush=True)
        return
    if mode == 'sparse':
        t0 = time.time(); O = Ops(p)
        if kind == 'T1': O.build_T1(max(Ns))
        tb = time.time() - t0
        for N in Ns:
            A0 = O.op(kind, N); t = time.time()
            la, sa, mv = lanczos_edges(A0, p + 1)
            rec = dict(mode='sparse', p=p, kind=kind, N=N, lam_max=la, lam_min=sa,
                       sigma=max(abs(la), abs(sa)), matvecs=mv, secs=round(time.time() - t, 1), build_secs=round(tb, 1))
            if piters:
                s, hist = power_iter(A0, p + 1, piters); rec.update(power=s, power_hist=hist)
                rec['secs_total'] = round(time.time() - t, 1)
            print(json.dumps(rec), flush=True)
        return

if __name__ == '__main__':
    main()
