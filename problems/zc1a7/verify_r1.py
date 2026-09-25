#!/usr/bin/env python3
"""
zc1a7 ROUND 1, step 3: INDEPENDENT re-verification (doctrine s105).

Shares NOTHING with a7_table.py / helpr1.py:
  * the group is built by sympy's AlternatingGroup(7), not by hand-rolled tuples;
  * conjugacy classes come from sympy's PermutationGroup.conjugacy_classes();
  * the ordinary character table is computed by DIXON's modular algorithm
    (class-sum matrices, common eigenvectors over F_p with p = 421 = 420+1,
    exp(A_7) = 420 | p-1), NOT by Murnaghan-Nakayama;
  * the HeLP inequality is evaluated with the LUTHAR-PASSI TRACE FORMULA as
    printed in arXiv:2006.09031 Thm 2.5,
        (1/n) sum_{d|n} Tr_{Q(zeta^d)/Q}( chi(u^d) zeta^{-d l} ),
    NOT with the discrete-Fourier multiplicity formula used in helpr1.py;
  * the 7-modular Brauer character of degree 5 is obtained from EXPLICIT MATRICES
    over F_7 (characteristic polynomial factorisation), not from "pi - 2".

POSITIVE CONTROLS (doctrine s62), each with a known answer:
  K1 sum of squares of the Dixon degrees = |A_7| = 2520.
  K2 the same HeLP formula applied to an ACTUAL GROUP ELEMENT h of order 4
     must return h's true eigenvalue multiplicities: checked against the
     eigenvalues of the explicit 7x7 permutation matrix of h (the 7-point
     permutation representation = 1 + chi_{deg 6}).
  K3 the formula must REJECT things it should reject: t = 4 and t = -4 are
     checked to be excluded (a probe that accepts everything is worthless).
  K4 the F_7 Brauer character value must agree with chi_{deg 6} - 1 on 2a, 4a.
"""

import itertools, random
import sympy as sp
from sympy.combinatorics.named_groups import AlternatingGroup
from sympy.combinatorics import Permutation

P = 421                      # prime, 420 = exp(A_7) divides P-1
assert sp.isprime(P)

G = AlternatingGroup(7)
ELTS = list(G.elements)
NG = len(ELTS)
assert NG == 2520
print("group order (sympy AlternatingGroup(7)) :", NG)

CC = G.conjugacy_classes()
CC = sorted(CC, key=lambda c: (min(x.order() for x in c), len(c)))
NCL = len(CC)
REPS = [sorted(c, key=lambda x: x.array_form)[0] for c in CC]
SIZE = [len(c) for c in CC]
ORD = [r.order() for r in REPS]
MEMB = {}
for k, c in enumerate(CC):
    for x in c:
        MEMB[x.array_form and tuple(x.array_form)] = k

def cls(x):
    return MEMB[tuple(x.array_form)]

print("classes (order,size) :", list(zip(ORD, SIZE)))
assert NCL == 9

# ---- class-sum structure constants  a_{k,i,j} : Chat_k Chat_i = sum_j a_{k,i,j} Chat_j
def struct(k, i, j):
    z = REPS[j]
    n = 0
    for x in CC[k]:
        y = x**-1 * z
        if cls(y) == i:
            n += 1
    return n

Amat = [[[struct(k, i, j) for j in range(NCL)] for i in range(NCL)] for k in range(NCL)]

# ---- Dixon: common eigenvectors of the M_k over F_P
F = sp.GF(P)
Ms = [sp.Matrix(NCL, NCL, lambda i, j: Amat[k][i][j] % P) for k in range(NCL)]

