#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r41 ITEM 1 -- SPECIFY SHAPE S2 AT THE LIST LEVEL, and settle whether the two engines
that called it "unsatisfiable as literally stated" were right ABOUT THE BRIEF.

WHERE THIS STARTS.  Two independent engines (E01, E02) attacking Candidate Lemma C1-W both
concluded "Shape S2 as literally stated is unsatisfiable", while notes/proofs/wowii61_draft.md
Sec 7.54 (c) records 1016 real S2 instances.  cert_engine_firstpass_r1.md Sec 4 rules that a
convergence of two independent readings against the source is evidence about the BRIEF.

THE BRIEF'S S2 SENTENCE, quoted from briefs/E01_w61_C1W_angleA.md line 51 (planner-authored):
    Shape S2 ("max_rises"): A = W-(c) u tail, and B is obtained from A by the UP2 move that
    sends W-(c) -> W+(c+1): the head block changes SIZE (not just a swap within it), i.e.
    B = W+(c+1) u tail'' ... (two of A's entries equal to c-1 or c are raised so that the
    count of (c+1)-copies becomes 3 and c-copies becomes c+1).
and line 57: "In both shapes ... B = A with exactly two entries raised by 1 (an UP2 pair),
and A, B both have the same length n."

THE AUTHORITATIVE SOURCE is the generator in w61_r39_monodd.py, reproduced here BY SOURCE
TEXT (not retyped) so that no transcription can drift:
    Wp(c) = [c]*3 + [c-1]*c        Wm(c) = [c]*2 + [c-1]*(c+1)
    head_of(T) = Wp(T[0]) if sum(T) even else Wm(T[0])
    L_of(T)    = head_of(T) + list(T[1:])
    f(T)       = residue(L_of(T))
and the shape split, at w61_r39_monodd.py:224-226:  i == 0 or T[i] == T[0]  ->  S2_max_rises.

WHAT THIS SCRIPT DOES
  [0] controls, incl. corrupt companions, all fired before any verdict
  [1] reproduce the Sec 7.54 (c) census exactly: 4073 instances, S1 / S2 split
  [2] the STRUCTURE of S2, measured on every S2 instance: tail is IDENTICAL, head block
      is REBUILT, lengths differ by 1, sums differ by 2c+4
  [3] is S2 ever a UP2 pair?  the brief says always; measure it
  [4] worked instances, printed in full with both Havel-Hakimi trajectories
  [5] the brief's other two population errors (the 6469 census, and "tail entries <= c-1")

RULING CO': step process extracted BY SOURCE TEXT from w61_r29_c1audit.py -- two independent
implementations diffed on every call.  No SAT, no exhaustive search, no solver.
INTERNAL HARD LIMIT: every loop checks the clock and prints PARTIAL rather than running on.
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 60.0          # seconds, internal.  Never rely on an external timeout.
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
SRC39 = ROOT / "problems/wowii/w61_r39_monodd.py"
text = SRC.read_text()
text39 = SRC39.read_text()


def grab(t, name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---|print|NMAX))" % re.escape(name),
                  t, re.S | re.M)
    assert m, name
    return m.group(0)


ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(text, n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]

DIFFED = 0
FAIL = []
OUT_OF_TIME = []
CTRL = []


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


def bad(tag, detail):
    FAIL.append("%s  %s" % (tag, detail))
    print("   ** DEFECT %s  %s" % (tag, detail))


def ms(lst):
    return tuple(sorted(lst, reverse=True))


def step(lst):
    r = stepA(sorted(lst, reverse=True))
    if r == "TERMINAL" or r is None:
        return r
    return ms(r)


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


# ---- THE DEFINITIONS, LIFTED BY SOURCE TEXT FROM w61_r39_monodd.py (no retyping) --------
ns39 = {"ms": ms, "res": res, "sorted": sorted}
_defs = "\n".join(grab(text39, n) for n in ("Wp", "Wm", "head_of", "L_of"))
exec(compile(_defs, str(SRC39), "exec"), ns39)
Wp, Wm, head_of, L_of = ns39["Wp"], ns39["Wm"], ns39["head_of"], ns39["L_of"]
FC = {}


