#!/usr/bin/env python3
"""K5-GFQ exact reciprocal-root placement solver and table generator.
Stdlib only. Exact finite-field arithmetic; no floating point.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


# ---------- prime powers and exact finite fields ----------

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = math.isqrt(n)
    f = 3
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    return True


def prime_power(q: int) -> Tuple[int, int]:
    if q < 2:
        raise ValueError("q must be at least 2")
    for p in range(2, q + 1):
        if not is_prime(p) or q % p:
            continue
        x, d = q, 0
        while x % p == 0:
            x //= p
            d += 1
        if x == 1:
            return p, d
    raise ValueError(f"{q} is not a prime power")


def _fp_trim(a: List[int], p: int) -> List[int]:
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def _fp_divmod(a: Sequence[int], b: Sequence[int], p: int) -> Tuple[List[int], List[int]]:
    aa = _fp_trim(list(a), p)
    bb = _fp_trim(list(b), p)
    if not bb:
        raise ZeroDivisionError
    q = [0] * max(0, len(aa) - len(bb) + 1)
    ib = pow(bb[-1], p - 2, p)
    while aa and len(aa) >= len(bb):
        d = len(aa) - len(bb)
        c = aa[-1] * ib % p
        q[d] = c
        for j, y in enumerate(bb):
            aa[d + j] = (aa[d + j] - c * y) % p
        aa = _fp_trim(aa, p)
    return _fp_trim(q, p), aa


def _fp_gcd(a: Sequence[int], b: Sequence[int], p: int) -> List[int]:
    aa, bb = _fp_trim(list(a), p), _fp_trim(list(b), p)
    while bb:
        _, rr = _fp_divmod(aa, bb, p)
        aa, bb = bb, rr
    if aa:
        z = pow(aa[-1], p - 2, p)
        aa = [(x * z) % p for x in aa]
    return _fp_trim(aa, p)


def _fp_mulmod(a: Sequence[int], b: Sequence[int], mod: Sequence[int], p: int) -> List[int]:
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    _, r = _fp_divmod(c, mod, p)
    return r


def _fp_powmod_x(exp: int, mod: Sequence[int], p: int) -> List[int]:
    out, base = [1], [0, 1]
    e = exp
    while e:
        if e & 1:
            out = _fp_mulmod(out, base, mod, p)
        base = _fp_mulmod(base, base, mod, p)
        e >>= 1
    return out


def find_irreducible(p: int, d: int) -> List[int]:
    if d == 1:
        return [0, 1]
    # Deterministic lexicographic search among monic degree-d polynomials,
    # using Rabin's irreducibility criterion.
    for coeffs in itertools.product(range(p), repeat=d):
        if coeffs[0] == 0:
            continue
        f = list(coeffs) + [1]
        ok = True
        xpoly = [0, 1]
        # gcd(x^(p^i)-x, f)=1 for i=1,...,floor(d/2)
        xp = xpoly
        for i in range(1, d // 2 + 1):
            xp = _fp_powmod_x(p ** i, f, p)
            diff = xp[:]
            if len(diff) < 2:
                diff += [0] * (2 - len(diff))
            diff[1] = (diff[1] - 1) % p
            if len(_fp_gcd(diff, f, p)) > 1:
                ok = False
                break
        if not ok:
            continue
        # x^(p^d) == x mod f
        xp = _fp_powmod_x(p ** d, f, p)
        diff = xp[:]
        if len(diff) < 2:
            diff += [0] * (2 - len(diff))
        diff[1] = (diff[1] - 1) % p
        if not _fp_trim(diff, p):
            return f
    raise RuntimeError(f"no irreducible polynomial found for GF({p}^{d})")


class GF:
    """GF(p^d), elements encoded as base-p integers (polynomial basis)."""

    def __init__(self, q: int):
        self.q = q
        self.p, self.d = prime_power(q)
        self.modulus = find_irreducible(self.p, self.d)
        self._digits = [self._decode_raw(a) for a in range(q)]
        self._add = [[0] * q for _ in range(q)]
        self._mul = [[0] * q for _ in range(q)]
        self._neg = [0] * q
        for a in range(q):
            da = self._digits[a]
            self._neg[a] = self._encode([(-x) % self.p for x in da])
            for b in range(q):
                db = self._digits[b]
                self._add[a][b] = self._encode([(da[i] + db[i]) % self.p for i in range(self.d)])
                self._mul[a][b] = self._mul_raw(da, db)
        self._inv = [0] * q
        for a in range(1, q):
            for b in range(1, q):
                if self._mul[a][b] == 1:
                    self._inv[a] = b
                    break
            if self._inv[a] == 0:
                raise AssertionError("nonzero element has no inverse")

    def _decode_raw(self, a: int) -> List[int]:
        out = []
        x = a
        for _ in range(self.d):
            out.append(x % self.p)
            x //= self.p
        return out

    def _encode(self, coeffs: Sequence[int]) -> int:
        out, place = 0, 1
        for i in range(self.d):
            out += (coeffs[i] % self.p) * place
            place *= self.p
        return out

    def _mul_raw(self, a: Sequence[int], b: Sequence[int]) -> int:
        if self.d == 1:
            return (a[0] * b[0]) % self.p
        c = [0] * (2 * self.d - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i + j] = (c[i + j] + x * y) % self.p
        # modulus is f_0+...+f_{d-1}x^{d-1}+x^d
        for t in range(len(c) - 1, self.d - 1, -1):
            z = c[t] % self.p
            if z:
                for j in range(self.d):
                    c[t - self.d + j] = (c[t - self.d + j] - z * self.modulus[j]) % self.p
        return self._encode(c[: self.d])

    def add(self, a: int, b: int) -> int:
        return self._add[a][b]

    def neg(self, a: int) -> int:
        return self._neg[a]

    def sub(self, a: int, b: int) -> int:
        return self._add[a][self._neg[b]]

    def mul(self, a: int, b: int) -> int:
        return self._mul[a][b]

    def inv(self, a: int) -> int:
        if a == 0:
            raise ZeroDivisionError
        return self._inv[a]

    def div(self, a: int, b: int) -> int:
        return self._mul[a][self.inv(b)]

    def pow(self, a: int, e: int) -> int:
        if e < 0:
            return self.pow(self.inv(a), -e)
        out, base = 1, a
        while e:
            if e & 1:
                out = self.mul(out, base)
            base = self.mul(base, base)
            e >>= 1
        return out

    def sum(self, xs: Iterable[int]) -> int:
        out = 0
        for x in xs:
            out = self.add(out, x)
        return out

    def scalar(self, integer: int, a: int = 1) -> int:
        return self.mul(integer % self.p, a)

    def element_str(self, a: int) -> str:
        if self.d == 1:
            return str(a)
        ds = self._digits[a]
        terms = []
        for i, c in enumerate(ds):
            if not c:
                continue
            if i == 0:
                terms.append(str(c))
            elif i == 1:
                terms.append("a" if c == 1 else f"{c}a")
            else:
                terms.append(f"a^{i}" if c == 1 else f"{c}a^{i}")
        return "+".join(terms) if terms else "0"

    def self_check(self) -> None:
        q = self.q
        assert self.add(0, 1) == 1 and self.mul(1, 1) == 1
        for a in range(q):
            assert self.add(a, self.neg(a)) == 0
            assert self.add(a, 0) == a and self.mul(a, 1) == a and self.mul(a, 0) == 0
            if a:
                assert self.mul(a, self.inv(a)) == 1
        for a in range(q):
            for b in range(q):
                assert self.add(a, b) == self.add(b, a)
                assert self.mul(a, b) == self.mul(b, a)
                for c in range(q):
                    assert self.add(self.add(a, b), c) == self.add(a, self.add(b, c))
                    assert self.mul(self.mul(a, b), c) == self.mul(a, self.mul(b, c))
                    assert self.mul(a, self.add(b, c)) == self.add(self.mul(a, b), self.mul(a, c))


# ---------- polynomials over GF(q) ----------

def poly_trim(a: Sequence[int]) -> List[int]:
    out = list(a)
    while out and out[-1] == 0:
        out.pop()
    return out


def poly_divmod(a: Sequence[int], b: Sequence[int], F: GF) -> Tuple[List[int], List[int]]:
    aa, bb = poly_trim(a), poly_trim(b)
    if not bb:
        raise ZeroDivisionError
    q = [0] * max(0, len(aa) - len(bb) + 1)
    ib = F.inv(bb[-1])
    while aa and len(aa) >= len(bb):
        d = len(aa) - len(bb)
        c = F.mul(aa[-1], ib)
        q[d] = c
        for j, y in enumerate(bb):
            aa[d + j] = F.sub(aa[d + j], F.mul(c, y))
        aa = poly_trim(aa)
    return poly_trim(q), aa


def poly_gcd(a: Sequence[int], b: Sequence[int], F: GF) -> List[int]:
    aa, bb = poly_trim(a), poly_trim(b)
    while bb:
        _, rr = poly_divmod(aa, bb, F)
        aa, bb = bb, rr
    if aa:
        z = F.inv(aa[-1])
        aa = [F.mul(x, z) for x in aa]
    return poly_trim(aa)


def factor_m_and_h(n: int, p: int) -> Tuple[int, int]:
    m, h = n, 1
    while m % p == 0:
        m //= p
        h *= p
    return m, h


def reciprocal_profile(T: Sequence[int]) -> List[int]:
    m = len(T)
    if m == 0:
        return []
    out = [0] * m
    out[0] = T[0]
    for r in range(1, m):
        out[r] = T[m - r]
    return out


def clean_profile(T: Sequence[int], F: GF) -> Tuple[bool, List[int]]:
    m = len(T)
    if m == 1:
        return True, [1]
    C = [1] * m  # (x^m-1)/(x-1)
    g = poly_gcd(poly_gcd(T, reciprocal_profile(T), F), C, F)
    return len(g) <= 1, g


def profile_from_positions(n: int, coeffs: Sequence[int], positions: Sequence[int], F: GF) -> List[int]:
    if len(coeffs) != len(positions):
        raise ValueError("coefficients and positions have different lengths")
    if len(set(positions)) != len(positions) or any(s < 0 or s >= n for s in positions):
        raise ValueError("positions must be distinct elements of Z_n")
    m, _ = factor_m_and_h(n, F.p)
    T = [0] * m
    for u, s in zip(coeffs, positions):
        if not (0 < u < F.q):
            raise ValueError("all coefficients must be nonzero field elements")
        r = s % m
        T[r] = F.add(T[r], u)
    return T


def verify_witness(n: int, coeffs: Sequence[int], positions: Sequence[int], F: GF) -> Tuple[bool, List[int], List[int]]:
    T = profile_from_positions(n, coeffs, positions, F)
    ok, g = clean_profile(T, F)
    return ok, T, g


# ---------- exact normalized allocation search ----------

def bounded_vectors(total: int, caps: Sequence[int]) -> Iterator[Tuple[int, ...]]:
    """All x with 0<=x_i<=caps_i and sum x_i=total; high values first."""
    m = len(caps)
    suffix = [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        suffix[i] = suffix[i + 1] + caps[i]
    x = [0] * m

    def rec(i: int, left: int) -> Iterator[Tuple[int, ...]]:
        if i == m:
            if left == 0:
                yield tuple(x)
            return
        lo = max(0, left - suffix[i + 1])
        hi = min(caps[i], left)
        for v in range(hi, lo - 1, -1):
            x[i] = v
            yield from rec(i + 1, left - v)

    yield from rec(0, total)


@dataclass
class SearchResult:
    found: bool
    positions: Optional[List[int]]
    coeffs: List[int]
    profile: Optional[List[int]]
    gcd: Optional[List[int]]
    population: int
    exhaustive: bool
    normalized_space: str


def allocation_to_positions(m: int, h: int, anchor: int,
                            allocations: Dict[int, Tuple[int, ...]],
                            original_coeffs: Sequence[int]) -> Tuple[List[int], List[int]]:
    # Rebuild a coefficient list aligned with explicit positions.  The anchor is first.
    slots = [[r + j * m for j in range(h)] for r in range(m)]
    used = [0] * m
    coeff_out = [anchor]
    pos_out = [slots[0][0]]
    used[0] = 1
    remaining = Counter(original_coeffs)
    remaining[anchor] -= 1
    for value in sorted(allocations):
        vec = allocations[value]
        assert sum(vec) == remaining[value]
        for r, count in enumerate(vec):
            for _ in range(count):
                coeff_out.append(value)
                pos_out.append(slots[r][used[r]])
                used[r] += 1
    assert Counter(coeff_out) == Counter(original_coeffs)
    return coeff_out, pos_out


def solve_exact(F: GF, n: int, coeffs: Sequence[int], stop_at_first: bool = True) -> SearchResult:
    """Complete finite algorithm.  Rotation-normalize one anchor coefficient to residue 0."""
    coeffs = list(coeffs)
    if n < 2 or not (2 <= len(coeffs) <= n):
        raise ValueError("need n>=2 and 2<=k<=n")
    if any(u <= 0 or u >= F.q for u in coeffs):
        raise ValueError("coefficients must be encoded nonzero GF(q) elements")
    m, h = factor_m_and_h(n, F.p)
    if m == 1:
        positions = list(range(len(coeffs)))
        ok, T, g = verify_witness(n, coeffs, positions, F)
        assert ok
        return SearchResult(True, positions, coeffs, T, g, 1, False, "vacuous m=1")

    # Use a least-multiplicity value as anchor: fewer capacity-coupled duplicates at residue 0.
    counts = Counter(coeffs)
    anchor = min(counts, key=lambda x: (counts[x], x))
    counts[anchor] -= 1
    if counts[anchor] == 0:
        del counts[anchor]
    values = sorted(counts, key=lambda x: (-counts[x], x))
    caps = [h] * m
    caps[0] -= 1
    sums = [0] * m
    sums[0] = anchor
    allocations: Dict[int, Tuple[int, ...]] = {}
    population = 0
    witness: Optional[Tuple[List[int], List[int], List[int], List[int]]] = None

    def rec(j: int) -> bool:
        nonlocal population, witness
        if j == len(values):
            population += 1
            ok, g = clean_profile(sums, F)
            if ok:
                coeff_out, pos_out = allocation_to_positions(m, h, anchor, allocations, coeffs)
                ok2, T2, g2 = verify_witness(n, coeff_out, pos_out, F)
                assert ok2 and T2 == sums and g2 == g
                witness = (coeff_out, pos_out, list(sums), g)
                return True
            return False
        v = values[j]
        total = counts[v]
        for vec in bounded_vectors(total, caps):
            allocations[v] = vec
            for r, c in enumerate(vec):
                if c:
                    caps[r] -= c
                    sums[r] = F.add(sums[r], F.scalar(c, v))
            got = rec(j + 1)
            for r, c in enumerate(vec):
                if c:
                    caps[r] += c
                    sums[r] = F.sub(sums[r], F.scalar(c, v))
            if got and stop_at_first:
                return True
        allocations.pop(v, None)
        return False

    rec(0)
    if witness is not None:
        c, p, T, g = witness
        return SearchResult(True, p, c, T, g, population, False,
                            "all residue allocations modulo cyclic rotation")
    return SearchResult(False, None, coeffs, None, None, population, True,
                        "all residue allocations modulo cyclic rotation")


# ---------- mandatory controls and theorem checks ----------

def verdict(F: GF, n: int, coeffs: Sequence[int], positions: Sequence[int]) -> str:
    return "CLEAN" if verify_witness(n, coeffs, positions, F)[0] else "DIRTY"


def multiplicative_order(F: GF, a: int) -> int:
    if a == 0:
        raise ValueError
    x = 1
    for d in range(1, F.q):
        x = F.mul(x, a)
        if x == 1:
            return d
    raise AssertionError


def k2_predicate_correct(F: GF, m: int, u1: int, u2: int, g: int) -> bool:
    """True iff a nontrivial bad lambda exists; g is read modulo m."""
    if m == 1:
        return False
    gg = math.gcd(m, g)
    c = F.neg(F.div(u1, u2))
    if F.mul(c, c) != 1:
        return False
    if c == 1:
        return gg > 1
    order = multiplicative_order(F, c)
    return (m // gg) % order == 0


def run_controls(fields: Dict[int, GF]) -> None:
    F2 = fields.get(2) or GF(2)
    F2.self_check()
    print("V-a")
    for n in [9, 12, 15, 18, 21]:
        v = verdict(F2, n, [1] * 6, list(range(6)))
        print(f" q=2 n={n} k=6 consecutive: {v}")
        assert v == "DIRTY"
    print("V-b")
    vals = []
    for n in range(5, 30):
        v = verdict(F2, n, [1] * 4, [0, 1, 2, 3])
        vals.append(v)
        assert v == "CLEAN"
    print(" q=2 n=5..29 k=4 consecutive: " + ",".join(vals))

    print("V-c")
    examples = [
        (3, 6, [1, 1, 1, 1, 1, 2]),
        (3, 4, [1, 1, 1, 2]),
        (3, 5, [1, 1, 1, 1, 2]),
        (4, 3, [1, 1, 2]),
        (4, 6, [1, 1, 1, 1, 1, 2]),
    ]
    for q, n, cs in examples:
        F = fields[q]
        pos = list(range(n))
        changed = verdict(F, n, cs, pos)
        ones = verdict(F, n, [1] * n, pos)
        print(f" q={q} n={n}: changed={changed}, all-ones={ones}")
        assert changed == "CLEAN" and ones == "DIRTY"

    print("V-d")
    for q in sorted(fields):
        fields[q].self_check()
        print(f" GF({q}) p={fields[q].p} d={fields[q].d} modulus={fields[q].modulus}: PASS")

    # Explicit correction to the stated k=2 condition.
    F3 = fields[3]
    assert verdict(F3, 5, [1, 2], [0, 1]) == "CLEAN"
    print("k2-correction witness: GF(3), m=n=5, u=[1,2], s=[0,1] is CLEAN")
    # Exhaustively compare the corrected formula with the polynomial-gcd checker.
    for q, F in sorted(fields.items()):
        for m in range(2, 31):
            if m % F.p == 0:
                continue
            for u1 in range(1, q):
                for u2 in range(1, q):
                    for gap in range(0, m):
                        T = [0] * m
                        T[0] = u1
                        T[gap] = F.add(T[gap], u2)
                        actual_bad = not clean_profile(T, F)[0]
                        predicted_bad = k2_predicate_correct(F, m, u1, u2, gap)
                        assert actual_bad == predicted_bad, (q, m, u1, u2, gap, actual_bad, predicted_bad)
    print(" corrected k=2 criterion vs gcd checker, all q and m<=30: PASS")

    # First unequal-coefficient obstruction in odd characteristic.
    obstruction = solve_exact(F3, 4, [1, 1, 2, 2], stop_at_first=True)
    assert not obstruction.found and obstruction.exhaustive
    print(f"unequal obstruction: GF(3), n=4, coeffs=[1,1,2,2], NONE; population={obstruction.population}, exhaustive=yes")


# ---------- requested table ----------

def family_coeffs(F: GF, family: str, k: int) -> Optional[List[int]]:
    if family == "ones":
        return [1] * k
    if family == "one_changed":
        a = next(x for x in range(2, F.q) if x != 1)
        return [a] + [1] * (k - 1)
    if family == "all_distinct":
        if k > F.q - 1:
            return None
        return list(range(1, k + 1))
    raise ValueError(family)


def generate_table(qs: Sequence[int], nmax: int, csv_path: str) -> Dict[str, object]:
    fields = {q: GF(q) for q in sorted(set(qs) | {2})}
    run_controls(fields)
    families = ["ones", "one_changed", "all_distinct"]
    rows = []
    no_rows = []
    total_cells = 0
    for q in qs:
        F = fields[q]
        for n in range(2, nmax + 1):
            m, h = factor_m_and_h(n, F.p)
            for k in range(2, n + 1):
                for fam in families:
                    cs = family_coeffs(F, fam, k)
                    if cs is None:
                        continue
                    total_cells += 1
                    res = solve_exact(F, n, cs, stop_at_first=True)
                    if res.found:
                        ok, T, g = verify_witness(n, res.coeffs, res.positions or [], F)
                        assert ok and T == res.profile and len(g) <= 1
                        witness = json.dumps({"coeffs": res.coeffs, "positions": res.positions}, separators=(",", ":"))
                        profile = json.dumps(res.profile, separators=(",", ":"))
                    else:
                        assert res.exhaustive
                        witness, profile = "", ""
                        no_rows.append((q, n, k, fam, res.population))
                    row = {
                        "q": q,
                        "p": F.p,
                        "d": F.d,
                        "n": n,
                        "m": m,
                        "h": h,
                        "k": k,
                        "family": fam,
                        "verdict": "FOUND" if res.found else "NONE",
                        "witness": witness,
                        "profile": profile,
                        "population_searched": res.population,
                        "exhaustive": "yes" if res.exhaustive else "no",
                        "population_definition": res.normalized_space,
                    }
                    rows.append(row)
    fields_out = list(rows[0].keys()) if rows else []
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields_out)
        w.writeheader()
        w.writerows(rows)
    print(f"TABLE rows={len(rows)} cells={total_cells} csv={csv_path}")
    print("NO-CLEAN rows (all exhaustive):")
    for item in no_rows:
        print(" ", item)
    checked = reverify_csv(csv_path, fields)
    aggregate: Dict[str, Dict[str, int]] = {}
    for row in rows:
        key = f"q={row['q']}:{row['family']}"
        aggregate.setdefault(key, {"FOUND": 0, "NONE": 0})[row["verdict"]] += 1
    return {"rows": len(rows), "cells": total_cells, "found": checked["found"],
            "none": checked["none"], "no_rows": no_rows, "aggregate": aggregate, "csv": csv_path}


def reverify_csv(csv_path: str, fields: Dict[int, GF]) -> Dict[str, int]:
    found = none = 0
    no_cache: Dict[Tuple[int, int, Tuple[int, ...]], SearchResult] = {}
    with open(csv_path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            q, n = int(row["q"]), int(row["n"])
            F = fields[q]
            if row["verdict"] == "FOUND":
                obj = json.loads(row["witness"])
                ok, T, g = verify_witness(n, obj["coeffs"], obj["positions"], F)
                assert ok and T == json.loads(row["profile"]) and len(g) <= 1
                found += 1
            else:
                assert row["verdict"] == "NONE" and row["exhaustive"] == "yes"
                fam, k = row["family"], int(row["k"])
                cs = family_coeffs(F, fam, k)
                assert cs is not None
                key = (q, n, tuple(cs))
                if key not in no_cache:
                    no_cache[key] = solve_exact(F, n, cs, stop_at_first=True)
                rr = no_cache[key]
                assert not rr.found and rr.exhaustive
                assert rr.population == int(row["population_searched"])
                none += 1
    print(f"SECOND-PASS REVERIFY: witnesses={found}, NONE certificates={none}: PASS")
    return {"found": found, "none": none}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", action="store_true", help="generate the requested q,n,k table")
    ap.add_argument("--csv", default="k5_gfq_table.csv")
    ap.add_argument("--nmax", type=int, default=30)
    ap.add_argument("--qs", default="3,4,5,7,8,9")
    args = ap.parse_args()
    if args.table:
        qs = [int(x) for x in args.qs.split(",") if x]
        summary = generate_table(qs, args.nmax, args.csv)
        print("SUMMARY", json.dumps(summary, separators=(",", ":")))
    else:
        fields = {q: GF(q) for q in [2, 3, 4, 5, 7, 8, 9]}
        run_controls(fields)
        print("All controls passed.")


if __name__ == "__main__":
    main()
