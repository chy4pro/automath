#!/usr/bin/env python3
"""S3 round-B targeted probes for the K-chain.

(1) DETERMINISTIC ADVERSARIAL tie-break policies (not just random shuffles):
    the adversary tries to push future heads OUT of the block, which is exactly
    what Lemma Z+ / DICH(b) forbid.
(2) Named control cases: degseq [3,3,3,3,3,2,1]; K_{2,3}; K_6 / Corollary CNT.
(3) Boundary sweeps: tau=1,2,3; e_B=0; i=1 and i=s; g=s vs g=s+1; last HH step.
(4) Counterfactual availability: at each point where the K-chain invokes a
    toolkit lemma, check that lemma's hypotheses AND report what every OTHER
    toolkit lemma would give there if applied.
(5) Choice-of-A probe for Corollary K1.
"""
import sys, itertools, random
from collections import defaultdict
import networkx as nx


# --------------------------------------------------- HH with pluggable tie-break
def hh_trace(degmap, policy='canon', rng=None):
    """policy in {canon, orig_asc, orig_desc, lab_desc, rand}.
    orig_asc = among entries of equal CURRENT value, the ones with the LARGEST
    ORIGINAL degree are pushed to the END (most likely future heads pushed out
    of the block) -- the adversarial policy against Z+/DICH(b)."""
    ent = [[d, lab, d] for lab, d in degmap.items()]   # [cur, label, orig]
    D, heads, blocks, vals = [], [], [], []
    while True:
        if policy == 'rand':
            rng.shuffle(ent)
            ent.sort(key=lambda e: -e[0])
        elif policy == 'orig_asc':
            ent.sort(key=lambda e: (-e[0], e[2], e[1]))
        elif policy == 'orig_desc':
            ent.sort(key=lambda e: (-e[0], -e[2], e[1]))
        elif policy == 'lab_desc':
            ent.sort(key=lambda e: (-e[0], -hash(e[1]) % 997))
        else:
            ent.sort(key=lambda e: -e[0])
        if not ent or ent[0][0] == 0:
            break
        d0 = ent[0][0]
        vals.append({e[1]: e[0] for e in ent})
        D.append(d0); heads.append(ent[0][1])
        blk = ent[1:1 + d0]
        blocks.append(set(e[1] for e in blk))
        for e in blk:
            e[0] = max(0, e[0] - 1)
        ent = ent[1:]
    return dict(s=len(D), D=D, heads=heads, blocks=blocks, vals=vals)


POLICIES = ['canon', 'orig_asc', 'orig_desc', 'lab_desc'] + ['rand'] * 6


def audit(degmap, G=None):
    """Return dict of per-policy violation reports for Z+, DICH(a/b/c), and the
    tie-break-invariance of s and of the head multiset."""
    rng = random.Random(7)
    out = []
    for pol in POLICIES:
        T = hh_trace(degmap, pol, rng)
        s, D, heads, blocks, vals = T['s'], T['D'], T['heads'], T['blocks'], T['vals']
        hs_set, pos = set(heads), {l: i + 1 for i, l in enumerate(heads)}
        g = [degmap[l] for l in heads]
        h = [g[i] - D[i] for i in range(s)]
        bad = []
        for j in range(1, s + 1):
            for lab, v in vals[j - 1].items():
                if lab in hs_set and pos[lab] > j and v > s - j + 1 and lab not in blocks[j - 1]:
                    bad.append(('Zplus', j, lab, v))
        for i in range(1, s + 1):
            if g[i - 1] >= s + 1 and (h[i - 1] != i - 1 or D[i - 1] != g[i - 1] - (i - 1)):
                bad.append(('DICHb', i, heads[i - 1], g[i - 1], D[i - 1], h[i - 1]))
            if g[i - 1] <= s and D[i - 1] > s - i + 2:
                bad.append(('DICHc', i, heads[i - 1], g[i - 1], D[i - 1]))
        out.append((pol, s, tuple(D), tuple(sorted(hs_set)), bad))
    return out


def show(name, degmap, G=None):
    rep = audit(degmap, G)
    ss = set(r[1] for r in rep); DD = set(r[2] for r in rep)
    Ks = set(r[3] for r in rep)
    badtot = sum(len(r[4]) for r in rep)
    print('  %-28s s=%s  D=%s  #distinct-K=%d  violations=%d'
          % (name, sorted(ss), sorted(DD), len(Ks), badtot))
    for pol, s, D, K, bad in rep:
        if bad:
            print('      !! policy=%s  %s' % (pol, bad[:4]))
    return rep


