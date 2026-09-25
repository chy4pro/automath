#!/usr/bin/env python3
"""
Erdos #889, Theorem A / A_l / A_unif: rigorous computation of the thresholds.

Usage:
    export PATH="$HOME/.local/bin:$PATH"
    python3 n0_compute.py            # constants and thresholds (under 1 s)
    python3 n0_compute.py --check    # also the finite check of Lemma R (evidence only, about 6 s)

Every real quantity is an mpmath interval (iv context, outward rounding, 60 digits).
Printed numbers are rounded for display; a single number means both endpoints round to it.
A quantity used as an upper bound is read at its upper endpoint and a lower bound at its lower
endpoint. Each inequality that the proof needs is certified from the endpoints and printed
as 'OK' or 'FAIL'. The notation follows PROOF_THEOREM_A.md, sections 4-7:

  L = log n, ell = log L, c = C0 = 10, m = log(c*l),
  R11 = 1.3841 (Robin 1983, Thm 11), C1(t) = Matveev's C_1(t, kappa=1) (Cor. 2.3),
  kappa1, kappa2, kappa3, K as defined in (5.1) of the proof,
  phi(ell1) = ell1 - 5 log ell1 - log K(ell1).

If phi(ell1) >= 0 (and the side conditions hold), Theorem A_l holds for every n with
log log n >= ell1, i.e. n >= N(l) := exp(exp(ell1)).
"""
import sys
from mpmath import iv

iv.dps = 60
I = iv.mpf
E = iv.e
LOG2 = iv.log(I(2))
R11 = I('1.3841')    # Robin 1983, Theoreme 11: omega(n) <= 1.3841 log n / log log n, n >= 3
R13 = I('1.1714')    # Robin 1983, Theoreme 13: omega(n) <= log n / (log log n - 1.1714), n >= 26

ALL_OK = True


def ok(cond, label):
    global ALL_OK
    if not cond:
        ALL_OK = False
    print(f"    [{'OK' if cond else 'FAIL'}] {label}")


def s(x, d=12):
    """Display an interval as [lo, hi], each endpoint rounded to d significant digits.
    Display only: every certified comparison below uses the exact interval endpoints."""
    from mpmath import mp, nstr
    lo = mp.mpf(x.a._mpi_[0]); hi = mp.mpf(x.b._mpi_[1])
    a, b = nstr(lo, d), nstr(hi, d)
    return a if a == b else f"[{a}, {b}]"


def C1(t):
    """Matveev 2000, Cor. 2.3, kappa = 1 (K = Q subset R):
    C_1(t,1) = min{ (e t / 2) * 30^(t+3) * t^3.5 , 2^(6t+20) }. Returns an enclosure."""
    t = I(t)
    a = (E * t / 2) * I(30) ** (t + 3) * t ** 3 * iv.sqrt(t)
    b = I(2) ** (6 * t + 20)
    return iv.mpf([min(a.a, b.a), min(a.b, b.b)]), a, b


C1_3, C1_3a, C1_3b = C1(3)
C1_2, C1_2a, C1_2b = C1(2)


# ---------------------------------------------------------------------------------------------
# Section 5 of the proof: fixed l, main line (RS (3.5), Robin Thm 11, Matveev with B*)
# ---------------------------------------------------------------------------------------------
def fixed_l(ell1, l, c='10', R=R11, C13=None):
    C13 = C1_3 if C13 is None else C13
    l1 = I(ell1); L_ = I(l); c = I(c)
    d = {}
    d['m'] = m = iv.log(c * L_)
    d['kappa1'] = k1 = 1 + m / l1
    d['kappa2'] = k2 = 1 + (1 - iv.log(LOG2) + iv.exp(-l1)) / l1
    d['mu'] = mu = 2 * R * m / (c - 2 * R)
    d['ratio'] = ratio = (l1 + m - 1) / (l1 - mu)
    d['eps1'] = eps1 = 3 * iv.exp(-l1) / (c * (l1 + m - 1))
    d['e1'] = e1 = 2 * c + (2 * c * (m - 1) + 2 * R / l1 + 6 * iv.exp(-l1) + 1) / l1
    d['eps2'] = eps2 = e1 * k1 / ((c - 2 * R) * (1 - mu / l1)) * l1 ** 2 * iv.exp(-l1)
    d['kappa3'] = k3 = c / (c - 2 * R) * ratio * k1 * (1 + eps1) / (1 - eps2)
    d['K'] = K = C13 * k1 ** 2 * k2 * k3 + k1 / l1 ** 4
    d['phi'] = l1 - 5 * iv.log(l1) - iv.log(K)
    d['side'] = [
        (l1.a >= 10, 'ell1 >= 10 (phi increasing, ell^2 e^-ell decreasing)'),
        ((l1 - mu).a > 0, 'ell1 > mu'),
        (eps2.b < 1, 'eps2 < 1 (so A - 1 > 0)'),
        ((k3 * l1 ** 2).a >= 0.16, 'kappa3 * ell1^2 >= 0.16'),
        ((m - 1).a > 0, 'm > 1 (monotonicity of ratio, sign of e1 bracket)'),
        ((c * L_ * iv.exp(iv.exp(l1)) - 67).a > 0, 'y = c l L >= 67 (so >= 17)'),
    ]
    return d


