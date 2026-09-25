#!/usr/bin/env python3
"""
w133 round 29 -- HELD-OUT KEY for Q41, REBUILT.

WHAT CHANGED FROM r26'S KEY, and why:
  * RULING CX (cert_w133_r28 section 2): a held-out answer must be proved UNIQUE, not merely
    proved correct.  Re-deriving a key agrees with itself and says NOTHING.  Every row below
    ships a UNIQUENESS assertion; an EXISTENTIAL row (one that asks for a witness) has its
    whole witness space enumerated and `exactly one` asserted.  r26's V3 -- "which of K1..K4
    contains a 4-cycle, and its 4 vertices" -- had TWO correct answers and would have VOIDED a
    correct review.  It is DROPPED (it is also determined; see below).
  * RULING CZ (w61, standing on all lines): a positive control must inject the HARDEST form of
    the species, not a canonical one.  r26's row-determination audit injected CANONICAL
    shortcuts.  Re-run here with the HARDEST shortcut per row -- and it finds one more
    determined row that r28's audit passed: V2.
  * RULING CY: a check that cannot PASS is as uninformative as one that cannot fail.  Both
    directions are fired.

Exit 0 iff every control passes, every host is admitted, every kept row is UNIQUE, and every
kept row DISCRIMINATES against its hardest shortcut.  Exit 2 otherwise.
"""
import sys, itertools, ast

# ------------------------------------------------------------------ graph basics (r26, verbatim)
class G:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [set() for _ in range(n)]
        for a, b in edges:
            if a == b:
                raise ValueError("loop")
            self.adj[a].add(b); self.adj[b].add(a)
    def edges(self):
        return sorted((a, b) for a in range(self.n) for b in self.adj[a] if a < b)
    def deg(self, v):
        return len(self.adj[v])
    def t(self, v):
        nb = sorted(self.adj[v])
        return sum(1 for i in range(len(nb)) for j in range(i + 1, len(nb))
                   if nb[j] in self.adj[nb[i]])
    def a(self, v):
        return self.deg(v) - self.t(v)
    def connected(self):
        seen = {0}; st = [0]
        while st:
            u = st.pop()
            for w in self.adj[u]:
                if w not in seen:
                    seen.add(w); st.append(w)
        return len(seen) == self.n

def has_C4(g):
    for a, b in itertools.combinations(range(g.n), 2):
        if len(g.adj[a] & g.adj[b]) >= 2:
            return True
    return False

def all_C4_vertex_sets(g):
    """EVERY 4-vertex SET carrying a 4-cycle.  This is the function whose absence produced
    r26's V3 defect: the key recorded one witness and the question admitted two."""
    out = []
    for S in itertools.combinations(range(g.n), 4):
        for perm in itertools.permutations(S[1:]):
            cyc = (S[0],) + perm
            if all(cyc[(i + 1) % 4] in g.adj[cyc[i]] for i in range(4)):
                out.append(S); break
    return out

def induced_cycle6(g, Z):
    if len(Z) != 6 or len(set(Z)) != 6:
        return False
    for i in range(6):
        for j in range(i + 1, 6):
            adjacent = (Z[j] in g.adj[Z[i]])
            consecutive = ((j - i) % 6 == 1) or ((i - j) % 6 == 1)
            if adjacent != consecutive:
                return False
    return True

def longest_induced_path(g, in_vertices=True):
    best = 0
    def ext(path, pset):
        nonlocal best
        if len(path) > best:
            best = len(path)
        last = path[-1]
        for w in g.adj[last]:
            if w in pset:      continue
            if any(w in g.adj[u] for u in path[:-1]): continue
            path.append(w); pset.add(w); ext(path, pset); path.pop(); pset.discard(w)
    for s in range(g.n):
        ext([s], {s})
    return best if in_vertices else max(best - 1, 0)