random.seed(20260823)
omegas = None
for attempt in range(30):
    r = [random.randrange(P) for _ in range(NCL)]
    M = sp.zeros(NCL, NCL)
    for k in range(NCL):
        M += r[k]*Ms[k]
    M = M.applyfunc(lambda x: x % P)
    found = []
    for lam in range(P):
        A = (M - lam*sp.eye(NCL)).applyfunc(lambda x: x % P)
        ns = A.nullspace(iszerofunc=lambda x: x % P == 0) if False else None
        # nullspace over F_P by hand: row reduce mod P
        Awork = [[int(A[i, j]) % P for j in range(NCL)] for i in range(NCL)]
        piv = []
        row = 0
        for col in range(NCL):
            sel = None
            for rr in range(row, NCL):
                if Awork[rr][col] % P:
                    sel = rr; break
            if sel is None:
                continue
            Awork[row], Awork[sel] = Awork[sel], Awork[row]
            inv = pow(Awork[row][col], P-2, P)
            Awork[row] = [(v*inv) % P for v in Awork[row]]
            for rr in range(NCL):
                if rr != row and Awork[rr][col] % P:
                    f = Awork[rr][col]
                    Awork[rr] = [(Awork[rr][cc] - f*Awork[row][cc]) % P for cc in range(NCL)]
            piv.append(col); row += 1
            if row == NCL:
                break
        free = [c for c in range(NCL) if c not in piv]
        if len(free) == 1:
            fc = free[0]
            v = [0]*NCL
            v[fc] = 1
            for ri, pc in enumerate(piv):
                v[pc] = (-Awork[ri][fc]) % P
            found.append(v)
    if len(found) == NCL:
        omegas = found
        break
assert omegas is not None and len(omegas) == NCL, "Dixon eigenvector split failed"

one = [k for k in range(NCL) if ORD[k] == 1][0]
omegas = [[(v[k]*pow(v[one], P-2, P)) % P for k in range(NCL)] for v in omegas]

# class of inverses
INV = [cls(REPS[k]**-1) for k in range(NCL)]

DEGREES = []
CHARP = []                    # character values mod P
for w in omegas:
    s = 0
    for k in range(NCL):
        s = (s + w[k]*w[INV[k]]*pow(SIZE[k], P-2, P)) % P
    d2 = (NG % P)*pow(s, P-2, P) % P
    d = None
    for cand in range(1, 60):
        if (cand*cand) % P == d2:
            d = cand; break
    assert d is not None, "could not lift a degree"
    DEGREES.append(d)
    CHARP.append([(w[k]*d*pow(SIZE[k], P-2, P)) % P for k in range(NCL)])

order_idx = sorted(range(NCL), key=lambda i: DEGREES[i])
DEGREES = [DEGREES[i] for i in order_idx]
CHARP = [CHARP[i] for i in order_idx]

print("Dixon degrees :", DEGREES)
print("K1  sum of squares =", sum(d*d for d in DEGREES), "(want 2520) :",
      "OK" if sum(d*d for d in DEGREES) == NG else "FAIL")

# ---- which classes are RATIONAL (needed to lift mod-P values to Z by symmetric rep)
def is_rational_class(k):
    m = ORD[k]
    g = REPS[k]
    for j in range(1, m):
        if sp.gcd(j, m) == 1 and cls(g**j) != k:
            return False
    return True

RAT = [is_rational_class(k) for k in range(NCL)]
print("rational classes (order,size,rational) :",
      [(ORD[k], SIZE[k], RAT[k]) for k in range(NCL)])

def lift(v):
    """symmetric representative mod P; valid because |chi(g)| <= chi(1) <= 35 < P/2"""
    v %= P
    return v - P if v > P//2 else v

# indices of 1a, 2a, 4a
i1a = [k for k in range(NCL) if ORD[k] == 1][0]
i2a = [k for k in range(NCL) if ORD[k] == 2][0]
i4a = [k for k in range(NCL) if ORD[k] == 4][0]
for k in (i1a, i2a, i4a):
    assert RAT[k], "class of order %d is not rational -- lifting invalid" % ORD[k]
assert len([k for k in range(NCL) if ORD[k] == 2]) == 1
assert len([k for k in range(NCL) if ORD[k] == 4]) == 1

VAL = {}                       # (i, class) -> exact integer, for 1a,2a,4a only
for i in range(NCL):
    for k in (i1a, i2a, i4a):
        VAL[(i, k)] = lift(CHARP[i][k])
    assert VAL[(i, i1a)] == DEGREES[i], "degree mismatch on 1a"