# ---------------------------------------------------------------------------------------------
# Section 6: uniform in 1 <= l <= log n
# ---------------------------------------------------------------------------------------------
def uniform(ell1, c='10', R=R11):
    l1 = I(ell1); c = I(c)
    d = {}
    lc = iv.log(c)
    d['kappa1u'] = k1 = 2 + lc / l1
    d['kappa2'] = k2 = 1 + (1 - iv.log(LOG2) + iv.exp(-l1)) / l1
    d['muu'] = mu = 2 * R * lc / (c - 4 * R)
    d['ratiou'] = ratio = (2 * l1 + lc - 1) / (l1 - mu)
    d['eps1u'] = eps1 = 3 * iv.exp(-l1) / (c * (l1 + lc - 1))
    d['e1u'] = e1 = 4 * c + (2 * c * (lc - 1) + 2 * R / l1 + 6 * iv.exp(-l1) + 1) / l1
    d['eps2u'] = eps2 = e1 * k1 / ((c - 4 * R) * (1 - mu / l1)) * l1 ** 2 * iv.exp(-l1)
    d['kappa3u'] = k3 = c / (c - 4 * R) * ratio * k1 * (1 + eps1) / (1 - eps2)
    d['Ku'] = K = C1_3 * k1 ** 2 * k2 * k3 + k1 / l1 ** 4
    d['phi'] = l1 - 5 * iv.log(l1) - iv.log(K)
    d['side'] = [
        (l1.a >= 10, 'ell1 >= 10'),
        ((c - 4 * R).a > 0, 'c > 4*1.3841'),
        ((l1 - mu).a > 0, 'ell1 > mu_u'),
        (eps2.b < 1, 'eps2_u < 1'),
        ((k3 * l1 ** 2).a >= 0.16, 'kappa3_u * ell1^2 >= 0.16'),
        ((lc - 1).a > 0, 'log c > 1'),
    ]
    return d


# ---------------------------------------------------------------------------------------------
# Remark 7.2: refined inputs (RS (3.3), Robin Thm 13, Matveev's B from (1.3))
# ---------------------------------------------------------------------------------------------
def refined(ell1, l=1, c='10', rho=R13):
    l1 = I(ell1); L_ = I(l); c = I(c)
    d = {}
    d['m'] = m = iv.log(c * L_)
    d['kappa1'] = k1 = 1 + m / l1
    d['kappa2'] = k2 = 1 + (1 - iv.log(LOG2) + iv.exp(-l1)) / l1
    d['mu_r'] = mu = (c * rho + 2 * m - 1) / (c - 2)
    d['ratio_r'] = ratio = (l1 + m - 1) / (l1 - mu)
    d['g'] = g = 1 + (m - I(1) / 2) / l1
    d['eps1'] = eps1 = 3 * iv.exp(-l1) / (c * (l1 + m - 1))
    d['e1_r'] = e1 = 2 * c + (2 * c * (m - 1) + 2 / (l1 - rho) + 6 * iv.exp(-l1) + 1) / l1
    d['eps2_r'] = eps2 = e1 * g / ((c - 2) * (1 - mu / l1)) * l1 ** 2 * iv.exp(-l1)
    d['kappa3_r'] = k3 = c / (c - 2) * ratio * g * (1 + eps1) / (1 - eps2)
    d['dprime'] = dp = 2 * iv.log(l1) + iv.log(k3) - 1 - iv.exp(-l1)
    d['Q'] = Q = (k1 * l1 + C1_3 * k1 ** 2 * k3 * l1 ** 4 * (l1 - dp)) * iv.exp(-l1)
    d['phi'] = -iv.log(Q)   # >= 0 iff Q <= 1
    d['side'] = [
        (l1.a >= 10, 'ell1 >= 10'),
        ((l1 - mu).a > 0, 'ell1 > mu_r'),
        (eps2.b < 1, 'eps2_r < 1'),
        ((l1 - dp).a >= 3, "ell1 - d' >= 3 (Q non-increasing; 1 <= ell - d')"),
        ((k3 * l1 - C1_2 * k2 / C1_3).a >= 0, 'case W1 = W2 dominated: kappa3*ell1 >= C1(2) kappa2 / C1(3)'),
        ((m - 1 + mu).a > 0, 'm - 1 + mu_r > 0'),
    ]
    return d


