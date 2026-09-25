#!/usr/bin/env python3
"""
w133 round 26 — HELD-OUT KEY for the verification gate on the chain
    G58 (S35) -> G59/(B),(B') (S36) -> S37 (Z1..Z6) => (D3-C6).

OPS-3c: the withheld quantities are exactly the ones the LOAD-BEARING step (Z1) depends on:
    Sigma_{z in Z}(a(z)-3), T_Z, |W_1|, |W_cons|, |W_anti|, n_3, Sigma_v(a(v)-3).

B6 BY ROLE OF OBJECT: the hosts built here are TEST GRAPHS ONLY.  They are never class
instances in any argument, they are never named in the brief, and nothing in the brief asks
the judge to reason about them.  The attainment witnesses that DO carry a mathematical role
(the n=10 (n_3,m)=(0,3) region and the n=10 two-leak region) are DISCLOSED in the brief with
their longest induced paths, because the sharpness claims ARE claims about them.

RULING CQ: every detector whose output is a NEGATIVE is positive-controlled before use.
RULING BM: in-hypothesis membership is a PRECONDITION enforced by the Sample object; a
statistic read off an unadmitted or rejected sample raises.

Exit 0 iff every control passes and every host is admitted.  Exit 2 on any failure.
"""
import sys, itertools

# ----------------------------------------------------------------------------- graph basics
class G:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [set() for _ in range(n)]
        for a, b in edges:
            if a == b:
                raise ValueError("loop")
            self.adj[a].add(b)
            self.adj[b].add(a)
    def edges(self):
        return sorted((a, b) for a in range(self.n) for b in self.adj[a] if a < b)
    def deg(self, v):
        return len(self.adj[v])
    def t(self, v):
        """edges inside N(v)"""
        nb = sorted(self.adj[v])
        return sum(1 for i in range(len(nb)) for j in range(i + 1, len(nb)) if nb[j] in self.adj[nb[i]])
    def a(self, v):
        """a(v) = d(v) - t(v);  G55 says G[N(v)] is a matching, so a(v) counts the matching's
        unmatched vertices plus its edges -- but the DEFINITION used everywhere is d - t."""
        return self.deg(v) - self.t(v)
    def connected(self):
        seen = {0}
        st = [0]
        while st:
            u = st.pop()
            for w in self.adj[u]:
                if w not in seen:
                    seen.add(w)
                    st.append(w)
        return len(seen) == self.n

def has_C4(g):
    for a, b in itertools.combinations(range(g.n), 2):
        if len(g.adj[a] & g.adj[b]) >= 2:
            return True
    return False

def induced_cycle6(g, Z):
    """Z is an induced C6 in cyclic order."""
    k = len(Z)
    if k != 6 or len(set(Z)) != 6:
        return False
    for i in range(6):
        for j in range(i + 1, 6):
            adjacent = (Z[j] in g.adj[Z[i]])
            consecutive = ((j - i) % 6 == 1) or ((i - j) % 6 == 1)
            if adjacent != consecutive:
                return False
    return True

def longest_induced_path(g):
    """TRUSTED implementation: exhaustive DFS over induced paths, returns #VERTICES."""
    best = 0
    def ext(path, pset):
        nonlocal best
        if len(path) > best:
            best = len(path)
        last = path[-1]
        for w in g.adj[last]:
            if w in pset:
                continue
            # induced: w must not touch any earlier path vertex except `last`
            if any(w in g.adj[u] for u in path[:-1]):
                continue
            path.append(w); pset.add(w)
            ext(path, pset)
            path.pop(); pset.discard(w)
    for s in range(g.n):
        ext([s], {s})
    return best

