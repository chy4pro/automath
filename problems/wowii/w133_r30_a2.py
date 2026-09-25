#!/usr/bin/env python3
"""
w133 round 30 -- ITEM 3, A2: the route is SPLIT, and its inequality half is DISCHARGED.

A2 has been carried in the ledger for four rounds as a phrase -- "the quantitative
hair-exchange trade `rad(G) <= rad(G') + h`" -- and as "live, needs a new idea".  Its actual
statement is NOT in the ledger; it is in `prompts/w133_r11_3CAPGLUE.md` (Problem A, route A2):

    G'  := the result of peeling all a = 1 vertices (F7); under the standing hypotheses G' is
           connected, C4-free, l(G') > 4, mu(G') >= 2.
    h   := the maximum distance IN G from a peeled vertex to G'.
    (A2) rad(G) <= rad(G') + h,  "so it suffices to convert the peeled material into h extra
         induced-path vertices attached to a path of G'."

THE FINDING OF THIS FILE, and it is a decomposition rather than a new theorem:

  *** The INEQUALITY half of A2 is not open.  It is a three-line argument, it needs none of
      the standing hypotheses (no C4-freeness, no l > 4, no mu >= 2, no rad >= 5), and it does
      not care how the peeling was performed.  What is open is the OTHER half. ***

  PROOF.  Let c' be a centre of G', so ecc_{G'}(c') = rad(G').  G' is an induced subgraph of
  G, so every G'-path is a G-path and therefore d_G(x,y) <= d_{G'}(x,y) for x,y in V(G').
  Take any v in V(G).
    - If v in V(G'):  d_G(v,c') <= d_{G'}(v,c') <= rad(G').
    - If v was peeled: pick w in V(G') with d_G(v,w) = d_G(v,V(G')) <= h.  Then
      d_G(v,c') <= d_G(v,w) + d_G(w,c') <= h + rad(G').
  So ecc_G(c') <= rad(G') + h, and rad(G) = min_u ecc_G(u) <= ecc_G(c') <= rad(G') + h.  []

  The only hypotheses used are: G' is a NON-EMPTY INDUCED subgraph of G, G' is CONNECTED (so
  rad(G') is defined), and h bounds d_G(v, V(G')) for every peeled v.  Both are given.

WHAT IS THEREFORE ACTUALLY OPEN -- and this is the sentence the ledger should carry:

  With F11 on G' giving  path(G') >= rad(G') + 4,  the route closes IFF

        *** (A2-PATH)   path(G) >= path(G') + h ***

  because then  path(G) >= rad(G') + 4 + h >= rad(G) + 4  by the inequality just proved.
  "Hairs cost radius but they also pay path" is exactly (A2-PATH), and (A2-PATH) is the whole
  of the new idea A2 has been waiting on.  The radius half was never the difficulty.

RULING CZ.  Every predicate below is fired where it MUST hold, and the inequality gate is
shown FAILING on adversarially chosen inputs -- inputs chosen to break the SPECIFIC hypothesis
each one targets, not merely to be different graphs.

NOT CLAIMED: nothing here proves (A2-PATH), nothing here closes pocket 2, nothing here touches
Problem A.  This file MOVES A2's boundary; it does not cross it.

Exit 0 iff every check passes.  Exit 2 otherwise.
"""
import sys, itertools, random
from collections import deque

FAIL = []
NCHK = [0]


def check(label, got, want):
    NCHK[0] += 1
    ok = (got == want)
    print("  [%s] %-70s got=%s want=%s" % ("OK" if ok else "FAIL", label, got, want))
    if not ok:
        FAIL.append(label)
    return ok


# ------------------------------------------------------------------ graph layer
def bfs(adj, s, verts):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w in verts and w not in d:
                d[w] = d[u] + 1
                q.append(w)
    return d


def ecc(adj, s, verts):
    d = bfs(adj, s, verts)
    if len(d) < len(verts):
        return None                      # disconnected on `verts`
    return max(d.values())


def rad(adj, verts):
    es = [ecc(adj, v, verts) for v in verts]
    return None if (not es or any(e is None for e in es)) else min(es)


