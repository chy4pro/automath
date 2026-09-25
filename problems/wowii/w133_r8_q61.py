#!/usr/bin/env python3
"""
w133 round 8 -- owner's own attack on Claim Q6.1 (the last item of pocket 1).

Setting (draft sections 16-19):  C in RES(b) ^ (C6), diameter pair (u,z) with
a(u)=a(z)=2 (the ONLY shape left, by Corollary G26.1), and the induced C6
Z = (u, u1, u2, z, y, x) at positions 0..5 supplied by G13, with
  N(u) = comp(u1)  |_|  {x}       ({x} a SINGLETON component of N(u))
  N(z) = comp(u2)  |_|  {y}       ({y} a SINGLETON component of N(z))

Off-Z vertices carry 0 or 2 Z-neighbours at cyclic distance 1 or 3 (G15), so the
only slots are   u1' = (u,u1),  u2' = (z,u2),  A = (u1,u2),  B = (y,x),
                 P = (u1,y),    Q = (u2,x),    W = no Z-neighbour at all.
((u,z), (x,u), (z,y) are impossible: distance 3, resp. singleton components.)

This script asserts the round-8 lemmas G32/G33/G34 and the closing mass budget.
Everything here is run BEFORE it is written into the draft.
NO SAT.  The only sweeps are (i) the exhaustive n<=7 labelled C4-free table
(small-graph table, allowed) and (ii) an exhaustive enumeration of the 2^15
edge patterns on the SIX named slot vertices of one fixed 12-vertex frame,
plus a bounded random sample of frames carrying W-vertices.
"""
import sys, itertools, random
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    connected, hoffman_singleton, alpha)
from w133_res3_search import er_polarity

FAIL = 0


def check(cond, msg):
    global FAIL
    if not cond:
        FAIL += 1
        print("  *** ASSERT FAILED: " + msg)
    return cond


def has_induced_pk(adj, k):
    """True iff the graph contains an induced path on k vertices."""
    n = len(adj)

    def ext(path, forb):
        if len(path) == k:
            return True
        last = path[-1]
        for w in adj[last]:
            if w in forb:
                continue
            if any(w in adj[p] for p in path[:-1]):
                continue
            if ext(path + [w], forb | {w}):
                return True
        return False

    for s in range(n):
        if ext([s], {s}):
            return True
    return False


def induced_c6s(adj):
    """Yield every induced 6-cycle as a tuple (v0..v5) up to rotation/reflection."""
    n = len(adj)
    seen = set()
    for v0 in range(n):
        for v1 in adj[v0]:
            for v2 in adj[v1]:
                if v2 == v0 or v2 in adj[v0]:
                    continue
                for v3 in adj[v2]:
                    if v3 in (v0, v1) or v3 in adj[v0] or v3 in adj[v1]:
                        continue
                    for v4 in adj[v3]:
                        if v4 in (v0, v1, v2) or v4 in adj[v0] or v4 in adj[v1] or v4 in adj[v2]:
                            continue
                        for v5 in adj[v4]:
                            if v5 in (v0, v1, v2, v3):
                                continue
                            if v5 not in adj[v0]:
                                continue
                            if v5 in adj[v1] or v5 in adj[v2] or v5 in adj[v3]:
                                continue
                            cyc = (v0, v1, v2, v3, v4, v5)
                            key = min(min(tuple(cyc[(i + r) % 6] for i in range(6)),
                                          tuple(cyc[(r - i) % 6] for i in range(6)))
                                      for r in range(6))
                            if key in seen:
                                continue
                            seen.add(key)
                            yield cyc


def slot_of(adj, Z, i, j):
    """The unique vertex off Z adjacent to exactly Z[i] and Z[j] (or None)."""
    Zs = set(Z)
    out = [v for v in range(len(adj))
           if v not in Zs and set(Z) & adj[v] == {Z[i], Z[j]}]
    return out


print("=" * 74)
print("w133 round 8 -- Claim Q6.1: slot non-adjacency, mass caps, closure")
print("=" * 74)

# =================================================================== (A) POOL
print()
print("=== (A) POOL: exhaustive n<=7 C4-free table + explicit/greedy carriers ===")
pool = []
for n in range(6, 8):
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for mask in range(1 << len(pairs)):
        E = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        if len(E) < n - 1:
            continue
        adj = neighbours(E, n)
        if not connected(adj) or has_c4(adj):
            continue
        pool.append((f"small n={n}", n, adj))
