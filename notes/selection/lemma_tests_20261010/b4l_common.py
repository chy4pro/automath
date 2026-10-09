"""Common exact routines for the B4-L test (numpy int64; all quantities are exact integers)."""
import itertools, numpy as np

def u_of(N):
    """smallest positive integer u with u^17 >= N^13 (exact big-int)."""
    t = N**13
    u = max(1, int(round(N ** (13 / 17))) - 3)
    while u**17 < t: u += 1
    while u > 1 and (u - 1)**17 >= t: u -= 1
    return u

NMAX = 140000
_U = None
def utab():
    global _U
    if _U is None:
        _U = np.zeros(NMAX + 1, dtype=np.int64)
        u = 1
        for N in range(1, NMAX + 1):
            t = N**13
            while u**17 < t: u += 1
            _U[N] = u
        for N in (256, 300, 512, 4096, 100000, NMAX):  # cross-check against direct search
            assert _U[N] == u_of(N)
    return _U

_TUP = {}
def tuples(k):
    """unordered-pair formulation: arrays (pi,pj,qi,qj,w): P={i<=j}, Q={k<=l} disjoint index sets,
    w = (#ordered pairs for P)*(#ordered pairs for Q).  Equivalent to the ordered 4-tuples of T_A."""
    if k not in _TUP:
        prs = [(i, j, 1 if i == j else 2) for i in range(k) for j in range(i, k)]
        L = [(p[0], p[1], q[0], q[1], p[2] * q[2]) for p in prs for q in prs
             if not ({p[0], p[1]} & {q[0], q[1]})]
        a = np.array(L, dtype=np.int64).reshape(-1, 5)
        _TUP[k] = tuple(a[:, c] for c in range(5))
    return _TUP[k]

def b4_ok(rows):
    """rows n x k int array; True where all 4-multiset sums are pairwise distinct."""
    n, k = rows.shape
    if k == 0: return np.ones(n, bool)
    idx = np.array(list(itertools.combinations_with_replacement(range(k), 4)), dtype=np.int64)
    s = rows[:, idx[:, 0]] + rows[:, idx[:, 1]] + rows[:, idx[:, 2]] + rows[:, idx[:, 3]]
    s.sort(axis=1)
    return ~(s[:, 1:] == s[:, :-1]).any(axis=1)

def W_rows(rows, u):
    """W = sum_{0<|x|<u} T(x)(u-|x|) per row; u is array (n,)."""
    n, k = rows.shape
    if k < 2: return np.zeros(n, dtype=np.int64)
    pi, pj, qi, qj, w = tuples(k)
    x = rows[:, pi] + rows[:, pj] - rows[:, qi] - rows[:, qj]
    ax = np.abs(x)
    uu = u[:, None]
    m = (ax > 0) & (ax < uu)
    return (np.where(m, uu - ax, 0) * w).sum(axis=1)

def brute_hist(A):
    """independent brute force: ordered 4-tuples over A, returns dict x->T(x) (x may be 0)."""
    h = {}
    for a1 in A:
        for a2 in A:
            for b1 in A:
                for b2 in A:
                    if a1 == b1 or a1 == b2 or a2 == b1 or a2 == b2: continue
                    x = a1 + a2 - b1 - b2
                    h[x] = h.get(x, 0) + 1
    return h

def brute_D(A, N):
    u = u_of(N); h = brute_hist(A)
    return sum((4 - h.get(x, 0)) * (u - abs(x)) for x in range(-u + 1, u) if x != 0), u

def b4_brute(A):
    seen = {}
    for c in itertools.combinations_with_replacement(sorted(A), 4):
        s = sum(c)
        if s in seen: return False
        seen[s] = 1
    return True

def sumset_stats(A, u):
    S = sorted({a + b for a in A for b in A})
    d = {x - y for x in S for y in S}
    return len(S), sum(1 for x in range(1, u) if x in d) * 2

class Tracker:
    """per-(label, Nclass) minima of rho = 100 D/(u(u-1)); exact integers kept for the best."""
    def __init__(self): self.best = {}; self.cnt = {}; self.fail = []; self.cov = {}
    def update(self, label, base, rows, N, u, D, u_ok=True):
        pass

BASES = (256, 512, 4096)

class Acc:
    """accumulates exact results for one label (family,q or fixture group)."""
    def __init__(self, label):
        self.label = label; self.n = {}; self.invalid = 0
        self.best = {b: None for b in BASES}      # (rho, D, u, N, A, W)
        self.failures = []; self.cover = {b: 0 for b in BASES}   # ordinary translates covered per convention
    def add(self, rows, chunk=60000):
        """rows: n x k, sorted, rows[:,0]==0 (normalised by minimum)."""
        n, k = rows.shape
        if n == 0: return
        self.n[k] = self.n.get(k, 0) + n
        U = utab()
        for s0 in range(0, n, chunk):
            R = rows[s0:s0 + chunk]
            ok = b4_ok(R)
            if not ok.all():
                self.invalid += int((~ok).sum()); R = R[ok]
                if len(R) == 0: continue
            span = R[:, -1] + 1
            for b in BASES:
                N = np.maximum(b, span); u = U[N]
                W = W_rows(R, u)
                base = u * (u - 1)
                D = 4 * base - W
                self.cover[b] += int((N - span + 1).sum())
                for i in np.nonzero(100 * D < base)[0]:
                    self.failures.append((int(N[i]), int(u[i]), tuple(int(v) for v in R[i]), int(D[i])))
                rho = 100.0 * D / base
                i = int(np.argmin(rho))
                if self.best[b] is None or rho[i] < self.best[b][0]:
                    self.best[b] = (float(rho[i]), int(D[i]), int(u[i]), int(N[i]), tuple(int(v) for v in R[i]), int(W[i]))
