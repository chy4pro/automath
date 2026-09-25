#!/usr/bin/env python3
"""Select AI-tractable candidate problems from the Erdos problems database.

Filter logic (derived from 2024-2026 AI-solved case analysis):
  Tier A: status in {falsifiable, verifiable, decidable}  (finite-computation problems)
  Tier B: status == open AND formalized == yes AND prize is small/none
Exclusions: problems with a green (full resolution) AI contribution in the wiki page.
Cross-ref: formal-conjectures repo Lean statement availability.
Output: JSON + markdown shortlist sorted by tractability signals.
"""
import json
import os
import re
import sys

import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_YAML = os.path.join(BASE, "erdosproblems", "data", "problems.yaml")
AI_WIKI = os.path.join(BASE, "ai_contributions.md")
FC_DIR = os.path.join(BASE, "formal-conjectures", "FormalConjectures", "ErdosProblems")
OUT_JSON = os.path.join(BASE, "candidates.json")
OUT_MD = os.path.join(BASE, "candidates.md")

TIER_A_STATES = {"falsifiable", "verifiable", "decidable"}
SMALL_PRIZE = re.compile(r"^\$?(\d+)$")


def parse_prize(p):
    """Return numeric prize in dollars, 0 if none, None if unparseable."""
    if not p or p in ("no", "none", ""):
        return 0
    m = re.search(r"\$([\d,]+)", str(p))
    if m:
        return int(m.group(1).replace(",", ""))
    return None


def load_ai_exclusions(path):
    """Numbers with green-circle (full) AI resolutions, and yellow (partial)."""
    full, partial = set(), set()
    if not os.path.exists(path):
        return full, partial
    with open(path, encoding="utf-8") as f:
        for line in f:
            nums = re.findall(r"\[#?(\d+)\]", line)
            if "\U0001F7E2" in line:  # green circle
                full.update(nums)
            elif "\U0001F7E1" in line:  # yellow circle
                partial.update(nums)
    return full, partial


def main():
    with open(PROBLEMS_YAML, encoding="utf-8") as f:
        problems = yaml.safe_load(f)
    ai_full, ai_partial = load_ai_exclusions(AI_WIKI)
    fc_available = set()
    if os.path.isdir(FC_DIR):
        for name in os.listdir(FC_DIR):
            m = re.match(r"(\d+)\.lean$", name)
            if m:
                fc_available.add(m.group(1))

    candidates = []
    for p in problems:
        num = str(p.get("number"))
        state = (p.get("status") or {}).get("state", "")
        prize = parse_prize(p.get("prize"))
        formalized = (p.get("formalized") or {}).get("state") == "yes"
        oeis = p.get("oeis") or []
        tags = p.get("tags") or []

        tier = None
        if state in TIER_A_STATES:
            tier = "A"
        elif state == "open" and formalized and (prize is not None and prize <= 500):
            tier = "B"
        if tier is None:
            continue
        if num in ai_full:
            continue  # already fully resolved by AI per wiki

        score = 0
        score += 3 if tier == "A" else 0
        score += 2 if num in fc_available else 0
        score += 2 if oeis else 0
        score += 1 if prize == 0 else 0
        score -= 1 if num in ai_partial else 0  # others already tried partially

        candidates.append({
            "number": num,
            "tier": tier,
            "state": state,
            "prize": p.get("prize") or "none",
            "formalized_statement": formalized,
            "lean_statement_in_fc": num in fc_available,
            "oeis": oeis,
            "tags": tags,
            "ai_partial_progress": num in ai_partial,
            "score": score,
            "url": f"https://www.erdosproblems.com/{num}",
        })

    candidates.sort(key=lambda c: (-c["score"], int(c["number"])))
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(candidates, f, indent=2)

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(f"# Candidate problems ({len(candidates)} total)\n\n")
        f.write(f"Excluded {len(ai_full)} AI-solved; {len(ai_partial)} have partial AI progress.\n\n")
        f.write("| # | Tier | State | Prize | Lean stmt | OEIS | Tags | Score |\n")
        f.write("|---|------|-------|-------|-----------|------|------|-------|\n")
        for c in candidates[:60]:
            f.write(
                f"| [{c['number']}]({c['url']}) | {c['tier']} | {c['state']} | {c['prize']} | "
                f"{'Y' if c['lean_statement_in_fc'] else '-'} | "
                f"{','.join(c['oeis']) if c['oeis'] else '-'} | "
                f"{', '.join(c['tags'][:3])} | {c['score']} |\n"
            )

    print(f"total problems: {len(problems)}")
    print(f"candidates: {len(candidates)} "
          f"(tier A: {sum(1 for c in candidates if c['tier'] == 'A')}, "
          f"tier B: {sum(1 for c in candidates if c['tier'] == 'B')})")
    print(f"ai_full excluded: {len(ai_full)}, ai_partial flagged: {len(ai_partial)}")
    print(f"top 15: {[c['number'] for c in candidates[:15]]}")


if __name__ == "__main__":
    sys.exit(main())
