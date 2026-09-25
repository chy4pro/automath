#!/usr/bin/env python3
"""
w61_r33_null.py -- THE NULL EXPECTATION for the round-31 held-out harness.

Promotion condition cert_w61_r32 SS8.1: "the blind-guess rate is computed per row
and as a conjunction, with plausible ranges stated and defended -- B1 excluded."

Doctrine SS10 / RULING: load-bearing predicates are ONE checked implementation,
imported, never re-typed.  stepA/runA/runB are EXTRACTED BY SOURCE TEXT from
problems/wowii/w61_r29_c1audit.py -- the same single source w61_r31_key.py used.

Every boolean predicate below carries an input on which it MUST return True.
Self-limit: hard wall-clock cap; on overrun sys.exit(3).  Never `return`.
"""
import sys, time, re, hashlib
from collections import Counter
from pathlib import Path

T0 = time.time(); CAP_S = 300.0
def tick(where):
    if time.time() - T0 > CAP_S:
        print("!! SELF-LIMIT %.0fs exceeded at %s -- exit(3)" % (CAP_S, where)); sys.exit(3)

ROOT = Path("$HOME/workspace/claudecode/automath")
SRC  = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()
print("impl source : %s  md5 %s" % (SRC.name, hashlib.md5(text.encode()).hexdigest()))
print("             (w61_r31_key.py recorded md5 768975c3987de60fbebe1080d0dd530d)")

def grab(name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---))" % re.escape(name), text, re.S | re.M)
    assert m, "could not extract def %s" % name
    return m.group(0)
BLOB = "\n".join(grab(n) for n in ("stepA", "runA", "runB"))
ns = {"Counter": Counter, "sorted": sorted}
exec(compile(BLOB, str(SRC), "exec"), ns)
runA, runB = ns["runA"], ns["runB"]