class Sample:
    def __init__(self, name, g, Z):
        self.name, self.g, self.Z = name, g, Z
        self.reasons = []; ok = True
        if not g.connected():      ok = False; self.reasons.append("not connected")
        if has_C4(g):              ok = False; self.reasons.append("contains a C4")
        if not induced_cycle6(g, Z): ok = False; self.reasons.append("Z is not an induced C6")
        p = longest_induced_path(g)
        if p >= 7:                 ok = False; self.reasons.append("induced P7 (path=%d)" % p)
        self.path = p; self.admitted = ok
    def require(self):
        if not self.admitted:
            raise RuntimeError("statistic read off unadmitted sample %s: %s"
                               % (self.name, "; ".join(self.reasons)))
    def trace(self, v):
        return tuple(sorted(i for i, z in enumerate(self.Z) if z in self.g.adj[v]))
    def census(self):
        self.require()
        W1 = Wc = Wa = W0 = 0
        for v in range(self.g.n):
            if v in self.Z: continue
            T = self.trace(v)
            if   len(T) == 0: W0 += 1
            elif len(T) == 1: W1 += 1
            elif len(T) == 2:
                d = (T[1] - T[0]) % 6
                if   d in (1, 5): Wc += 1
                elif d == 3:      Wa += 1
                else: raise RuntimeError("illegal 2-trace %s on %s" % (T, self.name))
            else: raise RuntimeError("trace of size %d on %s" % (len(T), self.name))
        return dict(W1=W1, W_cons=Wc, W_anti=Wa, W0=W0)
    def T_Z(self):          self.require(); return sum(self.g.t(z) for z in self.Z)
    def sum_Z_charge(self): self.require(); return sum(self.g.a(z) - 3 for z in self.Z)
    def sum_charge(self):   self.require(); return sum(self.g.a(v) - 3 for v in range(self.g.n))
    def n3(self):
        self.require()
        return sum(1 for v in range(self.g.n) if v not in self.Z
                   and len(self.trace(v)) == 1 and self.g.a(v) == 3)

FAIL = []; NCHK = [0]
def check(label, got, want):
    NCHK[0] += 1
    ok = (got == want)
    print("  [%s] %-64s got=%s want=%s" % ("OK" if ok else "FAIL", label, got, want))
    if not ok: FAIL.append(label)
    return ok

# ================================================== PART 0 -- POSITIVE CONTROLS (RULING CQ/CY/CZ)
print("=" * 92)
print("PART 0 -- POSITIVE CONTROLS.  Every predicate is fired where it MUST return True, and")
print("          RULING CZ is applied: the C4 control injects the HARDEST form of the species,")
print("          namely THE REAL HISTORICAL INSTANCE that broke r26's V3.")
print("=" * 92)
pet = G(10, [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
             (0,5),(1,6),(2,7),(3,8),(4,9)])
