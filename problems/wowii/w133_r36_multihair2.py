#!/usr/bin/env python3
"""
WOWII-133 round 36 — MULTI-HAIR CASE II.

Self-contained: every primitive is COPIED into this file, nothing is imported from
another round's script.  Pure stdlib -> runs on SYSTEM python3 (no networkx, no sympy
needed).  Hard internal deadline; no SAT, no exhaustive search over a large space.

WHAT THIS FILE CERTIFIES (statements re-derived by hand in the round write-up):

  (MH-P2)   two-hair concatenation, RE-DERIVED IN MY OWN HAND (this is the one piece of
            the quarantined E12 that survived its own batch; it is used here only after
            re-derivation, never on E12's authority):
                path(G) >= h_i + h_j + d_{G'}(w_i,w_j) + 1     for any two hairs i != j.

  (MH-RAD-UB)  rad(G) <= ecc_G(w) = max( ecc_{G'}(w), max_m (d_{G'}(w,w_m)+h_m) )
               for w = the root of a longest hair;  and the coarse form
               rad(G) <= rad(G') + h_max.

  (MH-GAP)  path(G) - rad(G)  >=  endpath_{G'}(w_max) - rad(G')   [UNCONDITIONAL]
            -> the whole multi-hair front (BOTH cases) reduces to an ANCHORED endpath
               statement on G' at the root of a longest hair.

  (MH-II)   the Case-II (rad(G) > rad(G')) sub-closures that need NOTHING imported.

PART 0 is a GUARD with its class declared, tested against a member of the class it has
not seen (doctrine, cert_w133_r35 section 5).
"""
import sys, time, itertools
from collections import deque

T0 = time.time()
DEADLINE = 240.0          # hard internal self-limit, seconds
CHECKS = 0
FAILS = 0
PARTS_RUN = set()

def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg)

def deadline_hit():
    return (time.time() - T0) > DEADLINE

# ---------------------------------------------------------------- primitives
def mkadj(n, edges):
    adj = [set() for _ in range(n)]
    for (u, v) in edges:
        assert u != v
        adj[u].add(v); adj[v].add(u)
    return adj

def bfs(adj, s):
    n = len(adj); dist = [-1]*n; dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u]+1; q.append(v)
    return dist

def connected(adj):
    return all(d >= 0 for d in bfs(adj, 0))

def ecc_all(adj):
    return [max(bfs(adj, s)) for s in range(len(adj))]

def rad_of(adj):
    return min(ecc_all(adj))

def c4_free(adj):
    """this note's sense: no two vertices have two common neighbours."""
    n = len(adj)
    for u in range(n):
        for v in range(u+1, n):
            if len(adj[u] & adj[v]) >= 2:
                return False
    return True

def alpha_on(adj, S):
    """independence number of the induced subgraph on vertex set S (S small)."""
    S = list(S)
    best = 0
    m = len(S)
    for mask in range(1 << m):
        sel = [S[i] for i in range(m) if mask >> i & 1]
        if len(sel) <= best:
            continue
        ok = True
        for i in range(len(sel)):
            for j in range(i+1, len(sel)):
                if sel[j] in adj[sel[i]]:
                    ok = False; break
            if not ok: break
        if ok:
            best = len(sel)
    return best

def a_vec(adj):
    return [alpha_on(adj, adj[v]) for v in range(len(adj))]

def l_of(adj):
    a = a_vec(adj)
    return sum(a)/len(a), sum(a)

# ------------------------------------------------- induced path: the SEARCH
def _extend(adj, path, inpath, best, mode="ok"):
    """DFS.  CORRECT rule: a candidate x adjacent to the last vertex may be appended
    iff x has no neighbour in the path other than that last vertex."""
    if len(path) > best[0]:
        best[0] = len(path); best[1] = list(path)
    cur = path[-1]
    for x in adj[cur]:
        if inpath[x]:
            continue
        if mode == "ok":
            bad = any((y in adj[x]) for y in path[:-1])
        elif mode == "late":
            # DEFECT UNDER TEST (PART 0): only checks the *previous* vertex once the
            # path is long, so 0-step and 1-step behave correctly and only deeper
            # steps go wrong.  Neither r34's zero-step guard nor r35's one-step
            # post-mortem has seen this member of the family.
            if len(path) >= 3:
                bad = (path[-2] in adj[x])
            else:
                bad = any((y in adj[x]) for y in path[:-1])
        elif mode == "zero":
            bad = any((y in adj[x]) for y in path)      # r34's defect: blocks cur too
        else:
            raise ValueError(mode)
        if not bad:
            inpath[x] = True; path.append(x)
            _extend(adj, path, inpath, best, mode)
            path.pop(); inpath[x] = False