print(f"  connected C4-free graphs on 6 <= n <= 7: {len(pool)}")

extra = []
n, E = hoffman_singleton()
extra.append(("HS", n, neighbours(E, n)))
extra.append(("HS+leaf", n + 1, neighbours(list(E) + [(0, n)], n + 1)))
for q in (5, 7):
    nn, EE = er_polarity(q)
    extra.append((f"ER_{q}", nn, neighbours(EE, nn)))
    extra.append((f"ER_{q}+leaf", nn + 1, neighbours(list(EE) + [(0, nn)], nn + 1)))
pet_E = ([(i, (i + 1) % 5) for i in range(5)] +
         [(5 + i, 5 + (i + 2) % 5) for i in range(5)] + [(i, 5 + i) for i in range(5)])
extra.append(("Petersen", 10, neighbours(pet_E, 10)))
rng = random.Random(20260818)
for seed in range(40):
    nn = rng.choice([9, 10, 11, 12, 13, 14, 15])
    adj = [set() for _ in range(nn)]
    prs = [(u, v) for u in range(nn) for v in range(u + 1, nn)]
    rng.shuffle(prs)
    for u, v in prs:
        if any(adj[v] & adj[w] for w in adj[u] if w != v):
            continue
        if any(adj[u] & adj[w] for w in adj[v] if w != u):
            continue
        adj[u].add(v); adj[v].add(u)
    if connected(adj):
        extra.append((f"rand{seed}", nn, adj))
print(f"  extra explicit/greedy carriers: {len(extra)}")

# ================================= (B) G32: only ANTIPODAL slots survive (C6)
# G32 (**C4-free** + P6-free; strengthens G15(b) from "cyclic distance 1 or 3" to
#   "3"): in such a graph containing an induced C6 Z = (v0..v5), every vertex off Z
#   has 0 or 2 neighbours on Z, and if 2 they are ANTIPODAL (cyclic distance 3).
#   NOTE (round-8 blind-judge correction): the pool below is filtered to C4-free
#   graphs, so this section tests the C4-FREE statement -- which is the true one.
#   The version WITHOUT C4-freeness is FALSE (C6 + w with N(w) = {v0,v2} is P6-free);
#   only the consecutive-pair half (G32') is hypothesis-free, tested in (B2).
#   [w ~ v_i, v_{i+1} gives the induced P6 (w, v_i, v_{i-1}, v_{i-2}, v_{i-3}, v_{i-4}).]
# Consequence in a C4-free graph: d(v_i) = 2 + [(v_i, v_{i+3}) slot occupied] and
#   N(v_i) is triangle-free, so a(v_i) = 2 + [(v_i, v_{i+3}) slot occupied].
print()
print("=== (B) G32: off-C6 vertices carry only ANTIPODAL pairs; mass identity ===")
n_c6 = n_g32 = n_mass = n_pq = 0
for nm, n, adj in pool + extra:
    if has_c4(adj) or not connected(adj):
        continue
    cyc = list(induced_c6s(adj))
    if not cyc:
        continue
    if n <= 60 and has_induced_pk(adj, 6):
        continue                      # (C6) fails -- not our class
    a = avec(adj)
    for Z in cyc:
        n_c6 += 1
        for v in range(n):
            if v in Z:
                continue
            S = adj[v] & set(Z)
            n_g32 += 1
            if not check(len(S) in (0, 2), f"{nm}: G15(a) at v={v}"):
                continue
            if len(S) == 2:
                i, j = sorted(Z.index(w) for w in S)
                cd = min((j - i) % 6, (i - j) % 6)
                check(cd == 3, f"{nm}: G32 non-antipodal slot at v={v} (cyc-dist {cd})")
        for r in range(6):
            for refl in (1, -1):
                ZZ = tuple(Z[(r + refl * i) % 6] for i in range(6))
                o = slot_of(adj, ZZ, 1, 4)
                check(len(o) <= 1, f"{nm}: antipodal slot has {len(o)} vertices")
                n_mass += 1
                check(a[ZZ[1]] == 2 + (1 if o else 0),
                      f"{nm}: G32 mass identity a(v1)=2+[antipodal slot] "
                      f"(got {a[ZZ[1]]}, slot={o})")
        if slot_of(adj, Z, 1, 4) and slot_of(adj, Z, 2, 5):
            n_pq += 1
