"""DSS verification and window / boundary statistics on explicit DSS sets.

For a set A (sorted), with X(eps) = sum eps_i a_i (eps in {-1,+1}^n):
  occX   = #{X in (-a_n, a_n)} / (#lattice points of s+2Z in that open window)
  Y-count= #{Y in (-2a_n,0)}, Y = sums of A minus a_n           (fold: a_n >= 2*this)
  dB'    = inner vertex boundary of {Y<0} in Q_{n-1}            (Harper: >= beta(n-1))
  dB     = inner vertex boundary of {X<0} in Q_n                (Harper: >= beta(n))
  rho    = sum a_i^2 / (n a_n^2)
"""
import sys
from math import comb
import numpy as np

def beta(m):
    return comb(m, m // 2)

def conway_guy_set(n):
    u = [0, 1]
    for k in range(1, n):
        r = int(round((2 * k) ** 0.5))
        u.append(2 * u[k] - u[k - r])
    return sorted(u[n] - u[i] for i in range(n))

def all_pm_sums(a):
    """X for all eps; bit i of index = 1 means eps_i=+1 (a sorted ascending)."""
    X = np.zeros(1, dtype=np.int64)
    for ai in a:
        X = np.concatenate([X - ai, X + ai])  # new top bit: 0 -> -ai, 1 -> +ai
    return X

def is_dss(a):
    # numpy boolean bitset of 0/1 subset sums
    tot = sum(a)
    S = np.zeros(tot + 1, dtype=bool)
    S[0] = True
    hi = 0
    for ai in a:
        if np.any(S[: hi + 1] & S[ai: ai + hi + 1]):
            return False
        S[ai: ai + hi + 1] |= S[: hi + 1]
        hi += ai
    return True

def inner_boundary(X, a):
    """#{eps: X<0 and exists i with eps_i=-1, X+2a_i>0}.  Since a sorted, the best flip is the
    largest index i with eps_i=-1."""
    n = len(a)
    N = X.size
    idx = np.arange(N, dtype=np.int64)
    # m(eps) = a_j for j = highest index with bit 0
    mval = np.zeros(N, dtype=np.int64)
    found = np.zeros(N, dtype=bool)
    for j in range(n - 1, -1, -1):
        bit0 = ((idx >> j) & 1) == 0
        sel = bit0 & ~found
        mval[sel] = a[j]
        found |= bit0
    neg = X < 0
    return int(np.count_nonzero(neg & found & (X + 2 * mval > 0)))

def lattice_count_open(lo, hi, s):
    # number of integers x == s (mod 2) with lo < x < hi
    import math
    first = lo + 1
    if (first - s) % 2:
        first += 1
    last = hi - 1
    if (last - s) % 2:
        last -= 1
    return max(0, (last - first) // 2 + 1)

def stats(a, name):
    a = sorted(a)
    n = len(a)
    an = a[-1]
    assert is_dss(a), name
    X = all_pm_sums(a)
    Y = all_pm_sums(a[:-1])
    s = sum(a) % 2
    occ = np.count_nonzero((X > -an) & (X < an))
    lat = lattice_count_open(-an, an, s)
    ycnt = int(np.count_nonzero((Y > -2 * an) & (Y < 0)))
    dBp = inner_boundary(Y, a[:-1])
    dB = inner_boundary(X, a)
    rho = sum(x * x for x in a) / (n * an * an)
    sig = np.sqrt(sum(x * x for x in a))
    # central density: fraction of lattice points in (-L, L) occupied, L = 4 a_n (or less)
    L = min(4 * an, int(sig))
    occL = np.count_nonzero((X > -L) & (X < L)) / lattice_count_open(-L, L, s)
    print(f"{name:>10} n={n:2d} a_n={an:9d}  a_n/b(n)={an/beta(n):6.3f}  a_n/2b(n-1)={an/(2*beta(n-1)):6.3f} "
          f"rho={rho:5.3f} occ(-a_n,a_n)={occ/lat:5.3f} occ(-4a_n,4a_n)={occL:5.3f} "
          f"Ycnt/b(n-1)={ycnt/beta(n-1):6.3f} dB'/b(n-1)={dBp/beta(n-1):6.3f} dB/b(n)={dB/beta(n):6.3f} "
          f"fold-check {an}>={2*ycnt}:{an >= 2*ycnt}")
    assert occ == 2 * ycnt
    assert ycnt >= dBp >= beta(n - 1)
    assert dB >= beta(n)
    return dict(n=n, an=an)

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    for n in range(2, nmax + 1):
        stats(conway_guy_set(n), "CG")
    for n in [8, 12, 16]:
        stats([2 ** i for i in range(n)], "pow2")
    # a 'near-equal' DSS family: {2^n - 2^i}? check DSS-ness first
    for n in [6, 10, 14]:
        a = sorted(2 ** n - 2 ** i for i in range(n))
        if is_dss(a):
            stats(a, "2^n-2^i")
        else:
            print("2^n-2^i not DSS for n=", n)