print("\nindependent (Dixon) values on 1a,2a,4a:")
for i in range(NCL):
    print("   deg %-3d  chi(2a) = %-4d  chi(4a) = %-4d"
          % (DEGREES[i], VAL[(i, i2a)], VAL[(i, i4a)]))

# ---- 7-modular Brauer character of degree 5 from EXPLICIT F_7 MATRICES
def perm_matrix_F7(g, n=7):
    return sp.Matrix(n, n, lambda i, j: 1 if g(j) == i else 0)

def brauer_val_2element(g):
    """
    Brauer character value at a 2-element g of the F_7 A_7-module S/<1>,
    S = sum-zero subspace of F_7^7 (7 = 0 in F_7, so <1> < S).
    Eigenvalues of a 2-element are 4th roots of unity; over F_7 (7 = 3 mod 4)
    x^2+1 is irreducible, so the eigenvalue pair {i,-i} contributes i + (-i) = 0
    and the Brauer value is  m(1) - m(-1)  read off the F_7 characteristic
    polynomial of the induced action.  No lifting ambiguity.
    """
    Mp = perm_matrix_F7(g)
    # basis of S: e_j - e_0 (j=1..6) ... but <1> is inside S; build S/<1> explicitly.
    # S = {v : sum v_i = 0}.  basis s_j = e_j - e_0, j=1..6.
    S = [[0]*7 for _ in range(6)]
    for j in range(1, 7):
        S[j-1][j] = 1
        S[j-1][0] = -1
    Sm = sp.Matrix(S).T                        # 7x6, columns = basis of S
    # coordinates of 1 = (1,...,1) in that basis: 1 = -7 e_0 + sum_j (e_j - e_0)? check:
    # sum_j (e_j - e_0) = (sum_{j>=1} e_j) - 6 e_0 = (1,..,1) - 7 e_0 = (1,...,1) in F_7.
    onevec = sp.Matrix([1]*6)                  # coefficients (1,1,1,1,1,1)
    # action of g on S in these coordinates:
    def act_on_S(v6):
        v7 = Sm*v6
        w7 = Mp*v7
        # solve Sm x = w7 over F_7 : since w7 has coordinate sum 0, x_j = w7_j + ... use
        # x_j = w7[j] and check w7[0] = -sum x_j
        x = sp.Matrix([w7[j] % 7 for j in range(1, 7)])
        assert (sum(w7) % 7) == 0
        return x
    A = sp.zeros(6, 6)
    for j in range(6):
        e = sp.zeros(6, 1); e[j] = 1
        col = act_on_S(e)
        for i in range(6):
            A[i, j] = col[i] % 7
    # quotient by the line spanned by onevec: choose complement basis
    # build change of basis with onevec first
    B = sp.zeros(6, 6)
    for i in range(6):
        B[i, 0] = onevec[i]
    cols = 1
    for j in range(6):
        if cols == 6:
            break
        cand = sp.zeros(6, 1); cand[j] = 1
        test = B[:, :cols].row_join(cand)
        if sp.Matrix(test).rank(iszerofunc=lambda x: x % 7 == 0) > cols if False else True:
            # rank over F_7
            T = [[int(test[a, b]) % 7 for b in range(cols+1)] for a in range(6)]
            # gaussian elimination mod 7 to get rank
            rk = 0; rr = 0
            for cc in range(cols+1):
                sel = None
                for r2 in range(rr, 6):
                    if T[r2][cc] % 7:
                        sel = r2; break
                if sel is None:
                    continue
                T[rr], T[sel] = T[sel], T[rr]
                inv = pow(T[rr][cc], 5, 7)
                T[rr] = [(v*inv) % 7 for v in T[rr]]
                for r2 in range(6):
                    if r2 != rr and T[r2][cc] % 7:
                        f = T[r2][cc]
                        T[r2] = [(T[r2][c3] - f*T[rr][c3]) % 7 for c3 in range(cols+1)]
                rr += 1; rk += 1
            if rk == cols+1:
                for i in range(6):
                    B[i, cols] = cand[i]
                cols += 1
    assert cols == 6
    Binv = B.inv_mod(7)
    Ahat = (Binv*A*B).applyfunc(lambda x: x % 7)
    # the quotient action is the lower-right 5x5 block (first basis vector spans <1>,
    # which is g-invariant)
    for i in range(1, 6):
        assert Ahat[i, 0] % 7 == 0, "the line <1> is not invariant -- construction wrong"
    Q = Ahat[1:, 1:]
    x = sp.Symbol("x")
    cp = sp.Poly(Q.charpoly(x).as_expr(), x, modulus=7)
    fl = sp.factor_list(cp.as_expr(), x, modulus=7)
    m1 = m_1 = 0
    for fac, mult in fl[1]:
        f = sp.Poly(fac, x, modulus=7)
        if f.degree() == 1:
            root = (-f.all_coeffs()[1]*pow(int(f.all_coeffs()[0]), 5, 7)) % 7
            if root == 1:
                m1 += mult
            elif root == 6:
                m_1 += mult
            else:
                raise AssertionError("eigenvalue %d is not a 4th root of unity" % root)
        elif f.degree() == 2:
            assert sp.expand(f.as_expr() - (x**2 + 1)) == 0 or \
                   sp.simplify(sp.Poly(f.as_expr() - (x**2+1), x, modulus=7).as_expr()) == 0, \
                   "unexpected quadratic factor %s" % f
        else:
            raise AssertionError("unexpected factor of degree %d" % f.degree())
    return m1 - m_1, fl

