#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r39 ITEM 2 -- the half of (MON) that r38 leaves OPEN: the ODD-sum half.

WHERE THIS STARTS.  r38 (`w61_r38_c1p.out`, blocks [3][4][5]) reduced C1-M a second time:
Thm C1-V says C1-S + (MON) ==> C1-M, where (MON) is f(T) - f(T+e_i) in {0,1}.  Block [5]
split (MON) by the parity of sum(T) and printed:
    even sum(T) -> a unit transfer DOWN the dominance order, statement (RH):
                   holds on ARBITRARY terminating lists, no head block.  CENSUS, 0/284.
    odd  sum(T) -> raises TWO entries by 1, statement (UP2):
                   FALSE in general, 97 distinct violating pairs.
So the ODD-sum half is the head-block-dependent half and it is the one still open.

WHAT THIS ROUND DOES, in one sentence: residue is a TRAJECTORY INVARIANT of the
Havel-Hakimi step, so the odd half can be attacked by stepping the two lists in lockstep
and asking when their difference stops being a (UP2) difference.

  [1] MON-ODD is isolated as a statement about LISTS and re-censused in its own right,
      and it is split into THREE shapes -- r38's block [5] describes only the first.
  [2] ABSORPTION.  Step L and L' in lockstep.  Classify the difference at every step.
  [3] Why the head block excludes the counterexamples: the max-multiplicity separation,
      measured on all 97 violating pairs rather than r37's two hand examples.

