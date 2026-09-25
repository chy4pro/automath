"""owner-w61 round 4 — independent check of Theorem LOW (the tau-uniform K != B bound).

Written by owner-w61 from scratch (own labelled-HH implementation, own corpus
driver) so that it does NOT reuse the round-3 helper's `w61_r4_probe.py`.

Claims tested, all under the reductio hypothesis residue(G) = alpha(G) (s = tau):

  B_hi = {b in B : deg(b) >= tau+1},  p = |B_hi|,  B_lo = B \\ B_hi,  L = |B_lo|
  nu   = C(tau,2) - e_B          (number of non-adjacent pairs inside B)
  mbar = nu restricted to B_hi

  LOW1   Sum_{b in B_lo} deg(b) + nu <= L * (tau+1)
  LOW2   Sum_{b in B_lo} deg_A(b) + e(B_lo) + mbar <= L*(L+3)/2      (equivalent form)
  LOW3   Sum_{b in B_lo} deg_A(b) + mbar <= 2L + nu(B_lo)            (equivalent form)
  POS    Sum_{i in I_hi}(i-1) + Sum_{i in I_lo}(tau-i+2) = -C(tau,2) + L*(tau+1)
         (the position-independence identity the proof turns on)
  DICHb  every head of original degree >= s+1 satisfies h_i = i-1 and D_i = g-(i-1)
  DICHc  every head of original degree <= s satisfies D_i <= s-i+2
  KSUB   L = 0 forces e_B = C(tau,2)  (Theorem K, subsumed by LOW1)

Every claim is tested under the canonical sort AND randomised adversarial
tie-breaks.  Separately we histogram L over the *hard core without the reductio*
(connected, non-forest, diam 4, f = alpha+1), which is the regime a completed
proof must cover.
"""
import random
from itertools import combinations
from collections import Counter

import networkx as nx
from networkx.generators.atlas import graph_atlas_g


# ---------------------------------------------------------------- labelled HH
def hh(deg, rng=None):
    """Labelled Havel-Hakimi.  deg: dict label -> degree.
    Returns (heads, hvals, blocks) where heads[j] is the label deleted at step
    j+1, hvals[j] its value at deletion (= D_{j+1}), blocks[j] the set of labels
    decremented at that step."""
    cur = dict(deg)
    heads, hvals, blocks = [], [], []
    while cur and max(cur.values()) > 0:
        items = list(cur.items())
        if rng is not None:
            rng.shuffle(items)
        items.sort(key=lambda kv: -kv[1])
        h, D = items[0]
        del cur[h]
        rest = items[1:]
        blk = {lab for lab, _ in rest[:D]}
        for lab in blk:
            cur[lab] -= 1
        heads.append(h)
        hvals.append(D)
        blocks.append(blk)
    return heads, hvals, blocks


def residue_of(deg, rng=None):
    heads, _, _ = hh(deg, rng)
    return len(deg) - len(heads)


# ------------------------------------------------------------- graph routines
def max_ind_sets(G):
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    best, out = 0, []
    for r in range(n, 0, -1):
        if r < best:
            break
        for S in combinations(nodes, r):
            if all(not G.has_edge(u, v) for u, v in combinations(S, 2)):
                if r > best:
                    best, out = r, [set(S)]
                elif r == best:
                    out.append(set(S))
        if out:
            break
    return best, out


def forest_number(G):
    nodes = list(G.nodes())
    for r in range(len(nodes), 0, -1):
        for S in combinations(nodes, r):
            H = G.subgraph(S)
            if H.number_of_edges() == H.number_of_nodes() - nx.number_connected_components(H):
                return r
    return 0


# ------------------------------------------------------------------- checking
class Res:
    def __init__(self):
        self.n = 0
        self.red = 0
        self.fail = Counter()
        self.hit = Counter()
        self.wit = {}
        self.lhist = Counter()       # (tau, L) over reductio instances
        self.hc = Counter()          # (tau, L) over hard core WITHOUT reductio
        self.hcn = 0
        self.slack = {}
        self.slack2 = {}

    def bad(self, key, payload):
        self.fail[key] += 1
        self.wit.setdefault(key, payload)


