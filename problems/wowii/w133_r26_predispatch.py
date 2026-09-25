#!/usr/bin/env python3
"""
w133 r26 -- PRE-DISPATCH CHECK on the verification-gate brief.  Its exit code is chained
AHEAD of the dispatch command: no clearance, no call.

Two things it does that a string probe cannot:

  * RULING CP -- IT ASSERTS COMPLETENESS RATHER THAN PROBING FOR ABSENCE.  The populations
    (key rows, held-out hosts, import sites) are ENUMERATED and asserted contiguous/complete.
    An item written in an encoding the scanner misses opens a HOLE, and a hole is visible.
    String probes are still printed, but as EVIDENCE, labelled as such, with RAW and
    NORMALISED counts both shown.

  * DERIVABILITY, NOT OCCURRENCE.  A held-out answer here is a small integer; asking whether
    "6" occurs in a 36 KB brief is meaningless.  The real question is whether the brief
    DETERMINES the answer without the reviewer doing the row's work.  So every row carries an
    explicit audit of what the brief constrains it to, and a row whose constraint set has a
    single member is STRUCK by the owner before dispatch, not scored.
"""
import os, re, sys, unicodedata

BRIEF = os.path.expanduser("~/workspace/claudecode/automath-sandbox/briefs/w133_r26_chain.md")
KEY = "problems/wowii/w133_r26_key.key.txt"
DRAFT = "notes/proofs/wowii133_draft.md"

FAIL = []
N = 0
def ck(label, cond, detail=""):
    global N
    N += 1
    print("  [%s] %-64s %s" % ("OK" if cond else "FAIL", label, detail))
    if not cond:
        FAIL.append(label)

text = open(BRIEF, encoding="utf-8").read()
norm = unicodedata.normalize("NFKC", text)
key_lines = [l.rstrip("\n") for l in open(KEY, encoding="utf-8")]
hosts = {}
rows = []
for l in key_lines:
    if " edges: " in l:
        nm, e = l.split(" edges: ")
        hosts[nm.strip()] = e.strip()
    p = l.split("\t")
    if len(p) == 4 and p[0].startswith("V"):
        rows.append(p)

print("=" * 84)
print("PART A -- POPULATIONS ENUMERATED AND ASSERTED COMPLETE (RULING CP)")
print("=" * 84)

# --- key-row population: contiguity, not absence
ids = [r[0] for r in rows]
expect = ["V%d" % i for i in range(1, len(rows) + 1)]
ck("key row population is CONTIGUOUS V1..V%d, %d distinct, 0 holes" % (len(rows), len(rows)),
   ids == expect and len(set(ids)) == len(ids), "ids=%s" % ",".join(ids))
ck("every key row appears in the brief's tier table exactly once",
   all(text.count("| **%s** |" % r[0]) == 1 for r in rows),
   "counts=%s" % [text.count("| **%s** |" % r[0]) for r in rows])
ck("every key row's TIER is disclosed and matches the key",
   all(("| **%s** | **%s** |" % (r[0], r[1])) in text for r in rows))

# --- host population: each printed exactly once, and confined to PART 0
i_part1 = text.index("# PART 1 —")
part0, rest = text[:i_part1], text[i_part1:]
ck("held-out host population is complete: K1,K2,K3,K4 all present, 4 distinct, 0 holes",
   sorted(hosts) == ["K1", "K2", "K3", "K4"], "hosts=%s" % sorted(hosts))
for nm, e in sorted(hosts.items()):
    ck("%s edge list printed EXACTLY ONCE in the brief" % nm, text.count(e) == 1,
       "count=%d" % text.count(e))
    ck("%s is never NAMED outside PART 0 (no mathematical role)" % nm,
       rest.count(nm) == 0 or nm in ("K1",) and False, "occurrences after PART 1 = %d" % rest.count(nm))

# --- import-site population: guards at every import (RULING AZ)
IMPORTS = ["G54", "G55", "G57", "§34.4a", "the definition of `a`"]
blocks = re.findall(r"\*\*IMPORT \d+ —(.+?)(?=\n\n\*\*IMPORT|\n\*\*A GUARD THAT CANNOT MOVE)",
                    text, re.S)
ck("import-site population ENUMERATED: 5 IMPORT blocks, 0 holes", len(blocks) == 5,
   "found=%d" % len(blocks))
for i, b in enumerate(blocks, 1):
    has_guard = ("GUARD AT THIS IMPORT SITE" in b) or ("silently change" in b)
    has_hyp = ("Hypotheses" in b) or ("hypotheses" in b) or ("C4-free" in b)
    ck("IMPORT %d carries its GUARD at the import site" % i, has_guard)
    ck("IMPORT %d restates its HYPOTHESES in place" % i, has_hyp)
ck("the guard that CANNOT move is declared in place, not hidden",
   "A GUARD THAT CANNOT MOVE" in text and "does not pretend you can" in text)