def search(fun, lo=15.0, hi=80.0, step=0.01, **kw):
    """Smallest grid point ell1 (multiple of step) with certified phi >= 0 and all side conditions.
    Bisection on floats, then certification of the grid point and of failure one step below."""
    def good(x):
        d = fun(f"{x:.2f}", **kw)
        return d['phi'].a >= 0 and all(cnd for cnd, _ in d['side'])
    a, b = lo, hi
    assert good(b) and not good(a)
    while b - a > step / 4:
        mid = (a + b) / 2
        if good(mid):
            b = mid
        else:
            a = mid
    x = round(b / step) * step
    while not good(x):
        x += step
    while good(x - step):
        x -= step
    return f"{x:.2f}", f"{x - step:.2f}"


def report(title, fun, keys, **kw):
    x, below = search(fun, **kw)
    d = fun(x, **kw)
    print(f"\n== {title} ==")
    print(f"  ell1 = {x}   (grid 0.01; ell1 - 0.01 = {below} fails the certificate)")
    for k in keys:
        print(f"  {k:9s} = {s(d[k])}")
    print(f"  phi(ell1) = {s(d['phi'])}")
    ok(d['phi'].a >= 0, 'phi(ell1) >= 0')
    for cnd, lab in d['side']:
        ok(cnd, lab)
    L0 = iv.exp(I(x))
    print(f"  log N = exp(ell1) = {s(L0)}")
    return x, d, L0


# ---------------------------------------------------------------------------------------------
# Direct evaluation of the unsimplified bound (sanity check of the algebra in section 5)
# ---------------------------------------------------------------------------------------------
def G(M):
    return (M + 1) * iv.log(M) - M + 1


def direct_R(ell, l=1, c='10', R=R11):
    """Right-hand side of (4.1), with log Y, T, B* replaced by the bounds of steps S1-S5 of section 5
    (before the kappa simplifications)."""
    ell = I(ell); L = iv.exp(ell); c = I(c); l = I(l)
    y = c * l * L
    Pi = y / iv.log(y)
    Om = l * R * (L + 1) / ell
    F = G(y - l - 1)
    A = Pi - 2 * Om - 2 * F / L
    T = F / (A - 1)
    Bst = (L + 1) / LOG2
    rhs = iv.log(y) + C1_3 * iv.log(y) ** 2 * T * (1 + iv.log(Bst))
    return rhs, L, A, T


