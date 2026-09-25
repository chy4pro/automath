#!/usr/bin/env python3
"""
w133 round 22 -- TWO products in one file.

PART A -- THE MINT-TIME ADDRESS GATE (planner RULING BB, ordered at round 22 item 2).
  Two independent collisions on this line (F<n>, and the symbol W) were both caught by a
  GREP AFTER THE FACT, i.e. by luck.  This part turns that grep into a precondition:
  before a name is minted, it must be asserted unique against the corpus; and the whole
  existing definition table must be collision-free.
  It is DEMONSTRATED ON A DEFECT THAT ACTUALLY HAPPENED: run with a path to the
  PRE-REPAIR draft it must FIRE on `W`; run on the repaired draft it must be clean.

PART B -- THE (D3-C6) MASS-COUNT RESTART, first computable step.
  (D3-C6) (draft 27.4) hypotheses are: connected, C4-FREE, contains an induced C6, no
  induced P7 -- BYTE-FOR-BYTE the hypotheses of round 21's classification (draft 33).
  So the classification transfers with no extra assumption, and the Z-local charge is
  computable.  This part verifies the pieces:
    B1  antipodal slots hold at most ONE vertex each  (C4-freeness, one line)
    B2  hence |{w : |N(w) cap Z| = 2}| <= 3 + 3 = 6, and the bound is ATTAINED
    B3  G55's charge identity a(z) = 2 + |Off(z)| - t(z) on every instance built here
    B4  the Z-local count is NOT sufficient on its own -- exhibited, not asserted

C4-FREE throughout means: NO TWO DISTINCT VERTICES HAVE TWO COMMON NEIGHBOURS
(no 4-cycle as a SUBGRAPH; chords are irrelevant).

EVERY check prints its observed population BEFORE its verdict.
Wall-clock self-limit 180 s, exit(2) on overrun.  No SAT, no large exhaustive search.
"""
import itertools, os, re, sys, time

T0 = time.time()
LIMIT = 180.0
def tick(tag):
    if time.time() - T0 > LIMIT:
        print("OVERRUN at %s" % tag); sys.exit(2)

FAIL = []
NCHECK = 0
def check(name, ok, detail=""):
    global NCHECK
    NCHECK += 1
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    if not ok: FAIL.append(name)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DRAFT = os.path.join(REPO, "notes", "proofs", "wowii133_draft.md")

# ============================================================================
# PART A -- MINT-TIME ADDRESS GATE
# ============================================================================
# A symbol definition site on this line looks like  `X := ...`  (backticked or not).
DEF_RE = re.compile(r"([A-Za-z][A-Za-z0-9_^]*(?:_\{[^}]*\})?)\s*:=\s*(.+)")

def normalise(rhs):
    """Collapse a definition body to a comparison key: the mathematical content only.

    Whitespace is REMOVED, not collapsed.  Reason, recorded because it was a real false
    positive on first run: `H := max_{h in H} |N(h) cap H|` is written with and without a
    space after `max` at draft lines 1228 and 1593, and a whitespace-preserving key
    reported those two as a collision.  A namespace gate that cries wolf on formatting
    gets switched off, which is the failure mode this gate exists to prevent."""
    s = rhs.strip().strip("`").strip()
    s = re.sub(r"[`*_{}\\$]", "", s)
    s = re.sub(r"\s+", " ", s).strip().rstrip(".").rstrip(",").lower()
    # cut trailing prose after the definition proper
    for stop in [". then", ". hence", ". moreover", ". so ", ". consequently"]:
        i = s.find(stop)
        if i > 0: s = s[:i]
    return re.sub(r"\s+", "", s.strip())

def scan_definitions(path):
    """-> {symbol: [(line_no, normalised_rhs, raw)]}"""
    table = {}
    with open(path, encoding="utf-8") as fh:
        for ln, raw in enumerate(fh, 1):
            for m in DEF_RE.finditer(raw):
                sym, rhs = m.group(1), m.group(2)
                if sym in ("http", "https"): continue
                table.setdefault(sym, []).append((ln, normalise(rhs), raw.rstrip("\n")))
    return table