def longest_induced_path(adj, mode="ok"):
    n = len(adj); best = [0, []]
    for s in range(n):
        inpath = [False]*n; inpath[s] = True
        _extend(adj, [s], inpath, best, mode)
    return best[0], best[1]

def endpath(adj, w, mode="ok"):
    n = len(adj); best = [0, []]
    inpath = [False]*n; inpath[w] = True
    _extend(adj, [w], inpath, best, mode)
    return best[0]

# ------------------------------------ induced path: the INDEPENDENT ORACLE
def is_induced_path(adj, S):
    """True iff G[S] is a path (|S|>=1)."""
    S = list(S)
    if not S: return False
    idx = set(S)
    deg = {}
    for v in S:
        deg[v] = len(adj[v] & idx)
    if len(S) == 1:
        return True
    if any(d > 2 for d in deg.values()):
        return False
    if sum(1 for v in S if deg[v] == 1) != 2:
        return False
    # connectivity within S
    start = S[0]; seen = {start}; q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u] & idx:
            if v not in seen:
                seen.add(v); q.append(v)
    return len(seen) == len(S)

def oracle_longest_induced_path(adj, ncap=14):
    """Independent double-source: enumerate vertex subsets.  Only for n <= ncap, so
    this is a seconds-level check, not a heavy search."""
    n = len(adj)
    if n > ncap:
        return None
    best = 0
    for mask in range(1, 1 << n):
        k = bin(mask).count("1")
        if k <= best:
            continue
        S = [i for i in range(n) if mask >> i & 1]
        if is_induced_path(adj, S):
            best = k
    return best

def oracle_endpath(adj, w, ncap=14):
    n = len(adj)
    if n > ncap:
        return None
    best = 0
    for mask in range(1, 1 << n):
        if not (mask >> w & 1):
            continue
        k = bin(mask).count("1")
        if k <= best:
            continue
        S = [i for i in range(n) if mask >> i & 1]
        if is_induced_path(adj, S):
            idx = set(S)
            if len(S) == 1 or len(adj[w] & idx) == 1:
                best = k
    return best

# ------------------------------------------------------------------- bases
def cycle(n):   return n, [(i, (i+1) % n) for i in range(n)]
def path_g(n):  return n, [(i, i+1) for i in range(n-1)]

def petersen():
    e = [(i, (i+1) % 5) for i in range(5)]
    e += [(i, i+5) for i in range(5)]
    e += [(5+i, 5+(i+2) % 5) for i in range(5)]
    return 10, e

def theta333():
    # two hubs joined by three internally disjoint paths of length 3
    e = []; nxt = 2
    for _ in range(3):
        a, b = nxt, nxt+1; nxt += 2
        e += [(0, a), (a, b), (b, 1)]
    return nxt, e

def two_c9():
    e = [(i, (i+1) % 9) for i in range(9)]
    e += [(9+i, 9+(i+1) % 9) for i in range(9)]
    e += [(0, 9)]
    return 18, e

BASES = [("C6", cycle(6)), ("C9", cycle(9)), ("Petersen", petersen()),
         ("Theta333", theta333()), ("P5", path_g(5)), ("2C9e", two_c9())]

def build_hairs(nbase, ebase, roots, hs):
    """attach hair i of length hs[i] at roots[i]; roots must be DISTINCT."""
    assert len(set(roots)) == len(roots)
    e = list(ebase); n = nbase
    hair_vs = []
    for r, h in zip(roots, hs):
        prev = r; this = []
        for _ in range(h):
            e.append((prev, n)); this.append(n); prev = n; n += 1
        hair_vs.append(this)
    return n, e, hair_vs

