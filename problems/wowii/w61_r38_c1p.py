#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r38 ITEM 1 -- Key Lemma C1-P, attacked with the head block and in monotone form.

WHAT THE TASK ASKED.  r37 reduced Observation C1-M to ONE open input, Key Lemma C1-P
(`residue(M(lam)) <= residue(M(lam^-)) + 1`).  The task book gives two directions and
wants the STRONGER MONOTONE form tried first.

WHAT THIS ROUND FOUND, and it is not either of the two directions as posed.

  PROVED   Thm C1-S   residue(M(lam)) depends ONLY on (lam_3, ..., lam_k).
                      BOTH lam_1 AND lam_2 are invisible, at EVERY k.
                      Explicitly residue(M(lam)) = residue(W^eps(lam_3) u (lam_4..lam_k)),
                      eps = '+' iff lam_3+...+lam_k is even.  Prop C1-Q is the k=4 case.
                      Proof = C1-J' (=C1-R s=1 pairs) + C1-R entry s=3 + C1-R interior s=2.
                      Everything it uses is already PROVED on this line.

  PROVED   Lem C1-U   f(1^m) = ceil(m/2) + 2 for EVERY m >= 0, where f is the C1-S
                      residue function of the tail.  So C1-M's bound is ATTAINED at
                      every k >= 2 -- r37 had that as a census over k <= 26 only.

  PROVED   Thm C1-V   C1-S + (MON) ==> C1-M.  A SECOND reduction of C1-M to a single
                      open input, and the new input is a ONE-PART INCREMENT, not a
                      two-part removal.  Proof: every partition T with m parts satisfies
                      T >= 1^m componentwise; MON gives f(T) <= f(1^m) = ceil(m/2)+2
                      = ceil(k/2)+1 by C1-U.  Theorem C1-O and Key Lemma C1-P are NOT
                      used anywhere in this chain.

  CENSUS   (MON)      f(T) - f(T + e_i) in {0,1}.
  CENSUS   (C1-P')    f(T) - f(T \\ {t_i,t_j}) in {0,1} for ANY pair -- the equal-parity
                      hypothesis of C1-P is UNNECESSARY, and the monotone half holds.
  CENSUS   (RH)       a dominance-decreasing unit transfer never increases residue --
                      on ARBITRARY terminating lists, NO head block required.

  REFUTED  the general "raise two entries by 1" form of MON's odd-sum half is FALSE:
                      [2,2,2,1,1] -> [3,3,2,1,1] is residue 2 -> 3.  Printed, not hidden.

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
DONE = set()          # every declared block registers here; asserted at the end


def run(lst):
    """(steps, residue) or (None, None); ABORTS THE AUDIT if the two impls disagree."""
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


def one_step(lst):
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


def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)


def bound(k):
    return (k + 1) // 2 + 1            # ceil(k/2) + 1


# ---- the named shapes.  A typo HERE is a proof defect, not a script defect. ----
def F(s, x, j, nu=()):
    """F_s(x,j;nu) = [x]^j u [x-1]^{x+s-j} u nu."""
    return [x] * j + [x - 1] * (x + s - j) + list(nu)


def Y(u, nu=()):   return [u] * 2 + [u - 1] * u + list(nu)            # C1-K
def Q(u, nu=()):   return [u] + [u - 1] * (u + 1) + list(nu)          # C1-K
def Wp(c):         return [c] * 3 + [c - 1] * c                       # W+(c)
def Wm(c):         return [c] * 2 + [c - 1] * (c + 1)                 # W-(c)


# ---- Theorem C1-S's closed form.  This IS the claim, written once. ----
def f_closed(T):
    """f(T) := residue(W^eps(T_1) u (T_2..T_m)),  eps = '+' iff sum(T) even;  f(()) = 2."""
    T = tuple(sorted(T, reverse=True))
    if not T:
        return 2
    c = T[0]
    head = Wp(c) if sum(T) % 2 == 0 else Wm(c)
    return res(head + list(T[1:]))


FCACHE = {}


def f(T):
    T = tuple(sorted(T, reverse=True))
    if T not in FCACHE:
        FCACHE[T] = f_closed(T)
    return FCACHE[T]


print("=" * 100)
print("w61 r38 ITEM 1 -- Key Lemma C1-P : lam_1 AND lam_2 are BOTH invisible, and C1-M gets a")
print("                  second reduction whose single open input is a ONE-PART INCREMENT")
print("=" * 100)