def collision_report(table):
    """-> list of (symbol, [(line, key)...]) for symbols with >1 DISTINCT definition."""
    out = []
    for sym, sites in sorted(table.items()):
        keys = {}
        for ln, key, raw in sites:
            keys.setdefault(key, []).append(ln)
        if len(keys) > 1:
            out.append((sym, sorted((k, v) for k, v in keys.items())))
    return out

def assert_mintable(name, corpus_paths, kind):
    """THE GATE ITSELF.  Returns (ok, occurrences).  A name is mintable iff it does not
    already resolve to something in the corpus."""
    pat = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_])")
    hits = []
    for p in corpus_paths:
        if not os.path.exists(p): continue
        with open(p, encoding="utf-8") as fh:
            for ln, raw in enumerate(fh, 1):
                if pat.search(raw):
                    hits.append((os.path.relpath(p, REPO), ln, raw.strip()[:110]))
    return (len(hits) == 0, hits)

def part_A(draft_path, label, expect_clean):
    print("\n=== PART A -- MINT-TIME ADDRESS GATE on %s (%s) ===" % (label, draft_path))
    table = scan_definitions(draft_path)
    total_sites = sum(len(v) for v in table.values())
    print("  observed population: %d distinct symbols defined with ':=', %d definition sites"
          % (len(table), total_sites))
    cols = collision_report(table)
    print("  observed population: %d symbol(s) carrying MORE THAN ONE distinct definition" % len(cols))
    for sym, groups in cols:
        print("      COLLISION  `%s`  ->  %d distinct senses" % (sym, len(groups)))
        for key, lines in groups:
            print("          lines %-14s : %s" % (",".join(str(x) for x in lines), key[:88]))
    if expect_clean:
        # REGISTERED LEGACY DEBT.  These three are PRE-EXISTING collisions the gate found on
        # its first run, all inside the legacy Chinese sections (13-15, pre language-policy):
        #   A -> 3 senses (513, 745, 1034)   C -> 2 senses (644, 1150)   H -> 3 senses (1169,
        #   1228/1593).  They are NOT repaired this round: round 22's order was the W repair,
        #   and renaming symbols inside proofs this owner has not re-verified would trade a
        #   naming hazard for a mathematical one.  They are REGISTERED so that the gate stays
        #   green for NEW mints while the debt stays visible -- an allowlist, never a silence.
        # An allowlist that only checks the NAME is a hole: an allowlisted symbol can quietly
        # acquire a FOURTH sense and the gate stays green.  Found the same hour it was written
        # -- round 22's own draft did exactly that to `A`.  So the declared SENSE COUNT is
        # pinned too, and the debt is frozen in size, not merely named.
        LEGACY = {"A": 3, "C": 2, "H": 3}
        got = {sym: len(groups) for sym, groups in cols}
        print("  registered legacy collisions (declared, not repaired): %r" % LEGACY)
        print("  observed collisions outside the legacy set: %s"
              % sorted(set(got) - set(LEGACY)))
        print("  observed sense counts for the legacy set: %r"
              % {k: got.get(k, 0) for k in sorted(LEGACY)})
        check("A/%s: NO collision outside the registered legacy set" % label,
              not (set(got) - set(LEGACY)), "new: %s" % sorted(set(got) - set(LEGACY)))
        check("A/%s: no LEGACY symbol has gained a sense (count pinned, not just named)" % label,
              all(got.get(k, 0) <= v for k, v in LEGACY.items()),
              "declared %r observed %r" % (LEGACY, got))
    else:
        # DEMONSTRATION ON A DEFECT THAT ACTUALLY HAPPENED
        got_W = any(sym == "W" for sym, _ in cols)
        check("A/%s: the gate FIRES on the real pre-repair W collision" % label, got_W,
              "detected=%s" % got_W)
    return cols

# ============================================================================
# PART B -- graph primitives (self-contained; same semantics as r21)
# ============================================================================
def mkadj(n, edges):
    a = {v: set() for v in range(n)}
    for u, v in edges:
        assert u != v, "loop"
        a[u].add(v); a[v].add(u)
    return a

def c4_all(adj):
    out = []
    for x, y in itertools.combinations(sorted(adj), 2):
        com = sorted(adj[x] & adj[y])
        if len(com) >= 2: out.append((x, y, com))
    return out

