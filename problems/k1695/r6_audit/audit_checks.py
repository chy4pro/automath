#!/usr/bin/env python3
"""Independent integer-population checks for the K1695 round-6 audit."""

from math import comb, prod


def gl(n: int, q: int) -> int:
    return prod(q**n - q**i for i in range(n))


expected_gl = {
    (3, 2): 168,
    (3, 3): 11_232,
    (3, 4): 181_440,
    (3, 5): 1_488_000,
    (4, 2): 20_160,
    (4, 3): 24_261_120,
    (4, 4): 2_961_100_800,
    (5, 2): 9_999_360,
}
for key, expected in expected_gl.items():
    actual = gl(*key)
    assert actual == expected, (key, actual, expected)
    print(f"GL{key}={actual}")

for q, irreducible_quadratics, expected_union in [(2, 1, 112), (3, 3, 12_636)]:
    class_size = gl(4, q) // gl(2, q * q)
    assert class_size * irreducible_quadratics == expected_union
    print(
        f"stratum_b_GF({q}): class={class_size} "
        f"union={class_size * irreducible_quadratics}"
    )

multiset_cells = [
    (5, 2, 2_324_784),
    (4, 3, 32_801_517),
    (3, 2, 330),
    (3, 3, 27_405),
    (3, 4, 766_480),
    (3, 5, 10_668_000),
    (3, 7, 586_862_710),
    (3, 8, 2_896_986_240),
    (3, 9, 11_864_996_235),
]
for m, q, expected in multiset_cells:
    actual = comb(q**m + m, m + 1)
    assert actual == expected, (m, q, actual, expected)
    print(f"T{m}_GF({q})_column_multisets={actual}")

rank1_expected = {
    2: 105,
    3: 2_120,
    4: 16_235,
    5: 77_844,
    7: 822_800,
    8: 2_096_055,
    9: 4_781_420,
}
for q, expected in rank1_expected.items():
    actual = ((q**4 - 1) // (q - 1)) * (q**4 - 1 - q**3)
    assert actual == expected, (q, actual, expected)
    print(f"rank1_GF({q})={actual}")

print("ALL_POPULATION_CHECKS_PASS")