def f(T):
    T = ms(T)
    if T not in FC:
        FC[T] = 2 if not T else res(L_of(T))
    return FC[T]


print("=" * 100)
print("w61 r41 ITEM 1 -- SHAPE S2 SPECIFIED AT THE LIST LEVEL")
print("=" * 100)
print("definitions Wp/Wm/head_of/L_of lifted by SOURCE TEXT from w61_r39_monodd.py:")
for ln in _defs.strip().splitlines():
    if ln.strip():
        print("   | " + ln.rstrip())

# ================================================================ 0. CONTROLS
print("\n[0] CONTROLS -- fired on the feature, before any verdict (RULING CZ')")


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append(ok)
    print("   %-62s hits=%-8s %s" % (name, hits, "OK" if ok else "** CONTROL DID NOT FIRE"))
    if not ok:
        bad("CONTROL", name)


def known(name, got, exp):
    CTRL.append(got == exp)
    print("   known-value  %-34s = %-10s expect %-10s %s"
          % (name, got, exp, "OK" if got == exp else "** MISMATCH"))
    if got != exp:
        bad("KNOWN", "%s got %s expect %s" % (name, got, exp))


def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)


known("residue(M((5,4,3)))", res(M((5, 4, 3))), 2)
known("[1,1,0,0] boundary", run([1, 1, 0, 0]), (1, 3))
known("W+(2)u[2] boundary", res(Wp(2) + [2]), 3)
known("W-(3)u[2] boundary", res(Wm(3) + [2]), 3)
known("f(1^5)  (C1-U: ceil(5/2)+2)", f((1,) * 5), 5)
known("|W-(c)| = c+3, c=1..12", [len(Wm(c)) - c - 3 for c in range(1, 13)], [0] * 12)
known("|W+(c)| = c+3, c=1..12", [len(Wp(c)) - c - 3 for c in range(1, 13)], [0] * 12)
n_ab = sum(1 for L in ([3, 1, 1], [5, 1], [4, 2, 1], [2]) if res(L) is None)
known("MUST_ABORT inputs aborting", n_ab, 4)

inv_n = inv_bad = 0
for N in range(2, 15):
    for L in parts(N):
        r = res(list(L))
        if r is None:
            continue
        s = step(list(L))
        if s in ("TERMINAL", None):
            continue
        inv_n += 1
        if res(list(s)) != r:
            inv_bad += 1
print("   TOOL CONTROL  residue is a trajectory invariant: %d lists, %d violations"
      % (inv_n, inv_bad))
CTRL.append(inv_bad == 0)
if inv_bad:
    bad("INVARIANT", "residue not step-invariant")
cnt_bad = 0
for N in range(2, 12):
    for L in parts(N):
        a = run(list(L))
        if a[0] is None:
            continue
        s = step(list(L))
        if s in ("TERMINAL", None):
            continue
        if run(list(s))[0] != a[0]:
            cnt_bad += 1
ctrl("CORRUPT: 'step COUNT is also invariant' is violated", cnt_bad)

