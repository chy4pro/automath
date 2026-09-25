#!/usr/bin/env python3
"""
Search for the configuration (P) of ROUND1.md, which defeats the counting (pigeonhole) route:

  (P_Q)  omega(n) <= 2, n > Q^2, and for every prime p <= Q with p not dividing n,
         ceil(n/p) is prime.

For n in [lo, hi) this finds depth(n) = the largest prime Q with (P_Q) (0 if (P_2) fails),
and prints the smallest n reaching each new depth >= 13 (v2: vectorised filter for p <= 13;
the smaller depths 5, 7, 11 are reached at n = 1125, 1225, 1893, see data/p_config_partial_v1.log), with log n, Q/log n (the effective constant C
at which the counting certificate sigma(n, K=Q) fails -- see Prop. 3.3), and k3_0(n)
(smallest k >= 0 with v(n,k) >= 3, to show that level 3 is still attained).

Usage: python3 p_config_search.py --lo 1000 --hi 2000000000 --seg 10000000
"""
import argparse, math, time
import numpy as np
from sympy import isprime, factorint, primerange

def base_primes(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]

def seg_isprime(a, b, bp):
    """boolean array for primality of integers in [a, b)"""
    L = b - a
    s = np.ones(L, dtype=bool)
    for p in bp:
        p = int(p)
        if p * p >= b:
            break
        st = max(p * p, ((a + p - 1) // p) * p)
        s[st - a::p] = False
    for x in (0, 1):
        if a <= x < b:
            s[x - a] = False
    return s

def v(n, k):
    return sum(1 for p in factorint(n + k) if p > k)

def k3(n):
    """smallest k >= 0 with v(n,k) >= 3, or -1 if none (v(n,k) >= 3 needs n+k >= (k+1)(k+2)(k+3))"""
    k = 0
    while (k + 1) * (k + 2) * (k + 3) <= n + k:
        if v(n, k) >= 3:
            return k
        k += 1
    return -1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lo', type=int, default=1000)
    ap.add_argument('--hi', type=int, default=10 ** 9)
    ap.add_argument('--seg', type=int, default=10 ** 7)
    a = ap.parse_args()
    bp = base_primes(int(math.isqrt(a.hi // 2 + 2)) + 2)
    Ps = list(primerange(2, 200))
    best = 0
    t = time.time()
    for A in range(a.lo, a.hi, a.seg):
        B = min(A + a.seg, a.hi)
        n = np.arange(A, B, dtype=np.int64)
        ok = np.ones(B - A, dtype=bool)
        ndiv = np.zeros(B - A, dtype=np.int64)
        for p in (2, 3, 5, 7, 11, 13):   # vectorised filter: depth >= 13 is necessary for a new record here
            c = -(-n // p)
            lo_c, hi_c = int(c[0]), int(c[-1]) + 1
            pr = seg_isprime(lo_c, hi_c, bp)
            div = (n % p == 0)
            ndiv += div
            ok &= div | pr[c - lo_c]
        ok &= ndiv <= 2                  # omega(n) <= 2 is necessary
        for idx in np.nonzero(ok)[0]:
            m = int(n[idx])
            d = 13
            for p in Ps:
                if p <= 13:
                    continue
                if p * p >= m:
                    break
                if m % p == 0 or isprime(-(-m // p)):
                    d = p
                else:
                    break
            if d <= best:
                continue
            f = factorint(m)
            if len(f) > 2:
                continue
            best = d
            print(f'depth Q={d:3d}  n={m}  factor(n)={dict(f)}  log n={math.log(m):.3f}  '
                  f'Q/log n={d/math.log(m):.3f}  pi(Q)={len(list(primerange(2, d+1)))}  k3_0(n)={k3(m)}  '
                  f'[{time.time()-t:.0f}s]', flush=True)
        if (B // 10 ** 9) != (A // 10 ** 9):
            print(f'# progress: searched to {B} [{time.time()-t:.0f}s]', flush=True)
    print(f'# searched [{a.lo}, {a.hi}); max depth {best}; {time.time()-t:.0f}s')

if __name__ == '__main__':
    main()
