#!/usr/bin/env python3
"""owner-w61 round 11 — adjudication of the Q27 Spark report on Lemma TAIL.

Own residueAux/steps implementation, written fresh (no reuse of the judge's
w61_S3_TAIL_spark_check.py or of any prior adjudication script's numbers).
Calibrated on residue(K2)=1 and residue(C_n)=ceil(n/3) BEFORE any adjudication
number is trusted.

Claims reproduced-or-refuted:
  A. calibration values in the report
  B. box: partitions with sum(lambda)<=12 (272 incl. empty), L in [0,15];
     in-hypothesis pairs (lambda nonempty, L>=lambda1) = 3125 with 0 mismatches
     against (L-lambda1)+s0(lambda); out-of-hypothesis pairs = 1211 with 462
     mismatches
  C. steps([2,2,2,2]) = 2 (FAN-5 second half, s0([2]) = 2 = lambda1)
  D. boundary rows: lambda=[1,1] L=1 -> 2; lambda=[2nu] at L=lambda1 gives
     s0 = 2nu for nu=1..6; repeated-maxima samples
  E. the judge's superlative: smallest out-of-hypothesis mismatch is
     lambda=[2], L=0 (observed 1, predicted 0) — check under the orders
     (sum(lambda)+L), (len(multiset)), and lexicographic
  F. tie-robustness (adjudicator's own extra): steps() under ADVERSARIAL
     tie-breaking (all ways of choosing the block among equal values, sampled)
     equals canonical steps() on the in-hypothesis box restricted to
     sum(lambda)<=8, L<=8 — the lemma is a multiset statement, so any
     tie-dependence would be a defect in J-TAIL-BLOCK that canonical
     simulation cannot see.
"""

import random
from functools import lru_cache

# ---------- fresh HH implementation ----------

def hh_once(ms):
    """One residueAux step on a descending-sorted tuple. Head must be > 0.
    Decrements the next min(head, len(rest)) entries with N-truncation."""
    head, rest = ms[0], list(ms[1:])
    k = min(head, len(rest))
    for i in range(k):
        rest[i] = rest[i] - 1 if rest[i] > 0 else 0
    rest.sort(reverse=True)
    return tuple(rest)


def steps_canon(ms):
    """Number of HH steps until the head is 0 (or list empty)."""
    cur = tuple(sorted((x for x in ms), reverse=True))
    n = 0
    while cur and cur[0] > 0:
        cur = hh_once(cur)
        n += 1
    return n


def residue(ms):
    cur = tuple(sorted((x for x in ms), reverse=True))
    while cur and cur[0] > 0:
        cur = hh_once(cur)
    return len(cur)


# ---------- adversarial-tie steps: choose the block among ties randomly ----------

def steps_tie(ms, rng):
    """HH steps where, at each step, the head is any max entry and the block is
    the top-k entries with ties at the block boundary resolved randomly.
    Implemented on labelled entries so tie choices are real choices."""
    cur = list(ms)
    n = 0
    while cur and max(cur) > 0:
        cur.sort(reverse=True)
        # head: any entry of maximal value — value-identical, pick index 0
        head = cur[0]
        rest = cur[1:]
        k = min(head, len(rest))
        if k > 0:
            # boundary value: rest sorted desc; entries strictly above the
            # k-th value are forced; among entries equal to the k-th value we
            # choose randomly which ones complete the block
            rest.sort(reverse=True)
            bval = rest[k - 1]
            forced = [i for i, v in enumerate(rest) if v > bval]
            tied = [i for i, v in enumerate(rest) if v == bval]
            need = k - len(forced)
            chosen = set(forced) | set(rng.sample(tied, need))
            rest = [ (v - 1 if v > 0 else 0) if i in chosen else v
                     for i, v in enumerate(rest) ]
        cur = rest
        n += 1
    return n


# ---------- partitions ----------

def partitions_upto(total):
    """All partitions (descending tuples of positive ints) with sum <= total,
    including the empty partition."""
    out = [()]

    def rec(rem, maxp, pref):
        for p in range(min(rem, maxp), 0, -1):
            out.append(pref + (p,))
            rec(rem - p, p, pref + (p,))

    rec(total, total, ())
    return out


@lru_cache(maxsize=None)
def s0(lam):
    m = lam[0]
    return steps_canon((m,) * (m + 1) + lam)