# ================================================================ 1. CENSUS REPRODUCED
print("\n[1] REPRODUCE THE Sec 7.54 (c) CENSUS -- same generator, same range")
print("    population: MON instances (T, T+e_i) with sum(T) ODD, over all partitions T")
print("    with sum(T) <= 18.  Aborting instances are skipped on BOTH sides and counted")
print("    nowhere else.  Exclusion list for every 0 below: none.")
NMAX = 18
shape_hist = Counter()
delta_hist = {}
viol = {}
pop = 0
S2 = []          # (T, U, c, tail, L, Lp, fT, fU) for every S2 instance
S1 = []
for N in range(1, NMAX + 1):
    if over():
        break
    for T in parts(N):
        if sum(T) % 2 == 0:
            continue
        for i in range(len(T)):
            U = list(T)
            U[i] += 1
            U = ms(U)
            sh = "S2_max_rises" if (i == 0 or T[i] == T[0]) else "S1_head_parity_flip"
            if len(U) != len(T):
                bad("SHAPE", "raising a part changed the number of parts: %s" % (T,))
            a, b = f(T), f(U)
            if a is None or b is None:
                continue
            pop += 1
            shape_hist[sh] += 1
            delta_hist.setdefault(sh, Counter())[a - b] += 1
            if not (0 <= a - b <= 1):
                viol.setdefault(sh, []).append((T, U, a, b))
            rec = (ms(T), ms(U), T[0], ms(T[1:]), ms(L_of(T)), ms(L_of(U)), a, b)
            (S2 if sh == "S2_max_rises" else S1).append(rec)
print("   population (both shapes, sum(T) odd, sum(T) <= %d): %d" % (NMAX, pop))
for sh in sorted(shape_hist):
    print("   %-22s n=%-7d delta = f(T)-f(T+e_i) histogram %s"
          % (sh, shape_hist[sh], dict(sorted(delta_hist[sh].items()))))
for sh in sorted(shape_hist):
    v = viol.get(sh, [])
    print("      %-22s violations of 0<=delta<=1 = %-4d  exclusions: none; list=%s"
          % (sh, len(v), v[:3] if v else "[]"))
ctrl("CORRUPT: 'delta is always 0' is violated",
     sum(h[1] for h in delta_hist.values() if 1 in h))

# ================================================================ 2. THE STRUCTURE OF S2
print("\n[2] THE STRUCTURE OF S2 -- measured on EVERY S2 instance in the census")
print("    population for every count in this block: the %d S2 instances of block [1]."
      % len(S2))
tail_same = 0
head_pair = 0
len_plus1 = 0
sum_2c4 = 0
tail_gt_cm1 = 0
lenL = Counter()
for (T, U, c, tail, L, Lp, a, b) in S2:
    if ms(U[1:]) == tail:
        tail_same += 1
    if L == ms(list(Wm(c)) + list(tail)) and Lp == ms(list(Wp(c + 1)) + list(tail)):
        head_pair += 1
    if len(Lp) - len(L) == 1:
        len_plus1 += 1
    if sum(Lp) - sum(L) == 2 * c + 4:
        sum_2c4 += 1
    if tail and max(tail) > c - 1:
        tail_gt_cm1 += 1
    lenL[len(Lp) - len(L)] += 1
print("   (i)   U[1:] == T[1:] as multisets (the TAIL IS UNCHANGED)      : %d of %d"
      % (tail_same, len(S2)))
print("   (ii)  L == W-(c) u tail   AND   L' == W+(c+1) u tail          : %d of %d"
      % (head_pair, len(S2)))
print("   (iii) len(L') - len(L) == 1  (LISTS OF DIFFERENT LENGTH)      : %d of %d"
      % (len_plus1, len(S2)))
print("   (iv)  sum(L') - sum(L) == 2c+4                                 : %d of %d"
      % (sum_2c4, len(S2)))
print("   (v)   histogram of len(L')-len(L) over all S2 instances        : %s"
      % dict(sorted(lenL.items())))
print("   (vi)  S2 instances whose tail has an entry > c-1 (brief says none): %d of %d"
      % (tail_gt_cm1, len(S2)))
for nm, got in (("tail unchanged", tail_same), ("head pair", head_pair),
                ("length +1", len_plus1), ("sum 2c+4", sum_2c4)):
    CTRL.append(got == len(S2))
    if got != len(S2):
        bad("S2STRUCT", "%s holds only %d of %d" % (nm, got, len(S2)))