# ----------------------------------------------------------------- RULING BM: Sample object
class Sample:
    """A host is ADMITTED before any statistic is read off it, or reads raise."""
    def __init__(self, name, g, Z):
        self.name, self.g, self.Z = name, g, Z
        self.reasons = []
        ok = True
        if not g.connected():
            ok = False; self.reasons.append("not connected")
        if has_C4(g):
            ok = False; self.reasons.append("contains a C4")
        if not induced_cycle6(g, Z):
            ok = False; self.reasons.append("Z is not an induced C6")
        p = longest_induced_path(g)
        if p >= 7:
            ok = False; self.reasons.append("induced P7 present (path=%d)" % p)
        self.path = p
        self.admitted = ok
    def require(self):
        if not self.admitted:
            raise RuntimeError("statistic read off an unadmitted sample %s: %s"
                               % (self.name, "; ".join(self.reasons)))
    # ---- the withheld quantities (all require admission first)
    def trace(self, v):
        return tuple(sorted(i for i, z in enumerate(self.Z) if z in self.g.adj[v]))
    def census(self):
        self.require()
        W1 = W_cons = W_anti = W0 = 0
        for v in range(self.g.n):
            if v in self.Z:
                continue
            T = self.trace(v)
            if len(T) == 0:
                W0 += 1
            elif len(T) == 1:
                W1 += 1
            elif len(T) == 2:
                d = (T[1] - T[0]) % 6
                if d in (1, 5):
                    W_cons += 1
                elif d == 3:
                    W_anti += 1
                else:
                    raise RuntimeError("illegal 2-trace %s on %s (G54 violated)" % (T, self.name))
            else:
                raise RuntimeError("trace of size %d on %s (G54 violated)" % (len(T), self.name))
        return dict(W1=W1, W_cons=W_cons, W_anti=W_anti, W0=W0)
    def T_Z(self):
        self.require()
        return sum(self.g.t(z) for z in self.Z)
    def sum_Z_charge(self):
        self.require()
        return sum(self.g.a(z) - 3 for z in self.Z)
    def sum_charge(self):
        self.require()
        return sum(self.g.a(v) - 3 for v in range(self.g.n))
    def n3(self):
        self.require()
        c = 0
        for v in range(self.g.n):
            if v in self.Z:
                continue
            if len(self.trace(v)) == 1 and self.g.a(v) == 3:
                c += 1
        return c

FAIL = []
def check(label, got, want):
    ok = (got == want)
    print("  [%s] %-58s got=%s want=%s" % ("OK" if ok else "FAIL", label, got, want))
    if not ok:
        FAIL.append(label)

# ============================================================== PART 0 -- POSITIVE CONTROLS
print("=" * 78)
print("PART 0 -- POSITIVE CONTROLS (RULING CQ: a detector whose output is a NEGATIVE is")
print("          silent when broken, so it is controlled on inputs where the answer is YES)")
print("=" * 78)

# Petersen: C4-free, longest induced path = 5, a(v) == 3 for all v
pet_e = [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
         (0,5),(1,6),(2,7),(3,8),(4,9)]
pet = G(10, pet_e)
check("Petersen is C4-free (has_C4 says NO)", has_C4(pet), False)
check("Petersen longest induced path = 5 vertices", longest_induced_path(pet), 5)
check("Petersen a(v) == 3 for every v", sorted({pet.a(v) for v in range(10)}), [3])

# POSITIVE control for the C4 detector: it must say YES on a graph that HAS one.
c4 = G(4, [(0,1),(1,2),(2,3),(3,0)])
check("C4 detector fires on an actual C4 (YES)", has_C4(c4), True)
k24 = G(6, [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)])
check("C4 detector fires on K_{2,3} (two common nbrs, YES)", has_C4(k24), True)

# POSITIVE controls for the induced-path finder: inputs where the answer is a long YES.
p7 = G(7, [(i, i+1) for i in range(6)])
check("bare P7 -> longest induced path = 7 (positive control)", longest_induced_path(p7), 7)
p9 = G(9, [(i, i+1) for i in range(8)])
check("bare P9 -> longest induced path = 9 (positive control)", longest_induced_path(p9), 9)
c6 = G(6, [(i, (i+1) % 6) for i in range(6)])
check("bare induced C6 -> longest induced path = 5", longest_induced_path(c6), 5)
star = G(5, [(0,1),(0,2),(0,3),(0,4)])
check("K_{1,4} -> longest induced path = 3", longest_induced_path(star), 3)
check("K_{1,4}: a(centre) = 4 - 0 = 4", star.a(0), 4)
tri = G(3, [(0,1),(1,2),(2,0)])
check("triangle: a(v) = 2 - 1 = 1 (t counts the N(v) edge)", tri.a(0), 1)

# induced-C6 detector positive AND negative control
check("induced_cycle6 accepts the bare hexagon", induced_cycle6(c6, [0,1,2,3,4,5]), True)
c6chord = G(6, [(i, (i+1) % 6) for i in range(6)] + [(0,3)])
check("induced_cycle6 rejects a chorded hexagon", induced_cycle6(c6chord, [0,1,2,3,4,5]), False)

# Sample object refuses to answer on a rejected sample (RULING BM, controlled positively)
bad = Sample("CONTROL-REJECT", c6chord, [0,1,2,3,4,5])
try:
    bad.census()
    check("Sample refuses statistics on a rejected sample", "no raise", "RuntimeError")
except RuntimeError:
    check("Sample refuses statistics on a rejected sample", "RuntimeError", "RuntimeError")

# ================================================= PART 1 -- THE HELD-OUT TEST HOSTS
print()
print("=" * 78)
print("PART 1 -- HELD-OUT TEST HOSTS (built this round, never shipped to any engine)")
print("          ROLE: test graphs only.  They are NOT class instances in any argument and")
print("          the brief asks the judge to reason about them NOWHERE.")
print("=" * 78)

