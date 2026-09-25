#!/usr/bin/env python3
"""
owner-w61 round 17 -- THE DIFF, both directions, of the round-17 independent
recomputation against every prior roster artifact on disk.

Planner ruling RW61-1(b): "code and output archived and diffed against sol's
roster", and the diff is reported even when empty.

Sources diffed (three, of two different provenances):
  MINE  problems/wowii/w61_r17_roster_recompute.out   (this round, from spec)
  SOL   problems/wowii/w61_S3_GFAN_sol_check.out      (nu<=6 roster; the artifact
                                                       current confidence rests on)
  DRAFT notes/proofs/wowii61_draft.md SS7.22 (c-2)/(c-3)/(c-4)  (the PRINTED
                                                       roster a judge actually reads)
  EXT   problems/wowii/w61_r12_gfannu_ext.out         (nu=7..10 COUNTS only --
                                                       no roster exists there, which
                                                       is exactly the gap RW61-1(b)
                                                       and task item 3 close)
Every comparison is a SET comparison in both directions: MINE\\OTHER and
OTHER\\MINE are both printed.

ONE PRODUCT: the report written to w61_r17_roster_diff.out.
"""

import re

MINE = "problems/wowii/w61_r17_roster_recompute.out"
SOL = "problems/wowii/w61_S3_GFAN_sol_check.out"
DRAFT = "notes/proofs/wowii61_draft.md"
EXT = "problems/wowii/w61_r12_gfannu_ext.out"
OUT = "problems/wowii/w61_r17_roster_diff.out"

lines = []


def rep(s=""):
    lines.append(s)


def pk(s):
    """'3+1' -> (3,1) as a canonical descending tuple."""
    s = s.strip().strip("[]`* ")
    if not s or s == "()":
        return ()
    return tuple(sorted((int(x) for x in s.split("+")), reverse=True))


# ---------------------------------------------------------------- MINE ----
mine_e1, mine_bd, mine_e0, mine_s0 = set(), set(), set(), {}
nu = None
for ln in open(MINE):
    m = re.match(r"^nu = (\d+)", ln)
    if m:
        nu = int(m.group(1))
        continue
    m = re.match(r"^\s+survivors\s+: \[(.+)\]$", ln)
    if m and nu:
        mine_e0.add((nu, pk(m.group(1))))
        continue
    if "s0 column" in ln:
        continue
    if ln.startswith("      ") and ":" in ln and "." in ln and "cert" not in ln \
            and "lambda" not in ln and nu:
        for tok in ln.strip().split(" . "):
            tok = tok.strip()
            if not tok:
                continue
            body = tok.strip("*")
            lam, val = body.rsplit(":", 1)
            mine_s0[(nu, pk(lam))] = int(val)
        continue
    m = re.match(r"^\s+survivors \(\d+\)\s+: (.+)$", ln)
    if m and nu and m.group(1).strip() != "none":
        for a, b in re.findall(r"\((\d+),\[([\d+]+)\]\)", m.group(1)):
            mine_bd.add((nu, int(a), pk(b)))
        continue
    m = re.match(r"^\s+L(\d+)\s+E(\d+) e=(\S+)\s+lambda=(\S+)", ln)
    if m and nu:
        mine_e1.add((nu, int(m.group(1)), int(m.group(2)), pk(m.group(3)), pk(m.group(4))))

# ----------------------------------------------------------------- SOL ----
sol_e1, sol_bd, sol_e0 = set(), set(), set()
nu = None
for ln in open(SOL):
    m = re.match(r"^nu=(\d+):", ln)
    if m:
        nu = int(m.group(1))
        continue
    m = re.match(r"^\s+E0 tail: \[(.*)\]", ln)
    if m and nu:
        for t in re.findall(r"'([\d+]+)'", m.group(1)):
            sol_e0.add((nu, pk(t)))
        continue
    m = re.match(r"^\s+boundary: \[(.*)\]", ln)
    if m and nu:
        for a, b in re.findall(r"\((\d+), '([\d+]+)'", m.group(1)):
            sol_bd.add((nu, int(a), pk(b)))
        continue
    m = re.match(r"^\s+L(\d+) E(\d+) e=(\S+) lambda=(\S+) steps=", ln)
    if m and nu:
        sol_e1.add((nu, int(m.group(1)), int(m.group(2)), pk(m.group(3)), pk(m.group(4))))

# --------------------------------------------------------------- DRAFT ----
txt = open(DRAFT).read()
c4 = txt[txt.index("**(c-4) The `E ≥ 1` rows"):txt.index("**(c-5) What a re-reader")]
parts = re.split(r"\*\*ν = (\d+)\*\* \(\d+\):", c4)
draft_e1 = set()
for i in range(1, len(parts), 2):
    n = int(parts[i])
    for a, b, c, d in re.findall(r"L(\d+) E(\d+) e=([\d+]+) λ=([\d+]+)", parts[i + 1]):
        draft_e1.add((n, int(a), int(b), pk(c), pk(d)))

# (c-2) printed s0 column
c2 = txt[txt.index("**(c-2) The `E = 0` column"):txt.index("**(c-3) The `E = 0` boundary")]
c2 = c2[:c2.index("**Reading.**")]   # the prose after the last token is not data
draft_s0 = {}
parts = re.split(r"\*\*ν = (\d+)\*\* — `p\(\d+\) = \d+`:", c2)
for i in range(1, len(parts), 2):
    n = int(parts[i])
    body = parts[i + 1].replace("\n>", " ").replace("\n", " ")
    for tok in body.split("·"):
        tok = tok.strip().strip(">").strip()
        mm = re.match(r"^\*{0,2}([\d+]+):(\d+)\*{0,2}$", tok)
        if mm:
            draft_s0[(n, pk(mm.group(1)))] = int(mm.group(2))