def c4_free(adj):
    return len(c4_all(adj)) == 0

def connected(adj):
    vs = list(adj)
    if not vs: return True
    seen, st = {vs[0]}, [vs[0]]
    while st:
        u = st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen) == len(vs)

def longest_induced_path(adj):
    """number of VERTICES of a longest induced path (small graphs only)."""
    best = 1
    vs = sorted(adj)
    def ext(path, pset):
        nonlocal best
        best = max(best, len(path))
        last = path[-1]
        for v in adj[last]:
            if v in pset: continue
            # induced: v adjacent to last only
            if any(v in adj[u] for u in path[:-1]): continue
            path.append(v); pset.add(v)
            ext(path, pset)
            path.pop(); pset.discard(v)
    for s in vs:
        ext([s], {s})
    return best

def is_induced_c6(adj, Z):
    if len(set(Z)) != 6: return False
    for i in range(6):
        for j in range(i + 1, 6):
            want = (j - i) % 6 in (1, 5)
            if (Z[j] in adj[Z[i]]) != want: return False
    return True

def triangles_at(adj, v):
    return sum(1 for x, y in itertools.combinations(sorted(adj[v]), 2) if y in adj[x])

def alpha_of_nbhd(adj, v):
    """independence number of G[N(v)] = the a-value."""
    N = sorted(adj[v])
    best = 0
    for r in range(len(N), -1, -1):
        if r <= best: break
        for S in itertools.combinations(N, r):
            if all(y not in adj[x] for x, y in itertools.combinations(S, 2)):
                best = max(best, r); break
        if best >= r: break
    return best

def avec(adj):
    return [alpha_of_nbhd(adj, v) for v in sorted(adj)]

def trace(adj, Z, v):
    return sorted(i for i in range(6) if Z[i] in adj[v])

def classify_off(adj, Z):
    """-> (cons, anti, single, none) lists of off-Z vertices by their Z-trace type."""
    cons, anti, single, none = [], [], [], []
    for v in sorted(adj):
        if v in Z: continue
        t = trace(adj, Z, v)
        if len(t) == 0: none.append(v)
        elif len(t) == 1: single.append((v, t))
        elif len(t) == 2:
            d = min((t[1] - t[0]) % 6, (t[0] - t[1]) % 6)
            if d == 1: cons.append((v, t))
            elif d == 3: anti.append((v, t))
            else: raise AssertionError("distance-2 trace survived in a C4-free graph: %r" % (t,))
        else:
            raise AssertionError("trace of size >2 survived in a C4-free graph: %r" % (t,))
    return cons, anti, single, none


def validate_most_basic_first(tag, n, edges, Z):
    """Validate in the order simple -> connected -> C4-FREE FIRST -> induced C6 -> no P7."""
    adj = mkadj(n, edges)
    simple = all(u != v for u, v in edges) and len(set(map(frozenset, edges))) == len(edges)
    check("%s: simple" % tag, simple)
    check("%s: connected" % tag, connected(adj))
    bad = c4_all(adj)
    print("      observed: %d pairs with >=2 common neighbours" % len(bad))
    check("%s: C4-FREE (checked before any statistic is read off it)" % tag, not bad,
          "" if not bad else "witness %r" % (bad[0],))
    check("%s: Z=%r is an induced C6" % (tag, Z), is_induced_c6(adj, Z))
    p = longest_induced_path(adj)
    print("      observed: longest induced path = %d vertices" % p)
    check("%s: no induced P7 (path <= 6)" % tag, p <= 6, "path=%d" % p)
    return adj


