#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r42 -- A MECHANISM FOR SHAPE S2.

WHERE THIS STARTS.  prompts/w61_S2_SPEC.md (r41) proves that S2 is NOT a UP2 move: the two
lists have different LENGTHS (Dlen = +1) and different sums (Dsum = 2c+4), so Candidate
Lemma C1-W -- a statement about stepping a UP2 pair in lockstep -- has NO CONTENT on S2.
Consequence recorded in draft Sec 7.56 (c): the odd half is C1-W (S1, 3057 of 4073) PLUS
(S2) (1016 of 4073), and (S2) had NO MECHANISM.

THE CLAIM THIS ROUND TESTS (owner-w61, r42), by hand first and then by machine:

  LEMMA S2-STEP.  For every c >= 1 and every weakly-decreasing tail with entries in [0,c],
  ONE Havel-Hakimi step applied to L' = W+(c+1) u tail never aborts, and lands on
        L'_1  =  L  with TWO entries equal to c-1 replaced by c,
  where L = W-(c) u tail.  In particular L'_1 and L have the SAME LENGTH and
  sum(L'_1) = sum(L) + 2, i.e. (L, L'_1) IS a UP2 pair.

  COROLLARY S2-RED.  R is a trajectory invariant (Lemma C1-X corollary, PROVED, Sec 7.55 c),
  so R(L') = R(L'_1) and therefore
        delta_S2 := R(L) - R(L')  =  R(L) - R(L'_1)  =  the UP2-delta of the pair (L, L'_1).
  Equivalently s(L') = s(L'_1) + 1, so "s(L') - s(L) in {1,2}" becomes "s(L'_1) - s(L) in {0,1}".

  So (S2) is not a second, mechanism-free problem.  It is the SAME lockstep relation-persistence
  statement C1-W is, evaluated on a DIFFERENT starting pair, reached by one step.

HAND PROOF (this is arithmetic, not a census; the script MEASURES it, it does not establish it):
  W+(c+1) = [c+1]*3 + [c]*(c+1)                   len c+4
  W-(c)   = [c]*2   + [c-1]*(c+1)                 len c+3
  tail entries are <= c, so in L' the pivot is d = c+1 and
      rest = [c+1]*2 + [c]*(c+1+m) + tail_{<c}    where m = #{tail entries = c}
  |rest| = c+3+|tail| >= c+1 = d, so the step does not abort on length; and every entry of
  blk = rest[:c+1] = [c+1]*2 + [c]*(c-1) is >= c >= 1, so it does not abort on a zero either.
  Subtracting 1 from blk gives [c]*2 + [c-1]*(c-1); the untouched remainder of rest is
  [c]*(2+m) + tail_{<c}.  As a multiset
      L'_1 = {c: 4+m} u {c-1: c-1} u tail_{<c}
      L    = {c: 2+m} u {c-1: c+1} u tail_{<c}
  which differ exactly by moving two copies of c-1 up to c.  L has c+1 >= 2 copies of c-1, so
  the move is always available.  QED

WHAT THIS SCRIPT DOES
  [0] controls, corrupt companions, tool controls -- all fired before any verdict
  [1] reproduce the r41 S2 census (population check: 1016 instances / 686 distinct (c,tail))
  [2] LEMMA S2-STEP measured on every distinct (c,tail) of the census
  [3] COROLLARY S2-RED -- the residue/step bookkeeping, reconciled against the census deltas
  [4] the lemma OUTSIDE the census range: an independent (c,tail) sweep, parity-free
  [5] the LOCKSTEP DICHOTOMY run on the S2-derived pairs, with the SAME classifier that
      certified C1-W (relation() from w61_r39_monodd.py) -- doctrine Sec 59
  [6] WHICH two entries are raised: the S2 sub-family vs the S1 sub-family
  [7] self-audit

RULING CO': the step process is extracted BY SOURCE TEXT from w61_r29_c1audit.py and run in two
independent implementations diffed on every call.  W+/W-/head/L and relation() are extracted BY
SOURCE TEXT from w61_r39_monodd.py.  Nothing is retyped, so census/lemma transcription drift is
impossible.  No SAT, no solver, no exhaustive search of an infeasible space -- every sweep below
is a census over an explicitly stated finite population.
INTERNAL HARD LIMIT: every loop checks the clock and prints PARTIAL rather than running on.
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 90.0          # seconds, internal.  Never rely on an external timeout.
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
SRC39 = ROOT / "problems/wowii/w61_r39_monodd.py"
text = SRC.read_text()
text39 = SRC39.read_text()


def grab(t, name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---|print|NMAX|absorb))" % re.escape(name),
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


