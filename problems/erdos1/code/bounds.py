"""Bounds table for the distinct-subset-sums problem (clean-room probe).

All quantities normalised by 2^n / sqrt(n).  Exact rationals/integers where possible,
mpmath for integrals.
"""
from math import comb, isqrt
import mpmath as mp

mp.mp.dps = 40

def beta(m):
    return comb(m, m // 2) if m >= 0 else 0

def conway_guy(nmax):
    # u_0=0, u_1=1, u_{k+1} = 2 u_k - u_{k-r}, r = round(sqrt(2k))
    u = [0, 1]
    for k in range(1, nmax):
        r = int(mp.nint(mp.sqrt(2 * k)))
        u.append(2 * u[k] - u[k - r])
    return u

def lemmaF(n, rho=1):
    # 2^{n-1} * int_{-1}^{1} (1-|s|) cos(pi s/2)^{rho n} ds
    f = lambda s: (1 - s) * mp.cos(mp.pi * s / 2) ** (rho * n)
    return mp.mpf(2) ** (n - 1) * 2 * mp.quad(f, [0, mp.mpf(1) / mp.sqrt(n), 1])

def fourier_ideal(n):
    f = lambda s: mp.cos(mp.pi * s / 2) ** n
    return mp.mpf(2) ** (n - 1) * 2 * mp.quad(f, [0, mp.mpf(1) / mp.sqrt(n), 1])

def main():
    c = mp.sqrt(2 / mp.pi)
    u = conway_guy(80)
    print("n | true/CG a_n | var | E|X| | Harper b(n) | fold 2b(n-1) | Fourier ideal | LemmaF(rho=1)   [all / (2^n/sqrt n)]")
    for n in list(range(2, 13)) + [20, 21, 40, 41, 60, 61, 79]:
        norm = mp.mpf(2) ** n / mp.sqrt(n)
        cg = u[n]  # max of CG set {u_n - u_i}
        var = mp.sqrt((mp.mpf(4) ** n - 1) / (3 * n))
        eabs = mp.mpf(4) ** (n - 1) / (n * beta(n - 1))
        h = beta(n)
        fo = 2 * beta(n - 1)
        fi = fourier_ideal(n)
        lf = lemmaF(n)
        print(f"{n:3d} {mp.nstr(cg/norm,6):>9} {mp.nstr(var/norm,6):>8} {mp.nstr(eabs/norm,6):>8} "
              f"{mp.nstr(h/norm,6):>8} {mp.nstr(fo/norm,6):>8} {mp.nstr(fi/norm,6):>8} {mp.nstr(lf/norm,6):>8}")
    print()
    print("second-order coefficients  n*(bound/(c 2^n/sqrt n) - 1):")
    for n in [1000, 1001, 4000, 4001, 20000, 20001]:
        norm = c * mp.mpf(2) ** n / mp.sqrt(n)
        h = mp.mpf(beta(n)) / norm
        fo = mp.mpf(2 * beta(n - 1)) / norm
        print(n, "Harper:", mp.nstr(n * (h - 1), 8), " fold:", mp.nstr(n * (fo - 1), 8))
    print()
    print("check identity 2^{n-1} int_{-1}^1 cos^n(pi s/2) ds == beta(n) for even n:")
    for n in [2, 4, 10, 30, 31]:
        print(n, mp.nstr(fourier_ideal(n), 20), beta(n), 2 * beta(n - 1))
    print()
    print("Lemma F with rho<1 (n=200): bound/(c 2^n/sqrt(n)) vs 1/sqrt(rho)")
    n = 200
    norm = c * mp.mpf(2) ** n / mp.sqrt(n)
    for rho in [1, 0.9, 0.8, 0.5]:
        print(rho, mp.nstr(lemmaF(n, rho) / norm, 8), mp.nstr(1 / mp.sqrt(rho), 8))
    print()
    print("Is beta(n) >= c 2^n n^{-1/2} (1 - 1/(4n)) for even n, and 2beta(n-1) >= c 2^n n^{-1/2}(1+1/(4n)) - ? for odd n")
    bad_even = [n for n in range(2, 3001, 2) if mp.mpf(beta(n)) < c * mp.mpf(2) ** n / mp.sqrt(n) * (1 - mp.mpf(1) / (4 * n))]
    print("even n in [2,3000] violating (1-1/(4n)):", bad_even[:10])
    bad_odd = [n for n in range(3, 3001, 2) if mp.mpf(2 * beta(n - 1)) < c * mp.mpf(2) ** n / mp.sqrt(n) * (1 - mp.mpf(1) / (4 * n))]
    print("odd n in [3,3000] violating 2b(n-1) >= (1-1/(4n)) c 2^n/sqrt n:", bad_odd[:10])
    bad_odd2 = [n for n in range(3, 3001, 2) if mp.mpf(2 * beta(n - 1)) < c * mp.mpf(2) ** n / mp.sqrt(n)]
    print("odd n in [3,3000] violating 2b(n-1) >= c 2^n/sqrt n:", bad_odd2[:10])

if __name__ == "__main__":
    main()