# ================================================================ 3. IS S2 EVER A UP2 PAIR
print("\n[3] IS S2 EVER THE 'RAISE TWO ENTRIES BY 1' (UP2) MOVE THE BRIEF SAYS IT IS?")
print("    UP2 requires, necessarily: len(L')==len(L) and sum(L')==sum(L)+2.")


def is_up2(A, B):
    """POSITIONAL test (Sec 7.54 (f) 3: a multiset test measures the wrong thing)."""
    if len(A) != len(B) or sum(B) != sum(A) + 2:
        return False
    for x in range(len(A)):
        for y in range(x, len(A)):
            C = list(A)
            C[x] += 1
            C[y] += 1
            if ms(C) == B:
                return True
    return False


s2_up2 = sum(1 for r in S2 if is_up2(r[4], r[5]))
s2_lenok = sum(1 for r in S2 if len(r[4]) == len(r[5]))
s2_sumok = sum(1 for r in S2 if sum(r[5]) == sum(r[4]) + 2)
print("   S2 instances that ARE a UP2 pair                : %d of %d" % (s2_up2, len(S2)))
print("   ...of which fail on LENGTH alone                : %d of %d have len(L')==len(L)"
      % (s2_lenok, len(S2)))
print("   ...of which fail on SUM alone                   : %d of %d have sum(L')==sum(L)+2"
      % (s2_sumok, len(S2)))
print("   EXCLUSION LIST for the three 0s above: none -- every one of the %d S2 instances"
      % len(S2))
print("   of block [1] is tested; nothing is skipped, nothing is counted elsewhere.")
# the SAME test on S1, which the brief describes correctly -- so the test can distinguish
s1_up2 = sum(1 for r in S1 if is_up2(r[4], r[5]))
print("   CONTROL, same test on S1 (which the brief states correctly): %d of %d ARE UP2"
      % (s1_up2, len(S1)))
ctrl("CONTROL: the UP2 test is not vacuous (fires positive on S1)", s1_up2)
CTRL.append(s2_up2 == 0)
if s2_up2:
    bad("S2UP2", "some S2 instance IS a UP2 pair -- the brief would be satisfiable")

print("\n   THE ARITHMETIC, INDEPENDENT OF THE CENSUS -- why no c can ever work:")
print("   c | |W-(c)| |W+(c+1)| dlen | sum W-(c) sum W+(c+1) dsum | UP2 needs dlen=0,dsum=2")
bad_c = 0
for c in range(1, 11):
    dl = len(Wp(c + 1)) - len(Wm(c))
    dsm = sum(Wp(c + 1)) - sum(Wm(c))
    print("  %2d |  %4d   %6d   %+3d |  %7d   %9d   %+4d | %s"
          % (c, len(Wm(c)), len(Wp(c + 1)), dl, sum(Wm(c)), sum(Wp(c + 1)), dsm,
             "UNSATISFIABLE" if (dl != 0 or dsm != 2) else "satisfiable"))
    if dl == 0 and dsm == 2:
        bad_c += 1
print("   values of c in 1..10 for which the brief's S2 sentence is satisfiable: %d" % bad_c)
print("   EXCLUSION LIST for that 0: none in the range c=1..10; and the general reason is")
print("   printed, not sampled -- |W+(c+1)|-|W-(c)| = (c+4)-(c+3) = 1 for EVERY c, so no")
print("   length-preserving move exists at any c whatsoever.")
CTRL.append(bad_c == 0)

# ================================================================ 4. WORKED INSTANCES
print("\n[4] WORKED INSTANCES, DRAWN FROM THE %d-INSTANCE S2 CENSUS OF BLOCK [1]" % len(S2))


def traj(L):
    out = [ms(L)]
    cur = list(L)
    while True:
        nxt = step(cur)
        if nxt == "TERMINAL":
            return out, "TERMINAL"
        if nxt is None:
            return out, "ABORT"
        out.append(nxt)
        cur = list(nxt)