def steps_of(lst):
    return run(lst)[0]


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


# ---- DEFINITIONS LIFTED BY SOURCE TEXT FROM w61_r39_monodd.py (no retyping) -------------
ns39 = {"ms": ms, "res": res, "sorted": sorted, "Counter": Counter}
_defs = "\n".join(grab(text39, n) for n in ("Wp", "Wm", "head_of", "L_of", "relation"))
exec(compile(_defs, str(SRC39), "exec"), ns39)
Wp, Wm, head_of, L_of, relation = (ns39["Wp"], ns39["Wm"], ns39["head_of"],
                                   ns39["L_of"], ns39["relation"])
FC = {}


def f(T):
    T = ms(T)
    if T not in FC:
        FC[T] = 2 if not T else res(L_of(T))
    return FC[T]


print("=" * 100)
print("w61 r42 -- A MECHANISM FOR SHAPE S2:  ONE HH STEP ON L' LANDS ON A UP2 PARTNER OF L")
print("=" * 100)
print("definitions Wp/Wm/head_of/L_of/relation lifted by SOURCE TEXT from w61_r39_monodd.py;")
print("stepA/runA/runB lifted by SOURCE TEXT from w61_r29_c1audit.py.  Nothing retyped.")
print("relation() is THE CLASSIFIER THAT CERTIFIED C1-W -- doctrine Sec 59: an invariant ships")
print("with the classifier that certified it, so the S2 pairs are judged by the same one.")

# ================================================================ 0. CONTROLS
print("\n[0] CONTROLS -- fired on the feature, before any verdict (RULING CZ')")


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append(ok)
    print("   %-64s hits=%-8s %s" % (name, hits, "OK" if ok else "** CONTROL DID NOT FIRE"))
    if not ok:
        bad("CONTROL", name)


def known(name, got, exp):
    CTRL.append(got == exp)
    print("   known-value  %-36s = %-12s expect %-12s %s"
          % (name, got, exp, "OK" if got == exp else "** MISMATCH"))
    if got != exp:
        bad("KNOWN", "%s got %s expect %s" % (name, got, exp))


def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)


known("residue(M((5,4,3)))", res(M((5, 4, 3))), 2)
known("[1,1,0,0] boundary", run([1, 1, 0, 0]), (1, 3))
known("|W-(c)| = c+3, c=1..14", [len(Wm(c)) - c - 3 for c in range(1, 15)], [0] * 14)
known("|W+(c)| = c+3, c=1..14", [len(Wp(c)) - c - 3 for c in range(1, 15)], [0] * 14)
known("sum W-(c) = c*c+2c-1, c=1..14",
      [sum(Wm(c)) - (c * c + 2 * c - 1) for c in range(1, 15)], [0] * 14)
known("sum W+(c) = c*(c+2), c=1..14",
      [sum(Wp(c)) - c * (c + 2) for c in range(1, 15)], [0] * 14)
n_ab = sum(1 for L in ([3, 1, 1], [5, 1], [4, 2, 1], [2]) if res(L) is None)
known("MUST_ABORT inputs aborting", n_ab, 4)
known("relation() on an EQ pair", relation((2, 1), (2, 1)), "EQ")
known("relation() on a hand UP2 pair", relation((2, 1, 1), (2, 2, 2)), "UP2")
# NOTE (owner-w61 r42, defect 1 of this round, caught by this control on its FIRST run):
# I first wrote the expectation for relation((3,1),(2,2)) as "DOM".  The classifier returns
# UNIT_DOWN, and the CLASSIFIER IS RIGHT -- (3,1)->(2,2) moves one unit from a larger entry
# to a smaller one, which is precisely what UNIT_DOWN names.  My expectation was wrong, not
# the tool.  Corrected here, and a genuinely-DOM pair added beside it so the DOM branch is
# still exercised.  Recording rather than deleting, per Sec 7.55 (d) "trace, do not strike".
known("relation() on a hand UNIT_DOWN pair", relation((3, 1), (2, 2)), "UNIT_DOWN")
known("relation() on a hand DOM pair", relation((4, 1, 1), (2, 2, 2)), "DOM")