print(f"  induced C6 in C4-free P6-free pool members : {n_c6}")
print(f"  off-C6 vertices classified (G32)           : {n_g32}")
print(f"  antipodal mass identity instances          : {n_mass}")
print(f"  two antipodal slots simultaneously occupied: {n_pq}")


# ======================= (B2) G32' : the UNCONDITIONAL half, and the counterexamples
# G32' (no C4-freeness, no other hypothesis): in a P6-free graph containing an
# induced C6, no outside vertex has EXACTLY TWO consecutive Z-neighbours.
# Also record the machine counterexamples that force the C4-free hypothesis on the
# full G32 (blind-judge finding, round 8).
print()
print("=== (B2) G32' unconditional half + the counterexamples forcing C4-free ===")
C6E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
ce = 0
for S in [(0, 2), (0, 1, 2), (0, 2, 4), (0, 1, 3)]:
    ad = neighbours(C6E + [(6, v) for v in S], 7)
    p6 = has_induced_pk(ad, 6)
    c4 = has_c4(ad)
    check(p6 is False and c4 is True,
          f"counterexample N(w)={S} is not (P6-free and non-C4-free)")
    ce += 1
    print(f"    C6 + w with N(w)={S}: P6-free={not p6}, C4-free={not c4}"
          f"  => violates G32-without-C4-free")
print(f"  {ce} machine counterexamples  =>  the C4-free hypothesis is NECESSARY")
tot = bad = 0
for k in (1, 2):
    vv = 6 + k
    others = [(i, j) for i in range(6, vv) for j in range(i + 1, vv)] + \
             [(v, z) for v in range(7, vv) for z in range(6)]
    for m in range(1 << len(others)):
        E2 = C6E + [(6, 0), (6, 1)] + [others[i] for i in range(len(others)) if m >> i & 1]
        ad = neighbours(E2, vv)
        if sorted(ad[6] & set(range(6))) != [0, 1]:
            continue
        tot += 1
        if not has_induced_pk(ad, 6):
            bad += 1
            check(False, "G32' violated: exactly-consecutive pair in a P6-free graph")
print(f"  G32' : {tot} frames whose vertex 6 has EXACTLY the consecutive pair (v0,v1),")
print(f"         with arbitrary edges elsewhere and NO C4-free filter; P6-free ones = {bad}")
tot2 = c4f = bad2 = 0
for k in (1, 2, 3):
    vv = 6 + k
    ex = [(i, j) for i in range(vv) for j in range(i + 1, vv) if not (i < 6 and j < 6)]
    for m in range(1 << len(ex)):
        ad = neighbours(C6E + [ex[i] for i in range(len(ex)) if m >> i & 1], vv)
        tot2 += 1
        if has_c4(ad):
            continue
        c4f += 1
        if has_induced_pk(ad, 6):
            continue
        for v in range(6, vv):
            S2 = sorted(ad[v] & set(range(6)))
            if len(S2) not in (0, 2):
                bad2 += 1; check(False, f"G32 violated (degree {S2})")
            elif len(S2) == 2 and min((S2[1] - S2[0]) % 6, (S2[0] - S2[1]) % 6) != 3:
                bad2 += 1; check(False, f"G32 violated (non-antipodal {S2})")
print(f"  G32 (C4-free version): {tot2} frames on C6 + <=3 vertices, {c4f} C4-free;")
print(f"         violations among the C4-free AND P6-free ones = {bad2}")

# ============================== (C) G33: consecutive-pair slots CANNOT EXIST
# In the Q6.1 frame N(u) = comp(u1) |_| {x}.  If comp(u1) = {u1, u1'} then
# (u1', u, x, y, z, u2) is an INDUCED P6 -- every non-edge is forced by the
# induced C6 plus G15(a) (u1' has exactly the two Z-neighbours u, u1).
# Hence under (C6):  u1' and u2' do NOT exist, N(u) = {u1, x}, N(z) = {u2, y},
# d(u) = d(z) = 2, and EVERY vertex with no Z-neighbour is at distance 3 from
# BOTH u and z -- so by Corollary G26.1 it has a-value 2 and is not a hub.
# Consequence:  H is contained in {u1, u2, x, y, A, B, P, Q}.
print()
print("=== (C) G34: every CONSECUTIVE-pair slot forces an induced P6 ===")
U, U1, U2, ZV, Y, X = 0, 1, 2, 3, 4, 5
U1P, U2P, A_, B_, P_, Q_ = 6, 7, 8, 9, 10, 11
Zc = (U, U1, U2, ZV, Y, X)
ZEDGES = [(U, U1), (U1, U2), (U2, ZV), (ZV, Y), (Y, X), (X, U)]
SLOTZ = {U1P: (U, U1), U2P: (ZV, U2), A_: (U1, U2), B_: (Y, X),
         P_: (U1, Y), Q_: (U2, X)}
