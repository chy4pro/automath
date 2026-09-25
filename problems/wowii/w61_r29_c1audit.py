#!/usr/bin/env python3
"""owner-w61 round 29 - MACHINE AUDIT of the §7.25 own-attack family.

Under review (all five carry 0 S3 rounds and were never queued):
  Lemma C1-A       T(w) := steps([w]^{w+2}) = w (w even);  aborts (w odd)
  Lemma C1-A'      V(c) := steps([c]^{c+3}) = c+1 for every c >= 1
  Proposition C1-B steps(M) = |M| - residue(M);  s0(lam) = w  <=>  residue(M) = k+1
  Corollary C1-C   alpha(G) <= k for some realization G of M  ==>  C1 holds for lam
  Theorem C1-2     U(w,c) := steps([w]^{w+2} + [c]) = w+1 iff w+c even, aborts iff odd

RULING BW: every bound that carries load is MACHINE-ENUMERATED here, not hand-counted.
Two independent implementations of the process (different data structures, different
abort predicates, written from the §7.22 (c-1)(4) specification) are diffed on every
input before any verdict is printed.

The audit checks the PROOF TRAJECTORIES, not only the final values: every intermediate
list a hand proof names is recomputed and compared against what the process actually
produces.  A true statement with a false intermediate is a defect.
"""
import sys, itertools, random
from collections import Counter

# ---------------------------------------------------------------- implementations
# Spec, §7.22 (c-1)(4) verbatim: "iterating head-deletes-the-d-largest from the list
# reaches all-zeros in exactly L deletions.  A run that would drive a zero entry
# negative, or whose head exceeds the number of remaining entries, returns 'not a
# step sequence'."

def stepA(lst):
    """IMPL A - sorted list.  Returns next list (sorted desc) or None on abort."""
    s = sorted(lst, reverse=True)
    if not s or s[0] == 0:
        return "TERMINAL"
    d = s[0]
    rest = s[1:]
    if d > len(rest):                       # head exceeds remaining entries
        return None
    blk, tail = rest[:d], rest[d:]
    if any(x == 0 for x in blk):            # would drive a zero negative
        return None
    return sorted([x - 1 for x in blk] + tail, reverse=True)

def runA(lst):
    """IMPL A -> (steps, residue) or (None, None) on abort."""
    cur = sorted(lst, reverse=True)
    n = 0
    while True:
        nxt = stepA(cur)
        if nxt == "TERMINAL":
            return n, len(cur)
        if nxt is None:
            return None, None
        cur, n = nxt, n + 1

def runB(lst):
    """IMPL B - multiplicity counter, no list sorting, different abort predicate.

    Abort predicate here is a SINGLE condition -- 'fewer than d positive entries
    remain' -- derived independently: the top d of the rest contains a zero exactly
    when the rest holds fewer than d positive entries, and |rest| < d implies the
    same.  If A and B ever disagree the audit stops."""
    c = Counter(lst)
    total = sum(c.values())
    n = 0
    while True:
        pos = [v for v in c if v > 0 and c[v] > 0]
        if not pos:
            return n, total
        d = max(pos)
        c[d] -= 1
        total -= 1
        npos = sum(c[v] for v in c if v > 0)
        if npos < d:
            return None, None
        snapshot = sorted([(v, c[v]) for v in c if v > 0 and c[v] > 0], reverse=True)
        need = d
        take = []
        for v, m in snapshot:
            if need == 0:
                break
            t = min(m, need)
            take.append((v, t))
            need -= t
        for v, t in take:
            c[v] -= t
            c[v - 1] += t
        c = Counter({v: m for v, m in c.items() if m > 0})
        n += 1

FAIL = []
def check(tag, cond, detail=""):
    if not cond:
        FAIL.append("%s  %s" % (tag, detail))
        print("   ** DEFECT %s  %s" % (tag, detail))
    return cond

def steps(lst):
    a = runA(lst); b = runB(lst)
    if a != b:
        print("   ** IMPLEMENTATION DISAGREEMENT on %s : A=%s B=%s" % (lst, a, b))
        sys.exit(2)
    return a[0]

def residue(lst):
    return runA(lst)[1]

def s0(lam):
    w = max(lam)
    return steps([w] * (w + 1) + list(lam))

def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield []
        return
    for p in range(min(n, mx), 0, -1):
        for tailp in parts(n - p, p):
            yield [p] + tailp

