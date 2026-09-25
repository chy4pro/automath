#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r50 HELD-OUT CHECK -- the four-case decomposition of (MON) re-run on the OTHER
implementation of the walk, and on a range r38 never used.

sec 146: an unexpectedly SHORT resolution is a defect report against the line that
produced it.  (MON) has been open since r38 and this round closes it in one page of
argument.  So the whole of w61_r50_mon.py is re-run here through a walk that shares NO
LINE with it: stepA / runA / runB lifted BY SOURCE TEXT from w61_r29_c1audit.py (RULING
CO'), the same pair r38 itself used to MEASURE (MON).  If r50's Counter walk and its
list walk were both wrong in the same way -- they were written by the same hand today --
this file is what catches it.

It also re-derives the four case identities WITHOUT the c_m shape machinery: case (2a)'s
hh(L') = L and case (2b)'s "hh(L') = L with two (c-1)'s raised to c" are checked as
MULTISET identities, and case (1a)/(1b)'s shape is checked by explicit multiset
subtraction.  Nothing here imports or reads w61_r50_mon.py.

DIRECTION FIXED BEFORE THE RUN: every count below must either reproduce r38/r50 exactly
or expose a defect.  I expect r38's 31766 / 28288 / 3478 and r50's case split
14518 / 10826 / 3625 / 2797 at sum(T) <= 22, and NO structural failure at sum(T) <= 28.

** IT DID NOT COME OUT THAT WAY ON THE FIRST RUN, AND THAT IS THE POINT OF THE FILE. **
Run 1 (kept, w61_r50b_holdout_FAILING_v1.out) reported 1 600 + 121 + 1 structural
failures.  ALL of them are defects in THIS FILE's comparison primitives, not in the
proof: 1 600 of 1 600 have t = c-2, where the expected multiset difference CANCELS, and
121 of 121 plus the 1 have c = 1, where the head block's (c-1)-entries are ZEROS and my
pos() deleted them.  Both are repaired below BY RUNNING, with the failing run kept.
The two diagnoses were checked by a separate breakdown before either was acted on.

Interpreter: .venv/bin/python3.  No SAT, no solver, no exhaustive local search.
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
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

FAIL = []
CTRL = []
DIFFED = 0
PARTIAL = False
LIMIT = 420.0


def over():
    global PARTIAL
    if time.time() - T0 > LIMIT:
        PARTIAL = True
        return True
    return False


def bad(tag, detail):
    FAIL.append("%s  %s" % (tag, detail))
    print("   ** DEFECT %s  %s" % (tag, detail))


def ctrl(name, hits, must_fire=True):
    CTRL.append((name, hits, must_fire))
    ok = (hits > 0) if must_fire else True
    print("   [%s] %-72s hits=%d" % ("ok " if ok else "DEAD", name, hits))
    if must_fire and hits == 0:
        bad("DEAD CONTROL", name)


def known(name, got, want):
    tag = "ok " if got == want else "MISMATCH"
    print("   [%s] KNOWN VALUE %-52s got=%s want=%s" % (tag, name, got, want))
    if got != want:
        bad("KNOWN VALUE MISMATCH", "%s got=%s want=%s" % (name, got, want))


def run(lst):
    """(steps, residue) or (None, None); ABORTS if the two lifted impls disagree."""
    global DIFFED
    a, b = runA(list(lst)), runB(list(lst))
    if a != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (lst, a, b))
        sys.exit(2)
    DIFFED += 1
    return a


def ms(l):
    return tuple(sorted(l, reverse=True))


def pos(l):
    return tuple(sorted([x for x in l if x], reverse=True))


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


def Wp(c):
    return [c] * 3 + [c - 1] * c


def Wm(c):
    return [c] * 2 + [c - 1] * (c + 1)


def L_of(T):
    T = ms(T)
    c = T[0]
    return (Wp(c) if sum(T) % 2 == 0 else Wm(c)) + list(T[1:])


def f_of(T):
    return run(L_of(T))[1]


def one_step(lst):
    """ONE HH step through the LIFTED stepA.  Returns a sorted tuple of positive parts."""
    r = stepA(sorted([x for x in lst if x], reverse=True))
    if r == "TERMINAL":
        return ()
    if r is None:
        return None
    return pos(r)


print("=" * 100)
print("w61 r50 HELD-OUT -- (MON)'s four-case decomposition on the r29 walk (sec 105/%d)" % (145 + 1))
print("=" * 100)
print("interpreter: .venv/bin/python3 ; walk lifted BY SOURCE TEXT from w61_r29_c1audit.py")

# ---------------------------------------------------------------- [0] known values first
print("\n[0] KNOWN VALUES FIRST (sec 148).")
c1u = 0
for m in range(0, 31):
    if m and f_of(tuple([1] * m)) != (m + 1) // 2 + 2:
        c1u += 1
known("r38 Lem C1-U f(1^m)=ceil(m/2)+2, failures", c1u, 0)

NMAX = 22
hist = Counter()
for N in range(1, NMAX + 1):
    for T in parts(N):
        for i in range(len(T)):
            Tp = list(T)
            Tp[i] += 1
            hist[f_of(T) - f_of(ms(Tp))] += 1
known("r38 [3] (MON) population, sum(T)<=22", sum(hist.values()), 31766)
known("r38 [3] (MON) delta 0", hist[0], 28288)
known("r38 [3] (MON) delta 1", hist[1], 3478)
ctrl("CORRUPT: delta in {0} is violated", hist[1])
if set(hist) - set([0, 1]):
    bad("MON", "delta outside {0,1}: %s" % dict(hist))

# ---------------------------------------------------------------- [1] the four identities
print("\n[1] THE FOUR CASE IDENTITIES, checked as MULTISET statements -- no c_m profile,")
print("    no shape() function, no in_R().  Every claim of r50's proof, re-derived here.")


def msub(X, Y):
    """multiset difference both ways: (X\\Y, Y\\X) as sorted tuples, on PADDED lists.

    ** MY OWN DEFECT, CAUGHT BY THIS FILE'S FIRST RUN AND REPAIRED BY RUNNING (sec 81). **
    The first version of this helper called pos() on both sides -- it DELETED the padded
    zeros.  W^eps(1) is (1,1,1,0) / (1,1,0,0): at c = 1 the head block's (c-1)-entries ARE
    zeros, so "two (c-1)'s raised to c" became invisible and case (2b) reported 121
    spurious failures, every one of them at c = 1, plus 1 spurious count-bound failure.
    The failing run is kept at w61_r50b_holdout_FAILING_v1.out; it is not deleted.
    Padding is restored here.  r50_mon.py never had this defect: its shape() reads the
    c_m profile, which is padding-invariant."""
    lx, ly = list(X), list(Y)
    n = max(len(lx), len(ly))
    cx = Counter(lx + [0] * (n - len(lx)))
    cy = Counter(ly + [0] * (n - len(ly)))
    return ms((cx - cy).elements()), ms((cy - cx).elements())


def want(outv, inv):
    """the EXPECTED two-way difference, REDUCED.

    ** SECOND DEFECT OF THE SAME RUN. ** I compared the raw pairs {t, c-1} -> {t+1, c}.
    At t = c-2 the value c-1 stands on BOTH sides and a multiset difference cancels it,
    so the honest expectation is {c-2} -> {c}, not {c-2,c-1} -> {c-1,c}.  1 600 spurious
    case-(1b) failures at sum(T) <= 22, EVERY ONE of them at t = c-2, and 4 312 more on
    the wide range.  Reducing the expectation is the repair."""
    a, b = Counter(outv), Counter(inv)
    common = a & b
    return ms((a - common).elements()), ms((b - common).elements())


def check(NLO, NHI):
    cases = Counter()
    fails = Counter()
    deltas = Counter()
    for N in range(NLO, NHI + 1):
        if over():
            break
        for T in parts(N):
            c = T[0]
            ev = (sum(T) % 2 == 0)
            for i in range(len(T)):
                t = T[i]
                U = ms([T[k] + (k == i) for k in range(len(T))])
                L, Lp = L_of(T), L_of(U)
                d = f_of(T) - f_of(U)
                deltas[d] += 1
                if d not in (0, 1):
                    fails["(MON) ITSELF"] += 1
                if t < c:
                    cs = "1a" if ev else "1b"
                    cases[cs] += 1
                    if len(L) != len(Lp):
                        fails[cs + ":len"] += 1
                    out, inn = msub(L, Lp)
                    if cs == "1a":
                        # one unit moved from a part of size c down to a part of size t
                        if t == c - 1:
                            if (out, inn) != ((), ()):
                                fails["1a:t=c-1 not identical"] += 1
                        else:
                            if (out, inn) != want([c, t], [c - 1, t + 1]):
                                fails["1a:not a c->t transfer"] += 1
                    else:
                        # two units added, at part-sizes t and c-1
                        if (out, inn) != want([t, c - 1], [t + 1, c]):
                            fails["1b:not a (t,c-1) double raise"] += 1
                        # the head-block counting bound, stated directly, ON THE PADDED list
                        S = ms(L)
                        if len(S) < c + 3 or S[c + 2] < c - 1:
                            fails["1b:fewer than c+3 entries >= c-1"] += 1
                        if S[0] != c:
                            fails["1b:max != c"] += 1
                else:
                    cs = "2a" if ev else "2b"
                    cases[cs] += 1
                    if len(Lp) != len(L) + 1:
                        fails[cs + ":len not +1"] += 1
                    if ms(U[1:]) != ms(T[1:]):
                        fails[cs + ":U[1:] != T[1:]"] += 1
                    h = one_step(Lp)
                    if h is None:
                        fails[cs + ":L' not steppable"] += 1
                        continue
                    if cs == "2a":
                        if h != pos(L):
                            fails["2a:hh(L') != L"] += 1
                        if msub(L, list(h) + [0]) != ((), ()):
                            fails["2a:hh(L') != L as a padded multiset"] += 1
                    else:
                        out, inn = msub(L, h)
                        if (out, inn) != want([c - 1, c - 1], [c, c]):
                            fails["2b:hh(L') != L + two (c-1)->c"] += 1
                        S = ms(L)
                        if len(S) < c + 3 or S[c + 2] < c - 1:
                            fails["2b:fewer than c+3 entries >= c-1"] += 1
                    # and the s-gap the proof predicts
                    sL, sLp = run(L)[0], run(Lp)[0]
                    if cs == "2a" and sLp - sL != 1:
                        fails["2a:s(L')-s(L) != 1"] += 1
                    if cs == "2b" and sLp - sL not in (1, 2):
                        fails["2b:s(L')-s(L) outside {1,2}"] += 1
    return cases, fails, deltas


cases, fails, deltas = check(1, NMAX)
print("    sum(T) <= %d : cases %s" % (NMAX, dict(sorted(cases.items()))))
print("                   STRUCTURAL FAILURES %s"
      % (dict(sorted(fails.items())) if fails else "NONE"))
print("                   delta histogram %s" % dict(sorted(deltas.items())))
known("r50 case (1a) at sum(T)<=22", cases["1a"], 14518)
known("r50 case (1b) at sum(T)<=22", cases["1b"], 10826)
known("r50 case (2a) at sum(T)<=22", cases["2a"], 3625)
known("r50 case (2b) at sum(T)<=22", cases["2b"], 2797)
if fails:
    bad("FOUR-CASE (held out)", str(dict(fails)))

# ---------------------------------------------------------------- [2] a range r38 never used
HL, HH = NMAX + 1, NMAX + 6
print("\n[2] HELD-OUT RANGE sum(T) in [%d,%d] -- wider than r38's census and wider than" % (HL, HH))
print("    r50's own held-out block.")
cases2, fails2, deltas2 = check(HL, HH)
print("    cases %s" % dict(sorted(cases2.items())))
print("    STRUCTURAL FAILURES %s" % (dict(sorted(fails2.items())) if fails2 else "NONE"))
print("    delta histogram %s ; instances %d"
      % (dict(sorted(deltas2.items())), sum(deltas2.values())))
if fails2:
    bad("FOUR-CASE (held out, wide)", str(dict(fails2)))
if set(deltas2) - set([0, 1]):
    bad("MON (held out, wide)", str(dict(deltas2)))

# ---------------------------------------------------------------- [3] corrupt controls
print("\n[3] CORRUPT CONTROLS -- each identity must FAIL when its hypothesis is removed.")
c_wrongblock = c_2bfalse = c_nohead = 0
for N in range(1, 15):
    for T in parts(N):
        c = T[0]
        ev = (sum(T) % 2 == 0)
        for i in range(len(T)):
            if T[i] != c:
                continue
            U = ms([T[k] + (k == i) for k in range(len(T))])
            L = L_of(T)
            if ev:
                wrong = Wp(c + 1) + list(U[1:])
                if one_step(wrong) != pos(L):
                    c_wrongblock += 1
            else:
                if one_step(L_of(U)) != pos(L):
                    c_2bfalse += 1
ctrl("CORRUPT: case (2a) with the WRONG head block -- hh != L", c_wrongblock)
ctrl("CORRUPT: case (2b) does NOT satisfy hh(L') = L", c_2bfalse)
# the head block is what supplies c+3 entries >= c-1: strip it and count how often the
# counting bound dies on the SAME tails.
for N in range(2, 17):
    for T in parts(N):
        c = T[0]
        S = pos(T)
        if len(S) < c + 3 or S[c + 2] < c - 1:
            c_nohead += 1
ctrl("the c+3-entries-of-height-c-1 bound FAILS on bare partitions (no head block)",
     c_nohead)

# ---------------------------------------------------------------- [4] the chain to C1-M
print("\n[4] THE CHAIN r38 BUILT, END TO END AND THROUGH M(lam) ITSELF -- not through the")
print("    closed form.  C1-S says residue(M(lam)) = f(lam[2:]); (MON) + C1-U then give")
print("    C1-M: residue(M(lam)) <= ceil(k/2)+1.  BOTH re-measured here, on the r29 walk.")


def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)