# ============================================================ PART 0 — GUARD
print("="*78)
print("PART 0 — THE GUARD, ITS DECLARED CLASS, AND AN UNSEEN MEMBER OF THAT CLASS")
print("="*78)
print("""GUARD (new this round): every induced-path / endpath value used anywhere below is
  cross-checked against an INDEPENDENT subset-enumeration oracle on every host with
  n <= 14.  The oracle shares no code path with the DFS: it enumerates vertex subsets
  and tests the 'is a path' predicate directly.
CLASS THE GUARD CLAIMS TO COVER: *any* induced-path search that returns a value other
  than the true longest induced path -- searches that block the wrong vertex set at ANY
  depth (zero-step, one-step, or later), searches that stop early, searches that admit
  a chord.  It is NOT a check on a symptom (a suspicious printed number); it is an
  independent recomputation of the quantity.
UNSEEN MEMBER USED AS THE TEST: a LATE-BLOCKING defect -- correct for the first two
  steps, and from length 3 on it only excludes the previous vertex instead of the whole
  path.  r34's guard was written for the ZERO-step defect; r35's real defect was the
  ONE-step defect.  Neither has seen this one.""")
PARTS_RUN.add(0)

# the guard must FIRE on the unseen member, and must NOT fire on the correct search
guard_hosts = [("C6", cycle(6)), ("Theta333", theta333()), ("Petersen", petersen()),
               ("P5", path_g(5)), ("C9", cycle(9))]
fired_late = 0; fired_zero = 0; false_alarm = 0
for nm, (n, e) in guard_hosts:
    adj = mkadj(n, e)
    orc = oracle_longest_induced_path(adj)
    good = longest_induced_path(adj, "ok")[0]
    late = longest_induced_path(adj, "late")[0]
    zero = longest_induced_path(adj, "zero")[0]
    if orc is None:
        continue
    if good != orc: false_alarm += 1
    if late != orc: fired_late += 1
    if zero != orc: fired_zero += 1
    print("  %-9s n=%2d  oracle=%2d  correct=%2d  LATE-defect=%2d  ZERO-defect=%2d"
          % (nm, n, orc, good, late, zero))
ck(false_alarm == 0, "guard false-alarms on the correct search")
ck(fired_late >= 1, "guard did NOT fire on the UNSEEN member (late-blocking)")
ck(fired_zero >= 1, "guard did not fire on the known zero-step member")
print("  guard fired on the UNSEEN late-blocking defect at %d/%d hosts; on the known"
      % (fired_late, len(guard_hosts)))
print("  zero-step defect at %d/%d; false alarms on the correct search: %d"
      % (fired_zero, len(guard_hosts), false_alarm))
print("  POPULATION for these counts: the %d guard hosts listed above, all n <= 14."
      % len(guard_hosts))

# ================================================= the certification family
print()
print("="*78)
print("PARTS 1-4 — THE MULTI-HAIR FAMILY")
print("="*78)
CONFIGS = []
for bname, (nb, eb) in BASES:
    adjb = mkadj(nb, eb)
    if not connected(adjb):
        continue
    for k in (1, 2, 3):
        for roots in itertools.combinations(range(min(nb, 4)), k):
            for hs in itertools.product((1, 2, 3), repeat=k):
                if nb + sum(hs) > 16:
                    continue
                CONFIGS.append((bname, nb, eb, roots, hs))
print("configurations generated: %d" % len(CONFIGS))
print("EXCLUSION LIST (identical population for every count below): 6 designed bases")
print("  (C6, C9, Petersen, Theta(3,3,3), P5, two C9 joined by an edge); roots among the")
print("  first min(n,4) vertices, distinct; k in {1,2,3}; h_i in {1,2,3}; total order")
print("  capped at 16.  DESIGNED, NOT EXHAUSTIVE, NO RANDOM TRAWL.")

# ============================================ PARTS 1-4, one pass over the family
p2_pop = p2_ok = 0
radub_pop = radub_ok = 0
radub2_pop = radub2_ok = 0
gap_pop = gap_ok = 0
oracle_pop = oracle_ok = 0
case1 = case2 = 0
c2_closed_uncond = 0
c2_residual = 0
c2_conj_true = 0
c2_closed_at4 = 0
c2_residual_at4 = 0
lfloor_hist = {}
lfloor_hist_c2 = {}
c2_l_gt4 = 0
skipped_c4 = skipped_mu = skipped_deadline = skipped_disc = 0
residual_examples = []
implication_pop = implication_ok = 0

