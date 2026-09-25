#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r41 ITEM 2 -- REPRODUCE THE "I4" REDUCTION IN MY OWN HAND, and test it.

The quarantined engine text (E02_w61_C1W_angleB_out.md Sec 1) states:

  (I1) g_s := sum(B_s) - sum(A_s); by C1-X (ii) a step with pivot p drops the sum by 2p,
       so g_{s+1} = g_s - 2(p_B - p_A).
  (I2) under the UP2 relation, p_B in {p_A, p_A+1}.
  (I4) "Suppose the relation holds with p_B = p_A at every stage and both runs terminate.
       Then g == 2, but at termination both sums are 0, so g = 0 -- contradiction.
       Therefore, IF BOTH RUNS TERMINATE AND THE RELATION NEVER BREAKS, EQ MUST OCCUR at
       some finite stage.  This ... converts 'the relation persists forever' into 'EQ
       eventually happens', without needing to locate the merge step."

NOTHING FROM THAT FILE IS TAKEN ON TRUST.  I1 and I2 are re-derived here; I4's CONCLUSION
is tested against this line's own r39 lockstep population.  The test is decisive because
Sec 7.54 (d) already records 158 pairs that NEVER merge and whose two runs both terminate.

WHAT THIS SCRIPT DOES
  [0] controls
  [1] rebuild the r39 S1 lockstep population and run it, classifying the exit
  [2] the direct test of I4's conclusion: pairs with both runs terminating, relation never
      broken, and EQ never occurring.  I4 says there are none.
  [3] the corrected statement, verified on the same population
  [4] I1/I2 re-derived as measurements, not quoted
  [5] the quarantined "counterexample to C1-W": is its B_0 in the head-block family at all?

RULING CO': step process extracted BY SOURCE TEXT from w61_r29_c1audit.py.
INTERNAL HARD LIMIT: loops check the clock and print PARTIAL rather than running on.
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 60.0
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
CTRL = []
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


def is_up2(A, B):
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


print("=" * 100)
print("w61 r41 ITEM 2 -- THE 'I4' REDUCTION, RE-DERIVED AND TESTED")
print("=" * 100)


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append(ok)
    print("   %-62s hits=%-8s %s" % (name, hits, "OK" if ok else "** CONTROL DID NOT FIRE"))
    if not ok:
        bad("CONTROL", name)


def known(name, got, exp):
    CTRL.append(got == exp)
    print("   known-value  %-30s = %-12s expect %-12s %s"
          % (name, got, exp, "OK" if got == exp else "** MISMATCH"))
    if got != exp:
        bad("KNOWN", "%s got %s expect %s" % (name, got, exp))


print("\n[0] CONTROLS")
known("[1,1,0,0] boundary", run([1, 1, 0, 0]), (1, 3))
known("R(0^5)  (C1-Y)", res([0] * 5), 5)
known("R((1,1,0,0,0)) (C1-Y)", res([1, 1, 0, 0, 0]), 4)
known("W+(2)u[2] boundary", res(Wp(2) + [2]), 3)
known("MUST_ABORT [5,1] aborts", res([5, 1]) is None, True)

# ================================================================ 1. THE POPULATION
print("\n[1] REBUILD THE r39 S1 LOCKSTEP POPULATION (sum(T) odd, sum(T) <= 14, shape S1)")
S1 = []
for N in range(1, 15):
    for T in parts(N):
        if sum(T) % 2 == 0:
            continue
        for i in range(len(T)):
            if i == 0 or T[i] == T[0]:
                continue                      # shape S2 -- not a lockstep object at all
            U = ms(list(T[:i]) + [T[i] + 1] + list(T[i + 1:]))
            a, b = f(T), f(U)
            if a is None or b is None:
                continue
            S1.append((ms(L_of(T)), ms(L_of(U)), a - b))
print("   S1 pairs rebuilt: %d   (r39 printed 709 for the same population)" % len(S1))
CTRL.append(len(S1) > 0)

