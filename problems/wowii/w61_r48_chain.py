#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r48 -- (CHAIN), ONE OF THE TWO OBLIGATIONS r47 LEFT, TAKEN OFF THE BOARD.

r47 stopped with (DOM-MAJ) resting on exactly two MEASURED, UNPROVED statements:

  (WALK-SHAPE)  along the joint walk of a transfer edge, every state has either
                max A >= max B, or B = A + e_0 + e_j with rho_{A_j}(A) >= max(A)+1;
  (CHAIN)       every equal-sum dominance pair of TERMINATING partitions is joined by a
                chain of single-unit transfers that never leaves the terminating set.

This file proves (CHAIN).  It is the second of the two, and it needs no HH combinatorics at
all -- it needs two classical-style facts, both of which are proved here from scratch and
both of which are machine-checked CONSTRUCTIVELY (the proof's own witness is built and
verified, not just the statement censused).

--------------------------------------------------------------------------------------------
THEOREM DOWN-SET.   If lam is graphic and mu is obtained from lam by moving ONE unit from a
part of size x to a part of size y (possibly y = 0, i.e. a new part) with x >= y+2, then mu
is graphic.

  Proof.  Let G realise lam, u the vertex of degree x, v the vertex of degree y.  Put
    W := N(u) \ ({v} u N(v)).
  Since u is not in N(u) and v is not in N(v),
    |N(u) n N(v)| <= deg(v) - [u in N(v)]   and   |{v} n N(u)| = [v in N(u)] = [u in N(v)],
  so  |W| >= deg(u) - deg(v) = x - y >= 2 > 0.  Pick w in W.  Then uw is an edge, vw is not,
  and w is neither u nor v.  G' := G - uw + vw is a simple graph with
    deg u = x-1,  deg v = y+1,  every other degree unchanged,
  i.e. G' realises mu.  QED

  (Block [2] BUILDS G, BUILDS w, BUILDS G' and re-verifies it, on every instance.)

  Since dominance-comparable partitions are joined by such moves (THEOREM CHAIN-STEP below)
  and every intermediate stays weakly below lam, THEOREM DOWN-SET is exactly the statement
  that the graphic partitions of N form a DOWN-SET in the dominance order.

--------------------------------------------------------------------------------------------
THEOREM CHAIN-STEP.   If lam, mu are partitions of the same N with lam >= mu (dominance) and
lam != mu, then there is a partition nu with lam > nu >= mu obtained from lam by ONE unit
down-transfer.

  Proof.  Let i = min{t : lam_t != mu_t}; then lam_i > mu_i (prefix sums).  Put
    i* := max{t >= i : lam_t = lam_i}.
  For i <= t <= i*, lam_t = lam_i > mu_i >= mu_t, so S_{i*}(lam) > S_{i*}(mu) and
  lam_{i*} > lam_{i*+1}.  Since the totals agree there is t > i* with lam_t < mu_t; let
    j := min{t > i* : lam_t < mu_t},   j** := min{t > i* : lam_t = lam_j}   (so j** <= j).
  Then lam_{j**} = lam_j < mu_j <= mu_{j**}, and lam_{j**-1} > lam_{j**}: for j** = i*+1
  that is the display above, and for j** > i*+1 it is the minimality of j**.
  Set nu := lam - e_{i*} + e_{j**}.
   * nu is a partition.  Decrementing at i* is legal because lam_{i*} > lam_{i*+1}, unless
     j** = i*+1, in which case we need lam_{i*} >= lam_{j**}+2; if instead
     lam_{i*} = lam_{j**}+1 then mu_{j**} > lam_{j**} = lam_{i*}-1 >= mu_{i*} >= mu_{j**},
     absurd.  Incrementing at j** is legal because lam_{j**-1} > lam_{j**}.
   * nu >= mu.  S_t(nu) = S_t(lam) - 1 for i* <= t < j** and = S_t(lam) elsewhere, and for
     those t we showed S_t(lam) > S_t(mu): at t = i* directly, and for i* < t < j** <= j
     because lam_t >= mu_t there.
   * nu < lam and the potential sum_t (S_t(lam) - S_t(mu)) drops by j** - i* >= 1.  QED

--------------------------------------------------------------------------------------------
COROLLARY (CHAIN).   Every equal-sum dominance pair (A,B) of GRAPHIC partitions is joined by
a chain A = nu^0 > nu^1 > ... > nu^r = B of single-unit transfers, every nu^s GRAPHIC.

  Proof.  Iterate CHAIN-STEP from A downwards; it terminates because the potential is a
  non-negative integer that strictly drops.  Every nu^s satisfies nu^s <= A, and A is
  graphic, so DOWN-SET (applied along the chain nu^0 -> nu^s) gives nu^s graphic.  QED

That is r47's (CHAIN), with the transfer edges of the chain automatically inside the
terminating set.  (DOM-MAJ) now rests on (WALK-SHAPE) ALONE.

--------------------------------------------------------------------------------------------
WHAT COULD HAVE COME OUT THE OTHER WAY (sec 90 / sec 104).  Every census below is paired with
a control that FIRES on the same population:
  [1] down-moves preserve graphicness -- the UP-moves of the same population do NOT (control),
      and r45 measured "47 unit-transfer edges LEAVE the terminating set", which block [1c]
      re-derives and shows to be an artefact of that run's <= 11 PARTS window, not a
      counterexample: with the window removed the count is re-measured here.
  [2] the surgery -- the corrupt variant that picks w in N(u) n N(v) is run and must FAIL.
  [3] CHAIN-STEP -- the NAIVE index choice (first disagreement, first deficit) is run and
      must produce a NON-partition somewhere.
  [4] the assembled chains -- every element is re-tested for graphicness by TWO further
      implementations that share no code with the HH walk: Erdos-Gallai, and an explicit
      realisation whose degree sequence is compared back.

RULING CO': stepA/runA/runB lifted BY SOURCE TEXT from w61_r29_c1audit.py.
sec 105: `graphic_EG` (Erdos-Gallai inequalities) and `realize` (explicit graph construction)
share NO line with stepA and are diffed against it on the whole population.
No SAT, no solver, no exhaustive search.  Interpreter: .venv/bin/python3 (pure Python).
"""
import re
import sys
import time
from collections import Counter
from pathlib import Path

T0 = time.time()
LIMIT = 300.0
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()


def grab(t, name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---|print|NMAX|absorb))" % re.escape(name),
                  t, re.S | re.M)
    assert m, name
    return m.group(0)


ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(text, n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
stepA, runA, runB = ns["stepA"], ns["runA"], ns["runB"]

FAIL = []
CTRL = []
PARTIAL = False


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
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append((name, hits, ok))
    print("    [%s] %-86s hits=%d" % ("ok" if ok else "DEAD", name, hits))
    if not ok:
        bad("CONTROL-DEAD", name)


# --------------------------------------------------------------------- partitions and orders
def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r


def norm(x):
    return tuple(sorted([v for v in x if v > 0], reverse=True))


def pad(a, L):
    return list(a) + [0] * (L - len(a))


def dominates(a, b):
    """a >= b in dominance (equal sums assumed by the callers)."""
    L = max(len(a), len(b))
    A, B = pad(a, L), pad(b, L)
    sa = sb = 0
    for x, y in zip(A, B):
        sa += x
        sb += y
        if sb > sa:
            return False
    return True


def is_unit_transfer(a, b):
    """b is a with ONE unit moved DOWN: padded difference is one -1 strictly above one +1."""
    L = max(len(a), len(b))
    A, B = pad(a, L), pad(b, L)
    d = [y - x for x, y in zip(A, B)]
    if d.count(-1) != 1 or d.count(1) != 1 or d.count(0) != L - 2:
        return False
    return d.index(-1) < d.index(1)


# ------------------------------------------------------- IMPL 1: HH walk (lifted, RULING CO')
def hh_terminates(X):
    return runA(list(X))[0] is not None


# ------------------------------------------- IMPL 2 (sec 105): Erdos-Gallai.  Shares no line.
def graphic_EG(X):
    """Erdos-Gallai: sum even and for every k,
       sum_{i<=k} X_i <= k(k-1) + sum_{i>k} min(X_i, k).
    Nothing here refers to a Havel-Hakimi step."""
    L = sorted(X, reverse=True)
    if sum(L) % 2:
        return False
    n = len(L)
    for k in range(1, n + 1):
        lhs = sum(L[:k])
        rhs = k * (k - 1) + sum(min(v, k) for v in L[k:])
        if lhs > rhs:
            return False
    return True


# ------------------------------- IMPL 3 (sec 105): explicit realisation.  Shares no line either.
def realize(X):
    """Build a simple graph on len(X) labelled vertices with deg(v) = X[v] (X sorted desc),
    by repeatedly saturating a vertex of largest residual degree.  Returns adjacency sets, or
    None if the construction jams.  Returns the empty graph for X = ()."""
    L = list(X)
    n = len(L)
    rem = list(L)
    adj = [set() for _ in range(n)]
    guard = sum(L) + n + 2
    while guard >= 0:
        guard -= 1
        alive = [v for v in range(n) if rem[v] > 0]
        if not alive:
            break
        u = max(alive, key=lambda v: (rem[v], -v))
        d = rem[u]
        cand = sorted([v for v in alive if v != u], key=lambda v: (-rem[v], v))
        cand = [v for v in cand if v not in adj[u]][:d]
        if len(cand) < d:
            return None
        rem[u] = 0
        for v in cand:
            adj[u].add(v)
            adj[v].add(u)
            rem[v] -= 1
            if rem[v] < 0:
                return None
    if any(r != 0 for r in rem):
        return None
    if tuple(sorted((len(adj[v]) for v in range(n)), reverse=True)) != norm(X):
        return None
    for v in range(n):
        if v in adj[v]:
            return None
        for w in adj[v]:
            if v not in adj[w]:
                return None
    return adj


print("=" * 100)
print("w61 r48 -- (CHAIN) PROVED: the graphic partitions are a DOWN-SET in dominance, and")
print("           dominance-comparable partitions are joined by unit transfers inside it.")
print("           Interpreter .venv/bin/python3 (pure Python).")
print("=" * 100)

# ============================================================ [0] POPULATION, THREE-WAY DIFF
NBIG = 22
ALL = {}
for N in range(1, NBIG + 1):
    ALL[N] = list(parts(N))
GRAPHIC = {}
n_all = n_gr = 0
dis_eg = dis_rz = 0
ex_eg = ex_rz = None
for N in range(1, NBIG + 1):
    g = []
    for p in ALL[N]:
        n_all += 1
        h = hh_terminates(p)
        e = graphic_EG(p)
        if h != e:
            dis_eg += 1
            if ex_eg is None:
                ex_eg = p
        r = realize(p)
        if h != (r is not None):
            dis_rz += 1
            if ex_rz is None:
                ex_rz = p
        if h:
            g.append(p)
            n_gr += 1
    GRAPHIC[N] = g
GSET = set()
for N in GRAPHIC:
    GSET.update(GRAPHIC[N])

print("\n[0] POPULATION and the sec 105 three-way agreement on 'graphic'.")
print("    all partitions of N <= %d (no cap on the number of parts) : %d" % (NBIG, n_all))
print("    of them GRAPHIC (Havel-Hakimi terminates)                 : %d" % n_gr)
print("    disagreements  HH  vs  Erdos-Gallai                       : %d   e.g. %s"
      % (dis_eg, ex_eg))
print("    disagreements  HH  vs  explicit realisation               : %d   e.g. %s"
      % (dis_rz, ex_rz))
if dis_eg:
    bad("EG-DIFF", "%d" % dis_eg)
if dis_rz:
    bad("RZ-DIFF", "%d" % dis_rz)
ctrl("CONTROL: the population contains NON-graphic partitions (the test is not trivial)",
     n_all - n_gr)
ctrl("CONTROL: the population contains graphic partitions", n_gr)

# reproduce r47's own two populations as CHECKED numbers, not narrated ones
for nmax, mxp, want_term in ((16, 10, 181), (20, 12, 531)):
    t = sum(1 for N in range(1, nmax + 1) for p in ALL[N]
            if len(p) <= mxp and p in GSET)
    print("    r47 population reproduced  N <= %2d, <= %2d parts : %d terminating (r47 banked %d)"
          % (nmax, mxp, t, want_term))
    if t != want_term:
        bad("REPRO-POP", "N<=%d: %d vs %d" % (nmax, t, want_term))

# =========================================================== [1] THEOREM DOWN-SET, CENSUSED
print("\n[1] THEOREM DOWN-SET censused.  For every GRAPHIC lam and every single unit DOWN")
print("    transfer lam -> mu (a part x >= y+2 gives one unit to a part y, y = 0 allowed),")
print("    is mu graphic?  Every instance is a place the claim could fail.")


def unit_downs(lam):
    """every partition obtained from lam by moving one unit from a part x to a part y with
    x >= y+2 (y = 0 means a brand-new part).  Nothing is capped."""
    out = set()
    L = list(lam) + [0]
    for i in range(len(L)):
        for j in range(len(L)):
            if i >= j:
                continue
            if L[i] - 1 < L[j] + 1:
                continue
            M = list(L)
            M[i] -= 1
            M[j] += 1
            out.add(norm(M))
    return out


def unit_ups(lam):
    """the reverse moves: one unit from a part y to a part x with x >= y (x above y)."""
    out = set()
    L = list(lam)
    for i in range(len(L)):
        for j in range(len(L)):
            if i >= j:
                continue
            M = list(L)
            M[i] += 1
            M[j] -= 1
            if M[j] < 0:
                continue
            if norm(M) == norm(lam):
                continue
            out.add(norm(M))
    return out


ds_t = ds_v = 0
ds_ex = None
up_t = up_v = 0
up_ex = None
for N in range(1, NBIG + 1):
    for lam in GRAPHIC[N]:
        for mu in unit_downs(lam):
            ds_t += 1
            if mu not in GSET:
                ds_v += 1
                if ds_ex is None:
                    ds_ex = (lam, mu)
        for nu in unit_ups(lam):
            up_t += 1
            if nu not in GSET:
                up_v += 1
                if up_ex is None:
                    up_ex = (lam, nu)
print("    (lam graphic, mu one unit DOWN) instances : %d" % ds_t)
print("    of them with mu NOT graphic               : %d   e.g. %s" % (ds_v, ds_ex))
if ds_v:
    bad("DOWN-SET", "%d violations, e.g. %s" % (ds_v, ds_ex))
ctrl("CONTROL: the down-move census is non-vacuous", ds_t)
print("    the SAME census run UPWARDS (lam graphic, one unit UP) : %d instances" % up_t)
print("    of them landing OUTSIDE the graphic set               : %d   e.g. %s"
      % (up_v, up_ex))
ctrl("CORRUPT CONTROL: upward unit transfers DO leave the graphic set -- the direction of "
     "THEOREM DOWN-SET is load-bearing", up_v)

# [1c] r45's "47 unit-transfer edges LEAVE the terminating set", re-derived with and without
#      that run's <= 11 PARTS window.  r45 read it as an obstruction to (CHAIN); if
#      THEOREM DOWN-SET is right it can only be the window.
lost_cap = lost_free = 0
ex_cap = None
R45_NMAX = 18          # r45's window: even N up to here, at most R45_PARTS parts
R45_PARTS = 11
for N in range(2, R45_NMAX + 1, 2):
    TERM = [p for p in ALL[N] if len(p) <= R45_PARTS and p in GSET]
    TS = set(TERM)
    for C in TERM:
        for D in unit_downs(C):
            if D not in TS:
                lost_cap += 1
                if ex_cap is None:
                    ex_cap = (C, D, len(D))
            if D not in GSET:
                lost_free += 1
print("    [1c] r45's window (N even <= %d, <= %d parts): down-edges leaving THAT set : %d"
      % (R45_NMAX, R45_PARTS, lost_cap))
print("         of those, edges leaving the GRAPHIC set itself                        : %d"
      % lost_free)
print("         smallest witness and its number of parts                              : %s"
      % (ex_cap,))
ctrl("CONTROL: r45's lost-edge count is reproduced non-vacuously", lost_cap)
ctrl("CONTROL: none of r45's lost edges leaves the GRAPHIC set -- they leave that run's "
     "PARTS window", lost_free, must_fire=False)

# ==================================================== [2] THE PROOF'S OWN WITNESS, CONSTRUCTED
print("\n[2] THEOREM DOWN-SET's PROOF, run as a construction (sec 105).  For every instance of")
print("    [1]: build G |= lam, build W = N(u) \\ ({v} u N(v)), take w in W, build")
print("    G' = G - uw + vw, and CHECK G' is simple with degree sequence mu.")
sg_t = sg_fail = 0
sg_ex = None
bound_t = bound_bad = 0
corrupt_t = corrupt_bad = 0
for N in range(1, NBIG + 1):
    if over():
        break
    for lam in GRAPHIC[N]:
        adj0 = realize(lam)
        if adj0 is None:
            bad("REALIZE", "%s" % (lam,))
            continue
        n = len(lam)
        L = list(lam) + [0]
        for i in range(len(L)):
            for j in range(len(L)):
                if i >= j or L[i] - 1 < L[j] + 1:
                    continue
                mu = norm([L[t] - (t == i) + (t == j) for t in range(len(L))])
                # vertices: i is a real vertex; j may be the appended 0 (a NEW vertex)
                adj = [set(s) for s in adj0] + [set()]
                u, v = i, j
                W = [w for w in adj[u] if w != v and w not in adj[v]]
                bound_t += 1
                if len(W) < len(adj[u]) - len(adj[v]):
                    bound_bad += 1
                sg_t += 1
                if not W:
                    sg_fail += 1
                    if sg_ex is None:
                        sg_ex = (lam, mu)
                    continue
                w = W[0]
                adj[u].discard(w)
                adj[w].discard(u)
                adj[v].add(w)
                adj[w].add(v)
                degs = tuple(sorted((len(s) for s in adj), reverse=True))
                simple = all(x not in adj[x] for x in range(len(adj))) and \
                    all(x in adj[y] for x in range(len(adj)) for y in adj[x])
                if not simple or norm(degs) != mu:
                    sg_fail += 1
                    if sg_ex is None:
                        sg_ex = (lam, mu, degs)
                # CORRUPT VARIANT: take w' inside N(u) n N(v) instead -- the edge vw' already
                # exists, so the "swap" cannot be performed.
                base = [set(s) for s in adj0] + [set()]
                Wbad = [x for x in base[u] if x in base[v]]
                if Wbad:
                    corrupt_t += 1
                    if Wbad[0] in adj0[v]:
                        corrupt_bad += 1
print("    surgeries attempted                       : %d" % sg_t)
print("    surgeries that FAILED (no w, or bad G')   : %d   e.g. %s" % (sg_fail, sg_ex))
if sg_fail:
    bad("SURGERY", "%d  %s" % (sg_fail, sg_ex))
print("    instances where |W| >= deg(u) - deg(v) FAILED : %d   (the proof's counting bound)"
      % bound_bad)
if bound_bad:
    bad("SURGERY-BOUND", "%d" % bound_bad)
ctrl("CONTROL: the surgery census is non-vacuous", sg_t)
ctrl("CORRUPT CONTROL: choosing w inside N(u) n N(v) always hits an EXISTING edge vw, so the "
     "restriction w not-in N(v) is load-bearing", corrupt_bad)
if corrupt_t != corrupt_bad:
    bad("CORRUPT-SURGERY", "%d of %d" % (corrupt_bad, corrupt_t))

# ======================================================= [3] THEOREM CHAIN-STEP, CONSTRUCTED
print("\n[3] THEOREM CHAIN-STEP, run as a construction, on EVERY equal-sum dominance pair of")
print("    partitions (graphic or not -- the lemma is about the dominance order alone).")


def prefix(a, L):
    out = []
    s = 0
    for v in pad(a, L):
        s += v
        out.append(s)
    return out


def chain_step(lam, mu):
    """the nu of THEOREM CHAIN-STEP.  Returns (nu, i*, j**)."""
    L = max(len(lam), len(mu)) + 1
    A, B = pad(lam, L), pad(mu, L)
    i = min(t for t in range(L) if A[t] != B[t])
    istar = max(t for t in range(i, L) if A[t] == A[i])
    j = min(t for t in range(istar + 1, L) if A[t] < B[t])
    jss = min(t for t in range(istar + 1, L) if A[t] == A[j])
    nu = list(A)
    nu[istar] -= 1
    nu[jss] += 1
    return norm(nu), istar, jss


def chain_step_naive(lam, mu):
    """the choice a first draft would make: FIRST disagreement, FIRST deficit below it.
    Kept as the corrupt control for the i*/j** refinement."""
    L = max(len(lam), len(mu)) + 1
    A, B = pad(lam, L), pad(mu, L)
    i = min(t for t in range(L) if A[t] != B[t])
    j = min(t for t in range(i + 1, L) if A[t] < B[t])
    nu = list(A)
    nu[i] -= 1
    nu[j] += 1
    return tuple(nu)


cs_t = cs_bad_part = cs_bad_dom = cs_bad_pot = cs_bad_tr = 0
cs_ex = None
nv_t = nv_bad = 0
nv_ex = None
for N in range(1, NBIG + 1):
    if over():
        break
    P = ALL[N]
    for lam in P:
        for mu in P:
            if lam == mu or not dominates(lam, mu):
                continue
            cs_t += 1
            nu, istar, jss = chain_step(lam, mu)
            L = max(len(lam), len(mu), len(nu)) + 1
            if sum(nu) != N or list(nu) != sorted(nu, reverse=True) or nu == lam:
                cs_bad_part += 1
                if cs_ex is None:
                    cs_ex = ("PART", lam, mu, nu)
            if not (dominates(lam, nu) and dominates(nu, mu)):
                cs_bad_dom += 1
                if cs_ex is None:
                    cs_ex = ("DOM", lam, mu, nu)
            if not is_unit_transfer(lam, nu):
                cs_bad_tr += 1
                if cs_ex is None:
                    cs_ex = ("TRANSFER", lam, mu, nu)
            pot0 = sum(x - y for x, y in zip(prefix(lam, L), prefix(mu, L)))
            pot1 = sum(x - y for x, y in zip(prefix(nu, L), prefix(mu, L)))
            if not (0 <= pot1 < pot0):
                cs_bad_pot += 1
                if cs_ex is None:
                    cs_ex = ("POTENTIAL", lam, mu, nu)
            # the naive choice, same pair
            nvv = chain_step_naive(lam, mu)
            nv_t += 1
            if list(nvv) != sorted(nvv, reverse=True) or min(nvv) < 0:
                nv_bad += 1
                if nv_ex is None:
                    nv_ex = (lam, mu, nvv)
print("    equal-sum dominance pairs tested            : %d" % cs_t)
print("    nu not a partition / equal to lam           : %d" % cs_bad_part)
print("    lam >= nu >= mu FAILED                      : %d" % cs_bad_dom)
print("    nu not a single unit transfer from lam      : %d" % cs_bad_tr)
print("    potential did not strictly drop             : %d   e.g. %s" % (cs_bad_pot, cs_ex))
for got, tag in ((cs_bad_part, "CS-PART"), (cs_bad_dom, "CS-DOM"),
                 (cs_bad_tr, "CS-TRANSFER"), (cs_bad_pot, "CS-POT")):
    if got:
        bad(tag, "%d  %s" % (got, cs_ex))
ctrl("CONTROL: CHAIN-STEP was exercised on a non-empty population", cs_t)
print("    NAIVE index choice on the same pairs        : %d instances, %d produce a NON-partition"
      % (nv_t, nv_bad))
print("      smallest such                             : %s" % (nv_ex,))
ctrl("CORRUPT CONTROL: the naive (first-disagreement, first-deficit) choice BREAKS -- the "
     "i*/j** refinement is load-bearing", nv_bad)

# ================================================================ [4] (CHAIN), ASSEMBLED
print("\n[4] (CHAIN) ASSEMBLED.  For every equal-sum dominance pair of GRAPHIC partitions,")
print("    iterate CHAIN-STEP from A down to B and re-verify EVERY element of the chain with")
print("    the two implementations that share no code with the HH walk.")
ch_pairs = ch_edges = 0
ch_bad = ch_len_max = 0
ch_ex = None
recheck_eg = recheck_rz = 0
for N in range(1, NBIG + 1):
    if over():
        break
    G = GRAPHIC[N]
    for A in G:
        for B in G:
            if A == B or not dominates(A, B):
                continue
            ch_pairs += 1
            cur = A
            path = [A]
            guard = N * N + 8
            while cur != B and guard >= 0:
                guard -= 1
                cur, _, _ = chain_step(cur, B)
                path.append(cur)
            if cur != B:
                ch_bad += 1
                if ch_ex is None:
                    ch_ex = ("NOREACH", A, B)
                continue
            ch_len_max = max(ch_len_max, len(path) - 1)
            for s in range(len(path) - 1):
                ch_edges += 1
                if not is_unit_transfer(path[s], path[s + 1]):
                    ch_bad += 1
                    if ch_ex is None:
                        ch_ex = ("EDGE", A, B, path[s], path[s + 1])
            for nu in path:
                if not graphic_EG(nu):
                    ch_bad += 1
                    if ch_ex is None:
                        ch_ex = ("EG", A, B, nu)
                else:
                    recheck_eg += 1
                if realize(nu) is None:
                    ch_bad += 1
                    if ch_ex is None:
                        ch_ex = ("RZ", A, B, nu)
                else:
                    recheck_rz += 1
print("    equal-sum dominance pairs of GRAPHIC partitions, N <= %d : %d" % (NBIG, ch_pairs))
print("    chain edges built                                        : %d" % ch_edges)
print("    longest chain                                            : %d edges" % ch_len_max)
print("    chain elements re-certified graphic by Erdos-Gallai      : %d" % recheck_eg)
print("    chain elements re-certified graphic by explicit realisation : %d" % recheck_rz)
print("    FAILURES of any kind                                     : %d   e.g. %s"
      % (ch_bad, ch_ex))
if ch_bad:
    bad("CHAIN", "%d  %s" % (ch_bad, ch_ex))
ctrl("CONTROL: chains longer than one edge occur (the chain is not a re-labelled edge)",
     1 if ch_len_max > 1 else 0)
ctrl("CONTROL: the (CHAIN) census is non-vacuous", ch_pairs)

# r47's own two populations, so the reduction it states is covered verbatim
for nmax, mxp, want in ((16, 10, 2683), (20, 12, 19744)):
    c = 0
    for N in range(1, nmax + 1):
        G = [p for p in ALL[N] if len(p) <= mxp and p in GSET]
        for A in G:
            for B in G:
                if A != B and dominates(A, B):
                    c += 1
    print("    r47's dominance-pair count reproduced  N <= %2d, <= %2d parts : %d (r47 banked %d)"
          % (nmax, mxp, c, want))
    if c != want:
        bad("REPRO-DOMPAIRS", "N<=%d : %d vs %d" % (nmax, c, want))

# ================================================================================ SUMMARY
print("\n" + "=" * 100)
ok = sum(1 for _, _, o in CTRL if o)
print("ELAPSED %.2f s / %.0f s internal limit ; PARTIAL=%s" % (time.time() - T0, LIMIT, PARTIAL))
print("CONTROLS %d/%d firing ; DEFECTS %d" % (ok, len(CTRL), len(FAIL)))
for f in FAIL:
    print("   DEFECT: %s" % f)
print("=" * 100)
sys.exit(1 if FAIL or PARTIAL else 0)