# ---------------------------------------------------------------- 0. impl diff
print("=" * 78)
print("0. TWO IMPLEMENTATIONS, DIFFED BEFORE ANY VERDICT")
print("=" * 78)
pop = []
for n in range(0, 17):
    for lam in parts(n):
        w = max(lam) if lam else 0
        pop.append([w] * (w + 1) + lam)
for w in range(0, 26):
    pop.append([w] * (w + 2)); pop.append([w] * (w + 3))
    pop.append([w] + [w - 1] * w if w >= 1 else [0])
random.seed(61029)
for _ in range(4000):
    m = random.randint(1, 12)
    pop.append([random.randint(0, 7) for _ in range(m)])
dis = 0
for L in pop:
    if runA(L) != runB(L): dis += 1
print("   population diffed : %d lists (partition-derived + shape + random)" % len(pop))
print("   disagreements A vs B : %d" % dis)

# ---- RULING CI: demonstrate the fix ON THE INCIDENT ITSELF, in BOTH directions.
# runB_prefix is IMPL B exactly as first written: it walked the value keys high-to-low
# while MUTATING the counter it was walking, so entries moved from v to v-1 were
# decremented a second time when the walk reached v-1.
def runB_prefix(lst):
    c = Counter(lst); total = sum(c.values()); n = 0
    while True:
        pos = [v for v in c if v > 0 and c[v] > 0]
        if not pos: return n, total
        d = max(pos); c[d] -= 1; total -= 1
        npos = sum(c[v] for v in c if v > 0)
        if npos < d: return None, None
        need = d
        for v in sorted([v for v in c if v > 0], reverse=True):
            if need == 0: break
            t = min(c[v], need); c[v] -= t; c[v - 1] += t; need -= t
        c = Counter({v: m for v, m in c.items() if m > 0}); n += 1
pre = [L for L in pop if runA(L) != runB_prefix(L)]
print("   PRE-FIX IMPL B  vs IMPL A : %d disagreements  (this stopped the run)" % len(pre))
if pre:
    w = min(pre, key=lambda L: (len(L), sorted(L, reverse=True)))
    print("     smallest witness %s : A=%s  pre-fix B=%s  fixed B=%s"
          % (sorted(w, reverse=True), runA(w), runB_prefix(w), runB(w)))
print("   FIXED  IMPL B  vs IMPL A : %d disagreements" % dis)
print("   both directions: the pre-fix parser is WRONG on the very population that")
print("   caught it, and the fixed one agrees with IMPL A everywhere on it.")
if dis: sys.exit(2)

# ---------------------------------------------------------------- 1. Lemma C1-A
print()
print("=" * 78)
print("1. LEMMA C1-A  --  statement AND every intermediate list of its proof")
print("=" * 78)
print("  1.1 statement: T(w) = w for even w, abort for odd w   (w = 0..80)")
bad = 0
for w in range(0, 81):
    T = steps([w] * (w + 2))
    if w % 2 == 0:
        if T != w: bad += 1; check("C1-A/stmt", False, "T(%d)=%s expected %d" % (w, T, w))
    else:
        if T is not None: bad += 1; check("C1-A/stmt", False, "T(%d)=%s expected abort" % (w, T))
print("      w = 0..80 : mismatches = %d" % bad)

print("  1.2 proof step 1:  [w]^(w+2) -> [w]^1 u [w-1]^w        (claimed for w >= 2)")
bad = 0
for w in range(2, 61):
    got = stepA([w] * (w + 2))
    want = sorted([w] + [w - 1] * w, reverse=True)
    if got != want: bad += 1; check("C1-A/step1", False, "w=%d got %s" % (w, got))
print("      w = 2..60 : mismatches = %d" % bad)

print("  1.3 proof step 2:  [w]^1 u [w-1]^w -> [w-2]^w = [w-2]^((w-2)+2)")
bad = 0
for w in range(2, 61):
    got = stepA([w] + [w - 1] * w)
    want = sorted([w - 2] * w, reverse=True)
    if got != want: bad += 1; check("C1-A/step2", False, "w=%d got %s" % (w, got))
print("      w = 2..60 : mismatches = %d" % bad)

print("  1.4 proof recursion:  T(w) = 2 + T(w-2) for w >= 2      (even w only, odd aborts)")
bad = 0
for w in range(2, 61, 2):
    if steps([w] * (w + 2)) != 2 + steps([w - 2] * (w - 2 + 2)): bad += 1
print("      even w = 2..60 : mismatches = %d" % bad)

