#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r36 ITEM 1 -- Conjecture C1 at k = 3: the PROOF, machine-audited.

Round 35 left Observation C1-I as a CENSUS: for even n the near-miss set is
{(w,c): w+c=n} u {(a,b,1): a+b=n-1}, no near-miss has k >= 4.  The k=2 half is
Theorem C1-2.  This round proves the k = 3 half -- and it proves MORE than the
task asked: not just that every (a,b,1) IS a near-miss, but that nothing else at
k = 3 is, i.e. the exact value of s0 on EVERY three-part partition.

What is under audit here is the TRAJECTORY of each hand proof, not only its final
value (RULING BW / the round-29 doctrine): every intermediate list the hand proof
names is recomputed by the process and compared as a MULTISET.  A true statement
with a false intermediate is a defect.

RULING CO': step process extracted by source text from w61_r29_c1audit.py -- the
same two independent implementations (runA sorted-list, runB multiplicity-counter,
different abort predicates), diffed on every input before any verdict is printed.
No SAT, no exhaustive local search.  Self-limits with sys.exit, never `return`.
"""
import re, sys, time, hashlib
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

DIFFED = 0
FAIL = []

def run(lst):
    """(steps, residue) or (None, None); ABORTS THE AUDIT if the two impls disagree."""
    global DIFFED
    a, b = runA(list(lst)), runB(list(lst))
    if a != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (lst, a, b))
        sys.exit(2)
    DIFFED += 1
    return a

def bad(tag, detail):
    FAIL.append("%s  %s" % (tag, detail))
    print("   ** DEFECT %s  %s" % (tag, detail))

def ms(lst):
    return tuple(sorted(lst, reverse=True))

def one_step(lst):
    """Next list as a sorted tuple, or 'TERMINAL', or None on abort."""
    r = stepA(sorted(lst, reverse=True))
    if r == "TERMINAL" or r is None:
        return r
    return ms(r)

def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield (); return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r

def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)

# ---------------------------------------------------------------- the named shapes
# Every list the hand proof of Theorem C1-3 names, as a function.  The proof is
# checked BY these, so a typo here is a proof defect, not a script defect.
def L_head(u, mu):      return [u] * (u + 2) + list(mu)          # M(lam) with lam=(u,mu)
def L_mid(u, mu):       return [u] + [u - 1] * u + list(mu)      # after ONE step
def Y(u, nu):           return [u] * 2 + [u - 1] * u + list(nu)  # W(u) u nu
def Q(u, nu):           return [u] + [u - 1] * (u + 1) + list(nu)
def Wplus(c):           return [c] * 3 + [c - 1] * c
def Wminus(c):          return [c] * 2 + [c - 1] * (c + 1)
def G(q, i):            return [2*q - i] * (3 + i) + [2*q - 1 - i] * (2*q - 2*i)
def V_list(c):          return [c] * (c + 3)                     # Lemma C1-A'

print("=" * 92)
print("w61 r36 ITEM 1 -- Conjecture C1 for k = 3: PROOF, trajectory-audited")
print("=" * 92)
print("impl source md5 %s   (w61_r29_c1audit.py, extracted by source text)" % hashlib.md5(text.encode()).hexdigest())

# ================================================================ 1. TRAJECTORIES
print()
print("1. TRAJECTORY CHECKS -- every intermediate list the hand proof names")
print("   (multiset equality against what the process actually produces)")

# T1 -- Lemma C1-J, the residue-preserving descent, TWO steps.
n1 = 0
for u in range(2, 26):
    for sz in range(1, 5):
        for mu in parts(sz * 3):
            if len(mu) < 1 or len(mu) > 4 or max(mu) > u - 1:
                continue
            a = one_step(L_head(u, mu))
            if a != ms(L_mid(u, mu)):
                bad("T1a", "u=%d mu=%s got %s want %s" % (u, mu, a, ms(L_mid(u, mu))))
            b = one_step(list(a)) if isinstance(a, tuple) else a
            if b != ms([u - 2] * u + list(mu)):
                bad("T1b", "u=%d mu=%s got %s want %s" % (u, mu, b, ms([u-2]*u + list(mu))))
            n1 += 1
print("   T1  Lemma C1-J two-step descent  [u]^(u+2) u mu -> [u]^1 u [u-1]^u u mu -> [u-2]^u u mu")
print("       %d (u, mu) pairs, max(mu) <= u-1, |mu| <= 4      defects so far: %d" % (n1, len(FAIL)))

# T2 -- the Y descent (case A interior)
n2 = 0
for u in range(2, 40):
    for nu in [(c,) for c in range(1, u)] + [(c, d) for c in range(1, u) for d in range(1, c + 1)][:60]:
        if max(nu) > u - 1:
            continue
        if one_step(Y(u, nu)) != ms(Y(u - 1, nu)):
            bad("T2", "u=%d nu=%s" % (u, nu))
        n2 += 1
print("   T2  Y(u;nu) = [u]^2 u [u-1]^u u nu  -> Y(u-1;nu)      %d cases, defects: %d" % (n2, len(FAIL)))

# T3 -- the Q descent (case B interior)
n3 = 0
for u in range(2, 40):
    for nu in [(c,) for c in range(1, u)] + [(c, d) for c in range(1, u) for d in range(1, c + 1)][:60]:
        if max(nu) > u - 1:
            continue
        if one_step(Q(u, nu)) != ms(Q(u - 1, nu)):
            bad("T3", "u=%d nu=%s" % (u, nu))
        n3 += 1
print("   T3  Q(u;nu) = [u] u [u-1]^(u+1) u nu -> Q(u-1;nu)     %d cases, defects: %d" % (n3, len(FAIL)))

# T4 -- case A entry:  [b]^(b+3) u [c]  ->  Y(b;[c])
n4 = 0
for b in range(1, 45):
    for c in range(1, b + 1):
        if one_step([b] * (b + 3) + [c]) != ms(Y(b, (c,))):
            bad("T4", "b=%d c=%d" % (b, c))
        n4 += 1
print("   T4  [b]^(b+3) u [c] -> Y(b;[c])                       %d cases, defects: %d" % (n4, len(FAIL)))

# T5 -- the G descent inside W+(2q), and its exit into Lemma C1-A'
n5 = 0
for q in range(1, 30):
    if ms(G(q, 0)) != ms(Wplus(2 * q)):
        bad("T5-init", "q=%d" % q)
    for i in range(0, q):
        want = ms(G(q, i + 1)) if i + 1 <= q - 1 else ms(V_list(q))
        if one_step(G(q, i)) != want:
            bad("T5", "q=%d i=%d got %s want %s" % (q, i, one_step(G(q, i)), want))
        n5 += 1
    # G(q,q) as written IS [q]^(q+3) u [q-1]^0
    if ms(G(q, q)) != ms(V_list(q)):
        bad("T5-exit", "q=%d G(q,q)=%s" % (q, ms(G(q, q))))
print("   T5  G_i(q) -> G_(i+1)(q), G_(q-1)(q) -> [q]^(q+3)     %d steps, defects: %d" % (n5, len(FAIL)))

# T6 -- W-(c) -> W+(c-1) in one step.  NOTE c=1 IS included: the step identity
# holds there too (W+(0) = [0,0,0]); what fails at c=1 is the VALUE formula, and
# that boundary is the whole source of the k=3 near-miss.  See DEFECT LEDGER D1.
n6 = 0
for c in range(1, 60):
    if one_step(Wminus(c)) != ms(Wplus(c - 1)):
        bad("T6", "c=%d" % c)
    n6 += 1
print("   T6  W-(c) = [c]^2 u [c-1]^(c+1) -> W+(c-1)            %d cases, defects: %d" % (n6, len(FAIL)))

# T7 -- the floor of the c=1 descent
if one_step(Q(1, (1,))) != ms([0, 0, 0]):
    bad("T7", "Q(1;[1]) = %s -> %s" % (ms(Q(1, (1,))), one_step(Q(1, (1,)))))
if one_step([0, 0, 0]) != "TERMINAL":
    bad("T7t", "[0,0,0] not terminal")
print("   T7  Q(1;[1]) = [1,1,0,0] -> [0,0,0] TERMINAL          checked, defects: %d" % len(FAIL))

# ================================================================ 2. VALUES
print()
print("2. VALUE CHECKS -- the closed forms the trajectories add up to")

def chk(tag, it):
    n = 0; b0 = len(FAIL)
    for label, got, want in it:
        if got != want:
            bad(tag, "%s got %s want %s" % (label, got, want))
        n += 1
    print("   %-4s %-52s %6d cases, defects: %d" % (tag, chk.msg, n, len(FAIL) - b0))

chk.msg = ""
chk.msg = "Lemma C1-A'  V(c) = steps([c]^(c+3)) = c+1"
chk("V0", (( "c=%d" % c, run(V_list(c))[0], c + 1) for c in range(1, 80)))

chk.msg = "W+(c) even: steps = c+1, residue 2; odd: aborts"
chk("V1", (("c=%d" % c, run(Wplus(c)), ((c + 1, 2) if c % 2 == 0 else (None, None)))
           for c in range(1, 70)))

# D1 (see DEFECT LEDGER): the first draft of this line claimed (c+1, 2) for EVERY
# odd c.  It is FALSE at c = 1: W-(1) = [1,1,0,0] has (steps, residue) = (1, 3),
# because its one step lands on W+(0) = [0,0,0], which is TERMINAL rather than a
# c+1 = 1-step run.  The corrected statement carries the boundary explicitly.
chk.msg = "W-(c): c=1 -> (1,3) BOUNDARY; c odd>=3 -> (c+1,2); c even aborts"
chk("V2", (("c=%d" % c, run(Wminus(c)),
            ((1, 3) if c == 1 else ((c + 1, 2) if c % 2 == 1 else (None, None))))
           for c in range(1, 70)))
chk.msg = "W+(c): c=0 -> (0,3) BOUNDARY; c even>=2 -> (c+1,2); c odd aborts"
chk("V2b", (("c=%d" % c, run(Wplus(c)),
             ((0, 3) if c == 0 else ((c + 1, 2) if c % 2 == 0 else (None, None))))
            for c in range(0, 70)))

def a_case(b, c):
    return run([b] * (b + 3) + [c])
chk.msg = "case-A base [b]^(b+3) u [c]: c even -> (b+2, 2), c odd -> abort"
chk("V3", (("b=%d c=%d" % (b, c), a_case(b, c), ((b + 2, 2) if c % 2 == 0 else (None, None)))
           for b in range(1, 40) for c in range(1, b + 1)))

def b_case(b, c):
    return run(Q(b, (c,)))
chk.msg = "case-B base Q(b;[c]): c=1 ->(b,3); c odd>=3 ->(b+1,2); c even abort"
chk("V4", (("b=%d c=%d" % (b, c), b_case(b, c),
            ((b, 3) if c == 1 else ((b + 1, 2) if c % 2 == 1 else (None, None))))
           for b in range(1, 40) for c in range(1, b + 1)))

# ---- THE THEOREM ITSELF
def c1_3_predicted(w, b, c):
    """Theorem C1-3, as a function. (steps, residue) or (None, None)."""
    if (w + b + c) % 2 == 1:
        return (None, None)
    return (w + 1, 3) if c == 1 else (w + 2, 2)

WMAX = 60
n = 0; b0 = len(FAIL)
for w in range(1, WMAX + 1):
    for b in range(1, w + 1):
        for c in range(1, b + 1):
            got = run(M((w, b, c)))
            want = c1_3_predicted(w, b, c)
            if got != want:
                bad("THM", "(%d,%d,%d) got %s want %s" % (w, b, c, got, want))
            n += 1
print("   THM  Theorem C1-3 on EVERY (w,b,c), 1<=c<=b<=w<=%d      %6d cases, defects: %d"
      % (WMAX, n, len(FAIL) - b0))

# ---- Lemma C1-J in the general form actually used (residue-preserving)
def base_of(lam):
    w = lam[0]; mu = list(lam[1:]); m = max(mu)
    return ([m] * (m + 2) + mu) if (w - m) % 2 == 0 else ([m - 1] * (m + 1) + mu)

n = 0; b0 = len(FAIL)
for N in range(2, 27):
    for lam in parts(N):
        if len(lam) < 2:
            continue
        w = lam[0]; m = max(lam[1:])
        sM, rM = run(M(lam)); sB, rB = run(base_of(lam))
        off = (w - m) if (w - m) % 2 == 0 else (w - m + 1)
        pred_s = None if sB is None else off + sB
        if (sM, rM) != (pred_s, rB):
            bad("C1J", "lam=%s got %s want %s" % (lam, (sM, rM), (pred_s, rB)))
        n += 1
print("   C1J  s0 = offset + steps(base) AND residue(M) = residue(base)")
print("        every lam |- N <= 26 with >= 2 parts               %6d cases, defects: %d"
      % (n, len(FAIL) - b0))

# ================================================================ 3. PREDICATE + CONTROLS
print()
print("3. THE PREDICATE, AND CONTROLS THAT FIRE ON THE FEATURE (RULING CZ')")

def is_near_miss(lam):
    """TRUE iff M(lam) terminates with residue = k, i.e. s0(lam) = lam_1 + 1.
    Boolean, computed from the process -- NOT from the closed form."""
    lam = tuple(sorted(lam, reverse=True))
    s, r = run(M(lam))
    return s is not None and r == len(lam)

# (a) the MUST-BE-TRUE input, required before the predicate may be used at all
# D2 (see DEFECT LEDGER): the first draft of MUST_TRUE contained (7,2), which
# ABORTS -- 7+2 is odd, so Theorem C1-2 gives no run at all.  The must-be-true
# input was itself false and the rule caught it.  (7,2) is retained below, in the
# category it actually belongs to, rather than deleted.
MUST_TRUE = [(3, 2, 1), (5, 4, 1), (2, 1, 1), (7, 3), (4, 2)]
for t in MUST_TRUE:
    if not is_near_miss(t):
        bad("PRED-TRUE", "predicate returned False on a KNOWN near-miss %s" % (t,))
MUST_FALSE = [(3, 3, 2), (6, 4, 2), (5, 3, 3)]
for t in MUST_FALSE:
    if is_near_miss(t):
        bad("PRED-FALSE", "predicate returned True on a KNOWN non-near-miss %s" % (t,))
MUST_ABORT = [(7, 2), (5, 2), (3, 2, 2)]
for t in MUST_ABORT:
    if run(M(tuple(sorted(t, reverse=True))))[0] is not None:
        bad("PRED-ABORT", "%s was expected to abort and did not" % (t,))
    if is_near_miss(t):
        bad("PRED-ABORT2", "an ABORTING lam %s was reported a near-miss" % (t,))
print("   PRED near_miss() TRUE on %d known near-misses, FALSE on %d known non-,"
      " and %d aborting lam are neither" % (len(MUST_TRUE), len(MUST_FALSE), len(MUST_ABORT)))
print("        defects: %d" % len(FAIL))

# (b) controls: corrupt the CLAIM, not the instance.  Each control mutates the
#     closed form as a FUNCTION and must be caught on a FAMILY, not one row.
def control(name, claim, lo=1, hi=24):
    hits = []
    for w in range(lo, hi + 1):
        for b in range(1, w + 1):
            for c in range(1, b + 1):
                if run(M((w, b, c))) != claim(w, b, c):
                    hits.append((w, b, c))
    return name, len(hits), hits[:3]

CTRL = [
    ("CTRL-1 off-by-one on the near-miss value (w+1 -> w)",
     lambda w, b, c: (None, None) if (w+b+c) % 2 else ((w, 3) if c == 1 else (w+2, 2))),
    ("CTRL-2 near-miss condition widened c=1 -> c<=2",
     lambda w, b, c: (None, None) if (w+b+c) % 2 else ((w+1, 3) if c <= 2 else (w+2, 2))),
    ("CTRL-3 parity gate dropped (claims every (w,b,c) terminates)",
     lambda w, b, c: (w+1, 3) if c == 1 else (w+2, 2)),
    ("CTRL-4 residue in the non-near-miss branch 2 -> 3",
     lambda w, b, c: (None, None) if (w+b+c) % 2 else ((w+1, 3) if c == 1 else (w+2, 3))),
]
for name, claim in CTRL:
    nm, cnt, ex = control(name, claim)
    print("   %-58s misses %5d  e.g. %s" % (nm, cnt, ex))
    if cnt == 0:
        bad("CTRL", "%s was NOT caught -- the value check is blind to this feature" % nm)
# the TRUE claim must survive the same harness -- a control that fires on everything is useless
_, cnt0, _ = control("TRUE CLAIM", c1_3_predicted)
print("   %-58s misses %5d  <- must be 0" % ("CTRL-0 the theorem itself (false-positive probe)", cnt0))
if cnt0 != 0:
    bad("CTRL-0", "the theorem itself fails the control harness")

# (c) a trajectory control: corrupt the descent's multiplicity and check T1 sees it
tj = 0
for u in range(3, 12):
    for mu in [(1,), (2, 1), (3, 2, 1)]:
        if max(mu) > u - 1:
            continue
        if one_step(one_step(L_head(u, mu))) == ms([u - 2] * (u + 1) + list(mu)):
            tj += 1
print("   CTRL-5 corrupted descent target [u-2]^(u+1) matched by the process: %d  <- must be 0" % tj)
if tj != 0:
    bad("CTRL-5", "the trajectory check cannot tell [u-2]^u from [u-2]^(u+1)")

# ================================================================ 4. k >= 4
print()
print("4. ITEM 1b -- is k >= 4 EASIER than k = 3?  The r35 hypothesis, TESTED.")
print("   The k=3 proof above bottoms out in Lemma C1-A' after TWO descents (Y or Q,")
print("   then G).  For k >= 4 the same Lemma C1-J applies unchanged, but the base")
print("   carries |mu| = k-1 >= 3 tail entries, so the descent bottoms out in a")
print("   family that is NOT [c]^(c+3).  Measured below: the number of DISTINCT base")
print("   shapes the descent must resolve, by k.")
seen = {}
for N in range(2, 27):
    for lam in parts(N):
        if len(lam) < 2:
            continue
        k = len(lam)
        bs = ms(base_of(lam))
        seen.setdefault(k, set()).add(bs)
print("   k   distinct base shapes reachable (n <= 26)")
for k in sorted(seen):
    if k <= 8:
        print("   %-3d %d" % (k, len(seen[k])))

print()
print("   OBSERVATION C1-M (CENSUS, NOT A THEOREM): residue(M(lam)) <= ceil(k/2) + 1")
worst = {}
viol = 0
for N in range(2, 31):
    for lam in parts(N):
        if len(lam) < 2:
            continue
        k = len(lam)
        s, r = run(M(lam))
        if s is None:
            continue
        worst[k] = max(worst.get(k, 0), r)
        if r > -(-k // 2) + 1:
            viol += 1
            if viol < 4:
                print("   ** VIOLATION lam=%s k=%d residue=%d" % (lam, k, r))
print("   violations over every lam |- n <= 30 with >= 2 parts : %d" % viol)
print("   k   max residue observed   ceil(k/2)+1")
for k in sorted(worst):
    if k <= 12:
        print("   %-3d %-21d %d" % (k, worst[k], -(-k // 2) + 1))
print("   C1-M implies C1 for every k >= 2 (ceil(k/2)+1 < k+1 exactly when k >= 2 --")
print("   at k = 1 the two are EQUAL, which is precisely C1's equality case) AND no")
print("   near-miss for k >= 4 (ceil(k/2)+1 <= k-1 exactly when k >= 4).  It is")
print("   ATTAINED at k = 2 and k = 3, which is why those two carry near-misses.")
print("   STATED AS A CENSUS.  This line was burned once already by promoting one.")

print()
print("   VERDICT on the r35 hypothesis: the k=3 proof went through, and it did NOT")
print("   go through a route that k >= 4 makes shorter -- the base-shape count above")
print("   grows with k.  What IS easier at k >= 4 is the CONCLUSION (a slack of 2 is")
print("   more room), not the PROOF.  Attack order NOT inverted; the successor is")
print("   C1-M, which is one statement covering every k at once.")

# ================================================================ 5. verdict
print()
print("DEFECT LEDGER -- both found by this script against its OWN first draft, both MINE")
print("  D1  V2's lemma statement claimed W-(c) = (c+1, 2) for EVERY odd c.  FALSE at")
print("      c = 1: W-(1) = [1,1,0,0] is (1, 3).  The one step from W-(1) lands on")
print("      W+(0) = [0,0,0], which is TERMINAL, so the +1 the formula charges for it")
print("      is not spent.  Species: BOUNDARY/BOOKKEEPING, the Repair AG2 species, in a")
print("      lemma written the same hour.  Theorem C1-3 is UNAFFECTED -- c = 1 was")
print("      already routed through its own branch -- but the LEMMA was false as stated.")
print("      And the boundary is not incidental: W-(1)/W+(0) having residue 3 instead of")
print("      2 is the ENTIRE source of the k = 3 near-miss family.  Corrected above.")
print("  D2  The MUST-return-True input for near_miss() contained (7,2), which ABORTS")
print("      (7+2 odd).  The must-be-true input was itself false.  The standing rule")
print("      caught it on the first run; (7,2) is now in MUST_ABORT, not deleted.")
print()
print("=" * 92)
print("runA/runB diffed calls: %d, 0 disagreements" % DIFFED)
print("DEFECTS: %d" % len(FAIL))
for f in FAIL:
    print("   %s" % f)
print("VERDICT: %s" % ("ALL CHECKS PASS" if not FAIL else "** DEFECTS PRESENT **"))
print("elapsed %.1fs" % (time.time() - T0))
sys.exit(0 if not FAIL else 1)
