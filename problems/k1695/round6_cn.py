#!/usr/bin/env python3
"""ROUND 6-G (line k1695): Combinatorial-Nullstellensatz certificate for (S').

Factorial-base factorisation: every sigma in S_n is uniquely c_{n-1}^{a_{n-1}} ... c_1^{a_1} with
c_k = (1 2 ... k+1) and 0 <= a_k <= k.  So D_i(sigma) = f(a_1..a_{n-1}) on the grid prod {0..k}.
The Lagrange interpolant has degree <= k in a_k; CN: if its top coefficient
   Delta = sum_a prod_k [(-1)^(k-a_k) / (a_k! (k-a_k)!)] * D_i(sigma_a)
is nonzero then some D_i(sigma) != 0.  Question: is Delta(A) a nonzero multiple of det(A)^k as a
polynomial in A?  (n = 3 symbolic, n = 4 numeric over Q.)
"""
import sys, time, itertools, random, math
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
T0 = time.time()

def perm_matrix(s, n):
    return sp.Matrix(n, n, lambda i, j: 1 if s[j] == i else 0)

def compose(s, t):
    """(s o t)(x) = s(t(x))"""
    return tuple(s[t[x]] for x in range(len(s)))

def cyc(k, n):
    """c_k = (0 1 ... k) as a tuple on range(n): x -> x+1 for x<k, k -> 0"""
    return tuple((x+1 if x < k else (0 if x == k else x)) for x in range(n))

def perm_of_a(a, n):
    s = tuple(range(n))
    for k in range(n-1, 0, -1):          # sigma = c_{n-1}^{a_{n-1}} ... c_1^{a_1}
        ck = cyc(k, n)
        for _ in range(a[k-1]):
            s = compose(s, ck)
    return s

def krylov_det(A, s, i, n):
    M = A * perm_matrix(s, n)
    e = sp.zeros(n, 1); e[i] = 1
    cols = [e]; v = e
    for _ in range(n-1):
        v = M * v; cols.append(v)
    return sp.Matrix.hstack(*cols).det()

def delta(A, i, n):
    tot = 0; seen = set()
    for a in itertools.product(*[range(k+1) for k in range(1, n)]):
        s = perm_of_a(a, n); seen.add(s)
        w = sp.Integer(1)
        for k in range(1, n):
            ak = a[k-1]
            w *= sp.Integer((-1)**(k-ak)) / (math.factorial(ak) * math.factorial(k-ak))
        tot += w * krylov_det(A, s, i, n)
    assert len(seen) == math.factorial(n), "factorisation is not a bijection"
    return sp.expand(tot)

print("ROUND 6-G: CN top coefficient Delta")
n = 3
syms = sp.symbols('a0:%d' % (n*n)); A = sp.Matrix(n, n, syms)
D = delta(A, 0, n)
print("n=3 symbolic Delta = %s" % sp.factor(D))
detA = sp.expand(A.det())
print("n=3: Delta == c*det(A)? remainder zero: %s" % (sp.rem(sp.Poly(D, *syms), sp.Poly(detA, *syms)) == 0))
random.seed(7)
for n in (4,):
    rat = set(); zeros = 0
    for t in range(10):
        A = sp.Matrix(n, n, lambda i, j: random.randint(-3, 3))
        dA = A.det()
        if dA == 0: continue
        D = delta(A, 0, n)
        if D == 0: zeros += 1
        r = sp.Rational(D, dA**1)
        rat.add(r)
        print("n=4 trial %d det=%s Delta=%s Delta/det=%s" % (t, dA, D, r))
    print("n=4: Delta zero in %d trials; distinct Delta/det = %d  [%.1fs]" % (zeros, len(rat), time.time()-T0))
print("done")