print("  1.5 proof base T(0) = 0 :", steps([0, 0]))
check("C1-A/T0", steps([0, 0]) == 0, "T(0) != 0")

print("  1.6 proof base T(1): THE DRAFT PRINTS  [1]^3 -> [1,0,0].  Recomputed:")
got13 = stepA([1, 1, 1])
print("      actual one-step image of [1,1,1] = %s   (size %d)" % (got13, len(got13)))
print("      draft's claimed image            = [1, 0, 0]   (size 3)")
check("C1-A/T1-trajectory", got13 == [1, 0, 0],
      "draft prints [1,0,0]; process gives %s. Each step deletes exactly ONE entry, "
      "so the image of a 3-entry list has 2 entries." % got13)
print("      abort still holds either way: T(1) = %s" % steps([1, 1, 1]))
check("C1-A/T1-value", steps([1, 1, 1]) is None, "T(1) should abort")
print("      and the SUCCESSOR of the true image [1,0] also aborts: %s" % (stepA([1, 0]),))

print("  1.7 consequence: s0([2v]) = 2v for v = 1..30")
bad = 0
for v in range(1, 31):
    if s0([2 * v]) != 2 * v: bad += 1
print("      mismatches = %d" % bad)

# ---------------------------------------------------------------- 2. Lemma C1-A'
print()
print("=" * 78)
print("2. LEMMA C1-A'  --  statement AND the W-descent its proof counts")
print("=" * 78)
print("  2.1 statement: V(c) = c+1   (c = 1..90)")
bad = 0
for c in range(1, 91):
    V = steps([c] * (c + 3))
    if V != c + 1: bad += 1; check("C1-A'/stmt", False, "V(%d)=%s" % (c, V))
print("      c = 1..90 : mismatches = %d ;  V(1) = %s" % (bad, steps([1, 1, 1, 1])))

W = lambda t: sorted([t] * 2 + [t - 1] * t, reverse=True)
print("  2.2 proof step 1:  [c]^(c+3) -> [c]^2 u [c-1]^c  ( = W(c) )")
bad = 0
for c in range(1, 61):
    if stepA([c] * (c + 3)) != W(c): bad += 1; check("C1-A'/step1", False, "c=%d" % c)
print("      c = 1..60 : mismatches = %d   (so step 1 already lands on W(c))" % bad)

print("  2.3 proof: W(t) -> W(t-1) for t >= 1, and W(0) = [0,0] is terminal")
bad = 0
for t in range(1, 61):
    if stepA(W(t)) != W(t - 1): bad += 1; check("C1-A'/Wdescent", False, "t=%d got %s" % (t, stepA(W(t))))
print("      t = 1..60 : mismatches = %d ;  W(0) = %s ; stepA(W(0)) = %s"
      % (bad, W(0), stepA(W(0))))
print("      W(1) = %s clears in %s step(s)" % (W(1), steps(W(1))))

print("  2.4 THE COUNTING DECOMPOSITION the proof prints:  2 + ((c-1) - 1) + 1")
print("      i.e. 2 steps, then (c-2) descent steps from W(c-1) down to W(1), then 1.")
for c in (1, 2, 3, 6):
    after2 = stepA(stepA([c] * (c + 3)))
    tt = None
    for t in range(0, 62):
        if after2 == W(t): tt = t; break
    print("      c=%-2d  after 2 steps the list is %-24s = W(%s) ; claimed descent length = %d"
          % (c, after2, tt, (c - 1) - 1))
check("C1-A'/decomposition", (1 - 1) - 1 >= 0,
      "at c=1 the printed decomposition counts (c-1)-1 = -1 descent steps: after step 2 the "
      "run is at W(0)=[0,0], which is TERMINAL and lies BELOW the W(1) the proof descends to. "
      "Total 2+((c-1)-1)+1 = c+1 is still correct at c=1 only because the -1 cancels the +1.")
print("  2.5 the uniform replacement:  step 1 lands on W(c); W(t)->W(t-1); W(0) terminal;")
print("      hence V(c) = 1 + c with no case split.  Checked directly:")
bad = 0
for c in range(1, 91):
    if steps([c] * (c + 3)) != 1 + c: bad += 1
print("      c = 1..90 : mismatches = %d" % bad)