def main():
    global ALL_OK
    print("Erdos #889 -- threshold computation (mpmath", __import__('mpmath').__version__,
          ", iv.dps =", iv.dps, ")")
    print("\n== Matveev constants (Cor. 2.3, kappa = 1, D = 1) ==")
    print(f"  C1(3): (3e/2)*30^6*3^3.5 = {s(C1_3a)} ; 2^38 = {s(C1_3b)} ; min = {s(C1_3)}")
    print(f"  C1(2): e*30^5*2^3.5      = {s(C1_2a)} ; 2^32 = {s(C1_2b)} ; min = {s(C1_2)}")
    print(f"  comparison: 1.4*30^6*3^4.5 = {s(I('1.4') * I(30) ** 6 * I(3) ** 4 * iv.sqrt(3))}")
    ok(C1_2.b <= (I('0.16') * C1_3).a, 'C1(2) <= 0.16 * C1(3)  (case W1 = W2 is dominated)')
    print(f"  -log log 2 = {s(-iv.log(LOG2))}")

    keys = ['m', 'kappa1', 'kappa2', 'mu', 'ratio', 'eps1', 'e1', 'eps2', 'kappa3', 'K']
    xA, dA, L0 = report("Theorem A  (l = 1, C0 = 10; RS (3.5), Robin Thm 11, Matveev B*)",
                        fixed_l, keys, l=1)
    print(f"  => Theorem A holds for all n with log log n >= {xA},")
    print(f"     i.e. log n >= {s(L0, 6)}, and on that range log n < K (log log n)^5 fails.")
    print(f"  => N0 := exp(exp({xA})),  log N0 = {s(L0, 4)}")

    BMS = I('1.4') * I(30) ** 6 * I(3) ** 4 * iv.sqrt(3)
    xB, _ = search(fixed_l, l=1, C13=BMS)
    print(f"  (variant) with the simplified constant 1.4*30^6*3^4.5 in place of C1(3): ell1 = {xB}, "
          f"log N0 = {s(iv.exp(I(xB)), 4)}")

    print("\n== Sanity: unsimplified RHS of (4.1) vs K*ell^5 and vs L (direct evaluation) ==")
    K = dA['K']
    for ell in [xA, '46', '50', '60', '100', '1000']:
        rhs, L, A, T = direct_R(ell)
        Kl5 = K * I(ell) ** 5
        print(f"  ell={ell:>7s}: A={s(A, 6)} T={s(T, 6)} RHS={s(rhs, 6)} K ell^5={s(Kl5, 6)} L={s(L, 6)}")
        ok(rhs.b <= Kl5.a, f'RHS <= K ell^5 at ell = {ell}')
        ok(rhs.b < L.a, f'RHS < L at ell = {ell}')
    # informational: where the unsimplified bound itself crosses L
    a, b = 40.0, float(xA)
    for _ in range(60):
        mid = (a + b) / 2
        rhs, L, _, _ = direct_R(f"{mid:.12f}")
        if rhs.b < L.a:
            b = mid
        else:
            a = mid
    print(f"  (info) the unsimplified bound first falls below L near ell = {b:.4f} "
          f"(no monotonicity claimed there; the theorem uses ell1 = {xA})")

    print("\n== Theorem A_l, C0 = 10, per l (same method, fixed l) ==")
    print("   l   ell1(l)   log N(l) = exp(ell1)       K(l)")
    table = []
    for l in range(1, 21):
        x, below = search(fixed_l, l=l)
        d = fixed_l(x, l=l)
        good = d['phi'].a >= 0 and all(cc for cc, _ in d['side'])
        Ll = iv.exp(I(x))
        table.append((l, x, Ll))
        print(f"  {l:2d}   {x}   {s(Ll, 4):28s} {s(d['K'], 4)}  {'OK' if good else 'FAIL'}")
        if not good:
            ALL_OK = False

    keysu = ['kappa1u', 'kappa2', 'muu', 'ratiou', 'eps1u', 'e1u', 'eps2u', 'kappa3u', 'Ku']
    xu, du, Lu = report("Theorem A_unif (all 1 <= l <= log n, C0 = 10)", uniform, keysu)
    print(f"  => for every l >= 1 and every n with log n >= max(exp({xu}), l):")
    print(f"     some k in [l, 10 l log n] has v(n,k) >= 2.   exp({xu}) = {s(Lu, 4)}")

    keysr = ['m', 'kappa1', 'mu_r', 'ratio_r', 'g', 'eps1', 'e1_r', 'eps2_r', 'kappa3_r', 'dprime', 'Q']
    xr, dr, Lr = report("Remark 7.2: refined inputs, l = 1 (RS (3.3), Robin Thm 13, Matveev B of (1.3))",
                        refined, keysr, l=1)
    print(f"  => log N0' = exp({xr}) = {s(Lr, 4)}")

    print("\n== Summary ==")
    print(f"  Theorem A:        log log N0 = {xA}, log N0 = {s(L0, 4)}")
    print(f"  Theorem A_unif:   log log N* = {xu}, log N* = {s(Lu, 4)}")
    print(f"  Remark (refined): log log N0' = {xr}, log N0' = {s(Lr, 4)}")
    print(f"  ALL CHECKS {'PASSED' if ALL_OK else 'FAILED'}")


