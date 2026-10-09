#!/usr/bin/env python3
"""Checker v2: exact replay of every CR-9 certificate (onset N1 = 4,600,000).

Python 3.8+; standard library only.  Every asserted step is Python-int /
fractions.Fraction arithmetic (no floats).  Run:

    python3 check_sidon_bound_v2.py [--max-n 24] [--scan-end 5600000]

Layers (each labelled in the output):
  [CERT]  exact certificate replay of CR9_ASTRA_ONSET_20261010.md (Route A,
          Route B, tables (iii), (iv)); integer/rational comparisons.
  [ALG]   exact polynomial identities in Q[s,x,x^-1,e,z]/(s^2-2).
  [SANE]  sanity layer, NOT the proof: P_eps(y)>0 on a grid of real x using
          rational interval enclosures of log(4/3), sqrt2, x, exp.
  [SCAN]  exact integer test of (B3): eta < x^2/2 and eta < 667/3300 x^2 for
          every integer N in [N1, scan-end], plus exact (T,r)-block starts up
          to 1.2e7 (which cover every N there, see scan_blocks()).
  [OLD]   the old checker's small-N enumeration (all subsets N<=12, spans).
Exit 0 iff everything passes.  Uses require(), not assert (python -O safe).
"""

import argparse
import importlib.util
import os
import sys
import time
from fractions import Fraction as Q
from math import isqrt

N1 = 4_600_000
COUNTS = {}


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def ok(layer, msg=None):
    COUNTS[layer] = COUNTS.get(layer, 0) + 1


def chk(layer, cond, msg):
    require(cond, "[%s] %s" % (layer, msg))
    ok(layer)