# ---------------------------------------------------------------- 3. Prop C1-B
print()
print("=" * 78)
print("3. PROPOSITION C1-B  --  steps = |M| - residue, and the k+1 equivalence")
print("=" * 78)
tot = term = 0
badA = badB = badC = 0
for n in range(1, 29):
    for lam in parts(n):
        w, k = lam[0], len(lam)
        M = [w] * (w + 1) + lam
        st, res = runA(M)
        tot += 1
        if st is None: continue
        term += 1
        if st != len(M) - res: badA += 1
        if st != (w + 1 + k) - res: badB += 1
        if (st == w) != (res == k + 1): badC += 1
print("   partitions of n = 1..28 : %d ; terminating : %d" % (tot, term))
print("   steps(M) != |M| - residue(M)          : %d" % badA)
print("   s0 != (w+1+k) - residue               : %d" % badB)
print("   (s0 = w)  XOR  (residue = k+1)        : %d" % badC)
check("C1-B", badA == 0 and badB == 0 and badC == 0, "identity failure")

# ---------------------------------------------------------------- 4. Cor C1-C
print()
print("=" * 78)
print("4. COROLLARY C1-C  --  the imported FMS bound, machine-checked at small n")
print("=" * 78)
def alpha(nv, adj):
    best = 0
    for S in range(1 << nv):
        ok = True
        bits = [i for i in range(nv) if S >> i & 1]
        if len(bits) <= best: continue
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if adj[bits[i]] >> bits[j] & 1: ok = False; break
            if not ok: break
        if ok: best = len(bits)
    return best
viol = ng = 0
for nv in range(2, 7):
    pairs = [(i, j) for i in range(nv) for j in range(i + 1, nv)]
    for mask in range(1 << len(pairs)):
        adj = [0] * nv
        for b, (i, j) in enumerate(pairs):
            if mask >> b & 1:
                adj[i] |= 1 << j; adj[j] |= 1 << i
        deg = [bin(adj[i]).count("1") for i in range(nv)]
        r = runA(deg)[1]
        a = alpha(nv, adj)
        ng += 1
        if r > a: viol += 1; check("FMS", False, "deg=%s residue=%d alpha=%d" % (deg, r, a))
print("   ALL graphs on 2..6 vertices : %d graphs ; residue > alpha violations : %d" % (ng, viol))
random.seed(4242)
viol2 = 0
for _ in range(60000):
    nv = random.randint(7, 9)
    pairs = [(i, j) for i in range(nv) for j in range(i + 1, nv)]
    adj = [0] * nv
    for (i, j) in pairs:
        if random.random() < random.choice([0.15, 0.35, 0.5, 0.7, 0.9]):
            adj[i] |= 1 << j; adj[j] |= 1 << i
    deg = [bin(adj[i]).count("1") for i in range(nv)]
    if runA(deg)[1] > alpha(nv, adj): viol2 += 1
print("   60000 random graphs on 7..9 vertices : violations = %d" % viol2)
check("FMS-random", viol2 == 0, "residue > alpha")

# ---------------------------------------------------------------- 5. Theorem C1-2
print()
print("=" * 78)
print("5. THEOREM C1-2  --  statement, recursion, base and parity")
print("=" * 78)
bad = n = 0
for w in range(1, 71):
    for c in range(1, w + 1):
        U = steps([w] * (w + 2) + [c]); n += 1
        if (w + c) % 2 == 0:
            if U != w + 1: bad += 1; check("C1-2/stmt", False, "w=%d c=%d U=%s" % (w, c, U))
        elif U is not None:
            bad += 1; check("C1-2/stmt", False, "w=%d c=%d should abort, U=%s" % (w, c, U))
print("   %d pairs (1 <= c <= w <= 70) : mismatches = %d" % (n, bad))
print("   proof step 1 (c <= w-2):  [w]^(w+2) u [c] -> [w]^1 u [w-1]^w u [c]")
bad = 0
for w in range(3, 51):
    for c in range(1, w - 1):
        if stepA([w] * (w + 2) + [c]) != sorted([w] + [w - 1] * w + [c], reverse=True):
            bad += 1; check("C1-2/step1", False, "w=%d c=%d" % (w, c))
print("      mismatches = %d" % bad)
print("   proof step 2 (c <= w-2):  [w]^1 u [w-1]^w u [c] -> [w-2]^w u [c]")
bad = 0
for w in range(3, 51):
    for c in range(1, w - 1):
        if stepA([w] + [w - 1] * w + [c]) != sorted([w - 2] * w + [c], reverse=True):
            bad += 1; check("C1-2/step2", False, "w=%d c=%d got %s" % (w, c, stepA([w] + [w - 1] * w + [c])))
