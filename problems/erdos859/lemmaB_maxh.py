# -*- coding: utf-8 -*-
"""max_g h(g), h(g)=A_g*g/A, against sqrt(log t).  And B against a + b*loglog t."""
import math
from collections import defaultdict
NMAX = 1000000
spf = list(range(NMAX + 1))
for p in range(2, int(NMAX ** 0.5) + 1):
    if spf[p] == p:
        for m in range(p * p, NMAX + 1, p):
            if spf[m] == m: spf[m] = p
phi = list(range(NMAX + 1))
for p in range(2, NMAX + 1):
    if spf[p] == p:
        for m in range(p, NMAX + 1, p): phi[m] -= phi[m] // p

def prac_divs(n):
    if n == 1: return [1]
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
    D = [1]
    for p, e in f:
        D = [d * p ** i for d in D for i in range(e + 1)]
    return D

print("  t        A         B         maxh   argmax   sqrt(log t)  maxh/sqrt   B_fit(0.123+0.179ll)")
t = 2000
while 2 * t <= NMAX:
    Ag = defaultdict(float); A = 0.0
    for m in range(t + 1, 2 * t + 1):
        D = prac_divs(m)
        if D is None: continue
        inv = 1.0 / m; A += inv
        for d in D: Ag[d] += inv
    B = sum(phi[g] * v * v for g, v in Ag.items())
    mh, arg = 0.0, 0
    for g, v in Ag.items():
        h = v * g / A
        if h > mh: mh, arg = h, g
    L = math.log(t); ll = math.log(L)
    print("  %-8d %-9.6f %-9.5f %-6.3f %-8d %-12.4f %-11.3f %.4f"
          % (t, A, B, mh, arg, math.sqrt(L), mh / math.sqrt(L), 0.123 + 0.179 * ll))
    t *= 2