g2 = REPS[i2a]
g4 = REPS[i4a]
b2, _ = brauer_val_2element(g2)
b4, _ = brauer_val_2element(g4)
chi6 = [i for i in range(NCL) if DEGREES[i] == 6][0]
print("\nK4  7-modular Brauer character of the 5-dim module, from F_7 matrices:")
print("      phi(2a) = %d   (chi_{deg6}(2a) - 1 = %d)" % (b2, VAL[(chi6, i2a)] - 1))
print("      phi(4a) = %d   (chi_{deg6}(4a) - 1 = %d)" % (b4, VAL[(chi6, i4a)] - 1))
K4 = (b2 == VAL[(chi6, i2a)] - 1) and (b4 == VAL[(chi6, i4a)] - 1)
print("      K4 : %s" % ("OK" if K4 else "FAIL"))

# ---------------------------------------------------------------- HeLP, trace formula

zeta4 = sp.I

def trace_formula_mult(chi_1, chi_u, chi_u2, ell):
    """
    (1/4) sum_{d|4} Tr_{Q(zeta^d)/Q}( chi(u^d) zeta^{-d l} ),  zeta = i.
    d=1 : Q(i)/Q, Galois {1, complex conj}: Tr(chi(u) i^{-l}) = chi(u)(i^{-l} + i^{l})
          (chi(u) is a rational integer here: classes 2a, 4a are rational)
    d=2 : Q(-1)=Q : chi(u^2) (-1)^{-l}
    d=4 : Q       : chi(1)
    """
    t1 = chi_u*(zeta4**(-ell) + zeta4**(ell))
    t2 = chi_u2*sp.Integer(-1)**(-ell)
    t4 = chi_1
    return sp.simplify(sp.expand(sp.Rational(1, 4)*(t1 + t2 + t4)))

t = sp.Symbol("t", integer=True)

# characters usable for |u| = 4 : all ordinary + the 7-modular 5-dim one
CHARS = []
for i in range(NCL):
    CHARS.append(("ordinary deg %d" % DEGREES[i], DEGREES[i], VAL[(i, i2a)], VAL[(i, i4a)]))
CHARS.append(("7-modular deg 5 (F_7 matrices)", 5, b2, b4))