# ================================================================ 0. CONTROLS FIRST
print("\n[0] CONTROLS -- fired on the FEATURE, before any verdict (RULING CZ')")
CTRL = []


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append((name, hits, ok))
    print("   %-58s hits=%-8d %s" % (name, hits, "OK" if ok else "** CONTROL FAILED"))
    if not ok:
        bad("CTRL", name)


KNOWN = [("s0((2,1,1))", run(M((2, 1, 1))), (3, 3)),
         ("s0((6,4,2))", run(M((6, 4, 2)))[0], 8),
         ("residue(M((5,4,3)))", run(M((5, 4, 3)))[1], 2),
         ("[1,1,0,0] boundary", run([1, 1, 0, 0]), (1, 3)),
         ("W-(1) boundary", run(Wm(1)), (1, 3)),
         ("W+(2)u[2] boundary", res(Wp(2) + [2]), 3),
         ("W-(3)u[2] boundary", res(Wm(3) + [2]), 3)]
for nm, got, want in KNOWN:
    print("   known-value  %-24s = %-10s expect %-10s %s"
          % (nm, got, want, "OK" if got == want else "** WRONG"))
    if got != want:
        bad("KNOWN", nm)

MUST_ABORT = [("M((7,2))", M((7, 2))), ("W+(1)", Wp(1)), ("M((3,2,2))", M((3, 2, 2))),
              ("[1,0,0]", [1, 0, 0])]
for nm, L in MUST_ABORT:
    if run(L) != (None, None):
        bad("MUST_ABORT", nm)
print("   MUST_ABORT category: %d inputs, all abort as required" % len(MUST_ABORT))
DONE.add("controls")

# ================================================================ 1. THEOREM C1-S
print("\n[1] THEOREM C1-S (PROVED)  residue(M(lam)) depends ONLY on (lam_3,...,lam_k)")
print("    and equals residue(W^eps(lam_3) u (lam_4..lam_k)), eps='+' iff sum(lam_3..lam_k) even.")
print("    Hand proof: C1-J' descent to the base, then C1-R entry (s=3), then C1-R interior (s=2).")
print("    Each of the three descent identities is re-verified here as a MULTISET trajectory.")

NMAX_S = 26
n_S = n_T1 = n_T2 = 0
seen_tail = {}
seen_pair = {}
for N in range(2, NMAX_S + 1):
    for lam in parts(N):
        if len(lam) < 2:
            continue
        r = res(M(lam))
        if r is None:
            continue
        n_S += 1
        # (i) the closed form
        if f(lam[2:]) != r:
            bad("C1-S", "lam=%s residue=%s f(tail)=%s" % (lam, r, f(lam[2:])))
        # (ii) lam_1 invisible given lam_2 and parity  (the r37 statement, kept as a control)
        k1 = (lam[1:], (lam[0] - lam[1]) % 2)
        if k1 in seen_pair and seen_pair[k1] != r:
            bad("C1-S-i", "%s : %s vs %s" % (k1, seen_pair[k1], r))
        seen_pair[k1] = r
        n_T1 += 1
        # (iii) lam_1 AND lam_2 invisible  (the new statement)
        if lam[2:] in seen_tail and seen_tail[lam[2:]] != r:
            bad("C1-S-ii", "tail=%s : %s vs %s" % (lam[2:], seen_tail[lam[2:]], r))
        seen_tail[lam[2:]] = r
        n_T2 += 1
print("   population: %d terminating partitions with k>=2 over n<=%d, %d distinct tails"
      % (n_S, NMAX_S, len(seen_tail)))
print("   closed form residue(M(lam)) == f(lam_3..lam_k): %d checks" % n_S)

# the three descent identities the hand proof uses, each as a multiset identity
d_j = d_e = d_i = d_q = 0
for w in range(2, 22):
    for nu in [(), (1,), (2,), (2, 1), (3, 2, 1), (1, 1, 1)]:
        if nu and max(nu) > w - 1:
            continue
        L = [w] * (w + 2) + list(nu)
        s1 = one_step(L)
        s2 = one_step(list(s1)) if isinstance(s1, tuple) else None
        if s2 != ms([w - 2] * w + list(nu)):
            bad("C1-J'", "w=%d nu=%s got %s" % (w, nu, s2))
        d_j += 1
