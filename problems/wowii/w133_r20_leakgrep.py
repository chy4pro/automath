#!/usr/bin/env python3
"""w133_r20_leakgrep.py — BLOCKING pre-dispatch gate for the round-20 P7G32 brief.

RULING V / DEBT-5: a held-out answer printed anywhere else in the brief is a leak, and the
round-18 failure (T8/T9 burned by a worked example in a section written for another purpose)
is what this exists to stop.  Exit code is non-zero on any BLOCKING failure, and the dispatch
command is chained behind it, so the gate cannot be forgotten.

RULING W: the brief must refuse the n-route by NAME and REGISTRY LOCATION only; none of
G49's data may appear.

NEW THIS ROUND (advisory, non-blocking) — the RESIDUAL-GUESSABILITY audit.  Round 19's grep
asked "is the answer stated about the held-out graph?"  It did not ask "does the answer VALUE
appear anywhere in the brief attached to any graph?"  A value printed about a different graph
is not a leak, but it lowers the cost of a lucky guess, and the honest thing is to measure it
and put the number on the ledger rather than to let a clean BLOCKING pass imply it is zero.

Self-limit 120s.
"""
import sys, re, time, os

T0 = time.time()
BRIEF = sys.argv[1] if len(sys.argv) > 1 else \
    "$HOME/workspace/claudecode/automath-sandbox/briefs/w133_r20_P7G32.md"
KEY = "$HOME/workspace/claudecode/automath/problems/wowii/w133_r19_p7g32_key.key.txt"

BLOCK = []
ADVIS = []
N = [0]


def check(label, cond, extra="", blocking=True):
    N[0] += 1
    if time.time() - T0 > 120:
        print("SELF-LIMIT EXCEEDED")
        sys.exit(2)
    if cond:
        print(f"  PASS  {label}" + (f"   [{extra}]" if extra else ""))
    else:
        tag = "FAIL " if blocking else "ADVIS"
        print(f"  {tag} {label}" + (f"   [{extra}]" if extra else ""))
        (BLOCK if blocking else ADVIS).append(label)


text = open(BRIEF, encoding="utf-8").read()
lines = text.split("\n")
# Markdown hard-wraps split phrases across lines ("Do not use a SAT / newline / solver.").
# Phrase-presence checks run on the whitespace-normalised text; the leak checks
# below deliberately stay line-oriented, because a leak is a LINE-level event.
flat = re.sub(r"\s+", " ", text)

# key rows: id, tier, graph, question, answer
rows = []
for ln in open(KEY, encoding="utf-8"):
    ln = ln.rstrip("\n")
    if not ln.strip():
        continue
    parts = ln.split("\t")
    if len(parts) >= 5:
        rows.append(parts[:5])

print("=" * 78)
print(f"[0] INPUTS   brief={os.path.basename(BRIEF)}  {len(text)} B   key rows={len(rows)}")
print("=" * 78)
check("brief file is non-empty and >5 KB", len(text) > 5000, f"{len(text)} B")
check("key has exactly 9 rows V1..V9", len(rows) == 9 and [r[0] for r in rows] ==
      [f"V{i}" for i in range(1, 10)], str([r[0] for r in rows]))

# ---- locate PART 6 ----
p6 = None
for i, ln in enumerate(lines):
    if ln.startswith("# PART 6"):
        p6 = i
check("PART 6 header found", p6 is not None, f"line {p6}")
before = "\n".join(lines[:p6])
after = "\n".join(lines[p6:])

print()
print("=" * 78)
print("[1] BLOCKING — the two held-out graphs must not be mentioned before PART 6")
print("=" * 78)
# The brief renames the key's N1/N2 to X1/X2.  Check BOTH labels, in both directions.
for tok in ["X1", "X2", "N1", "N2"]:
    cnt = len(re.findall(r"\b" + tok + r"\b", before))
    check(f"token {tok} appears 0 times before PART 6", cnt == 0, f"count={cnt}")

print()
print("=" * 78)
print("[2] BLOCKING — no held-out ANSWER is stated as a fact about its own graph, anywhere")
print("=" * 78)
gmap = {"N1": ["X1", "N1"], "N2": ["X2", "N2"]}
for rid, tier, graph, q, ans in rows:
    labels = gmap[graph]
    bad = []
    for ln in lines:
        if not any(re.search(r"\b" + L + r"\b", ln) for L in labels):
            continue
        # a line mentioning the graph AND asserting the answer with an = or "is"
        if re.search(r"\b" + re.escape(ans) + r"\b", ln) and re.search(r"=|\bis\b|:", ln):
            # the table row itself asks the question; it must not contain the answer
            bad.append(ln.strip()[:90])
    check(f"{rid} answer '{ans}' never asserted about {graph} anywhere in the brief",
          not bad, " | ".join(bad[:2]))

print()
print("=" * 78)
print("[3] BLOCKING — the PART 6 table asks, and does not answer")
print("=" * 78)
tbl = [ln for ln in after.split("\n") if ln.startswith("| **V")]
check("all 9 table rows present", len(tbl) == 9, f"{len(tbl)} rows")
for (rid, tier, graph, q, ans), ln in zip(rows, tbl):
    # A row is only leaking if it ASSERTS the answer, not if the token happens to occur
    # as an answer-FORMAT prompt ("YES or NO") or as a vertex label inside a set.
    probe = re.sub(r"YES or NO", "", ln)          # answer-format prompt, not an answer
    probe = re.sub(r"\{[^}]*\}", "{}", probe)      # vertex sets: labels are not answers
    probe = re.sub(r"`[^`]*\((?:[^`)]*)\)`", "``", probe)  # a(6), path(X1): args are not answers
    # NOTE (V7 fault-3 finding, round 20): the right-hand lookahead used to be `(?![\w.])`,
    # which made a sentence-final "which is 2." INVISIBLE — the period matched the exclusion.
    # `.` is excluded only when a DIGIT follows it (a decimal), never at end of sentence.
    leaking = re.search(r"(?<![\w.])" + re.escape(ans) + r"(?!\d)(?!\.\d)", probe) and \
        re.search(r"=|\bis\b(?! it)", probe)
    check(f"{rid} row asserts no answer (format prompts and vertex labels excluded)",
          not leaking, probe.strip()[:70])
    check(f"{rid} row declares its tier {tier}", f"| {tier} |" in ln, ln.strip()[:40])