# TOOL CONTROL: residue is a trajectory invariant (the fact Corollary S2-RED rests on)
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
    bad("INVARIANT", "residue not step-invariant -- Corollary S2-RED would be unfounded")

# CORRUPT COMPANION: the step COUNT is not invariant (so [3]'s s(L')=s(L'_1)+1 is content)
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
ctrl("CORRUPT: 'the step COUNT is also invariant' is violated", cnt_bad)

# ================================================================ 1. CENSUS REPRODUCED
print("\n[1] THE S2 CENSUS REPRODUCED -- population check against r41 / draft Sec 7.54 (c)")
print("    population: MON instances (T, T+e_i), sum(T) ODD, over all partitions T with")
print("    sum(T) <= 18, i = any index.  Instances where either side's HH run ABORTS are")
print("    skipped on BOTH sides and counted nowhere else.  Exclusion list for every 0: none.")
NMAX = 18
shape_hist = Counter()
delta_hist = {}
S2 = []
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
            a, b = f(T), f(U)
            if a is None or b is None:
                continue
            shape_hist[sh] += 1
            delta_hist.setdefault(sh, Counter())[a - b] += 1
            rec = (ms(T), ms(U), T[0], ms(T[1:]), a, b)
            (S2 if sh == "S2_max_rises" else S1).append(rec)
for sh in sorted(shape_hist):
    print("   %-22s instances=%-7d delta = f(T)-f(T+e_i) histogram %s"
          % (sh, shape_hist[sh], dict(sorted(delta_hist[sh].items()))))
print("   total instances = %d" % sum(shape_hist.values()))
CT = sorted(set((r[2], r[3]) for r in S2))
print("   distinct (c, tail) pairs among the S2 instances: %d" % len(CT))
print("   POPULATION for every count in blocks [2],[3],[5],[6]: these %d distinct (c,tail)"
      % len(CT))
ctrl("CORRUPT: 'delta is always 0' is violated on S2",
     sum(v for k, v in delta_hist.get("S2_max_rises", {}).items() if k != 0))

# ================================================================ 2. LEMMA S2-STEP
print("\n[2] LEMMA S2-STEP, MEASURED on every distinct (c,tail) of block [1]")
print("    claim: ONE HH step on L' = W+(c+1) u tail never aborts and yields L'_1, which is")
print("    L = W-(c) u tail with exactly TWO entries equal to c-1 replaced by c.")
n_ct = 0
step_ok = 0
shape_ok = 0
updiff_ok = 0
rel_up2 = Counter()
len_eq = 0
sum_p2 = 0
lemma_bad = []
PAIRS = []          # (c, tail, L, Lp, Lp1)
for (c, tail) in CT:
    if over():
        break
    n_ct += 1
    L = ms(list(Wm(c)) + list(tail))
    Lp = ms(list(Wp(c + 1)) + list(tail))
    s1 = step(list(Lp))
    if s1 in ("TERMINAL", None):
        lemma_bad.append(("STEP_ABORTED", c, tail))
        continue
    step_ok += 1
    up = Counter(s1) - Counter(L)
    dn = Counter(L) - Counter(s1)
    if dict(up) == {c: 2} and dict(dn) == {c - 1: 2}:
        shape_ok += 1
    else:
        lemma_bad.append(("SHAPE", c, tail, dict(up), dict(dn)))
    if sum(up.values()) == 2 and sum(dn.values()) == 2:
        updiff_ok += 1
    if len(s1) == len(L):
        len_eq += 1
    if sum(s1) == sum(L) + 2:
        sum_p2 += 1
    rel_up2[relation(L, s1)] += 1
    PAIRS.append((c, tail, L, Lp, s1))
print("   (c,tail) pairs examined                                    : %d of %d" % (n_ct, len(CT)))
print("   one HH step on L' TERMINATES-or-ABORTS (must be 0)          : %d"
      % (n_ct - step_ok))
print("   L'_1 = L with exactly two (c-1) -> c  (multiset difference) : %d of %d"
      % (shape_ok, n_ct))
print("   len(L'_1) == len(L)                                        : %d of %d" % (len_eq, n_ct))
print("   sum(L'_1) == sum(L) + 2                                    : %d of %d" % (sum_p2, n_ct))
print("   relation(L, L'_1) as judged by THE CERTIFYING CLASSIFIER    : %s"
      % dict(sorted(rel_up2.items())))
print("   EXCLUSION LIST for the 0 above (aborts/terminals): none -- every one of the %d"
      % len(CT))
