#!/usr/bin/env python3
"""Correctness cross-check for agrawal_A1_probe.py (V7: settle by execution, not by reading)."""
import sys, math
import numpy as np
sys.path.insert(0, "$HOME/workspace/claudecode/automath/tools")
from agrawal_A1_probe import primes_upto, attribute_pass, best_odd_k, log_binom


def naive_factor(m):
    f = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def main():
    # 1. sieve check
    P = primes_upto(200)
    assert list(P[:10]) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], list(P[:10])
    assert len(primes_upto(10 ** 6)) == 78498, len(primes_upto(10 ** 6))
    assert len(primes_upto(10 ** 7)) == 664579
    print("sieve OK: pi(1e6)=78498, pi(1e7)=664579")

    # 2. attribute pass vs naive factorisation
    X = 200000
    pr = primes_upto(X)
    m4 = (pr % 4) == 3
    r5 = pr % 5
    baseP = pr[m4 & ((r5 == 2) | (r5 == 3))]
    A = (baseP - 1) // 2
    Bv = (baseP + 1) // 4
    small = primes_upto(100000)
    maxfA, sqfA, clsA = attribute_pass(A, small, 3, "A")
    maxfB, sqfB, clsB = attribute_pass(Bv, small, 1, "B")
    bad = 0
    for i in range(len(baseP)):
        for val, mf, sq, cl, want in ((int(A[i]), maxfA[i], sqfA[i], clsA[i], 3),
                                      (int(Bv[i]), maxfB[i], sqfB[i], clsB[i], 1)):
            f = naive_factor(val) if val > 1 else {}
            e_mf = max(f) if f else 0
            e_sq = all(e == 1 for e in f.values())
            e_cl = all(q % 4 == want for q in f)
            if (int(mf), bool(sq), bool(cl)) != (e_mf, e_sq, e_cl):
                bad += 1
                if bad < 6:
                    print("MISMATCH p=%d val=%d got=(%d,%s,%s) want=(%d,%s,%s) f=%s"
                          % (baseP[i], val, mf, sq, cl, e_mf, e_sq, e_cl, f))
    print("attribute cross-check on %d primes (2 sides): %d mismatches" % (len(baseP), bad))
    assert bad == 0

    # 3. Lenstra kernel spot-check: the known A329223 candidate
    n = 330468624532072027
    ps = [2003, 574003, 287432003]
    assert n == ps[0] * ps[1] * ps[2]
    car = all((n - 1) % (p - 1) == 0 for p in ps)
    lc = all((n + 1) % (p + 1) == 0 for p in ps)
    print("A329223 candidate: Carmichael=%s  Lucas-Carmichael=%s  (expect True/False)" % (car, lc))
    assert car and not lc
    # and check its p_i land in the pool shape Lenstra needs
    print("  p_i mod 80 =", [p % 80 for p in ps])
    for p in ps:
        fa = naive_factor((p - 1) // 2)
        fb = naive_factor((p + 1) // 4)
        print("  p=%d  (p-1)/2=%s  cls3=%s sqf=%s maxf=%d | (p+1)/4=%s cls1=%s sqf=%s maxf=%d"
              % (p, fa, all(q % 4 == 3 for q in fa), all(e == 1 for e in fa.values()), max(fa),
                 fb, all(q % 4 == 1 for q in fb), all(e == 1 for e in fb.values()), max(fb)))

    # 4. inequality helper check
    assert abs(log_binom(10, 5) - math.log(252)) < 1e-9
    k, v = best_odd_k(25)
    print("best_odd_k(25) =", k, v, "-> C(25,%d)=%.3e" % (k, math.exp(v)))
    print("ALL VALIDATION OK")


if __name__ == "__main__":
    main()