print('=' * 78)
print('(2a) CONTROL (a): "D_i <= d_i - (i-1)"  on degseq [3,3,3,3,3,2,1]')
dm = {i: d for i, d in enumerate([3, 3, 3, 3, 3, 2, 1])}
rep = show('[3,3,3,3,3,2,1]', dm)
T = hh_trace(dm)
print('      heads D =', T['D'], ' s =', T['s'], ' residue = 7 - s =', 7 - T['s'])
dsort = sorted(dm.values(), reverse=True)
for i, Di in enumerate(T['D'], 1):
    print('      i=%d  D_i=%d  d_i=%d  d_i-(i-1)=%d  %s'
          % (i, Di, dsort[i - 1], dsort[i - 1] - (i - 1),
             'VIOLATES control (a)' if Di > dsort[i - 1] - (i - 1) else 'ok'))
print('      DICH(c) bound s-i+2 =', [T['s'] - i + 2 for i in range(1, T['s'] + 1)])
G7 = nx.Graph([(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 4), (3, 4), (3, 5), (4, 6)])
print('      realising graph degseq:', sorted([d for _, d in G7.degree()], reverse=True),
      ' connected:', nx.is_connected(G7))

print()
print('=' * 78)
print('(2b) CONTROL (b): K_{2,3} vs Corollary N2')
G = nx.complete_bipartite_graph(2, 3)
deg = dict(G.degree()); n = G.number_of_nodes(); m = G.number_of_edges()
A = frozenset([2, 3, 4]); B = set(G.nodes()) - A
alpha = len(A); tau = n - alpha
eB = G.subgraph(B).number_of_edges(); Delta = max(deg.values())
T = hh_trace(deg)
print('  degrees=%s  n=%d m=%d alpha=%d tau=%d e_B=%d Delta=%d' %
      (sorted(deg.values(), reverse=True), n, m, alpha, tau, eB, Delta))
print('  HH heads D=%s  s=%d  residue=n-s=%d   alpha-1=%d' %
      (T['D'], T['s'], n - T['s'], alpha - 1))
print('  min_B deg = %d  (tau+1 = %d)  hypothesis (i): %s'
      % (min(deg[b] for b in B), tau + 1, min(deg[b] for b in B) >= tau + 1))