for (bname, nb, eb, roots, hs) in CONFIGS:
    if deadline_hit():
        skipped_deadline += 1
        continue
    adjb = mkadj(nb, eb)
    if not c4_free(adjb):
        skipped_c4 += 1; continue
    ab = a_vec(adjb)
    if min(ab) < 2:
        skipped_mu += 1; continue            # (TAIL-1) needs mu(G') >= 2
    n, e, hair_vs = build_hairs(nb, eb, roots, hs)
    adj = mkadj(n, e)
    if not c4_free(adj):
        skipped_c4 += 1; continue
    if not connected(adj):
        skipped_disc += 1; continue

    r_prime = rad_of(adjb)
    R = rad_of(adj)
    dist_b = [bfs(adjb, s) for s in range(nb)]
    ecc_b = ecc_all(adjb)

    # --- longest hair and its root
    imax = max(range(len(hs)), key=lambda i: hs[i])
    hmax = hs[imax]; wmax = roots[imax]
    e_w = ecc_b[wmax]
    M = max(dist_b[wmax][roots[m]] + hs[m] for m in range(len(hs)))

    P = longest_induced_path(adj)[0]
    orc = oracle_longest_induced_path(adj)
    if orc is not None:
        oracle_pop += 1
        if orc == P: oracle_ok += 1
        else: ck(False, "%s roots=%s hs=%s: DFS path=%d oracle=%d" % (bname, roots, hs, P, orc))
    ep = endpath(adjb, wmax)
    orc_e = oracle_endpath(adjb, wmax)
    if orc_e is not None:
        oracle_pop += 1
        if orc_e == ep: oracle_ok += 1
        else: ck(False, "%s w=%d: DFS endpath=%d oracle=%d" % (bname, wmax, ep, orc_e))

    # --- (MH-P2) two-hair concatenation
    if len(hs) >= 2:
        for i in range(len(hs)):
            for j in range(i+1, len(hs)):
                bound = hs[i] + hs[j] + dist_b[roots[i]][roots[j]] + 1
                p2_pop += 1
                if P >= bound: p2_ok += 1
                else: ck(False, "(MH-P2) violated %s roots=%s hs=%s pair(%d,%d): P=%d bound=%d"
                         % (bname, roots, hs, i, j, P, bound))

    # --- (MH-RAD-UB) sharp form at w_max, and coarse form
    radub_pop += 1
    if R <= max(e_w, M): radub_ok += 1
    else: ck(False, "(MH-RAD-UB sharp) violated %s roots=%s hs=%s: R=%d max(e,M)=%d"
             % (bname, roots, hs, R, max(e_w, M)))
    radub2_pop += 1
    if R <= r_prime + hmax: radub2_ok += 1
    else: ck(False, "(MH-RAD-UB coarse) violated %s roots=%s hs=%s: R=%d r'+hmax=%d"
             % (bname, roots, hs, R, r_prime + hmax))

    # --- (MH-GAP)
    gap_pop += 1
    if P - R >= ep - r_prime: gap_ok += 1
    else: ck(False, "(MH-GAP) violated %s roots=%s hs=%s: P-R=%d ep-r'=%d"
             % (bname, roots, hs, P - R, ep - r_prime))

    # --- the conjecture itself, and the case split
    lG, _ = l_of(adj)
    lGp, _ = l_of(adjb)
    tG = int(lG // 1)
    conj = (P >= R + tG)
    ck(conj, "CONJECTURE FALSE on %s roots=%s hs=%s: P=%d R=%d floor(l)=%d"
       % (bname, roots, hs, P, R, tG))

    # implication form: conjecture for G' => conjecture for G, via (MH-C) + (MH-GAP)
    Pp = longest_induced_path(adjb)[0]
    tGp = int(lGp // 1)
    if Pp >= r_prime + tGp:                 # G' satisfies the conjecture
        implication_pop += 1
        if conj: implication_ok += 1

    lfloor_hist[tG] = lfloor_hist.get(tG, 0) + 1

    if R == r_prime:
        case1 += 1
    elif R > r_prime:
        case2 += 1
        lfloor_hist_c2[tG] = lfloor_hist_c2.get(tG, 0) + 1
        if lG > 4: c2_l_gt4 += 1
        if conj: c2_conj_true += 1
        # unconditional sub-closure: (MH-GAP) + (TAIL-1) with no import
        floor_A = hmax + (e_w + 2) - max(e_w, M)          # route A vs sharp radius
        floor_B = (hmax + M + 1) - max(e_w, M) if len(hs) >= 2 else -10**9
        floor_C = ep - r_prime                            # (MH-GAP), still no import
        floor = max(floor_A, floor_B, floor_C)
        # THE COUNTERFACTUAL THAT MATTERS: route A2 lives in the l>4 regime, where the
        # target constant is 4, not this family's floor(l).  Re-score against 4.
        if floor >= 4: c2_closed_at4 += 1
        else: c2_residual_at4 += 1
        if floor >= tG:
            c2_closed_uncond += 1
        else:
            c2_residual += 1
            if len(residual_examples) < 6:
                residual_examples.append((bname, roots, hs, R, r_prime, tG, floor, P))
    else:
        ck(False, "rad(G) < rad(G') on %s roots=%s hs=%s" % (bname, roots, hs))

PARTS_RUN.update({1, 2, 3, 4})
certified = case1 + case2

print()
print("--- skipped, with reasons (every 0 below ships with this list) ---")
print("  not C4-free (base or G): %d   mu(G') < 2: %d   disconnected: %d   past deadline: %d"
      % (skipped_c4, skipped_mu, skipped_disc, skipped_deadline))
print("  CERTIFIED and fully computed: %d of %d generated" % (certified, len(CONFIGS)))

print()
print("PART 1 — (MH-P2) two-hair concatenation, RE-DERIVED IN MY OWN HAND")
print("  path(G) >= h_i + h_j + d_{G'}(w_i,w_j) + 1 : %d of %d hair PAIRS" % (p2_ok, p2_pop))
print("PART 2 — (MH-RAD-UB)")
print("  sharp   rad(G) <= max(ecc_{G'}(w_max), M) : %d of %d" % (radub_ok, radub_pop))
print("  coarse  rad(G) <= rad(G') + h_max         : %d of %d" % (radub2_ok, radub2_pop))
print("PART 3 — (MH-GAP)  path(G)-rad(G) >= endpath_{G'}(w_max) - rad(G')")
print("  holds on %d of %d certified configurations" % (gap_ok, gap_pop))
print("PART 3b — INDEPENDENT ORACLE double-source on every path/endpath value, n <= 14")
print("  agreement: %d of %d (population = the values the oracle could afford)"
      % (oracle_ok, oracle_pop))
print("PART 4 — THE CASE SPLIT")
print("  CASE I  rad(G) = rad(G') : %d   (closed by (MH-I), r35)" % case1)
print("  CASE II rad(G) > rad(G') : %d" % case2)
print("    conjecture MEASURED true on            : %d of %d" % (c2_conj_true, case2))
print("    CLOSED UNCONDITIONALLY by this round's")
print("    floors (no l>4, no rad>=5, no F11)     : %d of %d" % (c2_closed_uncond, case2))
print("    RESIDUAL (floor < floor(l(G)))         : %d of %d" % (c2_residual, case2))
print("  implication form (conj for G' -> conj for G), over configurations where G'")
print("    itself satisfies the conjecture        : %d of %d" % (implication_ok, implication_pop))
print()
print("PART 5 — AGAINST THIS ROUND'S OWN INTEREST: WHAT THE CASE-II COUNT IS NOT")
print("  floor(l(G)) histogram over ALL %d certified configs : %s"
      % (certified, dict(sorted(lfloor_hist.items()))))
print("  floor(l(G)) histogram over the %d CASE II configs    : %s"
      % (case2, dict(sorted(lfloor_hist_c2.items()))))
print("  CASE II configurations with l(G) > 4                 : %d of %d" % (c2_l_gt4, case2))
print("  RE-SCORED with the target constant FORCED TO 4 (the l>4 regime route A2 lives in):")
print("    closed by the same unconditional floors            : %d of %d"
      % (c2_closed_at4, case2))
print("    RESIDUAL at constant 4                             : %d of %d"
      % (c2_residual_at4, case2))
if residual_examples:
    print("  residual examples (base, roots, hs, R, r', floor(l(G)), floor, path):")
    for r in residual_examples:
        print("    ", r)

print()
print("PARTS DECLARED: {0,1,2,3,4}   PARTS RUN: %s" % sorted(PARTS_RUN))
ck(PARTS_RUN == {0, 1, 2, 3, 4}, "not every declared part ran")
print("CHECKS=%d FAILURES=%d ELAPSED=%.1fs" % (CHECKS, FAILS, time.time()-T0))
print("EXIT=%d" % (1 if FAILS else 0))
sys.exit(1 if FAILS else 0)
