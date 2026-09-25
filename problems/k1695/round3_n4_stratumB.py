#!/usr/bin/env python3
"""ROUND 3-F (line k1695): the SECOND n=4 stratum.

For n=4 a counterexample A must be derogatory, so some lambda in F-bar has geometric
multiplicity >= 2.  The Galois count 2*[F(lam):F] <= 4 leaves exactly two strata:
  (a) lam in F  ->  A = lam*(I + U W^T), rank <= 2  -- the rank-<=2 perturbation stratum;
  (b) lam of degree 2 over F -> charpoly = f^2 and geometric multiplicity 2 at each root,
      so the invariant factors are (f, f): minpoly(A) = f, an IRREDUCIBLE QUADRATIC.
Stratum (b) is NOT reachable by the rank-one/rank-two machinery (A is not a scalar plus
small rank over F at all), so it needs its own argument.  Before looking for one, find out
what is actually true there.

Question probed: for A in stratum (b), which cycle types give a cyclic A*P?
Populations: stratum (b) is the union over irreducible monic quadratics f of the single
similarity class of C_f (+) C_f.  Small cells are enumerated EXHAUSTIVELY by orbit BFS
(conjugation by transvection-style generators of GL(4,q)); the population is checked
against the class-size formula |GL(4,q)|/|GL(2,q^2)|, which is a real control -- a BFS that
closed early would miss it.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round3_family.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 3-B family attack start')], "rf", "exec"), G)
GF, cyclic, cycle_type = G['GF'], G['cyclic'], G['cycle_type']

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
                    if b:
                        C[ri+j] = ADD[C[ri+j]][Ma[b]]
    return tuple(C)

N = 4
def perms():
    out = []
    for s in itertools.permutations(range(N)):
        out.append((cycle_type(s), tuple(1 if s[j] == i else 0 for i in range(N) for j in range(N))))
    return out
PL = perms()

def minpoly_deg(M, F):
    """degree of the minimal polynomial (2 for stratum (b))."""
    MUL, ADD, NEG, INV = F.MUL, F.ADD, F.NEG, F.INV
    rows = []
    cur = tuple(1 if i == j else 0 for i in range(N) for j in range(N))
    for d in range(N+1):
        v = list(cur)
        for (piv, rw) in rows:
            f = v[piv]
            if f:
                Mnf = MUL[NEG[f]]
                for t in range(piv, N*N):
                    if rw[t]: v[t] = ADD[v[t]][Mnf[rw[t]]]
        piv = next((i for i, x in enumerate(v) if x), None)
        if piv is None:
            return d
        Miv = MUL[INV[v[piv]]]
        rows.append((piv, [Miv[x] for x in v]))
        cur = matmul(cur, M, N, F)
    return N+1

def inv4(A, F):
    M = [list(A[i*N:(i+1)*N]) + [1 if i == j else 0 for j in range(N)] for i in range(N)]
    for c in range(N):
        piv = next((r for r in range(c, N) if M[r][c]), None)
        if piv is None: return None
        M[c], M[piv] = M[piv], M[c]
        iv = F.INV[M[c][c]]
        M[c] = [F.MUL[x][iv] for x in M[c]]
        for r in range(N):
            if r != c and M[r][c]:
                f = M[r][c]; Mnf = F.MUL[F.NEG[f]]
                M[r] = [F.ADD[M[r][t]][Mnf[M[c][t]]] for t in range(2*N)]
    return tuple(M[i][N+j] for i in range(N) for j in range(N))

def gl_gens(F):
    q = F.q; gens = []
    for i in range(N):
        for j in range(N):
            if i != j:
                g = [1 if a == b else 0 for a in range(N) for b in range(N)]
                g[i*N+j] = 1
                gens.append(tuple(g))
    g = [1 if a == b else 0 for a in range(N) for b in range(N)]
    if q > 2:
        g[0] = 2
        gens.append(tuple(g))
    return gens

def irreducible_quadratics(F):
    q = F.q; out = []
    for c1 in range(q):
        for c0 in range(q):
            # x^2 + c1 x + c0 irreducible <=> no root in F, and c0 != 0 for invertibility
            if c0 == 0: continue
            if any(F.ADD[F.ADD[F.MUL[x][x]][F.MUL[c1][x]]][c0] == 0 for x in range(q)):
                continue
            out.append((c1, c0))
    return out

def companion_pair(c1, c0, F):
    """C_f (+) C_f for f = x^2 + c1 x + c0."""
    M = [0]*(N*N)
    for b in (0, 2):
        M[(b+1)*N + b] = 1
        M[b*N + b+1] = F.NEG[c0]
        M[(b+1)*N + b+1] = F.NEG[c1]
    return tuple(M)

def class_size(q):
    o4 = 1
    for i in range(4): o4 *= q**4 - q**i
    o2 = (q**4 - 1)*(q**4 - q**2)
    return o4 // o2

print("ROUND 3-F: n=4 stratum (b) -- minpoly an irreducible quadratic")
for q in [2, 3]:
    F = GF(q)
    gens = gl_gens(F)
    ginv = [inv4(g, F) for g in gens]
    quads = irreducible_quadratics(F)
    tot = 0; hist = {}; worst = []
    for (c1, c0) in quads:
        rep = companion_pair(c1, c0, F)
        assert minpoly_deg(rep, F) == 2, "representative has wrong minpoly degree"
        seen = {rep}; stack = [rep]
        while stack:
            A = stack.pop()
            for g, gi in zip(gens, ginv):
                B = matmul(matmul(g, A, N, F), gi, N, F)
                if B not in seen:
                    seen.add(B); stack.append(B)
        assert len(seen) == class_size(q), \
            "ORBIT CONTROL FAILED f=x^2+%dx+%d: got %d, class-size formula says %d" % (c1, c0, len(seen), class_size(q))
        for A in seen:
            tot += 1
            assert minpoly_deg(A, F) == 2, "class member with wrong minpoly"
            hit = None
            for (ct, P) in PL:
                if cyclic(matmul(A, P, N, F), N, F):
                    hit = ct
                    if ct == (4,): break
            assert hit is not None, "*** STRATUM-B COUNTEREXAMPLE q=%d A=%s ***" % (q, A)
            hist[hit] = hist.get(hit, 0) + 1
    print("q=%d  irreducible quadratics=%d  class size=%d  stratum-(b) matrices=%d  "
          "counterexamples=0  |  best-type histogram: %s"
          % (q, len(quads), class_size(q), tot, sorted(hist.items(), key=str)))
print("%.1fs" % (time.time()-T0))
