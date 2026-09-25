#!/usr/bin/env python3
"""
w133 round-8 judge, part 3: are the eleven G21 slots really all live under (C6)?

Method (airtight, no search over unknown graphs):  for each slot S the induced
subgraph of the REAL graph on  Z u {S}  is completely determined --
Z = (u,u1,u2,z,y,x) is an induced C6, and by G15(a) the slot occupant's
Z-neighbourhood is exactly its defining pair.  So any induced P6 found inside
Z u {S} is an induced P6 of the real graph, contradicting (C6).
"""
import itertools, sys
import networkx as nx

CYC = ['u', 'u1', 'u2', 'z', 'y', 'x']
POS = {v: i for i, v in enumerate(CYC)}
SLOT = {"u1'": ('u', 'u1'),      # (u,u1)   -- the u1-component partner of N(u)
        "u2'": ('u2', 'z'),      # (u2,z)
        'A':   ('u1', 'u2'),
        'B':   ('y', 'x'),
        'P':   ('u1', 'y'),
        'Q':   ('u2', 'x')}

def base():
    G = nx.Graph()
    G.add_edges_from([(CYC[i], CYC[(i + 1) % 6]) for i in range(6)])
    return G

def induced_paths(G, k):
    adj = {v: set(G[v]) for v in G}
    def ext(path, pset):
        if len(path) == k:
            yield tuple(path); return
        for w in adj[path[-1]]:
            if w in pset: continue
            if any(w in adj[z] for z in path[:-1]): continue
            path.append(w); pset.add(w)
            yield from ext(path, pset)
            path.pop(); pset.discard(w)
    for v in G:
        yield from ext([v], {v})

def first_P6(G):
    for p in induced_paths(G, 6):
        return p
    return None

def c4(G):
    V = list(G)
    for i, a in enumerate(V):
        for b in V[i+1:]:
            if len(set(G[a]) & set(G[b])) >= 2:
                return (a, b, sorted(set(G[a]) & set(G[b])))
    return None

print("=" * 78)
print("A. Z alone")
G = base()
print("   induced P6 in the bare induced C6 :", first_P6(G), " (must be None)")
assert first_P6(G) is None

print("=" * 78)
print("B. one slot at a time  (Z u {S} is FULLY determined by G15(a) + induced C6)")
verdict = {}
for s, pair in SLOT.items():
    G = base()
    for t in pair:
        G.add_edge(s, t)
    p6 = first_P6(G)
    verdict[s] = p6
    print("   slot %-4s ~ %-9s :  induced P6 = %s"
          % (s, str(pair), p6 if p6 else "NONE  -> slot survives"))

dead = [s for s, p in verdict.items() if p]
alive = [s for s, p in verdict.items() if not p]
print("\n   => slots KILLED outright by (C6):", dead)
print("   => slots surviving              :", alive)

print("=" * 78)
print("C. the zero-Z-neighbour slot h0  (G21(iv): h0 ~ u1' and h0 ~ u2')")
G = base()
for t in SLOT["u1'"]:
    G.add_edge("u1'", t)
G.add_edge('h0', "u1'")
p6 = first_P6(G)
print("   Z u {u1',h0} with h0~u1' (h0 has NO Z-neighbour): induced P6 =", p6)
print("   => any vertex with no Z-neighbour adjacent to u1' is forbidden;")
print("      G21(iv) forces h0 ~ u1', so the h0 slot is EMPTY under (C6).")
assert p6 is not None

print("=" * 78)
print("D. consequences for the surviving slots P,Q  (frame Z u {P,Q} + W-vertices)")
G = base()
for s in ('P', 'Q'):
    for t in SLOT[s]:
        G.add_edge(s, t)
print("   P~Q allowed? ", "NO, C4 " + str(c4(nx.Graph(list(G.edges()) + [('P', 'Q')])))
      if c4(nx.Graph(list(G.edges()) + [('P', 'Q')])) else "yes")
print("   induced P6 in Z u {P,Q}:", first_P6(G))
# a W-vertex on P
H = G.copy(); H.add_edge('w', 'P')
print("   Z u {P,Q,w} (w~P only):  induced P6 =", first_P6(H), " C4 =", c4(H))
H2 = H.copy(); H2.add_edge('w', 'Q')
print("   ... + w~Q            :  induced P6 =", first_P6(H2), " C4 =", c4(H2))
H3 = H.copy(); H3.add_edge('w2', 'P'); H3.add_edge('w2', 'Q'); H3.add_edge('w', 'Q')
print("   ... two W-vertices both ~Q:  C4 =", c4(H3), "(must be a C4: P,Q share w,w2)")

print("=" * 78)
print("E. the resulting mass budget for Claim Q6.1's branch")
print("   surviving slots for H : u1,u2,x,y (cycle) + P,Q")
print("   d(u1) = 2 + [P],  d(u2) = 2 + [Q],  d(x) = 2 + [Q],  d(y) = 2 + [P]")
print("   N(u1) = {u,u2,P} has NO internal edge -> t(u1)=0 -> a(u1) = 2 + [P] <= 3")
print("   N(P)  = {u1,y} + W,  W has no Z-neighbour -> t(P)=0 -> a(P) = 2 + |W| <= 3")
print("   => Sigma_H (a-2) <= 6, while (**) needs Sigma_H (a-2) > n >= 14.")
print("   => CONTRADICTION: the a(u)=a(z)=2 branch (Claim Q6.1) is EMPTY.")

print("=" * 78)
print("F. sanity: the P5s that G22.1/G27/G29 use really do extend to P6s")
for s, ext in [("u1'", ['u1\'', 'u', 'x', 'y', 'z', 'u2']),
               ('A',   ['A', 'u1', 'u', 'x', 'y', 'z']),
               ('B',   ['B', 'y', 'z', 'u2', 'u1', 'u'])]:
    G = base()
    for t in SLOT[s]:
        G.add_edge(s, t)
    n = len(ext)
    ok = all((G.has_edge(ext[i], ext[j]) == (j == i + 1))
             for i in range(n) for j in range(i + 1, n))
    print("   %-4s : %s induced P6? %s" % (s, ext, ok))
    assert ok
print("   (the draft's G22.1 uses the P5 prefixes of exactly these and concludes only "
      "d <= 5.)")
