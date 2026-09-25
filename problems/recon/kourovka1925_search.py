#!/usr/bin/env python3
"""Pure-Python computations for Kourovka Notebook problem 19.25.

The script computes element-order distributions (and hence
T(G)=sum_g phi(ord(g))) for the first small nonabelian simple groups, checks
all 13 groups of order 60, and searches several reproducible families at the
larger orders.  No GAP/Sage or network access is used.
"""

from __future__ import annotations

from collections import Counter, deque
from functools import reduce
from itertools import product
from math import factorial, gcd, lcm


Profile = Counter[int]
Perm = tuple[int, ...]


def phi(n: int) -> int:
    result, x, p = n, n, 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    if x > 1:
        result -= result // x
    return result


def invariant(profile: Profile) -> int:
    return sum(count * phi(order) for order, count in profile.items())


def profile_text(profile: Profile) -> str:
    return " ".join(f"{order}^{profile[order]}" for order in sorted(profile))


def compose(p: Perm, q: Perm) -> Perm:
    """Return p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: Perm) -> Perm:
    ans = [0] * len(p)
    for i, j in enumerate(p):
        ans[j] = i
    return tuple(ans)


def cycle(*xs: int, degree: int) -> Perm:
    p = list(range(degree))
    for a, b in zip(xs, xs[1:] + xs[:1]):
        p[a] = b
    return tuple(p)


def generated_group(generators: list[Perm]) -> list[Perm]:
    degree = len(generators[0])
    identity = tuple(range(degree))
    gens = generators + [inverse(g) for g in generators]
    seen = {identity}
    queue = deque([identity])
    while queue:
        x = queue.popleft()
        for g in gens:
            y = compose(x, g)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return list(seen)


def perm_order(p: Perm) -> int:
    seen = [False] * len(p)
    ans = 1
    for i in range(len(p)):
        if not seen[i]:
            j, length = i, 0
            while not seen[j]:
                seen[j] = True
                length += 1
                j = p[j]
            ans = lcm(ans, length)
    return ans


def perm_profile(generators: list[Perm], expected: int | None = None) -> Profile:
    group = generated_group(generators)
    if expected is not None:
        assert len(group) == expected, (len(group), expected)
    return Counter(perm_order(g) for g in group)


def alternating_profile(n: int) -> Profile:
    gens = [cycle(0, 1, i, degree=n) for i in range(2, n)]
    return perm_profile(gens, factorial(n) // 2)


def symmetric_profile(n: int) -> Profile:
    return perm_profile(
        [cycle(0, 1, degree=n), cycle(*range(n), degree=n)], factorial(n)
    )


def psl2_prime_profile(q: int) -> Profile:
    infinity = q

    def translation(x: int) -> int:
        return infinity if x == infinity else (x + 1) % q

    def inversion(x: int) -> int:
        if x == infinity:
            return 0
        if x == 0:
            return infinity
        return (-pow(x, -1, q)) % q

    t = tuple(translation(x) for x in range(q + 1))
    s = tuple(inversion(x) for x in range(q + 1))
    expected = q * (q * q - 1) // gcd(2, q - 1)
    return perm_profile([t, s], expected)


def gf8_mul(a: int, b: int) -> int:
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011  # x^3+x+1
    return ans


def gf8_pow(a: int, n: int) -> int:
    ans = 1
    while n:
        if n & 1:
            ans = gf8_mul(ans, a)
        a = gf8_mul(a, a)
        n >>= 1
    return ans


def psl2_8_profile() -> Profile:
    infinity = 8
    primitive = 2

    def translation(x: int) -> int:
        return infinity if x == infinity else x ^ 1

    def inversion(x: int) -> int:
        if x == infinity:
            return 0
        if x == 0:
            return infinity
        return gf8_pow(x, 6)

    scalar = gf8_pow(primitive, 2)

    def dilation(x: int) -> int:
        return infinity if x == infinity else gf8_mul(scalar, x)

    gens = [tuple(f(x) for x in range(9)) for f in (translation, inversion, dilation)]
    return perm_profile(gens, 504)


def direct_product_profile(a: Profile, b: Profile) -> Profile:
    ans: Profile = Counter()
    for x, cx in a.items():
        for y, cy in b.items():
            ans[lcm(x, y)] += cx * cy
    return ans


def cyclic_profile(n: int) -> Profile:
    return Counter({d: phi(d) for d in divisors(n)})


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    maximum = n if maximum is None else min(n, maximum)
    for first in range(maximum, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def prime_factors(n: int) -> dict[int, int]:
    ans: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def abelian_p_profile(p: int, part: tuple[int, ...]) -> Profile:
    ans: Profile = Counter({1: 1})
    previous = 1
    for k in range(1, max(part) + 1):
        at_most = p ** sum(min(k, e) for e in part)
        ans[p**k] = at_most - previous
        previous = at_most
    return ans


def abelian_profiles(n: int) -> list[tuple[str, Profile]]:
    choices = []
    for p, exponent in prime_factors(n).items():
        choices.append([(f"{p}:{part}", abelian_p_profile(p, part)) for part in partitions(exponent)])
    ans = []
    for selection in product(*choices):
        name = "Ab(" + ",".join(x[0] for x in selection) + ")"
        profile = reduce(direct_product_profile, (x[1] for x in selection), Counter({1: 1}))
        ans.append((name, profile))
    return ans


def dihedral_profile(n: int) -> Profile:
    """Profile of C_n semidirect C_2 by inversion (order 2n)."""
    ans = cyclic_profile(n)
    ans[2] += n
    return ans


def dicyclic_profile(n: int) -> Profile:
    """Profile of Dic_n of order 4n, <a,x|a^2n=1,x^2=a^n,xax^-1=a^-1>."""
    ans = cyclic_profile(2 * n)
    ans[4] += 2 * n
    return ans


def generalized_dihedral_profile(a: Profile) -> Profile:
    size = sum(a.values())
    ans = a.copy()
    ans[2] += size
    return ans


def semidirect_cyclic_profile(n: int, m: int, r: int) -> Profile:
    """Profile of C_n semidirect C_m, generator of C_m acting by x -> r*x."""
    assert gcd(r, n) == 1 and pow(r, m, n) == 1

    ans: Profile = Counter()
    # For x=(a,b), put k=ord_{C_m}(b).  Then
    # x^k=(a*(1+r^b+...+r^((k-1)b)),0), so
    # ord(x)=k*n/gcd(n,a*S).  Precomputing (k,S) for each b makes a full
    # profile essentially linear in the group order.
    for b in range(m):
        k = m // gcd(b, m)
        rb = pow(r, b, n)
        power = 1
        geometric_sum = 0
        for _ in range(k):
            geometric_sum = (geometric_sum + power) % n
            power = (power * rb) % n
        assert power == 1
        for a in range(n):
            ans[k * n // gcd(n, a * geometric_sum)] += 1
    return ans


def all_semidirect_cyclic_profiles(order: int) -> dict[tuple[tuple[int, int], ...], list[str]]:
    ans: dict[tuple[tuple[int, int], ...], list[str]] = {}
    for n in divisors(order):
        m = order // n
        if n == 1:
            units = [0]
        else:
            units = [r for r in range(1, n) if gcd(r, n) == 1 and pow(r, m, n) == 1]
        for r in units:
            profile = cyclic_profile(m) if n == 1 else semidirect_cyclic_profile(n, m, r)
            key = tuple(sorted(profile.items()))
            ans.setdefault(key, []).append(f"C{n}:C{m}[r={r}]")
    return ans


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def matrix_multiply(a: Matrix, b: Matrix, p: int) -> Matrix:
    k = len(a)
    return tuple(
        tuple(sum(a[i][t] * b[t][j] for t in range(k)) % p for j in range(k))
        for i in range(k)
    )


def matrix_vector(a: Matrix, v: Vector, p: int) -> Vector:
    return tuple(sum(row[j] * v[j] for j in range(len(v))) % p for row in a)


def matrix_add(a: Matrix, b: Matrix, p: int) -> Matrix:
    return tuple(
        tuple((x + y) % p for x, y in zip(row_a, row_b))
        for row_a, row_b in zip(a, b)
    )


def matrix_power(a: Matrix, n: int, p: int) -> Matrix:
    k = len(a)
    ans: Matrix = tuple(tuple(int(i == j) for j in range(k)) for i in range(k))
    while n:
        if n & 1:
            ans = matrix_multiply(ans, a, p)
        a = matrix_multiply(a, a, p)
        n >>= 1
    return ans


def matrix_power_sum(a: Matrix, n: int, p: int) -> tuple[Matrix, Matrix]:
    """Return (a^n, I+a+...+a^(n-1)) by binary powering."""
    k = len(a)
    identity: Matrix = tuple(tuple(int(i == j) for j in range(k)) for i in range(k))
    zero: Matrix = tuple(tuple(0 for _ in range(k)) for _ in range(k))
    result_power, result_sum = identity, zero
    block_power, block_sum = a, identity
    while n:
        if n & 1:
            result_sum = matrix_add(
                result_sum, matrix_multiply(result_power, block_sum, p), p
            )
            result_power = matrix_multiply(result_power, block_power, p)
        block_sum = matrix_add(
            block_sum, matrix_multiply(block_power, block_sum, p), p
        )
        block_power = matrix_multiply(block_power, block_power, p)
        n >>= 1
    return result_power, result_sum


def matrix_rank(a: Matrix, p: int) -> int:
    rows = [list(row) for row in a]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][col], -1, p)
        rows[rank] = [(x * scale) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % p:
                scale = rows[i][col]
                rows[i] = [(x - scale * y) % p for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def elementary_abelian_cyclic_profile(p: int, k: int, m: int, a: Matrix) -> Profile:
    """Profile of (F_p)^k semidirect C_m with generator acting as a."""
    identity: Matrix = tuple(tuple(int(i == j) for j in range(k)) for i in range(k))
    zero = (0,) * k
    vectors = list(product(range(p), repeat=k))
    powers = [identity]
    for _ in range(1, m):
        powers.append(matrix_multiply(powers[-1], a, p))

    ans: Profile = Counter()
    for b in range(m):
        complement_order = m // gcd(b, m)
        ab = powers[b]
        power, geometric = matrix_power_sum(ab, complement_order, p)
        assert power == identity
        for v in vectors:
            residual = matrix_vector(geometric, v, p)
            ans[complement_order * (1 if residual == zero else p)] += 1
    return ans


def elementary_abelian_cyclic_profiles(
    order: int,
) -> tuple[int, dict[tuple[tuple[int, int], ...], list[str]]]:
    """Enumerate raw matrix actions (F_p)^k : C_m for 2 <= k <= 4."""
    raw_actions = 0
    ans: dict[tuple[tuple[int, int], ...], list[str]] = {}
    for p, exponent in prime_factors(order).items():
        for k in range(2, min(exponent, 4) + 1):
            normal_order = p**k
            m = order // normal_order
            identity: Matrix = tuple(tuple(int(i == j) for j in range(k)) for i in range(k))
            for entries in product(range(p), repeat=k * k):
                a: Matrix = tuple(tuple(entries[i * k + j] for j in range(k)) for i in range(k))
                if matrix_rank(a, p) != k or matrix_power(a, m, p) != identity:
                    continue
                raw_actions += 1
                profile = elementary_abelian_cyclic_profile(p, k, m, a)
                key = tuple(sorted(profile.items()))
                ans.setdefault(key, []).append(f"(C{p})^{k}:C{m}")
    return raw_actions, ans


def brute_profile(elements, identity, multiply) -> Profile:
    ans: Profile = Counter()
    bound = len(elements)
    for x in elements:
        y = identity
        for element_order in range(1, bound + 1):
            y = multiply(y, x)
            if y == identity:
                ans[element_order] += 1
                break
        else:
            raise AssertionError(x)
    return ans


def self_test() -> None:
    """Independent small-case checks of both semidirect order formulas."""
    for n, m, r in [(5, 4, 2), (3, 4, 2), (7, 3, 2)]:
        elements = list(product(range(n), range(m)))

        def multiply(x, y):
            return ((x[0] + pow(r, x[1], n) * y[0]) % n, (x[1] + y[1]) % m)

        brute = brute_profile(elements, (0, 0), multiply)
        assert brute == semidirect_cyclic_profile(n, m, r)

    p, k, m = 2, 2, 3
    a: Matrix = ((0, 1), (1, 1))
    vectors = list(product(range(p), repeat=k))
    powers = [matrix_power(a, b, p) for b in range(m)]
    elements = list(product(vectors, range(m)))

    def add_vectors(v, w):
        return tuple((x + y) % p for x, y in zip(v, w))

    def multiply_affine(x, y):
        return (add_vectors(x[0], matrix_vector(powers[x[1]], y[0], p)), (x[1] + y[1]) % m)

    brute = brute_profile(elements, ((0, 0), 0), multiply_affine)
    assert brute == elementary_abelian_cyclic_profile(p, k, m, a)

    # This divisibility is also an audit of the cyclic-subgroup reformulation:
    # elements of order d split into phi(d)-element generator sets.
    for _, _, profile in simple_profiles():
        assert all(count % phi(d) == 0 for d, count in profile.items())


# Small complement models for the complete order-60 check.
def s3_elements() -> list[Perm]:
    return generated_group([cycle(0, 1, degree=3), cycle(0, 1, 2, degree=3)])


def a4_elements() -> list[Perm]:
    return generated_group([cycle(0, 1, 2, degree=4), cycle(0, 1, 3, degree=4)])


def permutation_sign(p: Perm) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


def order60_semidirect_profile(kind: str, action: str) -> Profile:
    """Profile of C5 semidirect K for one of the five groups K of order 12."""
    if kind == "C12":
        elements = list(range(12))
        identity = 0
        multiply_k = lambda x, y: (x + y) % 12
        exponent = lambda x: x
    elif kind == "C6xC2":
        elements = list(product(range(6), range(2)))
        identity = (0, 0)
        multiply_k = lambda x, y: ((x[0] + y[0]) % 6, (x[1] + y[1]) % 2)
        exponent = lambda x: x[1]
    elif kind == "S3xC2":
        ss = s3_elements()
        elements = list(product(ss, range(2)))
        identity = (tuple(range(3)), 0)
        multiply_k = lambda x, y: (compose(x[0], y[0]), (x[1] + y[1]) % 2)
        if action == "sign":
            exponent = lambda x: 0 if permutation_sign(x[0]) == 1 else 1
        else:
            exponent = lambda x: x[1]
    elif kind == "A4":
        elements = a4_elements()
        identity = tuple(range(4))
        multiply_k = compose
        exponent = lambda x: 0
    elif kind == "Dic3":
        elements = list(product(range(3), range(4)))
        identity = (0, 0)
        multiply_k = lambda x, y: ((x[0] + (-1 if x[1] % 2 else 1) * y[0]) % 3, (x[1] + y[1]) % 4)
        exponent = lambda x: x[1]
    else:
        raise ValueError(kind)

    r = {"trivial": 1, "involution": 4, "faithful": 2, "sign": 4, "central": 4}[action]

    def chi(k) -> int:
        return pow(r, exponent(k), 5)

    def multiply(x, y):
        a, k = x
        b, ell = y
        return ((a + chi(k) * b) % 5, multiply_k(k, ell))

    ans: Profile = Counter()
    group_identity = (0, identity)
    for x in product(range(5), elements):
        y = group_identity
        for order in range(1, 61):
            y = multiply(y, x)
            if y == group_identity:
                ans[order] += 1
                break
        else:
            raise AssertionError((kind, action, x))
    assert sum(ans.values()) == 60
    return ans


ORDER60_CASES = [
    ("C5 x C12 = C60", "C12", "trivial"),
    ("C5 : C12 (image C2)", "C12", "involution"),
    ("C5 : C12 (image C4)", "C12", "faithful"),
    ("C5 x (C6 x C2) = C30 x C2", "C6xC2", "trivial"),
    ("C5 : (C6 x C2) (nonzero C2-character)", "C6xC2", "involution"),
    ("C5 x (S3 x C2)", "S3xC2", "trivial"),
    ("C5 : (S3 x C2) (S3-sign action)", "S3xC2", "sign"),
    ("C5 : (S3 x C2) (central-C2 action)", "S3xC2", "central"),
    ("C5 x A4", "A4", "trivial"),
    ("C5 x Dic3", "Dic3", "trivial"),
    ("C5 : Dic3 (image C2)", "Dic3", "involution"),
    ("C5 : Dic3 (image C4)", "Dic3", "faithful"),
]


def simple_profiles() -> list[tuple[str, int, Profile]]:
    return [
        ("A5", 60, alternating_profile(5)),
        ("PSL(2,7)", 168, psl2_prime_profile(7)),
        ("A6 = PSL(2,9)", 360, alternating_profile(6)),
        ("PSL(2,8)", 504, psl2_8_profile()),
        ("PSL(2,11)", 660, psl2_prime_profile(11)),
        ("PSL(2,13)", 1092, psl2_prime_profile(13)),
        ("PSL(2,17)", 2448, psl2_prime_profile(17)),
        ("A7", 2520, alternating_profile(7)),
    ]


def named_factor_profiles(max_order: int) -> dict[int, list[tuple[str, Profile]]]:
    ans: dict[int, list[tuple[str, Profile]]] = {}

    def add(order: int, name: str, profile: Profile):
        if order <= max_order:
            ans.setdefault(order, []).append((name, profile))

    for n in range(1, max_order + 1):
        if max_order % n == 0:
            add(n, f"C{n}", cyclic_profile(n))
            for name, profile in abelian_profiles(n):
                add(n, name, profile)
    for order in divisors(max_order):
        if order >= 6 and order % 2 == 0:
            add(order, f"Dih(C{order // 2})", dihedral_profile(order // 2))
        if order >= 8 and order % 4 == 0:
            add(order, f"Dic_{order // 4}", dicyclic_profile(order // 4))
    for n in range(4, 8):
        order = factorial(n) // 2
        if max_order % order == 0:
            add(order, f"A{n}", alternating_profile(n))
    for n in range(3, 6):
        order = factorial(n)
        if max_order % order == 0:
            add(order, f"S{n}", symmetric_profile(n))
    return ans


def search_families(order: int, target: int) -> dict[str, object]:
    hits: list[str] = []
    examples_by_t: dict[int, str] = {}
    profile_keys: set[tuple[tuple[int, int], ...]] = set()
    candidate_entries = 0

    def inspect(name: str, profile: Profile):
        nonlocal candidate_entries
        candidate_entries += 1
        profile_keys.add(tuple(sorted(profile.items())))
        value = invariant(profile)
        examples_by_t.setdefault(value, name)
        if value == target:
            hits.append(name)

    abs_for_half = abelian_profiles(order // 2) if order % 2 == 0 else []
    for name, profile in abelian_profiles(order):
        inspect(name, profile)
    for name, profile in abs_for_half:
        inspect(f"Dih({name})", generalized_dihedral_profile(profile))
    cyclic_semidirects = all_semidirect_cyclic_profiles(order)
    for key, names in cyclic_semidirects.items():
        inspect(f"{names[0]} ({len(names)} action descriptions share this profile)", Counter(dict(key)))
    elementary_raw, elementary_semidirects = elementary_abelian_cyclic_profiles(order)
    for key, names in elementary_semidirects.items():
        labels = sorted(set(names))
        inspect(f"{labels[0]} ({len(names)} matrices share this profile)", Counter(dict(key)))

    factors = named_factor_profiles(order)
    direct_products = 0
    for a in divisors(order):
        b = order // a
        # Exclude identity factors: these merely reproduce a listed group,
        # including the target simple group itself.
        if a == 1 or b == 1 or a > b or a not in factors or b not in factors:
            continue
        for name_a, profile_a in factors[a]:
            for name_b, profile_b in factors[b]:
                direct_products += 1
                inspect(f"{name_a} x {name_b}", direct_product_profile(profile_a, profile_b))

    below = max((value for value in examples_by_t if value < target), default=None)
    above = min((value for value in examples_by_t if value > target), default=None)
    return {
        "candidate_profile_entries": candidate_entries,
        "distinct_profiles": len(profile_keys),
        "cyclic_semidirect_constructions": sum(len(v) for v in cyclic_semidirects.values()),
        "cyclic_semidirect_profiles": len(cyclic_semidirects),
        "elementary_abelian_cyclic_matrix_actions": elementary_raw,
        "elementary_abelian_cyclic_profiles": len(elementary_semidirects),
        "abelian": len(abelian_profiles(order)),
        "generalized_dihedral": len(abs_for_half),
        "named_direct_products": direct_products,
        "nearest_below": None if below is None else (below, examples_by_t[below]),
        "nearest_above": None if above is None else (above, examples_by_t[above]),
        "hits": sorted(set(hits)),
    }


def main() -> None:
    self_test()
    print("SELF-CHECKS PASSED")
    simples = simple_profiles()
    print("SIMPLE GROUPS")
    for name, order, profile in simples:
        print(f"{name:16} |G|={order:4} T={invariant(profile):5} profile={profile_text(profile)}")

    print("\nALL GROUPS OF ORDER 60")
    a5_t = invariant(simples[0][2])
    profiles = set()
    for name, kind, action in ORDER60_CASES:
        profile = order60_semidirect_profile(kind, action)
        profiles.add(tuple(sorted(profile.items())))
        print(f"{name:52} T={invariant(profile):4} profile={profile_text(profile)}")
    print(f"A5{'':50} T={a5_t:4} profile={profile_text(simples[0][2])}")
    profiles.add(tuple(sorted(simples[0][2].items())))
    print(f"distinct order profiles among 13 groups: {len(profiles)}")

    print("\nLARGER-ORDER FAMILY SEARCH")
    for name, order, profile in simples[1:]:
        result = search_families(order, invariant(profile))
        print(f"{name:16} order={order:4} target={invariant(profile):5} {result}")


if __name__ == "__main__":
    main()
