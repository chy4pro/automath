#!/usr/bin/env python3
"""S3 round-B: two exhaustive tests.

(I)  EXHAUSTIVE TIE-BREAK ENUMERATION.  Not random shuffles: every legal
     labelled Havel-Hakimi execution is enumerated (every choice of which
     maximum-valued entry becomes the head, and every choice of which
     equal-valued entries fall inside the block at the block boundary).
     Z+, DICH(a), DICH(b), DICH(c), S, F3, BO, Z are checked on every branch.
     Also confirms that s and the multiset (D_1..D_s) are tie-break invariant
     while the head SET K is not.

(II) EXHAUSTIVE SEARCH INSIDE THEOREM K'S REGIME.  For tau=2,3 and every
     G[B] on tau vertices, every A-B bipartite adjacency with |A|<=amax and
     min_B deg >= tau+1: is A really a maximum independent set, is residue=alpha,
     and is B a clique?  Theorem K predicts: no instance with residue=alpha,
     min_B deg >= tau+1 and B a non-clique.
"""
import sys, itertools
from collections import defaultdict
import networkx as nx

sys.setrecursionlimit(10000)

# --------------------------------------------------------- (I) all executions
def all_traces(degmap, cap=200000):
    """Yield every legal labelled HH execution as (D, heads, blocks, vals)."""
    items = tuple(sorted(degmap.items()))
    out = []
    seen = 0

    def rec(state, D, heads, blocks, vals):
        nonlocal seen
        if seen > cap:
            return
        vals_now = dict(state)
        pos = [(v, l) for l, v in state.items()]
        mx = max(v for v, l in pos) if pos else 0
        if not pos or mx == 0:
            out.append((tuple(D), tuple(heads), list(blocks), list(vals)))
            seen += 1
            return
        for hv, hl in pos:
            if hv != mx:
                continue
            rest = [(v, l) for v, l in pos if l != hl]
            rest.sort(key=lambda t: -t[0])
            d0 = hv
            if d0 > len(rest):
                continue                       # truncation (should not happen)
            boundary = rest[d0 - 1][0]
            strict = [l for v, l in rest[:d0] if v > boundary]
            ties = [l for v, l in rest if v == boundary]
            need = d0 - len(strict)
            for chosen in itertools.combinations(sorted(ties), need):
                blk = set(strict) | set(chosen)
                ns = dict(state)
                del ns[hl]
                for l in blk:
                    ns[l] -= 1
                rec(ns, D + [d0], heads + [hl], blocks + [blk], vals + [vals_now])

    rec(dict(degmap), [], [], [], [])
    return out


def audit_trace(degmap, D, heads, blocks, vals):
    s = len(D)
    hset = set(heads); pos = {l: i + 1 for i, l in enumerate(heads)}
    surv = set(degmap) - hset
    g = [degmap[l] for l in heads]
    h = [g[i] - D[i] for i in range(s)]
    bad = []
    for j in range(1, s + 1):
        for lab, v in vals[j - 1].items():
            if lab in surv and v > s - j + 1:
                bad.append(('F3', j, lab, v))
            if lab in hset and pos[lab] > j and v > s - j + 1 and lab not in blocks[j - 1]:
                bad.append(('Zplus', j, lab, v))
            if lab in hset and pos[lab] > j and v > s - j + 1 and j < s:
                if lab in vals[j] and not vals[j][lab] > s - j:
                    bad.append(('DICHa', j, lab))
    for lab in surv:
        if degmap[lab] > s:
            bad.append(('S', lab))
    for i in range(1, s + 1):
        if g[i - 1] >= s + 1 and (h[i - 1] != i - 1 or D[i - 1] != g[i - 1] - (i - 1)):
            bad.append(('DICHb', i, g[i - 1], D[i - 1], h[i - 1]))
        if g[i - 1] <= s and D[i - 1] > s - i + 2:
            bad.append(('DICHc', i, g[i - 1], D[i - 1]))
    beta = [sum(1 for l in blocks[j] if l in hset and pos[l] > j + 1) for j in range(s)]
    if sum(beta) != sum(h):
        bad.append(('BO', sum(beta), sum(h)))
    for j in range(s):
        if beta[j] == 0:
            for i in range(j + 1, s):
                if D[i] > s - (j + 1) + 1:
                    bad.append(('Z', j + 1, i + 1))
    return bad


