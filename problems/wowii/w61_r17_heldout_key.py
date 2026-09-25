#!/usr/bin/env python3
"""
owner-w61 round 17 -- the Q36 held-out key, at nu = 11.

WHY nu = 11: SS7.31 (f) -- after the nu <= 10 fold every value at nu <= 10 is
BURNED (45/75/120/187, 3 340/8 457/20 126/45 450, 75/137/251/447 all reach the
next brief), so the key must live strictly above the folded range.  Task book
item 3 and planner RW61-6 both say "nu >= 11".

OPS-3 (planner): a held-out table needs >= 2 genuinely HAND-derivable rows AND
>= 2 genuinely NON-hand-derivable rows.  SS7.31 (b) records that the r15 key was
5-for-5 hand-derivable and that its own claim that G2/G5 "require actually
running the process" was EMPIRICALLY REFUTED -- a no-execution judge printed the
full 11-step Havel-Hakimi trajectory for both.  So "one trajectory on a
13-entry list" is HAND, and this key classifies it as HAND.  The
non-hand-derivable rows are therefore chosen to be things no hand can do:
  * H3 -- a survivor COUNT over 98 384 enumerated shapes, WITH its per-E split
  * H4 -- a histogram bucket over all 1 002 partitions of 22, i.e. 1 002
          separate Havel-Hakimi runs before the first digit can be written
Neither is extrapolable from the published sequences: the published survivor
counts 0,1,4,9,20,38,75,137,251,447 have no closed form in this document, and
an extrapolation is graded WRONG, not partially right.

SELF-CALIBRATION (mandatory, r15 pattern): the generator reproduces the PRINTED
nu <= 10 data from the draft BEFORE computing a single held-out value, and
aborts without writing on any mismatch.

THE KEY IS NOT PASTED INTO ANY BRIEF.  ONE PRODUCT: w61_r17_heldout_key.txt.
"""

import time
# load the round-17 recomputation as a library, without running its main()
src = open("problems/wowii/w61_r17_roster_recompute.py").read()
rec = {}
exec(compile(src.replace('if __name__ == "__main__":', 'if False:'),
             "w61_r17_roster_recompute.py", "exec"), rec)
steps, partitions, p_euler = rec["steps"], rec["partitions"], rec["p_euler"]
s0, fmt_part = rec["s0"], rec["fmt_part"]

T0 = time.time()
LIMIT = 900.0
OUT = "problems/wowii/w61_r17_heldout_key.txt"

# ---------------------------------------------------------------- CALIBRATION
# every one of these is PRINTED in the draft (SS7.22 (c-2)/(c-3)/(c-4),
# SS7.25 (c)) and therefore may be used to calibrate but never as a held-out.
PUB_BD_PAIRS = [0, 1, 3, 7, 14, 26, 45, 75, 120, 187]
PUB_BD_SURV = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
PUB_S = [0, 3, 24, 110, 397, 1211, 3340, 8457, 20126, 45450]
PUB_SURV = [0, 1, 4, 9, 20, 38, 75, 137, 251, 447]
PUB_S0_NU6 = {  # a spot slice of the printed (c-2) column at nu = 6
    (12,): 12, (11, 1): 12, (6, 6): 7, (4, 4, 4): 6, (3, 3, 3, 3): 6,
    (2,) * 6: 6, (1,) * 12: 7,
}

