#!/usr/bin/env python3
"""Adversarial verification for W61 TAIL (Spark prompt).

Implements Havel–Hakimi/"residueAux" process directly and validates
Lemma TAIL counts on a finite search box.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import islice
from typing import Iterable, List, Sequence, Tuple


def hh_step(seq: Tuple[int, ...]) -> Tuple[int, ...]:
    """One Havel–Hakimi step for a descending multiset.

    `0` head would be terminal in residueAux; callers should check this.
    """
    if not seq:
        return ()

    d = seq[0]
    if d == 0:
        # terminal case handled by caller in residueAux/steps
        return seq

    tail = list(seq[1:])
    dec = min(d, len(tail))
    for i in range(dec):
        if tail[i] > 0:
            tail[i] -= 1
        else:
            # This should not occur under well-behaved sorted HH runs in tested box,
            # but we keep safe against malformed input.
            tail[i] = 0

    tail.sort(reverse=True)
    return tuple(tail)


def normalize(seq: Sequence[int]) -> Tuple[int, ...]:
    """Sort descending and drop negative entries."""
    return tuple(sorted((int(x) for x in seq if x >= 0), reverse=True))


def residue_aux(seq: Sequence[int]) -> int:
    """Exact residueAux semantics from the stated spec:

    residueAux [] = 0,
    residueAux (0::s) = 1 + |s|,
    else recurse on one HH step.
    """
    current = normalize(seq)
    if not current:
        return 0

    while True:
        if current[0] == 0:
            return len(current)
        current = hh_step(current)


def steps(seq: Sequence[int]) -> int:
    """Number of HH steps executed before head becomes 0.

    This matches residueAux call count convention used in lemma prose.
    """
    current = normalize(seq)
    if not current:
        return 0

    count = 0
    while current:
        if current[0] == 0:
            return count
        current = hh_step(current)
        count += 1
    return count


def s0(lam: Sequence[int]) -> int:
    lam = normalize(lam)
    if not lam:
        raise ValueError("s0(λ) is undefined in this text for λ = []")
    m = lam[0]
    return steps((m,) * (m + 1) + lam)


def gen_partitions(total: int, max_part: int | None = None) -> List[Tuple[int, ...]]:
    if total < 0:
        return []
    if max_part is None:
        max_part = total

    out: List[Tuple[int, ...]] = [()]

    def rec(rem: int, limit: int):
        if rem == 0:
            return [()]
        vals: List[Tuple[int, ...]] = []
        for first in range(min(rem, limit), 0, -1):
            for rest in rec(rem - first, first):
                vals.append((first,) + rest)
        return vals

    for s in range(1, total + 1):
        out.extend(rec(s, min(max_part, s)))
    return out


@dataclass
class Mismatch:
    lam: Tuple[int, ...]
    lam1: int
    L: int
    observed: int
    predicted: int


def residue_k2() -> int:
    return residue_aux((1, 1))


def residue_cycle(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return residue_aux((2,) * n)


def steps_cycle(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return steps((2,) * n)


def run_tail_box(max_lambda_sum: int = 12, max_L: int = 15):
    partitions = gen_partitions(max_lambda_sum)
    in_scope_mismatch: List[Mismatch] = []
    out_scope_mismatch: List[Mismatch] = []

    in_scope_pairs = 0
    out_scope_pairs = 0

    cache_s0 = {}

    for lam in partitions:
        lam1 = lam[0] if lam else 0
        if lam:
            cache_s0[lam] = s0(lam)

        for L in range(max_L + 1):
            init = (L,) * (L + 1) + lam
            observed = steps(init)

            if lam and L >= lam1:
                in_scope_pairs += 1
                predicted = (L - lam1) + cache_s0[lam]
                if observed != predicted:
                    in_scope_mismatch.append(Mismatch(lam=lam, lam1=lam1, L=L, observed=observed, predicted=predicted))
            elif lam:
                out_scope_pairs += 1
                predicted = (L - lam1) + cache_s0[lam]
                if observed != predicted:
                    out_scope_mismatch.append(Mismatch(lam=lam, lam1=lam1, L=L, observed=observed, predicted=predicted))

    return {
        "partitions": partitions,
        "in_scope_pairs": in_scope_pairs,
        "out_scope_pairs": out_scope_pairs,
        "in_scope_mismatch": in_scope_mismatch,
        "out_scope_mismatch": out_scope_mismatch,
    }


def format_partition(lam: Tuple[int, ...]) -> str:
    if not lam:
        return "[]"
    return "[" + ",".join(map(str, lam)) + "]"


def first_mismatches(mismatches: List[Mismatch], n: int) -> List[Mismatch]:
    return mismatches[: min(n, len(mismatches))]


def save_report(path: str = "problems/wowii/w61_S3_TAIL_spark_check.out") -> dict:
    cal = [
        "[CALIBRATION]",
        f"residue(K2)={residue_k2()}",
        f"steps(K2)={steps((1,1))}",
    ]

    for n in range(3, 10):
        cal.append(f"n={n}: residue(C_n)={residue_cycle(n)}, steps(C_n)={steps_cycle(n)}, ceil(n/3)={(n + 2)//3}")

    box = run_tail_box()

    lines: List[str] = []
    lines.extend(cal)
    lines.append(f"[BOX] max|λ|={12} maxL=15")
    lines.append(f"#partitions(including empty)={len(box['partitions'])}")
    lines.append(f"in_scope_pairs={box['in_scope_pairs']}")
    lines.append(f"in_scope_mismatches={len(box['in_scope_mismatch'])}")

    for m in box["in_scope_mismatch"]:
        lines.append(f"IN  λ={format_partition(m.lam)} λ1={m.lam1} L={m.L} observed={m.observed} predicted={m.predicted}")

    lines.append(f"out_scope_pairs={box['out_scope_pairs']}")
    lines.append(f"out_scope_mismatches={len(box['out_scope_mismatch'])}")
    for m in box["out_scope_mismatch"]:
        lines.append(f"OUT λ={format_partition(m.lam)} λ1={m.lam1} L={m.L} observed={m.observed} predicted={m.predicted}")

    # Boundary/spot checks
    lines.append("[BOUNDARY]")
    lines.append("lambda_empty: not admissible for s0 under this statement")
    lam2 = (2,)
    s02 = s0(lam2)
    lines.append(f"L=lambda1 boundary λ={format_partition(lam2)}: for L=2 observed={steps((2,)*3 + lam2)} predicted={0 + s02}")
    lines.append(f"L=lambda1-1 boundary λ={format_partition(lam2)}: for L=1 observed={steps((1,)*2 + lam2)} predicted={-1 + s02}")

    lam11 = (1, 1)
    s01 = s0(lam11)
    lines.append(f"λ={format_partition(lam11)} L=1 observed={steps((1,)*2 + lam11)} predicted={(1 - 1) + s01}")

    for nu in range(1, 7):
        lam = (2 * nu,)
        s = s0(lam)
        lines.append(f"two_nu nu={nu} λ={format_partition(lam)} λ1={lam[0]}: L=λ1 observed={steps((lam[0],)*(lam[0]+1) + lam)} predicted={s}")

    # Smallest repeated-max partitions in-scope sample
    samples = [((3, 3), None), ((4, 4), None), ((3, 3, 1), None), ((3, 2, 1, 1), None)]
    for lam, _ in samples:
        lam1 = lam[0]
        L = lam1
        lines.append(f"sample-lam-equal-max λ={format_partition(lam)} L=λ1 observed={steps((L,) * (L + 1) + lam)} predicted={s0(lam)}")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return {
        "calibration": cal,
        "box": box,
        "s0_values": {"2": s02},
    }


def main() -> None:
    result = save_report()

    print("VERIFICATION_SUMMARY")
    print(f"in_scope_pairs={result['box']['in_scope_pairs']}")
    print(f"in_scope_mismatches={len(result['box']['in_scope_mismatch'])}")
    print(f"out_scope_pairs={result['box']['out_scope_pairs']}")
    print(f"out_scope_mismatches={len(result['box']['out_scope_mismatch'])}")


if __name__ == "__main__":
    main()