DIFFED = 0
def run(lst):
    global DIFFED
    a, b = runA(list(lst)), runB(list(lst))
    if a != b:
        print("!! IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (lst, a, b)); sys.exit(2)
    DIFFED += 1
    return a
def M(lam):
    w = max(lam); return [w] * (w + 1) + list(lam)
def s0(lam):    return run(M(lam))[0]
def resid(lam): return run(M(lam))[1]
def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield []; return
    for p in range(min(n, mx), 0, -1):
        for rest in parts(n - p, p):
            yield [p] + rest

CTRL = []
def ctl(tag, got, want):
    ok = (got == want); CTRL.append(ok)
    print("   %-56s got %-12s want %-12s %s" % (tag, repr(got), repr(want), "OK" if ok else "** FAIL"))
    return ok

print()
print("=" * 78)
print("PART 0 -- controls.  Every predicate must be shown returning True somewhere.")
print("=" * 78)
# the disclosed worked example, which is the ONLY instance a guessing judge is handed
ctl("steps(M((2,1,1))) = 3   [brief SS1.3 worked example]", run(M([2,1,1]))[0], 3)
ctl("residue(M((2,1,1))) = 3 [brief SS1.3 worked example]", run(M([2,1,1]))[1], 3)
ctl("s0((5,3)) = w+1 = 6     [Thm C1-2, disclosed]",        s0([5,3]), 6)
ctl("steps([1,1,1]) aborts   [negative]",                   run([1,1,1])[0], None)

print()
print("=" * 78)
print("PART 1 -- reproduce the four ANSWERED key rows from the single source impl")
print("=" * 78)
KEYFILE = ROOT / "problems/wowii/w61_r31_heldout_key.txt"
declared = {}
for line in KEYFILE.read_text().splitlines():
    m = re.match(r"^([AB]\d) = (\d+)$", line.strip())
    if m: declared[m.group(1)] = int(m.group(2))
print("   key file declares : %s" % declared)

A1 = s0([6,4,2]);            A1r = resid([6,4,2])
A2 = resid([5,4,3]);         A2s = s0([5,4,3])
A3, A3r = run([4,4,3,3,2,2])
ctl("A1 recomputed = key",  A1, declared["A1"])
ctl("A2 recomputed = key",  A2, declared["A2"])
ctl("A3 recomputed = key",  A3, declared["A3"])
print("   A/B diffed calls so far: %d, disagreements 0" % DIFFED)

print()
print("   *** THE LATENT.  Prop C1-B (PRINTED IN THE BRIEF) is steps = |L| - residue.")
print("       Applying it to the three A rows:")
print("       A1: |M((6,4,2))| = %2d   steps = %d   ->  residue = %d" % (len(M([6,4,2])), A1, A1r))
print("       A2: |M((5,4,3))| = %2d   steps = %d   ->  residue = %d" % (len(M([5,4,3])), A2s, A2))
print("       A3: |[4,4,3,3,2,2]| = %d   steps = %d   ->  residue = %d" % (6, A3, A3r))
SAME = (A1r == A2 == A3r)
ctl("ALL THREE A ROWS HAVE THE SAME RESIDUE [predicate, True here]", SAME, True)
ctl("  ... and that common residue is 2", A1r, 2)
# the same predicate MUST be able to return False -- negative control on a triple
# that genuinely differs, so the True above is not an unconditional True.
ctl("  negative control: residues of M((2,1,1)),M((5,3)),[4,4,3,3,2,2] differ",
    (resid([2,1,1]) == resid([5,3]) == A3r), False)
tick("part1")

print()
print("=" * 78)
print("PART 2 -- the plausible-answer SET per row, DERIVED from the brief alone")
print("=" * 78)
print("""   A judge who does not run the process still has, from the brief's own text:
     (i)  Prop C1-B, printed:  steps(L) = |L| - residue(L).
     (ii) residue >= 1 always (a length-1 list [x] steps only if x = 0, i.e. is
          already terminal), so steps <= |L| - 1.
     (iii)Thm C1-2's proof, printed:  Sum(L) = 2 * Sum(heads).  Heads are integers
          in [1, max(L)] and the FIRST head is exactly max(L).
          => steps >= 1 + ceil((Sum/2 - max) / max)   and   steps <= 1 + (Sum/2 - max).
     (iv) Conjecture C1 (SS3): s0(lambda) != lambda_1 for lambda |- 2v, k >= 2.
   None of (i)-(iv) requires running a single step.""")

def struct_steps_set(L):
    """Set of step-counts NOT excluded by (i)-(iii).  Pure arithmetic, no stepping."""
    n = len(L); S = sum(L); m = max(L)
    if S % 2: return set()
    H = S // 2
    lo = 1 + -(-(H - m) // m) if H > m else 1
    hi = min(n - 1, 1 + (H - m))
    return set(range(lo, hi + 1))

# POSITIVE control for struct_steps_set: it MUST contain the true value on the one
# instance the brief discloses, and on instances whose answers the brief prints.
ctl("struct set contains truth for the worked example M((2,1,1))",
    3 in struct_steps_set(M([2,1,1])), True)
ctl("struct set contains truth for M((5,3)) [Thm C1-2 prints 6]",
    6 in struct_steps_set(M([5,3])), True)
ctl("struct set contains truth for [4]^6 [Lemma C1-A prints 4]",
    4 in struct_steps_set([4]*6), True)
# NEGATIVE control: the set must actually EXCLUDE something, else it is vacuous.
ctl("struct set for M((6,4,2)) is a PROPER subset of 1..|M|-1",
    struct_steps_set(M([6,4,2])) < set(range(1, len(M([6,4,2])))), True)

rows = {}
for tag, L, truth in (("A1", M([6,4,2]), A1), ("A2", M([5,4,3]), A2s), ("A3", [4,4,3,3,2,2], A3)):
    S = struct_steps_set(L)
    print("   %s  L has n=%d Sum=%d max=%d  ->  steps in %s  (truth %d, in set: %s)"
          % (tag, len(L), sum(L), max(L), sorted(S), truth, truth in S))
    ctl("   %s structural set contains the true value" % tag, truth in S, True)
    rows[tag] = S

# (iv) C1 prunes A1 and A2 (both lambdas are partitions of 12, k >= 2)
print()
print("   Applying (iv) Conjecture C1  [both (6,4,2) and (5,4,3) partition 12, k=3]:")
w1 = 6; rows["A1"].discard(w1)
print("     A1: s0 != w = 6  ->  %s   (size %d)" % (sorted(rows["A1"]), len(rows["A1"])))
w2 = 5
before = len(rows["A2"]); rows["A2"] = {x for x in rows["A2"] if x != w2}
print("     A2: s0 != w = 5  ->  steps in %s ; residue = 9 - steps in %s   (size %d)"
      % (sorted(rows["A2"]), sorted(9 - x for x in rows["A2"]), len(rows["A2"])))
print("     A3: no statement in the brief speaks to it   ->  %s   (size %d)"
      % (sorted(rows["A3"]), len(rows["A3"])))
tick("part2")

print()
print("=" * 78)
print("PART 3 -- the SHORTCUT anchors the brief actually hands a judge")
print("=" * 78)
print("   Every value of s0 the brief DISCLOSES, and what a judge would read off them:")
disc = [("worked example s0((2,1,1))", [2,1,1]), ("Thm C1-2 s0((5,3))", [5,3]),
        ("Thm C1-2 s0((4,2))", [4,2]), ("Lemma C1-A s0((6)) via T(6)", [6])]
for name, lam in disc:
    v = s0(lam); w = max(lam)
    print("      %-32s = %-3s   w = %-2d   ->  v - w = %+d" % (name, v, w, v - w))
print("   => the brief's disclosed instances all read s0 = w+1 (k>=2) or s0 = w (k=1).")
print("      A JUDGE ANCHORED ON THE DISCLOSED VALUES ANSWERS A1 = 7.  Truth is 8.")
print("      Anchored on the worked example's residue (=3) they answer A2 = 3, A3 = 3.")
print("      All three anchors are WRONG.  The rows were built to defeat the anchor;")
print("      that is what makes the META-GAME below the conservative model.")

print()
print("=" * 78)
print("PART 4 -- B1 re-enumerated here (planner's figure VERIFIED, not assumed)")
print("=" * 78)
def alpha(nv, adj):
    best = 0
    for Smask in range(1 << nv):
        bits = [i for i in range(nv) if Smask >> i & 1]
        if len(bits) <= best: continue
        ok = True
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if adj[bits[i]] >> bits[j] & 1: ok = False; break
            if not ok: break
        if ok: best = len(bits)
    return best
def _cyc(n):
    adj = [0]*n
    for i in range(n):
        j = (i+1) % n; adj[i] |= 1 << j; adj[j] |= 1 << i
    return adj
def _cliq(n):
    adj = [0]*n
    for i in range(n):
        for j in range(i+1, n): adj[i] |= 1 << j; adj[j] |= 1 << i
    return adj
ctl("alpha(C_5) = 2   [POSITIVE ctrl]",  alpha(5, _cyc(5)), 2)
ctl("alpha(K_4) = 1   [POSITIVE ctrl]",  alpha(4, _cliq(4)), 1)
ctl("alpha(empty_4)=4 [POSITIVE ctrl]",  alpha(4, [0]*4), 4)

seq = [2,2,2,2,2,1,1]
nv = len(seq); tgt = sorted(seq, reverse=True)
pairsL = [(i, j) for i in range(nv) for j in range(i+1, nv)]
hist = Counter(); realizations = 0
for mask in range(1 << len(pairsL)):
    adj = [0]*nv
    for b, (i, j) in enumerate(pairsL):
        if mask >> b & 1: adj[i] |= 1 << j; adj[j] |= 1 << i
    if sorted((bin(a).count("1") for a in adj), reverse=True) != tgt: continue
    realizations += 1
    hist[alpha(nv, adj)] += 1
print("   population : all 2^%d labelled graphs on %d vertices, filtered to realizations"
      % (len(pairsL), nv))
print("   realizations of [2,2,2,2,2,1,1] : %d" % realizations)
print("   alpha histogram : %s" % dict(sorted(hist.items())))
ctl("planner's counts {3:672, 4:2835} reproduce", dict(sorted(hist.items())), {3:672, 4:2835})
ctl("B1 true answer space size = 2", len(hist), 2)
ctl("B1 key value 3 = min of that space", min(hist), declared["B1"])
tick("part4")

print()
print("=" * 78)
print("PART 5 -- is the single-latent guess ('residue = r for all three') realistic?")
print("=" * 78)
print("   Reference population: every lambda with EXACTLY 3 parts and Sum <= 30 whose")
print("   padded list terminates.  This is what 'the residue of a padded 3-part list'")
print("   ranges over.  A judge cannot compute it -- it is printed to show that the")
print("   single-latent model is not a strawman, i.e. residue really is concentrated.")
rh = Counter(); tot3 = 0
for n in range(3, 31):
    for lam in parts(n):
        if len(lam) != 3: continue
        r = resid(lam)
        if r is None: continue
        tot3 += 1; rh[r] += 1
print("   3-part lambdas with terminating M, Sum<=30 : %d" % tot3)
print("   residue(M(lambda)) histogram : %s" % dict(sorted(rh.items())))
mode, mcount = rh.most_common(1)[0]
print("   modal residue = %d with %d/%d = %.3f of the population" % (mode, mcount, tot3, mcount/tot3))
ctl("the modal residue over 3-part lambdas is 2 [predicate, True here]", mode, 2)
print("   support size = %d ; a uniform guess over the support scores %.4f" % (len(rh), 1.0/len(rh)))
tick("part5")

print()
print("=" * 78)
print("PART 6 -- THE NULL")
print("=" * 78)
sA1, sA2, sA3 = len(rows["A1"]), len(rows["A2"]), len(rows["A3"])
print("   MODEL 1 (structural): uniform over the set (i)-(iv) leaves standing.")
print("      A1 1/%d = %.4f | A2 1/%d = %.4f | A3 1/%d = %.4f"
      % (sA1, 1/sA1, sA2, 1/sA2, sA3, 1/sA3))
print("      product IF THE ROWS WERE INDEPENDENT : 1/%d = %.5f" % (sA1*sA2*sA3, 1/(sA1*sA2*sA3)))
print()
print("   MODEL 2 (meta-game, the CONSERVATIVE model -- guessing made to look EASY):")
print("      the judge assumes a row that coincides with a brief shortcut would have")
print("      been struck, so answers 'shortcut, displaced by one'.")
print("      A1: {w+1, w+2} = {7,8}          -> 1/2")
print("      A2: residue not in {k, k+1} = {3,4}, and >=1  -> {1,2} -> 1/2")
print("      A3: no shortcut exists          -> 1/%d" % sA3)
print("      product IF THE ROWS WERE INDEPENDENT : 1/%d = %.4f" % (2*2*sA3, 1/(4*sA3)))
print()
print("   *** ROW INDEPENDENCE IS NOT ESTABLISHED, AND THE PRODUCT IS THEREFORE NOT")
print("       CITABLE.  All three A rows are the SAME LATENT: residue = 2, reachable")
print("       from the brief's own Prop C1-B.  One guess answers all three.")
lat = sorted(set([9 - x for x in rows["A2"]]))
print("       residue sets: A1 %s | A2 %s | A3 %s"
      % (sorted(len(M([6,4,2])) - x for x in rows["A1"]), lat,
         sorted(6 - x for x in rows["A3"])))
print("       smallest of the three latent sets has size %d." % min(len(rows["A1"]), len(rows["A2"]), len(rows["A3"])))
print()
print("   CITABLE CONJUNCTION OVER {A1, A2, A3}  (B1 excluded, B2/B3 declined):")
print("      structural  , dependence-honest : 1/3    = %.4f" % (1/3))
print("      meta-gamed  , dependence-honest : 1/2    = %.4f" % (1/2))
print("      => the harness is worth between 1.0 and 1.6 BITS.")
print("      For comparison: the standing ~1/240 is 7.9 bits; 677's 1/4.8e6 is 22.2 bits.")
print()
print("   SEAT MULTIPLICATION IS REFUSED: cert SS6 already declined to treat the two")
print("   families as independent (the fluent-echo shape).  1/3 is not squared to 1/9.")

print()
print("=" * 78)
print("PART 7 -- HOW MUCH WORK an A row actually costs (planner's datum, checked)")
print("=" * 78)
print("   w61_r32_uniqueness.out reports 9 / 8 / 5 states explored for A1/A2/A3.")
print("   States = steps + 1, so that file is reporting 8 / 7 / 4 hand steps.")
for tag, L, st in (("A1", M([6,4,2]), 9), ("A2", M([5,4,3]), 8), ("A3", [4,4,3,3,2,2], 5)):
    n = run(L)[0]
    print("      %s : %d steps on a %d-entry list  ->  %d states ; uniqueness file says %d  %s"
          % (tag, n, len(L), n + 1, st, "MATCH" if n + 1 == st else "** MISMATCH"))
    ctl("   %s state count matches the uniqueness file" % tag, run(L)[0] + 1, st)
print("   The most expensive A row is 8 steps on a 10-entry list.  That is inside a")
print("   competent judge's HEAD, let alone a language model's scratchpad.  Landing it")
print("   demonstrates that the definitions were applied -- which is exactly what the")
print("   brief SS4 says the table grades ('non-fabrication, not correctness').  It is")
print("   NOT evidence about the six verdicts and must not be cited as if it were.")
print()
print("   ALSO, and it is a miss in the uniqueness file itself: its outcome sets print")
print("   (8, 2), (7, 2), (4, 2) -- the residue 2 is RIGHT THERE on all three rows and")
print("   the file did not remark on it.  The collinearity was visible and unnoticed.")

print()
print("   controls run : %d ; passed : %d" % (len(CTRL), sum(CTRL)))
print("   A/B diffed calls : %d ; disagreements : 0" % DIFFED)
if not all(CTRL):
    print("!! a control failed -- the null above is NOT to be cited.  exit(2)"); sys.exit(2)
print("elapsed %.1fs" % (time.time() - T0))
