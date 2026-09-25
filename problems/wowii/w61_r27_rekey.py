#!/usr/bin/env python3
"""
owner-w61 round 27, task item 2 -- RE-KEY the held-out harness.

WHY.  `w61_r17_heldout_key.txt` (nu = 11) has now graded FOUR outings: Q36, Q37,
Q38 and the round-26 NVIDIA qualification.  Planner: "four outings on the r17 key
is overdue, and this round's qualification failure burned it against a fifth
reader."  It has not leaked as a KEY -- the harness ships the questions, never the
answers -- but this builder does not take that on faith either: it MEASURES the
burn of nu = 11 against the draft and against every shipped brief before choosing
the new range, and prints the measurement whether or not it is comfortable.

RANGE.  New key at nu = 12 (2nu = 24).  Burn ladder, measured below, not asserted:
  * nu <= 10  -- PUBLISHED.  The SS7.31 (f) fold prints every nu <= 10 value.
  * nu = 11   -- BURNED, and worse than "four outings": the r17 key's own ANSWERS
                 are now printed in the DRAFT (SS7.35/SS7.37/SS7.39 harvest tables
                 print S(11), the H3 survivor count and the H4 bucket).  A fifth
                 outing on this key would be graded against numbers a reader of
                 our own ledger can read off.
  * nu = 12   -- the new key.  Probed clean below against the draft AND against
                 every prompts/w61_*.md ever shipped.

DISCIPLINE, unchanged from r17 and from RULING CD's round:
  * SELF-CALIBRATION FIRST.  The generator reproduces the PRINTED nu <= 10 draft
    data before it computes a single held-out value, and aborts without writing on
    any mismatch.  RULING CD's rider is printed with it: a passed calibration is
    NOT a passed harness -- calibration measures whether the GENERATOR understood
    the setup, exactly as it measures that and nothing more for a judge.
  * OPS-3: >= 2 genuinely HAND-derivable rows AND >= 2 genuinely NON-hand rows.
  * LEAK PROBE: every discriminating value, and every H1/H5 shape, is counted in
    the draft and in all shipped briefs.  The POPULATION is printed before the
    verdict (RULING AS), and a non-zero count aborts the write.
  * THE KEY IS NOT PASTED INTO ANY BRIEF.  One product: w61_r27_heldout_key.txt.
"""

import glob
import re
import time

src = open("problems/wowii/w61_r17_roster_recompute.py").read()
rec = {}
exec(compile(src.replace('if __name__ == "__main__":', 'if False:'),
             "w61_r17_roster_recompute.py", "exec"), rec)
steps, partitions, p_euler = rec["steps"], rec["partitions"], rec["p_euler"]
s0, fmt_part = rec["s0"], rec["fmt_part"]

T0 = time.time()
LIMIT = 900.0
OUT = "problems/wowii/w61_r27_heldout_key.txt"
DRAFT = "notes/proofs/wowii61_draft.md"
BRIEFS = sorted(glob.glob("prompts/w61_*.md"))

log = []
def say(s=""):
    log.append(s)
    print(s)

# =========================================================== 0. THE BURN LEDGER
# Measured, not asserted.  For each candidate range, how much of it is already
# readable off our own artifacts?
say("=== owner-w61 round 27 -- RE-KEY: the burn measurement, run BEFORE the choice ===")
draft_txt = open(DRAFT).read()
brief_txt = {p: open(p).read() for p in BRIEFS}

def mask(v):
    """DEFECT E-1 root fix -- a leak probe must never print what it is probing for."""
    s = str(v)
    return re.sub(r"[0-9]", "#", s) + " <%dch>" % len(s)


def occurrences(tok):
    """count of tok in the draft and across every shipped brief, both the bare
    and the thin-space-grouped rendering."""
    forms = {str(tok)}
    s = str(tok)
    if s.isdigit() and len(s) > 3:
        # 98384 -> '98 384'
        grp = ""
        while len(s) > 3:
            grp = " " + s[-3:] + grp
            s = s[:-3]
        forms.add(s + grp)
    d = sum(draft_txt.count(f) for f in forms)
    b = {p: sum(t.count(f) for f in forms) for p, t in brief_txt.items()}
    return d, {p: c for p, c in b.items() if c}, sorted(forms)

R17_ANSWERS = [98384, 791, 131, 1002]
say("  the r17 (nu = 11) key's OWN ANSWER values, looked for in our own artifacts:")
burned_in_draft = 0
for v in R17_ANSWERS:
    d, b, forms = occurrences(v)
    burned_in_draft += d
    say("    %-8s draft: %2d hit(s)   briefs: %s   forms %s"
        % (v, d, (", ".join("%s x%d" % (p.split('/')[-1], c) for p, c in b.items()) or "none"), forms))
say("  => nu = 11 is BURNED %s: %d hits on its answers in the draft itself."
    % ("BEYOND its four outings" if burned_in_draft else "by outing count only", burned_in_draft))
say("     A fifth outing would be graded against numbers a reader of our ledger can read off.")
say("")

