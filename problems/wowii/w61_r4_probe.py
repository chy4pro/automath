#!/usr/bin/env python3
"""
WOWII-61 round 4 probe (math-helper session, 2026-08-18): the K != B regime.

New claims under test (all under canonical AND randomised adversarial
tie-breaking; s = number of labelled-HH steps; NONE of the per-trajectory
claims assume the reductio hypothesis, they are stated with s):

  DICH (head dichotomy).  For every head at position i (1-based) with
        original degree g:
        - if g >= s+1 ("high"): it lies in EVERY earlier block, so
          h_i = i-1  and  D_i = g - (i-1)   (exact value);
        - if g <= s   ("low"):  D_i <= s - i + 2.
  ZPLUS (excess localisation).  At the start of step j, every LATER head
        whose current value exceeds s - j + 1 lies in block_j; hence
        X_j := #(excess later heads at step j) <= beta_j.
  F3S / P1 sanity: survivors' values <= s-j+1 at start of step j;
        head_i not in block_j (j<i)  ==>  D_i <= s-j+1.

  Under the reductio residue(G) = alpha(G)  (s = tau), per graph:
  CNT2  m <= Sum_{v: deg(v)>=tau+1} deg(v) + (tau-k)(tau+1) - tau(tau-1)/2
        where k = #{v : deg(v) >= tau+1}.        (pure degree-sequence)
  and per maximum independent set A (B = V-A, B_hi = {b: deg(b)>=tau+1},
  k' = |B_hi| (must equal k), B_lo = B - B_hi, l = |B_lo|):
  CLIQ  if l = 0 then e_B = tau(tau-1)/2  (B is a clique);
  LOW   Sum_{b in B_lo} deg_A(b) + e(B_lo) + (C(k,2) - e(B_hi)) <= l(l+3)/2.

  HS (empirical, task 1): per (A, trajectory) with t = |A cap K| >= 1,
     the distribution of hs - e_B versus t, and extreme witnesses.

Corpus: exhaustive n<=7 atlas; exhaustive n=8 cover; random n=9..12;
clique-with-leaves families; cycles and cycle powers.
"""
import random
import sys
from collections import Counter

WOWII = "$HOME/workspace/claudecode/automath/problems/wowii"
sys.path.insert(0, WOWII)
from w61_cstar import adj_masks, is_connected, diameter, largest_forest  # noqa: E402


# ---------------------------------------------------------------- labelled HH
def hh_full(degs, rng=None):
    """Labelled HH.  Returns (heads, survivors, snaps, beta, blocks):
    heads = [(label, g, D, h)] in removal order; snaps[j] = [(label, value)]
    at the START of step j+1 (sorted desc); blocks[j] = labels decremented."""
    n = len(degs)
    ent = [[d, i] for i, d in enumerate(degs)]
    dec = [0] * n
    heads, snaps, blocks = [], [], []
    while True:
        if rng is not None:
            rng.shuffle(ent)                      # adversarial tie-breaking
        ent.sort(key=lambda t: -t[0])
        if not ent or ent[0][0] == 0:
            break
        snaps.append([(lab, v) for v, lab in ent])
        d, hl = ent[0]
        heads.append((hl, degs[hl], d, dec[hl]))
        rest = ent[1:]
        blk = []
        for kk in range(min(d, len(rest))):
            rest[kk][0] = max(rest[kk][0] - 1, 0)
            dec[rest[kk][1]] += 1
            blk.append(rest[kk][1])
        blocks.append(blk)
        ent = rest
    survivors = [lab for _, lab in ent]
    pos = {h[0]: i for i, h in enumerate(heads)}          # 0-based
    beta = [sum(1 for lab in blk if lab in pos and pos[lab] > j)
            for j, blk in enumerate(blocks)]
    return heads, survivors, snaps, beta, blocks


