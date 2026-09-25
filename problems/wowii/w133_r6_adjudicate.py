#!/usr/bin/env python3
"""
Round 6 (owner-w133).  Three jobs, all assert-style, labels EXACTLY as in draft
notes/proofs/wowii133_draft.md (planner round-5 minor correction: script labels
must match draft numbering).

(A) ADJUDICATION of the Qwen S3 harvest problems/wowii/w133_S3_G12_qwen.md:
    claimed GAP on joint G12-J1 ("triangle-free + C4-free + diam 2 => girth 5 +
    regular, by Hoffman-Singleton").  Reproduce the star counterexample, then
    test the repair the owner adopts (Lemma G12.1, NOT Qwen's longer route).

(B) NEW unconditional Lemma G22 (owner, round 6):
        C4-free + no induced P6  ==>  every endpoint of an induced P5 has
        degree <= 5.
    Tightness witnesses: friendship graph F_k (no induced P5 at all, unbounded
    degree) and the C4-free P6-free graphs of the exhaustive n <= 7 pool.

(C) NEW Lemma G23 (owner, round 6): ball structure at a triangular diameter
    endpoint (a(u) = 1 branch, the single residual left by the round-6
    adjudication of problems/wowii/w133_RES_qwen_r5.md), plus the refutation of
    Tab B's claimed "minimal example".

Red lines: no SAT; the only exhaustive sweep is over all labelled graphs on
n <= 7 vertices (small-graph table, explicitly allowed); everything else is an
explicit construction.
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
                a=a, S=sum(a), l=sum(a) / n, c4free=not has_c4(adj),
                tri=has_triangle(adj), g=girth(adj))


def star(m):
    return m + 1, [(0, i) for i in range(1, m + 1)]


def friendship(k):
    """k triangles glued at vertex 0: C4-free, no induced P5, degree 2k."""
    E = []
    for i in range(k):
        u, v = 1 + 2 * i, 2 + 2 * i
        E += [(0, u), (0, v), (u, v)]
    return 2 * k + 1, E


def has_induced_path_on(adj, k):
    """exact: does the graph contain an induced path on k vertices?"""
    return any(induced_path_from(adj, s, k) for s in range(len(adj)))


def p5_endpoints(adj):
    return [s for s in range(len(adj)) if induced_path_from(adj, s, 5)]


# ================================================================= (A)
print("=== (A) ADJUDICATION: Qwen's claimed GAP on joint G12-J1 ===")
print("  literal claim under review (draft 13.1 Step 1, as written):")
print("    triangle-free + C4-free + diam 2  ==>  girth 5, Moore, k in {2,3,7,57}")
for m in (2, 3, 5, 9, 20):
    n, E = star(m)
    f = pack(f"K_1,{m}", n, E)
    degs = sorted(len(f['adj'][v]) for v in range(n))
    ok = (not f['tri']) and f['c4free'] and f['diam'] == 2 and f['g'] > 10 ** 8
    print(f"  K_1,{m:<2} n={n:<3} tri={f['tri']} C4free={f['c4free']} diam={f['diam']} "
          f"girth={'inf' if f['g'] > 10**8 else f['g']} regular={degs[0]==degs[-1]} "
          f"l={f['l']:.3f}")
    check(ok, f"K_1,{m} must satisfy the hypotheses and have NO cycle")
    check(f['l'] < 2, f"K_1,{m} must have l < 2 (so l>3 excludes it)")
print("  => the literal step is FALSE as stated: stars satisfy the hypotheses,")
print("     are not regular and contain no 5-cycle.  QWEN'S GAP IS REAL.")

print()
print("  Repair actually adopted (Lemma G12.1, owner's route, 2 lines):")
print("    (i) connected + acyclic + diam 2 => star => l < 2, killed by l > 3;")
print("    (ii) a graph WITH a cycle has girth <= 2*diam+1 = 5, and triangle-free")
print("         + C4-free gives girth >= 5, hence girth = 5 exactly;")
print("    (iii) diam 2 + girth 5 => Moore (Hoffman-Singleton), k in {2,3,7,57}.")

# (A2) exhaustive n <= 7: the whole hypothesis class of Step 1
print("  exhaustive check over ALL labelled graphs on n <= 7 vertices:")
tf_c4f_d2 = []          # triangle-free, C4-free, connected, diam 2
c4f_pool = []           # connected C4-free (any) -- reused by (B)
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
        D = alldist(adj)
        e, r = ecc_rad(D)
        if max(e) == 2 and not has_triangle(adj):
            tf_c4f_d2.append((n, E, adj))
print(f"    connected C4-free graphs found: {len(c4f_pool)}")
print(f"    of these triangle-free with diam 2: {len(tf_c4f_d2)}")
shapes = {}
for n, E, adj in tf_c4f_d2:
    g = girth(adj)
    degs = sorted(len(adj[v]) for v in range(n))
    kind = "star" if g > 10 ** 8 else f"girth{g}"
    shapes[kind] = shapes.get(kind, 0) + 1
    # Lemma G12.1 dichotomy
    if g > 10 ** 8:
        check(degs == [1] * (n - 1) + [n - 1], f"acyclic member on n={n} must be a star")
        check(sum(avec(adj)) / n < 2, f"star on n={n} must have l < 2")
    else:
        check(g == 5, f"member with a cycle on n={n} must have girth 5 (got {g})")
        check(degs[0] == degs[-1], f"girth-5 member on n={n} must be regular")
        check(degs[-1] in (2, 3, 7, 57), f"Moore degree on n={n}: {degs[-1]}")
print(f"    shape census: {shapes}   (only stars and girth-5 Moore graphs)")
for name, (n, E) in [("Petersen", (10, [(i, (i + 1) % 5) for i in range(5)] +
                                   [(5 + i, 5 + (i + 2) % 5) for i in range(5)] +
                                   [(i, 5 + i) for i in range(5)])),
                     ("HS", hoffman_singleton())]:
    f = pack(name, n, E)
    check(f['g'] == 5 and not f['tri'] and f['c4free'] and f['diam'] == 2,
          f"{name} is a girth-5 diam-2 C4-free triangle-free control")
    k = len(f['adj'][0])
    check(all(len(f['adj'][v]) == k for v in range(n)) and k in (2, 3, 7, 57),
          f"{name} Moore degree")
    print(f"    control {name:<9} n={n:<3} girth={f['g']} k={k} l={f['l']:.3f} "
          f"(l>3? {f['l'] > 3})")
print("  => after G12.1 the l>3 hypothesis leaves exactly k in {7,57}: G12 Step 1 REPAIRED.")

# ================================================================= (B)
print()
print("=== (B) Lemma G22 (NEW, unconditional): C4-free + P6-free =>")
print("        every endpoint of an induced P5 has degree <= 5 ===")
tested = 0
pool_b = []
for n, E, adj in c4f_pool:
    if has_induced_path_on(adj, 6):
        continue
    pool_b.append((n, E, adj))
    for s in p5_endpoints(adj):
        tested += 1
        check(len(adj[s]) <= 5, f"G22 on n={n} E={E} at s={s}: deg={len(adj[s])}")
print(f"  exhaustive n<=7 C4-free P6-free graphs: {len(pool_b)};"
      f" induced-P5 endpoints tested: {tested}")
maxdeg_seen = max((len(adj[s]) for n, E, adj in pool_b for s in p5_endpoints(adj)),
                  default=0)
print(f"  max degree over all tested P5-endpoints: {maxdeg_seen} (bound 5)")

def rand_c4free_p6free(n, seed):
    """greedy random edge-maximal graph that stays C4-free AND induced-P6-free;
       gives high-degree carriers for G22 (the n<=7 table only reaches degree 3)."""
    rng = random.Random(seed)
    adj = [set() for _ in range(n)]
    prs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(prs)
    E = []
    for u, v in prs:
        if any(adj[v] & adj[w] for w in adj[u] if w != v):
            continue
        if any(adj[u] & adj[w] for w in adj[v] if w != u):
            continue
        adj[u].add(v); adj[v].add(u)
        if has_induced_path_on(adj, 6):
            adj[u].discard(v); adj[v].discard(u)
            continue
        E.append((u, v))
    return n, E


gp = []
for seed in range(24):
    n = 8 + seed % 7
    nn, EE = rand_c4free_p6free(n, 4200 + seed)
    a2 = neighbours(EE, nn)
    if connected(a2):
        gp.append((nn, EE, a2))
tested_g = 0
maxdeg_g = 0
for nn, EE, a2 in gp:
    for s in p5_endpoints(a2):
        tested_g += 1
        maxdeg_g = max(maxdeg_g, len(a2[s]))
        check(len(a2[s]) <= 5, f"G22 on greedy P6-free n={nn} E={EE} at s={s}")
print(f"  greedy C4-free+P6-free carriers (n=8..14): {len(gp)}; "
      f"P5-endpoints tested: {tested_g}; max endpoint degree: {maxdeg_g}; "
      f"max degree in pool: {max((len(a2[v]) for nn, EE, a2 in gp for v in range(nn)), default=0)}")

print("  general form G22(k): C4-free + no induced P_{k+1} => every endpoint of an")
print("  induced P_k has degree <= k.  (k=5 is the case used by the line.)")
for k in (3, 4, 5):
    tk = 0
    for n, E, adj in c4f_pool:
        if has_induced_path_on(adj, k + 1):
            continue
        for s in range(n):
            if induced_path_from(adj, s, k):
                tk += 1
                check(len(adj[s]) <= k, f"G22(k={k}) n={n} E={E} s={s}")
    print(f"    k={k}: {tk} endpoints tested over the exhaustive n<=7 pool, bound {k}")

big = []
for name, (n, E) in [("Petersen", (10, [(i, (i + 1) % 5) for i in range(5)] +
                                   [(5 + i, 5 + (i + 2) % 5) for i in range(5)] +
                                   [(i, 5 + i) for i in range(5)])),
                     ("C5", (5, [(i, (i + 1) % 5) for i in range(5)])),
                     ("C6", (6, [(i, (i + 1) % 6) for i in range(6)]))]:
    big.append((name, n, E))
for k in (2, 3, 5, 10):
    big.append((f"friendship F_{k}", ) + friendship(k))
for name, n, E in big:
    adj = neighbours(E, n)
    p6 = has_induced_path_on(adj, 6)
    eps = p5_endpoints(adj)
    md = max(len(adj[v]) for v in range(n))
    print(f"  {name:<15} n={n:<3} C4free={not has_c4(adj)} P6free={not p6} "
          f"#P5-endpoints={len(eps)} maxdeg={md} "
          f"maxdeg(P5-endpoint)={max([len(adj[s]) for s in eps], default='-')}")
    if not p6 and not has_c4(adj):
        for s in eps:
            check(len(adj[s]) <= 5, f"G22 on {name} at {s}")
print("  => friendship F_k: C4-free, P6-free, degree 2k unbounded, but it has NO")
print("     induced P5 at all -- the P5-endpoint hypothesis of G22 is necessary.")

# ================================================================= (C)
print()
print("=== (C) Lemma G23 (NEW): ball structure at a triangular diameter endpoint ===")
print("  claim: C4-free, a(u)=1, ecc(u)=3.  Then N(u)={p,q} with p~q, and")
print("    ball_2(u) = {u,p,q} + B_p + B_q  (disjoint), |ball_2(u)| = d(p)+d(q)-1,")
print("    and every h in B_p has |N(h) & ({p,q} u B_p u B_q)| <= 3.")
inst = 0
g24a = 0
# add the big C4-free graphs as extra carriers
extra = []
n, E = hoffman_singleton()
extra.append(("HS+leaf", n + 1, list(E) + [(0, n)]))
for q in (5, 7):
    nn, EE = er_polarity(q)
    extra.append((f"ER_{q}+leaf", nn + 1, list(EE) + [(0, nn)]))
rng = random.Random(20260818)
for seed in range(30):                     # random maximal C4-free graphs
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

carriers = [(f"small n={n}", n, E) for n, E, adj in c4f_pool] + \
           [(nm, n, E) for nm, n, E in extra]
for nm, n, E in carriers:
    adj = neighbours(E, n)
    if not connected(adj) or has_c4(adj):
        continue
    D = alldist(adj)
    ecc, r = ecc_rad(D)
    a = avec(adj)
    for u in range(n):
        if a[u] != 1 or ecc[u] != 3 or len(adj[u]) != 2:
            continue
        p, q = sorted(adj[u])
        if q not in adj[p]:
            continue                       # a(u)=1 with d(u)=2 forces p~q anyway
        inst += 1
        check(adj[p] & adj[q] == {u}, f"{nm}: p,q must have u as unique common nb")
        Bp = adj[p] - {u, q}
        Bq = adj[q] - {u, p}
        check(not (Bp & Bq), f"{nm}: B_p and B_q disjoint")
        ball = {v for v in range(n) if D[u][v] <= 2}
        check(ball == {u, p, q} | Bp | Bq, f"{nm}: ball_2(u) decomposition")
        check(len(ball) == len(adj[p]) + len(adj[q]) - 1,
              f"{nm}: |ball_2(u)| = d(p)+d(q)-1")
        slots = {p, q} | Bp | Bq
        for h in Bp | Bq:
            check(len(adj[h] & slots) <= 3,
                  f"{nm}: |N(h) & slots| <= 3 at h={h} (got {len(adj[h] & slots)})")
        # G23(c): the two-sided degree count that drives the branch's mass bound
        Hp = {h for h in Bp | Bq if a[h] >= 3}
        check(sum(len(adj[h]) for h in Hp) <= 2 * (n - 3) + len(Hp),
              f"{nm}: sum_{{H'}} d(h) <= 2(n-3)+|H'| (u={u})")
        check(a[p] <= len(adj[p]) - 1 and a[q] <= len(adj[q]) - 1,
              f"{nm}: a(p) <= d(p)-1 (triangle upq)")
        # ---- G24 (round-6 decisive-step lemma), unconditional parts
        Dl = {v for v in range(n) if D[u][v] == 3}
        check(len(Dl) + len(Bp) + len(Bq) + 3 == n, f"{nm}: layer count")
        check(all(not (adj[v] & Dl) for v in (p, q)), f"{nm}: p,q have no D-neighbour")
        g24a += 1
        for h in Bp | Bq:
            check(a[h] - 2 <= len(adj[h] & Dl),
                  f"{nm}: G24(a) a(h)-2 <= |N(h)&D| at h={h}")
        for y in Dl:
            check(len(adj[y] & Bp) <= 1 and len(adj[y] & Bq) <= 1,
                  f"{nm}: G24 y has <=1 parent per side (y={y})")
        # injectivity of y -> (B_p-parent, B_q-parent) on the two-parent part
        seen = {}
        for y in Dl:
            pp, qq = adj[y] & Bp, adj[y] & Bq
            if pp and qq:
                key = (min(pp), min(qq))
                check(key not in seen,
                      f"{nm}: G24 two-parent map must be injective ({key})")
                seen[key] = y
print(f"  G23/G24 instances tested (a(u)=1 vertices of eccentricity 3): {inst}")
print(f"  G24(a) layer decomposition + parent-injectivity carriers: {g24a}")
check(inst >= 20, "G23 must be tested non-vacuously")

print()
print("  refutation of Tab B's claimed 'minimal example' (w133_RES_qwen_r5.md 7.2):")
print("    two triangles u,p,q and z,r,s joined by cross-edges p~r, q~s")
n6, E6 = 6, [(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5), (1, 4), (2, 5)]
f6 = pack("TabB-min", n6, E6)
print(f"    n=6 C4-free={f6['c4free']}  (cycle p-r-s-q-p is a C4)  l={f6['l']:.3f}")
check(not f6['c4free'], "Tab B's example must be shown to CONTAIN a C4")
check(f6['l'] < 3, "Tab B's example also fails l>3 (they said so themselves)")
print("    => the example is invalid twice over; it is only an illustration in")
print("       their text, but it is a verified error in the harvest.")

print()
print(f"TOTAL ASSERT FAILURES: {FAIL}")
sys.exit(1 if FAIL else 0)
