#!/usr/bin/env python3
"""Independent exact checker for the K5-GFQ clean-placement criterion."""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Iterator, Sequence


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def prime_power(value: int) -> tuple[int, int]:
    for prime in range(2, value + 1):
        if not is_prime(prime):
            continue
        remaining = value
        degree = 0
        while remaining % prime == 0:
            remaining //= prime
            degree += 1
        if remaining == 1 and degree:
            return prime, degree
    raise ValueError(f"{value} is not a prime power")


def trim_prime(poly: Sequence[int], prime: int) -> list[int]:
    result = [coefficient % prime for coefficient in poly]
    while result and result[-1] == 0:
        result.pop()
    return result


def prime_remainder(dividend: Sequence[int], divisor: Sequence[int], prime: int) -> list[int]:
    work = trim_prime(dividend, prime)
    base = trim_prime(divisor, prime)
    if not base:
        raise ZeroDivisionError
    inverse = pow(base[-1], prime - 2, prime)
    while len(work) >= len(base):
        shift = len(work) - len(base)
        scale = work[-1] * inverse % prime
        for index, coefficient in enumerate(base):
            work[shift + index] = (work[shift + index] - scale * coefficient) % prime
        work = trim_prime(work, prime)
    return work


def irreducible_by_trial(poly: Sequence[int], prime: int) -> bool:
    degree = len(poly) - 1
    for divisor_degree in range(1, degree // 2 + 1):
        for coefficients in itertools.product(range(prime), repeat=divisor_degree):
            if coefficients[0] == 0:
                continue
            divisor = list(coefficients) + [1]
            if not prime_remainder(poly, divisor, prime):
                return False
    return True


def first_irreducible(prime: int, degree: int) -> list[int]:
    if degree == 1:
        return [0, 1]
    for coefficients in itertools.product(range(prime), repeat=degree):
        if coefficients[0] == 0:
            continue
        candidate = list(coefficients) + [1]
        if irreducible_by_trial(candidate, prime):
            return candidate
    raise RuntimeError(f"no irreducible polynomial of degree {degree} over GF({prime})")


class Field:
    """A small GF(p^d) using an independently constructed polynomial basis."""

    def __init__(self, order: int):
        self.order = order
        self.prime, self.degree = prime_power(order)
        self.modulus = first_irreducible(self.prime, self.degree)
        self.digits = [self.decode(value) for value in range(order)]
        self.addition = [[0] * order for _ in range(order)]
        self.multiplication = [[0] * order for _ in range(order)]
        for left in range(order):
            for right in range(order):
                self.addition[left][right] = self.encode(
                    [
                        (self.digits[left][index] + self.digits[right][index]) % self.prime
                        for index in range(self.degree)
                    ]
                )
                self.multiplication[left][right] = self.multiply_digits(
                    self.digits[left], self.digits[right]
                )
        self.negatives = [
            self.encode([(-digit) % self.prime for digit in self.digits[value]])
            for value in range(order)
        ]
        self.inverses = [0] * order
        for value in range(1, order):
            candidates = [other for other in range(1, order) if self.mul(value, other) == 1]
            if len(candidates) != 1:
                raise AssertionError(f"element {value} has {len(candidates)} inverses")
            self.inverses[value] = candidates[0]

    def decode(self, value: int) -> list[int]:
        digits = []
        for _ in range(self.degree):
            digits.append(value % self.prime)
            value //= self.prime
        return digits

    def encode(self, digits: Sequence[int]) -> int:
        result = 0
        place = 1
        for index in range(self.degree):
            result += (digits[index] % self.prime) * place
            place *= self.prime
        return result

    def multiply_digits(self, left: Sequence[int], right: Sequence[int]) -> int:
        if self.degree == 1:
            return left[0] * right[0] % self.prime
        product = [0] * (2 * self.degree - 1)
        for i, first in enumerate(left):
            for j, second in enumerate(right):
                product[i + j] = (product[i + j] + first * second) % self.prime
        for power in range(len(product) - 1, self.degree - 1, -1):
            leading = product[power]
            if leading:
                for index in range(self.degree):
                    target = power - self.degree + index
                    product[target] = (
                        product[target] - leading * self.modulus[index]
                    ) % self.prime
        return self.encode(product[: self.degree])

    def add(self, left: int, right: int) -> int:
        return self.addition[left][right]

    def sub(self, left: int, right: int) -> int:
        return self.addition[left][self.negatives[right]]

    def mul(self, left: int, right: int) -> int:
        return self.multiplication[left][right]

    def inv(self, value: int) -> int:
        if value == 0:
            raise ZeroDivisionError
        return self.inverses[value]

    def scalar(self, count: int, value: int) -> int:
        result = 0
        for _ in range(count):
            result = self.add(result, value)
        return result

    def self_check(self) -> None:
        for first in range(self.order):
            assert self.add(first, 0) == first
            assert self.add(first, self.negatives[first]) == 0
            assert self.mul(first, 0) == 0
            assert self.mul(first, 1) == first
            if first:
                assert self.mul(first, self.inv(first)) == 1
            for second in range(self.order):
                assert self.add(first, second) == self.add(second, first)
                assert self.mul(first, second) == self.mul(second, first)
                for third in range(self.order):
                    assert self.add(self.add(first, second), third) == self.add(
                        first, self.add(second, third)
                    )
                    assert self.mul(self.mul(first, second), third) == self.mul(
                        first, self.mul(second, third)
                    )
                    assert self.mul(first, self.add(second, third)) == self.add(
                        self.mul(first, second), self.mul(first, third)
                    )


def trim(poly: Sequence[int]) -> list[int]:
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return result


def polynomial_remainder(
    dividend: Sequence[int], divisor: Sequence[int], field: Field
) -> list[int]:
    work = trim(dividend)
    base = trim(divisor)
    if not base:
        raise ZeroDivisionError
    leading_inverse = field.inv(base[-1])
    while len(work) >= len(base):
        shift = len(work) - len(base)
        scale = field.mul(work[-1], leading_inverse)
        for index, coefficient in enumerate(base):
            target = shift + index
            work[target] = field.sub(work[target], field.mul(scale, coefficient))
        work = trim(work)
    return work


def polynomial_gcd(left: Sequence[int], right: Sequence[int], field: Field) -> list[int]:
    first = trim(left)
    second = trim(right)
    while second:
        first, second = second, polynomial_remainder(first, second, field)
    if first:
        inverse = field.inv(first[-1])
        first = [field.mul(coefficient, inverse) for coefficient in first]
    return trim(first)


def prime_free_part(n: int, prime: int) -> tuple[int, int]:
    m = n
    capacity = 1
    while m % prime == 0:
        m //= prime
        capacity *= prime
    return m, capacity


def residue_profile(
    field: Field, n: int, coefficients: Sequence[int], positions: Sequence[int]
) -> list[int]:
    if len(coefficients) != len(positions):
        raise ValueError("coefficient and position lengths differ")
    if len(set(positions)) != len(positions):
        raise ValueError("positions are not distinct")
    if any(position < 0 or position >= n for position in positions):
        raise ValueError("position outside Z_n")
    if any(coefficient <= 0 or coefficient >= field.order for coefficient in coefficients):
        raise ValueError("coefficient is not a nonzero encoded field element")
    m, _ = prime_free_part(n, field.prime)
    profile = [0] * m
    for coefficient, position in zip(coefficients, positions):
        residue = position % m
        profile[residue] = field.add(profile[residue], coefficient)
    return profile


def profile_is_clean(field: Field, profile: Sequence[int]) -> tuple[bool, list[int]]:
    m = len(profile)
    if m == 1:
        return True, [1]
    reciprocal = [profile[0]] + list(reversed(profile[1:]))
    cyclotomic_quotient = [1] * m
    common = polynomial_gcd(profile, reciprocal, field)
    common = polynomial_gcd(common, cyclotomic_quotient, field)
    return len(common) <= 1, common


def placement_is_clean(
    field: Field, n: int, coefficients: Sequence[int], positions: Sequence[int]
) -> tuple[bool, list[int], list[int]]:
    profile = residue_profile(field, n, coefficients, positions)
    clean, common = profile_is_clean(field, profile)
    return clean, profile, common


def bounded_compositions(total: int, capacities: Sequence[int]) -> Iterator[tuple[int, ...]]:
    vector = [0] * len(capacities)

    def visit(index: int, remaining: int) -> Iterator[tuple[int, ...]]:
        if index == len(capacities):
            if remaining == 0:
                yield tuple(vector)
            return
        rest_capacity = sum(capacities[index + 1 :])
        low = max(0, remaining - rest_capacity)
        high = min(capacities[index], remaining)
        for count in range(low, high + 1):
            vector[index] = count
            yield from visit(index + 1, remaining - count)

    yield from visit(0, total)


def exhaustive_clean_profile_exists(
    field: Field, n: int, coefficients: Sequence[int]
) -> tuple[bool, int]:
    if not 2 <= len(coefficients) <= n:
        raise ValueError("expected 2 <= k <= n")
    m, capacity = prime_free_part(n, field.prime)
    if m == 1:
        return True, 1

    multiplicities = Counter(coefficients)
    anchor = min(multiplicities, key=lambda value: (multiplicities[value], value))
    multiplicities[anchor] -= 1
    if multiplicities[anchor] == 0:
        del multiplicities[anchor]
    values = sorted(multiplicities)
    remaining_capacity = [capacity] * m
    remaining_capacity[0] -= 1
    profile = [0] * m
    profile[0] = anchor
    population = 0
    found = False

    def allocate(index: int) -> None:
        nonlocal population, found
        if index == len(values):
            population += 1
            if profile_is_clean(field, profile)[0]:
                found = True
            return
        value = values[index]
        for vector in bounded_compositions(multiplicities[value], remaining_capacity):
            for residue, count in enumerate(vector):
                if count:
                    remaining_capacity[residue] -= count
                    profile[residue] = field.add(
                        profile[residue], field.scalar(count, value)
                    )
            allocate(index + 1)
            for residue, count in enumerate(vector):
                if count:
                    remaining_capacity[residue] += count
                    profile[residue] = field.sub(
                        profile[residue], field.scalar(count, value)
                    )

    allocate(0)
    return found, population


def coefficients_for_family(field: Field, family: str, k: int) -> list[int]:
    if family == "ones":
        return [1] * k
    if family == "one_changed":
        return [2] + [1] * (k - 1)
    if family == "all_distinct":
        if k > field.order - 1:
            raise ValueError("all_distinct family is undefined for this k")
        return list(range(1, k + 1))
    raise ValueError(f"unknown family {family}")


def run_controls() -> dict:
    orders = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16]
    fields = {order: Field(order) for order in orders}
    moduli = {}
    for order, field in fields.items():
        field.self_check()
        moduli[str(order)] = field.modulus

    va = {}
    for n in [9, 12, 15, 18, 21]:
        clean = placement_is_clean(fields[2], n, [1] * 6, list(range(6)))[0]
        va[str(n)] = "CLEAN" if clean else "DIRTY"
        assert not clean

    vb = {}
    for n in range(5, 30):
        clean = placement_is_clean(fields[2], n, [1] * 4, [0, 1, 2, 3])[0]
        vb[str(n)] = "CLEAN" if clean else "DIRTY"
        assert clean

    examples = [
        (3, 6, [1, 1, 1, 1, 1, 2]),
        (3, 4, [1, 1, 1, 2]),
        (3, 5, [1, 1, 1, 1, 2]),
        (4, 3, [1, 1, 2]),
        (4, 6, [1, 1, 1, 1, 1, 2]),
    ]
    vc = []
    for order, n, changed_coefficients in examples:
        positions = list(range(n))
        changed = placement_is_clean(
            fields[order], n, changed_coefficients, positions
        )[0]
        ones = placement_is_clean(fields[order], n, [1] * n, positions)[0]
        assert changed and not ones
        vc.append(
            {"q": order, "n": n, "changed": "CLEAN", "all_ones": "DIRTY"}
        )

    k2_clean = placement_is_clean(fields[3], 5, [1, 2], [0, 1])[0]
    assert k2_clean
    obstruction_found, obstruction_population = exhaustive_clean_profile_exists(
        fields[3], 4, [1, 1, 2, 2]
    )
    assert not obstruction_found and obstruction_population == 3

    return {
        "field_self_checks": "PASS",
        "moduli": moduli,
        "V-a": va,
        "V-b": vb,
        "V-c": vc,
        "worked_k2_correction": "CLEAN",
        "worked_1122_obstruction": {
            "verdict": "NONE",
            "population": obstruction_population,
            "exhaustive": True,
        },
    }


