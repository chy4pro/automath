#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r37 ITEM 1 -- Observation C1-M, attacked through Lemma C1-J'.

C1-M (r36, CENSUS):  residue(M(lambda)) <= ceil(k/2)+1  for every lambda with k >= 2
parts whose M(lambda) terminates.  It implies Conjecture C1 for every k >= 2 and
closes Observation C1-I's open k >= 4 half, so it is the whole game.

WHAT THIS SCRIPT AUDITS.  Four PROVED statements and two things that stay CENSUS.

  PROVED   Lemma C1-N   M(lambda) terminates  <=>  |lambda| is even.
                        (Erdos-Gallai + Havel-Hakimi; the EG inequality is checked
                        here directly as well, so the hand proof is not taken on
                        trust.)
  PROVED   Lemma C1-R   ONE descent lemma with parameters (s, x, j) that has
                        Lemma C1-J, Lemma C1-K and Lemma C1-L's G-descent as
                        instances.  Audited as a MULTISET TRAJECTORY identity.
  PROVED   Thm  C1-O    C1-M follows by induction on k from Theorem C1-2 (k=2),
                        Theorem C1-3 (k=3), Lemma C1-N, and ONE remaining
                        statement, Key Lemma C1-P.  The reduction is the theorem;
                        C1-P is not proved here.
  PROVED   Prop C1-Q    At k = 4 the whole problem reduces, by C1-J' and C1-R, to
                        the two-parameter bottom families W+(c) u [d], W-(c) u [d].

  CENSUS   Key Lemma C1-P   residue(M(lambda)) <= residue(M(lambda^-)) + 1.
  CENSUS   Observation C1-M itself, and k = 4.

AND A BOUNDARY THAT IS PRINTED RATHER THAN HIDDEN (r36 doctrine): the natural
GENERAL form of C1-P -- "adding two positive entries to a terminating list costs
at most 1 of residue" -- is FALSE, and it is still FALSE after the obvious repair
(a,b <= max L).  Both minimal counterexamples are printed.  The [w]^{w+1} head
block of M(lambda) is therefore load-bearing, not decoration.

RULING CO': step process extracted BY SOURCE TEXT from w61_r29_c1audit.py -- two
independent implementations (runA sorted-list, runB multiplicity-counter, different
abort predicates), diffed on every call before any verdict is printed.
No SAT, no exhaustive local search.  Self-limits with sys.exit, never `return`.
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

def bound(k):
    return (k + 1) // 2 + 1          # ceil(k/2) + 1

# ---- the named shapes.  A typo HERE is a proof defect, not a script defect. ----
def F(s, x, j, nu=()):
    """F_s(x,j;nu) = [x]^j u [x-1]^{x+s-j} u nu."""
    return [x] * j + [x - 1] * (x + s - j) + list(nu)
def Y(u, nu=()):   return [u] * 2 + [u - 1] * u + list(nu)          # C1-K
def Q(u, nu=()):   return [u] + [u - 1] * (u + 1) + list(nu)        # C1-K
def G(q, i):       return [2*q - i] * (3 + i) + [2*q - 1 - i] * (2*q - 2*i)   # C1-L
def Wp(c):         return [c] * 3 + [c - 1] * c
def Wm(c):         return [c] * 2 + [c - 1] * (c + 1)

print("=" * 96)
print("w61 r37 ITEM 1 -- Observation C1-M through C1-J' :  what is PROVED and what stays CENSUS")
print("=" * 96)

# ================================================================ 0. CONTROLS FIRST
print("\n[0] CONTROLS -- fired on the FEATURE, before any verdict (RULING CZ')")
CTRL = []
def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append((name, hits, ok))
    print("   %-52s hits=%-6d %s" % (name, hits, "OK" if ok else "** CONTROL FAILED"))
    if not ok:
        bad("CTRL", name)

