#!/usr/bin/env python3
"""
Independent checker for witness.csv (Erdos #889 mechanical computation).

Deliberately shares NO code with gen_witness.py: no SPF sieve, no numpy, no
imported helper functions from the generator. Everything here is plain
Python trial division, re-derived from scratch, so a bug in the generator's
vectorized SPF-peeling logic would not be replicated here.

For every row (n, k, p1, p2) of witness.csv this checks, purely by trial
division:
  (A) p1 and p2 are primes, p1 < p2, p1 > k, p2 > k, and p1 | (n+k), p2 | (n+k).
      I.e. (p1, p2) really is a valid witness that v(n, k) >= 2.
  (B) minimality: for every k' with 1 <= k' < k, v(n, k') < 2, i.e. (n+k')
      has at most one distinct prime factor exceeding k'. This re-derives
      that k is truly the SMALLEST k with v(n,k) >= 2 (which is exactly what
      witness.csv claims for these n, since it only lists n whose smallest
      such k exceeds 10), not merely that k works.

Prints PASS/FAIL counts and exits non-zero if anything fails.
"""
import csv
import sys
import time


def is_prime(x):
    """Plain trial division primality test."""
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def distinct_primes_above(m, k):
    """Trial-division factorization of m; return the sorted list of DISTINCT
    prime factors of m that are > k."""
    factors = []
    x = m
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        factors.append(x)
    return [p for p in factors if p > k]


def check_row(n, k, p1, p2):
    """Return (ok, reason_if_fail) for one witness.csv row."""
    m = n + k

    # --- (A) the claimed witness itself ---
    if not (p1 < p2):
        return False, f"p1={p1} is not < p2={p2}"
    if not (p1 > k and p2 > k):
        return False, f"p1={p1} or p2={p2} not > k={k}"
    if m % p1 != 0 or m % p2 != 0:
        return False, f"p1={p1} or p2={p2} does not divide n+k={m}"
    if not is_prime(p1):
        return False, f"p1={p1} is not prime"
    if not is_prime(p2):
        return False, f"p2={p2} is not prime"
    big_factors = distinct_primes_above(m, k)
    if len(big_factors) < 2:
        return False, f"trial division finds only {big_factors} distinct prime factors of n+k={m} exceeding k={k}"
    if {p1, p2} - set(big_factors):
        return False, f"p1,p2={p1},{p2} not among trial-division's big factors {big_factors} of n+k={m}"

    # --- (B) minimality: no smaller k' works ---
    for kp in range(1, k):
        mp = n + kp
        big = distinct_primes_above(mp, kp)
        if len(big) >= 2:
            return False, f"k'={kp} < k={k} already has v(n,k')>=2 via primes {big[:2]} of n+k'={mp}; k={k} is not minimal"

    return True, None


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "witness.csv"
    t0 = time.time()
    n_pass = 0
    n_fail = 0
    fails = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            n = int(row["n"])
            k = int(row["k"])
            p1 = int(row["p1"])
            p2 = int(row["p2"])
            ok, reason = check_row(n, k, p1, p2)
            if ok:
                n_pass += 1
            else:
                n_fail += 1
                fails.append((n, k, p1, p2, reason))

    elapsed = time.time() - t0
    print(f"check_witness.py: checked {n_pass + n_fail} rows from {csv_path}")
    print(f"PASS={n_pass} FAIL={n_fail}")
    print(f"elapsed={elapsed:.3f}s")
    if fails:
        print("First failures:")
        for n, k, p1, p2, reason in fails[:20]:
            print(f"  n={n} k={k} p1={p1} p2={p2}: {reason}")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