cal = []
ok = True
for nu in range(1, 11):
    two = 2 * nu
    parts = list(partitions(two))
    tail = [l for l in parts if s0(l) == l[0]]
    bp = sum(max(0, l[0] - nu - 1) for l in parts)
    bs = sum(1 for l in parts for L in range(nu + 1, l[0])
             if steps([L] * (L + 1) + list(l)) == L)
    S = sum((nu - E) * p_euler(E) * p_euler(two - E) for E in range(1, nu))
    good = (tail == [(two,)] and bp == PUB_BD_PAIRS[nu - 1]
            and bs == PUB_BD_SURV[nu - 1] and S == PUB_S[nu - 1])
    ok = ok and good
    cal.append("  nu=%-2d  E0surv=%-6s bdpairs=%-4d(pub %-4d) bdsurv=%d(pub %d) "
               "S=%-6d(pub %-6d)  %s"
               % (nu, "[%s]" % fmt_part(tail[0]) if tail else "none",
                  bp, PUB_BD_PAIRS[nu - 1], bs, PUB_BD_SURV[nu - 1],
                  S, PUB_S[nu - 1], "PASS" if good else "*** FAIL ***"))
for lam, v in sorted(PUB_S0_NU6.items()):
    got = s0(lam)
    good = got == v
    ok = ok and good
    cal.append("  s0([%s]) = %d (printed %d)  %s"
               % (fmt_part(lam), got, v, "PASS" if good else "*** FAIL ***"))
# survivor counts nu<=10, from the round-17 recomputation (already diffed clean
# against sol AND against the printed roster -- w61_r17_roster_diff.out)
if not ok:
    raise SystemExit("CALIBRATION FAILED -- no key written\n" + "\n".join(cal))

# ------------------------------------------------------------------ nu = 11
NU = 11
TWO = 22
parts22 = list(partitions(TWO))
assert len(parts22) == p_euler(TWO) == 1002

# H1 (HAND) -- four independent s0 values, one Havel-Hakimi run each.
H1_LAMS = [(12, 6, 4), (9, 7, 3, 3), (14, 5, 2, 1), (8, 8, 6)]
H1 = [(l, s0(l)) for l in H1_LAMS]

# H2 (HAND) -- the published closed form, evaluated at an unpublished nu.
H2_TERMS = [(E, NU - E, p_euler(E), p_euler(TWO - E),
             (NU - E) * p_euler(E) * p_euler(TWO - E)) for E in range(1, NU)]
H2 = sum(t[4] for t in H2_TERMS)

# H4 (NON-HAND) -- s0 histogram over ALL 1 002 partitions of 22.
hist = {}
for l in parts22:
    hist[s0(l)] = hist.get(s0(l), 0) + 1
    if time.time() - T0 > LIMIT:
        raise SystemExit("HARD TIME LIMIT")
H4_BUCKET = 13
H4 = hist.get(H4_BUCKET, 0)

# H3 (NON-HAND) -- E>=1 survivor count at nu = 11, with its per-E split.
per_E_surv, per_E_tested, surv_rows = {}, {}, []
for E in range(1, NU):
    eparts = list(partitions(E))
    lparts = list(partitions(TWO - E))
    cnt = c2 = 0
    for L in range(NU + 1, TWO - E + 1):
        for e in eparts:
            cpart = [L + x for x in e] + [L] * (L + 1 - len(e))
            for lam in lparts:
                cnt += 1
                if steps(cpart + list(lam)) == L:
                    c2 += 1
                    surv_rows.append((L, E, e, lam))
        if time.time() - T0 > LIMIT:
            raise SystemExit("HARD TIME LIMIT at E=%d L=%d" % (E, L))
    per_E_tested[E] = cnt
    per_E_surv[E] = c2
H3 = sum(per_E_surv.values())
TESTED = sum(per_E_tested.values())
assert TESTED == H2, (TESTED, H2)

# H5 (HAND) -- one explicit shape, yes/no plus the true step count.
H5_L, H5_E, H5_e, H5_lam = 13, 3, (2, 1), (5, 4, 4, 3, 3)
assert sum(H5_e) == H5_E and sum(H5_lam) == TWO - H5_E
assert NU + 1 <= H5_L <= TWO - H5_E
H5_list = [H5_L + x for x in H5_e] + [H5_L] * (H5_L + 1 - len(H5_e)) + list(H5_lam)
H5 = steps(H5_list)
# a row whose run ABORTS ("not a step sequence") has no step count to state and
# would grade ambiguously -- refuse to write such a key.
assert H5 is not None, "H5 shape is not a step sequence; pick another"