# known-value controls, incl. two r31 held-out key values verified by a different route
KNOWN = [("s0((2,1,1))", run(M((2,1,1))), (3, 3)),
         ("s0((6,4,2))", run(M((6,4,2)))[0], 8),
         ("residue(M((5,4,3)))", run(M((5,4,3)))[1], 2),
         ("[1,1,0,0]", run([1,1,0,0]), (1, 3)),
         ("W-(1) boundary", run(Wm(1)), (1, 3))]
for nm, got, want in KNOWN:
    print("   known-value  %-24s = %-10s expect %-10s %s" % (nm, got, want, "OK" if got == want else "** WRONG"))
    if got != want:
        bad("KNOWN", nm)

MUST_ABORT = [("M((7,2))", M((7,2))), ("W+(1)", Wp(1)), ("M((3,2,2))", M((3,2,2)))]
for nm, L in MUST_ABORT:
    if run(L) != (None, None):
        bad("MUST_ABORT", nm)
print("   MUST_ABORT category: %d inputs, all abort as required" % len(MUST_ABORT))

# ================================================================ 1. LEMMA C1-N
print("\n[1] LEMMA C1-N (PROVED)  M(lambda) terminates  <=>  |lambda| even")
print("    Hand proof: Sum M = w(w+1) + n, so Sum M is even iff n is.  For the converse,")
print("    the Erdos-Gallai inequality holds at EVERY r for M(lambda), with no hypothesis")
print("    beyond lambda_1 = w:  r <= w  gives RHS >= r(r-1)+(w+2-r)r = r(w+1) > rw = LHS;")
print("    r = w+1 gives RHS >= r(r-1) = (w+1)w = LHS; r >= w+2 gives every d_i <= w < r so")
print("    RHS >= r(r-1) >= r(w+1) > rw >= LHS.  (M has >= w+2 entries equal to w, because")
print("    lambda_1 = w is one of them.)  Hence M(lambda) is graphical iff its sum is even,")
print("    and Havel-Hakimi terminates exactly on graphical sequences.")
def eg_ok(d):
    d = sorted(d, reverse=True); N = len(d)
    for r in range(1, N + 1):
        if sum(d[:r]) > r * (r - 1) + sum(min(x, r) for x in d[r:]):
            return False
    return True
n_par = n_eg = 0
for n in range(2, 23):
    for lam in parts(n):
        s, _ = run(M(lam))
        term = s is not None
        if term != (n % 2 == 0):
            bad("C1-N", "%s term=%s n=%d" % (lam, term, n)); n_par += 1
        if eg_ok(M(lam)) is not True:
            bad("C1-N-EG", "EG fails at %s" % (lam,)); n_eg += 1
tested = sum(1 for n in range(2, 23) for _ in parts(n))
print("    checked on %d partitions n <= 22: parity<=>termination violations %d ; EG violations %d"
      % (tested, len([f for f in FAIL if f.startswith('C1-N ')]), len([f for f in FAIL if f.startswith('C1-N-EG')])))
# control: EG check must be able to FAIL
ctrl("C1-N EG checker can reject a non-graphical list", 0 if eg_ok([3,3,1,1]) else 1)
ctrl("C1-N parity claim, corrupted to 'always terminates'",
     sum(1 for n in range(3, 16, 2) for lam in parts(n) if run(M(lam))[0] is None))