c1s_n = c1s_bad = c1m_n = c1m_bad = 0
attained = set()
for N in range(2, 25):
    if over():
        break
    for lam in parts(N):
        k = len(lam)
        if k < 2:
            continue
        r = run(M(lam))[1]
        if r is None:
            continue
        c1s_n += 1
        pred = f_of(lam[2:]) if lam[2:] else 2
        if r != pred:
            c1s_bad += 1
        c1m_n += 1
        if r > (k + 1) // 2 + 1:
            c1m_bad += 1
        if r == (k + 1) // 2 + 1:
            attained.add(k)
print("    C1-S  residue(M(lam)) == f(lam[2:]) : %d instances, failures %d" % (c1s_n, c1s_bad))
print("    C1-M  residue(M(lam)) <= ceil(k/2)+1 : %d instances, failures %d" % (c1m_n, c1m_bad))
print("    C1-M's bound ATTAINED at k = %s" % sorted(attained))
if c1s_bad:
    bad("C1-S", "%d failures" % c1s_bad)
if c1m_bad:
    bad("C1-M", "%d failures" % c1m_bad)
# ** MY OWN MIS-DECLARED CONTROL, CAUGHT ON THIS FILE'S THIRD RUN. ** The first version of
# the line below was named "the tightened bound ceil(k/2) IS violated" and then counted the
# number of k at which C1-M's own bound is ATTAINED (23).  A control whose name and body
# describe different quantities is a DEAD control that happens to print a number -- r48 (g)
# item 3, same species.  It now counts what it says it counts.
tight_viol = 0
for N in range(2, 21):
    for lam in parts(N):
        k = len(lam)
        if k < 2:
            continue
        r = run(M(lam))[1]
        if r is not None and r > (k + 1) // 2:
            tight_viol += 1
ctrl("CORRUPT: the TIGHTENED bound ceil(k/2) is violated (C1-M is tight)", tight_viol)
ctrl("CONTROL: C1-M's own bound is ATTAINED, at this many distinct k", len(attained))

print("\n" + "=" * 100)
print("SELF-AUDIT")
print("  diffed runA/runB calls : %d  (any disagreement would have exited 2)" % DIFFED)
print("  controls               : %d declared, %d firing"
      % (len(CTRL), sum(1 for _, h, mf in CTRL if (h > 0) or not mf)))
print("  defects                : %d" % len(FAIL))
for x in FAIL:
    print("    - %s" % x)
print("  PARTIAL                : %s" % PARTIAL)
print("  elapsed                : %.1fs" % (time.time() - T0))
print("=" * 100)
sys.exit(1 if FAIL else 0)