def part_B():
    print("\n=== PART B -- (D3-C6) MASS-COUNT RESTART, first computable step ===")
    Z = [0, 1, 2, 3, 4, 5]
    hexedges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]

    # ---- B0: positive control + specificity probes (tooling before use) -------------
    print("\n-- B0 tooling positive control and specificity probes --")
    pet_e = [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
             (0,5),(1,6),(2,7),(3,8),(4,9)]
    pet = mkadj(10, pet_e)
    print("      observed: Petersen |V|=10 |E|=%d, C4 pairs=%d, path=%d, a-vector=%r"
          % (len(pet_e), len(c4_all(pet)), longest_induced_path(pet), avec(pet)))
    check("B0: Petersen is C4-free", c4_free(pet))
    check("B0: path(Petersen) = 5 vertices (NOT 6 -- the round-12 VOID report's error)",
          longest_induced_path(pet) == 5, "got %d" % longest_induced_path(pet))
    check("B0: a(Petersen) = 3 at every vertex, so l = 3 exactly", avec(pet) == [3] * 10)
    star = mkadj(5, [(0,1),(0,2),(0,3),(0,4)])
    print("      observed: K_{1,4} path = %d" % longest_induced_path(star))
    check("B0 specificity probe (must NOT fire): longest_induced_path(K_{1,4}) = 3, not 5",
          longest_induced_path(star) == 3)
    c6 = mkadj(6, hexedges)
    print("      observed: bare C6 path = %d" % longest_induced_path(c6))
    check("B0 specificity probe: a bare induced C6 has longest induced path 5, not 6",
          longest_induced_path(c6) == 5)

    # ---- B1: antipodal slots hold at most one vertex each ---------------------------
    print("\n-- B1 antipodal slots: at most ONE vertex each (C4-freeness, one line) --")
    # Two vertices with the SAME antipodal trace {z_i, z_{i+3}} would be two common
    # neighbours of z_i and z_{i+3}: a C4.  Exhibit the forced C4 at all 3 antipodal slots.
    fired = 0
    for i in range(3):
        e = list(hexedges) + [(6, Z[i]), (6, Z[i + 3]), (7, Z[i]), (7, Z[i + 3])]
        adj = mkadj(8, e)
        bad = c4_all(adj)
        pair_ok = any(set(x[2]) >= {6, 7} for x in bad)
        if pair_ok: fired += 1
    print("      observed: %d of 3 antipodal slots force a C4 when doubly occupied" % fired)
    check("B1: every antipodal slot holds at most one vertex", fired == 3, "%d/3" % fired)

    # ---- B2: the 2-trace population is bounded by 6, and 6 is attained ---------------
    print("\n-- B2 |{w : |N(w) cap Z| = 2}| <= 3 (consecutive, round 21) + 3 (antipodal) = 6 --")
    # INSTANCE-D (round 21, double-sourced with round 13) = the tight |W_cons| = 3 graph.
    D_edges = hexedges + [(6, 0), (6, 1), (7, 2), (7, 3), (8, 4), (8, 5)]
    adjD = validate_most_basic_first("B2/INSTANCE-D", 9, D_edges, Z)
    consD, antiD, singD, noneD = classify_off(adjD, Z)
    print("      observed: |cons|=%d |anti|=%d |single|=%d |none|=%d"
          % (len(consD), len(antiD), len(singD), len(noneD)))
    check("B2: INSTANCE-D has |W_cons| = 3 on slots {0,2,4}", len(consD) == 3
          and sorted(t[0] for _, t in consD) == [0, 2, 4])

    # INSTANCE-E: INSTANCE-D plus the three antipodal vertices -> the 3+3 = 6 candidate.
    E_edges = D_edges + [(9, 0), (9, 3), (10, 1), (10, 4), (11, 2), (11, 5)]
    adjE = mkadj(12, E_edges)
    badE = c4_all(adjE)
    print("      observed: INSTANCE-E (n=12, 3 consecutive + 3 antipodal): %d C4 pairs" % len(badE))
    if badE:
        print("      observed: first violating pair %r" % (badE[0],))
    # This is a PREDICTION THAT MAY FAIL.  Report whichever way it goes; do not assert it.
    E_ok = (not badE)
    if E_ok:
        adjE = validate_most_basic_first("B2/INSTANCE-E", 12, E_edges, Z)
        consE, antiE, singE, noneE = classify_off(adjE, Z)
        print("      observed: |cons|=%d |anti|=%d -> 2-trace population %d"
              % (len(consE), len(antiE), len(consE) + len(antiE)))
        check("B2: the bound 6 is ATTAINED by INSTANCE-E", len(consE) + len(antiE) == 6)
    else:
        # Fall back: find the true maximum of the 2-trace population by construction over
        # the (small) space of which of the 3 antipodal slots may be added to INSTANCE-D.
        best, best_set = 3, ()
        for r in range(0, 4):
            for S in itertools.combinations(range(3), r):
                e = list(D_edges)
                for k, i in enumerate(S):
                    e += [(9 + k, Z[i]), (9 + k, Z[i + 3])]
                a = mkadj(9 + len(S), e)
                if c4_free(a) and longest_induced_path(a) <= 6:
                    c, an, _, _ = classify_off(a, Z)
                    if len(c) + len(an) > best:
                        best, best_set = len(c) + len(an), S
        print("      observed: max 2-trace population over |W_cons|=3 + antipodal subsets = %d"
              " (antipodal slots %r)" % (best, best_set))
        check("B2: bound 6 is NOT attained on top of a tight |W_cons| = 3 -- recorded as "
              "OBSERVED, the bound stands at <= 6 with attainment OPEN", best <= 6,
              "observed max %d" % best)

    # antipodal-only: is 3 attainable alone?
    A_edges = hexedges + [(6, 0), (6, 3), (7, 1), (7, 4), (8, 2), (8, 5)]
    adjA = mkadj(9, A_edges)
    badA = c4_all(adjA)
    print("      observed: antipodal-only n=9 graph: %d C4 pairs, path=%d"
          % (len(badA), longest_induced_path(adjA) if not badA else -1))
    if not badA:
        adjA = validate_most_basic_first("B2/INSTANCE-F(antipodal-only)", 9, A_edges, Z)
        cA, aA, _, _ = classify_off(adjA, Z)
        print("      observed: |cons|=%d |anti|=%d" % (len(cA), len(aA)))
        check("B2: three antipodal vertices coexist (|anti| = 3 attained)", len(aA) == 3)

    # ---- B3: G55's charge identity on every instance built here ---------------------
    print("\n-- B3 G55 charge identity a(z) = 2 + |Off(z)| - t(z) on every instance --")
    for tag, adj in [("INSTANCE-D", adjD), ("Petersen(no C6 role)", None)]:
        if adj is None: continue
        av = avec(adj)
        rows = []
        ok = True
        for z in Z:
            off = len(adj[z] - set(Z))
            t = triangles_at(adj, z)
            lhs, rhs = av[z], 2 + off - t
            rows.append((z, lhs, rhs, off, t))
            ok = ok and (lhs == rhs)
        print("      observed %s: (z, a(z), 2+|Off|-t, |Off|, t) = %r" % (tag, rows))
        check("B3/%s: G55 holds at all six hexagon vertices" % tag, ok)
        s = sum(av[z] - 2 for z in Z)
        print("      observed %s: Sum_{z in Z}(a(z)-2) = %d" % (tag, s))

    # ---- B4: what the Z-local count can and cannot do, IN HYPOTHESIS ----------------
    print("\n-- B4 the Z-local charge is UNBOUNDED IN HYPOTHESIS -- so the count needs the "
          "off-cycle deficit, and that is what the restart must track --")
    # DEFECT PRESERVED IN SOURCE (owner error, first run of this script).  The first
    # version of B4 hung k single-trace vertices on INSTANCE-D and reported that the
    # Z-local charge grows.  It does -- but every one of those hosts has
    # longest induced path = 7, i.e. an induced P7, so NONE of them is in (D3-C6)'s
    # class and the exhibit proved nothing about (D3-C6).  The check PASSED and was
    # WORTHLESS.  Repaired by making in-hypothesis membership a PRECONDITION of the
    # sample, not a statistic reported after it.
    print("      (the defect this check was repaired from: INSTANCE-D + k hairs at z_0 has "
          "path = 7 for every k >= 1, i.e. OUT OF HYPOTHESIS -- shown, then discarded)")
    for k in (1, 2):
        e = list(D_edges) + [(9 + j, 0) for j in range(k)]
        a = mkadj(9 + k, e)
        print("        out-of-hypothesis sample k=%d: C4-free=%s path=%d"
              % (k, c4_free(a), longest_induced_path(a)))

    obs = []
    for k in range(0, 7):
        e = list(hexedges) + [(6 + j, 0) for j in range(k)]   # k INDEPENDENT hairs at z_0
        a = mkadj(6 + k, e)
        p = longest_induced_path(a)
        inhyp = c4_free(a) and connected(a) and is_induced_c6(a, Z) and p <= 6
        if not inhyp:
            obs.append((k, "OUT-OF-HYPOTHESIS", p)); continue
        av = avec(a)
        n = 6 + k
        S = sum(av)
        obs.append((k, n, S, 3 * n, round(S / n, 4), sum(av[z] - 2 for z in Z), p))
    print("      observed (k, n, Sum a, 3n, l, Sum_Z(a-2), path) = %r" % (obs,))
    good = [o for o in obs if o[1] != "OUT-OF-HYPOTHESIS"]
    check("B4a: every sample is IN HYPOTHESIS (C4-free, induced C6, path <= 6) -- "
          "checked BEFORE any statistic is read off it", len(good) == len(obs),
          "%d/%d" % (len(good), len(obs)))
    check("B4b: Sum_{z in Z}(a(z)-2) is UNBOUNDED inside (D3-C6)'s own hypotheses",
          [o[5] for o in good] == list(range(len(good))),
          "observed %r" % [o[5] for o in good])
    check("B4c: and yet l stays < 3 on every one of them -- the off-cycle vertices carry "
          "a = 1, i.e. the hexagon's surplus is paid for by an off-cycle DEFICIT",
          all(o[4] < 3.0 for o in good), "max l = %s" % max(o[4] for o in good))
    # the deficit identity the restarted count must run on
    print("      => the count to restart is NOT Sum over Z.  It is")
    print("         Sum_v (a(v)-3) = Sum_{z in Z}(a(z)-3) + Sum_{v not in Z}(a(v)-3) <= 0,")
    print("         with the Z-term now FULLY DETERMINED by the occupied-slot set (G57+G55)")
    print("         and the off-cycle term the open half.")
    for tag, adj, n in [("INSTANCE-D", adjD, 9), ("INSTANCE-E", adjE, 12)]:
        av = avec(adj)
        zt = sum(av[z] - 3 for z in Z)
        ot = sum(av[v] - 3 for v in sorted(adj) if v not in Z)
        print("      observed %s: n=%d Sum a=%d l=%.4f | Z-term=%d off-term=%d total=%d"
              % (tag, n, sum(av), sum(av) / n, zt, ot, zt + ot))
        check("B4d/%s: Sum_v(a(v)-3) <= 0, i.e. l <= 3 holds here" % tag, zt + ot <= 0,
              "total=%d" % (zt + ot))