print('  N2 RHS  Delta + tau(tau+1)/2 - 1 = %d   m = %d   -> unqualified N2 %s'
      % (Delta + tau * (tau + 1) // 2 - 1, m,
         'FALSE' if m > Delta + tau * (tau + 1) // 2 - 1 else 'holds'))
print('  reductio standpoint residue==alpha ? %s  -> patched N2 vacuous here'
      % (n - T['s'] == alpha))
print('  contrapositive form: m > RHS and indeed residue=%d <= alpha-1=%d : %s'
      % (n - T['s'], alpha - 1, n - T['s'] <= alpha - 1))
show('K_{2,3}', deg)

print()
print('=' * 78)
print('(2c) CONTROL (d): K_6 vs Corollary CNT (with and without the min)')
G = nx.complete_graph(6)
deg = dict(G.degree()); n = 6; m = 15
alpha = 1; tau = 5; Delta = 5
T = hh_trace(deg); s = T['s']; D = T['D']
heads = T['heads']; g = [deg[l] for l in heads]
hs = sum(g[i] - D[i] for i in range(s))
print('  K_6: s=%d D=%s residue=%d alpha=%d tau=%d hs=%d m=%d Delta=%d'
      % (s, D, n - s, alpha, tau, hs, m, Delta))
sm = sum(tau - i + 2 + hs for i in range(hs + 2, tau + 1))
print('  CNT with min : min(tau,hs+1)*Delta + sum = %d*%d + %d = %d   (m=%d) -> %s'
      % (min(tau, hs + 1), Delta, sm, min(tau, hs + 1) * Delta + sm, m,
         'holds' if m <= min(tau, hs + 1) * Delta + sm else 'FALSE'))
print('  CNT min DROPPED, sum form : (hs+1)*Delta + sum = %d   -> %s'
      % ((hs + 1) * Delta + sm,
         'holds (WEAKER, not false!)' if m <= (hs + 1) * Delta + sm else 'FALSE'))
cf = (hs + 1) * Delta + tau * (tau + 1) // 2 - (hs + 1) * (hs + 2) // 2
print('  CLOSED form (hs+1)Delta + t(t+1)/2 - (hs+1)(hs+2)/2 = %d  -> %s'
      % (cf, 'FALSE' if m > cf else 'holds'))
print('  NOTE: the closed form is only equal to the sum when hs+2 <= tau+1,')
print('        i.e. hs <= tau-1.  Here hs=%d > tau-1=%d, empty sum vs negative.'
      % (hs, tau - 1))

print()
print('=' * 78)
print('(3) BOUNDARY SWEEPS')


def named_cases():
    yield 'K_2 (tau=1)', nx.complete_graph(2)
    yield 'star K_{1,4} (tau=1,e_B=0)', nx.star_graph(4)
    yield 'P_3', nx.path_graph(3)
    yield 'P_5 (diam 4, tau=2)', nx.path_graph(5)
    yield 'C_5', nx.cycle_graph(5)
    yield 'K_{3,3}', nx.complete_bipartite_graph(3, 3)
    yield 'K_{2,4}', nx.complete_bipartite_graph(2, 4)
    yield 'K_4', nx.complete_graph(4)
    yield 'K_6', nx.complete_graph(6)
    # B = K_tau clique with p private leaves each  (Theorem K's extremal shape)
    for t in (1, 2, 3, 4):
        for p in (1, 2, 3):
            G = nx.complete_graph(t); nxt = t
            for b in range(t):
                for _ in range(p):
                    G.add_edge(b, nxt); nxt += 1
            yield 'K_%d + %d leaves each' % (t, p), G


def maxis(G):
    H = nx.complement(G); best, out = 0, []
    for c in nx.find_cliques(H):
        if len(c) > best: best, out = len(c), [frozenset(c)]
        elif len(c) == best: out.append(frozenset(c))
    return best, out


for name, G in named_cases():
    n = G.number_of_nodes(); m = G.number_of_edges(); deg = dict(G.degree())
    alpha, MIS = maxis(G); tau = n - alpha
    T = hh_trace(deg); s = T['s']; res = n - s
    heads = T['heads']; D = T['D']; g = [deg[l] for l in heads]
    lines = []
    for A in MIS:
        B = set(G.nodes()) - set(A)
        if not B: continue
        eB = G.subgraph(B).number_of_edges()
        mb = min(deg[b] for b in B)
        lines.append((sorted(A), eB, mb, mb >= tau + 1, eB == tau * (tau - 1) // 2))
    hyp = [l for l in lines if l[3]]
    print('  %-28s n=%d m=%d alpha=%d tau=%d s=%d res=%d D=%s' %
          (name, n, m, alpha, tau, s, res, D))
    print('       #MIS=%d  with hyp(i): %d   res==alpha: %s' % (len(MIS), len(hyp), res == alpha))
    for A, eB, mb, hi, cl in lines:
        flag = ''
        if res == alpha and hi:
            flag = ' <- ThmK applies: B clique? %s (e_B=%d, C(tau,2)=%d)' % (
                cl, eB, tau * (tau - 1) // 2)
        print('       A=%-16s e_B=%d min_Bdeg=%d hyp(i)=%s%s' % (A, eB, mb, hi, flag))
    # per-head g vs s boundary
    print('       heads: ' + ', '.join(
        'i=%d g=%d D_i=%d h_i=%d [%s]' % (
            i + 1, g[i], D[i], g[i] - D[i],
            'DICHb g>=s+1' if g[i] >= s + 1 else 'DICHc g<=s')
        for i in range(s)))

print()
print('=' * 78)
print('(5) CHOICE-OF-A PROBE: graphs with >1 maximum independent set where the')
print('    hypothesis min_B deg >= tau+1 holds for SOME but not ALL choices of A')
from networkx.generators.atlas import graph_atlas_g
mixed = 0; mixed_ex = []; kdisagree = 0
for G in graph_atlas_g():
    if G.number_of_nodes() < 2 or not nx.is_connected(G): continue
    n = G.number_of_nodes(); deg = dict(G.degree())
    alpha, MIS = maxis(G); tau = n - alpha
    if len(MIS) < 2: continue
    T = hh_trace(deg); res = n - T['s']
    sat = []
    for A in MIS:
        B = set(G.nodes()) - set(A)
        if not B: continue
        sat.append((min(deg[b] for b in B) >= tau + 1,
                    G.subgraph(B).number_of_edges() == tau * (tau - 1) // 2))
    if any(x[0] for x in sat) and not all(x[0] for x in sat):
        mixed += 1
        if res == alpha and len(mixed_ex) < 6:
            mixed_ex.append((sorted(G.edges()), tau, res, alpha, sat))
    # do all hypothesis-satisfying A give a clique B?
    if res == alpha:
        for hi, cl in sat:
            if hi and not cl: kdisagree += 1
print('    connected atlas graphs with >=2 MIS and hyp(i) A-dependent: %d' % mixed)
print('    among those with residue==alpha (ThmK live), examples:')
for e in mixed_ex:
    print('      E=%s tau=%d res=%d alpha=%d  per-A (hyp_i, B-clique)=%s' % e)
print('    ThmK failures over ALL (graph, hypothesis-satisfying A) pairs:', kdisagree)