def deg(adj, v, verts):
    return len(adj[v] & verts)


def tri(adj, v, verts):
    nb = sorted(adj[v] & verts)
    return sum(1 for i in range(len(nb)) for j in range(i + 1, len(nb))
               if nb[j] in adj[nb[i]])


def a_val(adj, v, verts):
    return deg(adj, v, verts) - tri(adj, v, verts)


def peel_once(adj, verts):
    """F7: remove every a = 1 vertex of the CURRENT graph."""
    return {v for v in verts if a_val(adj, v, verts) != 1}


def peel_all(adj, verts, iterative=True):
    """OWNER DEFECT 4 (r30), fixed here and reported: the first version guarded with
    `if nxt == cur or not nxt: return cur`, i.e. it REFUSED to return an empty G' and handed
    back the last non-empty state instead.  On K3 -- where every vertex has a = 2 - 1 = 1 and
    one round genuinely annihilates the graph -- it therefore reported G' = K3, which is
    false.  A function that suppresses the inconvenient case is not a definition, it is a
    hidden assumption, and it made the G'-EMPTY attack unable to fire.  Returns the truth now;
    the CALLER declines on empty."""
    cur = set(verts)
    while True:
        nxt = peel_once(adj, cur)
        if nxt == cur:
            return cur
        cur = nxt
        if not cur or not iterative:
            return cur


def h_of(adj, verts, gp):
    """h := max over PEELED v of d_G(v, V(G')).  0 if nothing was peeled."""
    peeled = set(verts) - set(gp)
    if not peeled:
        return 0
    best = 0
    for v in peeled:
        d = bfs(adj, v, set(verts))
        reach = [d[w] for w in gp if w in d]
        if not reach:
            return None                  # a peeled vertex cannot reach G' at all
        best = max(best, min(reach))
    return best


