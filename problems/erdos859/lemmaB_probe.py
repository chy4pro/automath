# -*- coding: utf-8 -*-
"""B(t) = sum_g phi(g) A_g^2 computed via divisors of practicals, not pairwise gcds.
Lets t reach 1e6 instead of 2e5.  Also measures h(g) = A_g*g/A over a wide g range."""
import sys, math
from collections import defaultdict

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000000

# smallest prime factor + totient sieve
spf = list(range(NMAX + 1))
for p in range(2, int(NMAX ** 0.5) + 1):
    if spf[p] == p:
        for m in range(p * p, NMAX + 1, p):
            if spf[m] == m:
                spf[m] = p

phi = list(range(NMAX + 1))
for p in range(2, NMAX + 1):
    if spf[p] == p:
        for m in range(p, NMAX + 1, p):
            phi[m] -= phi[m] // p

def factor(n):
    f = []
    while n > 1:
        p = spf[n]; e = 0
        while n % p == 0:
            n //= p; e += 1
        f.append((p, e))
    return f

def practical_and_divs(n):
    """Stewart's criterion; returns (is_practical, divisor list) -- divisors only if practical."""
    if n == 1: return True, [1]
    if n % 2: return False, None
    f = factor(n)
    s = 1
    for p, e in f:
        if p > s + 1: return False, None
        s *= (p ** (e + 1) - 1) // (p - 1)
    D = [1]
    for p, e in f:
        D = [d * p ** i for d in D for i in range(e + 1)]
    return True, D

print("NMAX = %d" % NMAX)
print("  t         |P|      A          B          B/A      A^2/B      loglog t")
rows = []
t = 1000
while 2 * t <= NMAX:
    Ag = defaultdict(float)
    A = 0.0; cnt = 0
    for m in range(t + 1, 2 * t + 1):
        ok, D = practical_and_divs(m)
        if not ok: continue
        cnt += 1; inv = 1.0 / m; A += inv
        for d in D:
            Ag[d] += inv
    B = 0.0
    for g, v in Ag.items():
        B += phi[g] * v * v
    print("  %-9d %-8d %-10.6f %-10.5f %-8.3f %-10.6f %.4f"
          % (t, cnt, A, B, B / A, A * A / B, math.log(math.log(t))))
    rows.append((t, A, B))
    t *= 2
