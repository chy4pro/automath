#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r43 -- TWO MEASUREMENTS THAT DECIDE WHAT THE ENGINE BRIEFS SHOULD SAY.

WHY THIS ROUND EXISTS.  The r43 task book asks for engine briefs (E03/E05 RESTATE, E07/E10
draft).  A brief must be self-contained and must not withhold anything the line holds -- so
before writing four briefs I must know two things that the ledger does NOT currently answer,
and neither may be guessed:

  [A] THE C1-Z COVERAGE QUESTION.
      Sec 7.55 (c) Theorem C1-Z: IF the lockstep dichotomy holds for every head-block pair
      THEN (MON) holds with delta in {0,1}, and both values are computed (C1-X, C1-Y).
      Sec 7.56 (i) derives the two branches:
         1. EQ occurs at a finite stage  ==> EQ absorbing ==> delta = 0
         2. EQ never occurs             ==> lockstep ends with A_s = 0^r and
                                            B_s = (1,1,0^{r-2})  ==> C1-Y ==> delta = 1
      Branch 2's proof uses "B_s is A_s with TWO ENTRIES RAISED BY 1", i.e. it needs the
      NARROW relation (UP2) at the exit stage.
      But Sec 7.56 (j) measured that 51 of the 709 S1 pairs reach a joint state that is
      NEITHER EQ NOR UP2, and the open obligation in Sec 7.56 (k) is stated with the WIDE
      class {EQ, UP2, UNIT_DOWN, DOM}.
      ==> THE HYPOTHESIS THAT C1-Z's PROOF NEEDS AND THE HYPOTHESIS THE LINE CALLS OPEN ARE
          NOT THE SAME HYPOTHESIS.  What happens on those 51 pairs is not recorded anywhere.
      This block measures it.  It is a question about a PROVISIONAL result of my own.

  [B] THE (RH) PIVOT-MAJORIZATION ROUTE.
      ENGINE_BACKLOG E05 asks for (RH) "via majorization / dominance order".  That framing is
      vague as written, and Sec 7.55 (b) already supplies a SHARP one that nobody has tested:
         C1-X: R(pi) = n - s(pi)     and     2 * sum(pivots) = sum(pi).
         A unit transfer down preserves BOTH n and sum(pi).  So p(pi) and p(pi') are two
         partitions OF THE SAME INTEGER sum(pi)/2, and
             (RH)  <=>  s(pi) <= s(pi')  <=>  p(pi) has no more parts than p(pi').
         For partitions of a fixed integer, a ⪰ b (dominance) IMPLIES #parts(a) <= #parts(b)
         (conjugate: a* ⪯ b*, and #parts(a) = a*_1).  So
             (PIVOT-MAJ)   pi' ⪯ pi   ==>   p(pi) ⪰ p(pi')      would IMPLY (RH).
      Is (PIVOT-MAJ) true?  Nobody has looked.  If it is false, E05 must NOT be sent at it.
      This block measures (PIVOT-MAJ) and (RH) itself on the same population, so the brief
      carries a measured fact instead of a hope.

RULING CO': stepA/runA/runB are extracted BY SOURCE TEXT from w61_r29_c1audit.py and run as
two independent implementations diffed on every call.  Wp/Wm/head_of/L_of/relation are
extracted BY SOURCE TEXT from w61_r39_monodd.py -- relation() is THE CLASSIFIER THAT CERTIFIED
C1-W (doctrine Sec 59).  Nothing is retyped.
No SAT, no solver, no exhaustive search of an infeasible space: every sweep below is a census
over an explicitly stated finite population, seconds of arithmetic.
INTERNAL HARD LIMIT: every loop checks the clock and prints PARTIAL rather than running on.
Interpreter: .venv/bin/python3 (pure Python; neither sympy nor networkx is imported).
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 120.0          # seconds, internal.  Never rely on an external timeout.
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
print("w61 r43 -- [A] WHAT HAPPENS ON THE 51 PAIRS C1-Z's PROOF DOES NOT REACH")
print("           [B] IS THE PIVOT SEQUENCE MAJORIZATION-MONOTONE?  ((RH) route for E05)")
print("=" * 100)
print("stepA/runA/runB lifted by SOURCE TEXT from w61_r29_c1audit.py;")
print("Wp/Wm/head_of/L_of/relation lifted by SOURCE TEXT from w61_r39_monodd.py.")
print("relation() is the classifier that certified C1-W -- doctrine Sec 59.")


# ================================================================ 0. CONTROLS
print("\n[0] CONTROLS -- fired on the feature, before any verdict (RULING CZ')")


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append(ok)
    print("   %-66s hits=%-8s %s" % (name, hits, "OK" if ok else "** CONTROL DID NOT FIRE"))
    if not ok:
        bad("CONTROL", name)


def known(name, got, exp):
    CTRL.append(got == exp)
    print("   known-value  %-40s = %-14s expect %-14s %s"
          % (name, got, exp, "OK" if got == exp else "** MISMATCH"))
    if got != exp:
        bad("KNOWN", "%s got %s expect %s" % (name, got, exp))


known("[1,1,0,0] boundary (steps,residue)", run([1, 1, 0, 0]), (1, 3))
known("|W-(c)| = c+3, c=1..14", [len(Wm(c)) - c - 3 for c in range(1, 15)], [0] * 14)
known("|W+(c)| = c+3, c=1..14", [len(Wp(c)) - c - 3 for c in range(1, 15)], [0] * 14)
known("relation() on an EQ pair", relation((2, 1), (2, 1)), "EQ")
known("relation() on a hand UP2 pair", relation((2, 1, 1), (2, 2, 2)), "UP2")
# r42 (h) 1: my own control had DOM here and the classifier was right with UNIT_DOWN.
# The corrected expectation and a genuinely-DOM companion are BOTH kept, per Sec 7.57 (h).
known("relation() on a unit-transfer-down pair", relation((3, 1), (2, 2)), "UNIT_DOWN")
known("relation() on a genuinely DOM pair", relation((4, 1, 1), (2, 2, 2)), "DOM")
n_ab = sum(1 for L in ([3, 1, 1], [5, 1], [4, 2, 1], [2]) if res(L) is None)
known("MUST_ABORT inputs aborting", n_ab, 4)
# C1-Y, the lemma E07 was originally aimed at, checked as a KNOWN VALUE rather than re-proved:
cy = [(res([0] * r), res([1, 1] + [0] * (r - 2))) for r in range(2, 13)]
known("C1-Y: R(0^r)=r and R(1,1,0^{r-2})=r-1, r=2..12",
      [(a, b) for (a, b) in cy], [(r, r - 1) for r in range(2, 13)])


# ================================================================ 1. REBUILD THE 709
print("\n[1] REBUILD THE S1 LOCKSTEP POPULATION -- generator lifted from w61_r39_monodd.py")
print("    Population: pairs (L(T), L(T+e_i)) with sum(T) ODD, sum(T) <= 14, shape S1")
print("    (i.e. the raised part is NOT the maximum), both residues defined.")
NMAX = 18
S1 = []
S1_meta = []
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
            if sh == "S1_head_parity_flip" and sum(T) <= 14:
                S1.append((ms(L_of(T)), ms(L_of(U)), a - b))
                S1_meta.append((T, U))
print("   S1 pairs rebuilt: %d   (r39 printed 709 for this same population)" % len(S1))
ctrl("CONTROL: the S1 population is non-empty", len(S1))


# ================================================================ 2. FULL LOCKSTEP WALK
print("\n[2] THE FULL LOCKSTEP WALK -- every pair walked to its exit, nothing stopped early")
print("    Per pair recorded: whether a joint state is ever OUTSIDE the NARROW class")
print("    {EQ, UP2}; how the lockstep exits; whether the exit signature is (0^r, 1,1,0^{r-2});")
print("    and the delta.  Nothing is aggregated before the walk finishes.")

WIDE = ("UNIT_DOWN", "DOM")
recs = []
PARTIAL = False
for idx, (A0, B0, dlt) in enumerate(S1):
    if over():
        PARTIAL = True
        break
    a, b, k = A0, B0, 0
    ever_wide = False
    ever_other = False
    first_wide = None
    eq_at = None
    exit_kind = None
    while k <= 80:
        r = relation(tuple(a), tuple(b))
        if r == "EQ":
            eq_at = k
            exit_kind = "EQ"
            break
        if r in WIDE:
            if not ever_wide:
                first_wide = (k, r, a, b)
            ever_wide = True
        if r == "OTHER":
            ever_other = True
            exit_kind = "OTHER_relation"
            break
        na, nb = step(list(a)), step(list(b))
        if na is None or nb is None:
            exit_kind = "ABORT"
            break
        if na == "TERMINAL" and nb == "TERMINAL":
            exit_kind = "BOTH_TERMINAL"
            break
        if na == "TERMINAL":
            exit_kind = "A_TERMINAL"
            break
        if nb == "TERMINAL":
            exit_kind = "B_TERMINAL"
            break
        a, b, k = na, nb, k + 1
    else:
        exit_kind = "RUNAWAY"
    sig = (set(a) <= {0},
           sorted(b, reverse=True)[:2] == [1, 1] and set(b) <= {0, 1})
    recs.append(dict(A0=A0, B0=B0, dlt=dlt, ever_wide=ever_wide, ever_other=ever_other,
                     first_wide=first_wide, eq_at=eq_at, exit_kind=exit_kind,
                     a=a, b=b, k=k, sig=sig))
print("   pairs walked: %d of %d   PARTIAL=%s" % (len(recs), len(S1), PARTIAL))
print("   exit classification  : %s" % dict(sorted(Counter(r["exit_kind"] for r in recs).items())))
print("   ever leaves {EQ,UP2} : %s" % dict(sorted(Counter(r["ever_wide"] for r in recs).items())))
print("   ever OTHER           : %s" % dict(sorted(Counter(r["ever_other"] for r in recs).items())))
narrow = [r for r in recs if not r["ever_wide"]]
widep = [r for r in recs if r["ever_wide"]]
print("   ----------------------------------------------------------------------------------")
print("   NARROW pairs (never leave {EQ,UP2}) : %d" % len(narrow))
print("   WIDE   pairs (leave it at least once): %d   <-- these are the pairs C1-Z's PROOF"
      % len(widep))
print("                                                does not reach; Sec 7.56 (j) counted 51")
print("   population for both counts: the %d S1 pairs of block [1].  Exclusions: none." % len(recs))
ctrl("CONTROL: the WIDE set is non-empty (else there is nothing to report)", len(widep))
ctrl("CONTROL: the NARROW set is non-empty (else the split is vacuous)", len(narrow))


# ================================================================ 3. THE COVERAGE QUESTION
print("\n[3] DOES C1-Z's CONCLUSION SURVIVE ON THE WIDE PAIRS?")
print("    C1-Z delivers delta by exactly two proved mechanisms:")
print("      (M1) EQ occurs  ==> EQ absorbing + R trajectory-invariant  ==> delta = 0")
print("      (M2) EQ never occurs, exit signature (0^r, (1,1,0^{r-2}))  ==> C1-Y ==> delta = 1")
print("    A pair covered by NEITHER has its delta explained by NOTHING this line has proved.")


def covered(r):
    if r["exit_kind"] == "EQ":
        return "M1_EQ"
    if r["sig"] == (True, True) and r["eq_at"] is None:
        return "M2_terminal_signature"
    return "UNCOVERED"


cov_all = Counter(covered(r) for r in recs)
cov_narrow = Counter(covered(r) for r in narrow)
cov_wide = Counter(covered(r) for r in widep)
print("   coverage over ALL %d pairs    : %s" % (len(recs), dict(sorted(cov_all.items()))))
print("   coverage over NARROW pairs    : %s" % dict(sorted(cov_narrow.items())))
print("   coverage over WIDE pairs      : %s" % dict(sorted(cov_wide.items())))
unc = [r for r in recs if covered(r) == "UNCOVERED"]
print("   UNCOVERED pairs: %d of %d.  Population: the %d S1 pairs.  Exclusions: none."
      % (len(unc), len(recs), len(recs)))
print("   delta histogram, WIDE pairs   : %s" % dict(sorted(Counter(r["dlt"] for r in widep).items())))
print("   delta histogram, NARROW pairs : %s" % dict(sorted(Counter(r["dlt"] for r in narrow).items())))
print("   delta histogram, UNCOVERED    : %s" % dict(sorted(Counter(r["dlt"] for r in unc).items())))
print("   WIDE pairs by (first relation left into, exit kind, mechanism):")
tab = Counter((r["first_wide"][1], r["exit_kind"], covered(r)) for r in widep if r["first_wide"])
for kk, vv in sorted(tab.items()):
    print("      %-34s %d" % (str(kk), vv))
if widep:
    z = sorted(widep, key=lambda r: (len(r["A0"]), sum(r["A0"]), r["A0"]))[0]
    k0, r0, a0, b0 = z["first_wide"]
    print("   smallest WIDE pair, printed rather than excluded:")
    print("      A_0 = %-28s B_0 = %s" % (str(z["A0"]), str(z["B0"])))
    print("      first non-{EQ,UP2} state at stage %d, relation %s:" % (k0, r0))
    print("         A_%d = %-24s B_%d = %-24s" % (k0, str(a0), k0, str(b0)))
    print("      lockstep exit: %-16s eq_at=%-6s delta=%s mechanism=%s"
          % (z["exit_kind"], str(z["eq_at"]), z["dlt"], covered(z)))
ctrl("CORRUPT: 'every pair is covered by M2' is violated",
     sum(1 for r in recs if covered(r) != "M2_terminal_signature"))
ctrl("CORRUPT: 'no pair is covered by M1' is violated", cov_all.get("M1_EQ", 0))


# ================================================================ 4. WHY THE WIDE PAIRS LAND WHERE THEY DO
print("\n[4] IF A WIDE STATE IS REACHED, WHAT CLOSES IT?  (this is what E07 must be aimed at)")
print("    At a UNIT_DOWN or DOM joint state the two lists have EQUAL SUM and EQUAL LENGTH,")
print("    and B is dominated by A.  So the residue comparison there is an instance of (RH)")
print("    -- the OPEN even half -- not of the (UP2)/C1-Y machinery of the odd half.")
sum_eq = len_eq = 0
for r in widep:
    k0, r0, a0, b0 = r["first_wide"]
    sum_eq += (sum(a0) == sum(b0))
    len_eq += (len(a0) == len(b0))
print("   WIDE pairs whose first wide state has equal SUM   : %d of %d" % (sum_eq, len(widep)))
print("   WIDE pairs whose first wide state has equal LENGTH : %d of %d" % (len_eq, len(widep)))
print("   WIDE pairs that go on to reach EQ                  : %d of %d"
      % (sum(1 for r in widep if r["exit_kind"] == "EQ"), len(widep)))
print("   WIDE pairs that do NOT reach EQ                    : %d of %d"
      % (sum(1 for r in widep if r["exit_kind"] != "EQ"), len(widep)))
print("   population: the WIDE subset of the %d S1 pairs.  Exclusions: none." % len(recs))
# does res(A) - res(B) at the FIRST wide state already equal the pair's delta?
agree = 0
tested = 0
for r in widep:
    if over():
        break
    k0, r0, a0, b0 = r["first_wide"]
    ra, rb = res(list(a0)), res(list(b0))
    if ra is None or rb is None:
        continue
    tested += 1
    agree += ((ra - rb) == r["dlt"])
print("   R is a trajectory invariant, so delta must already be readable at the first wide")
print("   state: (R(A_k) - R(B_k)) == delta on %d of %d WIDE pairs tested (%d skipped: a run"
      % (agree, tested, len(widep) - tested))
print("   aborts at that state and has no residue).")
ctrl("CONTROL: the trajectory-invariance cross-check was actually run", tested)


# ================================================================ 4b. THE SUM-GAP TRAJECTORY
print("\n[4b] THE SUM-GAP g_s := sum(B_s) - sum(A_s) ALONG THE LOCKSTEP")
print("     I1 / Lemma C1-X (ii): a step with pivot p drops the sum by exactly 2p, so")
print("        g_{s+1} = g_s - 2*(p_B - p_A).")
print("     g_0 = 2 (B_0 is A_0 with two entries raised by 1).  A UNIT_DOWN or DOM state has")
print("     g = 0.  QUESTION THAT DECIDES E07: once g reaches 0, can it return to 2?")
gseq_hist = Counter()
gvals = Counter()
returns = []
pdiff = Counter()
gpd = Counter()
relg = Counter()
for r in recs:
    if over():
        PARTIAL = True
        break
    a, b, k = r["A0"], r["B0"], 0
    gs = []
    hit0 = False
    ret = False
    while k <= 80:
        g = sum(b) - sum(a)
        gs.append(g)
        gvals[g] += 1
        if g == 0:
            hit0 = True
        elif hit0:
            ret = True
        if a == b:
            break
        na, nb = step(list(a)), step(list(b))
        if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
            break
        pdiff[(max(b) - max(a))] += 1
        gpd[(g, max(b) - max(a))] += 1
        relg[(g, relation(tuple(a), tuple(b)))] += 1
        a, b, k = na, nb, k + 1
    gseq_hist[tuple(gs)] += 1
    if ret:
        returns.append((r["A0"], r["B0"], gs))
print("     distinct g-trajectories seen: %d   over %d pairs" % (len(gseq_hist), len(recs)))
print("     g values seen at any joint state: %s" % dict(sorted(gvals.items())))
print("     pivot difference p_B - p_A at every stepped joint state: %s" % dict(sorted(pdiff.items())))
print("     CROSS-TAB (g_s, p_B - p_A) at every stepped joint state: %s" % dict(sorted(gpd.items())))
print("     CROSS-TAB (g_s, relation) at every stepped joint state  : %s" % dict(sorted(relg.items())))
print("     pairs where g reaches 0 and then RETURNS to a nonzero value: %d" % len(returns))
print("     population: the %d S1 pairs.  Exclusions: none." % len(recs))
if returns:
    print("     first such pair: %s" % (returns[0],))
print("     the 3 most common g-trajectories: %s" % gseq_hist.most_common(3))
ctrl("CORRUPT: 'g is constant along every lockstep' is violated",
     sum(v for kk, v in gseq_hist.items() if len(set(kk)) > 1))
ctrl("CONTROL: g = 2 actually occurs (else the UP2 start is not represented)", gvals.get(2, 0))


# ================================ 4c. THE SAME PIVOT QUESTION ON THE S2-DERIVED FAMILY
print("\n[4c] THE PIVOT GAP ON THE S2-DERIVED PAIRS (L, L'_1)  -- brief E07 needs this")
print("     Population rebuilt exactly as r42 did: the distinct (c, tail) pairs among the S2")
print("     instances with sum(T) ODD, sum(T) <= 18, both residues defined.  A_0 = L = W-(c)+tail,")
print("     B_0 = L'_1 = one HH step applied to L' = W+(c+1)+tail.")
S2rec = []
for N in range(1, NMAX + 1):
    if over():
        PARTIAL = True
        break
    for T in parts(N):
        if sum(T) % 2 == 0:
            continue
        for i in range(len(T)):
            U = list(T)
            U[i] += 1
            U = ms(U)
            if not (i == 0 or T[i] == T[0]):
                continue                     # S1, handled in [2]
            a, b = f(T), f(U)
            if a is None or b is None:
                continue
            S2rec.append((T[0], ms(T[1:]), a - b))
CT = sorted(set((c, t) for (c, t, _d) in S2rec))
print("     distinct (c,tail) pairs: %d   (r42 printed 686 for this same population)" % len(CT))
s2_g = Counter()
s2_pd = Counter()
s2_gpd = Counter()
s2_rel = Counter()
s2_exit = Counter()
s2_break = 0
for (c, tl) in CT:
    if over():
        PARTIAL = True
        break
    L = ms(Wm(c) + list(tl))
    Lp = ms(Wp(c + 1) + list(tl))
    L1 = step(list(Lp))
    if L1 in ("TERMINAL", None):
        s2_exit["STEP_FAILED"] += 1
        continue
    a, b, k = L, L1, 0
    while k <= 80:
        r = relation(tuple(a), tuple(b))
        s2_rel[r] += 1
        s2_g[sum(b) - sum(a)] += 1
        if r not in ("EQ", "UP2"):
            s2_break += 1
        if a == b:
            s2_exit["EQ"] += 1
            break
        na, nb = step(list(a)), step(list(b))
        if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
            s2_exit["TERMINAL" if na == "TERMINAL" or nb == "TERMINAL" else "ABORT"] += 1
            break
        s2_pd[max(b) - max(a)] += 1
        s2_gpd[(sum(b) - sum(a), max(b) - max(a))] += 1
        a, b, k = na, nb, k + 1
print("     joint-state relations over the whole lockstep : %s" % dict(sorted(s2_rel.items())))
print("     g values seen at any joint state              : %s" % dict(sorted(s2_g.items())))
print("     p_B - p_A at every STEPPED joint state        : %s" % dict(sorted(s2_pd.items())))
print("     CROSS-TAB (g_s, p_B - p_A) at stepped states  : %s" % dict(sorted(s2_gpd.items())))
print("     lockstep exits                                : %s" % dict(sorted(s2_exit.items())))
print("     joint states outside {EQ, UP2}                : %d" % s2_break)
print("     population: the %d distinct (c,tail) pairs above.  Exclusions: none." % len(CT))
ctrl("CONTROL: the S2-derived population is non-empty", len(CT))
ctrl("CONTROL: UP2 states actually occur on the S2-derived family", s2_rel.get("UP2", 0))


# ================================================================ 5. (RH) AND PIVOT MAJORIZATION
print("\n[5] (RH) AND THE PIVOT-MAJORIZATION ROUTE  --  the measurement E05 needs")
print("    DEFINITIONS USED, stated so the population cannot drift:")
print("      pivots(pi) = the sequence of maxima removed by Havel-Hakimi, sorted decreasing.")
print("      C1-X (ii): 2*sum(pivots(pi)) = sum(pi).")
print("      unit transfer DOWN: pi' = pi - e_i + e_j with pi_i >= pi_j + 2.")
print("        (Sec 7.55 (b) writes 'add 1 to an entry that is not larger'.  Taken literally")
print("         that also admits pi_i = pi_j, which moves UP in dominance, and pi_i = pi_j+1,")
print("         which is the identity as a multiset.  Only pi_i >= pi_j + 2 is a genuine")
print("         down-move, and that is the definition used here.  Both looser readings are")
print("         measured separately below so the discrepancy is on the record.)")
print("      dominance a >= b for partitions of the SAME integer: every partial sum of a")
print("        (sorted decreasing, zero-padded) is >= the corresponding partial sum of b.")


def pivots(lst):
    """the sequence of pivots of the HH run, sorted decreasing; None if the run aborts."""
    cur = sorted(lst, reverse=True)
    out = []
    guard = 0
    while True:
        guard += 1
        if guard > 400:
            return None
        nxt = stepA(sorted(cur, reverse=True))
        if nxt == "TERMINAL":
            return tuple(sorted(out, reverse=True))
        if nxt is None:
            return None
        out.append(max(cur))
        cur = list(nxt)


def dominates(a, b):
    """a >= b in dominance; a, b partitions of the same integer, zero-padded."""
    n = max(len(a), len(b))
    A = list(a) + [0] * (n - len(a))
    B = list(b) + [0] * (n - len(b))
    sa = sb = 0
    for x, y in zip(A, B):
        sa += x
        sb += y
        if sb > sa:
            return False
    return True


# known values for pivots(), before it is used for anything
known("pivots([1,1,0,0])", pivots([1, 1, 0, 0]), (1,))
known("2*sum(pivots) = sum, on (3,3,2,2,2,2,2)",
      2 * sum(pivots([3, 3, 2, 2, 2, 2, 2])) - sum([3, 3, 2, 2, 2, 2, 2]), 0)
known("dominates((3,1),(2,2))", dominates((3, 1), (2, 2)), True)
known("dominates((2,2),(3,1))", dominates((2, 2), (3, 1)), False)

NRH = 16
pop = 0
rh_ok = rh_bad = 0
rh_ce = []
maj_ok = 0
maj_n = 0
maj_bad = []
pv_bad = 0              # disagreements between pivots() and the diffed runA/runB step count
loose_eq = 0            # pi_i == pi_j  (moves UP in dominance -- the loose reading)
loose_eq_dom = 0
cx_ok = cx_bad = 0
for N in range(2, NRH + 1):
    if over():
        PARTIAL = True
        break
    for pi in parts(N):
        pv = pivots(list(pi))
        if pv is None:
            continue                      # run aborts: s(pi) undefined, skipped on BOTH sides
        if 2 * sum(pv) == sum(pi):
            cx_ok += 1
        else:
            cx_bad += 1
        n = len(pi)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if pi[i] < pi[j] + 2:
                    if pi[i] == pi[j]:
                        loose_eq += 1
                        u = list(pi)
                        u[i] -= 1
                        u[j] += 1
                        if dominates(ms(u), ms(pi)):
                            loose_eq_dom += 1
                    continue
                u = list(pi)
                u[i] -= 1
                u[j] += 1
                u = ms(u)
                if min(u) < 0:
                    continue
                pu = pivots(list(u))
                if pu is None:
                    continue              # pi' aborts: excluded, counted nowhere else
                pop += 1
                # (RH): R(pi') <= R(pi).  Same length n, so <=> s(pi) <= s(pi').
                if len(pv) <= len(pu):
                    rh_ok += 1
                else:
                    rh_bad += 1
                    if len(rh_ce) < 6:
                        rh_ce.append((pi, u, len(pv), len(pu)))
                # (PIVOT-MAJ): p(pi) dominates p(pi')
                if dominates(pv, pu):
                    maj_ok += 1
                else:
                    maj_n += 1
                    if len(maj_bad) < 6:
                        maj_bad.append((pi, u, pv, pu, len(pv), len(pu)))
                # cross-check pivots() against the DIFFED runA/runB step count
                if len(pv) != steps_of(list(pi)):
                    pv_bad += 1
print("   population: every partition pi of N in [2,%d] whose HH run TERMINATES, and every" % NRH)
print("   pi' = pi - e_i + e_j with pi_i >= pi_j + 2 whose run also terminates.")
print("   pairs in population: %d.  Exclusions: lists whose run ABORTS -- skipped on BOTH" % pop)
print("   sides and counted nowhere else.  N > %d is OUT OF POPULATION and claimed nowhere." % NRH)
print("   C1-X (ii) 2*sum(pivots) = sum : holds %d, fails %d" % (cx_ok, cx_bad))
print("   (RH)  s(pi) <= s(pi')          : holds %d, FAILS %d" % (rh_ok, rh_bad))
if rh_ce:
    print("      counterexamples to (RH) on this population (first %d):" % len(rh_ce))
    for z in rh_ce:
        print("         pi=%-22s pi'=%-22s s(pi)=%-3d s(pi')=%-3d" % (str(z[0]), str(z[1]), z[2], z[3]))
print("   (PIVOT-MAJ)  p(pi) >= p(pi')   : holds %d, FAILS %d (first %d printed)"
      % (maj_ok, maj_n, len(maj_bad)))
for z in maj_bad:
    print("      pi=%-20s pi'=%-20s p(pi)=%-18s p(pi')=%-18s s=%d s'=%d"
          % (str(z[0]), str(z[1]), str(z[2]), str(z[3]), z[4], z[5]))
print("   pivots() vs the DIFFED runA/runB step count: %d disagreements" % pv_bad)
if pv_bad:
    bad("PIVOTS", "pivots() length disagrees with the diffed step count on %d lists" % pv_bad)
print("   loose reading pi_i == pi_j: %d such moves; of those, pi' DOMINATES pi (i.e. the move"
      % loose_eq)
print("   goes UP, not down) in %d -- which is why the definition above requires pi_i >= pi_j+2."
      % loose_eq_dom)
ctrl("CONTROL: the (RH) population is non-empty", pop)
ctrl("CONTROL: the loose reading pi_i == pi_j really does go UP (Sec 7.55 (b) imprecision)",
     loose_eq_dom)


# ================================================================ 6. CORRUPT COMPANION FOR [5]
print("\n[6] CORRUPT COMPANIONS FOR BLOCK [5] -- so the block is not vacuous")
rev_bad = 0
rev_pop = 0
maj_rev_bad = 0
for N in range(2, NRH + 1):
    if over():
        PARTIAL = True
        break
    for pi in parts(N):
        pv = pivots(list(pi))
        if pv is None:
            continue
        n = len(pi)
        for i in range(n):
            for j in range(n):
                if i == j or pi[i] < pi[j] + 2:
                    continue
                u = list(pi)
                u[i] -= 1
                u[j] += 1
                u = ms(u)
                pu = pivots(list(u))
                if pu is None:
                    continue
                rev_pop += 1
                if not (len(pv) >= len(pu)):
                    rev_bad += 1            # the REVERSED (RH) must fail somewhere
                if not dominates(pu, pv):
                    maj_rev_bad += 1        # the REVERSED majorization must fail somewhere
print("   reversed (RH)  's(pi) >= s(pi')' fails on %d of %d -- a real claim, not a tautology"
      % (rev_bad, rev_pop))
print("   reversed majorization 'p(pi') >= p(pi)' fails on %d of %d" % (maj_rev_bad, rev_pop))
ctrl("CORRUPT: reversed (RH) is violated", rev_bad)
ctrl("CORRUPT: reversed majorization is violated", maj_rev_bad)


# ============================================ 6b. OUT-OF-RANGE CONTROL AND STRICTNESS
print("\n[6b] IS (PIVOT-MAJ) AN ARTIFACT OF N <= %d?  A SECOND, DISJOINT POPULATION" % NRH)
print("     Population: N in [%d, 20] ONLY -- disjoint from block [5], nothing shared." % (NRH + 1))
pop2 = maj2_ok = maj2_bad = rh2_ok = rh2_bad = 0
ce2 = []
for N in range(NRH + 1, 21):
    if over():
        PARTIAL = True
        break
    for pi in parts(N):
        pv = pivots(list(pi))
        if pv is None:
            continue
        n = len(pi)
        for i in range(n):
            for j in range(n):
                if i == j or pi[i] < pi[j] + 2:
                    continue
                u = list(pi)
                u[i] -= 1
                u[j] += 1
                u = ms(u)
                pu = pivots(list(u))
                if pu is None:
                    continue
                pop2 += 1
                if len(pv) <= len(pu):
                    rh2_ok += 1
                else:
                    rh2_bad += 1
                if dominates(pv, pu):
                    maj2_ok += 1
                else:
                    maj2_bad += 1
                    if len(ce2) < 4:
                        ce2.append((pi, u, pv, pu))
print("     pairs in population: %d.  Exclusions: aborting runs, skipped on BOTH sides." % pop2)
print("     (RH)        holds %d, FAILS %d" % (rh2_ok, rh2_bad))
print("     (PIVOT-MAJ) holds %d, FAILS %d" % (maj2_ok, maj2_bad))
for z in ce2:
    print("        pi=%-22s pi'=%-22s p(pi)=%-20s p(pi')=%s"
          % (str(z[0]), str(z[1]), str(z[2]), str(z[3])))
ctrl("CONTROL: the out-of-range population is non-empty", pop2)

print("\n[6c] IS (PIVOT-MAJ) STRICTLY STRONGER THAN (RH)?  -- i.e. is the reduction real work?")
print("     The implication used is STANDARD: for partitions of the same integer,")
print("     a >= b in dominance  ==>  a* <= b* (conjugates)  ==>  #parts(a) = a*_1 <= b*_1 =")
print("     #parts(b).  So (PIVOT-MAJ) ==> (RH).  The converse is NOT automatic; measured:")
imp_ok = imp_bad = 0
conv_fail = 0
conv_pop = 0
conv_ex = None
for N in range(2, 13):
    if over():
        PARTIAL = True
        break
    P = list(parts(N))
    for a in P:
        for b in P:
            conv_pop += 1
            da = dominates(a, b)
            if da:
                if len(a) <= len(b):
                    imp_ok += 1
                else:
                    imp_bad += 1
            elif len(a) <= len(b):
                conv_fail += 1
                if conv_ex is None:
                    conv_ex = (a, b)
print("     partition pairs (a,b) of the same N in [2,12] examined: %d" % conv_pop)
print("     dominance ==> fewer-or-equal parts : holds %d, FAILS %d" % (imp_ok, imp_bad))
print("     fewer-or-equal parts WITHOUT dominance: %d  (so the converse is false; example %s)"
      % (conv_fail, str(conv_ex)))
if imp_bad:
    bad("IMPLICATION", "dominance did not imply fewer parts on %d pairs" % imp_bad)
ctrl("CONTROL: the standard implication was actually exercised", imp_ok)
ctrl("CORRUPT: the CONVERSE implication is violated (so (PIVOT-MAJ) is strictly stronger)",
     conv_fail)


# ================================================================ 7. SELF-AUDIT
print("\n[7] SELF-AUDIT")
print("   elapsed            : %.2f s   internal limit %.0f s" % (time.time() - T0, LIMIT))
print("   PARTIAL            : %s" % (PARTIAL or bool(OUT_OF_TIME)))
print("   diffed runA/runB   : %d   disagreements: 0 (any disagreement exits with code 2)" % DIFFED)
print("   controls           : %d   all firing: %s" % (len(CTRL), all(CTRL)))
print("   DEFECTS            : %d %s" % (len(FAIL), FAIL if FAIL else ""))
print("   interpreter        : .venv/bin/python3, pure Python; sympy/networkx NOT imported")
print("   no SAT, no solver, no exhaustive search of an infeasible space -- every sweep is a")
print("   census over the finite population named beside it.")
print("=" * 100)
sys.exit(0 if not FAIL and all(CTRL) else 3)