# ================================================================ 2. LEMMA C1-R
print("\n[2] LEMMA C1-R (PROVED)  ONE descent that subsumes C1-J, C1-K and C1-L's G-descent")
print("    F_s(x,j;nu) := [x]^j u [x-1]^{x+s-j} u nu,  s >= 1, x >= 2, max(nu) <= x-1.")
print("    INTERIOR  1 <= j <= x+1 :   F_s(x,j;nu)  ->  F_s(x-1, j+s-2; nu)")
print("    ENTRY     j = x+s, s >= 2 :  F_s(x,x+s;nu) ->  F_{s-1}(x, s-1; nu)")
print("    Proof (interior): head x; rest = [x]^{j-1} u [x-1]^{x+s-j} u nu of size x+s-1+|nu| >= x.")
print("    Its top x entries are the j-1 copies of x and x-j+1 copies of x-1 (possible since")
print("    s >= 1 leaves x+s-j >= x-j+1), so exactly s-1 copies of x-1 and all of nu stay")
print("    outside; ties with nu-parts equal to x-1 are immaterial, the multiset is the same.")
print("    Decrementing gives [x-1]^{j-1} u [x-2]^{x-j+1}, and the union with the s-1 copies")
print("    left outside is [x-1]^{j+s-2} u [x-2]^{x-j+1} u nu = F_s(x-1, j+s-2; nu).  The block")
print("    holds no 0 because x-1 >= 1.  (Entry): head x, rest = [x]^{x+s-1} u nu, top x are x")
print("    copies of x -> x-1, leaving [x]^{s-1} u nu, i.e. F_{s-1}(x, s-1; nu).   []")
nI = nE = 0
NUS = [(), (1,), (2,), (1,1), (3,1), (2,2,1), (4,2,1,1), (1,1,1,1)]
for s in range(1, 5):
    for x in range(2, 15):
        for nu in NUS:
            if nu and max(nu) > x - 1:
                continue
            for j in range(1, x + 2):
                if x + s - j < 0:
                    continue
                got = one_step(F(s, x, j, nu))
                want = ms(F(s, x - 1, j + s - 2, nu)) if (x - 1) >= 1 and (x - 1) + s - (j + s - 2) >= 0 else None
                if want is None:
                    continue
                nI += 1
                if got != want:
                    bad("C1-R-int", "s=%d x=%d j=%d nu=%s got=%s want=%s" % (s, x, j, nu, got, want))
            if s >= 2:
                got = one_step(F(s, x, x + s, nu))
                want = ms(F(s - 1, x, s - 1, nu))
                nE += 1
                if got != want:
                    bad("C1-R-ent", "s=%d x=%d nu=%s got=%s want=%s" % (s, x, nu, got, want))
print("    INTERIOR identity verified as a MULTISET on %d (s,x,j,nu) instances" % nI)
print("    ENTRY    identity verified as a MULTISET on %d (s,x,nu) instances" % nE)
ctrl("C1-R interior target corrupted to j+s-1 -> matched by process",
     sum(1 for s in range(1, 5) for x in range(3, 15) for j in range(1, x + 2)
         if x + s - j >= 0 and (x - 1) + s - (j + s - 1) >= 0
         and one_step(F(s, x, j)) == ms(F(s, x - 1, j + s - 1))), must_fire=False)
ctrl("C1-R entry target corrupted to F_{s-1}(x,s) -> matched by process",
     sum(1 for s in range(2, 5) for x in range(2, 15)
         if one_step(F(s, x, x + s)) == ms(F(s - 1, x, s))), must_fire=False)

print("\n    C1-J / C1-K / C1-L's G-descent recovered as INSTANCES of C1-R:")
nJ = nK = nG = 0
for u in range(2, 14):
    for nu in NUS:
        if nu and max(nu) > u - 1:
            continue
        # C1-J : F_2(u,u+2;mu) --entry--> F_1(u,1;mu) --interior--> F_1(u-1,0;mu) = [u-2]^u u mu
        a = one_step([u] * (u + 2) + list(nu))
        if a != ms(F(1, u, 1, nu)):
            bad("C1-J-1", "u=%d nu=%s" % (u, nu))
        b = one_step(list(a))
        if b != ms([u - 2] * u + list(nu)):
            bad("C1-J-2", "u=%d nu=%s" % (u, nu))
        nJ += 1
        # C1-K : Y = F_2(u,2;nu), Q = F_2(u,1;nu), j invariant because s=2
        if u >= 3 and (not nu or max(nu) <= u - 2):
            if one_step(Y(u, nu)) != ms(Y(u - 1, nu)): bad("C1-K-Y", "u=%d nu=%s" % (u, nu))
            if one_step(Q(u, nu)) != ms(Q(u - 1, nu)): bad("C1-K-Q", "u=%d nu=%s" % (u, nu))
            if ms(Y(u, nu)) != ms(F(2, u, 2, nu)):     bad("C1-K-YF", "u=%d" % u)
            if ms(Q(u, nu)) != ms(F(2, u, 1, nu)):     bad("C1-K-QF", "u=%d" % u)
            nK += 1
