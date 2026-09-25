#!/usr/bin/env python3
"""ROUND 3-A (line k1695, 2026-08-24): in-repo reproduction of selection probe P-K1,
EXTENDED with cycle-type structure and two structural hypotheses.

P-K1 (notes/selection/probe_k1695_smallfield.py) answered only "does SOME permutation
work?".  This run answers "WHICH cycle types work?", because the shape of any general
proof depends on how small a set of permutations always suffices.

Hypotheses tested (both refutable by a single matrix, both interesting either way):
  H-exist : for every invertible A there is SOME permutation P with AP cyclic  (= 16.95)
  H2      : some P of cycle type (n) or (n-1,1) already works
  H1      : some P with AT MOST TWO cycles already works
H1 is the interesting one: for A a rank-one perturbation of a monomial matrix, a
permutation with r >= 3 cycles can never work (nullity(P-1) >= r, and a rank-one
perturbation drops nullity by at most 1) -- so H1 asks whether that necessary condition
for the structured family is a sufficient search space in general.

Fields: GF(q) for q in {2,3,4,5,7,8,9} -- INCLUDING non-prime q, which P-K1 did not
reach (its stated frontier).  Exact table arithmetic, no floating point anywhere.

CONTROLS (all asserted; any failure aborts the run):
  NEG-1  identity I is judged NOT cyclic for n>=2 (a checker that says yes to everything
         would make every census row vacuous)
  NEG-2  scalar 2I judged NOT cyclic (q>2, n>=2)
  POS-1  companion matrix of x^n-1 is judged cyclic
  POS-2  population: enumerated |GL(n,q)| equals prod_i (q^n - q^i)
  KAT-1  known-answer test reproducing k1695_state.md R8 (an INDEPENDENT prior result):
         over GF(2), A=J-I, n=6: NO 6-cycle works, but a (5,1) does.
  KAT-2  its own sharpness control: over GF(2), A=J-I, n=4: a 4-cycle DOES work.
  KAT-3  reproduce two R2/R4 counts exactly: #good permutations for A=J-I is 14 at
         (q=2,n=4) and 5 at (q=3,n=3).
Hard wall limit; per-cell checkpoint to stdout (line buffered).
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
HARD_LIMIT = 1500.0

def check_time(tag=""):
    if time.time() - T0 > HARD_LIMIT:
        print("HARD TIMEOUT at %.1fs (%s) -- results printed above stand as stated" % (time.time()-T0, tag))
        sys.exit(2)

# ---------------------------------------------------------------- GF(q) tables
IRRED = {(2,2):[1,1,1], (2,3):[1,1,0,1], (3,2):[1,0,1], (5,2):[2,0,1], (2,4):[1,1,0,0,1]}

def prime_power(q):
    p = 2
    while p*p <= q and q % p:
        p += 1
    if q % p:
        p = q
    k, t = 0, q
    while t % p == 0:
        t //= p; k += 1
    assert t == 1, "q=%d not a prime power" % q
    return p, k

class GF(object):
    def __init__(self, q):
        p, k = prime_power(q)
        self.q, self.p, self.k = q, p, k
        if k == 1:
            self.ADD = [[(a+b) % p for b in range(q)] for a in range(q)]
            self.MUL = [[(a*b) % p for b in range(q)] for a in range(q)]
        else:
            f = IRRED[(p,k)]
            def digits(a):
                d = []
                for _ in range(k):
                    d.append(a % p); a //= p
                return d
            def undig(d):
                v = 0
                for i in reversed(range(k)):
                    v = v*p + d[i]
                return v
            def polymul(a, b):
                da, db = digits(a), digits(b)
                c = [0]*(2*k-1)
                for i in range(k):
                    if da[i]:
                        for j in range(k):
                            c[i+j] = (c[i+j] + da[i]*db[j]) % p
                for i in reversed(range(k, 2*k-1)):
                    if c[i]:
                        co = c[i]; c[i] = 0
                        for j in range(k):
                            c[i-k+j] = (c[i-k+j] - co*f[j]) % p
                return undig(c[:k])
            self.ADD = [[undig([(x+y) % p for x, y in zip(digits(a), digits(b))]) for b in range(q)] for a in range(q)]
            self.MUL = [[polymul(a, b) for b in range(q)] for a in range(q)]
        self.NEG = [next(b for b in range(q) if self.ADD[a][b] == 0) for a in range(q)]
        self.INV = [0]*q
        for a in range(1, q):
            self.INV[a] = next(b for b in range(1, q) if self.MUL[a][b] == 1)
        # field axiom self-check (cheap, catches a broken irreducible polynomial)
        for a in range(q):
            assert self.ADD[a][0] == a and self.MUL[a][1] == a
            for b in range(q):
                assert self.ADD[a][b] == self.ADD[b][a] and self.MUL[a][b] == self.MUL[b][a]
        assert all(self.MUL[a][self.INV[a]] == 1 for a in range(1, q)), "INV table broken"

# ------------------------------------------------------- matrices as flat tuples
def matmul(A, B, n, F):
    MUL, ADD = F.MUL, F.ADD
    C = [0]*(n*n)
    for i in range(n):
        ri = i*n
        for k in range(n):
            a = A[ri+k]
            if a:
                rk = k*n
                Ma = MUL[a]
                for j in range(n):
                    b = B[rk+j]
                    if b:
                        C[ri+j] = ADD[C[ri+j]][Ma[b]]
    return tuple(C)

def det_nonzero(A, n, F):
    MUL, ADD, NEG, INV = F.MUL, F.ADD, F.NEG, F.INV
    M = [list(A[i*n:(i+1)*n]) for i in range(n)]
    for c in range(n):
        piv = None
        for r in range(c, n):
            if M[r][c]:
                piv = r; break
        if piv is None:
            return False
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
        iv = INV[M[c][c]]
        for r in range(c+1, n):
            if M[r][c]:
                f = MUL[M[r][c]][iv]
                nf = NEG[f]
                Mnf = MUL[nf]
                for k in range(c, n):
                    if M[c][k]:
                        M[r][k] = ADD[M[r][k]][Mnf[M[c][k]]]
    return True

def cyclic(M, n, F):
    """True iff minpoly(M) has degree n, i.e. I,M,...,M^{n-1} are linearly independent."""
    MUL, ADD, NEG, INV = F.MUL, F.ADD, F.NEG, F.INV
    rows = []
    cur = tuple(1 if i == j else 0 for i in range(n) for j in range(n))
    for _ in range(n):
        v = list(cur)
        for (piv, rw) in rows:
            f = v[piv]
            if f:
                nf = NEG[f]; Mnf = MUL[nf]
                for t in range(piv, n*n):
                    if rw[t]:
                        v[t] = ADD[v[t]][Mnf[rw[t]]]
        piv = next((i for i, x in enumerate(v) if x), None)
        if piv is None:
            return False
        iv = INV[v[piv]]
        Miv = MUL[iv]
        v = [Miv[x] for x in v]
        rows.append((piv, v))
        cur = matmul(cur, M, n, F)
    return True

# ------------------------------------------------------------- permutation data
def cycle_type(s):
    n = len(s); seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]:
                seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))

def perm_plan(n):
    """All permutations, ordered by priority tier:
       tier 0 = cycle type (n); tier 1 = (n-1,1); tier 2 = other 2-cycle types;
       tier 3 = >=3 cycles.  Returns list of (tier, ctype, Pmatrix_flat)."""
    out = []
    for s in itertools.permutations(range(n)):
        ct = cycle_type(s)
        if len(ct) == 1:
            tier = 0
        elif ct == (n-1, 1):
            tier = 1
        elif len(ct) == 2:
            tier = 2
        else:
            tier = 3
        P = tuple(1 if s[j] == i else 0 for i in range(n) for j in range(n))
        out.append((tier, ct, P))
    out.sort(key=lambda r: r[0])
    return out

def J_minus_I(n, F):
    return tuple((1 if i != j else F.NEG[1] * 0 + 0) if i != j else 0 for i in range(n) for j in range(n))

def companion_xn_1(n):
    M = [[0]*n for _ in range(n)]
    for i in range(1, n):
        M[i][i-1] = 1
    M[0][n-1] = 1
    return tuple(M[i][j] for i in range(n) for j in range(n))

def gl_order(n, q):
    o = 1
    for i in range(n):
        o *= q**n - q**i
    return o

# ------------------------------------------------------------------- controls
def run_controls():
    print("--- CONTROLS ---")
    for q in [2, 3, 4, 5, 7, 8, 9]:
        F = GF(q)
        for n in [2, 3, 4]:
            I = tuple(1 if i == j else 0 for i in range(n) for j in range(n))
            assert not cyclic(I, n, F), "NEG-1 FAILED q=%d n=%d" % (q, n)
            if q > 2:
                two = tuple(2 if i == j else 0 for i in range(n) for j in range(n))
                assert not cyclic(two, n, F), "NEG-2 FAILED q=%d n=%d" % (q, n)
            assert cyclic(companion_xn_1(n), n, F), "POS-1 FAILED q=%d n=%d" % (q, n)
    print("NEG-1 (I not cyclic), NEG-2 (2I not cyclic), POS-1 (companion cyclic): PASS, q in 2,3,4,5,7,8,9, n in 2,3,4")
    # KAT: reproduce R8 (char 2, n=6: no n-cycle; (5,1) works) and its n=4 control
    F2 = GF(2)
    for n, expect_ncycle in [(6, False), (4, True)]:
        A = tuple(1 if i != j else 0 for i in range(n) for j in range(n))  # J - I over GF(2) == J + I
        plan = perm_plan(n)
        got_n = any(cyclic(matmul(A, P, n, F2), n, F2) for (t, ct, P) in plan if t == 0)
        got_f = any(cyclic(matmul(A, P, n, F2), n, F2) for (t, ct, P) in plan if t == 1)
        assert got_n == expect_ncycle, "KAT FAILED n=%d: n-cycle works=%s expected %s" % (n, got_n, expect_ncycle)
        assert got_f, "KAT FAILED n=%d: (n-1,1) does not work" % n
        print("KAT n=%d GF(2) A=J-I : n-cycle works=%s (expected %s), (n-1,1) works=%s  [reproduces R8]"
              % (n, got_n, expect_ncycle, got_f))
    # KAT-3: exact good-permutation counts from R2 section R4
    for (q, n, expect) in [(2, 4, 14), (3, 3, 5), (5, 4, 8), (2, 6, 144)]:
        F = GF(q)
        A = tuple(F.NEG[1] if i == j else 0 for i in range(n) for j in range(n))
        A = tuple(F.ADD[A[i*n+j]][1] for i in range(n) for j in range(n))   # J - I
        cnt = sum(1 for (t, ct, P) in perm_plan(n) if cyclic(matmul(A, P, n, F), n, F))
        assert cnt == expect, "KAT-3 FAILED q=%d n=%d: got %d expected %d" % (q, n, cnt, expect)
        print("KAT-3 q=%d n=%d A=J-I: #good permutations = %d (R2 sec R4 says %d) OK" % (q, n, cnt, expect))
    print("--- CONTROLS PASS ---")

# ---------------------------------------------------------------------- census
def scan(n, q):
    check_time("n=%d q=%d" % (n, q))
    F = GF(q)
    plan = perm_plan(n)
    tiers = [[r for r in plan if r[0] == t] for t in range(4)]
    total = 0
    need_fallback = 0        # no n-cycle works
    h2_viol, h1_viol, cex = [], [], []
    type_hist = {}
    t_start = time.time()
    for flat in itertools.product(range(q), repeat=n*n):
        A = tuple(flat)
        if not det_nonzero(A, n, F):
            continue
        total += 1
        if total % 100000 == 0:
            check_time("n=%d q=%d at %d" % (n, q, total))
        hit = None
        for t in range(4):
            for (_, ct, P) in tiers[t]:
                if cyclic(matmul(A, P, n, F), n, F):
                    hit = (t, ct); break
            if hit:
                break
        if hit is None:
            cex.append(A)
            print("  *** COUNTEREXAMPLE n=%d q=%d A=%s ***" % (n, q, A))
            if len(cex) >= 3:
                break
            continue
        t, ct = hit
        type_hist[ct] = type_hist.get(ct, 0) + 1
        if t >= 1:
            need_fallback += 1
        if t >= 2:
            h2_viol.append((A, ct))
        if t >= 3:
            h1_viol.append((A, ct))
    exp = gl_order(n, q)
    ok = (total == exp)
    print("n=%d q=%d |GL| enum=%d expected=%d POS-2=%s | no-n-cycle=%d | H2 viol=%d | H1 viol=%d | CEX=%d | %.1fs"
          % (n, q, total, exp, ok, need_fallback, len(h2_viol), len(h1_viol), len(cex), time.time()-t_start))
    assert ok or cex, "POS-2 population check FAILED n=%d q=%d" % (n, q)
    hs = sorted(type_hist.items(), key=lambda kv: -kv[1])
    print("     first-success cycle type histogram: %s" % ("; ".join("%s:%d" % (k, v) for k, v in hs[:8])))
    for (A, ct) in h2_viol[:3]:
        print("     H2-violating A (no (n) and no (n-1,1)): %s  first success type %s" % (A, ct))
    for (A, ct) in h1_viol[:3]:
        print("     H1-VIOLATING A (needs >=3 cycles): %s  first success type %s" % (A, ct))
    return cex, h2_viol, h1_viol

print("ROUND 3-A census start; hard limit %ds" % HARD_LIMIT)
run_controls()
print("--- CENSUS ---")
CELLS = [(2,2),(2,3),(2,4),(2,5),(2,7),(2,8),(2,9),(3,2),(3,3),(3,4),(4,2),(3,5)]
any_cex = False
tot_h2, tot_h1 = 0, 0
for (n, q) in CELLS:
    cex, h2, h1 = scan(n, q)
    any_cex = any_cex or bool(cex)
    tot_h2 += len(h2); tot_h1 += len(h1)
print("VERDICT: %s | total H2 violations=%d | total H1 violations=%d | elapsed %.1fs"
      % ("COUNTEREXAMPLE FOUND -- 16.95 REFUTED" if any_cex else "no counterexample in any cell",
         tot_h2, tot_h1, time.time()-T0))