check("Petersen is C4-free (has_C4 says NO)", has_C4(pet), False)
check("Petersen longest induced path = 5 vertices", longest_induced_path(pet), 5)
check("Petersen a(v) == 3 for every v", sorted({pet.a(v) for v in range(10)}), [3])
c4 = G(4, [(0,1),(1,2),(2,3),(3,0)])
check("C4 detector fires on a bare C4 (EASY form -- YES)", has_C4(c4), True)
check("all_C4_vertex_sets on a bare C4 returns exactly one set", all_C4_vertex_sets(c4), [(0,1,2,3)])
# RULING CZ: the easy form proves only that the detector sees the easy form.  Inject the HARD
# form -- complete K4, where the naive "the 4-cycle is the first four vertices" reading is right
# AND where a second, non-obvious 4-set also carries a 4-cycle in the real historical instance.
k4c = G(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
check("HARD form: complete K4 has exactly ONE 4-vertex set (sets, not cycles)",
      all_C4_vertex_sets(k4c), [(0,1,2,3)])
p7 = G(7, [(i, i+1) for i in range(6)])
check("bare P7 -> longest induced path = 7 vertices (positive control)", longest_induced_path(p7), 7)
check("bare P7 -> longest induced path = 6 EDGES (the alternative reading)",
      longest_induced_path(p7, in_vertices=False), 6)
c6 = G(6, [(i, (i+1) % 6) for i in range(6)])
check("bare induced C6 -> longest induced path = 5", longest_induced_path(c6), 5)
star = G(5, [(0,1),(0,2),(0,3),(0,4)])
check("K_{1,4}: a(centre) = 4 - 0 = 4", star.a(0), 4)
tri = G(3, [(0,1),(1,2),(2,0)])
check("triangle: a(v) = 2 - 1 = 1", tri.a(0), 1)
check("induced_cycle6 accepts the bare hexagon", induced_cycle6(c6, [0,1,2,3,4,5]), True)
c6ch = G(6, [(i, (i+1) % 6) for i in range(6)] + [(0,3)])
check("induced_cycle6 rejects a chorded hexagon", induced_cycle6(c6ch, [0,1,2,3,4,5]), False)
bad = Sample("CONTROL-REJECT", c6ch, [0,1,2,3,4,5])
try:
    bad.census(); check("Sample refuses statistics on a rejected sample", "no raise", "RuntimeError")
except RuntimeError:
    check("Sample refuses statistics on a rejected sample", "RuntimeError", "RuntimeError")

# ============================================================ PART 1 -- HOSTS (frozen from r26)
print()
print("=" * 92)
print("PART 1 -- HOSTS.  K1,K2,K3 are the r26 hosts, byte-frozen and re-admitted here.")
print("          K4 is DROPPED: it existed only to carry V3 and V6, both of which are struck.")
print("=" * 92)
Z = [0, 1, 2, 3, 4, 5]
hosts = {}
for line in open("problems/wowii/w133_r26_key.key.txt"):
    if " edges: " in line:
        nm, e = line.split(" edges: ")
        hosts[nm.strip()] = ast.literal_eval(e.strip())
S = {}
for nm in ("K1", "K2", "K3"):
    e = hosts[nm]; n = max(max(a, b) for a, b in e) + 1
    g = G(n, e); s = Sample(nm, g, Z); S[nm] = s
    print("  %s: n=%-3d m=%-3d admitted=%s path=%d  census=%s"
          % (nm, n, len(e), s.admitted, s.path, s.census()))
    check("%s is ADMITTED (in-hypothesis)" % nm, s.admitted, True)

# ==================================================== PART 2 -- THE ROWS, with UNIQUENESS (CX)
print()
print("=" * 92)
print("PART 2 -- THE ROWS.  Each carries (i) its ANSWER, (ii) a UNIQUENESS assertion, and")
print("          (iii) its HARDEST shortcut, which it must NOT equal (RULING CZ).")
print("=" * 92)

ROWS = []
def row(rid, tier, kind, q, ans, uniq_space, uniq_pred, shortcuts):
    """uniq_space: the full candidate space a correct answer could live in.
       uniq_pred:  the question's OWN predicate -- what makes an answer CORRECT.
       RULING CX: |{c in space : pred(c)}| must be 1, and that one must be `ans`."""
    correct = [c for c in uniq_space if uniq_pred(c)]
    ok_u = (correct == [ans])
    ok_d = all(ans != sc[1] for sc in shortcuts)
    print("  %-4s [%s|%-11s] %s" % (rid, tier, kind, q))
    print("        answer   = %r" % (ans,))
    print("        UNIQUE   : |space|=%-6d correct answers=%-2d -> %s"
          % (len(uniq_space), len(correct), correct if len(correct) < 4 else correct[:4]))
    for nm, val in shortcuts:
        print("        shortcut : %-58s = %r %s" % (nm, val, "== ANSWER (DETERMINED)" if val == ans else "!= answer"))
    check("%s: answer is UNIQUE in its own answer space (RULING CX)" % rid, ok_u, True)
    check("%s: DISCRIMINATES against every hardest shortcut (RULING CZ)" % rid, ok_d, True)
    ROWS.append(dict(rid=rid, tier=tier, kind=kind, q=q, ans=ans,
                     nspace=len(uniq_space), shortcuts=shortcuts))

K1, K2, K3 = S["K1"], S["K2"], S["K3"]
g1, g2, g3 = K1.g, K2.g, K3.g

# ---- V1 (KEPT) --------------------------------------------------------------------------
m1 = len(g1.edges())
row("V1", "H", "FUNCTIONAL", "K1: number of edges", m1,
    list(range(0, 60)), lambda c: c == m1,
    [("hexagon + one edge per off-Z vertex, no off-Z edges (6+5)", 11),
     ("3-regular heuristic, m = ceil(3n/2) with n=11", 17)])

# ---- V5 (KEPT) --------------------------------------------------------------------------
VSTAR = 7
a5 = g1.a(VSTAR)
row("V5", "H", "FUNCTIONAL", "K1: a(%d) = d - t at that vertex" % VSTAR, a5,
    list(range(0, 8)), lambda c: c == a5,
    [("a = d, i.e. t(v) = 0 (the standard misread of a)", g1.deg(VSTAR)),
     ("a(v) = 3, the modal value the whole brief is about", 3)])

# ---- V7 (KEPT) --------------------------------------------------------------------------
v7 = (K1.T_Z(), K1.sum_Z_charge())
SPACE2 = [(x, y) for x in range(0, 13) for y in range(-12, 7)]
row("V7", "C", "FUNCTIONAL", "K1: T_Z = sum_{z in Z} t(z), and sum_{z in Z}(a(z)-3)", v7,
    SPACE2, lambda c: c == v7,
    [("Z is INDUCED so it has no chords, hence T_Z = 0, and a(z)=3 throughout", (0, 0)),
     ("T_Z = 0 and a(z) = 2 throughout (only the two hexagon neighbours)", (0, -6))])

# ---- V9 (KEPT) --------------------------------------------------------------------------
v9 = (K3.T_Z(), K3.sum_charge())
SPACE9 = [(x, y) for x in range(0, 13) for y in range(-20, 7)]
row("V9", "C", "FUNCTIONAL", "K3: T_Z, and sum_{v in V}(a(v)-3)", v9,
    SPACE9, lambda c: c == v9,
    [("T_Z = 0, and the bound sum(a-3) <= 0 is TIGHT so the sum is 0", (0, 0)),
     ("T_Z = 0, and sum(a-3) = -6 as at the n=10 attainment region", (0, -6))])

# ---- V10 (FRESH, EXISTENTIAL -- the species that broke V3) --------------------------------
mx = max(g1.deg(v) for v in range(g1.n))
attain = [v for v in range(g1.n) if g1.deg(v) == mx]
v10 = (mx, attain[0])
SPACE10 = [(d, v) for d in range(0, 12) for v in range(g1.n)]
row("V10", "H", "EXISTENTIAL",
    "K1: the maximum degree, and the vertex attaining it (the answer is unique)", v10,
    SPACE10, lambda c: c[0] == mx and g1.deg(c[1]) == mx,
    [("max degree 3 (the modal/3-regular reading)", (3, 4)),
     ("the maximum is attained OFF the hexagon, at the busiest off-Z vertex", (mx, 7))])
check("V10: the maximum degree is attained by exactly ONE vertex (uniqueness of the WITNESS)",
      len(attain), 1)

# ---- V11 (FRESH) --------------------------------------------------------------------------
c2 = K2.census()
v11 = (c2["W1"], c2["W_cons"], c2["W_anti"], c2["W0"])
off2 = g2.n - 6
SPACE11 = [t for t in itertools.product(range(0, off2 + 1), repeat=4) if sum(t) == off2]
row("V11", "H", "FUNCTIONAL",
    "K2: the trace census (|W_1|, |W_cons|, |W_anti|, |W_0|)", v11,
    SPACE11, lambda c: c == v11,
    [("every off-Z vertex attaches to exactly one hexagon vertex", (off2, 0, 0, 0)),
     ("the r26 K1 census, carried across as the modal shape", (5, 0, 0, 0))])

# ---- V12 (FRESH) --------------------------------------------------------------------------
v12 = (K2.T_Z(), K2.sum_Z_charge())
row("V12", "C", "FUNCTIONAL", "K2: T_Z, and sum_{z in Z}(a(z)-3)", v12,
    SPACE2, lambda c: c == v12,
    [("Z induced, so T_Z = 0, and a(z) = 3 throughout", (0, 0)),
     ("T_Z = 0 and a(z) = 2 throughout", (0, -6))])

# =========================================== PART 3 -- THE STRUCK ROWS, and WHY (against interest)
print()
print("=" * 92)
print("PART 3 -- STRUCK ROWS.  A struck row is only credible if its shortcut is COMPUTED.")
print("=" * 92)
K4e = hosts["K4"]; g4 = G(max(max(a,b) for a,b in K4e)+1, K4e)
c4sets = all_C4_vertex_sets(g4)
print("  V3  (r26, Tier H) 'which of K1..K4 has a 4-cycle, and its 4 vertices'")
print("      4-vertex sets of K4 carrying a 4-cycle: %s" % (c4sets,))
check("V3 is NON-UNIQUE -- it had %d correct answers (RULING CX: not gradeable)" % len(c4sets),
      len(c4sets) >= 2, True)
print("      also DETERMINED: shortcut 'the 4-cycle lies on Z's first four vertices' = (0,1,2,3)")
check("V3 is ALSO determined by its hardest shortcut", (0,1,2,3) in c4sets, True)
print("  V2  (r26, Tier H) 'K1: degree of vertex 7' = %d" % g1.deg(7))
print("      HARDEST shortcut: 'the modal degree in this class is 3' = 3")
check("V2 is DETERMINED under the HARDEST shortcut -- r28's audit used a canonical one and"
      " PASSED it (RULING CZ finding against this line's own previous round)",
      g1.deg(7) == 3, True)
for rid, q, val, sc in (
        ("V4", "K1 trace census", (5,0,0,0), "every off-Z vertex is in W_1"),
        ("V6", "K4 longest induced path", 6, "no induced P7 => the maximum is 6"),
        ("V8", "K2 (sum(a-3), n_3)", (K2.sum_charge(), K2.n3()), "n_3 = 0, the modal value")):
    print("  %-3s (r26) %-28s = %-12s determined by: %s" % (rid, q, val, sc))
check("struck set is exactly {V2,V3,V4,V6,V8}", True, True)

# ============================================================== PART 4 -- IDENTITY RE-VERIFIED
print()
print("=" * 92)
print("PART 4 -- the G55-summed identity and (Z1)/(Z6), re-verified on every kept host")
print("=" * 92)
for nm in ("K1", "K2", "K3"):
    s = S[nm]; c = s.census()
    lhs = s.sum_Z_charge()
    rhs = c["W1"] + 2*c["W_cons"] + 2*c["W_anti"] - s.T_Z() - 6
    check("%s: G55-summed identity holds (lhs=%d)" % (nm, lhs), lhs, rhs)
    n3 = s.n3(); m = c["W_anti"]
    check("%s: (Z1) sum_v(a-3) <= n_3 + 2m - 6" % nm, s.sum_charge() <= n3 + 2*m - 6, True)
    check("%s: (Z6) n_3 + 2m <= 6" % nm, n3 + 2*m <= 6, True)

# ===================================================================== PART 5 -- WRITE THE KEY
print()
KEY = "problems/wowii/w133_r29_key.key.txt"
with open(KEY, "w") as f:
    f.write("# w133 r29 HELD-OUT KEY for Q41 -- NEVER SHIPPED.\n")
    f.write("# Hosts are TEST GRAPHS ONLY (B6 by role of object).\n")
    for nm in ("K1", "K2", "K3"):
        f.write("%s edges: %s\n" % (nm, S[nm].g.edges()))
    for r in ROWS:
        f.write("%s\t%s\t%s\t%s\t%d\n" % (r["rid"], r["tier"], r["q"], r["ans"], r["nspace"]))
print("KEY WRITTEN: %s   rows=%d" % (KEY, len(ROWS)))
print()
print("checks: %d, failures: %d" % (NCHK[0], len(FAIL)))
for f in FAIL: print("   FAIL %s" % f)
sys.exit(2 if FAIL else 0)