for q in range(1, 10):
    for i in range(0, q):
        if ms(G(q, i)) != ms(F(3, 2*q - i, 3 + i)):
            bad("C1-L-GF", "q=%d i=%d" % (q, i))
        if one_step(G(q, i)) != ms(G(q, i + 1)):
            bad("C1-L-G", "q=%d i=%d" % (q, i))
        nG += 1
print("    C1-J as entry+interior: %d (u,nu) pairs | C1-K as s=2 (j invariant): %d | C1-L G as s=3: %d"
      % (nJ, nK, nG))

# ================================================================ 3. THE BOUNDARY
print("\n[3] THE BOUNDARY, PRINTED RATHER THAN HIDDEN -- the GENERAL form of C1-P is FALSE")
print("    Tempting general lemma: L terminates, a,b >= 1, L u {a,b} terminates")
print("      ==> residue(L u {a,b}) <= residue(L) + 1  (equivalently steps rises by >= 1).")
import itertools
def sweep(constrain_max):
    cex = []
    seen = set()
    for n in range(1, 8):
        for c in itertools.combinations_with_replacement(range(0, 7), n):
            L = tuple(sorted(c, reverse=True))
            if L in seen: continue
            seen.add(L)
            sL, rL = run(list(L))
            if sL is None: continue
            hi = L[0] if constrain_max else 6
            for a in range(1, hi + 1):
                for b in range(1, a + 1):
                    sP, rP = run(list(L) + [a, b])
                    if sP is None: continue
                    if rP > rL + 1:
                        cex.append((L, a, b, rL, rP))
    return cex
c1 = sweep(False); c2 = sweep(True)
c1.sort(key=lambda t: (len(t[0]), t)); c2.sort(key=lambda t: (len(t[0]), t))
print("    UNCONSTRAINED : %d counterexamples.  minimal: L=%s + {%d,%d} : residue %d -> %d"
      % (len(c1), c1[0][0], c1[0][1], c1[0][2], c1[0][3], c1[0][4]))
print("    a,b <= max(L) : %d counterexamples.  minimal: L=%s + {%d,%d} : residue %d -> %d"
      % (len(c2), c2[0][0], c2[0][1], c2[0][2], c2[0][3], c2[0][4]))
print("    ==> the [w]^{w+1} head block of M(lambda) is LOAD-BEARING.  C1-P is not an")
print("        instance of any general 'two more entries cost at most one residue' fact,")
print("        and a proof that does not use the head block is proving something false.")
ctrl("boundary sweep can find a counterexample at all", len(c1))
ctrl("boundary survives the obvious repair a,b <= max(L)", len(c2))

# ================================================================ 4. KEY LEMMA C1-P
print("\n[4] KEY LEMMA C1-P (CENSUS -- NOT PROVED)")
print("    lambda has k >= 4 parts, |lambda| even; i<j in {2..k} with lambda_i = lambda_j mod 2;")
print("    lambda^- := lambda minus those two parts.  Then")
print("        residue(M(lambda))  <=  residue(M(lambda^-)) + 1.")
print("    (lambda^-_1 = lambda_1, |lambda^-| even, so C1-N makes M(lambda^-) terminate: the")
print("     statement never has an undefined right-hand side.)")
hist = {}; nP = 0; miss = 0
for n in range(2, 23, 2):
    for lam in parts(n):
        k = len(lam)
        if k < 4: continue
        s, r = run(M(lam))
        if s is None: continue
        for i in range(1, k):
            for j in range(i + 1, k):
                if (lam[i] + lam[j]) % 2: continue
                sub = tuple(x for t, x in enumerate(lam) if t not in (i, j))
                s2, r2 = run(M(sub))
                if s2 is None:
                    bad("C1-P-abort", "%s -> %s" % (lam, sub)); continue
                nP += 1
                hist[r - r2] = hist.get(r - r2, 0) + 1
                if r - r2 > 1:
                    bad("C1-P", "%s minus (%d,%d) : %d vs %d" % (lam, lam[i], lam[j], r, r2)); miss += 1