# ---------------------------------------------------------------------------------------------
# Finite check of Lemma R (evidence only; not used in the proof)
# ---------------------------------------------------------------------------------------------
def check_lemma(N=1000000, ls=(1, 2, 3), YCAP=150):
    from math import lgamma, log
    M = N + 64
    spf = list(range(M + 1))
    for p in range(2, int(M ** 0.5) + 1):
        if spf[p] == p:
            for q in range(p * p, M + 1, p):
                if spf[q] == q:
                    spf[q] = p

    def fac(x):
        f = {}
        while x > 1:
            p = spf[x]
            f[p] = f.get(p, 0) + 1
            x //= p
        return f

    def v(n, k):
        return sum(1 for p in fac(n + k) if p > k)

    primes = [p for p in range(2, 200) if spf[p] == p]
    stats = dict(instances=0, J1ge2=0, fail=0)
    fails = []
    for n in range(3, N + 1):
        for l in ls:
            # largest Y such that v(n,k) <= 1 for all l <= k <= Y
            k = l
            while k <= YCAP and v(n, k) <= 1:
                k += 1
            Ymax = k - 1
            for Y in range(l + 2, Ymax + 1):
                stats['instances'] += 1
                bad = []
                prodfac = {}
                for i in range(l):
                    for p in fac(n + i):
                        prodfac[p] = 1
                Pset = [p for p in primes if p <= Y and p not in prodfac]
                k0 = {}
                for p in Pset:
                    kk = next(t for t in range(l, p + 1) if (n + t) % p == 0)
                    if not (l <= kk <= p - 1):
                        bad.append(('k0 range', p, kk))
                    if max(fac(n + kk)) != p:
                        bad.append(('P(n+k0)!=p', p, kk))
                    k0[p] = kk
                J = sorted(set(k0.values()))
                if len(J) != len(Pset):
                    bad.append(('not injective',))
                if J:
                    a = {j: fac(n + j) for j in J}
                    pr = [p for p in primes if p <= Y]
                    jp = {}
                    for p in pr:
                        best = max(a[j].get(p, 0) for j in J)
                        jp[p] = min(j for j in J if a[j].get(p, 0) == best)
                    W = {}; U = {}; sj = {}
                    for j in J:
                        w = 1; u = 1; cnt = 0
                        for p, e in a[j].items():
                            if p > Y:
                                bad.append(('not Y-smooth', j))
                            if jp[p] == j:
                                u *= p ** e; cnt += 1
                            else:
                                w *= p ** e
                        W[j] = w; U[j] = u; sj[j] = cnt
                    logprodW = sum(log(W[j]) for j in J)
                    logfact = lgamma(Y - l - 1 + 1)
                    if logprodW > logfact + 1e-9:
                        bad.append(('prod W > (Y-l-1)!', logprodW, logfact))
                    J0 = [j for j in J if sj[j] == 0]
                    J1 = [j for j in J if sj[j] == 1]
                    piY = sum(1 for p in primes if p <= Y)
                    om = sum(1 for p in prodfac if p <= Y)
                    if len(J1) < piY - 2 * om - 2 * len(J0):
                        bad.append(('|J1| bound', len(J1), piY, om, len(J0)))
                    if len(J0) > logfact / log(n) + 1e-9:
                        bad.append(('|J0| bound',))
                    qs = [next(iter(fac(U[j]))) for j in J1]
                    if len(set(qs)) != len(qs):
                        bad.append(('q not distinct',))
                    if len(J1) >= 2:
                        stats['J1ge2'] += 1
                        ws = sorted(log(W[j]) for j in J1)
                        if ws[1] > logfact / (len(J1) - 1) + 1e-9:
                            bad.append(('two-smallest bound',))
                if bad:
                    stats['fail'] += 1
                    fails.append((n, l, Y, bad[:2]))
    # exceptions to the conclusion of Theorem A in the finite range (evidence only)
    exc = [n for n in range(2, N + 1)
           if not any(v(n, k) >= 2 for k in range(1, int(10 * log(n)) + 1))]
    print(f"\n== Finite check of Lemma R, 3 <= n <= {N}, l in {ls}, all admissible Y <= {YCAP} ==")
    print(f"  instances (n,l,Y) with v(n,k) <= 1 for all l <= k <= Y and Y >= l+2: {stats['instances']}")
    print(f"  of which |J1| >= 2: {stats['J1ge2']};  failures: {stats['fail']}")
    for f in fails[:10]:
        print('   ', f)
    print(f"  n in [2,{N}] with no k <= 10 log n and v(n,k) >= 2: {len(exc)} values, max {max(exc)}")
    print(f"  {exc}")


if __name__ == '__main__':
    main()
    if '--check' in sys.argv:
        check_lemma()
