# -*- coding: utf-8 -*-
"""Probe the practical-number route to a lower bound for d_t. Numerics before belief."""
import math

N = 200000
divs = [[] for _ in range(N + 1)]
for d in range(1, N + 1):
    for m in range(d, N + 1, d):
        divs[m].append(d)

def is_practical(m):
    """m practical iff every k <= sigma(m) is a sum of distinct divisors of m.
    Equivalent greedy test: sorted divisors d_1=1<...<d_k, each d_{i+1} <= 1 + sum of previous."""
    if m == 1:
        return True
    D = divs[m]
    if D[0] != 1:
        return False
    s = 0
    for d in D:
        if d > s + 1:
            return False
        s += d
    return True

def sigma(m):
    return sum(divs[m])

def in_At(n, t):
    reach = 1
    for d in divs[n]:
        if d > t:
            break
        reach |= reach << d
        reach &= (1 << (t + 1)) - 1
        if (reach >> t) & 1:
            return True
    return (reach >> t) & 1 == 1

# ---- Lemma check: m practical, m | n, sigma(m) >= t  =>  n in A_t
print("LEMMA CHECK: m practical, m|n, sigma(m)>=t  =>  n in A_t")
bad = 0; tested = 0
for t in range(1, 61):
    for m in range(1, 400):
        if not is_practical(m) or sigma(m) < t:
            continue
        for k in range(1, 12):
            n = m * k
            if n > N:
                break
            tested += 1
            if not in_At(n, t):
                bad += 1
                if bad <= 5:
                    print("   COUNTEREXAMPLE t=%d m=%d n=%d" % (t, m, n))
print("   tested %d (t,m,n) triples, counterexamples: %d" % (tested, bad))

# ---- practical number counting function vs C x / log x
print()
print("PRACTICAL NUMBER COUNT  P(x) vs C x/log x,  C = 1.33607")
C = 1.33607
pr = [m for m in range(1, N + 1) if is_practical(m)]
prset = set(pr)
for x in [1000, 5000, 20000, 50000, 100000, 200000]:
    cnt = sum(1 for m in pr if m <= x)
    pred = C * x / math.log(x)
    print("   x=%-7d P(x)=%-7d  Cx/log x=%-10.1f  ratio=%.4f" % (x, cnt, pred, cnt / pred))

# ---- |P| in (t,2t]
print()
print("|{practical m in (t,2t]}| and A = sum 1/m over it")
for t in [1000, 5000, 20000, 50000, 100000]:
    P = [m for m in pr if t < m <= 2 * t]
    A = sum(1.0 / m for m in P)
    print("   t=%-7d |P|=%-6d  A=%.6f   A*log t=%.4f" % (t, len(P), A, A * math.log(t)))
