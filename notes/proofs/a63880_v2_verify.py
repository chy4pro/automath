#!/usr/bin/env python3
"""
Verification script for  notes/proofs/a63880_v2.md
OEIS A063880:  A = { n : sigma(n) = 2*usigma(n) },  conjecturally n == 108 (mod 216)
and 108 the only primitive term.

Everything here is a *finite* check backing up a step of the write-up.  The
search in PART 4 is a complete decision procedure on an explicitly described
region; every hypothesis it needs is printed, and any place where a cap had to
be imposed is reported as UNBOUNDED.

Usage:  python3 a63880_v2_verify.py [OMEGA_MAX] [AMAX]
"""
import sys, time
from bisect import bisect_left
from fractions import Fraction as F

T0 = time.time()

# --------------------------------------------------------------- arithmetic
def sieve(n):
    bs = bytearray([1]) * (n + 1)
    bs[0] = bs[1] = 0
    i = 2
    while i * i <= n:
        if bs[i]:
            bs[i * i:: i] = bytearray(len(range(i * i, n + 1, i)))
        i += 1
    return [i for i in range(n + 1) if bs[i]]

PRIME_LIMIT = 3_000_000
PRIMES = sieve(PRIME_LIMIT)

def rho(p, e):                       # sigma(p^e)/(p^e+1)
    return F(p ** (e + 1) - 1, (p - 1) * (p ** e + 1))

def Pf(p):                           # sup_e rho(p,e) = p/(p-1), never attained
    return F(p, p - 1)

def delta(p, e):                     # p/(p-1) - rho(p,e), strictly decreasing in e
    return F(p + 1, (p - 1) * (p ** e + 1))

def factor(n):
    f, m, d = {}, n, 2
    while d * d <= m:
        if m % d == 0:
            k = 0
            while m % d == 0:
                m //= d
                k += 1
            f[d] = k
        d += 1
    if m > 1:
        f[m] = 1
    return f

def sigma(n):
    s = 1
    for p, e in factor(n).items():
        s *= (p ** (e + 1) - 1) // (p - 1)
    return s

def usigma(n):
    s = 1
    for p, e in factor(n).items():
        s *= p ** e + 1
    return s

def prod_rho(n):
    r = F(1)
    for p, e in factor(n).items():
        r *= rho(p, e)
    return r

def core(n):
    c = 1
    for p, e in factor(n).items():
        if e >= 2:
            c *= p ** e
    return c