print("\n--- HeLP for |u| = 4 via the Luthar-Passi TRACE formula")
lo, hi = -sp.oo, sp.oo
for name, d1, v2a, v4a in CHARS:
    chi_u = t*v2a + (1 - t)*v4a
    for ell in range(4):
        mu = sp.expand(trace_formula_mult(d1, chi_u, v2a, ell))
        pol = sp.Poly(mu, t)
        assert pol.degree() <= 1
        b = pol.coeff_monomial(t); a = pol.coeff_monomial(1)
        if b > 0:
            lo = max(lo, sp.ceiling(-a/b))
        elif b < 0:
            hi = min(hi, sp.floor(-a/b))
print("    proven interval : %s <= t <= %s" % (lo, hi))

# congruence (Prop. partial augmentations (iii)), p = 2, j = 1, D = 2a :
#   sum_{C : C^2 subset 2a} eps_C(u) = eps_2a(u^2) = 1  (mod 2)
sq_to_2a = [k for k in range(NCL) if cls(REPS[k]**2) == i2a]
print("    classes squaring into 2a :", [(ORD[k], SIZE[k]) for k in sq_to_2a])
assert sq_to_2a == [i4a]
print("    => eps_4a(u) = 1 - t = 1 (mod 2)  =>  t even")

surv = []
for v in range(int(lo), int(hi)+1):
    if (1 - v) % 2 != 1 % 2:
        continue
    ok = True
    for name, d1, v2a, v4a in CHARS:
        chi_u = v*v2a + (1 - v)*v4a
        for ell in range(4):
            mu = trace_formula_mult(d1, chi_u, v2a, ell)
            if mu < 0 or not sp.Integer(mu) == mu:
                ok = False
    if ok:
        surv.append(v)
print("    SURVIVORS (eps_2a, eps_4a) :", [(v, 1-v) for v in surv])

# ---- K3 : the probe must reject
print("\nK3  rejection control:")
for v in (-4, -2, 1, 3, 4):
    bad = []
    for name, d1, v2a, v4a in CHARS:
        chi_u = v*v2a + (1 - v)*v4a
        for ell in range(4):
            mu = trace_formula_mult(d1, chi_u, v2a, ell)
            if mu < 0:
                bad.append((name, ell, mu))
    cong_ok = ((1 - v) % 2 == 1)
    print("    t = %2d : rejected by %d inequalities%s ; congruence %s"
          % (v, len(bad), (" (first: %s l=%d mu=%s)" % bad[0] if bad else ""),
             "OK" if cong_ok else "FAILS"))

# ---- K2 : the same formula on an ACTUAL group element of order 4
print("\nK2  positive control -- the formula applied to a real group element h in 4a")
h = REPS[i4a]
Mh = sp.Matrix(7, 7, lambda i, j: 1 if h(j) == i else 0)
ev = Mh.eigenvals()
print("    eigenvalues of the 7x7 permutation matrix of h :",
      {sp.simplify(k): v for k, v in ev.items()})
mult_true = {}
for k, m in ev.items():
    mult_true[sp.simplify(k)] = m
# the 7-point permutation character = 1 + chi_{deg 6}; the formula with the TRIVIAL
# distribution eps_4a = 1 must return exactly those multiplicities for chi_{deg 6}
d6 = 6
v2a6, v4a6 = VAL[(chi6, i2a)], VAL[(chi6, i4a)]
pred = []
for ell in range(4):
    mu = trace_formula_mult(d6, v4a6, v2a6, ell)     # trivial distribution: chi(u) = chi(4a)
    pred.append(mu)
print("    predicted multiplicities of (1, i, -1, -i) on the degree-6 constituent :", pred)
obs = [mult_true.get(sp.Integer(1), 0) - 1, mult_true.get(sp.I, 0),
       mult_true.get(sp.Integer(-1), 0), mult_true.get(-sp.I, 0)]
print("    observed from the permutation matrix, minus the trivial summand    :", obs)
print("    K2 : %s" % ("OK" if [sp.Integer(x) for x in pred] == [sp.Integer(x) for x in obs] else "FAIL"))

print("\n=== INDEPENDENT VERDICT ===")
print("HeLP solution set for |u| = 4 in V(Z A_7) :", [(v, 1-v) for v in surv])
