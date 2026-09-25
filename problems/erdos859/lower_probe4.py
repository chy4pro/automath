# -*- coding: utf-8 -*-
"""F(n) = max sigma(m) over practical divisors m of n.  n in S_t iff F(n) >= t,
and S_t subset A_t by the reduction lemma.  One pass gives the whole density curve."""
import math

N = 2000000
sig = [0] * (N + 1)
for d in range(1, N + 1):
    for m in range(d, N + 1, d):
        sig[m] += d

# practical test via Stewart's criterion using smallest-prime-factor sieve
spf = list(range(N + 1))
for p in range(2, int(N ** 0.5) + 1):
    if spf[p] == p:
        for m in range(p * p, N + 1, p):
            if spf[m] == m:
                spf[m] = p

def practical(m):
    if m == 1: return True
    if m % 2: return False
    s = 1  # sigma of the part built so far
    x = m
    while x > 1:
        p = spf[x]; e = 0
        while x % p == 0:
            x //= p; e += 1
        if p > s + 1: return False
        s *= (p ** (e + 1) - 1) // (p - 1)
    return True

prac = bytearray(N + 1)
for m in range(1, N + 1):
    if practical(m):
        prac[m] = 1
print("practicals up to %d: %d" % (N, sum(prac)))

# F(n) = max sigma(m) over practical m | n   -- propagate from each practical m to its multiples
F = [0] * (N + 1)
for m in range(1, N + 1):
    if prac[m]:
        s = sig[m]
        for n in range(m, N + 1, m):
            if s > F[n]:
                F[n] = s
print("F computed")

import collections
Fs = sorted(F[1:], reverse=True)
print()
print("  t        dens(S_t)   1/log t    2/log^2 t   dens*log t   dens*log^2 t")
for t in [100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]:
    # dens(S_t) = fraction of n<=N with F(n) >= t
    import bisect
    cnt = bisect.bisect_left([-x for x in Fs], -t + 1)  # count of F >= t
    cnt = sum(1 for _ in ())  # placeholder
    cnt = 0
    # simple count
    cnt = sum(1 for v in Fs if v >= t)
    d = cnt / N
    L = math.log(t)
    print("  %-8d %-11.6f %-10.6f %-11.6f %-12.4f %.4f" % (t, d, 1/L, 2/L**2, d*L, d*L*L))
