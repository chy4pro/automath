#!/usr/bin/env python3
"""Falsification and boundary checks for W61 S3 TAIL (Spark brief)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple


def hh_single_step(seq: Tuple[int, ...]) -> Tuple[int, ...]:
    if not seq:
        return ()

    d = seq[0]
    if d == 0:
        return seq

    tail = list(seq[1:])
    dec = min(d, len(tail))
    for i in range(dec):
        if tail[i] > 0:
            tail[i] -= 1
    tail.sort(reverse=True)
    return tuple(tail)


def hh_steps(seq: Sequence[int]) -> Tuple[int, Tuple[int, ...]]:
    current = tuple(sorted((int(x) for x in seq if x >= 0), reverse=True))
    steps = 0

    while current:
        if current[0] == 0:
            return steps, current
        current = hh_single_step(current)
        steps += 1

    return steps, ()


def residue_aux(seq: Sequence[int]) -> int:
    return hh_steps(seq)[1].__len__()


def steps(seq: Sequence[int]) -> int:
    return hh_steps(seq)[0]


def residue_k2() -> int:
    return residue_aux((1, 1))


def residue_cycle(n: int) -> int:
    return residue_aux((2,) * n)


def steps_cycle(n: int) -> int:
    return steps((2,) * n)


def s0(lam: Sequence[int]) -> int:
    lam = tuple(sorted((int(x) for x in lam if x >= 0), reverse=True))
    if not lam:
        raise ValueError("s0 requires non-empty partition")
    lam1 = lam[0]
    start = (lam1,) * (lam1 + 1) + lam
    return steps(start)


def gen_partitions(n: int) -> List[Tuple[int, ...]]:
    out = [()]  # empty partition

    def rec(rem: int, max_part: int) -> List[Tuple[int, ...]]:
        if rem == 0:
            return [()]
        out_local: List[Tuple[int, ...]] = []
        for first in range(min(rem, max_part), 0, -1):
            for suf in rec(rem - first, first):
                out_local.append((first,) + suf)
        return out_local

    for total in range(1, n + 1):
        out.extend(rec(total, total))
    return out


@dataclass
class TailRecord:
    lam: Tuple[int, ...]
    lam1: int
    L: int
    observed: int
    predicted: int


def verify_tail(max_sum: int = 12, max_L: int = 15):
    partitions = gen_partitions(max_sum)
    s0_cache = {}

    in_mismatch: List[TailRecord] = []
    out_mismatch: List[TailRecord] = []
    in_total = 0
    out_total = 0

    for lam in partitions:
        lam1 = lam[0] if lam else 0
        if lam:
            s0_cache[lam] = s0(lam)

        for L in range(max_L + 1):
            init = (L,) * (L + 1) + lam
            observed = steps(init)

            if lam and L >= lam1:
                in_total += 1
                predicted = (L - lam1) + s0_cache[lam]
                if observed != predicted:
                    in_mismatch.append(TailRecord(lam=lam, lam1=lam1, L=L, observed=observed, predicted=predicted))
            elif lam:
                out_total += 1
                predicted = (L - lam1) + s0_cache[lam]
                if observed != predicted:
                    out_mismatch.append(TailRecord(lam=lam, lam1=lam1, L=L, observed=observed, predicted=predicted))

    return in_mismatch, out_mismatch, in_total, out_total, len(partitions)


def boundary_checks() -> List[Tuple[str, int]]:
    checks = {}

    # λ = ∅ boundary
    checks["lambda_empty__L2"] = steps((2,) * 3)

    # λ with repeated maxima and small ν patterns
    checks["lambda=[2] L=7 (E.g. observed) "] = steps((7,) * 8 + (2,))
    checks["lambda=[1,1] L=6"] = steps((6,) * 7 + (1, 1))
    checks["lambda=[2,2] L=7"] = steps((7,) * 8 + (2, 2))
    checks["lambda=[2,1,1] L=6"] = steps((6,) * 7 + (2, 1, 1))

    checks["lambda=[2], L=2, s0 pred"] = s0((2,)) + (2 - 2)
    return list(checks.items())


def main() -> None:
    cal = [
        "[CALIBRATION]",
        f"residue(K2) = {residue_k2()}",
        f"steps(K2) = 1",
    ]
    for n in range(3, 10):
        cal.append(f"n={n}: residue(C_n) = {residue_cycle(n)}, steps = {steps_cycle(n)}, ceil(n/3) = {(n + 2)//3}")

    in_mismatch, out_mismatch, in_total, out_total, part_count = verify_tail()

    out_lines = []
    out_lines.extend(cal)
    out_lines.append(f"[PARTITIONS] total partitions with |λ|<=12 (including ∅): {part_count}")
    out_lines.append(f"[HYPBOX] L<=15")
    out_lines.append(f"in-hypothesis pairs: {in_total}")
    out_lines.append(f"in-hypothesis mismatches: {len(in_mismatch)}")
    for r in in_mismatch:
        out_lines.append(f"IN  λ={r.lam} λ1={r.lam1} L={r.L} observed={r.observed} pred={r.predicted}")
    out_lines.append(f"outside-hypothesis pairs (λ non-empty): {out_total}")
    out_lines.append(f"outside-hypothesis mismatches: {len(out_mismatch)}")
    for r in out_mismatch:
        out_lines.append(f"OUT λ={r.lam} λ1={r.lam1} L={r.L} observed={r.observed} pred={r.predicted}")

    lam2_pred = (2 - 2) + s0((2,))
    lam2_pred_at_3 = (3 - 2) + s0((2,))
    lam2_steps_l2 = steps((2,) * 3 + (2,))
    lam11_steps = steps((2,) * 3 + (1, 1))
    lam11_pred = (2 - 1) + s0((1, 1))

    out_lines.append("[BOUNDARY]")
    out_lines.append("λ = [] : cannot form λ1; direct from [L]^(L+1), e.g. L=2 gives " + str(steps((2, 2, 2))))
    out_lines.append(
        "λ=[2], L=2: observed="
        + str(lam2_steps_l2)
        + ", s0([2])="
        + str(s0((2,)))
        + ", formula="
        + str(lam2_pred)
    )
    out_lines.append(
        "λ=[2], L=3: observed="
        + str(steps((3, 3, 3, 3, 2)))
        + ", s0([2])="
        + str(s0((2,)))
        + ", formula="
        + str(lam2_pred_at_3)
    )
    out_lines.append(
        "λ=[1,1], L=2: observed="
        + str(lam11_steps)
        + ", formula(if in-hyp)="
        + str(lam11_pred)
    )
    out_lines.append(
        "λ=[4], L=3 (L<λ1): observed="
        + str(steps((3, 3, 3, 4)))
        + ", formula="
        + str((3 - 4) + s0((4,)))
    )

    out_lines.append("[FAN-5 λ=[2] range L=2..10]")
    for L in range(2, 11):
        out_lines.append(f"L={L}: observed={steps((L,) * (L + 1) + (2,))}, predicted={ (L - 2) + s0((2,)) }")

    with open("problems/w61/w61_S3_TAIL_spark_check.out", "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines) + "\n")

    print("VERIFICATION_SUMMARY")
    print(f"in_hypothesis_pairs={in_total}")
    print(f"in_hypothesis_mismatches={len(in_mismatch)}")
    print(f"outside_hypothesis_pairs={out_total}")
    print(f"outside_hypothesis_mismatches={len(out_mismatch)}")


if __name__ == "__main__":
    main()