class F:
    def __init__(self):
        self.graphs = 0
        self.reductio = 0
        self.fail = Counter()
        self.wit = {}
        # HS stats
        self.hs_cnt = Counter()          # (tau, t, hs - e_B) -> count  (t>=1)
        self.hs_top = []                 # extreme (hs-e_B-t) witnesses
        self.kb_exact = 0                # t=0 cases (K=B), hs==e_B checked
        # hard-core stats
        self.hc = Counter()              # tau -> count of residual hard-core (graph,A)
        self.hc_lowhist = Counter()      # (tau, l) -> count
        self.hc_allhigh = 0              # residual hard core with min_B deg >= tau+1
        self.hc_l1 = []                  # small sample of l=1 witnesses
        self.cnt2_slack = Counter()      # slack of CNT2 under reductio

    def bad(self, key, payload):
        self.fail[key] += 1
        if key not in self.wit:
            self.wit[key] = payload


def check_traj(n, degs, heads, survivors, snaps, beta, blocks, R):
    s = len(heads)
    # F3S: survivors <= s-j+1 at start of step j
    for j in range(1, s + 1):
        val = dict(snaps[j - 1])
        for lab in survivors:
            if val.get(lab, 0) > s - j + 1:
                R.bad('F3S', (n, degs, j, lab, val[lab]))
        # ZPLUS: excess later heads must lie in block_j
        blkset = set(blocks[j - 1])
        X = 0
        for i in range(j + 1, s + 1):
            li = heads[i - 1][0]
            if val.get(li, 0) > s - j + 1:
                X += 1
                if li not in blkset:
                    R.bad('ZPLUS', (n, degs, j, i, val.get(li)))
        if X > beta[j - 1]:
            R.bad('XLEB', (n, degs, j, X, beta[j - 1]))
    # DICH + P1
    for i in range(1, s + 1):
        lab, g, D, h = heads[i - 1]
        if g >= s + 1:
            if h != i - 1 or D != g - (i - 1):
                R.bad('DICH_HI', (n, degs, i, g, D, h, s))
        else:
            if D > s - i + 2:
                R.bad('DICH_LO', (n, degs, i, g, D, s))
        for j in range(1, i):
            if lab not in blocks[j - 1] and D > s - j + 1:
                R.bad('P1', (n, degs, i, j, D, s))


