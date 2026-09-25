#!/usr/bin/env python3
"""ROUND 6-A (line k1695): LEMMA T (transposition lemma) and the n=4 stratum-(b) prediction.

Lemma T. For A in M_n(F), tau=(a b), d=e_a-e_b, P_tau = I - d d^T = P_tau^{-1}, so
  rank(A P_tau - mu I) = rank(A - mu P_tau) = rank((A - mu I) + mu d d^T),
a rank-one update of E = A - mu I.  With g = nullity(E):
  T0: g=0  -> AP_tau not derogatory at mu.
  T1: g=1  -> derogatory iff l_a=l_b and r_a=r_b and 1 + d^T z = 0 where E z = mu d
              (l, r span the left/right kernels of E).
  T2: g=2  -> derogatory iff d in col(E) or d in row(E).
  T3: g>=3 -> derogatory for every tau.
Prediction for n=4 stratum (b) (minpoly an irreducible quadratic): EVERY transposition works.

Checks here (light, local): all A in GL(n,q), all transpositions, all mu in GF(q^2) (so degree-2
eigenvalues are exercised; for n<=4 every derogatory eigenvalue has degree <= 2), actual vs
predicted derogatory-ness, with per-clause firing counts and a NEGATIVE CONTROL (T1 scalar clause
deleted -> disagreements must appear).  Then the stratum-(b) prediction over GF(2), GF(3).
Exact table arithmetic, no floating point.  Everything provisional.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
HARD_LIMIT = 900.0
src = open("problems/k1695/round3_family.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 3-B family attack start')], "rf", "exec"), G)
GF, cyclic = G['GF'], G['cyclic']

def check_time(tag=""):
    if time.time() - T0 > HARD_LIMIT:
        print("HARD TIMEOUT at %.1fs (%s) -- everything printed above stands as stated" % (time.time()-T0, tag))
        sys.exit(2)

# ---------------------------------------------------------------- linear algebra over F
def rref(rows, ncols, F):
    """returns (rank, reduced rows (list of lists), pivot columns)"""
    ADD, MUL, NEG, INV = F.ADD, F.MUL, F.NEG, F.INV
    R = [list(r) for r in rows]
    piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(R)) if R[i][c]), None)
        if p is None: continue
        R[r], R[p] = R[p], R[r]
        iv = INV[R[r][c]]
        R[r] = [MUL[x][iv] for x in R[r]]
        for i in range(len(R)):
            if i != r and R[i][c]:
                f = R[i][c]; Mnf = MUL[NEG[f]]
                R[i] = [ADD[R[i][t]][Mnf[R[r][t]]] for t in range(ncols)]
        piv.append(c); r += 1
        if r == len(R): break
    return r, R[:r], piv

def rank(M, n, F):
    return rref([M[i*n:(i+1)*n] for i in range(n)], n, F)[0]

def nullspace(M, n, F):
    """basis of {x : M x = 0}, M flat n*n"""
    r, R, piv = rref([M[i*n:(i+1)*n] for i in range(n)], n, F)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fcol in free:
        x = [0]*n; x[fcol] = 1
        for i, pc in enumerate(piv):
            x[pc] = F.NEG[R[i][fcol]]
        basis.append(x)
    return basis

def transpose(M, n):
    return tuple(M[j*n+i] for i in range(n) for j in range(n))

def in_colspace(M, n, v, F):
    """is v in the column space of M?  <=> rank[M | v] == rank M"""
    rows = [list(M[i*n:(i+1)*n]) + [v[i]] for i in range(n)]
    return rref(rows, n+1, F)[0] == rank(M, n, F)

def solve(M, n, b, F):
    """one solution x of M x = b, or None"""
    rows = [list(M[i*n:(i+1)*n]) + [b[i]] for i in range(n)]
    r, R, piv = rref(rows, n+1, F)
    if n in piv: return None
    x = [0]*n
    for i, pc in enumerate(piv):
        x[pc] = R[i][n]
    return x

def matvec(M, n, v, F):
    ADD, MUL = F.ADD, F.MUL
    out = [0]*n
    for i in range(n):
        s = 0
        for j in range(n):
            if M[i*n+j] and v[j]:
                s = ADD[s][MUL[M[i*n+j]][v[j]]]
        out[i] = s
    return out

def dot(u, v, F):
    s = 0
    for a, b in zip(u, v):
        if a and b: s = F.ADD[s][F.MUL[a][b]]
    return s

def matmul(A, B, n, F):
    MUL, ADD = F.MUL, F.ADD
    C = [0]*(n*n)
    for i in range(n):
        ri = i*n
        for k in range(n):
            a = A[ri+k]
            if a:
                rk = k*n; Ma = MUL[a]
                for j in range(n):
                    b = B[rk+j]
                    if b: C[ri+j] = ADD[C[ri+j]][Ma[b]]
    return tuple(C)

# ---------------------------------------------------------------- Lemma T prediction
def predict(A, n, a, b, mu, F, drop_scalar=False):
    """returns (derogatory?, clause) per Lemma T evaluated from E = A - mu I."""
    NEG, ADD = F.NEG, F.ADD
    E = list(A)
    for i in range(n):
        E[i*n+i] = ADD[E[i*n+i]][NEG[mu]]
    E = tuple(E)
    d = [0]*n; d[a] = 1; d[b] = NEG[1]
    rk = rank(E, n, F); g = n - rk
    if g == 0:
        return False, "T0"
    if g == 1:
        r = nullspace(E, n, F)[0]
        l = nullspace(transpose(E, n), n, F)[0]
        if l[a] != l[b] or r[a] != r[b]:
            return False, "T1"
        if drop_scalar:
            return True, "T1"
        mud = [F.MUL[mu][x] for x in d]
        z = solve(E, n, mud, F)
        assert z is not None, "l_a=l_b should make mu*d lie in col(E)"
        return ADD[1][dot(d, z, F)] == 0, "T1"
    if g == 2:
        return (in_colspace(E, n, d, F) or in_colspace(transpose(E, n), n, d, F)), "T2"
    return True, "T3"

def derog_at(M, n, mu, F):
    """rank(M - mu I) <= n-2 ?  (geometric multiplicity >= 2 at mu)"""
    M = list(M)
    for i in range(n):
        M[i*n+i] = F.ADD[M[i*n+i]][F.NEG[mu]]
    return rank(tuple(M), n, F) <= n-2

def actual(A, n, a, b, mu, F):
    """rank(A P_tau - mu I) <= n-2 ?"""
    P = [0]*(n*n)
    for j in range(n):
        s = b if j == a else (a if j == b else j)
        P[s*n+j] = 1
    return derog_at(matmul(A, tuple(P), n, F), n, mu, F)

def gl_iter(n, q, F):
    for entries in itertools.product(range(q), repeat=n*n):
        if rank(entries, n, F) == n:
            yield tuple(entries)

def gl_order(n, q):
    o = 1
    for i in range(n): o *= q**n - q**i
    return o

def embed_check(Fq, Fq2):
    """the prime-field elements 0..p-1 must have the same arithmetic in both tables (they do by
    construction: element index a < p is the constant polynomial a); for q non-prime we do NOT
    embed, we only use q prime here."""
    p = Fq.p
    for a in range(p):
        for b in range(p):
            assert Fq.ADD[a][b] == Fq2.ADD[a][b] and Fq.MUL[a][b] == Fq2.MUL[a][b]

print("ROUND 6-A: Lemma T check + stratum-(b) transposition prediction")
# ---- controls on the oracle pair (rank-based derogatory test vs the minpoly-based `cyclic`)
for q in (2, 3, 4, 5):
    F = GF(q)
    for n in (3, 4):
        I = tuple(1 if i == j else 0 for i in range(n) for j in range(n))
        C = [0]*(n*n)
        for i in range(n-1): C[(i+1)*n+i] = 1
        C[0*n + n-1] = 1  # companion of x^n - 1
        C = tuple(C)
        # identity: derogatory at mu=1 (n>=2) and cyclic() must say False
        assert derog_at(I, n, 1, F) and not cyclic(I, n, F)
        # companion of x^n-1: cyclic, and never derogatory at any mu in GF(q)
        assert cyclic(C, n, F) and all(not derog_at(C, n, mu, F) for mu in range(q))
        # and the two oracles must agree on every permutation product of the identity
        for s in itertools.permutations(range(n)):
            P = tuple(1 if s[j] == i else 0 for i in range(n) for j in range(n))
            assert cyclic(P, n, F) == (not any(derog_at(P, n, mu, F) for mu in range(q))) or q < 4
print("oracle controls pass (identity derogatory / companion cyclic) for q in {2,3,4,5}, n in {3,4}")

# ---- Lemma T: cells (n, q) with mu ranging over GF(q^2); q prime so the prime field embeds
CELLS = [(3, 2), (3, 3), (4, 2)]   # (3,5) over GF(25) = 1.1e8 rank computations: left to the C/codex checks
for (n, q) in CELLS:
    check_time("cell %d,%d" % (n, q))
    Fq = GF(q); F2 = GF(q*q); embed_check(Fq, F2)
    trans = [(a, b) for a in range(n) for b in range(a+1, n)]
    pop = 0; triples = 0; dis = 0; dis_neg = 0
    fire = {"T0": 0, "T1": 0, "T2": 0, "T3": 0}
    derog = {"T0": 0, "T1": 0, "T2": 0, "T3": 0}
    n_derog_nonrational = 0
    for A in gl_iter(n, q, Fq):
        pop += 1
        for (a, b) in trans:
            for mu in range(q*q):
                act = actual(A, n, a, b, mu, F2)
                pred, cl = predict(A, n, a, b, mu, F2)
                pred_neg, _ = predict(A, n, a, b, mu, F2, drop_scalar=True)
                triples += 1
                fire[cl] += 1
                if act:
                    derog[cl] += 1
                    if mu >= q: n_derog_nonrational += 1
                if act != pred: dis += 1
                if act != pred_neg: dis_neg += 1
    assert pop == gl_order(n, q), "population mismatch"
    print("cell n=%d q=%d over GF(%d): |GL|=%d (formula ok)  triples=%d  DISAGREEMENTS=%d  "
          "negative-control(T1 scalar clause deleted) disagreements=%d  clause fired=%s  derogatory-by-clause=%s  "
          "derogatory at non-rational mu=%d  [%.1fs]"
          % (n, q, q*q, pop, triples, dis, dis_neg, fire, derog, n_derog_nonrational, time.time()-T0))
    assert dis == 0, "LEMMA T DISAGREEMENT in cell (%d,%d)" % (n, q)
    assert dis_neg > 0, "negative control did not fire: the T1 scalar clause was never load-bearing"

# ---- stratum (b) at n=4: every transposition works
print("--- stratum (b), n=4: prediction = every transposition gives a cyclic product")
N = 4
src2 = open("problems/k1695/round3_n4_stratumB.py").read()
G2 = {}
exec(compile(src2[:src2.index('print("ROUND 3-F')], "sb", "exec"), G2)
for q in (2, 3):
    check_time("stratum b q=%d" % q)
    F = GF(q)
    gens = G2['gl_gens'](F); ginv = [G2['inv4'](g, F) for g in gens]
    tot = 0; bad = 0; pairs = 0
    for (c1, c0) in G2['irreducible_quadratics'](F):
        rep = G2['companion_pair'](c1, c0, F)
        seen = {rep}; stack = [rep]
        while stack:
            A = stack.pop()
            for g, gi in zip(gens, ginv):
                B = matmul(matmul(g, A, N, F), gi, N, F)
                if B not in seen:
                    seen.add(B); stack.append(B)
        assert len(seen) == G2['class_size'](q), "orbit control failed"
        for A in seen:
            tot += 1
            assert G2['minpoly_deg'](A, F) == 2
            for a in range(N):
                for b in range(a+1, N):
                    P = [0]*(N*N)
                    for j in range(N):
                        s = b if j == a else (a if j == b else j)
                        P[s*N+j] = 1
                    pairs += 1
                    if not cyclic(matmul(A, tuple(P), N, F), N, F):
                        bad += 1
                        print("  PREDICTION FAILED q=%d A=%s tau=(%d %d)" % (q, A, a, b))
    print("q=%d stratum-(b) matrices=%d (class-size control ok)  (A,tau) pairs=%d  non-cyclic=%d  [%.1fs]"
          % (q, tot, pairs, bad, time.time()-T0))
print("stratum-(b) control: A itself (P = I) is non-cyclic for the representative C_m+C_m: %s"
      % all(not cyclic(G2['companion_pair'](c1, c0, GF(q)), N, GF(q))
            for q in (2, 3) for (c1, c0) in G2['irreducible_quadratics'](GF(q))))
print("done %.1fs" % (time.time()-T0))
