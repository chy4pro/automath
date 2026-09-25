#!/usr/bin/env python3
"""
Round 7 (owner-w133).  Adjudication of the three Q12 harvests
(problems/wowii/w133_TRIEND_qwen_{A,B,C}.md) + the owner's own closure of the
triangular-endpoint branch.

(A) ADJUDICATION.  Reproduce-or-refute, step by step, the three self-reported
    SOLVED-EMPTY claims.  Two of their load-bearing steps are refuted by explicit
    carriers; one flagged strengthening (Entry A: "an edge B_p-B_q gives a C4")
    is CONFIRMED and is adopted with the owner's own proof as G25(a).

(B) NEW Lemma G25 (owner, round 7) -- the unconditional parts, tested on every
    carrier (a(u)=1, d(u)=2, ecc(u)=3) of the round-6 pool:
      (a) NO edge between B_p and B_q          [strengthens G23(c): 3 -> 2]
      (b) a(h) <= 1 + |N(h) & D| for h in B_p u B_q   [strengthens G24(a) by 1]
      (c) ecc(b) = 2 for b in B_p  ==>  |B_q| <= |N(b) & D|   [two-step reach]
      (d) (h,y,c,q,u) is an induced P5 whenever h in B_p, y in N(h)&D, c a
          B_q-parent of y                                   [F9/G24(e') core]
      (e) general C4-free: a(v) >= ceil(d(v)/2), so d <= 2a and a >= 3 if d >= 5.

(C) The integer endgame: (eta_p - 1)(eta_q - 1) >= 7 + e_p + e_q with
    eta <= beta <= 4 has the unique solution eta_p = eta_q = 4, e_p = e_q = 0,
    which forces n = 27, |D| = 16 and a D-vertex of degree >= 5 -- a hub in the
    distance-3 layer, contradiction.  Verified by exhaustive arithmetic over the
    bounded parameter box (no graph search, no SAT).

Red lines: no SAT; the only exhaustive sweep is the n <= 7 labelled-graph table
(small-graph table, explicitly allowed); everything else is explicit
construction or greedy random maximal C4-free generation.
"""
import sys, itertools, random
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    connected, girth, hoffman_singleton,
                                    induced_path_from, alpha)
from w133_res3_search import er_polarity, has_triangle

FAIL = 0


def check(cond, msg):
    global FAIL
    if not cond:
        FAIL += 1
        print("  *** ASSERT FAILED: " + msg)
    return cond


def pack(name, n, E):
    adj = neighbours(E, n)
    D = alldist(adj)
    e, r = ecc_rad(D)
    a = avec(adj)
    return dict(name=name, n=n, adj=adj, D=D, ecc=e, rad=r, diam=max(e),
                a=a, S=sum(a), l=sum(a) / n, c4free=not has_c4(adj))


print("=" * 74)
print("w133 round 7 -- triangular-endpoint branch: adjudication + closure")
print("=" * 74)

# ------------------------------------------------------------------ POOL
print()
print("=== POOL (identical to round 6: exhaustive n<=7 table + big carriers) ===")
c4f_pool = []
for n in range(2, 8):
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for mask in range(1 << len(pairs)):
        E = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        if len(E) < n - 1:
            continue
        adj = neighbours(E, n)
        if not connected(adj) or has_c4(adj):
            continue
        c4f_pool.append((n, E, adj))
print(f"  connected C4-free graphs on n <= 7: {len(c4f_pool)}")

extra = []
n, E = hoffman_singleton()
extra.append(("HS", n, list(E)))
extra.append(("HS+leaf", n + 1, list(E) + [(0, n)]))
for q in (5, 7):
    nn, EE = er_polarity(q)
    extra.append((f"ER_{q}", nn, list(EE)))
    extra.append((f"ER_{q}+leaf", nn + 1, list(EE) + [(0, nn)]))
pet = (10, [(i, (i + 1) % 5) for i in range(5)] +
       [(5 + i, 5 + (i + 2) % 5) for i in range(5)] + [(i, 5 + i) for i in range(5)])
extra.append(("Petersen", pet[0], pet[1]))
rng = random.Random(20260818)
for seed in range(30):
    nn = rng.choice([9, 10, 11, 12, 13, 14])
    adj = [set() for _ in range(nn)]
    prs = [(u, v) for u in range(nn) for v in range(u + 1, nn)]
    rng.shuffle(prs)
    EE = []
    for u, v in prs:
        if any(adj[v] & adj[w] for w in adj[u] if w != v):
            continue
        if any(adj[u] & adj[w] for w in adj[v] if w != u):
            continue
        adj[u].add(v); adj[v].add(u); EE.append((u, v))
    extra.append((f"rand{seed}", nn, EE))