def audit_csv(path: Path, sample_spec: str, seed: int) -> dict:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    found_indices = [index for index, row in enumerate(rows) if row["verdict"] == "FOUND"]
    none_indices = [index for index, row in enumerate(rows) if row["verdict"] == "NONE"]
    if len(found_indices) + len(none_indices) != len(rows):
        raise AssertionError("unexpected verdict in CSV")

    if sample_spec == "all":
        selected = found_indices
    else:
        requested = int(sample_spec)
        if requested > len(found_indices):
            raise ValueError("sample is larger than the FOUND population")
        selected = sorted(random.Random(seed).sample(found_indices, requested))

    fields: dict[int, Field] = {}
    for row in rows:
        order = int(row["q"])
        if order not in fields:
            fields[order] = Field(order)

    disagreements = []
    for index in selected:
        row = rows[index]
        field = fields[int(row["q"])]
        witness = json.loads(row["witness"])
        clean, profile, common = placement_is_clean(
            field, int(row["n"]), witness["coeffs"], witness["positions"]
        )
        printed_profile = json.loads(row["profile"])
        if not clean or profile != printed_profile or len(common) > 1:
            disagreements.append(
                {
                    "row": index + 2,
                    "q": row["q"],
                    "n": row["n"],
                    "k": row["k"],
                    "family": row["family"],
                    "reason": "FOUND witness failed independent check",
                }
            )

    none_details = []
    for index in none_indices:
        row = rows[index]
        field = fields[int(row["q"])]
        coefficients = coefficients_for_family(field, row["family"], int(row["k"]))
        found, population = exhaustive_clean_profile_exists(field, int(row["n"]), coefficients)
        expected_population = int(row["population_searched"])
        detail = {
            "q": int(row["q"]),
            "n": int(row["n"]),
            "k": int(row["k"]),
            "family": row["family"],
            "independent_population": population,
            "reported_population": expected_population,
        }
        none_details.append(detail)
        if found or population != expected_population or row["exhaustive"] != "yes":
            disagreements.append(
                {
                    **detail,
                    "row": index + 2,
                    "reason": "NONE cell failed independent exhaustive check",
                    "clean_profile_found": found,
                }
            )

    aggregate: dict[str, dict[str, int]] = defaultdict(
        lambda: {"FOUND": 0, "NONE": 0}
    )
    for row in rows:
        key = f"q={row['q']}:{row['family']}"
        aggregate[key][row["verdict"]] += 1

    return {
        "csv": str(path),
        "rows": len(rows),
        "found": len(found_indices),
        "none": len(none_indices),
        "found_check": {
            "seed": seed,
            "requested": sample_spec,
            "checked": len(selected),
        },
        "none_check": {"checked": len(none_indices), "all_exhaustive": True},
        "aggregate": dict(aggregate),
        "none_cells": none_details,
        "disagreements": disagreements,
        "verdict": "PASS" if not disagreements else "FINDING",
    }


def parse_integers(raw: str) -> list[int]:
    return [int(part) for part in raw.split(",") if part]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    controls = subparsers.add_parser("controls")
    controls.add_argument("--output", type=Path, required=True)

    check = subparsers.add_parser("check")
    check.add_argument("--q", type=int, required=True)
    check.add_argument("--n", type=int, required=True)
    check.add_argument("--coefficients", required=True)
    check.add_argument("--positions", required=True)

    audit = subparsers.add_parser("audit")
    audit.add_argument("--csv", type=Path, required=True)
    audit.add_argument("--found-sample", default="1000")
    audit.add_argument("--seed", type=int, default=1695)
    audit.add_argument("--output", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "controls":
        result = run_controls()
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, sort_keys=True))
        return 0
    if args.command == "check":
        field = Field(args.q)
        clean, profile, common = placement_is_clean(
            field,
            args.n,
            parse_integers(args.coefficients),
            parse_integers(args.positions),
        )
        result = {
            "q": args.q,
            "n": args.n,
            "clean": clean,
            "profile": profile,
            "common_gcd": common,
            "modulus": field.modulus,
        }
        print(json.dumps(result, sort_keys=True))
        return 0

    result = audit_csv(args.csv, args.found_sample, args.seed)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
