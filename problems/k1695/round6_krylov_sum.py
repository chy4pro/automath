#!/usr/bin/env python3
"""ROUND 6-F (line k1695): symmetrised Krylov determinants.

D_i(sigma) := det[e_i, M e_i, M^2 e_i, ..., M^{n-1} e_i],  M = A P_sigma.
(S') says: for every A in GL(n,F) and every i some D_i(sigma) != 0.
Experiment: are  S_plus = sum_sigma D_i(sigma)  or  S_minus = sum_sigma sgn(sigma) D_i(sigma)
nonzero multiples of det(A)^k (as polynomials in the entries of A)?  If yes for some n, that is a
one-line proof of (S') for that n (over every field where the constant is nonzero).
n = 3 fully symbolic (sympy); n = 4, 5 numerically over Q with random integer A, testing whether
S/det(A)^k is constant, and symbolically for the leading structure if cheap.
"""
import sys, time, itertools, random
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
T0 = time.time()

def perm_matrix(s, n):
    return sp.Matrix(n, n, lambda i, j: 1 if s[j] == i else 0)

def sign(s):
    n = len(s); sg = 1; seen = [False]*n
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = s[j]; L += 1
            if L % 2 == 0: sg = -sg
    return sg

def krylov_det(A, s, i, n):
    M = A * perm_matrix(s, n)
    e = sp.zeros(n, 1); e[i] = 1
    cols = [e]; v = e
    for _ in range(n-1):
        v = M * v; cols.append(v)
    return sp.Matrix.hstack(*cols).det()

print("ROUND 6-F: symmetrised Krylov determinants")
# ---- n = 3 symbolic
n = 3
syms = sp.symbols('a0:%d' % (n*n))
A = sp.Matrix(n, n, syms)
Sp = 0; Sm = 0
for s in itertools.permutations(range(n)):
    d = sp.expand(krylov_det(A, s, 0, n))
    Sp += d; Sm += sign(s) * d
Sp = sp.expand(Sp); Sm = sp.expand(Sm)
detA = sp.expand(A.det())
print("n=3 symbolic: S_plus = %s" % sp.factor(Sp))
print("n=3 symbolic: S_minus = %s" % sp.factor(Sm))
print("n=3: S_plus mod det(A) remainder zero? %s ; S_minus mod det(A) zero? %s"
      % (sp.simplify(sp.rem(sp.Poly(Sp, *syms), sp.Poly(detA, *syms))) == 0 if Sp != 0 else 'S_plus==0',
         sp.simplify(sp.rem(sp.Poly(Sm, *syms), sp.Poly(detA, *syms))) == 0 if Sm != 0 else 'S_minus==0'))
print("   [%.1fs]" % (time.time()-T0))

# ---- n = 4, 5 numeric over Q
random.seed(1695)
for n in (4, 5):
    perms = list(itertools.permutations(range(n)))
    ratios_p = set(); ratios_m = set(); zero_p = 0; zero_m = 0
    trials = 12 if n == 4 else 5
    for t in range(trials):
        A = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
        dA = A.det()
        if dA == 0: continue
        Sp = 0; Sm = 0
        for s in perms:
            d = krylov_det(A, s, 0, n)
            Sp += d; Sm += sign(s) * d
        # degree of D in A is n(n-1)/2; det A has degree n -> compare with dA^k for k = n(n-1)/(2n) = (n-1)/2
        if Sp == 0: zero_p += 1
        if Sm == 0: zero_m += 1
        ratios_p.add(sp.Rational(Sp, dA) if dA else None)
        ratios_m.add(sp.Rational(Sm, dA) if dA else None)
        print("n=%d trial %d: det=%s S_plus=%s S_minus=%s  S_plus/det=%s S_minus/det=%s" % (n, t, dA, Sp, Sm, sp.Rational(Sp, dA), sp.Rational(Sm, dA)))
    print("n=%d: S_plus zero in %d trials, S_minus zero in %d trials; distinct S_plus/det ratios=%d, S_minus/det ratios=%d  [%.1fs]"
          % (n, zero_p, zero_m, len(ratios_p), len(ratios_m), time.time()-T0))
print("done")