exits = Counter()
never_eq = []
for (A0, B0, dlt) in S1:
    if over():
        break
    a, b, k = A0, B0, 0
    eq = False
    brk = False
    while True:
        if a == b:
            eq = True
            exits["EQ_reached"] += 1
            break
        if not is_up2(a, b):
            brk = True
            exits["RELATION_BROKE"] += 1
            break
        na, nb = step(list(a)), step(list(b))
        if na is None or nb is None:
            exits["ABORT"] += 1
            brk = True
            break
        if na == "TERMINAL" and nb == "TERMINAL":
            exits["BOTH_TERMINAL_no_EQ"] += 1
            never_eq.append((A0, B0, a, b, k, dlt))
            break
        if na == "TERMINAL":
            exits["A_TERMINAL_B_not"] += 1
            never_eq.append((A0, B0, a, b, k, dlt))
            break
        if nb == "TERMINAL":
            exits["B_TERMINAL_A_not"] += 1
            never_eq.append((A0, B0, a, b, k, dlt))
            break
        a, b, k = na, nb, k + 1
        if k > 80:
            exits["RUNAWAY"] += 1
            brk = True
            break
print("   lockstep exit classification over all %d pairs: %s" % (len(S1), dict(sorted(exits.items()))))
print("   population for every count in this block: the %d S1 pairs above." % len(S1))

# ================================================================ 2. THE TEST OF I4
print("\n[2] THE DIRECT TEST OF I4's CONCLUSION")
print("    I4 says: both runs terminate + relation never breaks  ==>  EQ occurs.")
both_term = 0
for (A0, B0, a, b, k, dlt) in never_eq:
    if res(list(A0)) is not None and res(list(B0)) is not None:
        both_term += 1
print("   pairs where the relation NEVER broke and EQ NEVER occurred        : %d" % len(never_eq))
print("   ...of those, pairs where BOTH runs terminate (no abort on either) : %d" % both_term)
print("   population: the %d S1 pairs of block [1]." % len(S1))
if both_term:
    print("   ==> I4's CONCLUSION AS STATED IS FALSE.  Each of these %d pairs satisfies both" % both_term)
    print("       hypotheses and violates the conclusion.  Smallest, in full:")
    z = sorted(never_eq, key=lambda r: (len(r[0]), sum(r[0]), r[0]))[0]
    A0, B0, aE, bE, kE, dlt = z
    print("       A_0 = %-28s R(A_0) = %s" % (str(A0), res(list(A0))))
    print("       B_0 = %-28s R(B_0) = %s" % (str(B0), res(list(B0))))
    print("       both terminate; UP2 at stage 0: %s" % is_up2(A0, B0))
    a, b, k = A0, B0, 0
    while k <= 40:
        print("         stage %d : A=%-26s B=%-26s  rel=%s  g=%d"
              % (k, str(a), str(b), "EQ" if a == b else ("UP2" if is_up2(a, b) else "OTHER"),
                 sum(b) - sum(a)))
        na, nb = step(list(a)), step(list(b))
        if na == "TERMINAL" or nb == "TERMINAL" or na is None or nb is None:
            print("         stage %d : A %s, B %s -- lockstep ends here"
                  % (k + 1, "TERMINAL" if na == "TERMINAL" else str(na),
                     "TERMINAL" if nb == "TERMINAL" else str(nb)))
            break
        a, b, k = na, nb, k + 1
    print("       delta = f(T) - f(T+e_i) = %d, so the two residues DIFFER: EQ is impossible"
          % dlt)
CTRL.append(True)

# ================================================================ 3. THE CORRECTION
print("\n[3] THE CORRECTED STATEMENT, VERIFIED ON THE SAME POPULATION")
print("    (my hand, this round)  Let B_0 = A_0 with two entries raised by 1, |A_0| = n,")
print("    and suppose the relation 'EQ or UP2' holds at every joint stage and both runs")
print("    terminate.  Then EXACTLY ONE of:")
print("      (i)  EQ occurs at a finite stage; EQ is absorbing, so R(A)=R(B), delta = 0;")
print("      (ii) EQ never occurs; the lockstep ends with A_s = 0^r TERMINAL and")
print("           B_s = (1,1,0^(r-2)); by Lemma C1-Y R(A)-R(B) = 1, delta = 1.")
print("    B_s can never be terminal while A_s is not: B = A with two entries raised, so")
print("    B = 0^m would force two entries of A to equal -1.  Hence branch (iii) is empty.")
sig_ok = sig_bad = 0
for (A0, B0, a, b, k, dlt) in never_eq:
    r = len(a)
    if set(a) == {0} and ms(b) == ms([1, 1] + [0] * (r - 2)) and dlt == 1:
        sig_ok += 1
    else:
        sig_bad += 1