# ================================================================ 1. CALIBRATION
PUB_BD_PAIRS = [0, 1, 3, 7, 14, 26, 45, 75, 120, 187]
PUB_BD_SURV = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
PUB_S = [0, 3, 24, 110, 397, 1211, 3340, 8457, 20126, 45450]
PUB_S0_NU6 = {(12,): 12, (11, 1): 12, (6, 6): 7, (4, 4, 4): 6, (3, 3, 3, 3): 6,
              (2,) * 6: 6, (1,) * 12: 7}

cal, ok = [], True
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
               % (nu, "[%s]" % fmt_part(tail[0]) if tail else "none", bp,
                  PUB_BD_PAIRS[nu - 1], bs, PUB_BD_SURV[nu - 1], S, PUB_S[nu - 1],
                  "PASS" if good else "*** FAIL ***"))
for lam, v in sorted(PUB_S0_NU6.items()):
    got = s0(lam); good = got == v; ok = ok and good
    cal.append("  s0([%s]) = %d (printed %d)  %s"
               % (fmt_part(lam), got, v, "PASS" if good else "*** FAIL ***"))
say("--- SELF-CALIBRATION against PRINTED draft data (BEFORE any key value) ---")
for c in cal:
    say(c)
if not ok:
    raise SystemExit("CALIBRATION FAILED -- no key written")
say("  CALIBRATION PASS = True")
say("  RULING CD rider, printed with it and not after it: a passed calibration is")
say("  NOT a passed harness.  This says the generator understood the setup.  It says")
say("  nothing about whether anything downstream can do the work.")
say("")

# ==================================================================== 2. nu = 12
NU, TWO = 12, 24
parts24 = list(partitions(TWO))
assert len(parts24) == p_euler(TWO) == 1575

H1_LAMS = [(13, 7, 4), (10, 8, 5, 1), (16, 4, 3, 1), (9, 9, 6)]
for l in H1_LAMS:
    assert sum(l) == TWO, l
H1 = [(l, s0(l)) for l in H1_LAMS]

H2_TERMS = [(E, NU - E, p_euler(E), p_euler(TWO - E),
             (NU - E) * p_euler(E) * p_euler(TWO - E)) for E in range(1, NU)]
H2 = sum(t[4] for t in H2_TERMS)

hist = {}
for l in parts24:
    hist[s0(l)] = hist.get(s0(l), 0) + 1
    if time.time() - T0 > LIMIT:
        raise SystemExit("HARD TIME LIMIT")
H4_BUCKET = 14
H4 = hist.get(H4_BUCKET, 0)

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

H5_L, H5_E, H5_e, H5_lam = 14, 4, (3, 1), (6, 5, 4, 4, 1)
assert sum(H5_e) == H5_E and sum(H5_lam) == TWO - H5_E
assert NU + 1 <= H5_L <= TWO - H5_E
H5_list = [H5_L + x for x in H5_e] + [H5_L] * (H5_L + 1 - len(H5_e)) + list(H5_lam)
H5 = steps(H5_list)
assert H5 is not None, "H5 shape is not a step sequence; pick another"

misses = [r for r in surv_rows if not rec["fan6_kills"](r[3])]

# ================================================================ 3. LEAK PROBE
say("--- LEAK PROBE: the POPULATION first, the verdict after (RULING AS) ---")
probe = [("H2 S(12)", H2), ("H3 survivor count", H3), ("H4 bucket count", H4),
         ("H3 shapes tested", TESTED), ("p(24)", len(parts24))]
probe += [("H2 term E=%d" % E, t) for E, _, _, _, t in H2_TERMS]
probe += [("H3 per-E survivors E=%d" % E, v) for E, v in sorted(per_E_surv.items())]
leaks = []
for label, v in probe:
    d, b, _ = occurrences(v)
    flag = ""
    if d or b:
        # a bare small integer collides with ordinary prose; only >= 4 digits is
        # discriminating.  Both are PRINTED; only the discriminating ones abort.
        if len(str(v)) >= 4:
            leaks.append((label, mask(v), d, b)); flag = "  <== DISCRIMINATING HIT"
        else:
            flag = "  (non-discriminating: %d-digit value, collides with prose)" % len(str(v))
    # DEFECT E-1, caught on the first run and fixed at the root: this probe
    # PRINTED every key value in cleartext into a repo .out file in order to
    # prove that no key value appears in a repo file.  That is the checker
    # committing the exact species it hunts -- and it is how nu = 11's answers
    # reached the draft in the first place.  The probe now prints a MASK
    # (digit-count) and the hit counts, which is all the verdict needs.
    say("    %-26s %-8s draft %2d   briefs %-28s%s"
        % (label, mask(v), d, (", ".join("%s x%d" % (p.split('/')[-1], c) for p, c in b.items()) or "none"), flag))
for tag, lam in [("H1 shape %d" % i, l) for i, l in enumerate(H1_LAMS, 1)] + [("H5 lambda", H5_lam)]:
    pat = fmt_part(lam)
    alt = ",".join(str(x) for x in lam)
    d = draft_txt.count(pat) + draft_txt.count(alt)
    b = {p: t.count(pat) + t.count(alt) for p, t in brief_txt.items()}
    b = {p: c for p, c in b.items() if c}
    if d or b:
        leaks.append((tag, mask(pat), d, b))
    say("    %-26s %-14s draft %2d   briefs %s"
        % (tag, "[%s]" % mask(pat), d, (", ".join("%s x%d" % (p.split('/')[-1], c) for p, c in b.items()) or "none")))