Z = [0, 1, 2, 3, 4, 5]
HEX = [(i, (i + 1) % 6) for i in range(6)]

# ------------------------------------------------------------------------------------------
# THE HOSTS ARE SEARCHED, NOT HAND-BUILT.  The first draft of this script hand-built three
# hosts; the Sample object REJECTED ALL THREE (induced P7 at path = 8, 7, 7).  That is
# RULING BW firing again on a hand construction, caught this time by the precondition object
# rather than by an author reading his own witness -- so the hosts below are produced by a
# deterministic search whose acceptance test IS the admission test.
# ------------------------------------------------------------------------------------------
import random

LEGAL_TRACES = [()] + [(i,) for i in range(6)] \
             + [(i, (i + 1) % 6) for i in range(6)] \
             + [(i, (i + 3) % 6) for i in range(3)]
LEGAL_TRACES = [tuple(sorted(t)) for t in LEGAL_TRACES]

def search_hosts(k_off, want, tries=40000, seed=20260823, pool=None):
    """Return the first admitted host on 6+k_off vertices satisfying predicate `want`."""
    rng = random.Random(seed)
    P = pool if pool is not None else LEGAL_TRACES
    for _ in range(tries):
        n = 6 + k_off
        edges = list(HEX)
        for j in range(k_off):
            T = P[rng.randrange(len(P))]
            for z in T:
                edges.append((6 + j, z))
        for j1 in range(k_off):
            for j2 in range(j1 + 1, k_off):
                if rng.random() < 0.35:
                    edges.append((6 + j1, 6 + j2))
        g = G(n, edges)
        S = Sample("cand", g, Z)
        if not S.admitted:
            continue
        try:
            if want(S):
                return g, S
        except RuntimeError:
            continue
    return None, None

def _w(S):
    return S.census()

SINGLES = [(i,) for i in range(6)]
K1, S1 = search_hosts(5, lambda S: _w(S)["W1"] >= 4 and S.n3() >= 1, pool=SINGLES)
if K1 is None:   # a leak is not guaranteed at this size; fall back to W_1-rich without one
    K1, S1 = search_hosts(5, lambda S: _w(S)["W1"] >= 4, pool=SINGLES)
K2, S2 = search_hosts(6, lambda S: _w(S)["W_anti"] >= 1 and _w(S)["W0"] >= 1
                                   and _w(S)["W_cons"] >= 1)
K3, S3 = search_hosts(4, lambda S: _w(S)["W1"] >= 2 and _w(S)["W_anti"] == 0)
for nm, g in (("K1", K1), ("K2", K2), ("K3", K3)):
    if g is None:
        print("SEARCH FAILED for %s" % nm)
        sys.exit(2)
S1.name, S2.name, S3.name = "K1", "K2", "K3"

# K4 -- a DELIBERATE OUT-OF-CLASS decoy, so that "is it C4-free?" and "how long is the longest
# induced path?" cannot be answered by GUESSING the class hypotheses.  A judge who assumes every
# printed graph is in hypothesis gets V3 and V6 wrong; that is what the decoy is for.
def make_decoy(g):
    for a in range(g.n):
        for b in range(a + 1, g.n):
            if b in g.adj[a]:
                continue
            h = G(g.n, g.edges() + [(a, b)])
            if has_C4(h):
                return h, (a, b)
    return None, None
K4, DECOY_EDGE = make_decoy(K1)
if K4 is None:
    print("DECOY CONSTRUCTION FAILED"); sys.exit(2)
S4 = Sample("K4", K4, Z)
print("  K4 (DECOY, out of class by construction): n=%d m=%d added-edge=%s admitted=%s path=%d"
      % (K4.n, len(K4.edges()), DECOY_EDGE, S4.admitted, S4.path))
if S4.admitted:
    print("  DECOY IS STILL IN HYPOTHESIS -- it is not a decoy"); sys.exit(2)
C4WITNESS = None
for a, b in itertools.combinations(range(K4.n), 2):
    common = sorted(K4.adj[a] & K4.adj[b])
    if len(common) >= 2:
        C4WITNESS = (a, common[0], b, common[1]); break

for S in (S1, S2, S3):
    print("  %s: n=%d  m=%d  admitted=%s  path=%d  %s"
          % (S.name, S.g.n, len(S.g.edges()), S.admitted, S.path,
             "" if S.admitted else "REASONS: " + "; ".join(S.reasons)))
    if not S.admitted:
        FAIL.append("host %s not in hypothesis" % S.name)

if FAIL:
    print()
    print("ABORT: controls or admission failed: %s" % FAIL)
    sys.exit(2)

