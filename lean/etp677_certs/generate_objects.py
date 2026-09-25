#!/usr/bin/env python3
"""Regenerate the four Lean literal modules from the ticket's JSON objects."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "ETP677Certs"

OBJECTS = (
    ("R45L02", 3, "problems/etp677/R45_L02_q3_3perf_delta0.json", [4, 6, 10],
     "r45_l02_q3_certificate"),
    ("L03", 3, "problems/etp677/L03_q3_four_perfect_delta0.json", [4, 5, 6, 10],
     "l03_q3_four_perfect_certificate"),
    ("L05", 4, "problems/etp677/L05/L05_q4_P6_delta0.json", [0, 1, 2, 5, 15, 17],
     "l05_q4_p6_certificate"),
    ("L06", 7, "problems/etp677/L06/L06_q7_P14_delta0_best.json",
     [0, 4, 5, 6, 10, 13, 14, 15, 16, 21, 23, 31, 37, 39],
     "l06_q7_p14_certificate"),
)


def lean(value: object) -> str:
    return json.dumps(value, separators=(", ", ": "))


def module(name: str, q: int, source: str, rows: list[int], theorem: str) -> str:
    data = json.loads((ROOT / source).read_text())
    return f'''import ETP677Certs.Core

namespace ETP677Certs.{name}

/-- Literal transcription of `{source}`. -/
def object : Object := {{
  q := {q}
  table := {lean(data["table"])}
  lines := {lean(data["lines"])}
  nu := {lean(data["nu"])}
}}

theorem {theorem} : Certificate object {lean(rows)} := by
  change branchObjectB object = true ∧
    {lean(rows)}.all (perfectB object) = true ∧ deltaZeroB object = true
  native_decide

end ETP677Certs.{name}
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for args in OBJECTS:
        name = args[0]
        (OUT / f"{name}.lean").write_text(module(*args))


if __name__ == "__main__":
    main()
