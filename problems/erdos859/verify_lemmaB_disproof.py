# -*- coding: utf-8 -*-
"""Independent check of the Astra chain:  B >= S^2 / H_phi,  S(t) ~ c (log t)^delta,
delta = 0.7136125 (Weingartner Thm 3), hence B >> (log t)^{2delta-1} = (log t)^0.4272."""
import math
NMAX = 2000000
spf = list(range(NMAX + 1))
for p in range(2, int(NMAX ** 0.5) + 1):
    if spf[p] == p:
        for m in range(p * p, NMAX + 1, p):
            if spf[m] == m: spf[m] = p
phi = list(range(NMAX + 1))
for p in range(2, NMAX + 1):
    if spf[p] == p:
        for m in range(p, NMAX + 1, p): phi[m] -= phi[m] // p

def prac_tau_divs(n):
    """returns (tau, divisor list) if n practical else None"""
    if n == 1: return (1, [1])
    if n % 2: return None
    f = []; x = n
    while x > 1:
        p = spf[x]; e = 0
        while x % p == 0: x //= p; e += 1
        f.append((p, e))
    s = 1
    for p, e in f:
        if p > s + 1: return None
        s *= (p ** (e + 1) - 1) // (p - 1)
    tau = 1
    for _, e in f: tau *= (e + 1)
    D = [1]
    for p, e in f:
        D = [d * p ** i for d in D for i in range(e + 1)]
    return (tau, D)

# H_phi(x) = sum_{g<=x} 1/phi(g)
Hcum = [0.0] * (NMAX + 1)
acc = 0.0
for g in range(1, NMAX + 1):
    acc += 1.0 / phi[g]
    Hcum[g] = acc

DELTA = 0.7136125
print("  t         S(t)      S/(log t)^d   H_phi(2t)  S^2/H_phi   B(t)     ratio B/(S^2/H)  (log t)^0.4272")
t = 1000
from collections import defaultdict
while 2 * t <= NMAX:
    Ag = defaultdict(float); S = 0.0; A = 0.0
    for m in range(t + 1, 2 * t + 1):
        r = prac_tau_divs(m)
        if r is None: continue
        tau, D = r; inv = 1.0 / m
        A += inv; S += tau * inv
        for d in D: Ag[d] += inv
    B = sum(phi[g] * v * v for g, v in Ag.items())
    H = Hcum[2 * t]
    L = math.log(t)
    print("  %-9d %-9.4f %-13.4f %-10.3f %-11.5f %-8.5f %-16.3f %.4f"
          % (t, S, S / L ** DELTA, H, S * S / H, B, B / (S * S / H), L ** (2 * DELTA - 1)))
    t *= 2
