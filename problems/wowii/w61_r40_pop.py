"""
WOWII-61 round 40, block [0]/[1] -- POPULATION AUDIT.

Round 40 item 0 (cert_w61_r39.md sec.3): a number that is genuinely MEASURED but carried
under a sentence about a DIFFERENT POPULATION.  Two instances are audited here and both
are settled by measurement, not by arithmetic on someone else's printed line:

  [1] the 85 : the head-block-FREE violating pairs of (UP2).  r39 printed 97 (all
      violating pairs) and 12 (those containing a head block).  This block RE-DERIVES
      the split directly and prints the head-block-free count itself, so the number
      that goes in the ledger is measured, not subtracted.
  [2] the 5842-vs-635 : r39's ".out" line 51 says "(UP2) re-swept to reproduce r38 [5]:
      ok=5842  VIOLATIONS=97".  r38 [5] printed "DISTINCT pairs ok=635 VIOLATIONS=97".
      This block computes BOTH counters on the SAME sweep to establish whether 5842 and
      635 count the same objects.  If they do not, r39's word "exactly" is a population
      drift and the draft sentence carrying it is defective.
  [3] the DENOMINATOR the 85 needs, if one exists: split the OK side by head block too.

RULING CO': the Havel-Hakimi step is extracted BY SOURCE TEXT from w61_r29_c1audit.py,
two independent implementations diffed on every call.  No SAT, no exhaustive search over
anything but partitions of N <= 16 (the same range r38/r39 used).
INTERNAL HARD LIMIT: every loop checks the clock and prints PARTIAL rather than running on.
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
FAIL = []
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


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


def Wp(c):   return [c] * 3 + [c - 1] * c
def Wm(c):   return [c] * 2 + [c - 1] * (c + 1)


def is_headed(L):
    """VERBATIM the predicate w61_r39_monodd.py:455 used to print the 12."""
    L = ms(L)
    for c in range(1, max(L) + 1):
        for H in (Wp(c), Wm(c)):
            d = Counter(L) - Counter(H)
            if sum((Counter(H) - Counter(L)).values()) == 0 and (not d or max(d) <= c):
                return True
    return False


def up2(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            Lp = list(L)
            Lp[i] += 1
            Lp[j] += 1
            yield Lp


CTRLS = []


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRLS.append(ok)
    print("   CONTROL %-62s hits=%-6d %s" % (name, hits, "OK" if ok else "** DID NOT FIRE **"))


def known(name, got, want):
    ok = (got == want)
    CTRLS.append(ok)
    print("   KNOWN   %-62s got=%-6s want=%-5s %s" % (name, got, want, "OK" if ok else "** MISMATCH **"))


print("=" * 100)
print("W61 r40 [0] POPULATION AUDIT -- the 85, and the 5842-vs-635")
print("=" * 100)

known("res(W+(2) u [2]) boundary", res(Wp(2) + [2]), 3)
known("res(W-(3) u [2]) boundary", res(Wm(3) + [2]), 3)
known("res(star K_1,3 = [3,1,1,1])", res([3, 1, 1, 1]), 3)
known("res(P4 = [2,2,1,1])", res([2, 2, 1, 1]), 2)
known("res(C4 = [2,2,2,2])", res([2, 2, 2, 2]), 2)
print("   MUST_ABORT non-graphic [3,3,1]:", res([3, 3, 1]) is None)
CTRLS.append(res([3, 3, 1]) is None)

# ---------------------------------------------------------------- [1] the two counters
print()
print("[1] THE SAME (UP2) SWEEP, COUNTED BOTH WAYS -- r38's counter and r39's counter")
print("    population: every terminating partition L of every N in 2..16; L' = L with two")
print("    entries raised by 1 (generator up2(), byte-identical to w61_r38_c1p.py:453).")

ok_set, bad_set = set(), set()
ok_pos, bad_pos = 0, 0
PARTIAL = False
for N in range(2, 17):
    if over():
        PARTIAL = True
        print("   PARTIAL: internal limit reached at N=%d" % N)
        break
    for L in parts(N):
        r = res(list(L))
        if r is None:
            continue
        for Lp in up2(L):
            Lp = ms(Lp)
            if min(Lp) < 0:
                continue
            rp = res(list(Lp))
            if rp is None:
                continue
            if rp <= r:
                ok_set.add((L, Lp, r, rp))
                ok_pos += 1
            else:
                bad_set.add((L, Lp, r, rp))
                bad_pos += 1

print("   r38's counter -- DISTINCT (L,L',r,r') tuples : ok=%-6d VIOLATIONS=%-5d" % (len(ok_set), len(bad_set)))
print("   r39's counter -- POSITIONAL (i,j) increments : ok=%-6d VIOLATIONS=%-5d" % (ok_pos, bad_pos))
print("   exclusion list for this sweep: none -- every terminating partition of every N in")
print("   2..16 is included; lists whose Havel-Hakimi run aborts are skipped and counted")
print("   nowhere else, on BOTH the L side and the L' side.")
same = (len(ok_set) == ok_pos)
print("   DO THE TWO COUNTERS COUNT THE SAME OBJECTS ON THE OK SIDE?  %s" % ("YES" if same else "NO"))
print("   DO THEY AGREE ON THE VIOLATION SIDE?                        %s"
      % ("YES" if len(bad_set) == bad_pos else "NO"))
ctrl("CORRUPT: 'distinct ok == positional ok' (must FAIL, i.e. differ)", 0 if same else 1)

# ---------------------------------------------------------------- [2] the 85
print()
print("[2] THE 85 -- MEASURED, NOT SUBTRACTED")
uniq_bad = sorted(bad_set, key=lambda z: (sum(z[0]), len(z[0]), z[0]))
headed_bad = [z for z in uniq_bad if is_headed(z[0])]
free_bad = [z for z in uniq_bad if not is_headed(z[0])]
print("   population: the DISTINCT (UP2) violating pairs above.")
print("   violating pairs, ALL                                    : %d" % len(uniq_bad))
print("   violating pairs whose L CONTAINS a head block W^eps(c)  : %d" % len(headed_bad))
print("   violating pairs whose L is HEAD-BLOCK-FREE  <-- THE 85  : %d" % len(free_bad))
print("   partition check  headed + free == all                   : %s"
      % (len(headed_bad) + len(free_bad) == len(uniq_bad)))
CTRLS.append(len(headed_bad) + len(free_bad) == len(uniq_bad))
print("   three head-block-FREE violators, printed rather than excluded:")
for z in free_bad[:3]:
    print("      L=%s -> L'=%s : residue %d -> %d" % (z[0], z[1], z[2], z[3]))
ctrl("CORRUPT: 'no violating L is head-block-free' is violated", len(free_bad))
ctrl("CORRUPT: 'no violating L contains a head block' is violated", len(headed_bad))

# ---------------------------------------------------------------- [3] the denominator
print()
print("[3] THE DENOMINATOR -- the OK side split the same way, so the 85 can be a RATE")
if over():
    print("   PARTIAL: internal limit reached before the ok-side split; denominator PENDING")
else:
    headed_ok = free_ok = 0
    for z in ok_set:
        if over():
            PARTIAL = True
            print("   PARTIAL: internal limit reached inside the ok-side split")
            break
        if is_headed(z[0]):
            headed_ok += 1
        else:
            free_ok += 1
    print("   ok pairs whose L CONTAINS a head block                  : %d" % headed_ok)
    print("   ok pairs whose L is HEAD-BLOCK-FREE                     : %d" % free_ok)
    print("   => HEAD-BLOCK-FREE population swept  = %d ok + %d violating = %d pairs"
          % (free_ok, len(free_bad), free_ok + len(free_bad)))
    print("   => HEAD-BLOCK    population swept  = %d ok + %d violating = %d pairs"
          % (headed_ok, len(headed_bad), headed_ok + len(headed_bad)))
    print("   (UP2) fails on %d of %d head-block-free pairs; on %d of %d head-block pairs."
          % (len(free_bad), free_ok + len(free_bad), len(headed_bad), headed_ok + len(headed_bad)))

# ---------------------------------------------------------------- [4] self-audit
print()
print("[4] SELF-AUDIT")
print("   diffed runA/runB calls : %d   disagreements: 0 (any would exit(2))" % DIFFED)
print("   controls               : %d, all firing: %s" % (len(CTRLS), all(CTRLS)))
print("   PARTIAL                : %s" % PARTIAL)
print("   elapsed                : %.1fs   internal limit %.0fs" % (time.time() - T0, LIMIT))
print("   FAIL list              : %s" % (FAIL if FAIL else "empty"))
print("EXIT=0")
