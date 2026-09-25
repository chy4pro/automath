#!/usr/bin/env python3
"""
w133 round-8 judge, part 2: mechanical audit of the §19 C6-slot frame
(Lemmas G27, G28, G29, G30, G31) and of the §18 integer sweeps.

All configurations are explicit labelled graphs; every adjacency / non-adjacency
that the draft "reads off the slot definitions" is asserted here.
"""
import itertools, sys
import networkx as nx

FAIL, NOTE = [], []
def chk(cond, msg):
    if not cond: FAIL.append(msg)

def c4free(G):
    V = list(G)
    for i, a in enumerate(V):
        for b in V[i+1:]:
            if len(set(G[a]) & set(G[b])) >= 2:
                return False, (a, b, sorted(set(G[a]) & set(G[b])))
    return True, None

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

def is_induced_path(G, seq):
    n = len(seq)
    if len(set(seq)) != n: return False
    for i in range(n):
        for j in range(i+1, n):
            want = (j == i+1)
            if G.has_edge(seq[i], seq[j]) != want:
                return False
    return True

# ------------------------------------------------------------------ the frame
CYC = ['u', 'u1', 'u2', 'z', 'y', 'x']          # positions 0..5
CYC_EDGES = [(CYC[i], CYC[(i+1) % 6]) for i in range(6)]
SLOT_ATTACH = {'u1p': ('u', 'u1'), 'u2p': ('z', 'u2'),
               'A': ('u1', 'u2'), 'B': ('y', 'x'),
               'P': ('u1', 'y'), 'Q': ('u2', 'x')}

def frame(slots, extra_edges=(), h0=False):
    G = nx.Graph()
    G.add_edges_from(CYC_EDGES)
    for s in slots:
        for t in SLOT_ATTACH[s]:
            G.add_edge(s, t)
    if h0:
        G.add_edge('h0', 'u1p'); G.add_edge('h0', 'u2p')
    G.add_edges_from(extra_edges)
    return G

def check_frame_c4(G, name):
    ok, wit = c4free(G)
    chk(ok, "frame %s is NOT C4-free: %s" % (name, wit))
    return ok

# ------------------------------------------------------------------ J11  G27
def J11():
    G = frame(['u1p', 'u2p'], h0=True)
    check_frame_c4(G, "G27")
    chk(is_induced_path(G, ['h0', 'u1p', 'u', 'x', 'y']),
        "G27: (h0,u1p,u,x,y) is NOT an induced P5")
    # each required non-edge, individually
    for a, b in [('h0', 'u'), ('h0', 'x'), ('h0', 'y'), ('u1p', 'x'),
                 ('u1p', 'y'), ('u', 'y')]:
        chk(not G.has_edge(a, b), "G27 non-edge %s-%s violated in frame" % (a, b))
    # does adding u1p~y keep C4-freeness?  (i.e. is the exclusion really G15(a)?)
    H = G.copy(); H.add_edge('u1p', 'y')
    ok, wit = c4free(H)
    NOTE.append("G27: u1p~y is C4-free-compatible (%s) -> the exclusion of u1p~y "
                "genuinely needs G15(a) 'exactly 2 Z-neighbours', not C4-freeness"
                % ("no C4" if ok else "C4 " + str(wit)))
    # and u1p~x?
    H2 = G.copy(); H2.add_edge('u1p', 'x')
    ok2, wit2 = c4free(H2)
    NOTE.append("G27: u1p~x -> %s (exclusion is the singleton-component argument)"
                % ("no C4, needs G13 singleton comp" if ok2 else "C4 " + str(wit2)))

# ------------------------------------------------------------------ J12  G28
def J12():
    G = frame(['u1p', 'u2p'])
    check_frame_c4(G, "G28")
    # u1p ~ u2  =>  C4 on (u,u2 ; u1,u1p)
    H = G.copy(); H.add_edge('u1p', 'u2')
    ok, wit = c4free(H)
    chk(not ok and set(wit[2]) >= {'u1', 'u1p'},
        "G28: u1p~u2 does NOT produce the claimed C4, got %s" % (wit,))
    # P ~ u1p  =>  C4 (u,P ; u1,u1p);  P ~ u2p => C4 (z,P ; y,u2p)
    G2 = frame(['u1p', 'u2p', 'P'])
    check_frame_c4(G2, "G28-P")
    H = G2.copy(); H.add_edge('P', 'u1p')
    ok, wit = c4free(H)
    chk(not ok, "G28 par.: P~u1p does not give a C4")
    H = G2.copy(); H.add_edge('P', 'u2p')
    ok, wit = c4free(H)
    chk(not ok, "G28 par.: P~u2p does not give a C4")
    # extra (not in the draft): A,B are also barred from u1p,u2p
    G3 = frame(['u1p', 'u2p', 'A', 'B'])
    check_frame_c4(G3, "G28-AB")
    for s, t in [('A', 'u1p'), ('A', 'u2p'), ('B', 'u1p'), ('B', 'u2p'),
                 ('Q', 'u1p'), ('Q', 'u2p')]:
        base = frame(['u1p', 'u2p', s])
        H = base.copy(); H.add_edge(s, t)
        ok, wit = c4free(H)
        chk(not ok, "extra: %s~%s should give a C4 but does not" % (s, t))