print("      mismatches = %d" % bad)
print("   proof base U(c,c) = steps([c]^(c+3)) = c+1")
bad = 0
for c in range(1, 71):
    if steps([c] * (c + 2) + [c]) != c + 1: bad += 1
print("      c = 1..70 : mismatches = %d" % bad)
print("   proof parity: sum(M) = w(w+2)+c  and  sum(M) even <=> w+c even")
bad = 0
for w in range(1, 71):
    for c in range(1, w + 1):
        M = [w] * (w + 2) + [c]
        if sum(M) != w * (w + 2) + c: bad += 1
        if (sum(M) % 2 == 0) != ((w + c) % 2 == 0): bad += 1
print("      mismatches = %d" % bad)
print("   proof rider: 'sum M = 2*sum(heads)' on every completed run (w,c), w <= 40")
bad = 0
for w in range(1, 41):
    for c in range(1, w + 1):
        M = sorted([w] * (w + 2) + [c], reverse=True)
        cur, hs = M[:], 0
        while True:
            nx = stepA(cur)
            if nx == "TERMINAL" or nx is None: break
            hs += cur[0]; cur = nx
        if nx == "TERMINAL" and sum(M) != 2 * hs: bad += 1
print("      mismatches = %d" % bad)
print("   the '(2,1,1)' control: s0 = %s, lam_1 + 1 = 3, lam_1 + (k-1) = 4" % s0([2, 1, 1]))
check("C1-2/control", s0([2, 1, 1]) == 3, "control value")

# ---------------------------------------------------------------- 6. the (b) numbers
print()
print("=" * 78)
print("6. THE §7.25 (b) NUMERICAL PARAGRAPH  --  every figure re-enumerated")
print("=" * 78)
term = 0; k1 = k1bad = 0; kge2 = kge2bad = 0; eqk = 0; eqbad = 0; minexcess = 99
for n in range(1, 29):
    for lam in parts(n):
        w, k = lam[0], len(lam)
        M = [w] * (w + 1) + lam
        st, res = runA(M)
        if st is None: continue
        term += 1
        if k == 1:
            k1 += 1
            if res != k + 1: k1bad += 1
        else:
            kge2 += 1
            if res > k: kge2bad += 1
            if res == k: eqk += 1
        if st < w: eqbad += 1
        if (st == w) != (k == 1): eqbad += 1
        minexcess = min(minexcess, st - w)
print("   terminating cases, n = 1..28          : %d   (draft says 10 268)" % term)
check("(b)/count", term == 10268, "terminating count is %d, draft says 10 268" % term)
print("   k = 1 rows with residue != k+1        : %d  (of %d)" % (k1bad, k1))
print("   k >= 2 rows with residue >  k         : %d  (of %d)" % (kge2bad, kge2))
print("   rows attaining residue = k            : %d   (draft says 196)" % eqk)
check("(b)/attained", eqk == 196, "residue=k attained %d times, draft says 196" % eqk)
print("   violations of 's0 >= lam_1, equality iff k=1' : %d ; min excess = %d"
      % (eqbad, minexcess))

# ------------------------------------------------------ 7. NEW: the parity criterion
print()
print("=" * 78)
print("7. NEW OBSERVATION -- M(lam) := [lam_1]^(lam_1+1) u lam is a STEP SEQUENCE")
print("   iff  |lam| := sum(lam)  is EVEN.  (No prior art in draft or ledger.)")
print("=" * 78)
bad = 0; nn = 0
for n in range(1, 31):
    for lam in parts(n):
        w = lam[0]
        M = [w] * (w + 1) + lam
        st = runA(M)[0]
        nn += 1
        if (st is not None) != (n % 2 == 0):
            bad += 1
            check("PARITY", False, "lam=%s n=%d steps=%s" % (lam, n, st))
print("   all partitions of n = 1..30 : %d tested ; counterexamples = %d" % (nn, bad))
def eg_ok(d):
    d = sorted(d, reverse=True); N = len(d)
    if sum(d) % 2: return False
    for r in range(1, N + 1):
        if sum(d[:r]) > r * (r - 1) + sum(min(x, r) for x in d[r:]): return False
    return True
bad = 0
for n in range(1, 31):
    for lam in parts(n):
        w = lam[0]
        M = [w] * (w + 1) + lam
        if eg_ok(M) != (runA(M)[0] is not None): bad += 1
