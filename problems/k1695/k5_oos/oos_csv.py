#!/usr/bin/env python3
"""Filter and summarize K5-GFQ out-of-sample CSV tables."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def is_power_of_two(value: int) -> bool:
    return value > 0 and value & (value - 1) == 0


def literal_claim(row: dict[str, str]) -> bool:
    n = int(row["n"])
    k = int(row["k"])
    odd_characteristic = int(row["p"]) % 2 == 1
    forced_full = k == n and int(row["m"]) > 1
    listed_extra = odd_characteristic and n in {4, 8, 16} and k in {2, n - 2}
    return row["family"] == "ones" and (forced_full or listed_extra)


def power_two_extension(row: dict[str, str]) -> bool:
    n = int(row["n"])
    k = int(row["k"])
    return (
        row["family"] == "ones"
        and int(row["p"]) % 2 == 1
        and is_power_of_two(n)
        and k in {2, n - 2}
    )


def cell(row: dict[str, str]) -> dict[str, object]:
    return {
        "q": int(row["q"]),
        "n": int(row["n"]),
        "k": int(row["k"]),
        "family": row["family"],
        "m": int(row["m"]),
        "population": int(row["population_searched"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--qs", required=True)
    parser.add_argument("--n-min", type=int, required=True)
    parser.add_argument("--n-max", type=int, required=True)
    args = parser.parse_args()

    selected_qs = {int(value) for value in args.qs.split(",") if value}
    with args.input.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        if fieldnames is None:
            raise ValueError("input CSV has no header")
        rows = [
            row
            for row in reader
            if int(row["q"]) in selected_qs
            and args.n_min <= int(row["n"]) <= args.n_max
        ]

    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    aggregate: dict[str, dict[str, int]] = defaultdict(
        lambda: {"FOUND": 0, "NONE": 0}
    )
    for row in rows:
        aggregate[f"q={row['q']}:{row['family']}"][row["verdict"]] += 1

    none_rows = [row for row in rows if row["verdict"] == "NONE"]
    literal_breaks = [cell(row) for row in none_rows if not literal_claim(row)]
    literal_confirmations = [cell(row) for row in none_rows if literal_claim(row)]
    claimed_but_found = [
        cell(row) for row in rows if row["verdict"] == "FOUND" and literal_claim(row)
    ]
    generalized_power_two = [
        cell(row) for row in none_rows if power_two_extension(row)
    ]

    result = {
        "input": str(args.input),
        "output": str(args.output),
        "q_values": sorted(selected_qs),
        "n_range": [args.n_min, args.n_max],
        "rows": len(rows),
        "found": sum(row["verdict"] == "FOUND" for row in rows),
        "none": len(none_rows),
        "aggregate": dict(aggregate),
        "none_cells": [cell(row) for row in none_rows],
        "literal_claim_confirmations": literal_confirmations,
        "literal_claim_breaks": literal_breaks,
        "literal_claim_expected_but_found": claimed_but_found,
        "power_of_two_extension_none_cells": generalized_power_two,
    }
    args.summary.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
