# -*- coding: utf-8 -*-
"""Which g dominate B = sum_g phi(g) A_g^2 ?  This pins down what the missing lemma must control."""
import math
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

def phi(n):
    r = n; x = n; p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0: x //= p
            r -= r // p
        p += 1
    if x > 1: r -= r // x
    return r

for t in [5000, 20000, 50000]:
    P = [m for m in pr if t < m <= 2 * t]
    A = sum(1.0 / m for m in P)
    # A_g for every g that divides at least one m in P
    from collections import defaultdict
    Ag = defaultdict(float)
    for m in P:
        inv = 1.0 / m
        for g in divs[m]:
            Ag[g] += inv
    terms = [(phi(g) * v * v, g, v) for g, v in Ag.items()]
    B = sum(x[0] for x in terms)
    terms.sort(reverse=True)
    print("t=%d  |P|=%d  A=%.6f  B=%.5f  B/A=%.3f  #g with A_g>0 = %d (of %d)"
          % (t, len(P), A, B, B / A, len(Ag), 2 * t))
    cum = 0.0
    print("   top g by contribution:      g   phi(g)   A_g       term      cum%")
    for x in terms[:10]:
        cum += x[0]
        print("      %-8d %-8d %-9.6f %-9.6f %.1f%%" % (x[1], phi(x[1]), x[2], x[0], 100 * cum / B))
    # contribution split by size of g
    for lo, hi in [(1, 10), (11, 100), (101, 1000), (1001, 10000), (10001, 10**9)]:
        s = sum(x[0] for x in terms if lo <= x[1] <= hi)
        print("      g in [%d,%s]: %.1f%% of B" % (lo, hi if hi < 10**8 else 'inf', 100 * s / B))
    print()