# FAN-6' check over the whole nu=11 survivor roster (a control, not a key row)
misses = [r for r in surv_rows if not rec["fan6_kills"](r[3])]

lines = []
lines.append("=== owner-w61 round 17 -- Q36 HELD-OUT KEY, nu = 11 ===")
lines.append("NOT PASTED INTO ANY BRIEF.  Grading is exact-match; a stated wrong")
lines.append("value voids the round, 'CANNOT COMPUTE' does not.")
lines.append("")
lines.append("--- SELF-CALIBRATION against PRINTED draft data (run BEFORE any key value) ---")
lines.extend(cal)
lines.append("  CALIBRATION PASS = True")
lines.append("")
lines.append("--- THE KEY ---")
lines.append("")
lines.append("H1  [HAND, echo-proof: four independent values]")
lines.append("    s0(lambda) := steps([lambda_1]^{lambda_1+1} u lambda), lambda |- 22")
for l, v in H1:
    lines.append("      s0([%s]) = %d" % (fmt_part(l), v))
lines.append("")
lines.append("H2  [HAND: the published closed form, evaluated at an unpublished nu]")
lines.append("    S(11) = sum_{E=1}^{10} (11-E) p(E) p(22-E) = %d" % H2)
for E, w, pE, pL, t in H2_TERMS:
    lines.append("      E=%-2d  %2d * p(%d)=%-3d * p(%d)=%-4d = %d" % (E, w, E, pE, TWO - E, pL, t))
lines.append("")
lines.append("H3  [NON-HAND: a count over %d enumerated shapes, WITH per-E split]" % TESTED)
lines.append("    E>=1 survivors at nu = 11 : %d" % H3)
lines.append("    per-E split               : %s" % per_E_surv)
lines.append("    per-E shapes tested       : %s" % per_E_tested)
lines.append("    (the published counts 0,1,4,9,20,38,75,137,251,447 have no closed")
lines.append("     form in this document; an extrapolation grades WRONG)")
lines.append("")
lines.append("H4  [NON-HAND: %d separate Havel-Hakimi runs before the first digit]" % len(parts22))
lines.append("    #{lambda |- 22 : s0(lambda) = %d} = %d" % (H4_BUCKET, H4))
lines.append("    full histogram (NOT asked, recorded for adjudication): %s"
             % dict(sorted(hist.items())))
lines.append("")
lines.append("H5  [HAND: one explicit shape, one trajectory]")
lines.append("    nu=11, L=%d, E=%d, e=[%s], lambda=[%s]"
             % (H5_L, H5_E, fmt_part(H5_e), fmt_part(H5_lam)))
lines.append("    list = %s" % sorted(H5_list, reverse=True))
lines.append("    clears in exactly L = %d steps?  %s   (actual step count %s)"
             % (H5_L, "YES" if H5 == H5_L else "NO", H5))
lines.append("")
lines.append("--- OPS-3 accounting ---")
lines.append("    HAND-derivable rows      : H1, H2, H5  = 3   (>= 2 required)")
lines.append("    NON-hand-derivable rows  : H3, H4      = 2   (>= 2 required)")
lines.append("    OPS-3 MET.  H1 is the echo-proof discriminator (4 independent values).")
lines.append("")
lines.append("--- controls ---")
lines.append("    nu=11 E>=1 shapes tested : %d  (= S(11), loop and closed form agree)" % TESTED)
lines.append("    FAN-6' misses over the nu=11 survivor roster : %d" % len(misses))
lines.append("    elapsed %.1fs (hard limit %.0fs)" % (time.time() - T0, LIMIT))

with open(OUT, "w") as fh:
    fh.write("\n".join(lines) + "\n")
print("wrote %s  (calibration PASS, %.1fs)" % (OUT, time.time() - T0))