def show(rec, why):
    (T, U, c, tail, L, Lp, a, b) = rec
    print("\n   --- %s" % why)
    print("   T      = %-24s sum(T) = %-3d  (odd, as required)" % (str(T), sum(T)))
    print("   i      : the raised part is a copy of the maximum, so U[0] = c+1")
    print("   U      = %-24s sum(U) = %-3d" % (str(U), sum(U)))
    print("   c      = T[0] = %d      tail = T[1:] = %s   (UNCHANGED between T and U)"
          % (c, str(tail)))
    print("   W-(c)      = %s" % str(Wm(c)))
    print("   W+(c+1)    = %s   <- THREE copies of c+1 = %d, then %d copies of %d"
          % (str(Wp(c + 1)), c + 1, c + 1, c))
    print("   L  = W-(c)   u tail = %-30s |L|  = %-3d sum = %d" % (str(L), len(L), sum(L)))
    print("   L' = W+(c+1) u tail = %-30s |L'| = %-3d sum = %d" % (str(Lp), len(Lp), sum(Lp)))
    tA, eA = traj(L)
    tB, eB = traj(Lp)
    print("   HH trajectory of L  (%s): %s" % (eA, " -> ".join(str(x) for x in tA)))
    print("   HH trajectory of L' (%s): %s" % (eB, " -> ".join(str(x) for x in tB)))
    rA, rB = run(list(L)), run(list(Lp))
    print("   R(L)  = f(T)  = %d   (n=%d, s=%d, n-s=%d)" % (a, len(L), rA[0], len(L) - rA[0]))
    print("   R(L') = f(U)  = %d   (n=%d, s=%d, n-s=%d)" % (b, len(Lp), rB[0], len(Lp) - rB[0]))
    print("   delta = f(T) - f(U) = %d" % (a - b))
    print("   len(L')-len(L) = %d  and  sum(L')-sum(L) = %d = 2c+4 = %d"
          % (len(Lp) - len(L), sum(Lp) - sum(L), 2 * c + 4))
    print("   => NOT a UP2 pair: %s" % ("confirmed" if not is_up2(L, Lp) else "** IS a UP2 pair"))
    CTRL.append(a == rA[1] and b == rB[1])


S2s = sorted(S2, key=lambda r: (sum(r[0]), r[0]))
show(S2s[0], "SMALLEST S2 instance in the census")
c0 = [r for r in S2s if r[3] and r[6] - r[7] == 0]
c1 = [r for r in S2s if r[3] and r[6] - r[7] == 1]
c2 = [r for r in S2s if len(r[0]) > 1 and r[0][1] == r[0][0]]
if c0:
    show(c0[0], "smallest S2 instance with NON-EMPTY tail and delta = 0")
if c1:
    show(c1[0], "smallest S2 instance with NON-EMPTY tail and delta = 1")
if c2:
    show(c2[0], "smallest S2 instance where the raised part is a REPEATED maximum (i >= 1)")

# ================================================================ 5. THE OTHER TWO ERRORS
print("\n[5] THE BRIEF'S OTHER TWO POPULATION ERRORS, MEASURED")
print("   (a) the brief attributes its 6469-state-pair census to 'all S1/S2-shaped (A0,B0)")
print("       pairs'.  w61_r39_monodd.py:237 appends to the lockstep list ONLY when")
print("       sh == 'S1_head_parity_flip' and sum(T) <= 14.  Source line, verbatim:")
for ln in text39.splitlines():
    if "S1_head_parity_flip\" and sum(T)" in ln or "S1_head_parity_flip' and sum(T)" in ln:
        print("       | %s" % ln.strip())