print("   distinct (c,tail) pairs of block [1] is stepped; nothing skipped, nothing counted")
print("   elsewhere.  Failures, if any, are printed rather than excluded: %s"
      % (lemma_bad[:3] if lemma_bad else "[] (none)"))
if lemma_bad:
    bad("LEMMA", "S2-STEP failed on %d pairs" % len(lemma_bad))

# CORRUPT COMPANIONS for [2] -- the test must not be vacuous
c_raw_up2 = sum(1 for (c, tail, L, Lp, s1) in PAIRS if relation(L, Lp) == "UP2")
print("   CORRUPT COMPANION 1: is L' ITSELF a UP2 partner of L?      : %d of %d  (r41: never)"
      % (c_raw_up2, len(PAIRS)))
CTRL.append(c_raw_up2 == 0)
c_three = sum(1 for (c, tail, L, Lp, s1) in PAIRS
              if dict(Counter(s1) - Counter(L)) == {c: 3})
print("   CORRUPT COMPANION 2: 'THREE entries raised' instead of two  : %d of %d  (must be 0)"
      % (c_three, len(PAIRS)))
CTRL.append(c_three == 0)
c_two_steps = 0
for (c, tail, L, Lp, s1) in PAIRS:
    s2v = step(list(s1))
    if s2v not in ("TERMINAL", None) and relation(L, s2v) == "UP2":
        c_two_steps += 1
print("   CORRUPT COMPANION 3: TWO steps on L' also lands UP2 with L  : %d of %d  (must be small"
      % (c_two_steps, len(PAIRS)))
print("                        -- if it were %d of %d the step count would be arbitrary)"
      % (len(PAIRS), len(PAIRS)))
ctrl("CORRUPT COMPANION 3 does NOT hold universally", len(PAIRS) - c_two_steps)

# ================================================================ 3. COROLLARY S2-RED
print("\n[3] COROLLARY S2-RED -- the residue / step bookkeeping, on the same %d pairs" % len(PAIRS))
res_inv = 0
s_shift = Counter()
delta_match = 0
delta_hist_red = Counter()
both_term = 0
red_bad = []
for (c, tail, L, Lp, s1) in PAIRS:
    if over():
        break
    rL, rLp, rS = res(list(L)), res(list(Lp)), res(list(s1))
    if rLp is None or rL is None:
        continue
    both_term += 1
    if rLp == rS:
        res_inv += 1
    sL, sLp, sS = steps_of(list(L)), steps_of(list(Lp)), steps_of(list(s1))
    s_shift[sLp - sS] += 1
    d_spec = rL - rLp
    d_up2 = rL - rS
    delta_hist_red[d_spec] += 1
    if d_spec == d_up2:
        delta_match += 1
    else:
        red_bad.append((c, tail, d_spec, d_up2))
print("   pairs where BOTH runs terminate                            : %d of %d"
      % (both_term, len(PAIRS)))
print("   R(L') == R(L'_1)   (trajectory invariance, C1-X corollary)  : %d of %d"
      % (res_inv, both_term))
print("   s(L') - s(L'_1) histogram (must be all 1: one step)         : %s"
      % dict(sorted(s_shift.items())))
print("   delta_S2 = R(L)-R(L')  EQUALS  the UP2-delta R(L)-R(L'_1)   : %d of %d"
      % (delta_match, both_term))
print("   delta_S2 histogram over the %d distinct (c,tail) pairs      : %s"
      % (both_term, dict(sorted(delta_hist_red.items()))))
print("   violations of 0 <= delta_S2 <= 1                            : %d"
      % sum(v for k, v in delta_hist_red.items() if not 0 <= k <= 1))
print("   EXCLUSION LIST for that 0: none among the %d pairs that terminate on both sides;" % both_term)
print("   %d pairs abort and are counted nowhere else." % (len(PAIRS) - both_term))
if red_bad:
    bad("S2-RED", "delta mismatch on %d pairs: %s" % (len(red_bad), red_bad[:3]))

# ================================================================ 4. OUTSIDE THE CENSUS RANGE
print("\n[4] THE LEMMA OUTSIDE THE CENSUS RANGE -- an INDEPENDENT (c,tail) sweep")
print("    population: every c in [1,12] and every weakly-decreasing tail of length <= 4 with")
print("    entries in [1,c].  This sweep is PARITY-FREE (it does NOT impose c+sum(tail) odd),")
print("    so it also tests whether S2-STEP needs the parity hypothesis at all.  It is a")
print("    CENSUS over that stated finite population, not a search.")


