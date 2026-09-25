#!/usr/bin/env python3
"""Independent valuation-only checks for the A211417 adversarial review.

This deliberately avoids sympy and avoids constructing factorials.  It checks
divisibility prime by prime using Legendre's formula and trial division.
"""

from math import gcd


def vp_factorial(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def vp_a(n: int, p: int) -> int:
    return (
        vp_factorial(30 * n, p)
        + vp_factorial(n, p)
        - vp_factorial(15 * n, p)
        - vp_factorial(10 * n, p)
        - vp_factorial(6 * n, p)
    )


def factor_into(m: int, exponents: dict[int, int]) -> None:
    m = abs(m)
    p = 2
    while p * p <= m:
        while m % p == 0:
            exponents[p] = exponents.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        exponents[m] = exponents.get(m, 0) + 1


def primes_through(bound: int) -> list[int]:
    answer = []
    for q in range(2, bound + 1):
        if all(q % p for p in answer if p * p <= q):
            answer.append(q)
    return answer


def constant_c(k: int, r: int) -> int:
    m = 30 // k
    indices = [i for i in range(1, r + 1) if gcd(i, k) == 1]
    result = 1
    for p in primes_through(m * r):
        if k % p == 0:
            continue
        exponent = 0
        power = p
        while power <= m * r:
            class_sizes: dict[int, int] = {}
            for i in indices:
                residue = i % power
                class_sizes[residue] = class_sizes.get(residue, 0) + 1
            exponent += max(class_sizes.values())
            power *= p
        result *= p**exponent
    return result


def check_family(k: int, r: int, constant: int, n_max: int) -> None:
    indices = [i for i in range(1, r + 1) if gcd(i, k) == 1]
    constant_factors: dict[int, int] = {}
    factor_into(constant, constant_factors)
    for n in range(n_max + 1):
        product_factors: dict[int, int] = {}
        for i in indices:
            factor_into(k * n + i, product_factors)
        for p, needed in product_factors.items():
            available = constant_factors.get(p, 0) + vp_a(n, p)
            assert available >= needed, (k, r, n, p, needed, available)


def check_d13() -> None:
    indices = [1, 7, 11, 13]
    constant_factors = {7: 1, 11: 1, 13: 1}
    for n in range(51):
        product_factors: dict[int, int] = {}
        for i in indices:
            factor_into(30 * n - i, product_factors)
        for p, needed in product_factors.items():
            available = constant_factors.get(p, 0) + vp_a(n, p)
            assert available >= needed, (n, p, needed, available)


check_d13()
print("independent D(13)=1001 check: n=0..50 OK")

C_3_5 = constant_c(3, 5)
assert C_3_5 == 459117704332740252800
check_family(3, 5, C_3_5, 50)
print(f"independent C(3,5)={C_3_5} check: n=0..50 OK")
