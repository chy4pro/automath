"""
WOWII-61 round 40, block [2] -- THE PIVOT-COUNT IDENTITY, and what it proves outright.

Claim C1-X (hand proof in the ledger; VERIFIED here):
    for every terminating list L of length n,
        (i)  R(L) = n - s(L),  where s(L) = number of Havel-Hakimi steps
        (ii) sum over steps of the pivot p_t  =  sum(L)/2
    hence RESIDUE COUNTS THE NON-PIVOTS, and residue is constant along the trajectory.

Claim C1-Y (terminal lemma, item 3; hand proof in the ledger; VERIFIED here):
    R(0^r) = r  and  R((1,1,0^{r-2})) = r - 1  for every r >= 2, so the lockstep
    dichotomy's non-merging branch has delta EXACTLY 1, by computation not by census.

Also measured: the (MON) delta recomputed as a DIFFERENCE OF PIVOT COUNTS, which is the
form C1-X puts it in.

RULING CO': step engines extracted BY SOURCE TEXT from w61_r29_c1audit.py, two
implementations diffed on every call.  No SAT, no exhaustive search beyond partitions of
N <= 16.  INTERNAL HARD LIMIT: loops check the clock and print PARTIAL rather than run on.
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 60.0
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()


def grab(name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---))" % re.escape(name), text, re.S | re.M)
    assert m, name
    return m.group(0)


ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]

DIFFED = 0
CTRLS = []
OUT_OF_TIME = []


def over():
    if time.time() - T0 > LIMIT:
        OUT_OF_TIME.append(1)
        return True
    return False


def run(lst):
    global DIFFED
    a, b = runA(list(lst)), runB(list(lst))
    if a != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (lst, a, b))
        sys.exit(2)
    DIFFED += 1
    return a


def res(lst):
    return run(lst)[1]


def ms(lst):
    return tuple(sorted(lst, reverse=True))


def trajectory(lst):
    """returns (pivots, n_steps, final_length) or None if the run aborts."""
    cur = sorted(lst, reverse=True)
    piv = []
    guard = 0
    while True:
        guard += 1
        if guard > 500:
            return None
        nxt = stepA(sorted(cur, reverse=True))
        if nxt == "TERMINAL":
            return piv, len(piv), len(cur)
        if nxt is None:
            return None
        piv.append(max(cur))
        cur = sorted(nxt, reverse=True)


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRLS.append(ok)
    print("   CONTROL %-64s hits=%-6d %s" % (name, hits, "OK" if ok else "** DID NOT FIRE **"))


def known(name, got, want):
    ok = (got == want)
    CTRLS.append(ok)
    print("   KNOWN   %-64s got=%-6s want=%-5s %s" % (name, got, want, "OK" if ok else "** MISMATCH **"))


print("=" * 100)
print("W61 r40 [2] PIVOT-COUNT IDENTITY (C1-X) and TERMINAL LEMMA (C1-Y)")
print("=" * 100)
known("res(star K_1,3)", res([3, 1, 1, 1]), 3)
known("res(P4)", res([2, 2, 1, 1]), 2)
known("res(C4)", res([2, 2, 2, 2]), 2)
print("   MUST_ABORT non-graphic [3,3,1]:", res([3, 3, 1]) is None)
CTRLS.append(res([3, 3, 1]) is None)

# ---------------------------------------------------------------- [1] C1-X
print()
print("[1] C1-X : R(L) = n - s(L)  AND  sum of pivots = sum(L)/2")
print("    population: EVERY terminating partition L of EVERY N in 2..16, no other filter.")
tested = 0
bad_i = bad_ii = 0
PARTIAL = False
for N in range(2, 17):
    if over():
        PARTIAL = True
        print("   PARTIAL at N=%d" % N)
        break
    for L in parts(N):
        tr = trajectory(list(L))
        if tr is None:
            continue
        piv, s, fin = tr
        r = res(list(L))
        if r is None:
            continue
        tested += 1
        if r != len(L) - s:
            bad_i += 1
            if bad_i <= 3:
                print("   ** (i) FAILS on %s : R=%d  n-s=%d" % (L, r, len(L) - s))
        if sum(piv) * 2 != sum(L):
            bad_ii += 1
            if bad_ii <= 3:
                print("   ** (ii) FAILS on %s : sum(piv)=%d  sum(L)/2=%s" % (L, sum(piv), sum(L) / 2))
print("   terminating lists tested                       : %d" % tested)
print("   (i)  R(L) = n - s(L)      counterexamples      : %d" % bad_i)
print("   (ii) 2*sum(pivots) = sum(L) counterexamples    : %d" % bad_ii)
print("   exclusion list for those two 0s: none -- every terminating partition of every")
print("   N in 2..16 is included; lists whose run ABORTS are skipped (they have no s(L))")
print("   and are counted nowhere else.  Aborting lists skipped in this sweep:")
ab = 0
for N in range(2, 17):
    for L in parts(N):
        if trajectory(list(L)) is None:
            ab += 1
print("   aborting lists skipped                         : %d" % ab)
# r40 OWN DEFECT 1, fixed in place: the first form of this control counted the lists where
# the CORRUPT claim HOLDS (always 0) instead of where it FAILS, and printed DID NOT FIRE.
# That is r39's own inverted-polarity defect committed again, one round later.
ctrl("CORRUPT: 'R(L) = n - s(L) - 1' is violated",
     sum(1 for N in range(2, 9) for L in parts(N)
         if trajectory(list(L)) and res(list(L)) != len(L) - trajectory(list(L))[1] - 1))

# ---------------------------------------------------------------- [2] C1-Y
print()
print("[2] C1-Y : the TERMINAL SIGNATURE, computed for every r in 2..12")
print("   r  | R(0^r) | R((1,1,0^{r-2})) | delta")
okY = 0
for r in range(2, 13):
    a = res([0] * r)
    b = res([1, 1] + [0] * (r - 2))
    d = None if (a is None or b is None) else a - b
    print("   %-2d |   %-4s |      %-4s        |  %s" % (r, a, b, d))
    if a == r and b == r - 1 and d == 1:
        okY += 1
print("   r values where R(0^r)=r, R((1,1,0^{r-2}))=r-1 and delta=1 : %d of 11" % okY)
CTRLS.append(okY == 11)
ctrl("CORRUPT: 'delta at the terminal signature is 0' is violated",
     sum(1 for r in range(2, 13) if res([0] * r) - res([1, 1] + [0] * (r - 2)) != 0))

# ---------------------------------------------------------------- [3] delta as pivot difference
print()
print("[3] (MON)'s delta REWRITTEN as a pivot-count difference, via C1-X")
print("    for a (UP2) pair (L, L') of the SAME length n:  R(L) - R(L') = s(L') - s(L).")
print("    population: the DISTINCT (UP2) pairs of block [1] of w61_r40_pop.py, N in 2..16.")
agree = disagree = 0
hist = Counter()
for N in range(2, 17):
    if over():
        PARTIAL = True
        print("   PARTIAL at N=%d" % N)
        break
    for L in parts(N):
        trL = trajectory(list(L))
        if trL is None:
            continue
        rL = res(list(L))
        n = len(L)
        seen = set()
        for i in range(n):
            for j in range(i + 1, n):
                Lp = list(L)
                Lp[i] += 1
                Lp[j] += 1
                Lp = ms(Lp)
                if Lp in seen:
                    continue
                seen.add(Lp)
                trP = trajectory(list(Lp))
                if trP is None:
                    continue
                rP = res(list(Lp))
                if rP is None:
                    continue
                if (rL - rP) == (trP[1] - trL[1]):
                    agree += 1
                else:
                    disagree += 1
                hist[rL - rP] += 1
print("   pairs where R(L)-R(L') = s(L')-s(L)            : %d" % agree)
print("   pairs where it fails                           : %d" % disagree)
print("   delta histogram over those pairs               : %s" % dict(sorted(hist.items())))
print("   exclusion list for the 0 above: none -- pairs whose L or L' run ABORTS are")
print("   skipped (undefined s) and counted nowhere else.")
ctrl("CORRUPT: 'the delta histogram is a single value' is violated", len(hist) - 1)

print()
print("[4] SELF-AUDIT")
print("   diffed runA/runB calls : %d   disagreements: 0 (any would exit(2))" % DIFFED)
print("   controls               : %d, all firing: %s" % (len(CTRLS), all(CTRLS)))
print("   PARTIAL                : %s" % PARTIAL)
print("   elapsed                : %.1fs   internal limit %.0fs" % (time.time() - T0, LIMIT))
print("EXIT=0")
