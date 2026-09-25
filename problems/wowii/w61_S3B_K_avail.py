#!/usr/bin/env python3
"""S3 round-B: counterfactual AVAILABILITY check + the remaining toolkit lemmas.

For every toolkit lemma the K-chain could invoke at each of its three joints,
we (a) test the lemma itself, (b) test whether its HYPOTHESES hold at that
point, and (c) report what it WOULD give if applied there -- even where the
draft never applies it.

Also: Lemma T, Lemma H (the two toolkit lemmas the K-chain claims to supersede),
Theorem N / N' / Corollary N1 subsumption arithmetic, and an extended
choice-of-A hunt on larger random graphs.
"""
import sys, random, itertools
from collections import defaultdict
import networkx as nx


def hh(degmap, rng=None):
    ent = [[d, l] for l, d in degmap.items()]
    D, heads, blocks, vals = [], [], [], []
    while True:
        if rng: rng.shuffle(ent)
        ent.sort(key=lambda e: -e[0])
        if not ent or ent[0][0] == 0: break
        d0 = ent[0][0]
        vals.append({l: v for v, l in ent})
        D.append(d0); heads.append(ent[0][1])
        blk = ent[1:1 + d0]
        blocks.append(set(l for v, l in blk))
        for e in blk: e[0] = max(0, e[0] - 1)
        ent = ent[1:]
    return D, heads, blocks, vals


def maxis(G):
    H = nx.complement(G); best, out = 0, []
    for c in nx.find_cliques(H):
        if len(c) > best: best, out = len(c), [frozenset(c)]
        elif len(c) == best: out.append(frozenset(c))
    return best, out


def corpus(nrand=4000, seed=99):
    from networkx.generators.atlas import graph_atlas_g
    for G in graph_atlas_g():
        if 2 <= G.number_of_nodes() <= 7 and nx.is_connected(G):
            yield G
    rng = random.Random(seed); out = 0
    while out < nrand:
        n = rng.randint(8, 14); p = rng.uniform(0.2, 0.85)
        G = nx.gnp_random_graph(n, p, seed=rng.randint(0, 10**9))
        if G.number_of_edges() and nx.is_connected(G):
            out += 1; yield G
    for t in range(1, 7):
        for p in range(1, 5):
            G = nx.complete_graph(t); k = t
            for b in range(t):
                for _ in range(p):
                    G.add_edge(b, k); k += 1
            yield G


F = defaultdict(int); C = defaultdict(int); W = {}
rngs = [None, random.Random(3), random.Random(5)]

for G in corpus():
    n = G.number_of_nodes(); m = G.number_of_edges(); deg = dict(G.degree())
    Delta = max(deg.values()); alpha, MIS = maxis(G); tau = n - alpha
    for rng in rngs:
        D, heads, blocks, vals = hh(deg, rng)
        s = len(D); res = n - s
        hset = set(heads); pos = {l: i+1 for i, l in enumerate(heads)}
        g = [deg[l] for l in heads]; h = [g[i]-D[i] for i in range(s)]
        hs = sum(h)
        C['traces'] += 1

        # ---------- Lemma T : s = tau  <=>  table at start of step tau is [D,1^D,0..]
        if res == alpha:                       # s = tau
            tbl = sorted(vals[s-1].values(), reverse=True)
            want = [D[s-1]] + [1]*D[s-1]
            want += [0]*(len(tbl)-len(want))
            C['T_hits'] += 1
            if tbl != want:
                F['LemT'] += 1; W.setdefault('LemT', (sorted(G.edges()), tbl, want))
        # Lemma T second half: two entries >=2 at start of last-but-one step => res<=alpha-1
        if s >= 2:
            t2 = sorted(vals[s-1].values(), reverse=True)
            if len(t2) >= 2 and t2[1] >= 2:
                C['T2_hits'] += 1
                if res == alpha:
                    F['LemT2'] += 1; W.setdefault('LemT2', sorted(G.edges()))

        # ---------- Lemma H : if h_i <= i-2 then D_i <= s-i+2+h_i   (2<=i<=s)
        for i in range(2, s+1):
            if h[i-1] <= i-2:
                C['H_hyp_ok'] += 1
                if D[i-1] > s - i + 2 + h[i-1]:
                    F['LemH'] += 1; W.setdefault('LemH', (sorted(G.edges()), i, D[i-1], h[i-1]))
            else:
                C['H_hyp_fails'] += 1

        for A in MIS:
            B = set(G.nodes()) - set(A)
            if not B: continue
            eB = G.subgraph(B).number_of_edges()
            mb = min(deg[b] for b in B)
            if not (res == alpha and mb >= tau + 1):
                continue
            # ============ INSIDE THEOREM K's REGIME: availability of the toolkit
            C['K_regime'] += 1
            if hset != B: F['K_KB'] += 1
            if hs != eB: F['K_hs_eB'] += 1
            if eB != tau*(tau-1)//2: F['K_clique'] += 1
            # DICH(b) must apply to EVERY head here
            if any(gi < s+1 for gi in g): F['K_all_high'] += 1
            if h != list(range(s)): F['K_hprofile'] += 1
            # Lemma H availability: needs h_i <= i-2; DICH(b) says h_i = i-1
            if any(h[i-1] <= i-2 for i in range(2, s+1)): C['K_H_available'] += 1
            else: C['K_H_unavailable'] += 1
            # Lemma DEC availability: needs some i in [hs+2, tau]
            if hs + 2 <= tau: C['K_DEC_available'] += 1
            else: C['K_DEC_empty'] += 1
            # Corollary CNT: what would it give here?
            bound = min(tau, hs+1)*Delta + sum(tau-i+2+hs for i in range(hs+2, tau+1))
            if m > bound: F['K_CNT'] += 1
            if bound >= m: C['K_CNT_true_but'] += 1
            if bound == tau*Delta: C['K_CNT_trivialised'] += 1
            # Theorem N hypotheses here?
            if eB <= tau-2: C['K_N_ii_holds'] += 1
            else: C['K_N_ii_fails'] += 1
            # Corollary N2 hypotheses here?
            if eB == 0: C['K_N2_hyp'] += 1
            # Lemma Z availability: beta_j
            beta = [sum(1 for l in blocks[j] if l in hset and pos[l] > j+1) for j in range(s)]
            if any(b == 0 for b in beta): C['K_Z_available'] += 1
            else: C['K_Z_never'] += 1