print()
print("=" * 84)
print("PART B -- DERIVABILITY LEAK CHECK (not occurrence).  For each row: what does the brief")
print("          CONSTRAIN the answer to?  A row the brief pins to ONE value is STRUCK.")
print("=" * 84)
# constraint audit, written by hand against the brief's own claims, one entry per row.
# n_consistent = how many values remain consistent with everything the brief states.
AUDIT = {
 "V1": ("edge count of a graph the brief makes no claim about", 999),
 "V2": ("a degree; the brief's G58 bounds W_1 degrees by 4 but K1 carries no class claim", 5),
 "V3": ("which of FOUR printed graphs has a C4; the decoy makes this un-guessable "
        "(a reviewer who assumes all four are in hypothesis answers NONE and is wrong)", 5),
 "V4": ("a 4-tuple census; |W_cons|<=3 and |W_anti|<=3 are stated but pin nothing", 999),
 "V5": ("an a-value; G58's a<=3 is stated for class members, K1 is not claimed to be one", 4),
 "V6": ("longest induced path of the DECOY, which is out of class, so no stated bound applies", 999),
 "V7": ("(T_Z, sum_Z charge); the brief states the G55 identity RELATING them, so a reviewer "
        "who computes one can get the other -- that is doing the work, not a leak", 999),
 "V8": ("(sum charge, n_3); (Z1)/(Z6) bound both but pin neither", 999),
 "V9": ("(T_Z, sum charge) on a third host; same status as V7", 999),
}
ck("every key row has a derivability audit entry, 0 holes",
   sorted(AUDIT) == sorted(ids), "audited=%s" % sorted(AUDIT))
struck = []
for rid, tier, q, ans in rows:
    why, ncons = AUDIT[rid]
    if ncons <= 1:
        struck.append(rid)
    print("  [%s] %s  n_consistent=%s  %s" % ("OK" if ncons > 1 else "STRUCK", rid, ncons, why))
ck("no row is pinned to a single value by the brief (0 struck)", not struck, "struck=%s" % struck)

print()
print("  EVIDENCE ONLY (RULING CP: these are probes, NOT the check) -- literal answer strings,")
print("  raw and NFKC-normalised counts both shown.  A hit is not automatically a leak: these")
print("  are small integers and the brief is 36 KB of mathematics.")
for rid, tier, q, ans in rows:
    s = str(ans)
    print("    %s  answer=%-26s raw=%-4d normalised=%-4d" % (rid, s, text.count(s), norm.count(s)))

print()
print("=" * 84)
print("PART C -- BRIEF INTEGRITY")
print("=" * 84)
d = open(DRAFT, encoding="utf-8").readlines()
for lo, hi, nm in ((4592, 4717, "§35 / G58"), (4793, 4897, "§36 / G59"), (5005, 5093, "§37")):
    seg = "".join(d[lo - 1:hi])
    ck("%s is shipped VERBATIM from the draft (byte-for-byte)" % nm, seg in text,
       "%d bytes" % len(seg.encode()))
ck("no API key material anywhere in the brief",
   not re.search(r"(sk-[A-Za-z0-9\-_]{12,}|OR_KEY|OC_GO_KEY|Bearer\s+\S{12,})", text))
ck("no private email in the brief", "@gmail.com" not in text and "chenhaoyu" not in text)
ck("escape hatch present on EVERY tier (CANNOT COMPUTE accepted, Tier H included)",
   "CANNOT COMPUTE" in text and "Tier H included" in text)
ck("partial-answer escape hatch present ((P2)/(P3) NOT ATTEMPTED)", "NOT ATTEMPTED" in text)
ck("LOW FAN-IN: exactly one PRIMARY question, two explicitly ranked below it",
   text.count("THE PRIMARY QUESTION") == 1 and "(P2)" in text and "(P3)" in text)
ck("a located GAP is declared the SUCCESS case, in the brief",
   "A LOCATED GAP IS THE BEST OUTCOME" in text)
ck("the three BW controls are shipped, all three, in the author's own words",
   all(k in text for k in ("True but not sharp", "A claim inverted",
                           "A hand argument that DISPROVED a true theorem")))
ck("pre-stated refusals shipped (n-bound refusal; W_1=∅ refusal; counterexample grading)",
   all(k in text for k in ("is refused without being read on its merits",
                           "is refuted before it is read", "most-basic-first")))
ck("deliverable word cap stated", "about 1200 words" in text)
ck("held-out table is declared TEST-ONLY with no mathematical role",
   "TEST GRAPHS ONLY" in text and "nothing below asks" in text)
flat = " ".join(text.split())
ck("the decoy is disclosed as a decoy WITHOUT naming which graph it is",
   "One of the four is deliberately NOT in the class" in flat.replace("**", "")
   and "K4 is the decoy" not in flat)
ck("brief is self-contained: no file path a reviewer would need to open",
   "problems/wowii/w133_r26" not in text)

print()
print("CHECKS RUN: %d   FAILURES: %d" % (N, len(FAIL)))
if FAIL:
    print("VERDICT: DISPATCH BLOCKED -- %s" % FAIL)
    sys.exit(2)
print("VERDICT: DISPATCH CLEARED")
sys.exit(0)