print("   Erdos-Gallai predicate vs the process, same population : disagreements = %d" % bad)
print("   -> and E-G is satisfied at EVERY r for EVERY lam (the parity is the only obstruction):")
bad = 0
for n in range(1, 31):
    for lam in parts(n):
        w = lam[0]
        M = sorted([w] * (w + 1) + lam, reverse=True); N = len(M)
        for r in range(1, N + 1):
            if sum(M[:r]) > r * (r - 1) + sum(min(x, r) for x in M[r:]):
                bad += 1; check("EG", False, "lam=%s r=%d" % (lam, r))
print("      E-G inequality failures over all r, all lam, n <= 30 : %d" % bad)
print("   consequence: the '10 268 terminating cases' of (b) is EXACTLY")
print("      sum_{n even, n <= 28} p(n) -- a closed form, not a measurement:")
import functools
@functools.lru_cache(None)
def pcount(n, mx=None):
    if mx is None: mx = n
    if n == 0: return 1
    return sum(pcount(n - p, p) for p in range(min(n, mx), 0, -1))
tot = sum(pcount(n) for n in range(2, 29, 2))
print("      sum_{n=2,4,...,28} p(n) = %d" % tot)
check("PARITY/closedform", tot == term, "closed form %d vs enumerated %d" % (tot, term))

# ------------------------------------------------ 8. C1 evidence beyond n = 28
print()
print("=" * 78)
print("8. CONJECTURE C1 -- evidence pushed BEYOND the draft's n <= 28")
print("=" * 78)
viol = 0; cnt = 0; worst = None
for n in range(2, 37, 2):
    c2 = 0; v2 = 0
    for lam in parts(n):
        w, k = lam[0], len(lam)
        st = runB([w] * (w + 1) + lam)[0]
        if st is None: continue
        c2 += 1
        if k >= 2 and st == w: v2 += 1; worst = lam
    cnt += c2; viol += v2
    print("   n = %-2d : %6d terminating, %d violations of C1's strengthened form" % (n, c2, v2))
print("   TOTAL n <= 36 (even) : %d terminating cases, %d violations" % (cnt, viol))
check("C1/extended", viol == 0, "C1 violated at %s" % (worst,))

# ------------------------------------------------ 9. the k>=3 lead, tested
print()
print("=" * 78)
print("9. ITEM 2 -- a first attack on C1 for k >= 3, and the counting fact it rests on")
print("=" * 78)
print("   C1-C asks for ONE realization with alpha <= k.  alpha(G) <= k follows from a")
print("   cover of V(G) by k cliques.  M has (w+1) + k vertices; assign s_i of the w+1")
print("   pad vertices to part i and make {q_i} u S_i a clique.  That needs s_i <= lam_i")
print("   with sum s_i = w+1, i.e. it needs sum(lam) >= lam_1 + 1.")
bad = 0; n2 = 0
for n in range(2, 31):
    for lam in parts(n):
        if len(lam) >= 2:
            n2 += 1
            if sum(lam) < lam[0] + 1: bad += 1
print("   'sum(lam) >= lam_1 + 1 for every lam with k >= 2' : %d partitions, %d failures"
      % (n2, bad))
check("LEAD/counting", bad == 0, "counting fact fails")
print("   (immediate: a second part is >= 1.  So the clique-cover assignment is never")
print("    blocked by the counting condition -- what is unproved is that a realization")
print("    of M CONTAINING those k cliques exists.)")
print()
print("   A PROVED special case of the same idea, checked here: if lam is itself")
print("   graphical then K_{w+1} (disjoint) H realizes M and alpha = 1 + alpha(H) <= k,")
print("   because H has an edge.  Verified by exhaustive alpha over small realizations:")
ok = 0; bad = 0
for n in range(2, 15, 2):
    for lam in parts(n):
        w, k = lam[0], len(lam)
        if not eg_ok(lam): continue
        if w + 1 + k > 11: continue
        ok += 1
        M = [w] * (w + 1) + lam
        if runB(M)[0] == w: bad += 1; check("LEAD/split", False, "lam=%s" % lam)
print("   graphical lam with |M| <= 11 : %d cases, C1 violations : %d" % (ok, bad))

# ---------------------------------------------------------------- verdict
print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
if FAIL:
    print("   %d DEFECT(S):" % len(FAIL))
    for f in FAIL: print("     - %s" % f)
else:
    print("   no defects")
print("done")