say("  LEAK PROBE population = %d entries; discriminating hits = %d" % (len(probe) + 5, len(leaks)))
if leaks:
    raise SystemExit("LEAK PROBE FAILED -- a key value is already readable off our own "
                     "artifacts:\n" + "\n".join("  %s = %s" % (t, v) for t, v, _, _ in leaks))
say("  LEAK PROBE PASS: no discriminating nu = 12 value appears in the draft or in any")
say("  of the %d shipped briefs." % len(BRIEFS))
say("")

# ===================================================================== 4. WRITE
lines = []
lines.append("=== owner-w61 round 27 -- HELD-OUT KEY, nu = 12  (SUPERSEDES the r17 nu = 11 key) ===")
lines.append("NOT PASTED INTO ANY BRIEF.  Grading is exact-match; a stated wrong")
lines.append("value voids the round, 'CANNOT COMPUTE' does not.")
lines.append("")
lines.append("--- BURN LEDGER (why this range) ---")
lines.append("  nu <= 10 : PUBLISHED.  The SS7.31 (f) fold prints every value.")
lines.append("  nu = 11  : RETIRED THIS ROUND.  Four outings (Q36, Q37, Q38, the r26 NVIDIA")
lines.append("             qualification) AND its own answers are now printed in the draft:")
for v in R17_ANSWERS:
    d, _, _ = occurrences(v)
    lines.append("               %-8s %d hit(s) in notes/proofs/wowii61_draft.md" % (v, d))
lines.append("  nu = 12  : THIS KEY.  Leak-probed clean against the draft and all %d briefs." % len(BRIEFS))
lines.append("")
lines.append("--- SELF-CALIBRATION against PRINTED draft data (run BEFORE any key value) ---")
lines.extend(cal)
lines.append("  CALIBRATION PASS = True")
lines.append("  (RULING CD: a passed calibration is NOT a passed harness.)")
lines.append("")
lines.append("--- THE KEY ---")
lines.append("")
lines.append("H1  [HAND, echo-proof: four independent values]")
lines.append("    s0(lambda) := steps([lambda_1]^{lambda_1+1} u lambda), lambda |- 24")
for l, v in H1:
    lines.append("      s0([%s]) = %d" % (fmt_part(l), v))
lines.append("")
lines.append("H2  [HAND: the published closed form, evaluated at an unpublished nu]")
lines.append("    S(12) = sum_{E=1}^{11} (12-E) p(E) p(24-E) = %d" % H2)
for E, w, pE, pL, t in H2_TERMS:
    lines.append("      E=%-2d  %2d * p(%d)=%-3d * p(%d)=%-5d = %d" % (E, w, E, pE, TWO - E, pL, t))
lines.append("")
lines.append("H3  [NON-HAND: a count over %d enumerated shapes, WITH per-E split]" % TESTED)
lines.append("    E>=1 survivors at nu = 12 : %d" % H3)
lines.append("    per-E split               : %s" % per_E_surv)
lines.append("    per-E shapes tested       : %s" % per_E_tested)
lines.append("    (the published counts 0,1,4,9,20,38,75,137,251,447 have no closed")
lines.append("     form in this document; an extrapolation grades WRONG)")
lines.append("")
lines.append("H4  [NON-HAND: %d separate Havel-Hakimi runs before the first digit]" % len(parts24))
lines.append("    #{lambda |- 24 : s0(lambda) = %d} = %d" % (H4_BUCKET, H4))
lines.append("    full histogram (NOT asked, recorded for adjudication): %s"
             % dict(sorted(hist.items())))
lines.append("")
lines.append("H5  [HAND: one explicit shape, one trajectory]")
lines.append("    nu=12, L=%d, E=%d, e=[%s], lambda=[%s]"
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
lines.append("    nu=12 E>=1 shapes tested : %d  (= S(12), loop and closed form agree)" % TESTED)
lines.append("    FAN-6' misses over the nu=12 survivor roster : %d" % len(misses))
lines.append("    leak probe                                   : PASS (%d entries, 0 discriminating hits)" % (len(probe) + 5))
lines.append("    elapsed %.1fs (hard limit %.0fs)" % (time.time() - T0, LIMIT))

with open(OUT, "w") as fh:
    fh.write("\n".join(lines) + "\n")
say("--- KEY SUMMARY (values withheld from this log; they live only in %s) ---" % OUT)
say("    H1 4 values | H2 11 terms | H3 with %d-way per-E split | H4 over %s partitions | H5 yes/no + count"
    % (len(per_E_surv), mask(len(parts24))))
say("    FAN-6' misses over the nu=12 survivor roster : %d" % len(misses))
say("wrote %s  (calibration PASS, leak probe PASS, %.1fs)" % (OUT, time.time() - T0))