print(f"  extra explicit/greedy carriers: {len(extra)}")

# ============================================================ (B) + (A) carriers
print()
print("=== (B) Lemma G25 (NEW, unconditional) on every triangular-endpoint carrier ===")
carriers = [(f"small n={n}", n, E) for n, E, adj in c4f_pool] + \
           [(nm, n, E) for nm, n, E in extra]

inst = 0
n_g25a = n_g25b = n_g25c = n_g25d = 0
single_parent_witness = None    # refutes Entry A's "|D| <= 9" injection step
slot3_witness = None            # a carrier where the old G23(c) bound 3 is loose
for nm, n, E in carriers:
    adj = neighbours(E, n)
    if not connected(adj) or has_c4(adj):
        continue
    Dm = alldist(adj)
    ecc, r = ecc_rad(Dm)
    a = avec(adj)
    # (e) general C4-free degree/independence fact, checked on every vertex
    for v in range(n):
        d = len(adj[v])
        check(a[v] >= -(-d // 2), f"{nm}: a(v) >= ceil(d/2) at v={v}")
        check(d <= 2 * a[v], f"{nm}: d(v) <= 2 a(v) at v={v}")
        if a[v] == 1:
            check(d <= 2, f"{nm}: a=1 => d<=2 at v={v}")
        if a[v] <= 2:
            check(d <= 4, f"{nm}: non-hub degree <= 4 at v={v}")
    for u in range(n):
        if a[u] != 1 or ecc[u] != 3 or len(adj[u]) != 2:
            continue
        p, q = sorted(adj[u])
        if q not in adj[p]:
            continue
        inst += 1
        Bp = adj[p] - {u, q}
        Bq = adj[q] - {u, p}
        Dl = {v for v in range(n) if Dm[u][v] == 3}
        # ---- G25(a): NO edge between B_p and B_q  (Entry A's flagged strengthening)
        n_g25a += 1
        for h in Bp:
            check(not (adj[h] & Bq), f"{nm}: G25(a) edge B_p-B_q at h={h}")
        slots = {p, q} | Bp | Bq
        for h in Bp | Bq:
            check(len(adj[h] & slots) <= 2,
                  f"{nm}: G25(a') |N(h) & slots| <= 2 at h={h}")
            if slot3_witness is None and len(adj[h] & slots) == 2:
                slot3_witness = (nm, u, h)
        # ---- G25(b): a(h) <= 1 + |N(h) & D|
        for h in Bp | Bq:
            n_g25b += 1
            check(adj[h] <= ({p if h in Bp else q} | (Bp if h in Bp else Bq) | Dl),
                  f"{nm}: G25(b) N(h) confined at h={h}")
            check(a[h] <= 1 + len(adj[h] & Dl),
                  f"{nm}: G25(b) a(h) <= 1+|N(h)&D| at h={h}")
        # ---- G25(c): two-step reach.  ecc(b)=2 => |B_q| <= |N(b) & D|
        for b in Bp:
            if ecc[b] == 2:
                n_g25c += 1
                check(len(Bq) <= len(adj[b] & Dl),
                      f"{nm}: G25(c) |B_q|<=|N(b)&D| at b={b}")
        for c in Bq:
            if ecc[c] == 2:
                n_g25c += 1
                check(len(Bp) <= len(adj[c] & Dl),
                      f"{nm}: G25(c) |B_p|<=|N(c)&D| at c={c}")
        # ---- G25(d): the induced P5 (h,y,c,q,u)
        for h in Bp:
            for y in adj[h] & Dl:
                for c in adj[y] & Bq:
                    n_g25d += 1
                    P = [h, y, c, q, u]
                    ok = all((P[i] in adj[P[i + 1]]) for i in range(4)) and \
                         all((P[i] not in adj[P[j]])
                             for i in range(5) for j in range(i + 2, 5))
                    check(ok, f"{nm}: G25(d) (h,y,c,q,u) induced P5 at {P}")
        # ---- data for the Entry-A refutation: a D-vertex with only ONE parent
        for y in Dl:
            check(len(adj[y] & Bp) <= 1 and len(adj[y] & Bq) <= 1,
                  f"{nm}: <=1 parent per side at y={y}")
            if single_parent_witness is None and bool(adj[y] & Bp) != bool(adj[y] & Bq):
                single_parent_witness = (nm, n, E, u, y, sorted(Bp), sorted(Bq))

print(f"  triangular-endpoint carriers (a(u)=1, d(u)=2, ecc(u)=3): {inst}")
print(f"  G25(a) no-B_p-B_q-edge instances : {n_g25a}")
print(f"  G25(b) a(h) <= 1+|N(h)&D|        : {n_g25b}")
print(f"  G25(c) |B_q| <= |N(b)&D|         : {n_g25c}")
print(f"  G25(d) induced-P5 instances      : {n_g25d}")
check(inst >= 20, "G25 must be tested non-vacuously")
check(n_g25b >= 20 and n_g25c >= 1, "G25(b),(c) must be non-vacuous")

# ================================================================= (A)
print()
print("=== (A) ADJUDICATION of the three Q12 harvests ===")

print()
print("  A-1  Entry A, flagged strengthening 'any edge B_p-B_q gives a 4-cycle':")
print("       CONFIRMED (p,h,c,q is a 4-cycle: p~h, h~c, c~q, q~p).")
n4, E4 = 4, [(0, 1), (1, 2), (2, 3), (3, 0)]      # p,h,c,q
f4 = pack("p-h-c-q", n4, E4)
check(not f4['c4free'], "the configuration p~h~c~q~p must be a C4")
print(f"       explicit: p-h-c-q-p on 4 vertices, C4-free={f4['c4free']}")
print("       => adopted as owner's Lemma G25(a) with the owner's own proof;")
print("          it strengthens the brief's own F7(c) (which said 'at most one').")

print()
print("  A-2  Entry A, Case I step 'every D-vertex has one parent on each side and")
print("       injects into B_p x B_q, so |D| <= 9':  REFUTED as stated.")
if single_parent_witness:
    nm, n, E, u, y, Bp, Bq = single_parent_witness
    print(f"       witness {nm}: u={u}, B_p={Bp}, B_q={Bq}, y={y} in D has ONE parent")
    check(True, "single-parent witness found")
else:
    check(False, "expected a carrier with a single-parent D-vertex")
print("       (injectivity is available only on the two-parent set D2 = G24(d);")
print("        the summary's |D| <= 9 and 'hub excess <= |D|-1' do not follow from")
print("        the facts supplied.  Conclusion right, delivered proof NOT adopted.)")

print()
print("  A-3  Entry B is built on the F9 / G24(e') trigger (a hub of degree >= 6")
print("       inside B_p u B_q).  That trigger is VACUOUS: by G25(a) N(h) & B_q = 0,")
print("       so by G25(d)+G22 every D-child of such an h has no B_q-parent, and")
print("       then G25(c) forces |B_q| = 0, killed by G24(b).  Entry B is therefore")
print("       superseded, not adopted (its case analysis is unverifiable anyway:")
print("       the artifact is a summary, not a transcript).")

print()
print("  A-4  Entry C's accounting device ('every addition leaves S = sum(a-3)")
print("       unchanged or decreases it') is REFUTED as a general C4-free principle:")
for nm, n, E in [("HS", ) + hoffman_singleton(), ("ER_5", ) + er_polarity(5),
                 ("ER_7", ) + er_polarity(7)]:
    f = pack(nm, n, E)
    S = sum(x - 3 for x in f['a'])
    c6 = any(induced_path_from(f['adj'], s, 6) for s in range(n))
    print(f"       {nm:<6} n={n:<4} C4-free={f['c4free']} l={f['l']:.3f} "
          f"S=sum(a-3)={S:+d}  (induced P6 present={c6})")
    check(f['c4free'] and S > 0, f"{nm} must be a C4-free graph with S>0")
print("       A single hub with a(h)=5 contributes +2 to S; the claim can only hold")
print("       through branch-specific structure, which the artifact does not exhibit")
print("       (it also never treats the three unbounded-degree slots the brief named,")
print("        and its 'maximum' witness Z u {v3,v4} has 8 vertices, below n >= 14).")
print("       => Claim Q6.1 STAYS UNVERIFIED.  Entry C not adopted.")

print()
print("  A-5  Shared-hidden-assumption sweep (methodology multi-tab clause).")
print("       Common inputs of the three tabs = PART 1-2 of prompts/w133_r6_TRIEND_qwen.md")
print("       (F1-F9), all owner-proved.  Re-checked here: F1/F2 arithmetic, F3, F7(a)-(e),")
print("       F8(a)-(d) (= G24(a),(c),(d)) and F6/G22 were re-verified in round 6 and above.")
print("       ONE shared slack found: F7(c)/F8/F9 are stated with '<= 1 neighbour in B_q',")
print("       while the truth is ZERO (G25(a)).  It is a weakening, not an error, so no")
print("       tab's conclusion is invalidated by it -- but it is exactly the assumption")
print("       whose correction collapses the whole branch.  Entry A caught it; B and C")
print("       inherited the slack.  No other shared assumption is load-bearing.")

# ================================================================= (C)
print()
print("=== (C) The owner's closure of the branch: the integer endgame ===")
print("  Chain (all steps proved in draft 18.1): G25(a),(b) + F1 mass + injectivity")
print("  give  (eta_p-1)(eta_q-1) >= 7 + e_p + e_q  with eta_x = |H & B_x|,")
print("  e_x = #edges inside B_x.  G25(c)+(d)+G22 give hub degree <= 5 in B_p u B_q,")
print("  hence beta_q <= delta_b <= 4 and beta_p <= 4, so eta_p, eta_q <= 4.")
sols = [(ep, eq, xp, xq)
        for ep in range(0, 5) for eq in range(0, 5)
        for xp in range(0, 5) for xq in range(0, 5)
        if (ep - 1) * (eq - 1) >= 7 + xp + xq]
print(f"  exhaustive integer sweep over 0<=eta_p,eta_q<=4, 0<=e_p,e_q<=4: "
      f"{len(sols)} solution(s): {sols}")
check(all(s[0] == 4 and s[1] == 4 for s in sols) and sols,
      "every solution must have eta_p = eta_q = 4")
print("  => eta_p = eta_q = 4 in EVERY solution (e_p+e_q <= 2 still free here;")
print("     it is pinned to 0 by the separate degree step below).")
print("  => beta_p = eta_p = 4, beta_q = eta_q = 4: every B-vertex is a hub,")
print("     d(p) = d(q) = 6, a(p) = a(q) = 5.")
print("  degree step: for a hub b in B_p, G25(c) gives delta_b >= beta_q = 4 and")
print("     G25(c)+(d)+G22 give d(b) <= 5, while d(b) = 1 + eps_b + delta_b:")
deg_sols = [(eps, dlt) for eps in range(0, 2) for dlt in range(0, 6)
            if dlt >= 4 and 1 + eps + dlt <= 5]
print(f"     integer sweep over (eps_b, delta_b): {deg_sols}")
check(deg_sols == [(0, 4)], "the degree step must force eps_b = 0, delta_b = 4")
print("     => eps_b = 0, delta_b = 4, d(b) = 5 for every b in B_p u B_q, hence")
print("        e_p = e_q = 0 (all of B_p, B_q are hubs since beta = eta).")
beta_p = beta_q = 4
Dsize = beta_p * 4          # sum of delta_b over B_p = #edges(B_p,D) = |D|
n_forced = 3 + beta_p + beta_q + Dsize
print(f"     |D| = sum_b delta_b = {Dsize}, n = 3+{beta_p}+{beta_q}+{Dsize} = {n_forced}")
check(n_forced == 27, "the forced configuration must have n = 27")
print("     p,q are hubs => ecc = 2 => every y in D has BOTH parents; injectivity")
print("     then makes y -> (b,c) a BIJECTION D -> B_p x B_q.")
check(Dsize == beta_p * beta_q, "D must biject onto B_p x B_q")
print("  Final step: fix y in D with B_p-parent b1.  Each of the other 3 hubs")
print("  b2 in B_p has ecc(b2)=2, and (G25(a) + e_p=0) its only possible common")
print("  neighbour with y lies in N(y) & D, with a UNIQUE B_p-parent b2 -- so y")
print("  needs >= 3 distinct D-neighbours:")
dy = 2 + (beta_p - 1)
print(f"     d(y) >= 2 + {beta_p - 1} = {dy}  =>  a(y) >= ceil({dy}/2) = {-(-dy // 2)} >= 3")
check(-(-dy // 2) >= 3, "d(y)>=5 must force a(y)>=3 in a C4-free graph")
print("     so y is a HUB at distance 3 from u, contradicting H <= ball_2(u) (R3b).")
print("  => THE TRIANGULAR-ENDPOINT BRANCH IS EMPTY.  D6a and D6b both closed.")
print("  Note: the chain never uses the branch hypothesis (TRI) itself, only the")
print("  existence of ONE vertex u with a(u)=1, d(u)=2, ecc(u)=3.  Hence the")
print("  stronger statement: in RES(b) ^ (C6) NO vertex of eccentricity 3 has a=1,")
print("  i.e. EVERY distance-3 pair has both a-values equal to 2.")

# sanity: the controls must not be killed by the new lemmas
print()
print("=== (D) Control-case audit (the new chain must not 'prove' these impossible) ===")
for nm, n, E in [("Petersen", ) + (pet[0], pet[1]), ("HS", ) + hoffman_singleton(),
                 ("HS+leaf", extra[1][1], extra[1][2])]:
    f = pack(nm, n, E)
    a = f['a']
    cars = [v for v in range(n) if a[v] == 1 and f['ecc'][v] == 3 and len(f['adj'][v]) == 2]
    print(f"  {nm:<9} n={n:<3} diam={f['diam']} rad={f['rad']} l={f['l']:.3f} "
          f"triangular-endpoint carriers={len(cars)}")
print("  Petersen/HS: diam 2, so no distance-3 pair exists -- the chain never starts")
print("  (first failing step = the setup, exactly as required).  HS+leaf has diam 3")
print("  and l>3 but its ecc-3 vertex is a LEAF (a=1, d=1), excluded by G19/F4, and")
print("  it violates (R3b) anyway (it is the round-5 RES(a)-witness).")
hsl = pack("HS+leaf", extra[1][1], extra[1][2])
leafs = [v for v in range(hsl['n']) if hsl['a'][v] == 1 and hsl['ecc'][v] == 3]
check(all(len(hsl['adj'][v]) == 1 for v in leafs),
      "HS+leaf's a=1 ecc-3 vertices must all be leaves (so G19 excludes them)")
print(f"  HS+leaf a=1 ecc-3 vertices: {leafs}, degrees "
      f"{[len(hsl['adj'][v]) for v in leafs]} => all leaves, G19 applies.")

# ================================================================= (E)
print()
print("=== (E) Claim Q6.1 (the LAST pocket-1 item): the round-7 narrowing ===")
print("  Frame: induced C6 Z = (u,u1,u2,z,y,x) at positions 0..5 (G13), slots of G21:")
print("  u1',u2' (partners), A=(u1,u2), B=(y,x), P=(u1,y), Q=(u2,x), h0=(no Z-nbr).")

# explicit slot configuration: Z + every slot, as a labelled graph
LAB = dict(u=0, u1=1, u2=2, z=3, y=4, x=5, u1p=6, u2p=7, A=8, B=9, P=10, Q=11, h0=12)
ZE = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
SLOT = {'u1p': ('u', 'u1'), 'u2p': ('z', 'u2'), 'A': ('u1', 'u2'), 'B': ('y', 'x'),
        'P': ('u1', 'y'), 'Q': ('u2', 'x')}


def cfg(present, extra=()):
    """Z plus the named slots (each joined to its two Z-neighbours), plus extra edges."""
    E = list(ZE)
    for s in present:
        for t in SLOT[s]:
            E.append((LAB[s], LAB[t]))
    E += [(LAB[a], LAB[b]) for a, b in extra]
    return len(LAB), E


def induced_path(adj, P):
    return all(P[i] in adj[P[i + 1]] for i in range(len(P) - 1)) and \
        all(P[i] not in adj[P[j]] for i in range(len(P)) for j in range(i + 2, len(P)))


# --- E1: the C6 itself is induced and C4-free
adjZ = neighbours(ZE, 6)
check(not has_c4(adjZ) and all(len(adjZ[v]) == 2 for v in range(6)), "Z is an induced C6")
print("  E1  Z is an induced, C4-free 6-cycle.")

# --- E2 (NEW G27): h0 has degree <= 5 -- the 9th of G21's 11 slots gets bounded
n_, E_ = cfg(['u1p'], extra=[('h0', 'u1p')])
adj_ = neighbours(E_, n_)
P5 = [LAB['h0'], LAB['u1p'], LAB['u'], LAB['x'], LAB['y']]
check(induced_path(adj_, P5), "G27: (h0,u1',u,x,y) must be an induced P5")
check(not has_c4(adj_), "the h0/u1' configuration must itself be C4-free")
print("  E2  G27: (h0,u1',u,x,y) is an induced P5 with endpoint h0  =>  d(h0) <= 5 by G22.")
print("      (G21(iv) forces h0 ~ u1'; u1' has no other Z-neighbour by G15(b).)")
print("      => 9 of G21's 11 slots are now degree-bounded (was 8, Cor G22.1).")

# --- E3 (NEW G29): the P5s that bound P unless P is adjacent to A, B, Q
for tgt, path in [('B', ['P', 'u1', 'u', 'x', 'B']),
                  ('Q', ['P', 'u1', 'u', 'x', 'Q']),
                  ('A', ['P', 'y', 'z', 'u2', 'A'])]:
    n_, E_ = cfg(['P', tgt])
    adj_ = neighbours(E_, n_)
    check(induced_path(adj_, [LAB[v] for v in path]),
          f"G29: {tuple(path)} must be an induced P5")
    check(not has_c4(adj_), f"the P/{tgt} configuration must be C4-free")
print("  E3  G29: (P,u1,u,x,B), (P,u1,u,x,Q) and (P,y,z,u2,A) are induced P5's with")
print("      endpoint P, so d(P) >= 6 forces P ~ A, P ~ B and P ~ Q (whichever exist).")

# --- E4 (NEW G29 cont.): the C4s that make those adjacencies mutually exclusive
for pair, apex in [(('A', 'Q'), 'u2'), (('B', 'Q'), 'x')]:
    n_, E_ = cfg(['P', pair[0], pair[1]],
                 extra=[('P', pair[0]), ('P', pair[1])])
    adj_ = neighbours(E_, n_)
    check(has_c4(adj_), f"P~{pair[0]} and P~{pair[1]} must create a C4 through {apex}")
for s, apex in [('u1p', 'u'), ('u2p', 'z')]:
    n_, E_ = cfg(['P', s], extra=[('P', s)])
    check(has_c4(neighbours(E_, n_)), f"P ~ {s} must create a C4 through {apex}")
for s, apex in [('u1p', 'u'), ('u2p', 'z')]:
    n_, E_ = cfg(['Q', s], extra=[('Q', s)])
    check(has_c4(neighbours(E_, n_)), f"Q ~ {s} must create a C4 through {apex}")
print("  E4  C4-freeness then gives: P~A and P~Q are incompatible (apex u2), P~B and")
print("      P~Q are incompatible (apex x), and P,Q are never adjacent to u1' or u2'.")
print("      => d(P) >= 6 AND Q present  ==>  slots A and B are EMPTY, and then")
print("         N(x) = {u,y,Q}, N(y) = {z,x,P}, so a(x) = a(y) = 3 (not 4).")

# --- E5: no leaves at all (a=1 => ecc<=2 by G26; a leaf has ecc = 1 + ecc(nbr) = 3)
leafcheck = 0
for nm, n, E in carriers[:4000]:
    adj = neighbours(E, n)
    if not connected(adj) or n < 3:
        continue
    Dm = alldist(adj)
    ecc, _ = ecc_rad(Dm)
    for v in range(n):
        if len(adj[v]) == 1:
            leafcheck += 1
            w = next(iter(adj[v]))
            check(ecc[v] == 1 + ecc[w], f"{nm}: leaf ecc = 1 + nbr ecc at v={v}")
print(f"  E5  leaf identity ecc(leaf) = 1 + ecc(neighbour): {leafcheck} instances, 0 failures")
print("      With G26 (a=1 => ecc <= 2) and rad = 2 this forces: RES(b) ^ (C6) has NO")
print("      LEAF at all -- min degree >= 2 -- and every a=1 vertex w has ecc(w) = 2,")
print("      so G20 at w gives the rigid identity n = d(P) + d(w') - 1 for its triangle.")
# --- E6 (NEW G30): P's off-cycle neighbours are bounded => ALL 11 slots bounded
n_, E_ = cfg(['P'], extra=[])
n_ = n_ + 1
W0 = n_ - 1                                   # a fresh vertex w with N(w) ∋ P
E_ = E_ + [(W0, LAB['P'])]
adj_ = neighbours(E_, n_)
check(induced_path(adj_, [W0, LAB['P'], LAB['u1'], LAB['u'], LAB['x']]),
      "G30: (w,P,u1,u,x) must be an induced P5 for any off-Z neighbour w of P")
check(not has_c4(adj_), "the w/P configuration must be C4-free")
# and if w has a neighbour outside N(P) u N(u1) u N(u) u N(x), an induced P6 appears
n2 = n_ + 1
v0 = n2 - 1
adj2 = neighbours(E_ + [(W0, v0)], n2)
check(induced_path(adj2, [v0, W0, LAB['P'], LAB['u1'], LAB['u'], LAB['x']]),
      "G30: such an escaping neighbour must create an induced P6")
print("  E6  G30: (w,P,u1,u,x) is an induced P5 for every off-Z neighbour w of P, and a")
print("      neighbour of w outside N(P) u N(u1) u N(u) u N(x) extends it to an induced")
print("      P6 -- forbidden by (C6).  Hence N(w) is confined to {P,u1',A,B,Q} u W, at")
print("      most one w per apex (C4 through P), and N(P) induces a matching, so every")
print("      remaining w has d(w) = 2 with N(w) = {P,w'} a clique: a(w) = 1.  By G26")
print("      ecc(w) = 2, so w needs a neighbour in N(u) = {u1,u1',x}; but w' is off-Z")
print("      and u1' is not.  Contradiction => |W| <= 3, and |W| <= 2 when Q exists.")
print("  => **d(P), d(Q) <= 7, and <= 5 whenever both slots are occupied**: ALL ELEVEN")
print("     G21 SLOTS ARE NOW DEGREE-BOUNDED.  The mass budget sum_H (a-2) is therefore")
print("     bounded, and Claim Q6.1 collapses to a FINITE WINDOW:")
print("  E7  G31 (slot-wise a-caps, from the forced triangles inside each slot's")
print("      neighbourhood): d(u1) = 2+[u1']+[A]+[P] while t(u1) >= [u1']+[A], so")
print("      a(u1) <= 2 + [P]; symmetrically a(u2) <= 2+[Q], a(x) <= 2+[Q],")
print("      a(y) <= 2+[P]; and u1',u2',A,B each carry a forced triangle (u~u1, z~u2,")
print("      u1~u2, y~x respectively) so their a <= d-1 <= 4.")


def budget(p, q):
    """sum_H (a-2) cap as a function of which opposite slots are occupied."""
    cap = {'u1': p, 'u2': q, 'x': q, 'y': p,          # G31
           'u1p': 2, 'u2p': 2, 'A': 2, 'B': 2,        # a <= d-1 <= 4
           'h0': 3}                                   # G27: d <= 5
    cap['P'] = (3 if q else 5) * p                    # G30: d(P) <= 5 if Q present
    cap['Q'] = (3 if p else 5) * q
    return sum(cap.values())


for p, q, nm in [(1, 1, "both P,Q present"), (1, 0, "P only"),
                 (0, 1, "Q only"), (0, 0, "neither")]:
    b = budget(p, q)
    print(f"     {nm:<18}: sum_H(a-2) <= {b:>2}  => n <= {b - 1}")
check(budget(1, 1) == 21 and budget(1, 0) == 18 and budget(0, 0) == 11,
      "mass budgets must be 21 / 18 / 11")
print("     'neither' also gives H <= {u1',u2',A,B,h0}, i.e. |H| <= 5, contradicting")
print("     |H| >= 6 (G18.1) -- so AT LEAST ONE opposite slot is occupied, and with")
print("     n >= 14 (no C4-free graph with l > 3 on n <= 13):")
print("     **14 <= n <= 20** (both) / **14 <= n <= 17** (exactly one).")
check(budget(0, 0) < 14, "the 'neither' case must already contradict n >= 14")
print("  E8  G20 at x (if x is a hub, ecc(x) = 2): n = 1 + d(u)+d(y)+d(B)+d(Q) - 2t(x);")
print("      with B absent this is n <= 1+3+3+5 = 12 < 14, so x hub => B present;")
print("      symmetrically y hub => B present.")
check(1 + 3 + 3 + 5 < 14, "the B-absent count must fall below n >= 14")
print("  => Claim Q6.1 is no longer an open class: it is a bounded, explicitly listed")
print("     configuration problem with 14 <= n <= 20.  Round-8 target (NOT closed).")

print()
print(f"TOTAL ASSERT FAILURES: {FAIL}")
sys.exit(1 if FAIL else 0)
