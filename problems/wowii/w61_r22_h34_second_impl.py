#!/usr/bin/env python3
"""
w61_r22_h34_second_impl.py

SECOND, INDEPENDENT implementation, written from a written specification only.
No prior code from this repo was read.  Standard library only.

Definition 1 (step process, "head deletes the d largest"):
  sort non-increasing; d := head (largest); delete head;
  block := the d largest of the remaining entries; subtract 1 from each.
  Abort if d > (number of remaining entries) or if any block entry is 0
  before decrementing.  Terminate successfully when every entry is 0.

Definition 2:  s0(lambda) := step count of  [l1]*(l1+1)  ++  lambda.
"""

import sys
import time
from collections import Counter

T0 = time.time()
HARD_LIMIT = 600.0          # seconds, enforced inside the main loops

ROSTER_PATH = "$HOME/workspace/claudecode/automath/problems/wowii/w61_r22_h34_second_roster.txt"


class TimeUp(Exception):
    pass


def check_time(where):
    el = time.time() - T0
    if el > HARD_LIMIT:
        raise TimeUp("HARD TIME LIMIT %.1fs EXCEEDED at %s (elapsed %.1fs)"
                     % (HARD_LIMIT, where, el))


# ----------------------------------------------------------------------
# Definition 1 : the step process (own Havel-Hakimi)
# ----------------------------------------------------------------------
def run_process(values):
    """Return (ok, steps).

    ok == True  : process terminated successfully (all entries 0);
                  steps == number of steps taken.
    ok == False : the list is not a step sequence (aborted); steps ==
                  number of completed steps before the abort.
    """
    a = sorted(values, reverse=True)
    steps = 0
    while True:
        if not a or a[0] == 0:
            return (True, steps)          # every remaining entry is 0
        d = a[0]
        rest = a[1:]                      # delete the head
        if d > len(rest):                 # head exceeds remaining entries
            return (False, steps)
        if rest[d - 1] == 0:              # a block entry is 0 -> would go negative
            return (False, steps)
        for i in range(d):
            rest[i] -= 1
        rest.sort(reverse=True)
        a = rest
        steps += 1
        if steps > 100000:                # impossible; pure safety valve
            raise RuntimeError("step process did not terminate: %r" % (values,))


def step_count(values):
    ok, s = run_process(values)
    return s if ok else None              # None == aborted / not a step sequence


def clears_in_exactly(values, L):
    ok, s = run_process(values)
    return ok and s == L


# ----------------------------------------------------------------------
# Definition 2 : s0
# ----------------------------------------------------------------------
def s0(lam):
    if not lam:
        return step_count([])
    l1 = lam[0]
    vals = [l1] * (l1 + 1) + list(lam)
    return step_count(vals)


# ----------------------------------------------------------------------
# own partition generator
# ----------------------------------------------------------------------
def gen_partitions(n):
    """Yield every partition of n as a non-increasing list of positive ints."""
    if n == 0:
        yield []
        return
    cur = []

    def rec(remaining, maxp):
        if remaining == 0:
            yield list(cur)
            return
        top = remaining if remaining < maxp else maxp
        for k in range(top, 0, -1):
            cur.append(k)
            for r in rec(remaining - k, k):
                yield r
            cur.pop()

    for r in rec(n, n):
        yield r


def partitions_list(n):
    return [tuple(p) for p in gen_partitions(n)]


def fmt_list(t):
    return "[" + ",".join(str(x) for x in t) + "]"


def verdict(cond):
    return "PASS" if cond else "FAIL"