def check_reductio(n, edges, degs, m, al, isets, trajs, a, R):
    tau = n - al
    k_glob = sum(1 for d in degs if d >= tau + 1)
    hi_sum = sum(d for d in degs if d >= tau + 1)
    bound = hi_sum + (tau - k_glob) * (tau + 1) - tau * (tau - 1) // 2
    R.cnt2_slack[bound - m] += 1
    if m > bound:
        R.bad('CNT2', (n, edges, degs, tau, k_glob, m, bound))

    # hard-core detection (residual hard core: + residue = alpha, given)
    hard = False
    if diameter(a, n) == 4:
        f_val = largest_forest(a, n)
        if f_val == al + 1 and f_val < n:
            hard = True

    for S in isets[:24]:
        B = [v for v in range(n) if not (S >> v & 1)]
        Bset = set(B)
        eB = sum(1 for u, v in edges if u in Bset and v in Bset)
        Bhi = [b for b in B if degs[b] >= tau + 1]
        Blo = [b for b in B if degs[b] <= tau]
        kk, ll = len(Bhi), len(Blo)
        if kk != k_glob:
            R.bad('KSET', (n, edges, degs, tau, kk, k_glob))   # hi outside B?!
        eBhi = sum(1 for u, v in edges
                   if u in Bset and v in Bset and degs[u] > tau and degs[v] > tau)
        eBlo = sum(1 for u, v in edges
                   if u in Bset and v in Bset and degs[u] <= tau and degs[v] <= tau)
        degA = {b: sum(1 for u in range(n) if (S >> u & 1) and (a[u] >> b & 1))
                for b in B}
        # CLIQ
        if ll == 0 and eB != tau * (tau - 1) // 2:
            R.bad('CLIQ', (n, edges, degs, tau, eB))
        # LOW
        lhs = sum(degA[b] for b in Blo) + eBlo + (kk * (kk - 1) // 2 - eBhi)
        if lhs > ll * (ll + 3) // 2:
            R.bad('LOW', (n, edges, degs, tau, kk, ll, lhs))
        if hard:
            R.hc[tau] += 1
            R.hc_lowhist[(tau, ll)] += 1
            if ll == 0:
                R.hc_allhigh += 1
            if ll == 1 and len(R.hc_l1) < 6:
                b = Blo[0]
                nonnb = [c for c in B if c != b and not (a[b] >> c & 1)]
                R.hc_l1.append((n, edges, tau, b, degs[b], degA[b],
                                len(nonnb), kk * (kk - 1) // 2 - eBhi))
        # HS stats per trajectory
        for (heads, survivors, snaps, beta, blocks) in trajs:
            K = [h[0] for h in heads]
            Kset = set(K)
            hs = sum(g - D for (_, g, D, _) in heads)
            AK = [v for v in K if S >> v & 1]
            BnotK = [b for b in B if b not in Kset]
            t = len(AK)
            assert len(BnotK) == t
            # identity check
            ident = eB + sum(degs[x] for x in AK) - sum(degs[b] for b in BnotK)
            if ident != hs:
                R.bad('IDENT', (n, edges, degs, hs, ident))
            if t == 0:
                R.kb_exact += 1
                if hs != eB:
                    R.bad('HS0', (n, edges, degs, hs, eB))
            else:
                R.hs_cnt[(tau, t, hs - eB)] += 1
                key = hs - eB - t
                R.hs_top.append((key, n, tuple(edges), tau, t, eB, hs,
                                 tuple(sorted(degs[x] for x in AK)),
                                 tuple(sorted(degs[b] for b in BnotK))))
                R.hs_top.sort(key=lambda z: -z[0])
                del R.hs_top[8:]


def alpha_sets(a, n):
    best, sets = 0, []
    for S in range(1 << n):
        ok, mm = True, S
        while mm:
            b = mm & -mm
            mm ^= b
            if a[b.bit_length() - 1] & S:
                ok = False
                break
        if not ok:
            continue
        c = bin(S).count('1')
        if c > best:
            best, sets = c, [S]
        elif c == best:
            sets.append(S)
    return best, sets


def test_graph(n, edges, R, rng):
    a = adj_masks(n, edges)
    if not is_connected(a, n):
        return
    degs = [bin(x).count('1') for x in a]
    m = len(edges)
    R.graphs += 1
    trajs = [hh_full(degs)] + [hh_full(degs, rng) for _ in range(3)]
    for tr in trajs:
        check_traj(n, degs, *tr, R)
    s = len(trajs[0][0])
    al, isets = alpha_sets(a, n)
    if n - s != al:
        return
    R.reductio += 1
    check_reductio(n, edges, degs, m, al, isets, trajs, a, R)


def report(tag, R):
    print(f"[{tag}] graphs={R.graphs} reductio(residue=alpha)={R.reductio} "
          f"fails={dict(R.fail) or 0}")


def main():
    # default = quick (~15 s); `python3 w61_r4_probe.py full` reproduces the
    # archived w61_r4_probe.out (exhaustive n=8 cover + 1000 random/n, ~165 s)
    full = len(sys.argv) > 1 and sys.argv[1] == "full"
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g
    rng = random.Random(20260818)
    R = F()
    small = []
    for G in graph_atlas_g():
        if G.number_of_nodes() < 2 or not nx.is_connected(G):
            continue
        small.append((G.number_of_nodes(), [(u, v) for u, v in G.edges()]))
    for n, e in small:
        test_graph(n, e, R, rng)
    report("A n<=7 exhaustive", R)

    for n, edges in small:
        if n != 7:
            continue
        step = 1 if full else 11
        for mask in range(1, 1 << 7, step):
            e2 = list(edges) + [(7, v) for v in range(7) if mask >> v & 1]
            test_graph(8, e2, R, rng)
    report("+B n=8 cover" + ("" if full else " (1/11 sample)"), R)

    for n in range(9, 13):
        for _ in range(1000 if full else 150):
            p = rng.choice([0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7])
            edges = [(u, v) for u in range(n) for v in range(u + 1, n)
                     if rng.random() < p]
            test_graph(n, edges, R, rng)
    report("+C random n=9..12", R)

    fam = []
    # clique B = K_tau, p private leaves per clique vertex (K=B, high degrees)
    for tau in range(2, 7):
        for p in range(1, 5):
            e = [(i, j) for i in range(tau) for j in range(i + 1, tau)]
            nxt = tau
            for b in range(tau):
                for _ in range(p):
                    e.append((b, nxt))
                    nxt += 1
            fam.append((nxt, e))
    # cycles and cycle powers (pw < nn/2 keeps the graph simple, no loops);
    # n>=15 cycles cost ~2 s each in alpha_sets, so quick mode stops at 14
    for nn in range(3, 19 if full else 15):
        for pw in (1, 2, 3):
            if 2 * pw >= nn:
                continue
            e = sorted({(min(i, (i + d) % nn), max(i, (i + d) % nn))
                        for i in range(nn) for d in range(1, pw + 1)})
            fam.append((nn, e))
    # near-cliques on B with pendant trees (stress K != B)
    for tau in range(3, 7):
        for drop in range(1, 3):
            e = [(i, j) for i in range(tau) for j in range(i + 1, tau)]
            e = e[drop:]
            nxt = tau
            for b in range(tau):
                for _ in range(2):
                    e.append((b, nxt))
                    nxt += 1
            fam.append((nxt, e))
    for n, e in fam:
        test_graph(n, e, R, rng)
    report("+D structured", R)

    print(f"[KB] t=0 trajectories checked: {R.kb_exact} (hs==e_B enforced)")
    print(f"[CNT2] slack histogram (bound - m), reductio graphs: "
          f"{dict(sorted(R.cnt2_slack.items()))}")
    # HS empirical summary: per (tau, t), max hs-e_B
    per_tt = {}
    for (tau, t, d), c in R.hs_cnt.items():
        cur = per_tt.setdefault((tau, t), [10**9, -10**9, 0])
        cur[0] = min(cur[0], d)
        cur[1] = max(cur[1], d)
        cur[2] += c
    print("[HS] per (tau, t=|A cap K|>=1): (min, max of hs - e_B, #cases):")
    for (tau, t) in sorted(per_tt):
        v = per_tt[(tau, t)]
        print(f"     tau={tau} t={t}: min={v[0]} max={v[1]} n={v[2]}")
    print("[HS] top (hs - e_B - t) witnesses:")
    for w in R.hs_top[:5]:
        print("     ", w)
    print(f"[HC] residual hard core (reductio & diam=4 & f=alpha+1 & non-forest), "
          f"per tau (graph,A)-pairs: {dict(sorted(R.hc.items()))}")
    print(f"[HC] (tau, l=|B_lo|) histogram: {dict(sorted(R.hc_lowhist.items()))}")
    print(f"[HC] residual hard-core cases with ALL B-degrees >= tau+1 (l=0): "
          f"{R.hc_allhigh}   (CNT2+CLIQ predict 0 unless B is a clique)")
    print("[HC] l=1 witnesses (n, edges, tau, b, deg b, deg_A b, #nonnbrs of b in B,"
          " missing hi-edges):")
    for w in R.hc_l1:
        print("     ", w)
    for kkey, v in R.wit.items():
        print("  WITNESS", kkey, v)


if __name__ == "__main__":
    main()