ALL6 = [U1P, U2P, A_, B_, P_, Q_]


def build(occ, Wn, edgemask, extra_pairs):
    verts = list(Zc) + occ + list(range(100, 100 + Wn))
    idx = {v: i for i, v in enumerate(verts)}
    adj = [set() for _ in verts]
    for a, b in ZEDGES:
        adj[idx[a]].add(idx[b]); adj[idx[b]].add(idx[a])
    for s in occ:
        for t in SLOTZ[s]:
            adj[idx[s]].add(idx[t]); adj[idx[t]].add(idx[s])
    for i, (a, b) in enumerate(extra_pairs):
        if edgemask >> i & 1:
            adj[idx[a]].add(idx[b]); adj[idx[b]].add(idx[a])
    return adj, idx, verts


# every frame containing a CONSECUTIVE-pair slot carries the named induced P6,
# for EVERY edge pattern on the other five slots.
WIT = {U1P: (U1P, U, X, Y, ZV, U2), U2P: (U2P, ZV, Y, X, U, U1),
       A_: (A_, U1, U, X, Y, ZV), B_: (B_, X, U, U1, U2, ZV)}
n34 = 0
for tgt, w6 in WIT.items():
    others = [s for s in ALL6 if s != tgt]
    for sub in range(1 << 5):
        occ = [tgt] + [others[i] for i in range(5) if sub >> i & 1]
        free = [(a, b) for i, a in enumerate(occ) for b in occ[i + 1:]]
        for m in range(1 << len(free)):
            adj, idx, _ = build(occ, 0, m, free)
            if has_c4(adj):
                continue
            n34 += 1
            p6 = [idx[v] for v in w6]
            ok = all((p6[i + 1] in adj[p6[i]]) for i in range(5)) and \
                 all((p6[j] not in adj[p6[i]]) for i in range(6) for j in range(i + 2, 6))
            check(ok, f"G34: witness P6 for slot {tgt} is not induced")
            check(has_induced_pk(adj, 6), f"G34: frame with slot {tgt} is P6-free")
print(f"  C4-free frames carrying a consecutive-pair slot: {n34}")
print("  each carries the named induced P6  =>  u1', u2', A, B ALL die under (C6)")

# ======================= (D) exhaustive 10..12-vertex frame WITHOUT u1', u2'
# Z (6) + A,B,P,Q (any subset) + up to 2 W-vertices, ALL edge patterns among the
# non-Z vertices.  Keep the C4-free, connected, P6-free ones in which every
# W-vertex has a-value 2 (forced by Cor G26.1, since W-vertices sit at distance
# 3 from u).  Assert every round-8 claim.
print()
print("=== (D) exhaustive frame enumeration: Z + {P,Q} + <=3 W-vertices ===")
PAIRTAG = [(A_, B_, "A-B"), (A_, P_, "A-P"), (A_, Q_, "A-Q"),
           (B_, P_, "B-P"), (B_, Q_, "B-Q")]
kept = 0
cnt = {"a(P)<=3": 0, "a(Q)<=3": 0, "mass-id": 0, "N(w) in {P,Q}uW_P": 0,
       "|W_P|<=1": 0, "n<=9 (G35.2)": 0, "budget": 0}
