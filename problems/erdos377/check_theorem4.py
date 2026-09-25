# -*- coding: utf-8 -*-
"""Is EGRS Theorem 4's printed c(alpha) -> 1 right for NONDIVISORS, or for DIVISORS?
v_p(C(2n,n)) = (2 s_p(n) - s_p(2n))/(p-1)  (Legendre).  m | C(2n,n) iff v_p(m) <= v_p(C) for all p."""
import math
def sdig(n, p):
    s = 0
    while n: s += n % p; n //= p
    return s
def vp_central(n, p):
    return (2 * sdig(n, p) - sdig(2 * n, p)) // (p - 1)
def factor(m):
    f = {}; x = m; d = 2
    while d * d <= x:
        while x % d == 0: f[d] = f.get(d, 0) + 1; x //= d
        d += 1
    if x > 1: f[x] = f.get(x, 0) + 1
    return f
def divides(m, n):
    for p, a in factor(m).items():
        if vp_central(n, p) < a: return False
    return True

print("n        alpha   M=n^a    #nondiv   c_nondiv   #div    c_div")
for n in [10**4, 10**5, 10**6, 10**7]:
    for al in [1/2, 1/3, 1/4, 1/5]:
        M = int(n ** al)
        nd = sum(1 for m in range(1, M + 1) if not divides(m, n))
        print(" %-8d %.3f   %-8d %-9d %-10.4f %-7d %.4f"
              % (n, al, M, nd, nd / M, M - nd, (M - nd) / M))
    print()