# ================================================= PART 2 -- THE KEY
print()
print("=" * 78)
print("PART 2 -- THE KEY (rows V1..V9).  TIERS ARE PRE-REGISTERED AND ARE DISCLOSED IN THE")
print("          BRIEF.  Tier H = bounded local inspection of the printed edge list.")
print("          Tier C = not reliably hand-derivable; CANNOT COMPUTE is an accepted answer.")
print("=" * 78)

rows = []
def row(rid, tier, question, answer):
    rows.append((rid, tier, question, answer))

c1 = S1.census(); c2 = S2.census()

row("V1", "H", "K1: number of edges", len(K1.edges()))
VSTAR = max(range(6, K1.n), key=lambda v: (K1.deg(v), -v))
row("V2", "H", "K1: degree of vertex %d" % VSTAR, K1.deg(VSTAR))
row("V3", "H", "which of K1,K2,K3,K4 contains a 4-cycle, and its 4 vertices",
    ("K4", C4WITNESS))
row("V4", "H", "K1: trace census |W_1|,|W_cons|,|W_anti|,|W_0|",
    (c1["W1"], c1["W_cons"], c1["W_anti"], c1["W0"]))
row("V5", "H", "K1: a(%d) = d - t at that vertex" % VSTAR, K1.a(VSTAR))
row("V6", "C", "K4: longest induced path, in VERTICES", S4.path)
row("V7", "C", "K1: T_Z = sum_{z in Z} t(z), and sum_{z in Z}(a(z)-3)",
    (S1.T_Z(), S1.sum_Z_charge()))
row("V8", "C", "K2: sum_{v in V}(a(v)-3), and n_3", (S2.sum_charge(), S2.n3()))
row("V9", "C", "K3: T_Z, and sum_{v in V}(a(v)-3)", (S3.T_Z(), S3.sum_charge()))

for rid, tier, q, a in rows:
    print("  %s [Tier %s]  %-58s = %s" % (rid, tier, q, a))

# ------------------------------------------------- PART 3 -- the identity (Z1) rests on
print()
print("=" * 78)
print("PART 3 -- G55-SUMMED, THE IDENTITY (Z1) IS ARITHMETIC ON, re-verified on these hosts")
print("          sum_{z in Z}(a(z)-3) == |W_1| + 2|W_cons| + 2|W_anti| - T_Z - 6")
print("=" * 78)
for S, c in ((S1, c1), (S2, c2), (S3, S3.census())):
    lhs = S.sum_Z_charge()
    rhs = c["W1"] + 2 * c["W_cons"] + 2 * c["W_anti"] - S.T_Z() - 6
    check("%s: G55-summed identity holds (lhs=%d)" % (S.name, lhs), lhs, rhs)
    # and (Z1) itself must hold on every admitted host
    bound = S.n3() + 2 * c["W_anti"] - 6
    ok = S.sum_charge() <= bound
    print("  [%s] %-58s sum=%d  bound(n3+2m-6)=%d"
          % ("OK" if ok else "FAIL", "%s: (Z1) sum_v(a-3) <= n_3 + 2m - 6" % S.name,
             S.sum_charge(), bound))
    if not ok:
        FAIL.append("%s violates (Z1)" % S.name)
    ok6 = S.n3() + 2 * c["W_anti"] <= 6
    print("  [%s] %-58s n_3+2m=%d" % ("OK" if ok6 else "FAIL",
          "%s: (Z6) n_3 + 2m <= 6" % S.name, S.n3() + 2 * c["W_anti"]))
    if not ok6:
        FAIL.append("%s violates (Z6)" % S.name)

# ------------------------------------------------- PART 4 -- key file
print()
if FAIL:
    print("KEY NOT WRITTEN -- failures: %s" % FAIL)
    sys.exit(2)

with open("problems/wowii/w133_r26_key.key.txt", "w") as f:
    f.write("# w133 r26 HELD-OUT KEY -- NEVER SHIPPED.  Built %s.\n" % "2026-08-23 r26")
    f.write("# Hosts are TEST GRAPHS ONLY (B6 by role of object).\n")
    for name, g in (("K1", K1), ("K2", K2), ("K3", K3), ("K4", K4)):
        f.write("%s edges: %s\n" % (name, g.edges()))
    for rid, tier, q, a in rows:
        f.write("%s\t%s\t%s\t%s\n" % (rid, tier, q, a))
print("KEY WRITTEN: problems/wowii/w133_r26_key.key.txt   rows=%d" % len(rows))
print()
print("CHECKS RUN: all controls above.  FAILURES: %d" % len(FAIL))
print("KEY_STATUS=PASS")
sys.exit(0)