maxmass = -1
maxwit = None
for sub in range(1 << 2):
    occ = [s for i, s in enumerate([P_, Q_]) if sub >> i & 1]
    for Wn in (0, 1, 2, 3):
        nodes = occ + list(range(100, 100 + Wn))
        free = [(a, b) for i, a in enumerate(nodes) for b in nodes[i + 1:]]
        for m in range(1 << len(free)):
            adj, idx, verts = build(occ, Wn, m, free)
            if has_c4(adj) or not connected(adj):
                continue
            if has_induced_pk(adj, 6):
                continue
            av = avec(adj)
            Wid = [idx[v] for v in range(100, 100 + Wn)]
            if any(av[w] != 2 for w in Wid):
                continue          # excluded by Cor G26.1 (W sits at distance 3)
            kept += 1
            cnt["mass-id"] += 1
            check(av[idx[U1]] == 2 + (P_ in occ), "D: a(u1)=2+[P]")
            check(av[idx[U2]] == 2 + (Q_ in occ), "D: a(u2)=2+[Q]")
            check(av[idx[X]] == 2 + (Q_ in occ), "D: a(x)=2+[Q]")
            check(av[idx[Y]] == 2 + (P_ in occ), "D: a(y)=2+[P]")
            if P_ in occ:
                cnt["a(P)<=3"] += 1
                check(av[idx[P_]] <= 3, "D: a(P)<=3")
                WP = [w for w in Wid if idx[P_] in adj[w]]
                cnt["|W_P|<=1"] += 1
                check(len(WP) <= 1, "D: |W_P|<=1")
                allowed = {idx[P_]} | ({idx[Q_]} if Q_ in occ else set()) | set(WP)
                for w in WP:
                    cnt["N(w) in {P,Q}uW_P"] += 1
                    check(adj[w] <= allowed, "D: N(w) not in {P,Q} u W_P")
            if Q_ in occ:
                cnt["a(Q)<=3"] += 1
                check(av[idx[Q_]] <= 3, "D: a(Q)<=3")
            # the closing budget, evaluated on the REAL frame
            H = [v for v in range(len(adj)) if av[v] >= 3]
            mass = sum(av[v] - 2 for v in H)
            cnt["budget"] += 1
            if mass > maxmass:
                maxmass, maxwit = mass, (sorted(occ), Wn, len(adj))
            cnt["n<=9 (G35.2)"] += 1
            check(len(adj) <= 9, f"D: G35.2 n = {len(adj)} > 9")
            check(mass <= 6, f"D: mass {mass} exceeds the proved cap 6")
            check(not (mass > len(adj)), f"D: mass {mass} > n {len(adj)}")
print(f"  admissible frames kept: {kept}")
for k, v in cnt.items():
    print(f"    {k:22s}: {v} instances")
print(f"  max Sigma_H(a-2) realised in any admissible frame: {maxmass} "
      f"(slots={maxwit[0] if maxwit else None}, |W|={maxwit[1] if maxwit else None},"
      f" n={maxwit[2] if maxwit else None})")

# ============================================== (E) the closing mass budget
print()
print("=== (E) the closing arithmetic (bounded sweep over the 4 slot flags) ===")
worst = -1
for A, B, P, Q in itertools.product([0, 1], repeat=4):
    # a(h)-2 caps proved in round 8 (u1', u2', h0 all non-existent by G34):
    if A or B:
        continue                  # G34: A and B cannot exist under (C6)
    mass = P + Q + Q + P          # u1,u2,x,y : a = 2+[P] / 2+[Q]
    mass += P * 1 + Q * 1         # P, Q      : a <= 3
    nmin = 6 + P + Q              # Z plus the occupied slots
    worst = max(worst, mass)
    check(not (mass > nmin), f"budget: mass {mass} > n_min {nmin} at {(A,B,P,Q)}")
print(f"  max achievable Sigma_H (a-2) over all slot patterns : {worst}")
print(f"  (**) requires Sigma_H (a-2) > n >= 6  ==>  mass >= 7 > 6 : IMPOSSIBLE")
print("  ==> the a(u)=a(z)=2 branch of RES(b) ^ (C6) is EMPTY  [Claim Q6.1]")

# ================================================================= (F) controls
print()
print("=== (F) controls: first failing step named (T12) ===")
for nm, n, adj in extra[:8]:
    D = alldist(adj)
    e, r = ecc_rad(D)
    a = avec(adj)
    why = []
    if r != 2:
        why.append(f"rad={r}!=2")
    if max(e) != 3:
        why.append(f"diam={max(e)}!=3")
    if sum(a) / n <= 3:
        why.append(f"l={sum(a)/n:.3f}<=3")
    if n <= 60 and has_induced_pk(adj, 6):
        why.append("has induced P6 -> (C6) fails")
    print(f"  {nm:12s} n={n:4d}  first failing step: {why[0] if why else 'NONE'}")

print()
print("=" * 74)
print(f"TOTAL ASSERT FAILURES: {FAIL}")
print("=" * 74)
sys.exit(1 if FAIL else 0)