def check(G, R, rng):
    n = G.number_of_nodes()
    if n < 2 or not nx.is_connected(G):
        return
    R.n += 1
    deg = dict(G.degree())
    m = G.number_of_edges()
    alpha, isets = max_ind_sets(G)
    tau = n - alpha
    s_list = [hh(deg)] + [hh(deg, rng) for _ in range(3)]

    hard = None                                   # hard core, reductio not required
    if nx.diameter(G) == 4 and m >= n:
        if forest_number(G) == alpha + 1:
            hard = True

    for A in isets:
        B = [v for v in G.nodes() if v not in A]
        eB = G.subgraph(B).number_of_edges()
        nu = tau * (tau - 1) // 2 - eB
        Blo = [b for b in B if deg[b] <= tau]
        Bhi = [b for b in B if deg[b] >= tau + 1]
        L = len(Blo)
        eBlo = G.subgraph(Blo).number_of_edges()
        mbar = len(Bhi) * (len(Bhi) - 1) // 2 - G.subgraph(Bhi).number_of_edges()
        nuBlo = L * (L - 1) // 2 - eBlo
        degA = {b: sum(1 for w in G[b] if w in A) for b in B}

        if hard:
            R.hc[(tau, L)] += 1
            R.hcn += 1

        for heads, hvals, blocks in s_list:
            s = len(heads)
            if n - s != alpha:                    # reductio hypothesis
                continue
            R.red += 1
            R.lhist[(tau, L)] += 1

            # --- DICH, on this trajectory
            Ihi, Ilo = [], []
            for i, (lab, D) in enumerate(zip(heads, hvals), start=1):
                g = deg[lab]
                if g >= s + 1:
                    Ihi.append(i)
                    h = g - D
                    if h != i - 1 or D != g - (i - 1):
                        R.bad('DICHb', (n, sorted(G.edges()), lab, i, g, D))
                else:
                    Ilo.append(i)
                    if D > s - i + 2:
                        R.bad('DICHc', (n, sorted(G.edges()), lab, i, g, D))

            # I_hi must be exactly B_hi (Lemma S + A-degrees <= tau)
            if {heads[i - 1] for i in Ihi} != set(Bhi):
                R.bad('KHI', (n, sorted(G.edges()), sorted(Bhi),
                              sorted(heads[i - 1] for i in Ihi)))

            # --- POS: position independence
            lhs = -sum(i - 1 for i in Ihi) + sum(tau - i + 2 for i in Ilo)
            if lhs != -tau * (tau - 1) // 2 + L * (tau + 1):
                R.bad('POS', (n, sorted(G.edges()), Ihi, Ilo, lhs))

            # --- the three equivalent forms of Theorem LOW
            if sum(deg[b] for b in Blo) + nu > L * (tau + 1):
                R.bad('LOW1', (n, sorted(G.edges()), tau, L, nu))
            if sum(degA[b] for b in Blo) + eBlo + mbar > L * (L + 3) // 2:
                R.bad('LOW2', (n, sorted(G.edges()), tau, L, mbar))
            if sum(degA[b] for b in Blo) + mbar > 2 * L + nuBlo:
                R.bad('LOW3', (n, sorted(G.edges()), tau, L, mbar))

            # --- Theorem K as the L = 0 case
            if L == 0:
                R.hit['L0'] += 1
                if eB != tau * (tau - 1) // 2:
                    R.bad('KSUB', (n, sorted(G.edges()), tau, eB))
            if L == 1:
                R.hit['L1'] += 1
                b0 = Blo[0]
                nb0 = tau - 1 - sum(1 for w in G[b0] if w in B)
                R.hit['L1_nu0' if nb0 == 0 else 'L1_nupos'] += 1
            slack = L * (tau + 1) - (sum(deg[b] for b in Blo) + nu)
            if slack == 0:
                R.hit['tight'] += 1
            R.slack[L] = min(R.slack.get(L, 10 ** 9), slack)
            R.slack2[(L, min(tau, 9))] = min(R.slack2.get((L, min(tau, 9)), 10 ** 9),
                                             slack)


def report(tag, R):
    print(f"[{tag}] graphs={R.n} reductio(residue=alpha) traj-checks={R.red} "
          f"fails={dict(R.fail)}")
    print(f"[{tag}] hits={dict(R.hit)}")
    if R.fail:
        for k, v in R.wit.items():
            print(f"   WITNESS {k}: {v}")


def main():
    rng = random.Random(20260818)
    R = Res()

    for G in graph_atlas_g():
        check(G, R, rng)
    report("A n<=7 exhaustive atlas", R)

    for n in range(8, 13):
        for _ in range(1200):
            p = rng.choice([0.30, 0.40, 0.50, 0.62, 0.75])
            G = nx.gnp_random_graph(n, p, seed=rng.randrange(1 << 30))
            check(G, R, rng)
    report("+B random n=8..12", R)

    # structured: Family I(tau,c) from draft 7.2 B, which sits in the hard core
    for tau in range(3, 8):
        for c in range(2, 9):
            G = nx.Graph()
            Bv = [('b', i) for i in range(tau)]
            G.add_nodes_from(Bv)
            for j in range(c):                    # c universal A-vertices
                for b in Bv:
                    G.add_edge(('u', j), b)
            G.add_edge(('l', 0), Bv[0])           # two private leaves
            G.add_edge(('l', 1), Bv[1])
            check(G, R, rng)
    report("+C Family I(tau,c)", R)

    print(f"[LHIST] (tau,L) over reductio instances: "
          f"{dict(sorted(R.lhist.items()))}")
    print(f"[HARDCORE] instances (connected, non-forest, diam 4, f=alpha+1, "
          f"reductio NOT imposed) = {R.hcn}")
    print(f"[HARDCORE] (tau,L) histogram: {dict(sorted(R.hc.items()))}")
    print(f"[HARDCORE] L histogram: "
          f"{dict(sorted(Counter({k[1]: 0 for k in R.hc}).items()))}")
    agg = Counter()
    for (t, l), c in R.hc.items():
        agg[l] += c
    print(f"[HARDCORE] L histogram (aggregated over tau): {dict(sorted(agg.items()))}")
    print(f"[SLACK] min slack of LOW1 per L: {dict(sorted(R.slack.items()))}")
    print(f"[SLACK] min slack of LOW1 per (L, min(tau,9)): {dict(sorted(R.slack2.items()))}")


if __name__ == '__main__':
    main()