# ======================================================================
def main():
    print("=" * 72)
    print("w61_r22_h34_second_impl.py  --  SECOND INDEPENDENT IMPLEMENTATION")
    print("written from specification only; stdlib only; python", sys.version.split()[0])
    print("=" * 72)

    # ------------------------------------------------------------------
    # CHECK A
    # ------------------------------------------------------------------
    print()
    print("---- CHECK A : self-calibration of Definition 1 / Definition 2 ----")
    caseA = [
        ([1] * 12, 7,  "[1]*12"),
        ([2] * 6,  6,  "[2]*6"),
        ([3] * 4,  6,  "[3]*4"),
        ([4] * 3,  6,  "[4]*3"),
        ([6, 6],   7,  "[6,6]"),
        ([11, 1],  12, "[11,1]"),
        ([12],     12, "[12]"),
        ([12, 6, 4],   14, "[12,6,4]"),
        ([9, 7, 3, 3], 12, "[9,7,3,3]"),
        ([14, 5, 2, 1], 16, "[14,5,2,1]"),
        ([8, 8, 6],    10, "[8,8,6]"),
    ]
    checkA_ok = True
    for lam, expected, name in caseA:
        got = s0(lam)
        ok = (got == expected)
        checkA_ok = checkA_ok and ok
        print("  s0(%-12s) computed=%-6s expected=%-4d %s"
              % (name, str(got), expected, verdict(ok)))
    print("  CHECK A overall: %s" % verdict(checkA_ok))
    if not checkA_ok:
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!! CHECK A FAILED -- the Definition-1 implementation is WRONG.")
        print("!! Stopping.  NOT tuning anything.  Diagnose the step process.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()
        print("SUMMARY")
        print("CHECK A : FAIL")
        print("CHECK B : NOT RUN")
        print("H4      : NOT RUN")
        print("H3 total: NOT RUN")
        print("H3 per-E: NOT RUN")
        print("SHAPES  : NOT RUN")
        print("ELAPSED : %.2f" % (time.time() - T0))
        return 1

    # ------------------------------------------------------------------
    # CHECK B  (H5 control)
    # ------------------------------------------------------------------
    print()
    print("---- CHECK B : H5 control list L5 ----")
    L5 = [15, 14] + [13] * 12 + [5, 4, 4, 3, 3]
    print("  L5 = %s   (%d entries, sum=%d)" % (fmt_list(L5), len(L5), sum(L5)))
    okB_run, stepsB = run_process(L5)
    print("  terminated successfully? computed=%s" % okB_run)
    print("  step count: computed=%s expected=16 %s"
          % (str(stepsB if okB_run else None), verdict(okB_run and stepsB == 16)))
    clears13 = clears_in_exactly(L5, 13)
    ans13 = "YES" if clears13 else "NO"
    print("  clears in exactly 13 steps? computed=%s expected=NO %s"
          % (ans13, verdict(ans13 == "NO")))
    checkB_ok = (okB_run and stepsB == 16) and (ans13 == "NO")
    print("  CHECK B overall: %s" % verdict(checkB_ok))

    # ------------------------------------------------------------------
    # partition tables (own generator), p(n) counts derived from them
    # ------------------------------------------------------------------
    print()
    print("---- partition tables (own generator) ----")
    PT = {}
    for n in range(0, 23):
        check_time("partition table n=%d" % n)
        PT[n] = partitions_list(n)
    pcount = {n: len(PT[n]) for n in PT}
    print("  p(n) from my generator, n=0..22:")
    print("   ", {n: pcount[n] for n in range(0, 23)})

    # ------------------------------------------------------------------
    # H4 : histogram of s0 over all partitions of 22
    # ------------------------------------------------------------------
    print()
    print("---- H4 : histogram of s0(lambda) over lambda |- 22 ----")
    parts22 = PT[22]
    n_parts22 = len(parts22)
    print("  partitions of 22 generated: computed=%d expected=1002 %s"
          % (n_parts22, verdict(n_parts22 == 1002)))
    hist = Counter()
    aborted22 = []
    for lam in parts22:
        check_time("H4")
        v = s0(lam)
        if v is None:
            aborted22.append(lam)
        else:
            hist[v] += 1
    print("  aborted (not a step sequence) count: %d" % len(aborted22))
    if aborted22:
        print("  ABORTED partitions (first 20): %s"
              % [fmt_list(x) for x in aborted22[:20]])
    print("  histogram {s0: count} sorted by value:")
    print("   ", {k: hist[k] for k in sorted(hist)})
    hist_total = sum(hist.values())
    print("  histogram total: computed=%d expected=1002 %s"
          % (hist_total, verdict(hist_total == 1002)))
    h4 = hist.get(13, 0)
    print("  #{lambda |- 22 : s0(lambda) = 13} : computed=%d expected=131 %s"
          % (h4, verdict(h4 == 131)))
    h4_ok = (h4 == 131)
    h4_total_ok = (hist_total == 1002 and n_parts22 == 1002)

    # ------------------------------------------------------------------
    # H3 : E >= 1 survivors at nu = 11
    # ------------------------------------------------------------------
    print()
    print("---- H3 : E >= 1 survivors at nu = 11 ----")
    nu = 11
    shapes_by_E = {}
    surv_by_E = {}
    roster = []

    for E in range(1, nu):                       # 1 .. 10
        es = PT[E]
        lams = PT[2 * nu - E]                    # partitions of 22 - E
        n_shapes = 0
        n_surv = 0
        for L in range(nu + 1, 2 * nu - E + 1):  # 12 .. 22-E
            check_time("H3 E=%d L=%d" % (E, L))
            for e in es:
                if len(e) > L + 1:
                    # "at most L+1 parts" -- never binding here, but honour it
                    continue
                # C-part: parts of e padded with zeros to length L+1, each +L
                cpart = [L + x for x in e] + [L] * (L + 1 - len(e))
                for lam in lams:
                    n_shapes += 1
                    vals = cpart + list(lam)
                    ok, st = run_process(vals)
                    if ok and st == L:
                        n_surv += 1
                        roster.append((E, L, e, lam))
        shapes_by_E[E] = n_shapes
        surv_by_E[E] = n_surv
        print("  E=%-2d  L in [%d..%d] (%d values)  p(E)=%-3d p(22-E)=%-4d"
              "  shapes=%-6d survivors=%d"
              % (E, nu + 1, 2 * nu - E, nu - E, pcount[E], pcount[22 - E],
                 n_shapes, n_surv))

    total_shapes = sum(shapes_by_E.values())
    total_surv = sum(surv_by_E.values())

    print()
    print("  per-E shapes tested (computed): %s" % (shapes_by_E,))
    print("  total shapes tested (computed): %d" % total_shapes)
    print("  per-E survivors     (computed): %s" % (surv_by_E,))
    print("  total survivors     (computed): %d" % total_surv)

    # independent formula check from my own partition counts
    print()
    print("  independent formula (nu-E)*p(E)*p(22-E) from my partition counts:")
    formula = {E: (nu - E) * pcount[E] * pcount[22 - E] for E in range(1, nu)}
    print("   ", formula)
    S11 = sum(formula.values())
    print("    S(11) = sum_{E=1}^{10} (11-E)*p(E)*p(22-E) = %d" % S11)
    formula_ok = True
    for E in range(1, nu):
        ok = (shapes_by_E[E] == formula[E])
        formula_ok = formula_ok and ok
        if not ok:
            print("    E=%d shapes=%d != formula=%d  FAIL"
                  % (E, shapes_by_E[E], formula[E]))
    print("    per-E shapes == formula : %s" % verdict(formula_ok))
    print("    total shapes == S(11)   : computed=%d formula=%d %s"
          % (total_shapes, S11, verdict(total_shapes == S11)))

    # diff against the expected values given in the specification
    EXP_SHAPES_TOTAL = 98384
    EXP_SHAPES = {1: 7920, 2: 11286, 3: 11760, 4: 13475, 5: 12474, 6: 12705,
                  7: 10560, 8: 8910, 9: 6060, 10: 3234}
    EXP_SURV_TOTAL = 791
    EXP_SURV = {1: 6, 2: 14, 3: 21, 4: 35, 5: 47, 6: 85, 7: 110, 8: 155,
                9: 170, 10: 148}

    print()
    print("  diff vs expected -- shapes tested:")
    shapes_match = (total_shapes == EXP_SHAPES_TOTAL)
    shapes_perE_bad = []
    for E in range(1, nu):
        ok = (shapes_by_E[E] == EXP_SHAPES[E])
        if not ok:
            shapes_perE_bad.append(E)
        print("    E=%-2d computed=%-6d expected=%-6d %s"
              % (E, shapes_by_E[E], EXP_SHAPES[E], verdict(ok)))
    print("    TOTAL  computed=%-6d expected=%-6d %s"
          % (total_shapes, EXP_SHAPES_TOTAL, verdict(shapes_match)))

    print()
    print("  diff vs expected -- survivors:")
    surv_perE_bad = []
    for E in range(1, nu):
        ok = (surv_by_E[E] == EXP_SURV[E])
        if not ok:
            surv_perE_bad.append(E)
        print("    E=%-2d computed=%-5d expected=%-5d %s"
              % (E, surv_by_E[E], EXP_SURV[E], verdict(ok)))
    surv_match = (total_surv == EXP_SURV_TOTAL)
    print("    TOTAL  computed=%-5d expected=%-5d %s"
          % (total_surv, EXP_SURV_TOTAL, verdict(surv_match)))

    # ------------------------------------------------------------------
    # roster
    # ------------------------------------------------------------------
    roster.sort(key=lambda r: (r[0], r[1], r[2], r[3]))
    lines = ["E=%d L=%d e=%s lam=%s" % (E, L, fmt_list(e), fmt_list(lam))
             for (E, L, e, lam) in roster]
    with open(ROSTER_PATH, "w") as fh:
        for ln in lines:
            fh.write(ln + "\n")

    print()
    print("---- H3 FULL ROSTER (canonical, sorted by (E, L, e, lam)) ----")
    print("  format: E=<E> L=<L> e=[p,p,..] lam=[p,p,..]   (no spaces inside [])")
    for ln in lines:
        print(ln)
    print("  roster written to: %s" % ROSTER_PATH)
    with open(ROSTER_PATH) as fh:
        nlines = sum(1 for _ in fh)
    print("  roster line count: computed=%d survivor total=%d %s"
          % (nlines, total_surv, verdict(nlines == total_surv)))

    # ------------------------------------------------------------------
    # summary block
    # ------------------------------------------------------------------
    h3_perE_ok = (not surv_perE_bad)
    elapsed = time.time() - T0
    print()
    print("=" * 72)
    print("CHECK A : %s" % verdict(checkA_ok))
    print("CHECK B : %s" % verdict(checkB_ok))
    print("H4      : computed=%d expected=131 %s   (histogram total %d vs 1002)"
          % (h4, verdict(h4_ok), hist_total))
    print("H3 total: computed=%d expected=791 %s"
          % (total_surv, verdict(surv_match)))
    if h3_perE_ok:
        print("H3 per-E: PASS")
    else:
        print("H3 per-E: FAIL  (differing E: %s)"
              % ", ".join("E=%d computed=%d expected=%d"
                          % (E, surv_by_E[E], EXP_SURV[E]) for E in surv_perE_bad))
    if shapes_perE_bad:
        print("SHAPES  : computed=%d expected=98384 %s  (differing E: %s)"
              % (total_shapes, verdict(shapes_match),
                 ", ".join("E=%d computed=%d expected=%d"
                           % (E, shapes_by_E[E], EXP_SHAPES[E])
                           for E in shapes_perE_bad)))
    else:
        print("SHAPES  : computed=%d expected=98384 %s"
              % (total_shapes, verdict(shapes_match)))
    print("ELAPSED : %.2f" % elapsed)
    print("=" * 72)

    all_ok = (checkA_ok and checkB_ok and h4_ok and h4_total_ok and surv_match
              and h3_perE_ok and shapes_match and not shapes_perE_bad
              and formula_ok and nlines == total_surv and not aborted22)
    print("ALL CHECKS PASSED: %s" % ("YES" if all_ok else "NO"))
    return 0 if all_ok else 2


if __name__ == "__main__":
    try:
        rc = main()
    except TimeUp as exc:
        print()
        print("ABORTED: %s" % exc)
        print("ELAPSED : %.2f" % (time.time() - T0))
        rc = 3
    sys.exit(rc)