s1_le14 = sum(1 for r in S1 if sum(r[0]) <= 14)
s2_le14 = sum(1 for r in S2 if sum(r[0]) <= 14)
print("       S1 instances with sum(T) <= 14 (what was actually stepped) : %d" % s1_le14)
print("       S2 instances with sum(T) <= 14 (what was NOT stepped)      : %d" % s2_le14)
print("       population for both counts: block [1]'s census restricted to sum(T) <= 14.")
print("   (b) the brief defines a head-block list as W^eps(c) u tail with every tail entry")
print("       <= c-1.  In the real construction tail = T[1:], whose entries are <= T[0] = c.")
s1_tail_c = sum(1 for r in S1 if r[3] and max(r[3]) > r[2] - 1)
print("       S1 instances with a tail entry > c-1 : %d of %d" % (s1_tail_c, len(S1)))
print("       S2 instances with a tail entry > c-1 : %d of %d" % (tail_gt_cm1, len(S2)))
print("       population: block [1]'s census, both shapes, sum(T) <= 18.")

# ================================================================ 6. THE S2 STATEMENT
print("\n[6] THE STATEMENT S2 ACTUALLY IS -- and it is verified on the whole census")
print("   (S2)  Let c >= 1 and let tail be a weakly-decreasing list of integers in [0,c]")
print("         with c + sum(tail) ODD.  Put  L = W-(c) u tail  and  L' = W+(c+1) u tail.")
print("         If the Havel-Hakimi runs of L and of L' both terminate, then")
print("                        0 <= R(L) - R(L') <= 1.")
print("   Note |L'| = |L| + 1 and sum(L') = sum(L) + 2c + 4: these are TWO SEPARATELY")
print("   CONSTRUCTED lists, NOT one list and a perturbation of it.")
ok6 = bad6 = 0
seen = set()
for (T, U, c, tail, L, Lp, a, b) in S2:
    key = (c, tail)
    if key in seen:
        continue
    seen.add(key)
    if (c + sum(tail)) % 2 != 1:
        bad("S2PARITY", "c+sum(tail) not odd for c=%s tail=%s" % (c, tail))
    if tail and max(tail) > c:
        bad("S2RANGE", "tail entry > c for c=%s tail=%s" % (c, tail))
    rl, rp = res(list(L)), res(list(Lp))
    if rl is None or rp is None:
        continue
    if 0 <= rl - rp <= 1:
        ok6 += 1
    else:
        bad6 += 1
print("   distinct (c, tail) pairs arising in the census : %d" % len(seen))
print("   ...satisfying 0 <= R(L)-R(L') <= 1             : %d" % ok6)
print("   ...violating it                                : %d" % bad6)
print("   EXCLUSION LIST for that 0: none among the %d distinct (c,tail) pairs; pairs whose"
      % len(seen))
print("   run aborts on either side are skipped and counted nowhere else (%d skipped)."
      % (len(seen) - ok6 - bad6))
CTRL.append(bad6 == 0)
ctrl("CONTROL: the (c,tail) sweep is non-empty", len(seen))

# corrupt companion for [6]: the claim with the two lists SWAPPED must fail somewhere
sw_bad = 0
for (T, U, c, tail, L, Lp, a, b) in S2:
    rl, rp = res(list(L)), res(list(Lp))
    if rl is None or rp is None:
        continue
    if not (0 <= rp - rl <= 1):
        sw_bad += 1
ctrl("CORRUPT: 'R(L') - R(L) in [0,1]' (swapped) is violated", sw_bad)

# ================================================================ SUMMARY
print("\n" + "=" * 100)
print("SUMMARY")
print("=" * 100)
print("  diffed runA/runB calls : %d   disagreements: 0 (a disagreement exits 2)" % DIFFED)
print("  controls recorded      : %d   all true: %s" % (len(CTRL), all(CTRL)))
print("  DEFECTS                : %d  %s" % (len(FAIL), FAIL if FAIL else ""))
print("  PARTIAL (time limit)   : %s   elapsed %.1fs of internal limit %.0fs"
      % (bool(OUT_OF_TIME), time.time() - T0, LIMIT))
print("  VERDICT ON ITEM 1      : printed above; see [3] for whether the engines were right")
sys.exit(1 if FAIL else 0)
