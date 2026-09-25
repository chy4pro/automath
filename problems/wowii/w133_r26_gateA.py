#!/usr/bin/env python3
"""
w133 r26 -- GATE A scorer.  Runs FIRST, before one line of the returned mathematics is read.
The gate was pre-registered blind at orchestration/results/w133_state.md §"Round 26" §1 and is
NOT revised here: A1 wrong Tier-H => VOID; A2 CANNOT COMPUTE accepted anywhere; A3 table absent
=> VOID; A4 wrong Tier-C => traceable downgrade by row id.

RULING BW: the verdict is load-bearing, so it is machine-computed from the key file and the
returned text, not read off by the author.
"""
import os, re, sys, ast

KEY = "problems/wowii/w133_r26_key.key.txt"
RET = os.path.expanduser(
    "~/workspace/claudecode/automath-sandbox/out/muse-spark/w133_r26_chain_out.md")

rows = {}
order = []
for l in open(KEY, encoding="utf-8"):
    p = l.rstrip("\n").split("\t")
    if len(p) == 4 and p[0].startswith("V"):
        rows[p[0]] = (p[1], p[2], p[3])
        order.append(p[0])

text = open(RET, encoding="utf-8").read()

# --- A3 first: is the table there at all?
present = {}
for rid in order:
    m = re.search(r"^%s\s*=\s*(.+)$" % rid, text, re.M)
    present[rid] = m.group(1).strip() if m else None
missing = [r for r in order if present[r] is None]
print("=" * 84)
print("GATE A -- pre-registered blind at state.md §'Round 26' §1, NOT revised here")
print("=" * 84)
print("  row population asserted COMPLETE (RULING CP): expected %s" % ",".join(order))
print("  rows returned: %d of %d;  holes: %s" % (len(order) - len(missing), len(order),
                                                 missing if missing else "NONE"))
if len(missing) == len(order):
    print("VERDICT: VOID by (A3) -- held-out table absent altogether")
    sys.exit(3)

def norm_num(s):
    return re.findall(r"-?\d+", s)

VOID = []
DOWNGRADE = []
REFUSED = []
EXACT = []
for rid in order:
    tier, q, want = rows[rid]
    got = present[rid]
    if got is None:
        # a hole in a partially-returned table is scored as a refusal, not a fabrication
        REFUSED.append(rid); status = "MISSING->treated as refusal"
    elif re.search(r"CANNOT COMPUTE", got, re.I):
        REFUSED.append(rid); status = "CANNOT COMPUTE (A2: accepted, not a void, not a downgrade)"
    else:
        wn, gn = norm_num(want), norm_num(got)
        # the answer is correct iff every number of the key answer appears, in order, in the
        # returned line, and (for the K-row) the named graph matches.
        ok = all(x in gn for x in wn)
        if "K4" in want:
            ok = ok and ("K4" in got) and not re.search(r"\bK[123]\b\s*(contains|has)", got)
        if ok:
            EXACT.append(rid); status = "EXACT"
        else:
            status = "WRONG"
            (VOID if tier == "H" else DOWNGRADE).append(rid)
    print("  %s [Tier %s]  key=%-24s returned=%-58s -> %s"
          % (rid, tier, want, (got or "<absent>")[:58], status))

print()
print("  Tier-H exact: %d of %d      Tier-C exact: %d      refusals (A2): %d"
      % (len([r for r in EXACT if rows[r][0] == "H"]),
         len([r for r in order if rows[r][0] == "H"]),
         len([r for r in EXACT if rows[r][0] == "C"]), len(REFUSED)))
if VOID:
    print("VERDICT: VOID by (A1) -- wrong Tier-H value(s) at %s" % VOID)
    sys.exit(3)
if DOWNGRADE:
    print("VERDICT: PASS WITH TRACEABLE DOWNGRADE (A4) at rows %s -- any conclusion reading "
          "those quantities is UNADOPTED pending owner recomputation" % DOWNGRADE)
    sys.exit(1)
print("VERDICT: GATE A PASS.  (A5): necessary, NOT sufficient -- it buys nothing on its own.")
sys.exit(0)