print()
print("=" * 78)
print("[4] BLOCKING — RULING W: G49 by name and location only, none of its data")
print("=" * 78)
check("brief cites G49 by name", "G49" in text)
check("brief cites G49's registry location", "28.2" in text)
check("brief states G49's CONCLUSION", re.search(r"unbounded", text) is not None)
# the five data items round 18 printed and thereby burned T8/T9
for label, pat in [
    ("G49 family symbol", r"\bW1\b|\bH_k\b|\bmathcal\{W\}"),
    ("a size formula in n and k", r"n\s*=\s*[0-9]*\s*k\s*[\^\*+]"),
    ("an a-value sum for the family", r"Σ\s*a\s*=\s*\d{3,}|sum\s*a\s*=\s*\d{3,}"),
    ("the family's explicit vertex count", r"\bn\s*=\s*129\b"),
    ("the family's path value", r"path\s*\(\s*W1\s*\)"),
]:
    m = re.search(pat, text)
    check(f"G49 data item NOT present: {label}", m is None, m.group(0) if m else "")

print()
print("=" * 78)
print("[5] BLOCKING — harness elements the planner's conditions require")
print("=" * 78)
check("CANNOT COMPUTE appears at least 3 times (prominent)",
      text.count("CANNOT COMPUTE") >= 3, f"count={text.count('CANNOT COMPUTE')}")
check("CANNOT COMPUTE is stated to cost nothing", "costs you" in flat)
check("tiers are DISCLOSED with Tier H and Tier C explained",
      "Tier H" in text and "Tier C" in text)
check("Tier-C rows are declared not reliably hand-derivable",
      "hand-derivable" in flat)
check("word cap ~1100 stated", "1100" in text)
check("EXECUTION declaration required", "EXECUTION: NONE" in text and "EXECUTION: CODE" in text)
check("no-SAT red line stated", "SAT solver" in flat)
check("edge-list-and-validate rule present", "most basic first" in flat.lower())
check("the configuration-vs-graph trap is stated", "1112" in text)
check("no API key pattern anywhere",
      re.search(r"sk-[A-Za-z0-9_\-]{16,}", text) is None)

print()
print("=" * 78)
print("[6] BLOCKING — B6: the values the ARGUMENT needs are DISCLOSED, with witnesses")
print("=" * 78)
check("path(Q) is disclosed", re.search(r"path\(Q\)\s*=\s*6", text) is not None)
check("path(Q) ships an induced witness", "0–4–6–2–3–9" in text or "0-4-6-2-3-9" in text)
check("path(Petersen) is disclosed as 5", re.search(r"path\(Petersen\)\s*=\s*5", flat) is not None)
check("path(Petersen) ships an induced witness", "0–7–3–4–2" in text or "0-7-3-4-2" in text)
check("the round-12 fabrication is named so it cannot be re-inherited",
      "fabricated" in flat)
check("diam(Q) = 3 disclosed and the false 2 named",
      re.search(r"diam\(Q\)\s*=\s*3", flat) is not None and "not 2" in flat)
check("l(Petersen) = 3 disclosed (tightness, so no proof may give l < 3)",
      "`l = 3` exactly" in flat)
check("W-nonemptiness disclosed so B5 is enforceable",
      "W = {8}" in text or "`W = {8}" in text)

print()
print("=" * 78)
print("[7] ADVISORY (NEW) — residual guessability: does an answer VALUE appear at all?")
print("=" * 78)
print("  A value printed about a DIFFERENT graph is not a leak, but it cheapens a guess.")
print("  Measured, not assumed. These do NOT block dispatch.")
for rid, tier, graph, q, ans in rows:
    if ans in ("YES", "NO"):
        hits = len(re.findall(r"\bYES\b|\bNO\b", before))
        check(f"{rid} ('{ans}') — boolean row, prior appearances of YES/NO before PART 6",
              hits == 0, f"count={hits}", blocking=False)
        continue
    occ = []
    for ln in lines[:p6]:
        if re.search(r"(?<![\w.])" + re.escape(ans) + r"(?![\w.])", ln) and \
           re.search(r"=|\bis\b", ln):
            occ.append(ln.strip()[:80])
    check(f"{rid} ('{ans}') — value never appears as an '=' fact before PART 6",
          not occ, " | ".join(occ[:2]), blocking=False)

print()
print("=" * 78)
print(f"CHECKS: {N[0]}")
print(f"BLOCKING FAILURES: {len(BLOCK)}")
for f in BLOCK:
    print("   - " + f)
print(f"ADVISORY FLAGS:    {len(ADVIS)}")
for f in ADVIS:
    print("   ~ " + f)
print()
print("VERDICT: " + ("DISPATCH BLOCKED" if BLOCK else "DISPATCH CLEARED"))
print(f"elapsed {time.time() - T0:.1f}s")
sys.exit(1 if BLOCK else 0)
