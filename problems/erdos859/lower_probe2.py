# -*- coding: utf-8 -*-
"""Second-moment bound for the practical-divisor family, against the true density."""
import math
from math import gcd

N = 200000
divs = [[] for _ in range(N + 1)]
for d in range(1, N + 1):
    for m in range(d, N + 1, d):
        divs[m].append(d)

def is_practical(m):
    if m == 1: return True
    D = divs[m]
    if D[0] != 1: return False
    s = 0
    for d in D:
        if d > s + 1: return False
        s += d
    return True

pr = [m for m in range(1, N + 1) if is_practical(m)]

def in_At(n, t):
    reach = 1
    for d in divs[n]:
        if d > t: break
        reach |= reach << d
        reach &= (1 << (t + 1)) - 1
        if (reach >> t) & 1: return True
    return (reach >> t) & 1 == 1

print(" t    |P|    A        B        A^2/B     dens(union)  true d_t   union/d_t")
for t in [50, 100, 200, 400, 800]:
    P = [m for m in pr if t < m <= 2 * t]
    A = sum(1.0 / m for m in P)
    B = 0.0
    for i, m in enumerate(P):
        for m2 in P[i:]:
            g = gcd(m, m2)
            w = g / (m * m2)
            B += w if m2 == m else 2 * w
    # exact density of the union of multiples, measured on [1,N]
    hit = bytearray(N + 1)
    for m in P:
        for k in range(m, N + 1, m):
            hit[k] = 1
    du = sum(hit) / N
    dt = sum(1 for n in range(1, N + 1) if in_At(n, t)) / N
    print(" %-4d %-6d %-8.5f %-8.4f %-9.5f %-12.5f %-10.5f %.3f"
          % (t, len(P), A, B, A * A / B, du, dt, du / dt))