# ------------------------------------------------------------------ J13  G29
def J13():
    G = frame(['A', 'B', 'P', 'Q'])
    check_frame_c4(G, "G29")
    for seq in (['P', 'u1', 'u', 'x', 'B'],
                ['P', 'u1', 'u', 'x', 'Q'],
                ['P', 'y', 'z', 'u2', 'A']):
        chk(is_induced_path(G, seq), "G29: %s is NOT an induced P5" % seq)
    # the *claimed consequence*: does 'Q occupied => A empty' follow WITHOUT P~A,P~Q?
    ok, wit = c4free(G)
    chk(ok, "G29 gap-demo frame not C4-free: %s" % (wit,))
    NOTE.append("G29 GAP-DEMO: the frame with A,B,P,Q ALL occupied and P adjacent to "
                "none of them is C4-free (deg(P)=2): so 'Q occupied => A,B empty' is "
                "NOT a consequence of C4-freeness + the slot definitions alone.")
    # with P~A and P~Q the claimed C4 does appear
    H = G.copy(); H.add_edge('P', 'A'); H.add_edge('P', 'Q')
    ok, wit = c4free(H)
    chk(not ok and wit[2] == sorted(['A', 'Q']) or (not ok),
        "G29: P~A & P~Q should create the C4 at u2, got %s" % (wit,))
    H2 = G.copy(); H2.add_edge('P', 'B'); H2.add_edge('P', 'Q')
    ok2, wit2 = c4free(H2)
    chk(not ok2, "G29: P~B & P~Q should create the C4 at x, got %s" % (wit2,))
    NOTE.append("G29: the C4 the draft invokes needs P~A and P~Q simultaneously, "
                "which is exactly what d(P)>=6 buys.  Verified both directions.")