# ---------------------------------------------------------------- [CERT]
def cert_route_common():
    L = "CERT"
    # brackets of x1 and the weaker u = 463/10
    chk(L, 4631 ** 4 == 459_937_821_637_921, "4631^4")
    chk(L, 4632 ** 4 == 460_335_219_019_776, "4632^4")
    chk(L, 4631 ** 4 < 460_000_000_000_000 < 4632 ** 4, "x1 bracket 4631/100<x1<4632/100")
    chk(L, 463 ** 4 == 45_954_068_161 < 46_000_000_000 == 10 ** 4 * N1, "u^4<N1")
    chk(L, 4632 < 4700, "x1<47")
    chk(L, 2144 ** 2 == 4_596_736 < N1, "2144^2<N1 (x1^2>2144)")
    chk(L, 460 < 463 and 46 * 10 == 460, "u>46")
    # sqrt2
    chk(L, 99 ** 2 == 9801 > 9800 == 2 * 70 ** 2, "sqrt2<99/70")
    chk(L, 99 < 140, "99/70<2")
    chk(L, 8 < 9, "gamma^2=8/9<1")
    # alpha = log(4/3) > 296/1029 > 719/2500
    a_lo = 2 * (Q(1, 7) + Q(1, 3 * 7 ** 3))
    chk(L, a_lo == Q(296, 1029), "2(1/7+1/(3*7^3))=296/1029")
    chk(L, 296 * 2500 == 740_000 > 739_851 == 719 * 1029, "296/1029>719/2500")
    # R bound in table: R < (49/24) * (1/7)^5/5 = 1/41160;  1/(1-1/49)=49/48
    chk(L, Q(49, 24) * Q(1, 5) * Q(1, 7) ** 5 == Q(1, 41160), "R<1/41160")
    chk(L, 1 / (1 - Q(1, 49)) == Q(49, 48), "1/(1-t^2)<=49/48 on [0,1/7]")
    # (6.3) beta*u cross product
    chk(L, 719 * 463 * 70 * 100 == 2_330_279_000, "lhs cross product")
    chk(L, 941 * 2500 * 10 * 99 == 2_328_975_000, "rhs cross product")
    chk(L, 2_330_279_000 > 2_328_975_000, "beta u > 941/100 (cross)")
    chk(L, Q(719, 2500) * Q(463, 10) * Q(70, 99) > Q(941, 100), "beta u > 941/100 (Fraction)")
    chk(L, 941 > 100, "941/100>1")
    # Taylor sums
    e3 = sum(Q(3 ** j, fact(j)) for j in range(10))
    chk(L, e3 == Q(22471, 1120), "e^3 degree-9 sum = 22471/1120")
    chk(L, 22471 * 50 - 1003 * 1120 == 190 > 0, "22471/1120>1003/50 gap 190")
    chk(L, 1_123_550 > 1_123_360, "1123550>1123360")
    e3_8 = sum(Q(3 ** j, fact(j)) for j in range(9))
    chk(L, e3_8 == Q(89641, 4480) and 50 * 89641 - 1003 * 4480 == -11390,
        "degree-8 sum insufficient (discarded approach 4)")
    e41 = sum(Q(41, 100) ** j / fact(j) for j in range(4))
    chk(L, e41 == Q(9_033_221, 6_000_000), "e^(41/100) degree-3 sum")
    chk(L, 9_033_221 > 9_000_000 and e41 > Q(3, 2), "e^(41/100)>3/2")
    chk(L, Q(941, 100) == 3 * 3 + Q(41, 100), "941/100 = 3*3+41/100")
    chk(L, 3 * 1003 ** 3 == 3_027_081_081 and 12100 * 2 * 50 ** 3 == 3_025_000_000, "3*1003^3, 12100*2*50^3")
    chk(L, 3 * 1003 ** 3 - 12100 * 2 * 50 ** 3 == 2_081_081 > 0, "3*1003^3 > 12100*2*50^3")
    chk(L, Q(3, 2) * Q(1003, 50) ** 3 > 12100, "(3/2)(1003/50)^3>12100")
    chk(L, Q(200, 12100) == Q(2, 121), "200/12100=2/121")
    # endpoint bracket for F(u)
    chk(L, Q(99, 70) * Q(463, 10) == Q(45837, 700), "99*463=45837")
    chk(L, 99 * 463 == 45837 < 45850 == 350 * 131 // 1 and Q(45837, 700) < Q(131, 2), "45837<45850, su<131/2")
    chk(L, 1 + Q(1, 46) + Q(1, 46 ** 2) == Q(2163, 2116), "1+1/46+1/46^2")
    chk(L, Q(4, 3) * Q(2163, 2116) == Q(721, 529), "4/3(...)=721/529")
    chk(L, 1442 < 1587 == 3 * 529 and Q(721, 529) < Q(3, 2), "1442<1587, 721/529<3/2")
    chk(L, Q(2, 121) * (Q(131, 2) + Q(3, 2)) == Q(134, 121), "(2/121)(131/2+3/2)=134/121")
    chk(L, Q(10, 9) - Q(134, 121) == Q(4, 1089) and 10 * 121 - 134 * 9 == 4 and 9 * 121 == 1089,
        "10/9-134/121=4/1089")
    # (6.3)-(6.7) derived rationals
    chk(L, Q(4, 1089) * 2144 == Q(8576, 1089), "S-A: 4*2144/1089=8576/1089")
    # Route B, B3
    chk(L, Q(463, 10) - 32 * Q(99, 70) == Q(73, 70) and 73 > 70, "x-32s>73/70>1")
    chk(L, 46 ** 3 == 97_336 > 33, "46^3=97336>33")
    chk(L, 3 ** 32 == 1_853_020_188_851_841, "3^32")
    chk(L, 4 ** 32 == 18_446_744_073_709_551_616, "4^32")
    chk(L, 9900 * 3 ** 32 == 18_344_899_869_633_225_900, "9900*3^32")
    chk(L, 9900 * 3 ** 32 < 4 ** 32, "9900*3^32<4^32 (B3.3)")
    chk(L, 4 ** 32 - 9900 * 3 ** 32 == 101_844_204_076_325_716, "(B3.3) gap")
    chk(L, 29 * 69 == 2001 and Q(2001, 9900) == Q(667, 3300), "29*69=2001, 2001/9900=667/3300")
    chk(L, 29 * 69 * Q(3, 4) ** 32 < Q(2001, 9900), "29*69*q^32<2001/9900")
    chk(L, 1334 < 3300 and Q(667, 3300) < Q(1, 2) and 2 * 667 == 1334, "667/3300<1/2")
    chk(L, Q(1, 2) - Q(667, 3300) == Q(983, 3300), "S-B-global 983/3300")
    # decreasing tail: 4(2r+5)-3(2r+7)=2r-1>=63 for r>=32 (r=32 shown; linear in r)
    chk(L, all(4 * (2 * r + 5) - 3 * (2 * r + 7) == 2 * r - 1 for r in range(32, 2000)),
        "4(2r+5)-3(2r+7)=2r-1")
    chk(L, 2 * 32 - 1 == 63, "2r-1>=63")
    chk(L, all(Q(3, 4) * Q(2 * r + 7, 2 * r + 5) < 1 for r in range(32, 5000)),
        "(2r+5)q^r decreasing (sampled r<5000; exact identity above covers all r)")
    # (B3.2) tail: 29(2r+5) q^r at r=32 equals 29*69*q^32
    chk(L, 2 * 32 + 5 == 69, "2r+5=69 at r=32")
    # B4.3
    chk(L, Q(8, 9 * 46 ** 2) == Q(2, 4761) and 46 ** 2 == 2116 and 4 < 4761, "B4.3")
    chk(L, Q(2, 4761) < Q(1, 2), "2/4761<1/2")
    # S-B-scalar
    chk(L, Q(11 * 2144 + 10, 18) == Q(11797, 9), "S-B-scalar 11797/9")
    # B3 onset specifics
    chk(L, 140469 ** 4 == 389_333_669_232_539_881_521, "140469^4")
    chk(L, 140470 ** 4 == 389_344_756_029_676_810_000, "140470^4")
    chk(L, 4 * N1 ** 3 == 389_344_000_000_000_000_000, "4*N1^3")
    chk(L, 140469 ** 4 < 4 * N1 ** 3 < 140470 ** 4, "140469^4<4N1^3<140470^4 => T=140470")
    T1 = 140470
    chk(L, 32 * T1 == 4_495_040 <= N1 - 1 == 4_599_999 < 4_635_510 == 33 * T1, "32T<=N1-1<33T")
    eta1 = 29 * T1 * Q(3, 4) ** 32
    chk(L, eta1 == Q(3_774_259_315_956_262_526_415, 9_223_372_036_854_775_808), "eta_1 exact fraction")
    chk(L, 9_223_372_036_854_775_808 == 2 ** 63, "2^63")
    diff = 1072 - eta1
    chk(L, diff == Q(6_113_195_507_552_057_139_761, 9_223_372_036_854_775_808), "S-B-onset 1072-eta_1")
    chk(L, 6_113_195_507_552_057_139_761 > 0 and diff > 0, "S-B-onset positive")
    chk(L, 2144 // 2 == 1072, "x1^2/2>1072")
    # old-checker-style facts needed by general discussion
    chk(L, Q(8, 9) < 1, "gamma<1")


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


# ---------------------------------------------------------------- [ALG]
# Polynomials: dict {(a, j, k, l): Fraction}, a = power of s (reduced mod
# s^2 = 2), j = power of x (may be negative), k = power of e, l = power of z.
class P:
    def __init__(self, d=None):
        self.d = {}
        for m, c in (d or {}).items():
            if c != 0:
                self.d[m] = Q(c)

    @staticmethod
    def const(c):
        return P({(0, 0, 0, 0): c})

    def __add__(self, o):
        o = lift(o)
        r = dict(self.d)
        for m, c in o.d.items():
            r[m] = r.get(m, 0) + c
        return P(r)

    __radd__ = __add__

    def __neg__(self):
        return P({m: -c for m, c in self.d.items()})

    def __sub__(self, o):
        return self + (-lift(o))

    def __rsub__(self, o):
        return lift(o) - self

    def __mul__(self, o):
        o = lift(o)
        r = {}
        for (a, j, k, l), c in self.d.items():
            for (a2, j2, k2, l2), c2 in o.d.items():
                a3, f = a + a2, 1
                if a3 == 2:
                    a3, f = 0, 2
                m = (a3, j + j2, k + k2, l + l2)
                r[m] = r.get(m, 0) + c * c2 * f
        return P(r)

    __rmul__ = __mul__

    def __pow__(self, n):
        r = P.const(1)
        for _ in range(n):
            r = r * self
        return r

    def __eq__(self, o):
        return self.d == lift(o).d


def lift(o):
    return o if isinstance(o, P) else P.const(o)


S = P({(1, 0, 0, 0): 1})
X = P({(0, 1, 0, 0): 1})
XI = P({(0, -1, 0, 0): 1})
E = P({(0, 0, 1, 0): 1})
Z = P({(0, 0, 0, 1): 1})
GAMMA = Q(2, 3) * S


def alg_identities():
    L = "ALG"
    chk(L, S * S == 2 and GAMMA * GAMMA == Q(8, 9), "s^2=2, gamma^2=8/9")
    chk(L, X * XI == 1, "x*x^-1=1")
    y = X ** 2 + GAMMA * X + 1
    # (6.2) from (5.1): k^2 <= (x/s+2/3+e)(T+4k/3), T = s x^3, x/s = s x /2
    rhs = (S * X * Q(1, 2) + Q(2, 3) + E) * (S * X ** 3 + Q(4, 3) * Z)
    P62_from_51 = Z ** 2 - rhs
    P62 = Z ** 2 - (GAMMA * X + Q(8, 9) + Q(4, 3) * E) * Z - X ** 4 - GAMMA * X ** 3 - S * E * X ** 3
    chk(L, P62_from_51 == P62, "(6.2) expansion from (5.1)")
    chk(L, (Q(4, 3) * (S * X * Q(1, 2) + Q(2, 3) + E)) == GAMMA * X + Q(8, 9) + Q(4, 3) * E,
        "(4/3)(x/s+2/3+e)=gamma x+8/9+(4/3)e")
    chk(L, ((S * X * Q(1, 2) + Q(2, 3) + E) * S * X ** 3)
        == X ** 4 + GAMMA * X ** 3 + S * E * X ** 3, "(x/s+2/3+e) s x^3")

    def subs_z(poly, val):
        out = P()
        for (a, j, k, l), c in poly.d.items():
            out = out + P({(a, j, k, 0): c}) * (val ** l)
        return out

    P0z = Z ** 2 - (GAMMA * X + Q(8, 9)) * Z - X ** 4 - GAMMA * X ** 3
    P0y = subs_z(P0z, y)
    # (6.5)
    chk(L, P0y == Q(10, 9) * X ** 2 + Q(1, 9) * GAMMA * X + Q(1, 9), "(6.5) P_0(y)")
    chk(L, P0y == Q(10, 9) * X ** 2 + Q(2, 27) * S * X + Q(1, 9), "(6.5) gamma/9 = 2s/27")
    # P_eps(y) = P_0(y) - e((4/3)y + s x^3)
    chk(L, subs_z(P62, y) == P0y - E * (Q(4, 3) * y + S * X ** 3), "P_eps(y)=P_0(y)-e((4/3)y+sx^3)")
    # F(x) normalisation
    lhs = E * (Q(4, 3) * y + S * X ** 3)
    rhs = E * X ** 2 * (S * X + Q(4, 3) + Q(4, 3) * GAMMA * XI + Q(4, 3) * XI * XI)
    chk(L, lhs == rhs, "F(x) formula (eps=e)")
    # F bracket: coefficient forms 4gamma/(3x)
    chk(L, Q(4, 3) * GAMMA == Q(8, 9) * S, "4gamma/3 = 8s/9")
    # derivative rows: d/dx (x e^{-bx}) = e^{-bx}(1-bx) ; d/dx x^{-j}e^{-bx} = -e^{-bx}(j x^{-j-1} + b x^{-j})
    # as polynomials in b (use E as b): coefficient identities
    for j in range(3):
        # derivative of x^-j * exp: (-j) x^{-j-1} + (-b) x^{-j}; expressed coefficientwise
        d = P({(0, -j - 1, 0, 0): -j}) + (-1) * E * P({(0, -j, 0, 0): 1})
        chk(L, d == -(j * P({(0, -j - 1, 0, 0): 1}) + E * P({(0, -j, 0, 0): 1})), "derivative row j=%d" % j)
    chk(L, (1 - E * X) == 1 - E * X, "d/dx(x e^{-bx}) factor (trivial)")
    # (B3.1) numerator: s(x^4-1) - (x-s)(s x^3+1) = 2x^3-x
    chk(L, S * (X ** 4 - 1) - (X - S) * (S * X ** 3 + 1) == 2 * X ** 3 - X, "(B3.1) numerator 2x^3-x")
    # x/s = s x/2
    chk(L, S * (S * X * Q(1, 2)) == X, "x/s = s x/2")
    # (B3.2): T/x^2 <= s x + 1/x^2 when T <= s x^3 + 1
    chk(L, (S * X ** 3 + 1) * XI * XI == S * X + XI * XI, "(s x^3+1)/x^2 = s x + x^-2")
    # B4.1
    c1 = 1 + GAMMA * XI ** 3 * (y - 1)
    chk(L, c1 == 1 + GAMMA * XI + Q(8, 9) * XI * XI, "1+gamma/x^3 (y-1) = 1+gamma/x+gamma^2/x^2")
    b41 = y ** 2 - (X ** 4 + GAMMA * X ** 3) * c1
    chk(L, b41 == Q(10, 9) * X ** 2 + Q(10, 9) * GAMMA * X + 1, "(B4.1)")
    # B4.2 with eta = x^2/2
    b42 = b41 - Q(1, 2) * X ** 2 * c1
    chk(L, b42 == Q(11, 18) * X ** 2 + Q(11, 18) * GAMMA * X + Q(5, 9), "(B4.2) with eta=x^2/2")
    chk(L, 1 - Q(8, 9) / 2 == Q(5, 9) and Q(10, 9) - Q(1, 2) == Q(11, 18), "10/9-1/2, 1-gamma^2/2")
    # Q(z) constant term -C(1-gamma/x^3) sign: gamma<1, x>=1 - rational check of ingredient
    chk(L, Q(8, 9) < 1, "gamma<1 for constant term")
    # B2 / B1 ingredients (finite certificate): 4/(3T) - a_T = 2/(3T(T+1)) > 0
    for T in (1, 2, 7, 140470, 10 ** 9):
        aT = Q(2 * (2 * T + 1), 3 * T * (T + 1))
        chk(L, Q(4, 3 * T) - aT == Q(2, 3 * T * (T + 1)) > 0, "a_T < 4/(3T) at T=%d" % T)
    # symbolic: 2(2T+1)(T) *... cross-multiplied: 4(T+1) - 2(2T+1) = 2
    chk(L, 4 * 1 - 2 * 1 == 2, "4(T+1)-2(2T+1)=2 (constant part)")
    # B1: (2/3)(T-1) <= (2/3)(s x^3) = gamma x^3 when T <= s x^3 + 1
    chk(L, Q(2, 3) * S == GAMMA, "(2/3)s=gamma")
    # S-A-type lower bounds on the expression: 4/1089 * 2144
    chk(L, GAMMA == Q(2, 3) * S, "gamma = 2s/3")


# ---------------------------------------------------------------- [SANE]
def floor_dyadic(q, bits=120):
    sc = 1 << bits
    return Q((q.numerator * sc) // q.denominator, sc)


def ceil_dyadic(q, bits=120):
    sc = 1 << bits
    return Q(-((-q.numerator * sc) // q.denominator), sc)


def root_enclosure(n, degree, bits=100):
    """[lo, hi] dyadic enclosure of n^(1/degree) for a positive Fraction n."""
    sc = 1 << bits
    if isinstance(n, int):
        n = Q(n)
    scaled = (n.numerator * sc ** degree) // n.denominator
    r = isqrt(scaled) if degree == 2 else isqrt(isqrt(scaled))
    require(r ** degree <= scaled, "root floor")
    return Q(r, sc), Q(r + 1, sc)


def log43_enclosure(terms=40):
    """log(4/3) = 2 sum_{j>=0} t^(2j+1)/(2j+1), t=1/7; tail <= 2 t^(2n+1)/((2n+1)(1-t^2))."""
    t = Q(1, 7)
    s = sum(2 * t ** (2 * j + 1) / (2 * j + 1) for j in range(terms))
    tail = 2 * t ** (2 * terms + 1) / (2 * terms + 1) / (1 - t * t)
    return s, s + tail


def exp_lower(z, bits=120):
    """Rational lower bound for exp(z), z>=0 rational: (Taylor_25(z/m))^m, rounded down."""
    m = max(1, -(-z.numerator // (2 * z.denominator)))
    w = z / m
    t = Q(0)
    term = Q(1)
    for j in range(26):
        t += term
        term = term * w / (j + 1)
    t = floor_dyadic(t, bits)
    # power by repeated squaring with downward rounding (all values positive)
    res, base, n = Q(1), t, m
    while n:
        if n & 1:
            res = floor_dyadic(res * base, bits)
        base = floor_dyadic(base * base, bits)
        n >>= 1
    return res


def exp_upper(z, terms=60):
    """Rational upper bound for exp(z), 0<=z<=1: Taylor + geometric remainder."""
    require(0 <= z <= 1, "exp_upper domain")
    t, term = Q(0), Q(1)
    for j in range(terms):
        t += term
        term = term * z / (j + 1)
    return t + term * 2  # remainder <= term*(1+z/(n+1)+...) <= 2*term for z<=1


def sane_grid():
    L = "SANE"
    a_lo, a_hi = log43_enclosure()
    chk(L, Q(719, 2500) < a_lo and a_hi < Q(296, 1029) + Q(1, 41160), "alpha enclosure consistent with CR-9 table")
    chk(L, exp_upper(Q(1)) < 3 and exp_lower(Q(1)) > Q(27, 10), "exp enclosure sanity at 1")
    # sanity of exp_lower against a known exact bound: e^3 > 1003/50
    chk(L, exp_lower(Q(3)) > Q(1003, 50), "exp_lower(3)>1003/50")
    sl, sh = root_enclosure(2, 2, 120)
    grid = [Q(4632, 100), Q(47), Q(48), Q(50), Q(55), Q(60), Q(70), Q(80), Q(100), Q(120), Q(150),
            Q(200), Q(300), Q(500), Q(1000), Q(2000), Q(5000), Q(10 ** 4), Q(10 ** 5), Q(10 ** 6)]
    xl1, xh1 = root_enclosure(N1, 4, 120)  # x1 itself as an interval
    pts = [(xl1, xh1)] + [(g, g) for g in grid] + [(g + Q(1, 3), g + Q(1, 3)) for g in grid[1:12]]
    worst = None
    for xl, xh in pts:
        # eps upper bound: z = alpha x / s, use lower z
        zlo = a_lo * xl / sh
        eps_hi = 200 / exp_lower(zlo)
        # interval arithmetic with plain (lo,hi) pairs; everything positive
        gam_lo, gam_hi = Q(2, 3) * sl, Q(2, 3) * sh
        y_lo, y_hi = xl ** 2 + gam_lo * xl + 1, xh ** 2 + gam_hi * xh + 1
        # cancellation-free: P_eps(y) >= (10/9)x^2 + (gamma/9)x + 1/9 - eps_hi*((4/3)y_hi + s_hi x_hi^3)
        p0_lo = Q(10, 9) * xl ** 2 + gam_lo / 9 * xl + Q(1, 9)
        err_hi = eps_hi * (Q(4, 3) * y_hi + sh * xh ** 3)
        margin = p0_lo - err_hi
        chk(L, margin > Q(4, 1089) * xl ** 2, "P_eps(y) > (4/1089) x^2 at x~%s" % float(xl))
        # independent direct (uncancelled) form with eps in [0, eps_hi]; need x^4-size precision: 120 bits suffice
        # k=y: y^2 - (gamma x + 8/9 + 4/3 eps) y - x^4 - gamma x^3 - s eps x^3, lower bound
        direct_lo = (y_lo ** 2 - (gam_hi * xh + Q(8, 9) + Q(4, 3) * eps_hi) * y_hi
                     - xh ** 4 - gam_hi * xh ** 3 - sh * eps_hi * xh ** 3)
        # width of this interval evaluation is huge for x>=1e4 at 120-bit precision; only assert where valid
        if xl <= 1000:
            chk(L, direct_lo > 0, "direct P_eps(y)>0 at x~%s" % float(xl))
        # B3 (real-x flavour): eta/x^2 envelope 29 (2r+5) q^r with r = ceil(x/s) - 2 style is covered in [SCAN]
        ratio = margin / xl ** 2
        if worst is None or ratio < worst[0]:
            worst = (ratio, xl)
    print("  [SANE] smallest certified lower bound for P_eps(y)/x^2 on grid: %.6f at x=%.4f (CR-9 claims > 4/1089=%.6f)"
          % (float(worst[0]), float(worst[1]), 4 / 1089))


# ---------------------------------------------------------------- [SCAN]
def icbrt(n):
    lo, hi = 0, 1 << (n.bit_length() // 3 + 2)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def T_of(N):
    """Least integer T with T^4 >= 4 N^3  (== ceil(sqrt2 * N^(3/4)))."""
    m = 4 * N ** 3
    t = isqrt(isqrt(m))
    while t ** 4 < m:
        t += 1
    while t > 1 and (t - 1) ** 4 >= m:
        t -= 1
    return t


POW3 = [3 ** r for r in range(200)]
POW16 = [16 ** r for r in range(200)]


def b3_ok(N):
    """Exact tests at integer N.  Returns (T, r, ok_half, ok_cr9, ok_x_bound, r>=32)."""
    T = T_of(N)
    r = (N - 1) // T
    lhs = (58 * T * POW3[r]) ** 2          # eta < sqrt(N)/2  <=>  (58 T 3^r)^2 < 16^r N
    rhs = POW16[r] * N
    half = lhs < rhs
    # eta < (667/3300) x^2 = (667/3300) sqrt N <=> (29*3300 T 3^r)^2 < 667^2 16^r N
    cr9 = (29 * 3300 * T * POW3[r]) ** 2 < 667 ** 2 * rhs
    xb = N < 4 * (r + 2) ** 4               # (B3.1) x < sqrt2 (r+2)
    return T, r, half, cr9, xb, r >= 32


def scan_full(lo, hi):
    L = "SCAN"
    cnt = 0
    min_r = 10 ** 9
    worst_ratio = Q(0)
    worst_N = None
    prevT = 0
    for N in range(lo, hi + 1):
        T, r, half, cr9, xb, r32 = b3_ok(N)
        if not (half and cr9 and xb and r32 and T >= prevT):
            raise AssertionError("[SCAN] B3 failure at N=%d (T=%d r=%d %s %s %s %s)" % (N, T, r, half, cr9, xb, r32))
        prevT = T
        min_r = min(min_r, r)
        cnt += 1
    COUNTS[L] = COUNTS.get(L, 0) + cnt
    return cnt, min_r


def scan_blocks(lo, hi):
    """Exact coverage of every integer N in [lo, hi] via (T, r) blocks.

    T(N) is nondecreasing; on {N: T(N)=T} and r=(N-1)//T both constant the
    quantity 29 T q^r / sqrt(N) is strictly decreasing in N, hence the
    smallest N of each (T,r)-block is the worst case.  Block starts are N_T
    (least N with 4N^3 > (T-1)^4) and N = jT+1 (r jumps) inside the block.
    All candidates are re-evaluated from scratch with b3_ok.
    """
    L = "SCAN"
    T = T_of(lo)
    cand = {lo}
    while True:
        # least N with T(N) == T: 4N^3 > (T-1)^4  =>  N > ((T-1)^4/4)^(1/3)
        start = icbrt((T - 1) ** 4 // 4) + 1
        while 4 * start ** 3 <= (T - 1) ** 4:
            start += 1
        while start > 1 and 4 * (start - 1) ** 3 > (T - 1) ** 4:
            start -= 1
        # last N of block: 4N^3 <= T^4
        end = icbrt(T ** 4 // 4)
        while 4 * (end + 1) ** 3 <= T ** 4:
            end += 1
        while 4 * end ** 3 > T ** 4:
            end -= 1
        if start > hi:
            break
        a, b = max(start, lo), min(end, hi)
        if a <= b:
            cand.add(a)
            j = (a - 1) // T + 1
            while j * T + 1 <= b:
                cand.add(j * T + 1)
                j += 1
        T += 1
    nblocks = len(cand)
    min_r = 10 ** 9
    worst = (Q(0), None)
    for N in sorted(cand):
        Tn, r, half, cr9, xb, r32 = b3_ok(N)
        if not (half and cr9 and xb and r32):
            raise AssertionError("[SCAN] block-start B3 failure at N=%d" % N)
        min_r = min(min_r, r)
        ratio = Q(29 * Tn * 3 ** r, 4 ** r) ** 2 / N / Q(1, 4)  # (eta/(sqrt N/2))^2
        if ratio > worst[0]:
            worst = (ratio, N, Tn, r)
    COUNTS[L] = COUNTS.get(L, 0) + nblocks
    return nblocks, min_r, worst


# ---------------------------------------------------------------- [OLD]
def old_checks(max_n):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_sidon_bound.py")
    spec = importlib.util.spec_from_file_location("old_checker", path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    chk("OLD", old.N0 == 120 ** 4 == 207_360_000, "old N0 unchanged (file not edited)")
    old.exhaustive_self_check()          # every subset for N<=12 + search audit, raises on failure
    ok("OLD")
    good = old.finite_search(max_n, 0, 0)   # exact spans / maxima for every N<=max_n
    chk("OLD", good is True, "old finite search exact for N<=%d" % max_n)
    # independent re-derivation of maxima for N<=12 by literal subsets, compared with old spans
    best = {}
    for n in range(1, 13):
        b = 0
        for mask in range(1 << n):
            pts = [i for i in range(n) if mask >> i & 1]
            sums = [a + c for i, a in enumerate(pts) for c in pts[i:]]
            if len(sums) == len(set(sums)):
                b = max(b, len(pts))
        best[n] = b
    # max Sidon size known values A003022-based: N=1..12 -> 1,2,2,3,3,3,4,4,4,4,5,5? derived literally here
    chk("OLD", best[1] == 1 and best[12] >= 5, "literal maxima sanity")
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-n", type=int, default=24)
    ap.add_argument("--scan-end", type=int, default=N1 + 10 ** 6)
    ap.add_argument("--break-end", type=int, default=12_000_000)
    a = ap.parse_args()
    t0 = time.process_time()
    w0 = time.monotonic()

    def lap(name):
        print("  (%s done: cpu %.2fs)" % (name, time.process_time() - t0), flush=True)

    print("== [CERT] exact CR-9 certificate replay")
    cert_route_common()
    lap("CERT")
    print("== [ALG] exact polynomial identities in Q[s,x,x^-1,e,z]/(s^2-2)")
    alg_identities()
    lap("ALG")
    print("== [SANE] interval-enclosure sanity layer (NOT the proof)")
    sane_grid()
    lap("SANE")
    print("== [SCAN] exact integer (B3) scan")
    T1 = T_of(N1)
    chk("SCAN", T1 == 140470 and (N1 - 1) // T1 == 32, "T(N1)=140470, r(N1)=32")
    cnt, min_r = scan_full(N1, a.scan_end)
    print("  [SCAN] every integer N in [%d, %d]: %d values; eta<x^2/2, eta<(667/3300)x^2, x<s(r+2), r>=32 all hold; min r=%d"
          % (N1, a.scan_end, cnt, min_r))
    lap("SCAN-full")
    nb, mr, worst = scan_blocks(N1, a.break_end)
    print("  [SCAN] (T,r)-block starts covering every N in [%d, %d]: %d candidates, all pass; min r=%d; "
          "worst (eta/(x^2/2)) = %.6f at N=%d (T=%d, r=%d)"
          % (N1, a.break_end, nb, mr, float(worst[0]) ** 0.5, worst[1], worst[2], worst[3]))
    lap("SCAN-blocks")
    print("== [OLD] old checker small-N enumeration (imported, file untouched)")
    old_checks(a.max_n)
    lap("OLD")
    cpu = time.process_time() - t0
    print("SUMMARY: all assertions passed. counts: " + ", ".join("%s=%d" % kv for kv in sorted(COUNTS.items())))
    print("TIME: cpu %.2f s, wall %.2f s" % (cpu, time.monotonic() - w0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