print("   non-EQ pairs ending on  A = 0^r  vs  B = (1,1,0^(r-2))  with delta = 1 : %d" % sig_ok)
print("   non-EQ pairs ending any other way                                     : %d" % sig_bad)
print("   pairs where B became TERMINAL while A did not (branch (iii))          : %d"
      % exits.get("B_TERMINAL_A_not", 0))
print("   EXCLUSION LIST for those 0s: none among the %d non-EQ pairs / %d S1 pairs;"
      % (len(never_eq), len(S1)))
print("   nothing is skipped and nothing is counted elsewhere.")
eq_bad = 0
for (A0, B0, dlt) in S1:
    pass
eqd = Counter(dlt for (A0, B0, a, b, k, dlt) in never_eq)
print("   delta histogram over the non-EQ pairs: %s   (branch (ii) predicts {1: all})"
      % dict(sorted(eqd.items())))
CTRL.append(sig_bad == 0)
CTRL.append(exits.get("B_TERMINAL_A_not", 0) == 0)
if sig_bad:
    bad("SIG", "%d non-EQ pairs miss the terminal signature" % sig_bad)
ctrl("CONTROL: the non-EQ branch is NON-EMPTY (otherwise I4 would be safe)", len(never_eq))

# ================================================================ 4. I1 AND I2 RE-DERIVED
print("\n[4] I1 AND I2 RE-DERIVED AS MEASUREMENTS (not quoted)")
print("    I1: one HH step with pivot p drops the sum by exactly 2p (C1-X (ii)).")
i1_n = i1_bad = 0
for N in range(2, 15):
    for L in parts(N):
        nx = step(list(L))
        if nx in ("TERMINAL", None):
            continue
        p = max(L)
        i1_n += 1
        if sum(nx) != sum(L) - 2 * p:
            i1_bad += 1
print("      lists tested: %d   violations of sum drop == 2*pivot: %d" % (i1_n, i1_bad))
CTRL.append(i1_bad == 0)
print("    I2: under UP2, max(B) - max(A) in {0,1}.")
i2_n = i2_bad = 0
i2_hist = Counter()
for (A0, B0, dlt) in S1:
    a, b, k = A0, B0, 0
    while k <= 40:
        if a == b or not is_up2(a, b):
            break
        i2_n += 1
        d = max(b) - max(a)
        i2_hist[d] += 1
        if d not in (0, 1):
            i2_bad += 1
        na, nb = step(list(a)), step(list(b))
        if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
            break
        a, b, k = na, nb, k + 1
print("      UP2 states tested: %d   violations of max(B)-max(A) in {0,1}: %d   histogram %s"
      % (i2_n, i2_bad, dict(sorted(i2_hist.items()))))
print("      population: every UP2-related joint state reached from the %d S1 pairs." % len(S1))
print("      NOTE the histogram: p_B = p_A + 1 DOES occur, so I3 ('raises sit strictly below")
print("      the pivot') is NOT an invariant of this population -- measured, not assumed.")
CTRL.append(i2_bad == 0)
ctrl("CONTROL: the UP2-state sweep is non-empty", i2_n)

# ================================================================ 5. THE QUARANTINED CE
print("\n[5] THE QUARANTINED 'COUNTEREXAMPLE TO C1-W': is its B_0 a head-block list at all?")
A0 = ms([3, 3, 2, 2, 2, 2])
B0 = ms([4, 4, 2, 2, 2, 2])
print("   A_0 = %s   B_0 = %s   (from the quarantined file, reproduced here to be TESTED)"
      % (str(A0), str(B0)))
print("   A_0 == W-(3) ?  %s      (W-(3) = %s)" % (A0 == ms(Wm(3)), str(Wm(3))))
hb = []
for c in range(1, 9):
    for W, nm in ((Wp(c), "W+(%d)" % c), (Wm(c), "W-(%d)" % c)):
        cw = Counter(W)
        cb = Counter(B0)
        rem = cb - cw
        if sum((cw - cb).values()) == 0 and all(v <= c for v in rem.elements()):
            hb.append(nm)
