#!/usr/bin/env python3
"""Densities for the coarse model of Erdős #1212.
Coarse grid Z^2, phi(i,j) = (2i+1, 2j+1). Under a uniformly random translation t, the coarse point v is
p-closed iff v + t == ((p-1)/2, (p-1)/2) mod p (i.e. p divides both odd coordinates); closed iff p-closed
for some odd prime p; open otherwise.  For a finite set S:
  all_open_density(S)  = prod_{p>=3} (1 - |S mod p| / p^2)                  (exact; G1/G9)
  closed_upper_bound(S, B) = rigorous upper bound on the density that EVERY point of S is closed:
      exact distribution of the set of points closed by primes <= B (DP over the CRT classes), times
      tau_B^{#points not closed by small primes}, tau_B = sum_{p>B} p^-2 <= 1/(2B) (valid when B > diam(S)).
Usage: python3 density.py            (self-tests)
       python3 density.py "0,0 1,0"  (points; prints both quantities)"""
import sys
from fractions import Fraction
from math import pi

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(3, n + 1) if s[i]]

def all_open_density(S, P=200000):
    d = 1.0
    for p in primes_upto(P):
        k = len({(x % p, y % p) for x, y in S})
        d *= 1 - k / (p * p)
    return d

def closed_upper_bound(S, B=101):
    S = list(S); n = len(S)
    diam = max(max(abs(u[0] - v[0]), abs(u[1] - v[1])) for u in S for v in S) if n > 1 else 0
    assert B > diam, "need B > diam(S) so that primes > B close at most one point"
    tau = Fraction(1, 2 * B)  # sum_{p>B} p^-2 <= sum_{m>B, m odd} m^-2 <= 1/(2B)
    dist = {0: Fraction(1)}
    for p in primes_upto(B):
        a = (p - 1) // 2
        classes = {}
        for i, (x, y) in enumerate(S):
            c = ((a - x) % p, (a - y) % p)
            classes[c] = classes.get(c, 0) | (1 << i)
        occ = len(classes)
        new = {}
        for m, w in dist.items():
            new[m] = new.get(m, 0) + w * Fraction(p * p - occ, p * p)
            for cm in classes.values():
                new[m | cm] = new.get(m | cm, 0) + w * Fraction(1, p * p)
        dist = new
    total = Fraction(0)
    for m, w in dist.items():
        total += w * tau ** (n - bin(m).count("1"))
    return total

if __name__ == "__main__":
    if len(sys.argv) > 1:
        S = [tuple(map(int, t.split(","))) for t in sys.argv[1].split()]
        print("all-open density:", all_open_density(S))
        ub = closed_upper_bound(S); print("all-closed density <=", float(ub))
        sys.exit()
    q = 1 - 8 / pi ** 2
    print("single point: all-open =", round(all_open_density([(0, 0)]), 6), " 8/pi^2 =", round(8 / pi ** 2, 6))
    ub1 = float(closed_upper_bound([(0, 0)]))
    print("single point: all-closed <=", round(ub1, 6), " (true value 1-8/pi^2 =", round(q, 6), ") ok:", ub1 >= q)
    # two adjacent coarse points: exact all-closed density 1 - 2*8/pi^2 + prod(1-2/p^2) = 0.024129
    prod2 = 1.0
    for p in primes_upto(200000): prod2 *= 1 - 2 / (p * p)
    exact2 = 1 - 2 * 8 / pi ** 2 + prod2
    ub2 = float(closed_upper_bound([(0, 0), (1, 0)]))
    print("two adjacent: exact =", round(exact2, 6), " upper bound =", round(ub2, 6), " ok:", ub2 >= exact2)
    for r in (3, 4):
        S = [(i, 0) for i in range(r)]
        print(f"straight block of {r}: all-closed <=", round(float(closed_upper_bound(S)), 6))