# (c-3) printed boundary survivors
c3 = txt[txt.index("**(c-3) The `E = 0` boundary"):txt.index("**(c-4) The `E ≥ 1` rows")]
draft_bd = set()
draft_bd_pairs = {}
for ln in c3.splitlines():
    if not ln.startswith("|"):
        continue
    cells = [c.strip() for c in ln.strip("|").split("|")]
    if len(cells) < 3 or not cells[0].isdigit():
        continue
    n = int(cells[0])
    draft_bd_pairs[n] = int(cells[1])
    for a, b in re.findall(r"\((\d+), \[([\d+,\s]+)\]\)", cells[2]):
        draft_bd.add((n, int(a), pk(b.replace(",", "+").replace(" ", ""))))

# ----------------------------------------------------------------- EXT ----
ext = {}
for ln in open(EXT):
    c = [x.strip() for x in ln.split("|")]
    if len(c) >= 9 and c[0].isdigit():
        ext[int(c[0])] = (int(c[3]), int(c[4]), int(c[6]), int(c[7]))


# ---------------------------------------------------------------- diff ----
def both_ways(name, a, b, aname="MINE", bname="OTHER"):
    only_a = sorted(a - b)
    only_b = sorted(b - a)
    rep("  %-46s |%s| = %-6d |%s| = %-6d" % (name, aname, len(a), bname, len(b)))
    rep("      %s \\ %s : %s" % (aname, bname, only_a if only_a else "EMPTY"))
    rep("      %s \\ %s : %s" % (bname, aname, only_b if only_b else "EMPTY"))
    return len(only_a) + len(only_b)


fail = 0
rep("=== owner-w61 round 17 -- ROSTER DIFF, BOTH DIRECTIONS (planner RW61-1(b)) ===")
rep()
rep("A. nu <= 6 -- the 72-in-1745 obligation.  MINE vs SOL")
rep("   (sol = w61_S3_GFAN_sol_check.out, the artifact current confidence rests on;")
rep("    its .py was NOT read while w61_r17_roster_recompute.py was written)")
m6 = {x for x in mine_e1 if x[0] <= 6}
fail += both_ways("E>=1 survivor roster", m6, sol_e1, "MINE", "SOL")
fail += both_ways("E=0 TAIL survivors", {x for x in mine_e0 if x[0] <= 6}, sol_e0, "MINE", "SOL")
fail += both_ways("E=0 boundary survivors", {x for x in mine_bd if x[0] <= 6}, sol_bd, "MINE", "SOL")
rep()
rep("B. nu <= 6 -- MINE vs the DRAFT's PRINTED roster (SS7.22 (c-2)/(c-3)/(c-4)),")
rep("   i.e. the text a judge actually reads, parsed straight out of the draft")
fail += both_ways("E>=1 survivor roster", m6, draft_e1, "MINE", "DRAFT")
fail += both_ways("E=0 boundary survivors", {x for x in mine_bd if x[0] <= 6}, draft_bd, "MINE", "DRAFT")
bad_s0 = sorted(k for k in set(mine_s0) | set(draft_s0)
                if k[0] <= 6 and mine_s0.get(k) != draft_s0.get(k))
rep("  %-46s printed = %-6d recomputed = %-6d"
    % ("s0 column, all 159 printed values",
       len([k for k in draft_s0 if k[0] <= 6]),
       len([k for k in mine_s0 if k[0] <= 6])))
rep("      value mismatches : %s" % (bad_s0 if bad_s0 else "EMPTY"))
fail += len(bad_s0)
rep()
rep("C. nu = 7..10 -- the 910-in-77373 obligation.")
rep("   NO ROSTER EXISTS ANYWHERE ON DISK for this range: sol never covered it and")
rep("   w61_r12_gfannu_ext.out prints COUNTS only.  So the diff here is a count diff")
rep("   against EXT, and the round-17 run is the first printed roster.")
mine_counts = {}
for ln in open(MINE):
    c = [x.strip() for x in ln.split("|")]
    if len(c) >= 8 and c[0].isdigit():
        mine_counts[int(c[0])] = (int(c[2]), int(c[3]), int(c[4]), int(c[5]))
rep("  nu |   EXT: bdpair bdsurv  tested surv |  MINE: bdpair bdsurv  tested surv | agree?")
for n in range(7, 11):
    g, h = ext[n], mine_counts[n]
    ok = g == h and h[1] == len([x for x in mine_bd if x[0] == n]) \
        and h[3] == len([x for x in mine_e1 if x[0] == n])
    rep("  %2d |      %6d %6d %7d %4d |       %6d %6d %7d %4d | %s"
        % (n, g[0], g[1], g[2], g[3], h[0], h[1], h[2], h[3],
           "AGREE" if ok else "*** DIFF ***"))
    if not ok:
        fail += 1
rep()
rep("D. printed-roster count for nu = 7..10, produced this round : %d rows"
    % len([x for x in mine_e1 if x[0] >= 7]))
rep()
rep("DIFF_FAILURE_COUNT = %d" % fail)

with open(OUT, "w") as fh:
    fh.write("\n".join(lines) + "\n")
print("wrote %s  (DIFF_FAILURE_COUNT=%d)" % (OUT, fail))