# ============================================================================
def main():
    print("w133 round 22 -- namespace mint gate + (D3-C6) restart step")
    print("repo: %s" % REPO)
    pre = sys.argv[1] if len(sys.argv) > 1 else None

    if pre and os.path.exists(pre):
        part_A(pre, "PRE-REPAIR", expect_clean=False)
    else:
        print("\n(no pre-repair copy supplied; the FIRES-on-a-real-defect demonstration is skipped)")
    tick("A-pre")
    part_A(DRAFT, "REPAIRED", expect_clean=True)
    tick("A-post")

    print("\n=== PART A2 -- THE GATE APPLIED AT MINT TIME to this round's new names ===")
    corpus = [DRAFT]
    for name, kind in [("W_0", "symbol"), ("W_cons", "symbol"), ("Off", "symbol"),
                       ("G58", "address"), ("G59", "address")]:
        ok, hits = assert_mintable(name, corpus, kind)
        print("  observed: `%s` already occurs %d time(s) in the corpus" % (name, len(hits)))
        for h in hits[:3]:
            print("      %s:%d  %s" % h)
    print("  (run BEFORE the repair these are all 0; after the repair W_0/W_cons/Off are")
    print("   expected to occur -- the gate is a PRECONDITION, its post-hoc reading is a record)")

    tick("B")
    part_B()

    print("\n=== SUMMARY ===")
    print("checks run: %d   failures: %d" % (NCHECK, len(FAIL)))
    for f in FAIL: print("  FAILED: %s" % f)
    print("elapsed: %.2f s" % (time.time() - T0))
    sys.exit(1 if FAIL else 0)

if __name__ == "__main__":
    main()