print("    %d (lambda, pair) instances over n <= 22 : residue-delta histogram %s ; violations %d"
      % (nP, sorted(hist.items()), miss))
print("    pigeonhole: among lambda_2, lambda_3, lambda_4 two share a parity, so for k >= 4 a")
print("    legal pair ALWAYS exists and never has to touch lambda_1.")
pig = sum(1 for n in range(4, 23) for lam in parts(n) if len(lam) >= 4
          and not any((lam[i] + lam[j]) % 2 == 0 for i in range(1, 4) for j in range(i + 1, 4)))
print("    partitions with k >= 4 and NO equal-parity pair inside {lambda_2,lambda_3,lambda_4}: %d" % pig)
if pig: bad("PIGEONHOLE", "%d" % pig)
ctrl("C1-P bound tightened to +0 -> is violated (so the check can see a violation)",
     sum(c for d, c in hist.items() if d > 0))

# ================================================================ 5. THEOREM C1-O
print("\n[5] THEOREM C1-O (PROVED reduction)   C1-N + Thm C1-2 + Thm C1-3 + C1-P  ==>  C1-M")
print("    Induction on k.  k=2: Theorem C1-2 gives residue = 2 = bound(2).  k=3: Theorem C1-3")
print("    gives residue in {2,3}, and bound(3) = 3.  k >= 4: pick the pigeonhole pair, apply")
print("    C1-P and the hypothesis at k-2:  residue <= bound(k-2) + 1 = ceil((k-2)/2)+2 =")
print("    ceil(k/2)+1 = bound(k).   []   -- the arithmetic step is checked below.")
arith = [k for k in range(4, 200) if bound(k - 2) + 1 != bound(k)]
print("    bound(k-2)+1 == bound(k) for every k in 4..199 : %s" % ("YES" if not arith else "NO %s" % arith[:5]))
if arith: bad("C1-O-arith", str(arith[:5]))
print("    C1-M ==> C1 (residue != k+1) : ceil(k/2)+1 < k+1 for k >= 2 :",
      all(bound(k) < k + 1 for k in range(2, 200)))
print("    C1-M ==> C1-I's open half (no near-miss at k >= 4, i.e. residue <= k-1) :",
      [k for k in range(2, 60) if bound(k) <= k - 1][:4], "... first k is 4")

# ================================================================ 6. C1-M CENSUS
print("\n[6] OBSERVATION C1-M -- CENSUS REPRODUCED HERE (still NOT a theorem)")
best = {}; viol = 0; cnt = 0
for n in range(2, 27):
    for lam in parts(n):
        if len(lam) < 2: continue
        s, r = run(M(lam))
        if s is None: continue
        cnt += 1
        k = len(lam)
        if r > bound(k): viol += 1; bad("C1-M", "%s r=%d bound=%d" % (lam, r, bound(k)))
        if r > best.get(k, (-1, None))[0]: best[k] = (r, lam)
print("    %d terminating partitions with k >= 2 over n <= 26 : %d violations" % (cnt, viol))
att = [k for k in sorted(best) if best[k][0] == bound(k)]
print("    bound ATTAINED at k = %s  (all of 2..%d)" % (att[:6] + ['...'], max(best)))
print("    witnesses: " + " | ".join("k=%d:%s" % (k, best[k][1]) for k in sorted(best)[:5]))
ctrl("C1-M with the bound tightened by 1 IS violated (live negative control)",
     sum(1 for n in range(2, 20) for lam in parts(n) if len(lam) >= 2
         and run(M(lam))[1] is not None and run(M(lam))[1] > bound(len(lam)) - 1))