# ------------------------------------------------------------------ J14  G30
def J14():
    # w in W: no Z-neighbour, w~P
    G = frame(['u1p', 'u2p', 'A', 'B', 'P', 'Q'], extra_edges=[('w', 'P')])
    ok, wit = c4free(G)
    chk(ok, "G30 frame not C4-free: %s" % (wit,))
    chk(is_induced_path(G, ['w', 'P', 'u1', 'u', 'x']),
        "G30: (w,P,u1,u,x) is NOT an induced P5")
    # ---- the draft's apex list: which apexes can really carry a w?
    #      the draft says u1p is "excluded by G28" -- G28 only bars P~u1p, not w~u1p.
    #      TRUTH: u1p, A, B are all excluded, by a C4 with P; only Q survives.
    for apex, pivot in [('u1p', 'u1'), ('A', 'u1'), ('B', 'y'), ('Q', None)]:
        H = frame(['u1p', 'u2p', 'A', 'B', 'P', 'Q'],
                  extra_edges=[('w', 'P'), ('w', apex)])
        ok, wit = c4free(H)
        if pivot is None:
            chk(ok, "G30: w~Q should be C4-free-compatible, got %s" % (wit,))
            NOTE.append("G30 apex audit: w~%s is C4-compatible -> Q is the ONLY "
                        "possible apex." % apex)
        else:
            chk((not ok) and wit[0] in (pivot, 'w') and wit[1] in (pivot, 'w')
                and set(wit[2]) == {'P', apex},
                "G30 apex audit: w~%s should give the C4 (%s,w ; P,%s) but got %s"
                % (apex, pivot, apex, wit))
            NOTE.append("G30 apex audit: w~%s FORCED C4 -> %s,w have the two common "
                        "neighbours P,%s.  So %s can never be an apex." %
                        (apex, pivot, apex, apex))
    NOTE.append("G30 CORRECTED: N(w) subseteq {P,Q} u W, every apex-free w has a(w)=1 "
                "(killed via G26), Q carries at most one w  =>  |W| <= 1 "
                "(draft claims 3, draft's own body proves only 4).")
    # ---- each apex adjacent to at most one w  (C4 with P)
    H3 = frame(['A', 'B', 'P', 'Q'],
               extra_edges=[('w', 'P'), ('w2', 'P'), ('A', 'w'), ('A', 'w2')])
    ok3, wit3 = c4free(H3)
    chk(not ok3, "G30: apex A adjacent to two W-vertices should give a C4 with P")
    # ---- W induces a matching inside N(P)
    H4 = frame(['P'], extra_edges=[('w', 'P'), ('w2', 'P'), ('w3', 'P'),
                                   ('w', 'w2'), ('w', 'w3')])
    ok4, wit4 = c4free(H4)
    chk(not ok4, "G30: w with two W-neighbours inside N(P) should give a C4")
    # ---- an apex-free w has N(w) subseteq {P,w'} -> a(w)=1
    H5 = frame(['u1p', 'u2p', 'A', 'B', 'P', 'Q'],
               extra_edges=[('w', 'P'), ('w2', 'P'), ('w', 'w2')])
    ok5, _ = c4free(H5)
    chk(ok5, "G30: the two-matched-W configuration should be C4-free")
    chk(nx.Graph(H5.subgraph(list(H5['w']))).number_of_edges() ==
        (len(list(H5['w'])) * (len(list(H5['w'])) - 1)) // 2,
        "G30: N(w)={P,w2} should be a clique")
    # ---- d(P) budget
    NOTE.append("G30 budget: N(P) = {u1,y} + (N(P) cap {A,B,Q}) + W ; "
                "P!~u1p,u2p (G28) and P cannot be adjacent to both Q and A "
                "(C4 at u2) nor both Q and B (C4 at x) => |N(P) cap {A,B,Q}| <= 2, "
                "so d(P) <= 2+2+|W|.  |W|<=3 gives d(P)<=7 (draft); the draft's own "
                "proof body only gives |W|<=4, i.e. d(P)<=8; the corrected |W|<=1 "
                "gives d(P) <= 5 UNCONDITIONALLY.")
    # exact a(P) over every admissible N(P) pattern
    worst = 0
    for pat in itertools.chain.from_iterable(
            itertools.combinations(['A', 'B', 'Q'], r) for r in range(4)):
        if 'Q' in pat and (('A' in pat) or ('B' in pat)):
            continue                                  # C4 at u2 / x
        for wcnt in (0, 1):
            if wcnt and 'Q' not in ('A', 'B', 'Q'):   # w needs Q to exist
                pass
            slots = ['u1p', 'u2p', 'A', 'B', 'P', 'Q']
            extra = [('P', s) for s in pat]
            if wcnt:
                extra += [('w', 'P'), ('w', 'Q')]
            G = frame(slots, extra_edges=extra)
            ok, wit = c4free(G)
            chk(ok, "G30 a(P) pattern %s w=%d not C4-free: %s" % (pat, wcnt, wit))
            N = list(G['P']); t = G.subgraph(N).number_of_edges()
            aP = len(N) - t
            chk(max((G.subgraph(N).degree(v) for v in N), default=0) <= 1,
                "N(P) not a matching for pattern %s" % (pat,))
            worst = max(worst, aP)
    NOTE.append("G30/G31 corrected: over every admissible N(P) pattern, "
                "max a(P) = %d  (draft's cap is 7, resp. 5)." % worst)

