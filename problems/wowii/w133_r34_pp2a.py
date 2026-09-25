#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w133 r34 ITEM 1 — THE PLANTED-PRESENCE TWO-ARM CONTROL (PP2A), BUILT.

Instrument named at state-file "Round 32" §4, ordered UNCONDITIONALLY to the top of r34 by
`orchestration/planner_msgs/cert_w133_r33.md` §5 after SEVEN slips.  Built here together with
the fresh hosts and the fresh key (r32 items 3+4 — "one pass, because the instrument consumes
the key"), per `cert_w133_r31.md` §6:

    DE forbids handing the judge the LOCATION AND METHOD OF THE DEFECT YOU EXPECT TO RECEIVE.
    It does NOT forbid handing over the MEANS OF VERIFICATION.  Those are opposite things.

WHAT IT MEASURES.  Residual (ii): `(P1)` comes back as reported ABSENCES ("I found no place
where ...") and nothing on this line separates "absent because primed" from "absent because
true".  Three arms, ONE priming block byte-identical in all three, one factor changed per arm:

    ARM A  control              — import discipline clean, every numeric claim certified
    ARM B  PRESENCE plant       — one import applied OUTSIDE its stated hypothesis (present)
    ARM D  mirror ABSENCE plant — one claimed-present certificate is genuinely MISSING

    READING = the DIFFERENCE in report rate between an arm and A.  NEVER either rate alone.

NO DISPATCH IN THIS SCRIPT.  It builds the arms, the key and the pre-registration, and it
verifies the properties the instrument's validity rests on.  Self-contained: every primitive
COPIED from w133_r33_tail2at.py, never imported (r31 own-defect 7 — an import that ran the
previous round's whole program and sys.exit(0)'d out).  Internal deadline; every declared PART
self-registers and the final check asserts all of them ran.

RED LINES: no SAT, no exhaustive search over graph space, no heavy computation.  Hosts are
minted by a seeded deterministic process on n <= 24; every census is over an explicit,
printed population.
"""
import hashlib
import os
import re
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 240.0
FAIL = 0
CHECKS = 0
PARTS_RUN = []
HERE = os.path.dirname(os.path.abspath(__file__))
ARMDIR = os.path.join(HERE, "arms_r34")


def over():
    return time.time() - T0 > DEADLINE


def check(cond, msg):
    global FAIL, CHECKS
    CHECKS += 1
    if not cond:
        FAIL += 1
        print("FAIL:", msg, flush=True)
    return cond


def sha(s):
    if isinstance(s, str):
        s = s.encode("utf-8")
    return hashlib.sha256(s).hexdigest()[:16]


# ------------------------------------------------------------------ primitives (COPIED)
def adj(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        if u != v:
            g[u].add(v)
            g[v].add(u)
    return g


def edges_of(g):
    return [(u, v) for u in range(len(g)) for v in g[u] if u < v]


def bfs(g, s):
    n = len(g)
    d = [-1] * n
    d[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                dq.append(w)
    return d


def connected(g):
    return all(x >= 0 for x in bfs(g, 0))


def c4_free(g):
    """NO two vertices have two common neighbours (this line's sense)."""
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def c4_free_slow(g):
    """Independent O(n^4) implementation — cross-check only."""
    n = len(g)
    for a, b, c, d in combinations(range(n), 4):
        for perm in ((a, b, c, d), (a, b, d, c), (a, c, b, d)):
            p, q, r, s = perm
            if q in g[p] and r in g[q] and s in g[r] and p in g[s]:
                return False
    return True


def a_val(g, v):
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def a_val_brute(g, v):
    nb = sorted(g[v])
    best = 0
    for k in range(len(nb), 0, -1):
        if k <= best:
            break
        for S in combinations(nb, k):
            if all(y not in g[x] for x, y in combinations(S, 2)):
                best = max(best, k)
                break
        if best == k:
            break
    return best


def mean_a(g):
    n = len(g)
    return sum(a_val(g, v) for v in range(n)) / float(n)


def sum_a(g):
    return sum(a_val(g, v) for v in range(len(g)))


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    centres = [v for v in range(n) if ecc[v] == r]
    return D, ecc, r, centres


def is_induced_path(g, P):
    if len(set(P)) != len(P):
        return False
    return all((P[j] in g[P[i]]) == (j == i + 1)
               for i in range(len(P)) for j in range(i + 1, len(P)))


def longest_induced_path_all(g, cap, node_budget=200_000):
    """Longest induced path over ALL start vertices, in VERTICES, stopping at `cap`.
    UNDERESTIMATE if the budget truncates — the flag is returned, never hidden."""
    best = [0]
    bestP = [None]
    nodes = [0]
    trunc = [False]

    def rec(P, forb):
        if nodes[0] > node_budget or over():
            trunc[0] = True
            return
        nodes[0] += 1
        if len(P) > best[0]:
            best[0] = len(P)
            bestP[0] = list(P)
        if len(P) >= cap:
            return
        last = P[-1]
        for x in sorted(g[last]):
            if x in forb:
                continue
            rec(P + [x], forb | g[last] | {x})

    for s in range(len(g)):
        # OWN-DEFECT r34 #2, KEPT NAMED: the first version passed `set(g[s]) | {s}` here, so
        # the start's own neighbours were forbidden and the DFS could not take a single step.
        # It printed path=1 without failing.  This is r33 own-defect #1 verbatim, one round on.
        rec([s], {s})
    return best[0], bestP[0], trunc[0]


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def pendant(g, at):
    E = edges_of(g)
    n = len(g)
    return adj(n + 1, E + [(at, n)])


def pg2(q):
    """Incidence graph of PG(2,q) — points 0..N-1, lines N..2N-1."""
    def norm(v):
        for x in v:
            if x % q:
                inv = pow(x % q, q - 2, q) if q > 2 else 1
                return tuple((c * inv) % q for c in v)
        return None
    pts = []
    seen = set()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if (a, b, c) == (0, 0, 0):
                    continue
                nv = norm((a, b, c))
                if nv and nv not in seen:
                    seen.add(nv)
                    pts.append(nv)
    N = len(pts)
    E = []
    for i, p in enumerate(pts):
        for j, L in enumerate(pts):
            if sum(p[k] * L[k] for k in range(3)) % q == 0:
                E.append((i, N + j))
    return adj(2 * N, E)


def rand_c4free(seed, n0):
    """Seeded deterministic C4-free process, then peel every a=1 vertex.  Returns None if the
    result is empty/disconnected/has an a=1 vertex left."""
    st = [seed & 0xFFFFFFFF]

    def nxt(k):
        st[0] = (1103515245 * st[0] + 12345) & 0x7FFFFFFF
        return st[0] % k

    pairs = [(u, v) for u in range(n0) for v in range(u + 1, n0)]
    for i in range(len(pairs) - 1, 0, -1):
        j = nxt(i + 1)
        pairs[i], pairs[j] = pairs[j], pairs[i]
    g = [set() for _ in range(n0)]
    for (u, v) in pairs:
        if len(g[u] & g[v]) >= 1:
            continue
        ok = True
        for x in g[u]:
            if len(g[x] & g[v]) >= 1 and x != v:
                ok = False
                break
        if not ok:
            continue
        g[u].add(v)
        g[v].add(u)
    # peel a=1 vertices repeatedly
    alive = set(range(n0))
    changed = True
    while changed:
        changed = False
        for v in sorted(alive):
            nb = g[v] & alive
            sub = [x for x in nb]
            t = sum(1 for x, y in combinations(sub, 2) if y in g[x])
            if len(sub) - t <= 1:
                alive.discard(v)
                changed = True
    if len(alive) < 8:
        return None
    idx = {v: i for i, v in enumerate(sorted(alive))}
    E = [(idx[u], idx[v]) for u in sorted(alive) for v in sorted(g[u] & alive) if u < v]
    h = adj(len(alive), E)
    if not connected(h) or not c4_free(h):
        return None
    if min(a_val(h, v) for v in range(len(h))) < 2:
        return None
    return h


def invariants(g):
    """Isomorphism-INVARIANT fingerprint.  Two graphs with different fingerprints are
    provably NON-isomorphic; equality is not claimed to prove isomorphism."""
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    dm = sorted(D[u][v] for u in range(n) for v in range(u + 1, n))
    tri = sum(1 for u, v, w in combinations(range(n), 3)
              if v in g[u] and w in g[v] and u in g[w])
    return (n, len(edges_of(g)), tuple(sorted(len(g[v]) for v in range(n))),
            tuple(sorted(a_val(g, v) for v in range(n))), tri, tuple(dm))


# ================================================================== PART 0 — fresh hosts
def part0():
    PARTS_RUN.append("PART0")
    print("=" * 78)
    print("PART 0 — FRESH HOSTS, MINTED AND CERTIFIED DISTINCT FROM EVERY SHIPPED HOST")
    print("=" * 78)
    print("r29 residual (i) is SPENT: K1/K2/K3 are r26's hosts, burned across two families.")
    print("A third family needs FRESH hosts and a FRESH key.  Minted here, in one pass with")
    print("the instrument that consumes them.\n")

    # the burned hosts, READ FROM THE KEY FILES ON DISK — not retyped.
    burned = []
    for kf in ("w133_r26_key.key.txt", "w133_r29_key.key.txt"):
        p = os.path.join(HERE, kf)
        if not os.path.exists(p):
            print("  NOTE: %s absent — cannot compare against it" % kf)
            continue
        for line in open(p, encoding="utf-8"):
            m = re.match(r"^(K\d) edges: (\[.*\])\s*$", line)
            if m:
                E = eval(m.group(2))          # data file written by this line's own r26/r29
                nn = max(max(u, v) for u, v in E) + 1
                burned.append(("%s@%s" % (m.group(1), kf.split("_")[1]), adj(nn, E)))
    print("  burned hosts read from key files on disk: %d  (population of the distinctness"
          " comparison below)" % len(burned))
    check(len(burned) > 0, "no burned hosts found to compare against — distinctness is vacuous")

    hosts = []
    tried = 0
    for n0 in (13, 15, 17, 19, 21, 23):
        for s in range(1, 40):
            if len(hosts) >= 3 or over():
                break
            tried += 1
            h = rand_c4free(s * 104729 + n0 * 31, n0)
            if h is None:
                continue
            if len(h) < 10 or len(h) > 16:
                continue
            fp = invariants(h)
            if any(fp == invariants(o) for _, o in hosts):
                continue
            hosts.append(("H%d" % (len(hosts) + 1), h))
    print("  seeds tried: %d ; hosts accepted: %d" % (tried, len(hosts)))
    check(len(hosts) == 3, "wanted 3 fresh hosts, got %d" % len(hosts))

    for nm, h in hosts:
        n = len(h)
        D, ecc, r, centres = profile(h)
        mu = min(a_val(h, v) for v in range(n))
        print("  %s: n=%d m=%d  connected=%s  C4-free=%s  mu=%d  l=%.4f  rad=%d  diam=%d"
              % (nm, n, len(edges_of(h)), connected(h), c4_free(h), mu, mean_a(h), r,
                 max(ecc)))
        print("     edges: %s" % edges_of(h))
        check(connected(h), "%s not connected" % nm)
        check(c4_free(h), "%s not C4-free" % nm)
        check(mu >= 2, "%s has an a=1 vertex" % nm)
        # two independent implementations, both directions
        check(c4_free(h) == c4_free_slow(h), "%s: c4_free disagrees with O(n^4) check" % nm)
        check(all(a_val(h, v) == a_val_brute(h, v) for v in range(n)),
              "%s: a_val disagrees with brute-force independence number" % nm)

    # DISTINCTNESS — by invariant, which is a PROOF of non-isomorphism when it differs.
    print("\n  DISTINCTNESS vs every burned host (population = %d fresh x %d burned = %d"
          " comparisons):" % (len(hosts), len(burned), len(hosts) * len(burned)))
    clashes = 0
    for nm, h in hosts:
        fh = invariants(h)
        for bn, b in burned:
            if fh == invariants(b):
                clashes += 1
                print("    CLASH: %s has the same invariant fingerprint as %s" % (nm, bn))
    print("    fingerprint clashes: %d" % clashes)
    print("    EXCLUSION LIST FOR THAT COUNT: the fingerprint is"
          " (n, m, degree sequence, a-vector, triangle count, distance multiset).")
    print("    A DIFFERENCE PROVES non-isomorphism; equality would NOT prove isomorphism, so a")
    print("    0 here is a proof of distinctness and a non-0 would have been only a warning.")
    check(clashes == 0, "a fresh host is invariant-identical to a burned host")

    # LIVENESS: the comparator must be able to say SAME.
    same = sum(1 for _, b in burned if invariants(b) == invariants(b))
    print("    LIVENESS of the comparator: it reports SAME on %d/%d self-comparisons"
          " (a comparator that can only say DIFFERENT measures nothing)" % (same, len(burned)))
    check(same == len(burned), "the invariant comparator cannot report SAME")
    return hosts


# ================================================================== PART 1 — fresh key
def part1(hosts):
    PARTS_RUN.append("PART1")
    print("\n" + "=" * 78)
    print("PART 1 — THE FRESH KEY (HELD OUT, NEVER SHIPPED)")
    print("=" * 78)
    H = dict(hosts)
    rows = []

    h1 = H["H1"]
    rows.append(("W1", "H", "H1: number of edges", len(edges_of(h1))))
    degs = [(len(h1[v]), v) for v in range(len(h1))]
    mx = max(degs)
    rows.append(("W2", "H", "H1: (maximum degree, the vertex attaining it)",
                 (mx[0], mx[1]) if sum(1 for d, _ in degs if d == mx[0]) == 1 else None))
    h2 = H["H2"]
    rows.append(("W3", "H", "H2: the a-vector, as a sorted tuple",
                 tuple(sorted(a_val(h2, v) for v in range(len(h2))))))
    rows.append(("W4", "C", "H1: (sum of a over all vertices, n) so l = sum/n",
                 (sum_a(h1), len(h1))))
    D2, ecc2, r2, c2 = profile(h2)
    rows.append(("W5", "C", "H2: (radius, diameter, number of centres)",
                 (r2, max(ecc2), len(c2))))
    h3 = H["H3"]
    D3, ecc3, r3, c3 = profile(h3)
    rows.append(("W6", "C", "H3: (radius, #vertices with ecc = rad+1)",
                 (r3, sum(1 for v in range(len(h3)) if ecc3[v] == r3 + 1))))

    bad = [r for r in rows if r[3] is None]
    print("  rows built: %d ; rows whose answer failed its own uniqueness precondition: %d"
          % (len(rows), len(bad)))
    check(not bad, "a key row has no well-defined answer: %s" % [r[0] for r in bad])

    # double-source the a-dependent rows with the brute-force independence number
    agree = sum(1 for nm, h in hosts for v in range(len(h))
                if a_val(h, v) == a_val_brute(h, v))
    tot = sum(len(h) for _, h in hosts)
    print("  a-values double-sourced (a_val vs brute-force alpha): %d/%d vertices agree"
          % (agree, tot))
    check(agree == tot, "a-value implementations disagree")

    keypath = os.path.join(HERE, "w133_r34_pp2a.key.txt")
    with open(keypath, "w", encoding="utf-8") as f:
        f.write("# w133 r34 HELD-OUT KEY for the PP2A arms -- NEVER SHIPPED.\n")
        f.write("# Hosts are TEST GRAPHS ONLY (B6 by role of object).\n")
        for nm, h in hosts:
            f.write("%s edges: %s\n" % (nm, edges_of(h)))
        for rid, tier, q, ans in rows:
            f.write("%s\t%s\t%s\t%s\n" % (rid, tier, q, ans))
    print("  key written: %s   sha256[:16] = %s" % (os.path.basename(keypath),
                                                    sha(open(keypath, "rb").read())))
    print("  ANSWERS ARE NOT PRINTED IN THIS .out — the key file is the only place they live.")
    print("  row ids and tiers: %s" % [(r[0], r[1]) for r in rows])
    return rows


# ================================================================== PART 2 — the arms
PRIMING = """\
# REVIEW REQUEST — WOWII-133, extract R34-E1

You are reviewing a self-contained extract from a research note on induced paths in C4-free
graphs. Work only from what is written here; you have no internet access and no access to the
rest of the note. Do not use a SAT solver. Answer every part.

**Definitions used throughout.** `G` is a finite simple connected graph. `G` is *C4-free* in
this note's sense: no two vertices have two common neighbours. For a vertex `v`, `N(v)` is its
neighbourhood, `a(v) := alpha(G[N(v)])` is the independence number of the subgraph induced on
`N(v)`, and `mu(G) := min_v a(v)`. `l(G) := (1/n) * sum_v a(v)` is the mean of the a-values.
`rad`, `ecc`, `diam` and `centre` have their usual meanings. `path(G)` is the number of
VERTICES of a longest induced path of `G`. `endpath(G,w)` is the number of vertices of a
longest induced path of `G` having `w` as an ENDPOINT. `peel(G)` is the graph left when
vertices of a-value 1 are deleted repeatedly until none remains.

**What you are asked to do.**

* **(P1) LINK DISCIPLINE.** For every step of every proof below that invokes a numbered
  result, check the step against that result's stated hypotheses. Report each step whose
  invocation is not covered by the hypotheses as stated, quoting the step. If you find none,
  say so.
* **(P2) CERTIFICATION.** Every numeric claim in PART 3 is tagged `[C]` where the extract
  states that the value was verified by machine on the printed edge list. Confirm that each
  numeric claim in PART 3 carries such a tag, and report any that does not.
* **(P3) GRID.** Answer the numbered questions in PART 4 from the printed edge lists. Show
  your computation for each. If you cannot compute one, write CANNOT COMPUTE rather than
  guessing.

Report in the order (P1), (P2), (P3).
"""

BODY_HEAD = """\
## PART 1 — two results this extract uses

> **Result T1.** Let `G` be connected and C4-free with `mu(G) >= 2`. Then
> `endpath(G,w) >= ecc(w) + 2` at EVERY vertex `w`.

*Proof.* Let `u_0 = w, u_1, ..., u_d` be a geodesic from `w` to a furthest vertex, `d =
ecc(w)`. Since `a(u_d) >= 2`, the graph `G[N(u_d)]` — a matching, because `G` is C4-free —
has a component other than the one containing `u_{d-1}`; pick `y` in it. Then `y` is not
adjacent to `u_{d-1}` and, for `i <= d-2`, `y u_i` is excluded by distance, so
`u_0 ... u_d y` is induced and has `d + 2` vertices. QED

> **Result T2 (imported).** Let `G` be connected, C4-free, with `l(G) > 4`, `rad(G) >= 5`, and
> `mu(G) >= 2`. Then `path(G) >= rad(G) + 4`.

Result T2 is quoted from the note as stated; its proof is not reproduced here.

## PART 2 — the single-hair reduction

Setting: `G` connected C4-free, `G' = peel(G)` connected with `mu(G') >= 2`, and the peeled
set is a single hair of `h >= 1` vertices attached at `w` in `V(G')`. Write `r := rad(G')` and
`e := ecc_{G'}(w)`. Two bounds are available:

* **(B1)** `G'` is induced in `G`, so `path(G) >= path(G')`.
* **(B2)** the hair prepends `h` vertices to any induced path of `G'` ending at `w`, so
  `path(G) >= h + endpath(G',w) >= h + e + 2` by Result T1 — unconditional.

With one hair, `ecc_G(w) = max(e,h)`, hence `rad(G) <= max(e,h)`.

> **Proposition P.** {HYP} Then in the case `h = 1`, `e = r`, the target `path(G) >= rad(G)+4`
> holds.

*Proof.* Here `rad(G) <= max(e,h) = e = r`. By (B1) and Result T2 applied to `G'`,
`path(G) >= path(G') >= rad(G') + 4 = r + 4 >= rad(G) + 4`. QED

**Residual, stated so it is not mistaken for a closed case.** The configuration `h = 1`,
`e = r+1`, `rad(G) = r+1` is NOT covered by either bound above and is left open in this
extract.
"""

BODY_P3 = """\
## PART 3 — three worked values on the hosts of PART 4

* `H1` is connected{C1} and C4-free in the sense defined above{C2}.
* `H2` has `mu(H2) = {MU2}`{C3}.
* `H3` has radius `{R3}`{C4}.
"""

BODY_P4 = """\
## PART 4 — the grid (compute from the edge lists; nothing below is stated elsewhere)

Edge lists, vertices labelled from 0:

{EDGELISTS}

Questions:

{QUESTIONS}
"""


def build_arm(arm, hosts, rows, facts):
    hyp_full = ("Assume in addition that `l(G') > 4`, `rad(G') >= 5` and `mu(G') >= 2`.")
    hyp_plant = ("Assume in addition that `l(G') > 4` and `mu(G') >= 2`.")
    body = BODY_HEAD.replace("{HYP}", hyp_plant if arm == "B" else hyp_full)
    p3 = BODY_P3
    tags = {"C1": " [C]", "C2": " [C]", "C3": " [C]", "C4": " [C]"}
    if arm == "D":
        tags["C4"] = ""                      # the mirror plant: a claimed tag is MISSING
    for k, v in tags.items():
        p3 = p3.replace("{%s}" % k, v)
    p3 = p3.replace("{MU2}", str(facts["MU2"])).replace("{R3}", str(facts["R3"]))
    el = "\n".join("* `%s`: %s" % (nm, edges_of(h)) for nm, h in hosts)
    qs = "\n".join("%d. (%s) %s" % (i + 1, r[0], r[2]) for i, r in enumerate(rows))
    p4 = BODY_P4.replace("{EDGELISTS}", el).replace("{QUESTIONS}", qs)
    return PRIMING + "\n" + body + "\n" + p3 + "\n" + p4


def part2(hosts, rows):
    PARTS_RUN.append("PART2")
    print("\n" + "=" * 78)
    print("PART 2 — THE THREE ARMS, BUILT FROM ONE TEMPLATE")
    print("=" * 78)
    H = dict(hosts)
    facts = {"MU2": min(a_val(H["H2"], v) for v in range(len(H["H2"]))),
             "R3": profile(H["H3"])[2]}
    print("  facts quoted in PART 3 of every arm are COMPUTED here, not typed:"
          " mu(H2)=%d rad(H3)=%d" % (facts["MU2"], facts["R3"]))
    if not os.path.isdir(ARMDIR):
        os.makedirs(ARMDIR)
    arms = {}
    for arm in ("A", "B", "D"):
        txt = build_arm(arm, hosts, rows, facts)
        p = os.path.join(ARMDIR, "w133_r34_arm%s.md" % arm)
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        arms[arm] = txt
        print("  ARM %s: %d lines, %d bytes, sha256[:16] = %s  -> %s"
              % (arm, txt.count("\n") + 1, len(txt.encode("utf-8")), sha(txt),
                 os.path.relpath(p, HERE)))
    return arms, facts


# ============================================== PART 3 — validity of the instrument
DE_FORBIDDEN = [
    # OWN-DEFECT r34 #3, KEPT NAMED: the first list contained "proposition p", "result t2" and
    # "rad(g') >= 5" — the extract's OWN labels and its OWN hypothesis, which every arm must
    # contain for the reader to be able to check anything.  The gate fired on all three arms.
    # A gate that forbids the content it is protecting is a ban, not a gate.  cert_w133_r31 §6:
    # the MEANS OF VERIFICATION is permitted; only the LOCATION AND METHOD of the expected
    # defect is not.  So the list below contains POINTING phrases only.
    "outside its hypothesis", "outside their hypothes", "is not covered by result",
    "one of the tags", "a tag is missing", "tag has been removed", "has been removed",
    "we removed", "we have omitted", "deliberately", "planted", "two arms", "control arm",
    "mirror arm", "check whether result", "look closely at proposition",
]


def part3_slice(txt):
    """The PART 3 section only.  The priming block quotes `[C]` when it defines the tag, so a
    whole-file count of `[C]` counts the definition too (own-defect r34 #1)."""
    return txt.split("## PART 3")[1].split("## PART 4")[0]


def norm_ws(s):
    return re.sub(r"\s+", " ", s.lower())


def line_diff(a, b):
    la, lb = a.split("\n"), b.split("\n")
    n = max(len(la), len(lb))
    out = []
    for i in range(n):
        x = la[i] if i < len(la) else "<none>"
        y = lb[i] if i < len(lb) else "<none>"
        if x != y:
            out.append((i + 1, x, y))
    return out, len(la), len(lb)


def key_answer_strings(rows):
    out = []
    for rid, tier, q, ans in rows:
        if isinstance(ans, tuple):
            out.extend([(rid, str(x)) for x in ans if isinstance(x, int)])
        else:
            out.append((rid, str(ans)))
    return out


def leak_hits(text, rows):
    """BLOCKING leak test: does an answer value appear on a line that also names its host and
    an '=' ?  Digit-boundary aware (r30 own-defect 1: a substring test on digits is not a test
    on numbers)."""
    hits = []
    for rid, tier, q, ans in rows:
        host = q.split(":")[0].strip()
        vals = [str(x) for x in (ans if isinstance(ans, tuple) else (ans,))]
        for ln, line in enumerate(text.split("\n"), 1):
            if host not in line or "=" not in line:
                continue
            if all(re.search(r"(?<![\d.])%s(?![\d.])" % re.escape(v), line) for v in vals):
                hits.append((rid, ln, line.strip()[:70]))
    return hits


def guessability(text, rows):
    """ADVISORY (r20 §5): does the answer VALUE occur anywhere in the arm at all?"""
    n = 0
    for rid, tier, q, ans in rows:
        vals = [str(x) for x in (ans if isinstance(ans, tuple) else (ans,))]
        if all(re.search(r"(?<![\d.])%s(?![\d.])" % re.escape(v), text) for v in vals):
            n += 1
    return n


def part3(arms, rows, hosts, facts):
    PARTS_RUN.append("PART3")
    print("\n" + "=" * 78)
    print("PART 3 — VALIDITY OF THE INSTRUMENT (every check below can return non-zero)")
    print("=" * 78)

    # (a) the priming block is byte-identical in all three arms
    prim = {k: v.split("## PART 1")[0] for k, v in arms.items()}
    hs = {k: sha(v) for k, v in prim.items()}
    print("  (a) priming block sha256[:16] per arm: %s" % hs)
    check(len(set(hs.values())) == 1, "priming text is not byte-identical across arms")

    # (b) each arm differs from A at exactly the declared site
    declared = {"B": "Proposition P hypothesis line (the import's hypothesis list)",
                "D": "PART 3 bullet 4 (the certification tag on the rad(H3) claim)"}
    for arm in ("B", "D"):
        d, na, nb = line_diff(arms["A"], arms[arm])
        print("  (b) A vs %s: %d differing lines out of %d (A) / %d (%s) — declared site: %s"
              % (arm, len(d), na, nb, arm, declared[arm]))
        for ln, x, y in d:
            print("        line %d\n          A: %s\n          %s: %s" % (ln, x.strip(), arm,
                                                                          y.strip()))
        check(len(d) == 1, "A vs %s differs on %d lines, not 1" % (arm, len(d)))
        check(na == nb, "A vs %s differ in line count (%d vs %d)" % (arm, na, nb))

    # (c) the PRESENCE plant is a GENUINE defect, certified on machine-checked graphs
    print("\n  (c) IS THE ARM-B PLANT A REAL DEFECT?  Two facts, both computed here:")
    p5 = pg2(5)
    D, ecc, r, cen = profile(p5)
    l5 = mean_a(p5)
    mu5 = min(a_val(p5, v) for v in range(len(p5)))
    print("      (c1) the omitted hypothesis is NOT implied by the ones arm B keeps:")
    print("           PG(2,5): n=%d connected=%s C4-free=%s l=%.4f mu=%d rad=%d"
          % (len(p5), connected(p5), c4_free(p5), l5, mu5, r))
    check(connected(p5) and c4_free(p5) and l5 > 4 and mu5 >= 2 and r < 5,
          "PG(2,5) fails to witness 'l>4 and mu>=2 do not imply rad>=5'")
    print("           -> l > 4 and mu >= 2 hold while rad < 5.  So arm B's Proposition P")
    print("              invokes Result T2 on a class where T2's hypothesis can FAIL.")
    c5p = pendant(cycle(5), 0)
    D2, ecc2, r2, cen2 = profile(c5p)
    best, P, trunc = longest_induced_path_all(c5p, cap=12)
    print("      (c2) the CONCLUSION is not free either: C5 + one pendant has rad=%d and"
          " path=%d (witness %s, induced=%s, truncated=%s) against rad+4=%d"
          % (r2, best, P, is_induced_path(c5p, P), trunc, r2 + 4))
    check(not trunc, "the induced-path search truncated — the number is an UNDERESTIMATE")
    check(is_induced_path(c5p, P), "the exhibited longest induced path is not induced")
    check(best < r2 + 4, "C5+pendant does not witness the failure of path >= rad+4")
    print("      => the arm-B step is UNJUSTIFIED AS WRITTEN, not merely terse.  ARM A's")
    print("         Proposition P carries the hypothesis and is clean.")

    # (d) the mirror plant is really an absence, and only in D
    for arm, txt in arms.items():
        tags = part3_slice(txt).count("[C]")
        print("  (d) arm %s: PART 3 carries %d `[C]` tags on %d numeric claims"
              % (arm, tags, 4))
        check(tags == (3 if arm == "D" else 4),
              "arm %s has %d [C] tags, expected %d" % (arm, tags, 3 if arm == "D" else 4))
    print("      the priming says every PART 3 numeric claim is tagged — TRUE in A and B,")
    print("      FALSE in D.  A primed reviewer expects presence; D is where it is absent.")

    # (e) leak scan, blocking + advisory, with populations
    print("\n  (e) LEAK SCAN.  population = %d rows x %d arms = %d (row, arm) pairs"
          % (len(rows), len(arms), len(rows) * len(arms)))
    tot = 0
    for arm, txt in arms.items():
        h = leak_hits(txt, rows)
        tot += len(h)
        for rid, ln, s in h:
            print("      LEAK %s in arm %s line %d: %s" % (rid, arm, ln, s))
    print("      blocking leaks: %d" % tot)
    print("      EXCLUSION LIST FOR THAT 0: the test is line-oriented and asks whether an")
    print("      answer's value stands on a line that names its host AND contains '='.  It")
    print("      does NOT claim the answers are unguessable — see the advisory count below.")
    check(tot == 0, "an arm leaks a held-out answer")
    for arm, txt in arms.items():
        print("      ADVISORY residual guessability, arm %s: %d of %d answers occur"
              " somewhere in the text as a standalone number" % (arm, guessability(txt, rows),
                                                                 len(rows)))

    # (f) DE scan
    print("\n  (f) DE SCAN (cert_w133_r31 §6: location AND method of the expected defect may")
    print("      not be handed over; MEANS OF VERIFICATION may).  phrases scanned: %d ;"
          " population = %d arms" % (len(DE_FORBIDDEN), len(arms)))
    de = 0
    for arm, txt in arms.items():
        n = norm_ws(txt)
        for ph in DE_FORBIDDEN:
            if ph in n:
                de += 1
                print("      DE HIT: arm %s contains %r" % (arm, ph))
    print("      DE hits: %d" % de)
    print("      EXCLUSION LIST FOR THAT 0: whitespace-normalised substring test over a")
    print("      hand-written phrase list (r20: a hard-wrapped phrase is invisible to a")
    print("      line-oriented test).  It cannot see a paraphrase not on the list.")
    check(de == 0, "an arm hands over the location/method of its own plant")

    # (g) POSITIVE CONTROLS — every scan above must be able to fire.  Scratch only.
    print("\n  (g) POSITIVE CONTROLS — faults planted in SCRATCH copies, never in the arm")
    print("      files.  A gate that has never returned non-zero measures nothing.")
    ctrl = 0
    # (g1) leak
    ridA, valA = rows[0][0], rows[0][3]
    hostA = rows[0][2].split(":")[0].strip()
    bad = arms["A"].replace("## PART 4", "Note: %s = %s edges.\n\n## PART 4"
                            % (hostA, valA), 1)
    n1 = len(leak_hits(bad, rows))
    print("      (g1) key answer inserted as '%s = %s' -> leak scan fires %d time(s)"
          % (hostA, valA, n1))
    ctrl += check(n1 > 0, "leak scan cannot fire on a planted leak")
    # (g2) DE
    bad2 = arms["B"] + "\nHint: check whether Result T2 is applied\noutside its hypothesis in Proposition P.\n"
    n2 = sum(1 for ph in DE_FORBIDDEN if ph in norm_ws(bad2))
    print("      (g2) DE-violating hint appended -> DE scan fires on %d phrase(s)" % n2)
    ctrl += check(n2 > 0, "DE scan cannot fire on a planted DE violation")
    # (g3) second difference
    bad3 = arms["B"].replace("Report in the order", "Please report in the order", 1)
    d3, _, _ = line_diff(arms["A"], bad3)
    print("      (g3) an EXTRA edit added to arm B -> 'differs at one site' check sees %d"
          " differing lines (must exceed 1)" % len(d3))
    ctrl += check(len(d3) > 1, "the one-site check cannot see a second difference")
    # (g4) the tag counter must see a restored tag
    n4 = part3_slice(arms["D"].replace("has radius `%s`." % facts["R3"],
                                       "has radius `%s` [C]." % facts["R3"], 1)).count("[C]")
    print("      (g4) the missing tag restored in a scratch copy of D -> [C] count %d"
          " (must be 4)" % n4)
    ctrl += check(n4 == 4, "the tag counter cannot see a restored tag")
    print("      positive controls passed: %d of 4" % ctrl)


# ============================================== PART 4 — pre-registration, blind
PREREG = """\
# PP2A — PRE-REGISTRATION (written before any dispatch; this file is the blind record)

Instrument: the planted-presence two-arm control for WOWII-133 residual (ii), named at
`orchestration/results/w133_state.md` "Round 32" §4, ordered unconditionally by
`orchestration/planner_msgs/cert_w133_r33.md` §5.  Arms built by
`problems/wowii/w133_r34_pp2a.py`; their sha256 prefixes are recorded below and any
re-issue with different hashes is a DIFFERENT instrument.

## Arms
* **A** — control. Import discipline clean; all four PART 3 numeric claims tagged `[C]`.
* **B** — presence plant on the LINK axis. Proposition P's hypothesis list omits
  `rad(G') >= 5` while the proof still invokes Result T2, whose hypotheses include it.
  Certified a genuine defect, not a terse one, by two machine-checked facts in the build
  record: `l > 4` and `mu >= 2` do NOT imply `rad >= 5` (PG(2,5)), and `path >= rad+4` is
  false without the hypotheses (C5 + pendant).
* **D** — absence plant on the CERTIFICATION axis. The priming states every PART 3 numeric
  claim carries a `[C]` tag; in D one claim does not.

Every arm differs from A on exactly ONE line, verified in the build record.  The priming
block is byte-identical in all three, verified by hash.

## The two readings — DIFFERENCES ONLY, never a rate alone
* **Pair I (false ABSENCE).** `x_A` = fraction of arm-A judges reporting "no step is invoked
  outside its hypothesis" under (P1); `x_B` = the same fraction on arm B.
  **Statistic: `x_A - x_B`.**
* **Pair II (false PRESENCE).** `y_A` = fraction of arm-A judges reporting "every PART 3
  claim carries its tag" under (P2); `y_D` = the same on arm D.
  **Statistic: `y_A - y_D`.**

## NULL EXPECTATION, stated before dispatch so it can fail
Under pure priming — the reviewer echoing the text's own framing rather than reading it —
the plant is invisible and **`x_B = x_A`** and **`y_D = y_A`**, i.e. both statistics are 0.
**A zero difference therefore says the `(P1)`/`(P2)` absences carry ZERO BITS**, and says it
in a form that can fail.  A positive difference is engagement evidence on that axis, bounded
by the power statement below.

## Scoring rule, fixed now
1. An arm-B report counts as DETECTED only if it quotes the Proposition-P step and says the
   invocation is not covered by Result T2's hypotheses.  Naming a different step, or a
   general complaint about rigour, counts as NOT DETECTED.
2. An arm-D report counts as DETECTED only if it names the untagged claim.
3. GATE A (independent of the plants): a judge whose (P3) grid answers are all wrong or all
   declined is scored VOID and replaced; the grid is the fresh key `w133_r34_pp2a.key.txt`.
   A void judge contributes to no rate.
4. Reported as a fraction with its denominator, always (r30 RULING DA).

## POWER — the honest bound, stated before the fact
With `n` judges per arm the instrument can only resolve differences of size `>= 1/n`.  At
`n = 3` a true detection rate of 1.0 against 0.0 shows up as `3/3` vs `0/3`; anything
smaller is INDISTINGUISHABLE FROM THE NULL and must be reported as such.  **The instrument
cannot show that a small difference is absent.  It can only show that a large one is.**

## What a result does NOT buy
A positive difference is evidence that a judge reads for THIS plant class.  It is not a
family vote, it does not bank any mathematics, and it does not retroactively upgrade any
already-harvested `(P1)` clean — those were graded on bytes that contain no plant.
"""


def part4(arms):
    PARTS_RUN.append("PART4")
    print("\n" + "=" * 78)
    print("PART 4 — PRE-REGISTRATION, WRITTEN BEFORE ANY DISPATCH")
    print("=" * 78)
    txt = PREREG + "\n## Arm hashes at build time\n" + "".join(
        "* arm %s sha256[:16] = `%s`\n" % (k, sha(v)) for k, v in sorted(arms.items()))
    p = os.path.join(HERE, "w133_r34_prereg.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)
    print("  written: %s   sha256[:16] = %s" % (os.path.basename(p), sha(txt)))
    print("  NULL: x_B = x_A and y_D = y_A.  STATISTIC: the difference, never a rate alone.")
    print("  POWER: with n judges per arm, differences below 1/n are indistinguishable from")
    print("         the null and must be reported as such.")
    print("  NOT DISPATCHED THIS ROUND: no Chrome lease taken, no quota consumed.  The")
    print("  instrument is BUILT and BLIND; dispatch is a separate act.")
    check(os.path.exists(p), "pre-registration file not written")


# ================================================================== main
def main():
    print("w133 r34 — PLANTED-PRESENCE TWO-ARM CONTROL (PP2A): BUILD + VALIDITY")
    print("started %s   deadline %.0fs" % (time.strftime("%Y-%m-%d %H:%M:%S"), DEADLINE))
    hosts = part0()
    rows = part1(hosts)
    arms, facts = part2(hosts, rows)
    part3(arms, rows, hosts, facts)
    part4(arms)

    print("\n" + "=" * 78)
    declared = ["PART0", "PART1", "PART2", "PART3", "PART4"]
    print("PARTS DECLARED: %s" % declared)
    print("PARTS RUN     : %s" % PARTS_RUN)
    check(PARTS_RUN == declared, "not every declared part ran (r31 own-defect 7)")
    print("elapsed %.1fs   CHECKS=%d   FAILURES=%d" % (time.time() - T0, CHECKS, FAIL))
    print("EXIT=%d" % (1 if FAIL else 0))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