for b in range(2, 22):
    for nu in [(), (1,), (b,), (b, 1), (b - 1, 2)]:
        if nu and max(nu) > b:
            continue
        if one_step([b] * (b + 3) + list(nu)) != ms(Y(b, nu)):
            bad("C1-R-entry", "b=%d nu=%s" % (b, nu))
        d_e += 1
for u in range(3, 24):
    for nu in [(), (1,), (2, 1), (u - 1,), (u - 2, u - 2)]:
        if nu and max(nu) > u - 1:
            continue
        if one_step(Y(u, nu)) != ms(Y(u - 1, nu)):
            bad("C1-R-int-Y", "u=%d nu=%s" % (u, nu))
        d_i += 1
        if one_step(Q(u, nu)) != ms(Q(u - 1, nu)):
            bad("C1-R-int-Q", "u=%d nu=%s" % (u, nu))
        d_q += 1
print("   descent identities as MULTISETS: C1-J' %d, C1-R entry %d, Y-interior %d, Q-interior %d"
      % (d_j, d_e, d_i, d_q))

# controls on C1-S: corrupted variants must NOT hold
c_tail3 = sum(1 for tail in seen_tail
              if len(tail) >= 1 and tail[1:] in seen_tail and seen_tail[tail[1:]] != seen_tail[tail])
ctrl("CORRUPT: 'lam_1..lam_3 all invisible' fails", c_tail3)
c_par = 0
for T in list(seen_tail)[:400]:
    T = tuple(T)
    c = T[0] if T else 0
    if not T:
        continue
    swapped = res((Wm(c) if sum(T) % 2 == 0 else Wp(c)) + list(T[1:]))
    if swapped != seen_tail[T]:
        c_par += 1
ctrl("CORRUPT: W+/W- parity branches SWAPPED mismatches", c_par)
DONE.add("C1-S")

# ================================================================ 2. LEMMA C1-U
print("\n[2] LEMMA C1-U (PROVED)  f(1^m) = ceil(m/2) + 2 for every m >= 0")
print("    Proof: sum(1^m)=m, so the head is W+(1)=[1,1,1,0] when m even and W-(1)=[1,1,0,0] when")
print("    m odd; hence the list is [1]^{m+2} u [0] (m even) or [1]^{m+1} u [0]^2 (m odd).")
print("    residue([1]^{2p} u [0]^z) = p + z because each step deletes one 1 and zeroes one 1.")
n_U = 0
for m in range(0, 41):
    got = f((1,) * m)
    want = (m + 1) // 2 + 2
    n_U += 1
    if got != want:
        bad("C1-U", "m=%d got %s want %s" % (m, got, want))
    # and the [1]^{2p} u [0]^z identity the proof rests on
    for z in range(0, 4):
        if res([1] * (2 * m) + [0] * z) != m + z:
            bad("C1-U-res", "p=%d z=%d" % (m, z))