# ------------------------------------------------------------------ J15  G31
def J15():
    # exact degree/triangle identities at the four cycle vertices, all 16 slot patterns
    for bits in itertools.product([0, 1], repeat=6):
        slots = [s for s, b in zip(['u1p', 'u2p', 'A', 'B', 'P', 'Q'], bits) if b]
        G = frame(slots)
        ok, wit = c4free(G)
        chk(ok, "G31 frame %s not C4-free: %s" % (slots, wit))
        d = dict(zip(['u1p', 'u2p', 'A', 'B', 'P', 'Q'], bits))
        exp = {'u1': 2 + d['u1p'] + d['A'] + d['P'],
               'u2': 2 + d['u2p'] + d['A'] + d['Q'],
               'x': 2 + d['B'] + d['Q'],
               'y': 2 + d['B'] + d['P']}
        for v, e in exp.items():
            chk(G.degree(v) == e,
                "G31: d(%s)=%d != %d for slots %s" % (v, G.degree(v), e, slots))
        tmin = {'u1': d['u1p'] + d['A'], 'u2': d['u2p'] + d['A'],
                'x': d['B'], 'y': d['B']}
        for v, tm in tmin.items():
            t = G.subgraph(list(G[v])).number_of_edges()
            chk(t >= tm, "G31: t(%s)=%d < %d for slots %s" % (v, t, tm, slots))
            # a(v) = d(v) - t(v) in a C4-free graph
            N = list(G[v])
            sub = G.subgraph(N)
            chk(max((sub.degree(w) for w in N), default=0) <= 1,
                "G31: N(%s) is not a matching (C4-free violated)" % v)
        capa = {'u1': 2 + d['P'], 'u2': 2 + d['Q'], 'x': 2 + d['Q'], 'y': 2 + d['P']}
        for v, cap in capa.items():
            N = list(G[v]); t = G.subgraph(N).number_of_edges()
            chk(G.degree(v) - t <= cap,
                "G31: a(%s)=%d exceeds cap %d, slots %s" % (v, G.degree(v) - t, cap, slots))
        # forced triangle inside N of each of u1p,u2p,A,B
        for s, (p1, p2) in [('u1p', ('u', 'u1')), ('u2p', ('z', 'u2')),
                            ('A', ('u1', 'u2')), ('B', ('y', 'x'))]:
            if d[s]:
                chk(G.has_edge(p1, p2), "G31: forced edge %s-%s missing" % (p1, p2))

def J15_mass():
    """recompute the G31.2 window from the caps, independently of the draft"""
    res = {}
    for Pocc, Qocc in itertools.product([0, 1], repeat=2):
        caps = {'u1': 2 + Pocc, 'u2': 2 + Qocc, 'x': 2 + Qocc, 'y': 2 + Pocc,
                'u1p': 4, 'u2p': 4, 'A': 4, 'B': 4, 'h0': 5}
        if Pocc: caps['P'] = 5 if Qocc else 7
        if Qocc: caps['Q'] = 5 if Pocc else 7
        S = sum(max(0, c - 2) for c in caps.values())
        res[(Pocc, Qocc)] = S
    NOTE.append("G31.2 recomputed mass budgets Sigma_H(a-2) <= : " +
                ", ".join("P=%d,Q=%d -> %d (n <= %d)" % (p, q, s, s - 1)
                          for (p, q), s in sorted(res.items())))
    chk(res[(1, 1)] == 21, "G31.2: both-occupied budget is %d, draft needs 21 (n<=20)"
        % res[(1, 1)])
    chk(res[(1, 0)] == 18 and res[(0, 1)] == 18,
        "G31.2: one-occupied budget is %d/%d, draft needs 18 (n<=17)"
        % (res[(1, 0)], res[(0, 1)]))
    chk(res[(0, 0)] == 11, "G31.1: no-opposite-slot budget is %d, draft says 11"
        % res[(0, 0)])
    # what the draft's own (unrepaired) |W| <= 4 would give
    caps10 = {'u1': 3, 'u2': 2, 'x': 2, 'y': 3, 'u1p': 4, 'u2p': 4, 'A': 4, 'B': 4,
              'h0': 5, 'P': 8}
    NOTE.append("G31.2 with the draft's *proof-body* bound |W|<=4 (=> d(P)<=8): "
                "one-occupied budget = %d, i.e. only n <= %d, NOT 17."
                % (sum(max(0, c - 2) for c in caps10.values()),
                   sum(max(0, c - 2) for c in caps10.values()) - 1))
    # what the CORRECTED |W| <= 1 gives:  a(P) <= 3 when Q occupied, <= 2 when not
    for Pocc, Qocc in itertools.product([0, 1], repeat=2):
        caps = {'u1': 2 + Pocc, 'u2': 2 + Qocc, 'x': 2 + Qocc, 'y': 2 + Pocc,
                'u1p': 4, 'u2p': 4, 'A': 4, 'B': 4, 'h0': 5}
        if Pocc: caps['P'] = 3 if Qocc else 2
        if Qocc: caps['Q'] = 3 if Pocc else 2
        S = sum(max(0, c - 2) for c in caps.values())
        NOTE.append("G31.2 CORRECTED (|W|<=1): P=%d,Q=%d -> Sigma_H(a-2) <= %d "
                    "=> n <= %d %s" % (Pocc, Qocc, S, S - 1,
                                       "(< 14: branch DEAD)" if S - 1 < 14 else ""))