def tails(c, maxlen):
    out = [()]
    cur = [()]
    for _ in range(maxlen):
        nxt = []
        for t in cur:
            hi = t[-1] if t else c
            for v in range(hi, 0, -1):
                nxt.append(t + (v,))
        out.extend(nxt)
        cur = nxt
    return out


w_n = w_ok = w_abort = 0
w_odd = w_even = 0
w_bad = []
for c in range(1, 13):
    if over():
        break
    for tail in tails(c, 4):
        w_n += 1
        L = ms(list(Wm(c)) + list(tail))
        Lp = ms(list(Wp(c + 1)) + list(tail))
        s1 = step(list(Lp))
        if s1 in ("TERMINAL", None):
            w_abort += 1
            w_bad.append(("STEP_ABORTED", c, tail))
            continue
        up = Counter(s1) - Counter(L)
        dn = Counter(L) - Counter(s1)
        if dict(up) == {c: 2} and dict(dn) == {c - 1: 2}:
            w_ok += 1
            if (c + sum(tail)) % 2:
                w_odd += 1
            else:
                w_even += 1
        else:
            w_bad.append(("SHAPE", c, tail, dict(up), dict(dn)))
print("   (c,tail) pairs in this population                          : %d" % w_n)
print("   LEMMA S2-STEP holds (one step -> two (c-1) raised to c)     : %d of %d" % (w_ok, w_n))
print("      of those, c+sum(tail) ODD (i.e. genuine S2 instances)    : %d" % w_odd)
print("      of those, c+sum(tail) EVEN (OUTSIDE S2's hypothesis)     : %d" % w_even)
print("   the one HH step on L' aborted or terminated                 : %d" % w_abort)
print("   counterexamples, printed rather than excluded               : %s"
      % (w_bad[:3] if w_bad else "[] (none)"))
print("   EXCLUSION LIST for those 0s: none -- every (c,tail) in the stated population is")
print("   tested; c > 12 and |tail| > 4 are OUT OF POPULATION and are claimed nowhere.")
if w_bad:
    bad("LEMMA-WIDE", "S2-STEP failed outside the census on %d pairs" % len(w_bad))
ctrl("the wide sweep contains EVEN-parity pairs (so it really is wider than S2)", w_even)

# ================================================================ 5. LOCKSTEP ON S2 PAIRS
print("\n[5] THE LOCKSTEP DICHOTOMY, RUN ON THE S2-DERIVED PAIRS (L, L'_1)")
print("    Same procedure and SAME CLASSIFIER as the C1-W census (relation() from")
print("    w61_r39_monodd.py).  A joint state is UNBROKEN when relation() returns EQ, UP2,")
print("    UNIT_DOWN or DOM -- that is the WIDER, TRUE form established in draft Sec 7.56 (j),")
print("    not the narrow 'EQ or UP2' sentence, which is FALSE on 51 of the 709 S1 pairs.")
ACCEPT = ("EQ", "UP2", "UNIT_DOWN", "DOM")
lk_n = 0
lk_persist = 0
lk_break = []
exit_kind = Counter()
rel_seen = Counter()
branch_delta = Counter()
for (c, tail, L, Lp, s1) in PAIRS:
    if over():
        break
    if res(list(L)) is None or res(list(s1)) is None:
        continue
    lk_n += 1
    a, b, k, broke = L, s1, 0, False
    while k <= 200:
        r = relation(a, b)
        rel_seen[r] += 1
        if r not in ACCEPT:
            broke = True
            lk_break.append((c, tail, a, b, k, r))
            break
        if a == b:
            exit_kind["EQ_reached"] += 1
            break
        na, nb = step(list(a)), step(list(b))
        if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
            exit_kind["a_or_b_terminal"] += 1
            break
        a, b, k = na, nb, k + 1
    if not broke:
        lk_persist += 1
        branch_delta[res(list(L)) - res(list(s1))] += 1
print("   S2-derived pairs stepped in lockstep                       : %d of %d"
      % (lk_n, len(PAIRS)))
print("   RELATION-PERSISTENCE holds (never leaves {EQ,UP2,UNIT_DOWN,DOM}) : %d of %d"
      % (lk_persist, lk_n))
print("   pairs that BREAK the relation, printed rather than excluded : %d  %s"
      % (len(lk_break), lk_break[:2] if lk_break else "[] (none)"))
