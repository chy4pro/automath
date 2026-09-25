# -*- coding: utf-8 -*-
"""Is B = O(A)?  And where exactly does the elementary bound on B lose?"""
import math
from math import gcd

N = 400000
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

print("t      |P|     A         B         B/A      A^2/B     (A^2/B)*log t")
for t in [200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]:
    P = [m for m in pr if t < m <= 2 * t]
    A = sum(1.0 / m for m in P)
    B = 0.0
    for i, m in enumerate(P):
        inv = 1.0 / m
        for m2 in P[i:]:
            w = gcd(m, m2) * inv / m2
            B += w if m2 == m else 2 * w
    print(" %-6d %-7d %-9.6f %-9.5f %-8.3f %-9.6f %.4f"
          % (t, len(P), A, B, B / A, A * A / B, (A * A / B) * math.log(t)))

# Where the elementary bound loses: A_g = sum over practical m in (t,2t] with g|m of 1/m,
# compared with the crude bound (log 2)/g + 1/t which ignores that practicals have density 1/log.
print()
print("A_g against the crude bound, t = 20000")
t = 20000
P = [m for m in pr if t < m <= 2 * t]
A = sum(1.0 / m for m in P)
for g in [1, 2, 3, 4, 6, 8, 12, 16, 24, 48, 96, 240, 720]:
    Ag = sum(1.0 / m for m in P if m % g == 0)
    crude = math.log(2.0) / g + 1.0 / t
    print("   g=%-4d A_g=%-10.6f crude=%-10.6f  crude/A_g=%-8.2f  A_g*g/A=%.3f"
          % (g, Ag, crude, crude / Ag if Ag else float('inf'), Ag * g / A))