def part1():
    print('=' * 78)
    print('(I) EXHAUSTIVE TIE-BREAK ENUMERATION (every legal HH execution)')
    from networkx.generators.atlas import graph_atlas_g
    tot_g = tot_t = 0; fails = defaultdict(int); wit = {}
    s_varies = D_varies = K_varies = 0
    corpus = [G for G in graph_atlas_g()
              if 2 <= G.number_of_nodes() <= 7 and nx.is_connected(G)]
    # plus a few dense named graphs where ties are rampant
    extra = [nx.complete_graph(k) for k in range(2, 9)] + \
            [nx.complete_bipartite_graph(a, b) for a in range(1, 5) for b in range(1, 6)] + \
            [nx.cycle_graph(k) for k in range(3, 12)] + \
            [nx.circulant_graph(9, [1, 2]), nx.circulant_graph(10, [1, 3]),
             nx.petersen_graph(), nx.hypercube_graph(3), nx.hypercube_graph(4)]
    for G in corpus + extra:
        deg = {str(v): d for v, d in G.degree()}
        if not deg:
            continue
        tr = all_traces(deg, cap=4000)
        if not tr:
            continue
        tot_g += 1
        ss = set(len(t[0]) for t in tr)
        DD = set(t[0] for t in tr)
        KK = set(frozenset(t[1]) for t in tr)
        if len(ss) > 1: s_varies += 1
        if len(DD) > 1: D_varies += 1
        if len(KK) > 1: K_varies += 1
        for D, heads, blocks, vals in tr:
            tot_t += 1
            for b in audit_trace(deg, D, list(heads), blocks, vals):
                fails[b[0]] += 1
                wit.setdefault(b[0], (sorted(G.edges()), b))
    print('  graphs=%d   distinct legal executions enumerated=%d' % (tot_g, tot_t))
    print('  graphs where s varies with the tie-break      : %d' % s_varies)
    print('  graphs where the head vector D varies         : %d' % D_varies)
    print('  graphs where the head SET K varies            : %d  (K is NOT tie-invariant)'
          % K_varies)
    print('  violations = %s' % (dict(fails) or 'ALL ZERO'))
    for k, v in wit.items():
        print('   WITNESS[%s] %s' % (k, v))


# --------------------------------------- (II) exhaustive Theorem K regime search
def residue_of(deg_list):
    s = sorted(deg_list, reverse=True); steps = 0
    while True:
        if not s: return 0, steps
        if s[0] == 0: return len(s), steps
        d0 = s[0]; rest = s[1:]
        s = sorted([max(0, x - 1) for x in rest[:d0]] + rest[d0:], reverse=True)
        steps += 1


def part2(taus=(2, 3), amax=(7, 5)):
    print()
    print('=' * 78)
    print('(II) EXHAUSTIVE SEARCH INSIDE THEOREM K\'S REGIME')
    print('   for each tau, each graph G[B] on B, each A-B bipartite adjacency:')
    print('   keep those with G connected, A a MAXIMUM independent set,')
    print('   min_B deg >= tau+1.  Report residue vs alpha and B clique or not.')
    for tau, am in zip(taus, amax):
        Bpairs = list(itertools.combinations(range(tau), 2))
        tot = keep = resa = nonclique_resa = nonclique_total = 0
        clique_resa = 0
        examples = []
        for a in range(1, am + 1):
            n = tau + a
            for bmask in range(1 << len(Bpairs)):
                Bedges = [Bpairs[i] for i in range(len(Bpairs)) if bmask >> i & 1]
                eB = len(Bedges)
                for amask in range(1 << (tau * a)):
                    tot += 1
                    G = nx.Graph(); G.add_nodes_from(range(n))
                    G.add_edges_from(Bedges)
                    k = 0
                    for bi in range(tau):
                        for aj in range(a):
                            if amask >> k & 1:
                                G.add_edge(bi, tau + aj)
                            k += 1
                    if not nx.is_connected(G):
                        continue
                    deg = dict(G.degree())
                    if min(deg[b] for b in range(tau)) < tau + 1:
                        continue
                    # A must be a maximum independent set
                    H = nx.complement(G)
                    alpha = max(len(c) for c in nx.find_cliques(H))
                    if alpha != a:
                        continue
                    keep += 1
                    res, steps = residue_of(list(deg.values()))
                    isclique = (eB == tau * (tau - 1) // 2)
                    if not isclique:
                        nonclique_total += 1
                    if res == alpha:
                        resa += 1
                        if isclique:
                            clique_resa += 1
                        else:
                            nonclique_resa += 1
                            if len(examples) < 5:
                                examples.append((sorted(G.edges()), eB, res, alpha))
        print('  tau=%d, |A|<=%d : candidates scanned=%d  admissible=%d'
              % (tau, am, tot, keep))
        print('     admissible with B a NON-clique             : %d' % nonclique_total)
        print('     admissible with residue=alpha              : %d' % resa)
        print('       ... of those, B a clique                 : %d' % clique_resa)
        print('       ... of those, B a NON-clique (ThmK FAILS): %d' % nonclique_resa)
        for e in examples:
            print('       COUNTEREXAMPLE %s' % (e,))


if __name__ == '__main__':
    part1()
    part2()