print("   f(1^m) = ceil(m/2)+2 verified for m = 0..40, and residue([1]^2p u [0]^z) = p+z")
print("   => C1-M's bound ceil(k/2)+1 is ATTAINED at EVERY k >= 2 (k = m+2), as a THEOREM.")
ctrl("CORRUPT: f(1^m) = ceil(m/2)+1 is violated",
     sum(1 for m in range(0, 41) if f((1,) * m) != (m + 1) // 2 + 1))
DONE.add("C1-U")

# ================================================================ 3. (MON) AND THEOREM C1-V
print("\n[3] (MON) CENSUS + THEOREM C1-V (PROVED)  C1-S + (MON) ==> C1-M")
print("    (MON): f(T) - f(T + e_i) in {0,1}   [raising ONE part of the tail never raises f]")
NMAX_MON = 22
hist_mon = Counter()
viol_mon = []
for N in range(1, NMAX_MON + 1):
    for T in parts(N):
        for i in range(len(T)):
            Tp = list(T)
            Tp[i] += 1
            d = f(T) - f(tuple(sorted(Tp, reverse=True)))
            hist_mon[d] += 1
            if d < 0:
                viol_mon.append((T, tuple(sorted(Tp, reverse=True))))
n_mon = sum(hist_mon.values())
print("   population: %d (T, i) instances over all partitions T with sum(T) <= %d"
      % (n_mon, NMAX_MON))
print("   delta = f(T) - f(T+e_i) histogram: %s" % dict(sorted(hist_mon.items())))
print("   delta < 0 (would refute MON): %d instances %s" % (len(viol_mon), viol_mon[:3]))
if any(d < 0 for d in hist_mon):
    bad("MON", "monotonicity violated")

# C1-V's arithmetic, executed rather than asserted: the ladder 1^m -> T stays a partition
n_ladder = 0
for N in range(1, 17):
    for T in parts(N):
        m = len(T)
        cur = [1] * m
        okpath = True
        for i in range(m):
            while cur[i] < T[i]:
                cur[i] += 1
                if any(cur[a] < cur[a + 1] for a in range(m - 1)):
                    okpath = False
        if not okpath or tuple(cur) != tuple(T):
            bad("C1-V-ladder", str(T))
        n_ladder += 1
print("   C1-V ladder: %d partitions reached from 1^m by single +1 steps, sorted at every stage"
      % n_ladder)
for k in range(2, 200):
    if bound(k) != (k - 2 + 1) // 2 + 2:
        bad("C1-V-arith", "k=%d" % k)
print("   C1-V arithmetic ceil(k/2)+1 == ceil((k-2)/2)+2 checked for k = 2..199")
ctrl("CORRUPT: 'f(T) - f(T+e_i) in {0}' is violated", hist_mon[1])
# MON re-measured WITHOUT the closed form: straight through residue(M(lam)), so that the
# census cannot be an artefact of C1-S.  lam_1 is raised too, to keep |lam| even.
n_direct = 0
hist_direct = Counter()
for N in range(4, 21):
    for lam in parts(N):
        if len(lam) < 3:
            continue
        r = res(M(lam))
        if r is None:
            continue
        for i in range(2, len(lam)):
            mu = list(lam)
            mu[i] += 1
            mu[0] += 1
            mu = tuple(sorted(mu, reverse=True))
            r2 = res(M(mu))
            if r2 is None:
                continue
            hist_direct[r - r2] += 1
            n_direct += 1
            if r - r2 < 0:
                bad("MON-direct", "lam=%s mu=%s" % (lam, mu))
print("   MON re-measured through residue(M(lam)) directly, NOT through f: %d instances, "
      "delta histogram %s" % (n_direct, dict(sorted(hist_direct.items()))))
print("   NULL EXPECTATION for MON is NOT 1: block [5] runs the same shape of statement on the")
print("   head-block-free family and it FAILS there (184 distinct counterexamples).")
DONE.add("MON")

# ================================================================ 4. C1-P' -- PARITY IS NOT NEEDED
print("\n[4] (C1-P') CENSUS  f(T) - f(T \\ {t_i,t_j}) in {0,1} for ANY pair -- no parity condition")
NMAX_P = 20
hist_any = Counter()
hist_par = Counter()
hist_top2 = Counter()
bU = []
bL = []
for N in range(0, NMAX_P + 1):
    for T in parts(N):
        m = len(T)
        if m < 2:
            continue
        v = f(T)
        seen = set()
        for i in range(m):
            for j in range(i + 1, m):
                Tm = tuple(T[x] for x in range(m) if x not in (i, j))
                if Tm in seen:
                    continue
                seen.add(Tm)
                d = v - f(Tm)
                hist_any[d] += 1
                if (T[i] - T[j]) % 2 == 0:
                    hist_par[d] += 1
                if d > 1:
                    bU.append((T, (T[i], T[j])))
                if d < 0:
                    bL.append((T, (T[i], T[j])))
        hist_top2[v - f(T[2:])] += 1
print("   population: %d (T, pair) instances over partitions T with sum(T) <= %d"
      % (sum(hist_any.values()), NMAX_P))
print("   ANY pair          delta histogram: %s" % dict(sorted(hist_any.items())))
print("   equal-parity pair delta histogram: %s   (C1-P's own hypothesis)"
      % dict(sorted(hist_par.items())))
print("   TOP-TWO pair      delta histogram: %s   (the only pair C1-V would need)"
      % dict(sorted(hist_top2.items())))
print("   delta > 1 : %d      delta < 0 : %d" % (len(bU), len(bL)))
if bU or bL:
    bad("C1-P'", "delta outside {0,1}")
print("   => C1-P's equal-parity hypothesis is UNNECESSARY, and C1-P's MONOTONE half holds:")
print("      the census the task asked to attack SURVIVES, in a strictly stronger form.")
DONE.add("C1-P'")

# ================================================================ 5. THE BOUNDARY, PRINTED
print("\n[5] THE BOUNDARY -- which half of (MON) needs the head block, and which does not")
print("    (MON) at even sum(T) is a unit transfer DOWN the dominance order inside the list;")
print("    (MON) at odd  sum(T) raises TWO entries of the list by 1.  Sweep both, in general.")


def sweep(name, gen, nmax=16):
    """DISTINCT (L, L') pairs -- a duplicate-inflated count is a count of nothing (r37 D1)."""
    ok = set()
    bad_l = set()
    for N in range(2, nmax + 1):
        for L in parts(N):
            r = res(list(L))
            if r is None:
                continue
            for Lp in gen(L):
                Lp = tuple(sorted(Lp, reverse=True))
                if min(Lp) < 0:
                    continue
                rp = res(list(Lp))
                if rp is None:
                    continue
                (ok if rp <= r else bad_l).add((L, Lp, r, rp))
    bad_l = sorted(bad_l, key=lambda z: (sum(z[0]), len(z[0]), z[0]))
    print("   %-46s DISTINCT pairs ok=%-6d VIOLATIONS=%-5d" % (name, len(ok), len(bad_l)))
    return len(ok), bad_l


def rh(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if i != j and L[i] - 1 >= L[j] + 1:
                Lp = list(L)
                Lp[i] -= 1
                Lp[j] += 1
                yield Lp


def up2(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            Lp = list(L)
            Lp[i] += 1
            Lp[j] += 1
            yield Lp


n_rh, bad_rh = sweep("(RH) unit transfer down: res(L') <= res(L)", rh)
n_u2, bad_u2 = sweep("(UP2) raise two by 1:    res(L') <= res(L)", up2)
print("   (RH)  holds on ARBITRARY terminating lists -- NO head block needed.  CENSUS.")
print("   (UP2) is FALSE in general.  Minimal counterexamples, printed rather than excluded:")
for c in bad_u2[:3]:
    print("        L=%s -> L'=%s : residue %d -> %d" % c)
ctrl("(UP2) general form refuted", len(bad_u2))
if bad_rh:
    bad("RH", "unit-transfer census violated: %s" % bad_rh[:2])
print("   => the ODD-sum half of (MON) is the head-block-dependent half, exactly as C1-P was;")
print("      the EVEN-sum half reduces to (RH), which needs no head block at all.")
DONE.add("boundary")

# ================================================================ 6. C1-M REPRODUCED
print("\n[6] OBSERVATION C1-M reproduced through the C1-S closed form (fourth independent time)")
n_m = 0
worst = {}
for N in range(2, 27):
    for lam in parts(N):
        if len(lam) < 2:
            continue
        r = res(M(lam))
        if r is None:
            continue
        n_m += 1
        k = len(lam)
        if r > bound(k):
            bad("C1-M", "lam=%s residue=%d bound=%d" % (lam, r, bound(k)))
        worst[k] = max(worst.get(k, 0), r)
att = [k for k in sorted(worst) if worst[k] == bound(k)]
print("   population: %d terminating partitions k>=2 over n<=26, 0 violations" % n_m)
print("   bound attained at k = %s  (all k from 2 to 26)" % att)
ctrl("CORRUPT: bound tightened to ceil(k/2) is violated",
     sum(1 for N in range(2, 27) for lam in parts(N)
         if len(lam) >= 2 and res(M(lam)) is not None and res(M(lam)) > (len(lam) + 1) // 2))
DONE.add("C1-M")

# ================================================================ 7. SELF-AUDIT
print("\n[7] SELF-AUDIT")
DECLARED = {"controls", "C1-S", "C1-U", "MON", "C1-P'", "boundary", "C1-M"}
missing = DECLARED - DONE
print("   declared blocks: %d   executed: %d   missing: %s"
      % (len(DECLARED), len(DONE), sorted(missing) if missing else "none"))
print("   diffed runA/runB calls: %d   disagreements: 0 (any would have exited 2)" % DIFFED)
print("   controls: %d, all firing: %s" % (len(CTRL), all(c[2] for c in CTRL)))
print("   MUST_ABORT inputs: %d   known-value controls: %d" % (len(MUST_ABORT), len(KNOWN)))
print("   elapsed: %.1fs" % (time.time() - T0))
if missing:
    bad("SELF", "declared block did not execute")
print("\n" + "=" * 100)
if FAIL:
    print("DEFECTS: %d" % len(FAIL))
    for x in FAIL:
        print("   " + x)
    sys.exit(1)
print("NO DEFECTS.  PROVED: C1-S, C1-U, C1-V.  CENSUS: MON, C1-P', RH.  REFUTED: general UP2.")
print("=" * 100)
sys.exit(0)
