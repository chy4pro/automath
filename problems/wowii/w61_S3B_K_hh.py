#!/usr/bin/env python3
"""S3 round-B independent referee harness for the K-chain (Lemma Z+, Lemma DICH,
Theorem K, Corollary K1) of notes/proofs/wowii61_draft.md sec 7.5, plus the
sec 7.2B / 7.4 toolkit it rests on.

Everything here is written from the LEMMA STATEMENTS ONLY; no code from the
draft's own scripts is read or reused.  Labelled Havel-Hakimi with randomised
adversarial tie-breaking.

Usage: python3 w61_S3B_K_hh.py [quick|full]
"""
import sys, random, itertools, math
from collections import defaultdict
import networkx as nx

# ----------------------------------------------------------------- HH engine
def hh_trace(degmap, rng=None):
    """Labelled Havel-Hakimi.

    degmap : dict label -> degree.
    rng    : if given, equal-valued entries are permuted adversarially before
             the (stable) non-increasing sort.

    Returns dict with:
      s        number of steps performed (residue = n - s)
      D        [D_1..D_s] head values
      heads    [label_1..label_s] head labels, in deletion order
      blocks   [set of labels] block of each step
      vals     [dict label->value at START of step j]  (j=1..s)
      trunc    True if the N-truncated subtraction ever truncated
    """
    entries = [[d, lab] for lab, d in degmap.items()]
    D, heads, blocks, vals = [], [], [], []
    trunc = False
    while True:
        if rng is not None:
            rng.shuffle(entries)
        entries.sort(key=lambda e: -e[0])
        if not entries:
            break
        if entries[0][0] == 0:
            break
        d0 = entries[0][0]
        if d0 > len(entries) - 1:
            trunc = True
        vals.append({lab: v for v, lab in entries})
        D.append(d0)
        heads.append(entries[0][1])
        blk = entries[1:1 + d0]
        blocks.append(set(lab for v, lab in blk))
        for e in blk:
            e[0] = max(0, e[0] - 1)
        entries = entries[1:]
    return dict(s=len(D), D=D, heads=heads, blocks=blocks, vals=vals, trunc=trunc)


def residue_literal(degs):
    """Literal transcription of Lean residueAux on a plain degree list."""
    s = sorted(degs, reverse=True)
    while True:
        if not s:
            return 0
        if s[0] == 0:
            return len(s)
        d0 = s[0]
        rest = s[1:]
        head, tail = rest[:d0], rest[d0:]
        s = sorted([max(0, x - 1) for x in head] + tail, reverse=True)


# ------------------------------------------------------------- graph helpers
def all_max_ind_sets(G):
    """Every maximum independent set, as frozensets."""
    H = nx.complement(G)
    best, out = 0, []
    for c in nx.find_cliques(H):
        if len(c) > best:
            best, out = len(c), [frozenset(c)]
        elif len(c) == best:
            out.append(frozenset(c))
    if not out:                       # empty graph edge case
        return 0, []
    return best, out


# ------------------------------------------------------------------ the checks
FAILKEYS = ['TRUNC', 'L1_sum', 'L1_res', 'L1_D1', 'F3', 'S', 'Zplus', 'DICHa',
            'DICHb', 'DICHc', 'BO', 'Z', 'DEC', 'KB', 'ThmK', 'CorK1', 'CNT',
            'N2patch', 'N1', 'ThmN']
COUNTKEYS = ['graphs', 'traces', 'res_eq_alpha', 'hyp_i', 'ThmK_hits',
             'ThmK_clique', 'CorK1_hits', 'N2patch_hits', 'N2raw_hits',
             'N2raw_fails', 'ctrlA_hits', 'ctrlA_fails', 'CNTnomin_fails',
             'DICHb_hits', 'DICHc_hits', 'Zplus_hits', 'diam4']