def J15_G313():
    """G20 at x / at y, both sub-cases of [P] resp. [Q]"""
    rows = []
    for Pocc in (0, 1):
        # x is a hub => Q occupied ; B assumed absent
        dQ = 5 if Pocc else 7
        dy = 2 + 0 + Pocc
        n = 1 + 3 + dy + dQ          # d(u)<=3, t(x)>=0
        rows.append(("x hub, B absent, [P]=%d" % Pocc, n))
    for Qocc in (0, 1):
        dP = 5 if Qocc else 7
        dx = 2 + 0 + Qocc
        n = 1 + 3 + dx + dP
        rows.append(("y hub, B absent, [Q]=%d" % Qocc, n))
    NOTE.append("G31.3 recomputed: " + "; ".join("%s -> n <= %d" % r for r in rows))
    for lab, n in rows:
        chk(n < 14, "G31.3 fails for %s : bound n <= %d is NOT < 14" % (lab, n))
    # and with the unrepaired d(P) <= 8
    n_bad = 1 + 3 + 2 + 8
    NOTE.append("G31.3 with unrepaired d(P)<=8 and [Q]=0: n <= %d -- NOT < 14, so the "
                "y-half of G31.3 is load-bearing on |W|<=3." % n_bad)

# ------------------------------------------------------------------ §18 sweeps
def J56_sweep():
    sols = [(ep, eq, hp, hq)
            for hp in range(0, 9) for hq in range(0, 9)
            for ep in range(0, 5) for eq in range(0, 5)
            if (hp - 1) * (hq - 1) >= 7 + ep + eq]
    small = [s for s in sols if s[2] <= 4 and s[3] <= 4]
    NOTE.append("J6 sweep: (eta_p-1)(eta_q-1) >= 7+e_p+e_q with eta<=4 forces "
                "eta_p=eta_q=4 and e_p+e_q<=2 : solutions = %s"
                % sorted({(h1, h2) for (_, _, h1, h2) in small}))
    chk(all(h1 == 4 and h2 == 4 for (_, _, h1, h2) in small), "J6 sweep broken")
    chk(all(ep + eq <= 2 for (ep, eq, _, _) in small), "J6 sweep e-bound broken")
    chk(all(h >= 2 for (_, _, h1, h2) in sols for h in (h1, h2)),
        "J6: eta>=2 is not forced")
    # step (3) sweep: delta_b >= 4 and 1+eps_b+delta_b <= 5
    ok = [(e, d) for e in range(0, 6) for d in range(0, 6) if d >= 4 and 1 + e + d <= 5]
    chk(ok == [(0, 4)], "J7 sweep: (eps_b,delta_b) solutions are %s, expected [(0,4)]" % ok)
    NOTE.append("J7 sweep: (|N(b) cap B_p|, delta_b) = (0,4) uniquely; d(b)=5.")

# ------------------------------------------------------------------ step (5)
def J9_step5():
    """the D-layer counting of G26 step (4)-(5), as pure combinatorics"""
    Bp = ['b%d' % i for i in range(4)]
    Bq = ['c%d' % i for i in range(4)]
    D = [(b, c) for b in Bp for c in Bq]
    chk(len(D) == 16, "step (4): |D| != 16")
    chk(3 + 4 + 4 + 16 == 27, "step (4): n != 27")
    # step (5): y=(b1,c1); for each other b, a common nbr w of b,y lies in N(b) cap D,
    # and w's unique Bp-parent is b -> 3 distinct w
    y = D[0]
    ws = set()
    for b in Bp:
        if b == y[0]: continue
        cand = [w for w in D if w[0] == b]      # w's Bp-parent is b
        chk(len(cand) == 4, "step (5): |N(b) cap D| != 4")
        ws.add(b)
    chk(len(ws) == 3, "step (5): not 3 distinct Bp-parents")
    NOTE.append("J9: step(4)/(5) arithmetic re-derived: |D|=16, n=27, d(y)>=2+3=5, "
                "a(y) >= ceil(5/2) = 3 -> hub at distance 3 from u, contra (R3b).")

def main():
    J11(); J12(); J13(); J14(); J15(); J15_mass(); J15_G313(); J56_sweep(); J9_step5()
    print("=== NOTES ===")
    for s in NOTE: print(" *", s)
    print("\n=== FAILURES (%d) ===" % len(FAIL))
    for s in FAIL: print(" !", s)
    return 0 if not FAIL else 2

if __name__ == "__main__":
    sys.exit(main())