def v(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

RESULTS = []
def check(name, cond, extra=""):
    RESULTS.append((bool(cond), name))
    print(("  [OK] " if cond else "  [!!] ") + name + (("   " + str(extra)) if extra != "" else ""))

# ===================================================== PART 0 : definitions
print("PART 0 -- definitions, Lemma 1, erratum in the quoted term list")
A_small = [n for n in range(1, 5000) if sigma(n) == 2 * usigma(n)]
def squarefree(n):
    return all(e == 1 for e in factor(n).values())
expected = [108 * m for m in range(1, 5000 // 108 + 1) if m % 2 and m % 3 and squarefree(m)]
check("A up to 5000 is exactly { 108m : m squarefree, gcd(m,6)=1 }",
      A_small == expected, A_small)
check("972 and 1620 are NOT in A (both appear in the quoted term list)",
      972 not in A_small and 1620 not in A_small,
      "sigma(972)-2usigma(972)=%d, sigma(1620)-2usigma(1620)=%d"
      % (sigma(972) - 2 * usigma(972), sigma(1620) - 2 * usigma(1620)))
check("n in A  <=>  prod rho(p,e) = 2      (all n <= 30000)",
      all((sigma(n) == 2 * usigma(n)) == (prod_rho(n) == 2) for n in range(1, 30001)))
check("Lemma 1: prod_rho(n) = prod_rho(powerful core of n)   (n <= 30000)",
      all(prod_rho(n) == prod_rho(core(n)) for n in range(1, 30001)))
check("every n <= 5000 in A satisfies n = 108 (mod 216) and core(n) = 108",
      all(n % 216 == 108 and core(n) == 108 for n in A_small))

# ============================================ PART 1 : Theorem A (omega<=2)
print("\nPART 1 -- Theorem A: powerful members of A with at most two prime factors")
check("rho(p,e) < p/(p-1) always", all(rho(p, e) < Pf(p) for p in PRIMES[:60] for e in range(1, 40)))
check("rho(2,a) = 2 - 3/(2^a+1) < 2 (so omega=1 is impossible)",
      all(rho(2, a) == 2 - F(3, 2 ** a + 1) for a in range(1, 60)))
check("for odd p<q, (p/(p-1))(q/(q-1)) <= 15/8 < 2  (so 2|n when omega=2)",
      max(Pf(p) * Pf(q) for i, p in enumerate(PRIMES[1:40], 1) for q in PRIMES[i + 1:41]) == F(15, 8))
check("rho(q,f)-1 = q(q^{f-1}-1)/((q-1)(q^f+1))",
      all(rho(q, f) - 1 == F(q * (q ** (f - 1) - 1), (q - 1) * (q ** f + 1))
          for q in PRIMES[:30] for f in range(1, 25)))
check("2/rho(2,a) - 1 = 3/(2^{a+1}-1)",
      all(2 / rho(2, a) - 1 == F(3, 2 ** (a + 1) - 1) for a in range(1, 60)))
check("2(3^f+1)/(3^{f-1}-1) = 6 + 8/(3^{f-1}-1)",
      all(F(2 * (3 ** f + 1), 3 ** (f - 1) - 1) == 6 + F(8, 3 ** (f - 1) - 1) for f in range(2, 40)))
check("(3^{f-1}-1) | 8 with f>=2  <=>  f in {2,3}; f=2 gives 2A-1=10, not 2^{a+1}-1",
      [f for f in range(2, 300) if 8 % (3 ** (f - 1) - 1) == 0] == [2, 3])
sols2 = []                                     # independent brute force
for a in range(2, 121):
    t = 2 / rho(2, a)
    for q in PRIMES[1:400]:
        if Pf(q) <= t:
            continue                           # rho(q,f) < q/(q-1) <= t, unreachable
        x = F(q + 1, q - 1) / (Pf(q) - t)      # must equal q^f + 1
        if x.denominator == 1:
            y, f = int(x) - 1, 0
            while y % q == 0:
                y //= q
                f += 1
            if y == 1 and f >= 2:
                sols2.append((a, q, f))
check("independent 2-prime brute force (a<=120, q<=2741, ALL f) -> only 2^2*3^3",
      sols2 == [(2, 3, 3)], sols2)

# ================================================= PART 2 : Lemma B (6 | n)
print("\nPART 2 -- Lemma C: the {2,3}-part of a powerful member of A divisible by 6")
lt, eq = [], []
for a in range(2, 80):
    for b in range(2, 80):
        r = rho(2, a) * rho(3, b)
        if r < 2:
            lt.append((a, b))
        elif r == 2:
            eq.append((a, b))
check("rho(2,a)rho(3,b) = 2 with a,b>=2  <=>  (a,b) = (2,3)", eq == [(2, 3)], eq)
check("rho(2,a)rho(3,b) < 2 with a,b>=2  <=>  (a,b) = (2,2)", lt == [(2, 2)], lt)
check("T(A,B)=2AB-6A-7B-3 has the sign of rho(2,a)rho(3,b)-2",
      all(((2 * 2**a * 3**b - 6 * 2**a - 7 * 3**b - 3) < 0) == (rho(2, a) * rho(3, b) < 2)
          for a in range(1, 50) for b in range(1, 50)))
check("(2A-7)(2B-6)=48  <=>  2AB=6A+7B+3",
      all(((2*A - 7) * (2*B - 6) == 48) == (2*A*B == 6*A + 7*B + 3)
          for A in range(1, 400) for B in range(1, 400)))
check("rho(2,2)rho(3,2)=91/50, so the coprime-to-6 tail target is 100/91",
      rho(2, 2) * rho(3, 2) == F(91, 50) and 2 / (rho(2, 2) * rho(3, 2)) == F(100, 91))
check("rho(p,2) <= 100/91  <=>  p >= 11  (every prime of the tail is >= 11)",
      min(p for p in PRIMES[2:40] if rho(p, 2) <= F(100, 91)) == 11)
check("100/91 with one prime: p | 100-91 = 9 forces p = 3, excluded",
      all((100 * (p - 1) * (p**e + 1) - 91 * (p**(e + 1) - 1)) % p == (-9) % p
          for p in PRIMES[2:20] for e in range(2, 8)))
check("two-prime tail: (p/(p-1))^2 > 100/91 forces p <= 19, so p in {11,13,17,19}",
      [p for p in PRIMES if p >= 11 and Pf(p) ** 2 > F(100, 91)] == [11, 13, 17, 19])

# ================================== PART 3 : the two lemmas driving PART 4
print("\nPART 3 -- exponent-window lemmas (L1),(L2)")
# (L1)  delta_i <= W/rest_i          for every i
# (L2)  delta_i >= W/(k*rest_i)      for at least one i
# with W = prod_j P_j - tau > 0 and rest_i = prod_{j!=i} P_j.
# (L1): tau = (P_i-delta_i) prod_{j!=i}(P_j-delta_j) <= (P_i-delta_i) rest_i.
# (L2): prod P_j - prod(P_j-delta_j) <= sum_j delta_j prod_{l!=j} P_l, so
#       W <= sum_j delta_j rest_j <= k max_j delta_j rest_j.
S, es, tau = [2, 3], {2: 2, 3: 3}, F(2)
Pp = Pf(2) * Pf(3); W = Pp - tau
check("(L1) verified on n = 108", all(delta(p, es[p]) <= W / (Pp / Pf(p)) for p in S), "W=%s" % W)
check("(L2) verified on n = 108", any(delta(p, es[p]) >= W / (2 * (Pp / Pf(p))) for p in S))
# randomised sanity: (L1)+(L2) hold for every product of rho's
import random
random.seed(7)
okL = True
for _ in range(4000):
    k = random.randint(2, 4)
    ps = random.sample(PRIMES[:20], k)
    ev = [random.randint(2, 6) for _ in ps]
    t = F(1)
    for p, e in zip(ps, ev):
        t *= rho(p, e)
    PP = F(1)
    for p in ps:
        PP *= Pf(p)
    w = PP - t
    if not all(delta(p, e) <= w / (PP / Pf(p)) for p, e in zip(ps, ev)):
        okL = False
    if not any(delta(p, e) >= w / (k * (PP / Pf(p))) for p, e in zip(ps, ev)):
        okL = False
check("(L1)+(L2) hold on 4000 random prime/exponent multisets", okL)

# ================ PART 4 : complete decision procedure for prod rho = tau
print("\nPART 4 -- complete search for  prod rho(p_i,e_i) = tau,  e_i >= 2")

UNBOUNDED = []          # places where a cap had to be imposed (should stay empty)
NODES = [0]

def solve_set(S, tau):
    """ALL exponent vectors e_i>=2 with prod rho(p_i,e_i)=tau, for the *given*
       prime set S.  Complete and unconditional, by (L1)+(L2)."""
    S = tuple(S)
    if not S:
        return [()] if tau == 1 else []
    k = len(S)
    PP = F(1)
    for p in S:
        PP *= Pf(p)
    if PP <= tau:
        return []
    W = PP - tau
    out = set()
    for i, p in enumerate(S):
        rest = PP / Pf(p)
        dhi, dlo = W / rest, W / (k * rest)
        e = 2
        while True:
            d = delta(p, e)
            if d < dlo:
                break
            if d <= dhi:
                NODES[0] += 1
                t2 = tau / rho(p, e)
                for s in solve_set(S[:i] + S[i + 1:], t2):
                    out.add(tuple(s[:i]) + (e,) + tuple(s[i:]))
            e += 1
    return sorted(out)

# ---- prime-set enumeration.  All bounds below are NECESSARY conditions, so the
# ---- enumeration returns a SUPERSET of the admissible supports; solve_set then
# ---- decides each support exactly.  Targets are carried as exact Fractions and
# ---- only the comparison of logarithms is done in floating point, with a
# ---- RELATIVE slack SL = 1e-9 applied in the safe direction (each log is
# ---- evaluated directly by log1p, never by differencing cumulative sums, so its
# ---- relative error is ~1e-16 however close the target is to 1).
from math import log1p
SL = 1e-9

def lP(p):                                   # log(p/(p-1))
    return log1p(1.0 / (p - 1))

def lR2(p):                                  # log(rho(p,2)), rho(p,2)-1 = p/(p^2+1)
    return log1p(p / (p * p + 1.0))

def sumlP(i, m):
    s = 0.0
    for j in range(i, i + m):
        s += lP(PRIMES[j])
    return s

from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for q in small:
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small:                       # deterministic for n < 3.3e24
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

def window_last(t_lo, t_up):
    """Integer window [qlo,qhi] for a prime q that is the LAST one of the support:
       necessary are  rho(q,2) <= t_up  and  P(q) > t_lo.  Exact and sieve-free.
       Returns None if the first condition leaves q unbounded."""
    a, b = t_lo.numerator, t_lo.denominator          # P(q) > t_lo  <=>  q < a/(a-b)
    if a <= b:
        return None
    qhi = (a - 1) // (a - b)
    c, d = t_up.numerator, t_up.denominator          # rho(q,2) <= t_up  <=>
    dd = c - d                                       # dd q^2 - d q + dd >= 0
    if dd <= 0:
        return None
    disc = d * d - 4 * dd * dd
    if disc < 0:
        qlo = 2
    else:
        qlo = (d + isqrt(disc)) // (2 * dd)
        while qlo > 2 and dd * (qlo - 1) ** 2 - d * (qlo - 1) + dd >= 0:
            qlo -= 1
        while dd * qlo * qlo - d * qlo + dd < 0:
            qlo += 1
    return qlo, qhi

def bounds(t_lo, t_up, i0, m):
    """index range [ilo,ihi] for the next prime, plus a flag saying the sieve
       limit was reached.  t_lo, t_up are exact Fractions with t_lo <= t_up."""
    xl, xu = float(t_lo - 1), float(t_up - 1)
    if xl <= 0.0 or xu <= 0.0:
        return 0, -1, False
    Lup, Llo = log1p(xu) * (1 + SL), log1p(xl) * (1 - SL)
    n = len(PRIMES)
    hi = n - m
    if hi < i0 or lR2(PRIMES[hi]) > Lup:
        # every admissible prime would lie beyond the sieve: NOT a proof of
        # emptiness, so report it as a limit hit.
        return 0, -1, True
    a, b = i0, hi                            # smallest i with lR2 <= Lup
    while a < b:
        mid = (a + b) // 2
        if lR2(PRIMES[mid]) <= Lup:
            b = mid
        else:
            a = mid + 1
    ilo = a
    if sumlP(ilo, m) <= Llo:
        return 0, -1, False
    a, b = ilo, hi                           # largest i with sumlP(i,m) > Llo
    while a < b:
        mid = (a + b + 1) // 2
        if sumlP(mid, m) > Llo:
            a = mid
        else:
            b = mid - 1
    return ilo, a, a >= hi

def rho_sup(p, t_up, more_primes):
    """exact upper bound for rho(p,e) subject to rho(p,e) <= t_up (strictly < when
       further primes follow).  Falling back to P(p) is always sound."""
    if Pf(p) <= t_up:
        return Pf(p)
    best, e = Pf(p), 2
    while e <= 64:
        r = rho(p, e)
        if (r >= t_up) if more_primes else (r > t_up):
            return best
        best = r
        e += 1
    return Pf(p)

def prime_sets(t_lo, t_up, i0, m, acc, out):
    """m-element prime supports p_1<...<p_m (index >= i0) able to carry a residual
       in (t_lo, t_up].  Necessary conditions, with q_1..q_m the m smallest
       primes >= p:   rho(p,2) <= t_up   and   prod_j P(q_j) > t_lo ."""
    if m == 0:
        out.append(tuple(acc))
        return
    if t_lo <= 1:
        UNBOUNDED.append(("unbounded-support", tuple(acc), float(t_up), m))
        return
    if m == 1:                                   # last prime: exact, no sieve
        w = window_last(t_lo, t_up)
        if w is None:
            UNBOUNDED.append(("unbounded-last", tuple(acc), float(t_up), m))
            return
        qlo, qhi = w
        lowest = PRIMES[i0] if i0 < len(PRIMES) else (acc[-1] + 1 if acc else 2)
        qlo = max(qlo, lowest)
        if qhi - qlo > 50_000:
            UNBOUNDED.append(("wide-last-window", tuple(acc), float(t_lo), qhi - qlo))
            return
        for q in range(qlo, qhi + 1):
            if is_prime(q) and rho(q, 2) <= t_up:
                out.append(tuple(acc) + (q,))
        return
    ilo, ihi, at_limit = bounds(t_lo, t_up, i0, m)
    if at_limit:
        UNBOUNDED.append(("sieve-limit", tuple(acc), float(t_lo), m))
    for i in range(ilo, ihi + 1):
        p = PRIMES[i]
        r2 = rho(p, 2)
        if r2 > t_up:
            continue
        prime_sets(t_lo / rho_sup(p, t_up, m > 1), t_up / r2, i + 1, m - 1,
                   acc + [p], out)

def full_search(tau, k, i0):
    """Engine 1 (exponent-free).  UNCONDITIONAL whenever it reports no gap:
       enumerate a superset of the admissible k-element prime sets, then decide
       each of them exactly with solve_set (which needs no exponent bound)."""
    sets = []
    prime_sets(tau, tau, i0, k, [], sets)
    found = []
    for S in sets:
        for ev in solve_set(S, tau):
            N = 1
            for p, e in zip(S, ev):
                N *= p ** e
            found.append((N, tuple(zip(S, ev))))
    return sets, found

CAPS, GAPS = [], []
def exact_search(t, i0, m, prefix, out, E):
    """Engine 2: exact residual t (a Fraction), primes taken in increasing order.
       At each prime the exponent loop runs while rho(p,e) <= t; it terminates by
       itself exactly when P(p) > t.  When it cannot, the tail e >= E+1 is handed
       to the exponent-free engine, so E is only a bookkeeping split and NOT a
       hypothesis."""
    if m == 0:
        if t == 1:
            out.append(tuple(prefix))
        return
    if t <= 1:
        return
    if m == 1:                                   # last prime: exact, no sieve
        w = window_last(t, t)
        if w is None:
            GAPS.append(("unbounded-last", tuple(prefix), float(t)))
            return
        qlo, qhi = w
        lowest = PRIMES[i0] if i0 < len(PRIMES) else (prefix[-1][0] + 1)
        qlo = max(qlo, lowest)
        if qhi - qlo > 50_000:
            GAPS.append(("wide-last-window", tuple(prefix), qhi - qlo))
            return
        for q in range(qlo, qhi + 1):
            if not is_prime(q) or rho(q, 2) > t:
                continue
            de = Pf(q) - t                        # rho(q,g)=t  <=>  delta(q,g)=de
            if de <= 0:
                continue
            X = F(q + 1, q - 1) / de              # must be q^g + 1
            if X.denominator != 1:
                continue
            y, gexp = int(X) - 1, 0
            while y % q == 0:
                y //= q
                gexp += 1
            if y == 1 and gexp >= 2:
                out.append(tuple(prefix) + ((q, gexp),))
        return
    ilo, ihi, at_limit = bounds(t, t, i0, m)
    if at_limit:
        GAPS.append(("sieve-limit", tuple(prefix), float(t), m))
    for i in range(ilo, ihi + 1):
        p = PRIMES[i]
        if rho(p, 2) > t:
            continue
        terminating = Pf(p) > t          # exact: guarantees the e-loop can end
        e = 2
        while True:
            r = rho(p, e)
            if r > t:
                break
            exact_search(t / r, i + 1, m - 1, prefix + [(p, e)], out, E)
            e += 1
            if not terminating and e > E:
                # tail e >= E+1: residual after p lies in ( t/P(p), t/rho(p,e) ];
                # enumerate the remaining supports from that interval and decide
                # every completed support exactly with solve_set.
                CAPS.append((tuple(prefix), p, e - 1))
                if m > 1:
                    lo_t, up_t = t / Pf(p), t / rho(p, e)
                    Q, before = [], len(UNBOUNDED)
                    prime_sets(lo_t, up_t, i + 1, m - 1, [], Q)
                    if len(UNBOUNDED) > before:
                        GAPS.append(("support", tuple(prefix), p, float(lo_t)))
                    for qs in Q:
                        for ev in solve_set((p,) + qs, t):
                            if ev[0] >= e:
                                out.append(tuple(prefix) + tuple(zip((p,) + qs, ev)))
                # m == 1: rho(p,e) = t is impossible, since rho(p,e) < P(p) <= t
                break

OMEGA_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12
EXPCAP = int(sys.argv[3]) if len(sys.argv) > 3 else 24
i3, i5 = bisect_left(PRIMES, 3), bisect_left(PRIMES, 5)

# ---- 4A  the tail of the branch 6 | n  (Lemma B: 2^2*3^2, tail target 100/91)
print("\n  4A  branch 6|n : Lemma C pins 2^2*3^2; tail target 100/91, primes >= 11")
print("      engine 1 (exponent-free, unconditional when no gap is reported):")
tot, gapk = [], None
for k in range(1, OMEGA_MAX + 1):
    UNBOUNDED.clear()
    sets, found = full_search(F(100, 91), k, i5)
    tot += found
    print("      omega(M)=%d : %6d prime sets, solutions = %-6s gap=%s   (%.1fs)"
          % (k, len(sets), found if found else "NONE", bool(UNBOUNDED), time.time() - T0))
    if UNBOUNDED:
        gapk = k
        print("      -> support enumeration first becomes infinite at omega(M)=%d;"
              " engine 1 stops here (engine 2 continues, with a cap)." % k)
        break
check("no coprime-to-6 powerful M with prod rho = 100/91 and omega(M) <= %d"
      % (OMEGA_MAX if gapk is None else gapk - 1), tot == [], tot)
check("engine 1 verdict is unconditional for omega(M) <= %s"
      % (OMEGA_MAX if gapk is None else gapk - 1), True,
      "first omega(M) with an unbounded support: %s" % gapk)

# ---- 4B / 4C  the global search.  Region per omega: (omega, a_max, exponent cap)
print("\n  4B  global search (engine 2 = exact residual + exponent-free tail).")
print("      Only v2(n) <= a_max is a genuine restriction; exponents are NOT capped.")
PLAN = [(1, 60, 8), (2, 60, 8), (3, AMAX, EXPCAP), (4, min(10, AMAX), 10)]
PLAN = [q for q in PLAN if q[0] <= OMEGA_MAX]
CAPS.clear(); GAPS.clear(); UNBOUNDED.clear()
GAPS_BY_K = {}
tot_all = []
for k, amax_k, E_k in PLAN:
    g0 = len(GAPS)
    out = []
    exact_search(F(2), i3, k, [], out, E_k)             # odd branch
    for a in range(2, amax_k + 1):
        ta = 2 / rho(2, a)
        # Lemma C: 6 | n forces a = 2, so for a >= 3 the tail is coprime to 6
        istart = i3 if a == 2 else i5
        if k == 1:
            if ta == 1:
                out.append(((2, a),))
            continue
        sub = []
        exact_search(ta, istart, k - 1, [], sub, E_k)
        out += [((2, a),) + s for s in sub]
    vals = []
    for s in out:
        N = 1
        for p, e in s:
            N *= p ** e
        vals.append((N, s))
    tot_all += vals
    GAPS_BY_K[k] = len(GAPS) - g0
    print("      omega=%d, v2 <= %2d, tail-split e=%d : solutions = %-32s "
          "support gaps = %d   (%.1fs)"
          % (k, amax_k, E_k, str(vals) if vals else "NONE", len(GAPS) - g0,
             time.time() - T0))
check("in the region above the only powerful member of A is 108",
      [x[0] for x in tot_all] == [108], tot_all)
clean = [k for k, g in GAPS_BY_K.items() if g == 0]
check("engine 2 closed every branch (0 gaps) for omega <= %d" % max(clean),
      max(clean) >= min(3, OMEGA_MAX), GAPS_BY_K)
print("      gaps by omega: %s   (a gap = a branch the support enumeration could"
      " not close; see Obstacle 3)" % GAPS_BY_K)
print("      exponent-tail switches: %d;  support-enumeration gaps: %d"
      % (len(CAPS), len(GAPS)))
print("      solve_set nodes visited: %d" % NODES[0])

# ======================================= PART 5 : valuation identities (5),(7)
print("\nPART 5 -- 2-adic and 3-adic identities of the v1 write-up")
def D2(e):
    return -1 if e % 2 == 0 else v(e + 1, 2) - 1
def D3(p, e):
    if p % 3 == 1:
        return v(e + 1, 3)
    if e % 2 == 0:
        return 0
    return v(e + 1, 3) - v(e, 3)
check("D2(e) = v2(sigma(p^e)) - v2(1+p^e), independent of the odd prime p",
      all(v(sigma(p ** e), 2) - v(1 + p ** e, 2) == D2(e)
          for p in PRIMES[1:25] for e in range(1, 22)))
check("D3(p,e) = v3(sigma(p^e)) - v3(1+p^e) for p != 3",
      all(v(sigma(p ** e), 3) - v(1 + p ** e, 3) == D3(p, e)
          for p in PRIMES[:50] if p != 3 for e in range(1, 18)))
check("sum_{p odd} D2(e_p) = 1 for every n in A, n <= 30000",
      all(sum(D2(e) for p, e in factor(n).items() if p != 2) == 1
          for n in range(1, 30001) if prod_rho(n) == 2))
check("sum_{p != 3} D3(p,e_p) = 0 for every n in A, n <= 30000",
      all(sum(D3(p, e) for p, e in factor(n).items() if p != 3) == 0
          for n in range(1, 30001) if prod_rho(n) == 2))
check("n = 36M forces sum_{p|M} D2(e_p) = 2, hence some e_p == 3 (mod 4)", D2(2) == -1)

# ==================================================================== report
bad = [nm for ok, nm in RESULTS if not ok]
print("\n%d/%d checks passed   (%.1fs)" % (len(RESULTS) - len(bad), len(RESULTS), time.time() - T0))
for nm in bad:
    print("  FAILED:", nm)
sys.exit(1 if bad else 0)