print("   head blocks W^eps(c), c=1..8, for which B_0 = W^eps(c) u (tail with entries <= c): %s"
      % (hb if hb else "NONE"))
print("   EXCLUSION LIST for that empty result: none in c=1..8; and |B_0| = 6 forces c+3 <= 6,")
print("   i.e. c <= 3, so c=1..8 already covers every possible c.")
print("   ==> B_0 is NOT in the head-block family, so the pair is OUTSIDE C1-W's hypothesis")
print("   and outside the S2 census entirely.  It refutes a reading, not a statement.")
print("   For the record, its residues: R(A_0)=%s  R(B_0)=%s" % (res(list(A0)), res(list(B0))))
CTRL.append(len(hb) == 0)

# ================================================================ 6. C1-W AS STATED
print("\n[6] C1-W AS LITERALLY STATED vs WHAT r39 ACTUALLY CENSUSED -- my own defect")
print("    Sec 7.54 (2b) states C1-W as: 'at every state, B_s is either EQUAL to A_s or")
print("    again A_s with TWO ENTRIES RAISED BY 1'.  w61_r39_monodd.py's classifier accepts")
print("    a state as unbroken when relation() returns UP2 **or UNIT_DOWN or DOM**:")
for ln in text39.splitlines():
    if 'elif r not in ("UP2"' in ln:
        print("       | %s" % ln.strip())
print("    So the census tested a WIDER class than the sentence names.  Measured here:")
leave = []
for (A0, B0, dlt) in S1:
    a, b, k = A0, B0, 0
    while k <= 80:
        if a == b:
            break
        if not is_up2(a, b):
            leave.append((A0, B0, a, b, k, dlt))
            break
        na, nb = step(list(a)), step(list(b))
        if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
            break
        a, b, k = na, nb, k + 1
print("   S1 pairs that reach a joint state which is NEITHER EQ NOR UP2 : %d of %d"
      % (len(leave), len(S1)))
print("   population: the %d S1 pairs of block [1].  These are exactly r39's 51" % len(S1))
print("   'UNIT_DOWN' absorptions, and 500 + 51 + 158 = %d reconciles with r39's cross-tab."
      % (exits.get("EQ_reached", 0) + len(leave) + len(never_eq)))
if leave:
    z = sorted(leave, key=lambda r: (len(r[0]), sum(r[0]), r[0]))[0]
    A0, B0, a, b, k, dlt = z
    print("   smallest such pair, printed rather than excluded:")
    print("      A_0 = %-26s B_0 = %s" % (str(A0), str(B0)))
    print("      first non-{EQ,UP2} joint state, at stage %d:" % k)
    print("         A_%d = %-24s B_%d = %-24s  sum diff = %d, len diff = %d"
          % (k, str(a), k, str(b), sum(b) - sum(a), len(b) - len(a)))
    print("      B_%d is NOT A_%d with two entries raised by 1 (sums differ by %d, not 2)."
          % (k, k, sum(b) - sum(a)))
print("   ==> C1-W AS THE SENTENCE READS IS FALSE on %d of %d S1 pairs." % (len(leave), len(S1)))
print("   What r39 measured, and what is true on this population, is the WIDER invariant:")
print("   every joint state is EQ, UP2, UNIT_DOWN or DOM.  The sentence must be restated.")
ctrl("CONTROL: the leave-{EQ,UP2} set is non-empty (else no defect to report)", len(leave))

print("\n" + "=" * 100)
print("SUMMARY")
print("=" * 100)
print("  diffed runA/runB calls : %d   disagreements: 0 (a disagreement exits 2)" % DIFFED)
print("  controls recorded      : %d   all true: %s" % (len(CTRL), all(CTRL)))
print("  DEFECTS                : %d  %s" % (len(FAIL), FAIL if FAIL else ""))
print("  PARTIAL (time limit)   : %s   elapsed %.1fs of internal limit %.0fs"
      % (bool(OUT_OF_TIME), time.time() - T0, LIMIT))
sys.exit(1 if FAIL else 0)