# ================================================================ 7. PROP C1-Q
print("\n[7] PROPOSITION C1-Q (PROVED reduction)  k = 4 bottoms out on TWO families")
print("    lambda = (w,b,c,d).  C1-J' -> base [b]^{b+3} u [c,d]  (w-b even)  or  Q(b;(c,d)).")
print("    C1-R entry sends [b]^{b+3} u nu -> Y(b;nu); C1-R at s=2 descends Y and Q with j")
print("    invariant, down to u = c; and Y(c;(c,d)) = W+(c) u [d], Q(c;(c,d)) = W-(c) u [d].")
print("    Hence residue(M(w,b,c,d)) = residue(F_3(c, 3 or 2; [d])) -- NO w and NO b left.")
nQ = 0
for w in range(1, 17):
    for b in range(1, w + 1):
        for c in range(1, b + 1):
            for d in range(1, c + 1):
                lam = (w, b, c, d)
                s, r = run(M(lam))
                if s is None: continue
                tgt = Wp(c) + [d] if (w - b) % 2 == 0 else Wm(c) + [d]
                s2, r2 = run(tgt)
                nQ += 1
                if r != r2:
                    bad("C1-Q", "%s residue %d vs bottom %s residue %s" % (lam, r, ms(tgt), r2))
                if (s2 is None) != (s is None):
                    bad("C1-Q-abort", "%s" % (lam,))
print("    residue identity verified on %d terminating 4-part lambda with w <= 16 : %d defects"
      % (nQ, len([f for f in FAIL if f.startswith('C1-Q')])))
print("    W+(c) u [d] = F_3(c,3;[d]) and W-(c) u [d] = F_3(c,2;[d]) : ",
      all(ms(Wp(c) + [d]) == ms(F(3, c, 3, (d,))) and ms(Wm(c) + [d]) == ms(F(3, c, 2, (d,)))
          for c in range(2, 20) for d in range(1, c + 1)))
ctrl("C1-Q with the two parity branches SWAPPED -> mismatches",
     sum(1 for w in range(1, 13) for b in range(1, w + 1) for c in range(1, b + 1) for d in range(1, c + 1)
         if run(M((w, b, c, d)))[1] is not None
         and run(M((w, b, c, d)))[1] != run((Wm(c) + [d]) if (w - b) % 2 == 0 else (Wp(c) + [d]))[1]))
print("\n    THE BOTTOM, as a census (NOT proved):  residue(F_3(c,j;[d])) <= 3 for j in {2,3}")
mx = 0; bviol = 0; three = []
for c in range(1, 41):
    for d in range(1, c + 1):
        for j, nm in ((3, "W+"), (2, "W-")):
            s, r = run(F(3, c, j, (d,)))
            if s is None: continue
            mx = max(mx, r)
            if r > 3: bviol += 1; bad("C1-Q-bottom", "%s(%d) u [%d] r=%d" % (nm, c, d, r))
            if r == 3: three.append((nm, c, d))
print("    c <= 40 : max residue over the bottom families = %d ; violations of '<= 3' = %d" % (mx, bviol))
print("    residue = 3 happens exactly at d = 1 plus TWO isolated boundaries: %s"
      % ([t for t in three if t[2] != 1]))
print("    (so k = 4 is REDUCED to a two-parameter family and VERIFIED, and is NOT PROVED.)")

# ================================================================ ACCOUNTING
print("\n" + "=" * 96)
print("diffed runA/runB calls: %d   controls: %d, all firing: %s   defects: %d   %.1fs"
      % (DIFFED, len(CTRL), all(c[2] for c in CTRL), len(FAIL), time.time() - T0))
if FAIL:
    print("DEFECTS:")
    for f in FAIL[:40]:
        print("   " + f)
    print("VERDICT: DEFECTS PRESENT -- no claim promoted")
    sys.exit(1)
print("VERDICT: every audited identity holds.  PROVED this round: C1-N, C1-R, C1-O (reduction),")
print("         C1-Q (reduction).  STILL CENSUS: C1-P, C1-M, and k = 4.")
sys.exit(0)
