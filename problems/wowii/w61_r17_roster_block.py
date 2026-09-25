#!/usr/bin/env python3
"""
owner-w61 round 17 -- the brief-ready PRINTED roster for nu = 7..10.

SS7.31 (e) recorded the cost of the nu <= 10 fold: "No roster is printed for
nu = 7..10 ... Family 2's brief must print the nu = 7..10 rosters or the fold is
unreviewable."  Planner RW61-1(b) and RW61-6(3) both name this block as the
artifact the family-2 brief is blocked on.  This script emits it.

Rows are grouped by (E, e, lambda) with the surviving L values listed, because
survivors come in L-runs and the grouped form is COMPLETE, materially shorter,
and shows the structure (same residue, consecutive L) that the ungrouped list
hides.  A round-trip assertion re-expands the grouping and checks it against the
flat roster before anything is written, so the compression cannot lose a row.

ONE PRODUCT: problems/wowii/w61_r17_roster_nu7_10.md
"""

import sys

src = open("problems/wowii/w61_r17_roster_recompute.py").read()
rec = {}
exec(compile(src.replace('if __name__ == "__main__":', 'if False:'),
             "w61_r17_roster_recompute.py", "exec"), rec)
steps, partitions, p_euler = rec["steps"], rec["partitions"], rec["p_euler"]
s0, fmt_part, fan6_cert = rec["s0"], rec["fmt_part"], rec["fan6_cert"]
fan6_kills = rec["fan6_kills"]

OUT = "problems/wowii/w61_r17_roster_nu7_10.md"
out = []
grand_flat = 0

out.append("**(c-8) The `ν = 7…10` rosters, printed in full.** Same specification as")
out.append("(c-1), four steps outside the range (c-2)–(c-4) print. Produced by the")
out.append("round-17 **independent recomputation** `w61_r17_roster_recompute.py` →")
out.append("`.out`, whose `ν ≤ 6` output was diffed **both directions** against the")
out.append("prior machine roster and against the printed roster of (c-2)–(c-4) with")
out.append("**zero** differences (`w61_r17_roster_diff.out`).")
out.append("")

for nu in range(7, 11):
    two = 2 * nu
    parts = list(partitions(two))
    tail = [l for l in parts if s0(l) == l[0]]
    bd, bd_pairs = [], 0
    for lam in parts:
        for L in range(nu + 1, lam[0]):
            bd_pairs += 1
            if steps([L] * (L + 1) + list(lam)) == L:
                bd.append((L, lam))
    flat = []
    tested = 0
    for E in range(1, nu):
        eparts, lparts = list(partitions(E)), list(partitions(two - E))
        for L in range(nu + 1, two - E + 1):
            for e in eparts:
                cp = [L + x for x in e] + [L] * (L + 1 - len(e))
                for lam in lparts:
                    tested += 1
                    if steps(cp + list(lam)) == L:
                        flat.append((L, E, e, lam))
    grand_flat += len(flat)
    S = sum((nu - E) * p_euler(E) * p_euler(two - E) for E in range(1, nu))
    assert S == tested

    groups = {}
    for L, E, e, lam in flat:
        groups.setdefault((E, e, lam), []).append(L)
    # round-trip: the grouping must re-expand to exactly the flat roster
    back = {(L, E, e, lam) for (E, e, lam), Ls in groups.items() for L in Ls}
    assert back == set(flat) and len(flat) == sum(len(v) for v in groups.values())

    out.append("> **`ν = %d`** — `p(%d) = %d`; `S(%d) = %d` shapes with `E ≥ 1`;"
               % (nu, two, len(parts), nu, S))
    out.append("> `E = 0` TAIL survivor **`[%s]`** and nothing else; `%d` boundary pairs"
               % (fmt_part(tail[0]), bd_pairs))
    out.append("> `ν+1 ≤ L < λ₁` with `%d` survivors; `%d` `E ≥ 1` survivors."
               % (len(bd), len(flat)))
    out.append(">")
    out.append("> *Boundary survivors, with FAN-6′ certificate `(w, 2nd)`:* "
               + " · ".join("`(%d, [%s])` (%d,%d)" % (L, fmt_part(l), *fan6_cert(l))
                            for L, l in bd))
    out.append(">")
    out.append("> *`E ≥ 1` survivors, grouped by `(E, e, λ)` with the surviving `L`"
               " values; `e` lists the positive escape parts only:*")
    out.append(">")
    for (E, e, lam), Ls in sorted(groups.items()):
        out.append("> `E%d e=%s λ=%s` — `L ∈ {%s}` (%d,%d)"
                   % (E, fmt_part(e), fmt_part(lam),
                      ",".join(str(x) for x in sorted(Ls)), *fan6_cert(lam)))
    misses = [r for r in flat if not fan6_kills(r[3])] \
        + [r for r in bd if not fan6_kills(r[1])] \
        + [l for l in tail if not fan6_kills(l)]
    out.append(">")
    out.append("> **Every `(w, 2nd)` above has a unique max `w` with `2nd ≤ w−2`, so"
               " Lemma FAN-6′ kills every survivor at `ν = %d`. Misses: %d.**"
               % (nu, len(misses)))
    out.append("")
    assert not misses

out.append("**Reading.** `%d` `E ≥ 1` survivors across `ν = 7…10`, inside"
           % grand_flat)
out.append("`3 340 + 8 457 + 20 126 + 45 450 = 77 373` shapes, plus `16` boundary")
out.append("survivors inside `427` boundary pairs, plus the four single-part `E = 0`")
out.append("survivors — **and Lemma FAN-6′ kills every one of them**. The `ν ≤ 10`")
out.append("fold is now printed data at every `ν`, not an unreviewable citation.")

open(OUT, "w").write("\n".join(out) + "\n")
print("wrote %s  (%d grouped lines, %d flat survivor rows, %d chars)"
      % (OUT, len(out), grand_flat, sum(len(x) + 1 for x in out)))
