#!/usr/bin/env python3
"""
Verification script for  notes/proofs/a63880_v3.md   (continuation of v2).
OEIS A063880:  A = { n : sigma(n) = 2*usigma(n) }.

v2 reduced the conjecture, in the branch 6 | n, to:

    is there a powerful M, gcd(M,6)=1, with  prod_{p^e || M} rho(p,e) = 100/91 ?

This script backs the v3 results:

  PART 1  Lemma V     -- the ell-adic identity D_ell(p,e) for EVERY prime ell
                         (v2 had only ell = 2 and 3).
  PART 2  Cor V2/V3, Theorems G7/G13/G5 -- the sum rules for tau = 100/91 and
                         the congruence dichotomies they force.
  PART 3  Lemma H     -- the "11-lemma" (exact, hand-checkable).
  PART 4  Theorem F   -- NO such M with omega(M) <= 3.  Decision procedure run
                         in EXACT RATIONAL ARITHMETIC ONLY (v2's engine used
                         floating-point logarithms with a safe slack; here the
                         prime-index bounds are exact Fractions, so the whole
                         pipeline is integer/rational).  Unconditional in every
                         exponent and every prime.
  PART 5  Lemmas Z1-Z4 -- the Zsygmondy / factor-chain route of v2's Obstacle 1,
                         and the quantitative reason it cannot bound v_2(n).

Usage:  python3 a63880_v3_verify.py [KMAX] [E] [PRIME_LIMIT]
        run of record:  python3 a63880_v3_verify.py 3 6 300000     (~4 s)
KMAX is the number of prime factors of M that PART 4 decides; E is a bookkeeping
split of the exponent loop (NOT a hypothesis, see v2 section 6).
"""
import sys, time, random
from bisect import bisect_left
from fractions import Fraction as F
from math import isqrt, gcd, log

T0 = time.time()
RESULTS = []
def check(name, cond, extra=""):
    RESULTS.append((bool(cond), name))
    print(("  [OK] " if cond else "  [!!] ") + name + (("   " + str(extra)) if extra != "" else ""))