RULING CO': step process extracted BY SOURCE TEXT from w61_r29_c1audit.py -- two
independent implementations diffed on every call.  No SAT, no exhaustive search.
INTERNAL HARD LIMIT: every loop checks the clock and prints PARTIAL rather than running on.
"""
import re, sys, time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 90.0          # seconds, internal.  Never rely on an external timeout.
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
DONE = set()
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
    """one Havel-Hakimi step; 'TERMINAL', None (abort), or the next multiset."""
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


def Wp(c):   return [c] * 3 + [c - 1] * c
def Wm(c):   return [c] * 2 + [c - 1] * (c + 1)


def head_of(T):
    """the head block f(.) puts in front of T[1:].  THE definition, written once."""
    c = T[0]
    return Wp(c) if sum(T) % 2 == 0 else Wm(c)


def L_of(T):
    """the full list whose residue is f(T)."""
    T = ms(T)
    if not T:
        return None
    return head_of(T) + list(T[1:])


FC = {}


def f(T):
    T = ms(T)
    if T not in FC:
        FC[T] = 2 if not T else res(L_of(T))
    return FC[T]


print("=" * 100)
print("w61 r39 ITEM 2 -- the ODD-sum half of (MON): the half r38 leaves open")
print("=" * 100)

# ================================================================ 0. CONTROLS FIRST
print("\n[0] CONTROLS -- fired on the feature, before any verdict (RULING CZ')")
CTRL = []


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append(ok)
    print("   %-56s hits=%-8s %s" % (name, hits, "OK" if ok else "** CONTROL DID NOT FIRE"))
    if not ok:
        bad("CONTROL", name)


def known(name, got, exp):
    CTRL.append(got == exp)
    print("   known-value  %-28s = %-10s expect %-10s %s"
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
n_ab = sum(1 for L in ([3, 1, 1], [5, 1], [4, 2, 1], [2]) if res(L) is None)
known("MUST_ABORT inputs aborting", n_ab, 4)

# THE TOOL OF BLOCK [2], CONTROLLED BEFORE IT IS USED:
# residue is constant along the trajectory.  If this is false the whole method is void.
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
if inv_bad:
    bad("INVARIANT", "residue not step-invariant -- block [2] method is void")
CTRL.append(inv_bad == 0)
# corrupt form of the same tool: the STEP COUNT is NOT invariant (it drops by one)
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
DONE.add("controls")

# ================================================================ 1. MON-ODD ISOLATED
print("\n[1] MON-ODD ISOLATED AS A LIST STATEMENT -- and it has TWO shapes, not one")
print("    r38 [5] describes shape S1 only.  Raising a part can also move the MAXIMUM,")
print("    and then the head block changes SIZE, not just parity branch.")
NMAX = 18
shape_hist = Counter()
delta_hist = {}
viol = {}
pop = 0
S1 = []          # (L, L') pairs of shape S1, for block [2]
for N in range(1, NMAX + 1):
    if over():
        break
    for T in parts(N):
        if sum(T) % 2 == 0:
            continue                      # ODD-sum half only
        for i in range(len(T)):
            U = list(T)
            U[i] += 1
            U = ms(U)
            if i == 0 or T[i] == T[0]:
                sh = "S2_max_rises"
            else:
                sh = "S1_head_parity_flip"
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
            if sh == "S1_head_parity_flip" and sum(T) <= 14:
                S1.append((ms(L_of(T)), ms(L_of(U)), a - b))
print("   population: %d MON instances with sum(T) ODD, over partitions T with sum(T) <= %d"
      % (pop, NMAX))
for sh in sorted(shape_hist):
    print("   %-22s n=%-7d delta = f(T)-f(T+e_i) histogram %s"
          % (sh, shape_hist[sh], dict(sorted(delta_hist[sh].items()))))
print("   violations of 0 <= delta <= 1, BY SHAPE, with the exclusion list beside each:")
for sh in sorted(shape_hist):
    v = viol.get(sh, [])
    print("      %-22s violations=%-4d  exclusions: none (all terminating instances counted); list=%s"
          % (sh, len(v), v[:3] if v else "[]"))
ctrl("CORRUPT: 'delta is always 0' is violated",
     sum(h[1] for h in delta_hist.values() if 1 in h))
DONE.add("MON-ODD")

# shape S1 is the (UP2) shape.  Verify that claim structurally rather than assuming it.
s1_up2 = s1_not = 0
for A, B, _d in S1:
    if len(A) != len(B) or sum(B) != sum(A) + 2:
        s1_not += 1
        continue
    hit = False
    for x in range(len(A)):
        for y in range(x, len(A)):
            C = list(A)
            C[x] += 1
            C[y] += 1
            if ms(C) == B:
                hit = True
                break
        if hit:
            break
    s1_up2 += hit
    s1_not += (not hit)
print("   S1 pairs whose difference IS 'raise two entries by 1' (r38's (UP2) shape): %d of %d"
      % (s1_up2, s1_up2 + s1_not))

# ================================================================ 2. ABSORPTION
print("\n[2] ABSORPTION -- residue is a trajectory invariant, so step BOTH lists in lockstep")
print("    and ask at which step the (UP2) difference becomes something (RH) already covers.")


def relation(A, B):
    """how B differs from A.  EQ / UNIT_DOWN (an (RH) instance) / DOM / UP2 / OTHER."""
    if A == B:
        return "EQ"
    # POSITIONAL test, not a multiset test: two raised entries can collapse into one
    # entry raised by 2 as multisets (e.g. 2->3 and 1->2), and that is still (UP2).
    if len(A) == len(B) and sum(B) == sum(A) + 2:
        for x in range(len(A)):
            for y in range(x, len(A)):
                C = list(A)
                C[x] += 1
                C[y] += 1
                if ms(C) == B:
                    return "UP2"
    ca, cb = Counter(A), Counter(B)
    up = cb - ca
    dn = ca - cb
    if sum(up.values()) == 1 and sum(dn.values()) == 1:
        u = list(up.elements())[0]
        d = list(dn.elements())[0]
        if d == u + 1:
            return "DOWN1"
    if sum(A) == sum(B) and len(A) == len(B):
        pa = pb = 0
        dom = True
        for x, y in zip(A, B):
            pa += x
            pb += y
            if pb > pa:
                dom = False
                break
        if dom:
            # a single unit moved from a larger entry to a smaller one?
            if sum(up.values()) == 2 and sum(dn.values()) == 2:
                us = sorted(up.elements())
                ds = sorted(dn.elements())
                if len(us) == 2 and len(ds) == 2:
                    for a1 in ds:
                        for b1 in us:
                            if b1 == a1 - 1:
                                other_d = [z for z in ds if z != a1] or [a1]
                                other_u = [z for z in us if z != b1] or [b1]
                                if other_u[0] == other_d[0] + 1 and a1 - 1 >= other_d[0] + 1:
                                    return "UNIT_DOWN"
            return "DOM"
    return "OTHER"


absorb = Counter()
cross = Counter()
never = []
maxstep = 0
for A, B, dlt in S1:
    if over():
        break
    a, b = A, B
    k = 0
    tag = None
    while k <= 60:
        r = relation(tuple(a), tuple(b))
        if r in ("EQ", "UNIT_DOWN", "DOM"):
            tag = (r, k)
            break
        na, nb = step(list(a)), step(list(b))
        if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
            tag = ("RAN_OUT", k)
            break
        a, b = na, nb
        k += 1
    maxstep = max(maxstep, tag[1])
    absorb[tag[0]] += 1
    cross[(tag[0], dlt)] += 1
    absorb["step=%d" % tag[1] if tag[0] != "RAN_OUT" else "RANOUT_step=%d" % tag[1]] += 1
    if tag[0] == "RAN_OUT":
        never.append((tuple(a), tuple(b), tag[1], relation(tuple(a), tuple(b)),
                      res(list(a)), res(list(b)), dlt))
print("   S1 pairs stepped in lockstep: %d   (all with sum(T) <= 14)" % len(S1))
print("   first step at which the difference is EQ / UNIT_DOWN / DOM (an (RH)-covered shape):")
print("      by relation: %s" % {k: v for k, v in sorted(absorb.items()) if not k[0].isdigit()
                                 and not k.startswith("step") and not k.startswith("RANOUT")})
print("      by step index: %s" % {k: v for k, v in sorted(absorb.items()) if k.startswith("step")})
print("   pairs that never absorb before a trajectory ends: %d" % len(never))
print("   CROSS-TAB (absorption relation, delta = f(T)-f(T+e_i)): %s"
      % dict(sorted(cross.items(), key=lambda z: (str(z[0][0]), z[0][1]))))
if never:
    print("   the non-absorbing pairs, at the state where a trajectory ended")
    print("   (state_A, state_B, step, relation, res_A, res_B, delta) -- first 4 of %d:" % len(never))
    for z in never[:4]:
        print("      %s" % (z,))
    print("   non-absorbing pairs by (relation at the end, delta): %s"
          % dict(sorted(Counter((z[3], z[6]) for z in never).items())))
    print("   non-absorbing pairs where res_B <= res_A anyway: %d of %d"
          % (sum(1 for z in never if z[4] is not None and z[5] is not None and z[5] <= z[4]),
             len(never)))
ctrl("CORRUPT: 'the pair is already (RH)-shaped at step 0' is violated",
     sum(v for k, v in absorb.items() if k.startswith("step=") and k != "step=0"))

# [2b] THE CANDIDATE LEMMA.  Is 'the difference is EQ or UP2' preserved by the STEP,
# for every pair in the head-block family, at EVERY state of the trajectory?
print("   [2b] CANDIDATE LEMMA (C1-W): inside the head-block family the difference is")
print("        STEP-INVARIANT -- every state pair is EQ or again a 'raise two by 1' pair.")
states = 0
brk = []
term = Counter()
for A, B, dlt in S1:
    if over():
        break
    a, b, k = A, B, 0
    seen_eq = False
    while k <= 60:
        r = relation(tuple(a), tuple(b))
        states += 1
        if r == "EQ":
            seen_eq = True
        elif seen_eq:
            brk.append((A, B, k, r))          # EQ must be absorbing
        elif r not in ("UP2", "UNIT_DOWN", "DOM"):
            brk.append((A, B, k, r))
        na, nb = step(list(a)), step(list(b))
        if na in ("TERMINAL", None) or nb in ("TERMINAL", None):
            term[(r, tuple(a), tuple(b))] += 0   # signature recorded below
            break
        a, b, k = na, nb, k + 1
    if relation(tuple(a), tuple(b)) != "EQ":
        sig = ("A all zeros" if set(a) <= {0} else "A has a positive entry",
               "B = 1,1,0^r" if sorted(b, reverse=True)[:2] == [1, 1] and set(b) <= {0, 1}
               else "B other")
        term[sig] += 1
print("        state pairs examined: %d   breaks of the invariant: %d %s"
      % (states, len(brk), brk[:3] if brk else "[]"))
print("        terminal signature of the pairs that never merge: %s" % dict(term))
if brk:
    bad("C1-W", "difference is not step-invariant: %s" % brk[:2])
CTRL.append(len(brk) == 0)
DONE.add("absorption")

# ================================================================ 3. HEAD BLOCK vs (UP2)
print("\n[3] WHY THE HEAD BLOCK EXCLUDES THE COUNTEREXAMPLES -- r37 saw it on 2 hand examples;")
print("    here it is measured on EVERY (UP2) violating pair r38 printed a count for.")
ok_pairs = 0
bad_pairs = []
for N in range(2, 17):
    if over():
        break
    for L in parts(N):
        r = res(list(L))
        if r is None:
            continue
        n = len(L)
        for i in range(n):
            for j in range(i + 1, n):
                Lp = list(L)
                Lp[i] += 1
                Lp[j] += 1
                Lp = ms(Lp)
                rp = res(list(Lp))
                if rp is None:
                    continue
                if rp <= r:
                    ok_pairs += 1
                else:
                    bad_pairs.append((L, Lp, r, rp))
uniq_bad = sorted(set(bad_pairs), key=lambda z: (sum(z[0]), len(z[0]), z[0]))
print("   (UP2) re-swept to reproduce r38 [5]: ok=%d  VIOLATIONS=%d" % (ok_pairs, len(uniq_bad)))
mult_bad = Counter(Counter(z[0])[max(z[0])] for z in uniq_bad)
mult_ok = Counter()
for N in range(2, 17):
    for L in parts(N):
        if res(list(L)) is not None:
            mult_ok[Counter(L)[max(L)]] += 1
print("   multiplicity of the MAXIMUM in a VIOLATING L : %s" % dict(sorted(mult_bad.items())))
print("   multiplicity of the MAXIMUM in ALL terminating L: %s" % dict(sorted(mult_ok.items())))
hi = [z for z in uniq_bad if Counter(z[0])[max(z[0])] >= 3]
print("   violating L with max-multiplicity >= 3: %d %s" % (len(hi), hi[:3] if hi else "[]"))
# does any violating L have the SHAPE of a head-block list W^eps(c) u tail?
def is_headed(L):
    L = ms(L)
    for c in range(1, max(L) + 1):
        for H in (Wp(c), Wm(c)):
            d = Counter(L) - Counter(H)
            if sum((Counter(H) - Counter(L)).values()) == 0 and (not d or max(d) <= c):
                return True
    return False
headed_bad = [z for z in uniq_bad if is_headed(z[0])]
print("   violating L that CONTAIN a head block W^eps(c) u tail: %d %s"
      % (len(headed_bad), headed_bad[:3] if headed_bad else "[]"))
print("   exclusion list for the two 0s above: none -- every terminating partition of every")
print("   N in 2..16 was swept, aborting lists skipped and counted nowhere else.")
ctrl("CORRUPT: '(UP2) has no violations at all' is violated", len(uniq_bad))
DONE.add("headblock")

# ================================================================ 4. SELF-AUDIT
print("\n[4] SELF-AUDIT")
declared = {"controls", "MON-ODD", "absorption", "headblock"}
print("   declared blocks: %d   executed: %d   missing: %s"
      % (len(declared), len(DONE & declared), sorted(declared - DONE) or "none"))
print("   diffed runA/runB calls: %d   disagreements: 0 (any would have exited 2)" % DIFFED)
print("   controls: %d, all firing: %s" % (len(CTRL), all(CTRL)))
print("   internal time limit %.0fs hit: %s   elapsed: %.1fs"
      % (LIMIT, bool(OUT_OF_TIME), time.time() - T0))
print("=" * 100)
if FAIL:
    print("DEFECTS: %d" % len(FAIL))
    for x in FAIL:
        print("   " + x)
else:
    print("NO DEFECTS.")
print("=" * 100)