def main():
    ok = True

    # A. calibration
    print("[A] calibration")
    c1 = residue((1, 1))
    print(f"    residue(K2) = {c1}  (expect 1)")
    ok &= c1 == 1
    for n in range(3, 10):
        r = residue((2,) * n)
        s = steps_canon((2,) * n)
        exp = -(-n // 3)
        print(f"    C_{n}: residue={r} steps={s} ceil(n/3)={exp} n-steps={n-s}")
        ok &= r == exp and r == n - s
    rep_steps = {3: 2, 4: 2, 5: 3, 6: 4, 7: 4, 8: 5, 9: 6}
    ok &= all(steps_canon((2,) * n) == rep_steps[n] for n in rep_steps)
    print(f"    report's steps(C_n) table matches: "
          f"{all(steps_canon((2,)*n) == rep_steps[n] for n in rep_steps)}")

    # B. the box
    print("[B] box: sum(lambda)<=12, L in [0,15]")
    parts = partitions_upto(12)
    print(f"    #partitions incl. empty = {len(parts)}  (report: 272)")
    ok &= len(parts) == 272
    inp = outp = inm = outm = 0
    out_mm = []
    for lam in parts:
        if not lam:
            continue
        l1 = lam[0]
        for L in range(0, 16):
            obs = steps_canon((L,) * (L + 1) + lam)
            pred = (L - l1) + s0(lam)
            if L >= l1:
                inp += 1
                if obs != pred:
                    inm += 1
                    print(f"    IN-SCOPE MISMATCH lam={lam} L={L} obs={obs} pred={pred}")
            else:
                outp += 1
                if obs != pred:
                    outm += 1
                    out_mm.append((lam, L, obs, pred))
    print(f"    in-hyp pairs={inp} (report 3125), mismatches={inm} (report 0)")
    print(f"    out-hyp pairs={outp} (report 1211), mismatches={outm} (report 462)")
    ok &= (inp, inm, outp, outm) == (3125, 0, 1211, 462)

    # C. FAN-5 instance
    print("[C] FAN-5 second half")
    s2222 = steps_canon((2, 2, 2, 2))
    print(f"    steps([2,2,2,2]) = {s2222}  (expect 2);  s0([2]) = {s0((2,))}")
    ok &= s2222 == 2 and s0((2,)) == 2
    fan5 = all(steps_canon((L,) * (L + 1) + (2,)) == L for L in range(2, 16))
    print(f"    [L]^(L+1) u [2] clears in exactly L for L=2..15: {fan5}")
    ok &= fan5

    # D. boundary rows from the report
    print("[D] boundary rows")
    v = steps_canon((1, 1, 1, 1))
    print(f"    lam=[1,1] L=1: observed {v} (report 2)")
    ok &= v == 2
    for nu in range(1, 7):
        lam = (2 * nu,)
        got = s0(lam)
        print(f"    lam=[{2*nu}]: s0 = {got}  (expect {2*nu})")
        ok &= got == 2 * nu
    for lam in [(3, 3), (4, 4), (3, 3, 1), (3, 2, 1, 1)]:
        L = lam[0]
        obs = steps_canon((L,) * (L + 1) + lam)
        pred = s0(lam)
        print(f"    lam={lam} L=lam1={L}: obs={obs} pred={pred} match={obs==pred}")
        ok &= obs == pred

    # E. the superlative "smallest outside-hypothesis counterexample"
    print("[E] smallest out-of-hypothesis mismatch")
    by_content = sorted(out_mm, key=lambda t: (sum(t[0]) + t[1], len(t[0]) + t[1] + 1, t[0]))
    by_size = sorted(out_mm, key=lambda t: (len(t[0]) + t[1] + 1, sum(t[0]) + t[1], t[0]))
    print(f"    min by total content sum(lam)+L : lam={by_content[0][0]} L={by_content[0][1]} "
          f"obs={by_content[0][2]} pred={by_content[0][3]}")
    print(f"    min by multiset length          : lam={by_size[0][0]} L={by_size[0][1]} "
          f"obs={by_size[0][2]} pred={by_size[0][3]}")
    claim = ((2,), 0, 1, 0)
    print(f"    judge's claim lam=[2],L=0,obs=1,pred=0 is a mismatch: {claim in out_mm}")
    ok &= claim in out_mm
    ok &= by_content[0] == claim and by_size[0] == claim

    # F. adversarial tie-break robustness (judge ran canonical only)
    print("[F] adversarial tie-breaks, sum(lambda)<=8, L<=8, 3 random runs each")
    rng = random.Random(20260818)
    bad = 0
    tested = 0
    for lam in partitions_upto(8):
        if not lam:
            continue
        l1 = lam[0]
        for L in range(l1, 9):
            ms = (L,) * (L + 1) + lam
            base = steps_canon(ms)
            tested += 1
            for _ in range(3):
                if steps_tie(ms, rng) != base:
                    bad += 1
                    print(f"    TIE-DEPENDENCE lam={lam} L={L}")
                    break
    print(f"    {tested} in-hyp multisets x3 adversarial runs: {bad} tie-dependent")
    ok &= bad == 0

    print(f"\nADJUDICATION RESULT: {'ALL REPRODUCED' if ok else 'DISCREPANCY FOUND'}")


if __name__ == "__main__":
    main()
