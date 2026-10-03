# U(A) = sum(1 - a_i/a_n). Check (i) a_n >= (beta(n)-1)/U and (ii) Lemma F with exponent n-U, on explicit DSS sets.
import random
import mpmath as mp
from math import comb
from windows import conway_guy_set, is_dss, beta
from exhaust import enum
mp.mp.dps = 30
def lemF(n, e):
    f = lambda s: (1 - s) * mp.cos(mp.pi * s / 2) ** e
    return mp.mpf(2) ** (n - 1) * 2 * mp.quad(f, [0, 1 / mp.sqrt(max(e, 1)), 1])
def chk(a, name=None):
    a = sorted(a); n = len(a); an = a[-1]
    U = sum(1 - x / an for x in a)
    rhoN = sum(x * x for x in a) / an ** 2
    b1 = (beta(n) - 1) / U
    b2 = lemF(n, rhoN)
    assert an >= b1 - 1e-9 and an >= b2 * (1 - 1e-12), (a, b1, b2)
    if name:
        print(f"{name:>10} n={n:2d} U={U:7.3f} rho*n={rhoN:7.3f} a_n={an}  (beta-1)/U={b1:12.1f}  LemmaF(rho)={mp.nstr(b2,8):>12}  fold={2*beta(n-1)}")
for n in [4, 6, 8, 10, 14, 18, 22, 30, 40]:
    chk(conway_guy_set(n), "CG")
chk(sorted(2**12 - 2**i for i in range(12)), "2^n-2^i")
cnt = 0
for n, M in [(4, 12), (5, 20), (6, 30), (7, 48)]:
    for a in enum(n, M):
        chk(list(a)); cnt += 1
rng = random.Random(3)
for t in range(800):
    n = rng.randint(5, 13)
    a = sorted({max(1, int(2**i * rng.uniform(0.55, 1.0))) for i in range(n)})
    if len(a) == n and is_dss(a):
        chk(a); cnt += 1
print("additional sets checked:", cnt)