print("   EXCLUSION LIST for that 0: none among the %d stepped; pairs where either run" % lk_n)
print("   aborts are excluded and counted nowhere else (%d of %d)." % (len(PAIRS) - lk_n, len(PAIRS)))
print("   joint-state relations SEEN over the whole lockstep          : %s"
      % dict(sorted(rel_seen.items())))
narrow = sum(v for k, v in rel_seen.items() if k not in ("EQ", "UP2"))
print("   joint states needing the WIDER classes (UNIT_DOWN or DOM)   : %d of %d"
      % (narrow, sum(rel_seen.values())))
print("   -- for comparison, on the S1 population the narrow 'EQ or UP2' form FAILS on 51 of")
print("   709 pairs (draft Sec 7.56 j).  Whether it fails on the S2-derived population is")
print("   answered by the line above, on the %d joint states this block visited."
      % sum(rel_seen.values()))
print("   how the lockstep exited                                     : %s"
      % dict(sorted(exit_kind.items())))
print("   delta on the persisting pairs                               : %s"
      % dict(sorted(branch_delta.items())))
if lk_break:
    bad("LOCKSTEP", "relation broke on %d S2-derived pairs" % len(lk_break))
ctrl("CORRUPT: 'every S2 lockstep reaches EQ' is violated (else the dichotomy is one-sided)",
     lk_n - exit_kind.get("EQ_reached", 0))

# ================================================================ 6. WHICH ENTRIES ARE RAISED
print("\n[6] WHICH TWO ENTRIES ARE RAISED -- the S2 sub-family vs the S1 sub-family")
print("    r39's finding (draft Sec 7.54 e) is that WHICH pair of entries is raised, not how")
print("    many copies of the maximum exist, is what excludes the counterexamples.  So the")
print("    two sub-families must be told apart explicitly.")
print("   S2-derived pair (L, L'_1): the two raised entries are BOTH copies of c-1, both in")
print("   the head block.  Measured as the multiset difference in [2]: %d of %d."
      % (shape_ok, n_ct))
s1_head_tail = 0
s1_n = 0
for (T, U, c, tail, a, b) in S1:
    if over():
        break
    Ls = ms(L_of(T))
    Us = ms(L_of(U))
    up = Counter(Us) - Counter(Ls)
    dn = Counter(Ls) - Counter(Us)
    if sum(up.values()) == 2 and sum(dn.values()) == 2:
        s1_n += 1
        # one raise is the head block's W-(c) -> W+(c) (a c-1 becomes c); the other is in tail
        if up[c] >= 1 and dn[c - 1] >= 1:
            s1_head_tail += 1
print("   S1 pair (L(T), L(T+e_i)): one raise is the head flip W-(c)->W+(c) (a c-1 -> c) and")
print("   the OTHER is a tail part T_j -> T_j+1 : %d of %d S1 instances whose difference is a"
      % (s1_head_tail, s1_n))
print("   2-up/2-down multiset move.")
print("   population: the %d S1 instances of block [1]." % len(S1))
print("   ==> the two sub-families are DISJOINT in raise-position: S2 raises two entries at the")
print("   SAME level (c-1, both in the head), S1 raises one in the head and one in the tail.")
print("   Consequence stated plainly: the reduction does NOT put S2 inside C1-W's census")
print("   population.  It puts it inside the SAME STATEMENT on an adjacent population.")

# ================================================================ 7. SELF-AUDIT
print("\n[7] SELF-AUDIT")
print("   diffed runA/runB calls : %d   disagreements: 0 (a disagreement exits(2))" % DIFFED)
print("   controls               : %d   all firing: %s" % (len(CTRL), all(CTRL)))
print("   defects                : %d   %s" % (len(FAIL), FAIL if FAIL else ""))
print("   elapsed                : %.1f s   internal limit %.0f s" % (time.time() - T0, LIMIT))
print("   PARTIAL                : %s" % bool(OUT_OF_TIME))
print("   interpreter            : %s" % sys.executable)
print("   NO SAT, NO solver, NO exhaustive search of an infeasible space.  Every sweep above is")
print("   a census over the finite population named beside it.")
print("=" * 100)
print("EXIT=%d" % (1 if (FAIL or not all(CTRL) or OUT_OF_TIME) else 0))
sys.exit(1 if (FAIL or not all(CTRL) or OUT_OF_TIME) else 0)
