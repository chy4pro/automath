# -*- coding: utf-8 -*-
"""Empirical density of A_t = {n : t is a sum of distinct divisors of n}, small t.
Guards against misreading the object; not part of the proof."""
import math

N = 200000
divs = [[] for _ in range(N + 1)]
for d in range(1, N + 1):
    for m in range(d, N + 1, d):
        divs[m].append(d)

def in_At(n, t):
    reach = 1  # bitmask of attainable subset sums, bit s set = s attainable
    for d in divs[n]:
        if d > t:
            break
        reach |= reach << d
        reach &= (1 << (t + 1)) - 1
        if (reach >> t) & 1:
            return True
    return (reach >> t) & 1 == 1

print("N = %d" % N)
print(" t   |A_t cap [1,N]|/N   2/log t   (log t)^-d (loglog t)^(d-3/2)")
delta = 1.0 - (1.0 + math.log(math.log(2.0))) / math.log(2.0)
for t in [1, 2, 3, 4, 5, 6, 10, 12, 20, 30, 60]:
    c = sum(1 for n in range(1, N + 1) if in_At(n, t))
    L = math.log(t)
    cl = (L ** -delta) * (math.log(L) ** (delta - 1.5)) if L > 1.0 else float('nan')
    print(" %-3d  %.6f            %.4f    %s"
          % (t, c / N, 2.0 / L if L > 0 else float('inf'),
             ("%.4f" % cl) if cl == cl else "n/a"))