print('traces=%d' % C['traces'])
print()
print('--- toolkit lemma self-tests -------------------------------------------')
print('  Lemma T   : hits=%-7d failures=%d' % (C['T_hits'], F['LemT']))
print('  Lemma T(2nd half, two entries >=2 at last step => res<alpha):'
      ' hits=%-6d failures=%d' % (C['T2_hits'], F['LemT2']))
print('  Lemma H   : hypothesis h_i<=i-2 held %d times, failed %d times;'
      ' conclusion failures=%d' % (C['H_hyp_ok'], C['H_hyp_fails'], F['LemH']))
print()
print('--- COUNTERFACTUAL AVAILABILITY inside Theorem K\'s regime --------------')
print('  (graph, max-ind-set A) pairs with residue=alpha and min_B deg>=tau+1 : %d'
      % C['K_regime'])
print('    K=B failures                          : %d' % F['K_KB'])
print('    hs=e_B failures                       : %d' % F['K_hs_eB'])
print('    e_B=C(tau,2) (B clique) failures      : %d' % F['K_clique'])
print('    "every head has g>=s+1" failures      : %d' % F['K_all_high'])
print('    h-profile (h_i=i-1 for all i) failures: %d' % F['K_hprofile'])
print('    Lemma H AVAILABLE (some i with h_i<=i-2): %d   UNAVAILABLE: %d'
      % (C['K_H_available'], C['K_H_unavailable']))
print('    Lemma DEC range [hs+2,tau] non-empty  : %d   EMPTY: %d'
      % (C['K_DEC_available'], C['K_DEC_empty']))
print('    Corollary CNT violations              : %d  (bound collapses to tau*Delta in %d)'
      % (F['K_CNT'], C['K_CNT_trivialised']))
print('    Theorem N hyp (ii) e_B<=tau-2 holds   : %d   fails: %d'
      % (C['K_N_ii_holds'], C['K_N_ii_fails']))
print('    Corollary N2 hyp e_B=0 holds          : %d' % C['K_N2_hyp'])
print('    Lemma Z applicable (some beta_j=0)    : %d   never applicable: %d'
      % (C['K_Z_available'], C['K_Z_never']))
print()
for k, v in W.items():
    print('  WITNESS[%s] %s' % (k, str(v)[:300]))

print()
print('--- subsumption arithmetic --------------------------------------------')
for tau in range(1, 9):
    print('  tau=%d : C(tau,2)=%-3d  ThmN (ii) e_B<=tau-2 = %-3d  ->  compatible? %s'
          % (tau, tau*(tau-1)//2, tau-2,
             'YES' if tau*(tau-1)//2 <= tau-2 else 'NO'))

print()
print('--- extended choice-of-A hunt (does hyp (i) depend on WHICH A?) --------')
rng = random.Random(4242); found = 0; both = 0; scanned = 0; ex = []
while scanned < 30000:
    n = rng.randint(5, 11); p = rng.uniform(0.2, 0.8)
    G = nx.gnp_random_graph(n, p, seed=rng.randint(0, 10**9))
    if not G.number_of_edges() or not nx.is_connected(G): continue
    scanned += 1
    deg = dict(G.degree()); alpha, MIS = maxis(G); tau = n - alpha
    if len(MIS) < 2: continue
    sat = []
    for A in MIS:
        B = set(G.nodes()) - set(A)
        if not B: continue
        sat.append((min(deg[b] for b in B) >= tau+1,
                    G.subgraph(B).number_of_edges() == tau*(tau-1)//2, sorted(A)))
    yes = [x for x in sat if x[0]]
    if yes and len(yes) < len(sat):
        found += 1
        D, _, _, _ = hh(deg); res = n - len(D)
        if res == alpha and len(ex) < 4:
            ex.append((sorted(G.edges()), tau, res, alpha, [(x[0], x[1]) for x in sat]))
    if len(yes) >= 2:
        both += 1
print('  scanned=%d   graphs where hyp (i) holds for SOME but not ALL max ind sets: %d'
      % (scanned, found))
print('  graphs where hyp (i) holds for >=2 different max ind sets              : %d' % both)
for e in ex:
    print('    example with residue=alpha: %s' % (e,))