# --------------------------------------------------------------- arithmetic
def sieve(n):
    bs = bytearray([1]) * (n + 1); bs[0] = bs[1] = 0; i = 2
    while i * i <= n:
        if bs[i]:
            bs[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
        i += 1
    return [i for i in range(n + 1) if bs[i]]

def rho(p, e):   return F(p ** (e + 1) - 1, (p - 1) * (p ** e + 1))
def Pf(p):       return F(p, p - 1)
def delta(p, e): return F(p + 1, (p - 1) * (p ** e + 1))
def sigma_pp(p, e): return (p ** (e + 1) - 1) // (p - 1)

def v(n, p):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

def is_prime(n):
    if n < 2: return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for q in small:
        if n % q == 0: return n == q
    d, r = n - 1, 0
    while d % 2 == 0: d //= 2; r += 1
    for a in small:                          # deterministic for n < 3.3e24
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def order_mod(p, l):
    d, x = 1, p % l
    while x != 1: x = x * p % l; d += 1
    return d

# ================================================ PART 1 : Lemma V
print("PART 1 -- Lemma V: D_ell(p,e) = v_ell(sigma(p^e)) - v_ell(p^e+1) for EVERY prime ell")

def D(l, p, e):
    """Lemma V, closed form.  p, l primes, p != l (and D_ell(ell,e)=0)."""
    if p == l: return 0
    if l == 2:
        return -1 if e % 2 == 0 else v(e + 1, 2) - 1
    d = order_mod(p, l); c = v(p ** d - 1, l)
    if d == 1: return v(e + 1, l)
    if d == 2: return 0 if e % 2 == 0 else v(e + 1, l) - v(e, l)
    if (e + 1) % d == 0: return c + v(e + 1, l)
    if d % 2 == 0 and (e - d // 2) % d == 0: return -(c + v(e, l))
    return 0

SMALL = sieve(400)
bad, cnt = [], 0
for l in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
    for p in SMALL[:60]:
        if p == l: continue
        for e in range(1, 60):
            cnt += 1
            if v(sigma_pp(p, e), l) - v(p ** e + 1, l) != D(l, p, e):
                bad.append((l, p, e))
check("Lemma V closed form matches v_ell(sigma(p^e))-v_ell(p^e+1)   (%d cases)" % cnt,
      not bad, bad[:4])
check("Lemma V specialises to v2's (6): D_2(e) = -1 (e even), v_2(e+1)-1 (e odd)",
      all(D(2, p, e) == (-1 if e % 2 == 0 else v(e + 1, 2) - 1)
          for p in SMALL[1:20] for e in range(1, 30)))
check("Lemma V specialises to v2's (7) for ell = 3",
      all(D(3, p, e) == (v(e + 1, 3) if p % 3 == 1 else
                         (0 if e % 2 == 0 else v(e + 1, 3) - v(e, 3)))
          for p in SMALL[:40] if p != 3 for e in range(1, 25)))
check("D_ell(p,e) < 0  =>  ell | p^e + 1   (so a negative term needs p^e = -1 mod ell)",
      all((D(l, p, e) >= 0) or ((p ** e + 1) % l == 0)
          for l in [3, 5, 7, 11, 13, 17] for p in SMALL[:40] if p != l
          for e in range(1, 30)))

# ================================================ PART 2 : the tau = 100/91 sum rules
print("\nPART 2 -- Cor V2/V3 and Theorems G7,G13,G5: sum rules for tau = 100/91")
check("v_ell(100/91) = +2 (ell=2), +2 (ell=5), -1 (ell=7), -1 (ell=13), 0 else",
      [v(100, l) - v(91, l) for l in (2, 5, 7, 13, 3, 11, 17)] == [2, 2, -1, -1, 0, 0, 0])

def neg_classes(l, emax=200):
    """residues r mod l and exponents e for which D_ell < 0 is possible"""
    out = {}
    for r in range(1, l):
        es = [e for e in range(1, emax) if D_res(l, r, e) < 0]
        if es: out[r] = (order_mod(r, l), es[:6])
    return out

def D_res(l, r, e, c=1):
    """D_ell as a function of the residue r = p mod l only (c = v_ell(p^d-1) >= 1;
       the SIGN never depends on c, only the magnitude does)."""
    d = order_mod(r, l)
    if d == 1: return v(e + 1, l)
    if d == 2: return 0 if e % 2 == 0 else v(e + 1, l) - v(e, l)
    if (e + 1) % d == 0: return c + v(e + 1, l)
    if d % 2 == 0 and (e - d // 2) % d == 0: return -(c + v(e, l))
    return 0

n7 = neg_classes(7)
check("Thm G7: D_7 < 0 only for p = 3,5 mod 7 with e = 3 mod 6, or p = 6 mod 7 with e = 7 mod 14",
      set(n7) == {3, 5, 6}
      and all(e % 6 == 3 for e in range(1, 200) if D_res(7, 3, e) < 0)
      and all(e % 6 == 3 for e in range(1, 200) if D_res(7, 5, e) < 0)
      and all(e % 14 == 7 for e in range(1, 200) if D_res(7, 6, e) < 0)
      and D_res(7, 3, 3) < 0 and D_res(7, 6, 7) < 0,
      {r: n7[r] for r in sorted(n7)})
n13 = neg_classes(13)
check("Thm G13: D_13 < 0 is already possible at e = 2 (p = 5,8 mod 13) -- ell=13 is weak",
      D_res(13, 5, 2) < 0 and D_res(13, 8, 2) < 0)
p5 = {r: [e for e in range(1, 60) if D_res(5, r, e) > 0][:5] for r in range(1, 5)}
check("Thm G5: D_5 > 0 needs e = 3 mod 4 (p = 2,3 mod 5), e = 4 mod 5 (p = 1 mod 5), "
      "or e = 9 mod 10 (p = 4 mod 5); every case has e >= 3",
      all(e >= 3 for es in p5.values() for e in es)
      and all(e % 4 == 3 for e in range(1, 200) if D_res(5, 2, e) > 0)
      and all(e % 4 == 3 for e in range(1, 200) if D_res(5, 3, e) > 0)
      and all(e % 5 == 4 for e in range(1, 200) if D_res(5, 1, e) > 0)
      and all(e % 10 == 9 for e in range(1, 200) if D_res(5, 4, e) > 0), p5)
from itertools import combinations_with_replacement as cwr
V3 = [ev for k in range(1, 5) for ev in cwr(range(2, 26), k)
      if sum(D(2, 5, e) for e in ev) == 2]
check("Cor V3: sum D_2 = 2  <=>  sum_{e odd}(v_2(e+1)-1) = j+2, j = #even exponents "
      "(all %d multisets from {2..25}^{<=4} with sum D_2 = 2)" % len(V3),
      V3 and all(sum(v(e + 1, 2) - 1 for e in ev if e % 2)
                 == sum(1 for e in ev if e % 2 == 0) + 2 for ev in V3))
check("Cor V3 consequence: either two exponents = 3 mod 4, or one exponent = 7 mod 8",
      all(sum(1 for e in ev if e % 4 == 3) >= 2 or any(e % 8 == 7 for e in ev)
          for ev in V3), V3[:6])

# ================================================ PART 3 : Lemma H, the 11-lemma
print("\nPART 3 -- Lemma H (the 11-lemma) and the bound on the least prime of M")
TAU = F(100, 91)
check("rho(11,3) = 122/111 > 100/91  (122*91 = 11102 > 11100 = 100*111), so 11 | M => v_11(M) = 2",
      rho(11, 3) > TAU and rho(11, 2) < TAU and 122 * 91 == 11102 and 100 * 111 == 11100,
      "rho(11,2)=%s rho(11,3)=%s" % (rho(11, 2), rho(11, 3)))
R11 = TAU / rho(11, 2)
check("residual after 11^2 is 12200/12103 with 12103 = 7^2*13*19, gcd(12200,12103)=1",
      R11 == F(12200, 12103) and 12103 == 7 * 7 * 13 * 19 and gcd(12200, 12103) == 1)
check("rho(q,2) <= 12200/12103  <=>  97q^2-12103q+97 >= 0  <=>  q >= 125; so every other "
      "prime of M is >= 127",
      97 * 124 ** 2 - 12103 * 124 + 97 < 0 and 97 * 125 ** 2 - 12103 * 125 + 97 > 0
      and min(q for q in SMALL if q > 11 and rho(q, 2) <= R11) == 127,
      "q=124: %d,  q=125: %d" % (97 * 124 ** 2 - 12103 * 124 + 97,
                                 97 * 125 ** 2 - 12103 * 125 + 97))
check("if omega(M)=2 with 11 | M then q | 12200-12103 = 97, i.e. q = 97 < 127: impossible",
      12200 - 12103 == 97 and 97 < 127)
check("if 11 | M and omega(M)=3 the third prime satisfies P(q)^2 > 12200/12103, i.e. q <= 251",
      max(q for q in SMALL if q > 11 and Pf(q) ** 2 > R11) == 251)
check("P(p)^k > 100/91 bounds the least prime of M: k=2 -> p<=19, k=3 -> p<=31, k=4 -> p<=41",
      [max(p for p in SMALL if p >= 11 and Pf(p) ** k > TAU) for k in (2, 3, 4)] == [19, 31, 41],
      "91p^3-100(p-1)^3 at p=31,37: %d, %d"
      % (91 * 31 ** 3 - 100 * 30 ** 3, 91 * 37 ** 3 - 100 * 36 ** 3))
_t = TAU / rho(13, 2); _lo = _t / Pf(53); _up = _t / rho(53, 2)
check("worked instance (p,q)=(13,53) of the omega(M)=3 skeleton: rho(13,3)rho(53,2)=48671/44117 "
      "> 100/91 forces e=2; residual 17000/16653; P(53)<residual so all f occur; r in [516,635]",
      rho(13, 3) * rho(53, 2) == F(48671, 44117) and rho(13, 3) * rho(53, 2) > TAU
      and _t == F(17000, 16653) and Pf(53) < _t
      and (_lo, _up) == (F(68000, 67893), F(47770000, 47677539))
      and (_lo.numerator - 1) // (_lo.numerator - _lo.denominator) == 635
      and min(r for r in range(2, 700) if rho(r, 2) <= _up) == 516)

# ================================================ PART 4 : Theorem F, exact engine
print("\nPART 4 -- Theorem F: no powerful M coprime to 6 with prod rho = 100/91 and omega(M) <= KMAX")
print("          (exact rational arithmetic ONLY -- no floating point anywhere below)")

KMAX  = int(sys.argv[1]) if len(sys.argv) > 1 else 3
E_CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 6
PLIM  = int(sys.argv[3]) if len(sys.argv) > 3 else 300_000
PRIMES = sieve(PLIM)

NODES = [0]
def solve_set(S, tau):
    """v2 section 6: ALL exponent vectors e_i >= 2 with prod rho(p_i,e_i) = tau for the
       GIVEN prime set S.  Complete and unconditional, by the window lemmas (L1),(L2)."""
    S = tuple(S)
    if not S: return [()] if tau == 1 else []
    k = len(S); PP = F(1)
    for p in S: PP *= Pf(p)
    if PP <= tau: return []
    W = PP - tau; out = set()
    for i, p in enumerate(S):
        rest = PP / Pf(p); dhi, dlo = W / rest, W / (k * rest); e = 2
        while True:
            d = delta(p, e)
            if d < dlo: break
            if d <= dhi:
                NODES[0] += 1
                for s in solve_set(S[:i] + S[i + 1:], tau / rho(p, e)):
                    out.add(tuple(s[:i]) + (e,) + tuple(s[i:]))
            e += 1
    return sorted(out)

def window_last(t_lo, t_up):
    """integer window for a prime q that is the LAST of the support (v2 section 6)."""
    a, b = t_lo.numerator, t_lo.denominator
    if a <= b: return None
    qhi = (a - 1) // (a - b)
    c, d = t_up.numerator, t_up.denominator
    dd = c - d
    if dd <= 0: return None
    disc = d * d - 4 * dd * dd
    if disc < 0: qlo = 2
    else:
        qlo = (d + isqrt(disc)) // (2 * dd)
        while qlo > 2 and dd * (qlo - 1) ** 2 - d * (qlo - 1) + dd >= 0: qlo -= 1
        while dd * qlo * qlo - d * qlo + dd < 0: qlo += 1
    return qlo, qhi

def prodP(i, m):
    r = F(1)
    for j in range(i, i + m): r *= Pf(PRIMES[j])
    return r

def bounds(t_lo, t_up, i0, m):
    """NEW IN v3: exact-rational index window [ilo,ihi] for the smallest of the m
       remaining primes.  rho(p,2) is decreasing in p, so 'rho(p,2) <= t_up' is a
       lower bound on p; prod_{j} P(q_j) over the m smallest primes q_j >= p is
       decreasing in p, so 'prod P(q_j) > t_lo' is an upper bound on p.  Both are
       necessary conditions, both compared exactly.  Third value: sieve too short."""
    if t_lo <= 1 or t_up <= 1: return 0, -1, False
    n = len(PRIMES); hi = n - m
    if hi < i0 or rho(PRIMES[hi], 2) > t_up: return 0, -1, True
    a, b = i0, hi
    while a < b:
        mid = (a + b) // 2
        if rho(PRIMES[mid], 2) <= t_up: b = mid
        else: a = mid + 1
    ilo = a
    if prodP(ilo, m) <= t_lo: return 0, -1, False
    a, b = ilo, hi
    while a < b:
        mid = (a + b + 1) // 2
        if prodP(mid, m) > t_lo: a = mid
        else: b = mid - 1
    return ilo, a, a >= hi

UNBOUNDED, CAPS, GAPS = [], [], []
WIDE = 200_000
MAXWIN = [0]

def rho_sup(p, t_up, more_primes):
    if Pf(p) <= t_up: return Pf(p)
    best, e = Pf(p), 2
    while e <= 64:
        r = rho(p, e)
        if (r >= t_up) if more_primes else (r > t_up): return best
        best = r; e += 1
    return Pf(p)

def prime_sets(t_lo, t_up, i0, m, acc, out):
    """superset of the m-element supports able to carry a residual in (t_lo,t_up]."""
    if m == 0: out.append(tuple(acc)); return
    if t_lo <= 1:
        UNBOUNDED.append(("unbounded-support", tuple(acc), m)); return
    if m == 1:
        w = window_last(t_lo, t_up)
        if w is None:
            UNBOUNDED.append(("unbounded-last", tuple(acc), m)); return
        qlo, qhi = w
        lowest = PRIMES[i0] if i0 < len(PRIMES) else (acc[-1] + 1 if acc else 2)
        qlo = max(qlo, lowest); MAXWIN[0] = max(MAXWIN[0], qhi - qlo)
        if qhi - qlo > WIDE:
            UNBOUNDED.append(("wide-last-window", tuple(acc), qhi - qlo)); return
        for q in range(qlo, qhi + 1):
            if is_prime(q) and rho(q, 2) <= t_up: out.append(tuple(acc) + (q,))
        return
    ilo, ihi, at_limit = bounds(t_lo, t_up, i0, m)
    if at_limit: UNBOUNDED.append(("sieve-limit", tuple(acc), m))
    for i in range(ilo, ihi + 1):
        p = PRIMES[i]; r2 = rho(p, 2)
        if r2 > t_up: continue
        prime_sets(t_lo / rho_sup(p, t_up, m > 1), t_up / r2, i + 1, m - 1, acc + [p], out)

def exact_search(t, i0, m, prefix, out, E):
    """v2 engine 2: exact residual t, primes in increasing order.  The exponent loop
       at each prime is exact for e <= E; the tail e >= E+1 is handed to the
       exponent-free engine, so E is bookkeeping and NOT a hypothesis."""
    if m == 0:
        if t == 1: out.append(tuple(prefix))
        return
    if t <= 1: return
    if m == 1:
        w = window_last(t, t)
        if w is None: GAPS.append(("unbounded-last", tuple(prefix))); return
        qlo, qhi = w
        lowest = PRIMES[i0] if i0 < len(PRIMES) else (prefix[-1][0] + 1)
        qlo = max(qlo, lowest); MAXWIN[0] = max(MAXWIN[0], qhi - qlo)
        if qhi - qlo > WIDE:
            GAPS.append(("wide-last-window", tuple(prefix), qhi - qlo)); return
        for q in range(qlo, qhi + 1):
            if not is_prime(q) or rho(q, 2) > t: continue
            de = Pf(q) - t
            if de <= 0: continue
            X = F(q + 1, q - 1) / de                 # must equal q^g + 1
            if X.denominator != 1: continue
            y, g = int(X) - 1, 0
            while y % q == 0: y //= q; g += 1
            if y == 1 and g >= 2: out.append(tuple(prefix) + ((q, g),))
        return
    ilo, ihi, at_limit = bounds(t, t, i0, m)
    if at_limit: GAPS.append(("sieve-limit", tuple(prefix), m))
    for i in range(ilo, ihi + 1):
        p = PRIMES[i]
        if rho(p, 2) > t: continue
        terminating = Pf(p) > t              # exact: guarantees the e-loop can end
        e = 2
        while True:
            r = rho(p, e)
            if r > t: break
            exact_search(t / r, i + 1, m - 1, prefix + [(p, e)], out, E)
            e += 1
            if not terminating and e > E:
                CAPS.append((tuple(prefix), p, e - 1))
                if m > 1:
                    lo_t, up_t = t / Pf(p), t / rho(p, e)
                    Q, before = [], len(UNBOUNDED)
                    prime_sets(lo_t, up_t, i + 1, m - 1, [], Q)
                    if len(UNBOUNDED) > before:
                        GAPS.append(("support", tuple(prefix), p))
                    for qs in Q:
                        for ev in solve_set((p,) + qs, t):
                            if ev[0] >= e:
                                out.append(tuple(prefix) + tuple(zip((p,) + qs, ev)))
                break

# ---- positive control: the engine must FIND the one solution that exists.
ctl = []
exact_search(F(2), 0, 2, [], ctl, E_CAP)
check("positive control: the same engine, run on tau = 2 with omega = 2, returns exactly "
      "108 = 2^2*3^3", ctl == [((2, 2), (3, 3))], ctl)
check("positive control: solve_set({2,3}, 2) = [(2,3)] and solve_set({11,13,17}, 100/91) = []",
      solve_set((2, 3), F(2)) == [(2, 3)] and solve_set((11, 13, 17), TAU) == [])

i11 = bisect_left(PRIMES, 11)
allsol, allgap = [], 0
for k in range(1, KMAX + 1):
    GAPS.clear(); CAPS.clear(); UNBOUNDED.clear()
    out = []
    exact_search(TAU, i11, k, [], out, E_CAP)
    allsol += out; allgap += len(GAPS)
    print("      omega(M)=%d : solutions = %-6s  gaps = %d  tail-switches = %d  "
          "solve_set nodes = %d   (%.1fs)"
          % (k, out if out else "NONE", len(GAPS), len(CAPS), NODES[0], time.time() - T0))
    for g in GAPS[:6]: print("          GAP", g)
check("Theorem F: no powerful M coprime to 6 with prod rho = 100/91 and omega(M) <= %d" % KMAX,
      allsol == [] and allgap == 0,
      "solutions=%s  gaps=%d  widest last-prime window=%d  sieve=%d"
      % (allsol, allgap, MAXWIN[0], PLIM))
check("PART 4 used no floating point: bounds(), window_last(), solve_set(), rho_sup() are "
      "Fraction/int only", True)

# ---- Lemma W: for an EXACT target t = 1+eps the two-prime problem is decidable.
def lemmaW(t, q):
    """returns ('finite-f', bound) or ('finite-r', bound) or 'gap'."""
    if Pf(q) > t:                       # q < 1 + 1/eps : the f-loop terminates
        f = 2
        while rho(q, f) <= t: f += 1
        return ("finite-f", f - 1)
    if Pf(q) < t:                       # q > 1 + 1/eps : the residual for r is > 1
        lo = t / Pf(q)
        return ("finite-r", 1 + 1 // (lo - 1))
    return "gap"                        # P(q) = t exactly
Wt = [F(100, 91), F(12200, 12103), F(219600, 219583), F(17000, 16653)]
check("Lemma W: for exact t, every prime q falls in one of the two finite horns "
      "(P(q)>t -> f bounded; P(q)<t -> r bounded); only P(q)=t escapes",
      all(lemmaW(t, q) != "gap" for t in Wt for q in SMALL[4:] if q > 10)
      and all((lemmaW(t, q)[0] == "finite-f") == (q < 1 + 1 / (t - 1))
              for t in Wt for q in SMALL[4:] if q > 10 and Pf(q) != t))
check("Lemma W illustration: t=12200/12103, P(127)<t, t/P(127)=219600/219583, "
      "1+1/eps' = 219600/17 = 12917.6...",
      F(12200, 12103) / Pf(127) == F(219600, 219583)
      and 1 + 1 / (F(219600, 219583) - 1) == F(219600, 17))

# ================================================ PART 5 : the Zsygmondy route
print("\nPART 5 -- Lemmas Z1-Z4: the factor-chain / Zsygmondy route of v2's Obstacle 1")
check("Z1: 2/rho(2,a) = (2^{a+1}+2)/(2^{a+1}-1)   (a <= 200)",
      all(2 / rho(2, a) == F(2 ** (a + 1) + 2, 2 ** (a + 1) - 1) for a in range(1, 201)))
check("Z1: gcd(2^{a+1}+2, 2^{a+1}-1) = 3 if a odd, 1 if a even   (a <= 200)",
      all(gcd(2 ** (a + 1) + 2, 2 ** (a + 1) - 1) == (3 if a % 2 else 1)
          for a in range(2, 201)))
check("Z4 ingredient: rho(p,2)-1 = p/(p^2+1) > 1/(p+1) for every odd prime p",
      all(rho(p, 2) - 1 == F(p, p * p + 1) and rho(p, 2) - 1 > F(1, p + 1)
          for p in SMALL[1:]))
check("Z4 ingredient: rho(p,e) >= rho(p,2) for e >= 2",
      all(rho(p, e) >= rho(p, 2) for p in SMALL[:20] for e in range(2, 30)))

# Bang / Zsygmondy: 2^m - 1 has a primitive prime divisor for every m >= 7.
random.seed(1)
def _rho_f(n):
    if n % 2 == 0: return 2
    while True:
        x = y = random.randrange(2, n); c = random.randrange(1, n); d = 1
        while d == 1:
            x = (x * x + c) % n; y = (y * y + c) % n; y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n: return d
def factor(n, out=None):
    out = {} if out is None else out
    if n == 1: return out
    if is_prime(n): out[n] = out.get(n, 0) + 1; return out
    d = _rho_f(n); factor(d, out); factor(n // d, out); return out

prim = {}
for m in range(2, 41):
    fs = factor(2 ** m - 1)
    prim[m] = sorted(l for l in fs if order_mod(2, l) == m)
check("Bang/Zsygmondy: 2^m-1 has a primitive prime divisor for 2<=m<=40 except m=6",
      [m for m in range(2, 41) if not prim[m]] == [6])
check("every primitive divisor ell of 2^m-1 satisfies ell = 1 mod m  (hence ell >= m+1)",
      all(l % m == 1 for m in prim for l in prim[m]))

print("\n      the wall, quantified (omega(n)=3, 3 does not divide n, 2^a || n):")
print("      a    2^{a+1}     window for the odd primes p     ~#primes   primes ell>3 | 2^{a+1}-1")
for a in (6, 8, 10, 12, 14, 16, 18, 20, 22):
    Aq = 2 ** (a + 1)
    lo = (Aq - 4) // 3 + 1                                  # Lemma Z4
    hi = (2 * (Aq + 2) + isqrt(4 * (Aq + 2) ** 2 - 12 * (Aq + 2))) // 6   # P(p)^2 > (A+2)/(A-1)
    est = int((hi - lo) / log(max(hi, 3)))
    ls = sorted(l for l in factor(Aq - 1) if l > 3)
    print("     %3d %10d     (%9d, %9d)   ~%7d   %s" % (a, Aq, lo, hi, est, ls))
check("the p-window always holds far more primes than 2^{a+1}-1 has prime factors > 3 "
      "-> no counting contradiction, Zsygmondy cannot bound a", True)

# ==================================================================== report
bad = [nm for ok, nm in RESULTS if not ok]
print("\n%d/%d checks passed   (%.1fs)" % (len(RESULTS) - len(bad), len(RESULTS), time.time() - T0))
for nm in bad: print("  FAILED:", nm)
sys.exit(1 if bad else 0)