def check_graph(G, fails, cnt, wit, rngs):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    deg = dict(G.degree())
    Delta = max(deg.values()) if deg else 0
    alpha, MIS = all_max_ind_sets(G)
    tau = n - alpha
    res_lit = residue_literal(list(deg.values()))
    cnt['graphs'] += 1
    try:
        diam = nx.diameter(G)
    except Exception:
        diam = None
    if diam == 4:
        cnt['diam4'] += 1
    if res_lit == alpha:
        cnt['res_eq_alpha'] += 1

    # degree sequence sorted, for control case (a)
    dsort = sorted(deg.values(), reverse=True)

    for rng in rngs:
        T = hh_trace(deg, rng)
        cnt['traces'] += 1
        s, D, heads, blocks, vals = T['s'], T['D'], T['heads'], T['blocks'], T['vals']
        if T['trunc']:
            fails['TRUNC'] += 1; wit.setdefault('TRUNC', str(sorted(G.edges())))
        # Lemma 1
        if sum(D) != m:
            fails['L1_sum'] += 1; wit.setdefault('L1_sum', str(sorted(G.edges())))
        if n - s != res_lit:
            fails['L1_res'] += 1; wit.setdefault('L1_res', str(sorted(G.edges())))
        if D and D[0] != Delta:
            fails['L1_D1'] += 1; wit.setdefault('L1_D1', str(sorted(G.edges())))

        headset = set(heads)
        pos = {lab: i + 1 for i, lab in enumerate(heads)}   # 1-based step index
        survivors = set(G.nodes()) - headset
        g = [deg[lab] for lab in heads]
        h = [g[i] - D[i] for i in range(s)]
        hs = sum(h)

        # ---- Lemma F3 : survivor value at start of step j is <= s-j+1
        for j in range(1, s + 1):
            for lab, v in vals[j - 1].items():
                if lab in survivors and v > s - j + 1:
                    fails['F3'] += 1; wit.setdefault('F3', str(sorted(G.edges())))
        # ---- Lemma S : survivor degree <= s   (draft states it with tau, under res=alpha)
        for lab in survivors:
            if deg[lab] > s:
                fails['S'] += 1; wit.setdefault('S', str(sorted(G.edges())))

        # ---- Lemma Z+ : later head with value > s-j+1 at start of step j lies in block_j
        for j in range(1, s + 1):
            for lab, v in vals[j - 1].items():
                if lab in headset and pos[lab] > j and v > s - j + 1:
                    cnt['Zplus_hits'] += 1
                    if lab not in blocks[j - 1]:
                        fails['Zplus'] += 1
                        wit.setdefault('Zplus', str(sorted(G.edges())))
        # ---- DICH(a) persistence : excess at step j<i  =>  excess at step j+1
        for j in range(1, s):
            for lab, v in vals[j - 1].items():
                if lab in headset and pos[lab] > j and v > s - j + 1:
                    if j + 1 <= s and lab in vals[j]:
                        if not (vals[j][lab] > s - (j + 1) + 1):
                            fails['DICHa'] += 1
                            wit.setdefault('DICHa', str(sorted(G.edges())))
        # ---- DICH(b) : g >= s+1  =>  h_i = i-1 and D_i = g-(i-1) EXACTLY
        for i in range(1, s + 1):
            if g[i - 1] >= s + 1:
                cnt['DICHb_hits'] += 1
                if h[i - 1] != i - 1 or D[i - 1] != g[i - 1] - (i - 1):
                    fails['DICHb'] += 1
                    wit.setdefault('DICHb', str(sorted(G.edges())))
        # ---- DICH(c) : g <= s  =>  D_i <= s-i+2   unconditionally
        for i in range(1, s + 1):
            if g[i - 1] <= s:
                cnt['DICHc_hits'] += 1
                if D[i - 1] > s - i + 2:
                    fails['DICHc'] += 1
                    wit.setdefault('DICHc', str(sorted(G.edges())))
        # ---- beta_j and Lemma BO
        beta = []
        for j in range(1, s + 1):
            beta.append(sum(1 for lab in blocks[j - 1] if lab in headset and pos[lab] > j))
        if sum(beta) != hs:
            fails['BO'] += 1; wit.setdefault('BO', str(sorted(G.edges())))
        # ---- Lemma Z : beta_j = 0  =>  D_i <= s-j+1 for i>j
        for j in range(1, s + 1):
            if beta[j - 1] == 0:
                for i in range(j + 1, s + 1):
                    if D[i - 1] > s - j + 1:
                        fails['Z'] += 1; wit.setdefault('Z', str(sorted(G.edges())))
        # ---- Lemma DEC (stated under res=alpha, s=tau) : i>=hs+2 => D_i <= s-i+2+hs
        for i in range(hs + 2, s + 1):
            if D[i - 1] > s - i + 2 + hs:
                fails['DEC'] += 1; wit.setdefault('DEC', str(sorted(G.edges())))
        # ---- control case (a): D_i <= d_i - (i-1)  (KNOWN FALSE)
        for i in range(1, s + 1):
            cnt['ctrlA_hits'] += 1
            if D[i - 1] > dsort[i - 1] - (i - 1):
                cnt['ctrlA_fails'] += 1
                wit.setdefault('ctrlA', 'degseq=%s heads=%s' % (dsort, D))

        # ---- statements that mention A / B : quantify over EVERY maximum ind set
        for A in MIS:
            B = set(G.nodes()) - set(A)
            eB = G.subgraph(B).number_of_edges()
            if not B:
                continue
            mindegB = min(deg[b] for b in B)
            hyp_i = (mindegB >= tau + 1)
            if hyp_i:
                cnt['hyp_i'] += 1
            # Theorem K
            if res_lit == alpha and hyp_i:
                cnt['ThmK_hits'] += 1
                if headset != B:
                    fails['KB'] += 1; wit.setdefault('KB', str(sorted(G.edges())))
                if eB != tau * (tau - 1) // 2:
                    fails['ThmK'] += 1
                    wit.setdefault('ThmK', 'E=%s A=%s' % (sorted(G.edges()), sorted(A)))
                else:
                    cnt['ThmK_clique'] += 1
            # Corollary K1
            if diam == 4 and hyp_i:
                cnt['CorK1_hits'] += 1
                if not (res_lit <= alpha - 1):
                    fails['CorK1'] += 1
                    wit.setdefault('CorK1', 'E=%s A=%s' % (sorted(G.edges()), sorted(A)))
            # Corollary CNT  (under res = alpha; hs computed from THIS trace)
            if res_lit == alpha:
                bound = min(tau, hs + 1) * Delta + sum(
                    (tau - i + 2 + hs) for i in range(hs + 2, tau + 1))
                if m > bound:
                    fails['CNT'] += 1; wit.setdefault('CNT', str(sorted(G.edges())))
                bad = (hs + 1) * Delta + sum(
                    (tau - i + 2 + hs) for i in range(hs + 2, tau + 1))
                closed_bad = ((hs + 1) * Delta + tau * (tau + 1) // 2
                              - (hs + 1) * (hs + 2) // 2)
                if m > bad or m > closed_bad:
                    cnt['CNTnomin_fails'] += 1
                    wit.setdefault('CNTnomin',
                                   'E=%s tau=%d hs=%d m=%d Delta=%d bad=%d closed=%d'
                                   % (sorted(G.edges()), tau, hs, m, Delta, bad, closed_bad))
            # Corollary N2 -- raw (unqualified, KNOWN FALSE) and patched
            if hyp_i and eB == 0:
                cnt['N2raw_hits'] += 1
                if m > Delta + tau * (tau + 1) // 2 - 1:
                    cnt['N2raw_fails'] += 1
                    wit.setdefault('N2raw', 'E=%s A=%s tau=%d m=%d Delta=%d'
                                   % (sorted(G.edges()), sorted(A), tau, m, Delta))
                if res_lit == alpha:
                    cnt['N2patch_hits'] += 1
                    if m > Delta + tau * (tau + 1) // 2 - 1:
                        fails['N2patch'] += 1
                        wit.setdefault('N2patch', str(sorted(G.edges())))
                # Corollary N1
                if tau >= 2 and not (res_lit <= alpha - 1):
                    fails['N1'] += 1; wit.setdefault('N1', str(sorted(G.edges())))
            # Theorem N
            if hyp_i and eB <= tau - 2 and mindegB >= 2 * eB + 3:
                if not (res_lit <= alpha - 1):
                    fails['ThmN'] += 1; wit.setdefault('ThmN', str(sorted(G.edges())))


# ------------------------------------------------------------------- corpora
def atlas_connected(nmax):
    from networkx.generators.atlas import graph_atlas_g
    for G in graph_atlas_g():
        if 2 <= G.number_of_nodes() <= nmax and nx.is_connected(G):
            yield G


def n8_cover():
    """Every connected 8-vertex graph is H+v for connected H on 7 and non-empty
    N(v) subset V(H).  853 x 127 pairs."""
    sevens = [G for G in atlas_connected(7) if G.number_of_nodes() == 7]
    for H in sevens:
        nodes = list(H.nodes())
        for mask in range(1, 128):
            G = nx.Graph()
            G.add_nodes_from(range(7))
            G.add_edges_from((nodes.index(u), nodes.index(v)) for u, v in H.edges())
            for k in range(7):
                if mask >> k & 1:
                    G.add_edge(7, k)
            yield G


def random_graphs(count, nlo, nhi, seed):
    rng = random.Random(seed)
    out = 0
    while out < count:
        n = rng.randint(nlo, nhi)
        p = rng.uniform(0.25, 0.8)
        G = nx.gnp_random_graph(n, p, seed=rng.randint(0, 10 ** 9))
        if G.number_of_edges() == 0 or not nx.is_connected(G):
            continue
        out += 1
        yield G


def structured():
    for n in range(3, 14):
        yield nx.cycle_graph(n)
        yield nx.path_graph(n)
        yield nx.complete_graph(n)
        yield nx.wheel_graph(n)
    for a in range(1, 6):
        for b in range(1, 6):
            yield nx.complete_bipartite_graph(a, b)
    for a in range(2, 5):
        for b in range(2, 5):
            for c in range(1, 4):
                yield nx.complete_multipartite_graph(a, b, c)
    # B-clique-with-pendants family: B = K_t, each b gets p private A-leaves
    for t in range(1, 6):
        for p in range(1, 5):
            G = nx.complete_graph(t)
            nxt = t
            for b in range(t):
                for _ in range(p):
                    G.add_edge(b, nxt); nxt += 1
            yield G
    # Family I(tau,c): B independent, c universal-ish vertices + 2 private leaves
    for tau in range(2, 7):
        for c in range(2, 9):
            G = nx.Graph()
            Bv = ['b%d' % i for i in range(tau)]
            Av = ['a%d' % i for i in range(c)]
            for b in Bv:
                for a in Av:
                    G.add_edge(b, a)
                G.add_edge(b, 'p%s' % b)
                G.add_edge(b, 'q%s' % b)
            yield G


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'quick'
    fails = defaultdict(int); cnt = defaultdict(int); wit = {}
    rngs = [None] + [random.Random(1000 + k) for k in range(4)]

    def run(tag, it):
        f0 = dict(fails); c0 = dict(cnt)
        for G in it:
            check_graph(G, fails, cnt, wit, rngs)
        print('[%s] graphs=%d traces=%d res=alpha:%d  fails=%s' % (
            tag, cnt['graphs'] - c0.get('graphs', 0),
            cnt['traces'] - c0.get('traces', 0),
            cnt['res_eq_alpha'] - c0.get('res_eq_alpha', 0),
            {k: fails[k] - f0.get(k, 0) for k in FAILKEYS if fails[k] - f0.get(k, 0)} or 0))
        sys.stdout.flush()

    run('A exhaustive n<=7 (atlas)', atlas_connected(7))
    run('C structured families', structured())
    run('D random n=8..13', random_graphs(2500 if mode == 'quick' else 6000,
                                          8, 13, 20260818))
    if mode == 'full':
        run('B exhaustive n=8 cover', n8_cover())

    print()
    print('TOTAL fails  =', {k: fails[k] for k in FAILKEYS if fails[k]} or 'ALL ZERO')
    print('TOTAL counts =', {k: cnt[k] for k in COUNTKEYS if cnt[k]})
    print()
    for k, v in sorted(wit.items()):
        print('WITNESS[%s] %s' % (k, v[:400]))


if __name__ == '__main__':
    main()
