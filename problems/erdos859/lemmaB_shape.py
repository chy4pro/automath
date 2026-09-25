# -*- coding: utf-8 -*-
"""Test the model  h(g) := A_g*g/A  =  lambda(g) * log t / log(t/g),  lambda bounded and t-free."""
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

def table(t):
    Ag = defaultdict(float); A = 0.0
    for m in range(t + 1, 2 * t + 1):
        D = prac_divs(m)
        if D is None: continue
        inv = 1.0 / m; A += inv
        for d in D: Ag[d] += inv
    return A, Ag

TS = [16000, 64000, 256000]
tabs = {t: table(t) for t in TS}
print("lambda(g) = h(g) * log(t/g)/log t   at three t.  t-free and bounded?")
print("   g        " + "".join("lam(t=%-7d) " % t for t in TS) + "  sigma(g)/g")
for g in [1,2,4,6,8,12,16,24,48,96,240,720,2160,5040,10080,50400,100000,200000,500000]:
    row = "   %-9d" % g
    ok = True
    for t in TS:
        A, Ag = tabs[t]
        if g > 2 * t or Ag.get(g, 0) == 0:
            row += "%-16s" % "  -"; ok = False; continue
        h = Ag[g] * g / A
        lam = h * math.log(t / g) / math.log(t) if g < t else float('nan')
        row += "%-16.3f" % lam
    sg = sum(d for d in range(1, g + 1) if g % d == 0) / g if g <= 20000 else float('nan')
    print(row + ("  %.3f" % sg if sg == sg else "   -"))

print()
print("Constraint check:  sum_g phi(g) h(g)^2 / g^2  vs  0.8 log^2 t")
for t in TS:
    A, Ag = tabs[t]
    S = sum(phi[g] * (Ag[g] * g / A) ** 2 / (g * g) for g in Ag)
    print("   t=%-8d sum=%-10.2f  log^2 t=%-9.2f  ratio=%.3f" % (t, S, math.log(t) ** 2, S / math.log(t) ** 2))
