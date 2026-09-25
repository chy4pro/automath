#!/usr/bin/env python3
"""round2_rank_spotcheck.py -- FOURTH path to the single most load-bearing
NEGATIVE claim of round 2 (section R8: the n-cycle rule is false in
characteristic 2 for n = 2 mod 4).

Neither minimal-polynomial degree (round 2 main script) nor commutant nullity
(round 2 main script) nor the determinantal divisor (independent checker) is
used here.  Only: a matrix fails to be nonderogatory as soon as SOME eigenvalue
has geometric multiplicity >= 2, i.e. rank(M - lam I) <= n-2.  Pure rank, over
F_p, via sympy's GF domain rref.  Exact arithmetic.  Interpreter: .venv/bin/python3
"""
import sympy
from sympy import Matrix, GF
from sympy.polys.matrices import DomainMatrix


def J_minus_P(sig):
    n = len(sig)
    return [[1 - (1 if sig[j] == i else 0) for j in range(n)] for i in range(n)]


def type_perm(lam):
    s = []; b = 0
    for L in lam:
        s += [b + (k + 1) % L for k in range(L)]; b += L
    return s


def max_geom_mult(M, p):
    n = len(M); worst = 0
    for l in range(p):
        A = [[(M[i][j] - (l if i == j else 0)) % p for j in range(n)] for i in range(n)]
        R = DomainMatrix.from_Matrix(Matrix(A)).convert_to(GF(p)).rref()[0].to_Matrix()
        rr = sum(1 for i in range(n) if any(R[i, j] % p for j in range(n)))
        worst = max(worst, n - rr)
    return worst


print("k1695 round 2 -- fourth-path rank spot-check of section R8")
print("claim: char F = 2, n = 2 mod 4  =>  J - (n-cycle) is NOT cyclic,")
print("       while J - ((n-1)-cycle + fixed point) has no such obstruction.")
print()
print("%-4s %-4s %-10s %-28s %s" % ("p", "n", "type", "max geometric multiplicity", "verdict"))
p = 2
for n in (6, 10, 14, 18):
    for lam in ((n,), (n - 1, 1)):
        g = max_geom_mult(J_minus_P(type_perm(lam)), p)
        print("%-4d %-4d %-10s %-28d %s" % (p, n, "+".join(map(str, lam)), g,
              "DEROGATORY -> not cyclic" if g >= 2 else "no F_p obstruction"))
print()
print("CONTROL that could have gone the other way: n = 0 mod 4, same char.")
print("If the n-cycle were derogatory here too the R8 corollary would be vacuous.")
print("%-4s %-4s %-10s %-28s %s" % ("p", "n", "type", "max geometric multiplicity", "verdict"))
for n in (4, 8, 12):
    g = max_geom_mult(J_minus_P(type_perm((n,))), p)
    print("%-4d %-4d %-10s %-28d %s" % (p, n, str(n), g,
          "DEROGATORY -> not cyclic" if g >= 2 else "no F_p obstruction"))
