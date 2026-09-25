#!/usr/bin/env python3
"""Numeric sanity checks for batch-1 targets A108211 and A114362-c2.

A108211: certified check of floor(1/D(n)) == 16n^2+1 using exact rational
bounds on log 2 (via 2*atanh(1/3) series with tail bound).
A114362: even n exact via Bernoulli-free known zeta ratios; odd n via
high-precision partial sums with tail bounds (Decimal).
"""
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 50


def log2_bounds(terms=40):
    """log 2 = 2*atanh(1/3) = 2*sum_{k>=0} 1/((2k+1)*3^(2k+1)).
    Partial sum S_T is a lower bound; tail < (2/ (2T+1)) * 3^-(2T+1) * 9/8."""
    s = Fraction(0)
    for k in range(terms):
        s += Fraction(2, (2 * k + 1) * 3 ** (2 * k + 1))
    tail_hi = Fraction(2, (2 * terms + 1) * 3 ** (2 * terms + 1)) * Fraction(9, 8)
    return s, s + tail_hi  # lo < log2 < hi


def check_a108211(nmax):
    lo, hi = log2_bounds()
    bad = []
    for n in range(1, nmax + 1):
        h = sum(Fraction(1, k) for k in range(n + 1, 2 * n + 1))
        base = Fraction(1, 4 * n) + h
        d_lo, d_hi = base - hi, base - lo  # D in (d_lo, d_hi)
        target = 16 * n * n + 1
        # need target <= 1/D < target+1 certified: 1/d_hi <= 1/D <= 1/d_lo
        ok = (Fraction(1, 1) / d_hi >= target) and (Fraction(1, 1) / d_lo < target + 1)
        if not ok:
            bad.append(n)
    print(f"A108211: n=1..{nmax} certified floor==16n^2+1 except {bad if bad else 'NONE'}")


def zeta_dec(n, terms=200000):
    """Decimal partial sum + integral tail bounds (lo, hi)."""
    s = Decimal(0)
    for k in range(1, terms + 1):
        s += Decimal(1) / Decimal(k) ** n
    # tail: int_{terms}^inf u^-n du = terms^(1-n)/(n-1); lower 0 < tail
    tail = Decimal(terms) ** (1 - n) / (n - 1)
    return s, s + tail


def check_a114362(nlist):
    print("A114362-c2: y - sum(p^-n) vs 11^-n (ratio should be ~1, bounded):")
    exact = {2: Fraction(2, 5), 4: Fraction(6, 7),
             6: Fraction(3617, 3927) if False else None}
    for n in nlist:
        if n == 2:
            t = Fraction(2, 5)
        elif n == 4:
            t = Fraction(6, 7)
        else:
            zlo, zhi = zeta_dec(n, terms=3000 if n >= 5 else 200000)
            z2lo, z2hi = zeta_dec(2 * n, terms=2000)
            t = None
            t_lo = z2lo / (zhi * zhi)
            t_hi = z2hi / (zlo * zlo)
        if t is not None:
            y = Decimal(t.numerator) / Decimal(t.denominator)
            y = (1 - y) / (1 + y)
        else:
            y_lo = (1 - t_hi) / (1 + t_hi)
            y_hi = (1 - t_lo) / (1 + t_lo)
            y = (y_lo + y_hi) / 2
        s = sum(Decimal(p) ** (-n) for p in (2, 3, 5, 7))
        diff = y - s
        ratio = diff / (Decimal(11) ** (-n))
        print(f"  n={n}: diff={diff:.3E} ratio_to_11^-n={ratio:.6f}")


if __name__ == "__main__":
    check_a108211(300)
    check_a114362([2, 3, 4, 5, 6, 8, 10, 14, 20, 30])