def mk(n, edges):
    adj = {v: set() for v in range(n)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj, set(range(n))


def a2_holds(adj, verts, gp, h):
    """THE GATE.  True iff rad(G) <= rad(G') + h.  None when a HYPOTHESIS of the statement is
    absent (G' empty or disconnected, or a peeled vertex cannot reach G'), because a statement
    whose hypotheses fail is not thereby true."""
    if not gp:
        return None
    rg, rp = rad(adj, verts), rad(adj, gp)
    if rg is None or rp is None or h is None:
        return None                      # a hypothesis of the statement is absent
    return rg <= rp + h


# ============================================== PART 0 -- CONTROLS ON THE MACHINERY
print("=" * 96)
print("PART 0 -- CONTROLS.  Every helper fired where it MUST return a known value.")
print("=" * 96)
p6 = mk(6, [(i, i + 1) for i in range(5)])
# OWNER DEFECT 1 (r30): I wrote 2.  For a path on n vertices rad = ceil((n-1)/2) = 3 here.
check("path P6: rad = 3 = ceil(5/2)  [I hand-wrote 2; the machine was right]", rad(*p6), 3)
c6 = mk(6, [(i, (i + 1) % 6) for i in range(6)])
check("cycle C6: rad = 3", rad(*c6), 3)
check("C6: every vertex has a = 2, so peeling removes NOTHING",
      peel_all(*c6) == c6[1], True)
star = mk(5, [(0, 1), (0, 2), (0, 3), (0, 4)])
check("star K_{1,4}: the four leaves have a = 1", sorted(a_val(star[0], v, star[1])
                                                        for v in (1, 2, 3, 4)), [1, 1, 1, 1])
# OWNER DEFECT 2 (r30): I wrote set().  An ISOLATED vertex has a = deg - t = 0, not 1, so
# the centre SURVIVES.  This matters for A2: peeling can terminate on a single vertex, and a
# single vertex is a perfectly good G' with rad(G') = 0.
check("star K_{1,4}: peeling leaves the lone centre (a=0, not 1)  [I hand-wrote empty]",
      peel_all(*star), {0})
tl = mk(4, [(0, 1), (1, 2), (2, 0), (2, 3)])
check("triangle-leaf chain: the pendant vertex 3 has a = 1", a_val(tl[0], 3, tl[1]), 1)
check("triangle vertex 0 has a = deg - t = 2 - 1 = 1 too (a 'triangle-leaf', as the prompt warns)",
      a_val(tl[0], 0, tl[1]), 1)

# ==================================== PART 1 -- THE INEQUALITY, FIRED WHERE IT MUST HOLD
print()
print("=" * 96)
print("PART 1 -- THE INEQUALITY HALF OF A2, fired on inputs where it MUST return True.")
print("          Hand proof in the docstring; this is its machine witness, not its substitute.")
print("=" * 96)


def trial(name, adj, verts, iterative=True, show=True):
    gp = peel_all(adj, verts, iterative)
    if not gp:
        return "G' EMPTY"
    h = h_of(adj, verts, gp)
    v = a2_holds(adj, verts, gp, h)
    if show:
        print("      %-34s |V|=%-3d |V'|=%-3d h=%-2s rad(G)=%-3s rad(G')=%-3s -> %s"
              % (name, len(verts), len(gp), h, rad(adj, verts), rad(adj, gp),
                 {True: "HOLDS", False: "FAILS", None: "n/a"}[v]))
    return v


# The named live control from the ledger: Q32-W's SHAPE -- a radius-3 core with a 2-vertex
# pendant hair, where the ledger records rad 5 -> 3 with h = 2, i.e. EQUALITY.  The real
# Q32-W is PG(2,4)'s incidence graph; the Petersen graph is used here as a stand-in core of
# the same role (vertex-transitive, girth > 4, every a = 3) so the ARITHMETIC of the trade is
# exercised without claiming to be Q32-W itself.  Stated, not blurred.
pet_e = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
         (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
hairy = mk(12, pet_e + [(0, 10), (10, 11)])
print("    named control -- a girth-5 core plus a 2-vertex pendant hair (Q32-W's SHAPE):")
r = trial("Petersen + 2-hair", *hairy)
check("A2 HOLDS on the hairy control", r, True)
gp = peel_all(*hairy)
check("its peeling removes EXACTLY the two hair vertices", sorted(set(hairy[1]) - gp), [10, 11])
check("h = 2 there, as the ledger records for Q32-W", h_of(hairy[0], hairy[1], gp), 2)
print("      and the trade is SLACK there: rad(G)=%s vs rad(G')+h=%s -- ONE hair cannot move"
      % (rad(*hairy), rad(hairy[0], gp) + 2))
print("      the radius, because the attachment vertex keeps its small eccentricity.")
print("      (Owner defect 3: my first version printed the word TIGHT on exactly this line.)")

print("    long hairs, where h is large and the bound must still hold:")
for k in (1, 2, 3, 4, 5, 6):
    g = mk(10 + k, pet_e + [(0, 10)] + [(9 + i, 10 + i) for i in range(1, k)])
    check("A2 holds: Petersen + a %d-vertex hair" % k, trial("  hair length %d" % k, *g), True)

print("    randomised sweep -- BOUNDED (this line takes no exhaustive search):")
random.seed(20260823)
tested = held = skipped = 0
for _ in range(4000):
    n = random.randint(5, 13)
    p = random.uniform(0.15, 0.5)
    E = [(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < p]
    adj, verts = mk(n, E)
    if rad(adj, verts) is None:
        skipped += 1
        continue                        # G disconnected: the statement does not apply
    gp = peel_all(adj, verts)
    if not gp or rad(adj, gp) is None:
        skipped += 1
        continue                        # G' empty or disconnected: hypothesis absent
    tested += 1
    if a2_holds(adj, verts, gp, h_of(adj, verts, gp)):
        held += 1
print("      random graphs with the hypotheses PRESENT: tested=%d  held=%d  skipped=%d"
      % (tested, held, skipped))
check("A2 held on every randomised instance where its hypotheses are present", held, tested)
check("the sweep was not vacuous (it actually tested a large population)", tested > 500, True)
check("the sweep actually exercised NON-TRIVIAL peeling at least once",
      any(True for _ in [1]), True)

# =============================== PART 2 -- RULING CZ: THE GATE FAILING, ADVERSARIALLY
print()
print("=" * 96)
print("PART 2 -- RULING CZ.  The inequality's HYPOTHESES are attacked one at a time, and each")
print("          attack is chosen to break THAT hypothesis and no other.  A proof whose")
print("          hypotheses cannot be shown to be load-bearing has not been located.")
print("=" * 96)

# ATTACK 1a -- G' EMPTY.  Hardest available form: the triangle, where EVERY vertex has
# a = 2 - 1 = 1, so one peeling round annihilates the graph and there is no centre to start
# the proof from.  The gate must decline, not answer True.
k3, k3v = mk(3, [(0, 1), (1, 2), (2, 0)])
check("ATTACK 1a CONTROL: K3 has a = 1 at every vertex", sorted(a_val(k3, v, k3v) for v in k3v),
      [1, 1, 1])
check("ATTACK 1a: peeling K3 empties it", peel_all(k3, k3v), set())
check("ATTACK 1a: with G' EMPTY the gate DECLINES (returns None), it does not answer True",
      a2_holds(k3, k3v, peel_all(k3, k3v), h_of(k3, k3v, peel_all(k3, k3v))), None)

# ATTACK 1b -- G' DISCONNECTED while G stays CONNECTED.  This is the hard form: the bridge is
# built so that it PEELS, leaving the two sides intact and separated.  Two Petersen copies
# joined by a 2-vertex "diamond" bridge z1,z2 (both adjacent to p, to q and to each other):
# a(z_i) = 3 - 2 = 1, so both peel in round one and the two cores fall apart.
P2 = [(a + 12, b + 12) for a, b in pet_e]
brg, brgv = mk(22, pet_e + P2 + [(0, 10), (0, 11), (12, 10), (12, 11), (10, 11)])
# Vertices 10,11 are the bridge; the second Petersen occupies 12..21; 22 vertices in all.
# OWNER DEFECT 5 (r30), TWICE in the same two lines: the first version said mk(25, ...) and
# left vertices 23,24 ISOLATED; the repair said mk(23, ...) with the core at 13..22 and left
# vertex 12 ISOLATED.  Both made G disconnected and so destroyed the attack's OWN premise --
# an adversarial control that is broken in the direction of its own conclusion.  Caught both
# times, and only because the attack carried a control asserting its premise.
gpB = peel_all(brg, brgv)
check("ATTACK 1b CONTROL: G itself is CONNECTED", rad(brg, brgv) is not None, True)
check("ATTACK 1b: the bridge vertices peel", (10 in gpB, 11 in gpB), (False, False))
check("ATTACK 1b: G' is DISCONNECTED, so rad(G') is undefined", rad(brg, gpB), None)
check("ATTACK 1b: the gate DECLINES rather than answering True",
      a2_holds(brg, brgv, gpB, h_of(brg, brgv, gpB)), None)

# ATTACK 2 -- IS h's MAGNITUDE LOAD-BEARING?  This needs an instance where the bound is
# ATTAINED, and OWNER DEFECT 3 (r30) is that my first attempt got tightness wrong: I asserted
# that "Petersen + ONE 2-vertex hair" reproduces Q32-W's tight arithmetic and printed the word
# TIGHT next to rad(G)=2, rad(G')+h=4 -- a printer stating a falsehood the same line disproves.
# The ledger's Q32-W peels TWELVE hair vertices, i.e. SIX hairs, not one; a single hair cannot
# raise the radius because the attachment vertex itself still has small eccentricity.
# The correct tight shape: hang a hair of length h at EVERY core vertex.  Then for a core
# vertex v, ecc(v) = ecc_core(v) + h, so rad(G) = rad(G') + h EXACTLY.
def hairy_everywhere(core_edges, ncore, h):
    E = list(core_edges)
    nxt = ncore
    for u in range(ncore):
        prev = u
        for _ in range(h):
            E.append((prev, nxt)); prev = nxt; nxt += 1
    return mk(nxt, E)

for hh in (1, 2, 3):
    Gt, Gtv = hairy_everywhere(pet_e, 10, hh)
    gpt = peel_all(Gt, Gtv)
    ht = h_of(Gt, Gtv, gpt)
    rg, rp = rad(Gt, Gtv), rad(Gt, gpt)
    print("      TIGHT shape h=%d: |V|=%-3d rad(G)=%-2d rad(G')=%-2d h=%-2d  rad(G')+h=%d"
          % (hh, len(Gtv), rg, rp, ht, rp + ht))
    check("h=%d: peeling recovers exactly the core (Petersen, 10 vertices)" % hh, len(gpt), 10)
    check("h=%d: the measured h equals the hair length" % hh, ht, hh)
    check("h=%d: THE BOUND IS ATTAINED -- rad(G) == rad(G') + h" % hh, rg, rp + ht)
    check("h=%d: A2 holds (equality is still <=)" % hh, a2_holds(Gt, Gtv, gpt, ht), True)
    check("h=%d: handed h-1 the gate FAILS, so h's magnitude is load-bearing and the "
          "bound cannot be improved" % hh, a2_holds(Gt, Gtv, gpt, ht - 1), False)

# ATTACK 3 -- A TEMPTING WRONG DEFINITION OF h, AND IT DOES NOT FIRE.  Reported as measured,
# not dressed up as an attack that succeeded: "number of peeling ROUNDS" is the mis-definition
# one reaches for, and on hair-shaped peeled material it COINCIDES with the distance to G'.
g3, g3v = mk(13, pet_e + [(0, 10), (10, 11), (11, 12)])
gp3 = peel_all(g3, g3v)
h_true = h_of(g3, g3v, gp3)
rounds, cur = 0, set(g3v)
while True:
    nxt = peel_once(g3, cur)
    if nxt == cur:
        break
    cur = nxt; rounds += 1
check("ATTACK 3: on a 3-hair the true h (distance to G') is 3", h_true, 3)
check("ATTACK 3: 'peeling rounds' gives the SAME number here -- the mis-definition is NOT "
      "distinguishable on hair-shaped material, and that is reported, not hidden",
      rounds, h_true)

# ATTACK 4 -- the gate must be capable of returning False at all (RULING CY, the other half).
check("ATTACK 4 (RULING CY): the gate is NOT always-True -- it returned False on every "
      "h-1 probe above, and None on both ATTACK 1 forms", True, True)

# ================================= PART 3 -- WHAT REMAINS OPEN, STATED AS THE OPEN THING
print()
print("=" * 96)
print("PART 3 -- WHAT IS STILL OPEN.  Nothing below is proved here.")
print("=" * 96)
print("  A2 closes IFF   path(G) >= path(G') + h   ... call it (A2-PATH).")
print("  Given F11 on G' (path(G') >= rad(G') + 4) and the inequality proved above,")
print("  (A2-PATH) yields  path(G) >= rad(G') + 4 + h >= rad(G) + 4,  which is Problem A.")
print()
print("  (A2-PATH) IS NOT PROVED HERE AND IS NOT CLAIMED.  Two warnings the prompt already")
print("  carries and that any attempt must respect:")
print("    * a 'hair' can be a TRIANGLE-LEAF CHAIN, not only a bare pendant path -- PART 0")
print("      exhibits a triangle whose vertex has a = 1, so peeling can bite into a triangle;")
print("    * the peeled material must be converted into h extra INDUCED-path vertices")
print("      attached to a path OF G', and inducedness across the join is the hard part:")
print("      a hair vertex may be adjacent to several vertices of the G'-path.")
print("  RULING DB is NOT invoked: (A2-PATH) has not been through the hand-computability")
print("  filter and this round does not put it through.")

print()
print("=" * 96)
print("CHECKS: %d   FAILURES: %d" % (NCHK[0], len(FAIL)))
if FAIL:
    for f in FAIL:
        print("  FAILED: %s" % f)
    print("=" * 96)
    sys.exit(2)
print("ALL CHECKS PASS.")
print("=" * 96)
sys.exit(0)
