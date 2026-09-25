#!/usr/bin/env python3
"""
WOWII-61 round 3 (owner-w61): numerical stress test of the BLOCK-OCCUPANCY
route to a tau-uniform head-decay bound.  Everything below assumes the reductio
hypothesis  residue(G) = alpha(G), i.e. labelled Havel-Hakimi on d(G) takes
exactly s = tau = n - alpha steps.

Notation (matches notes/proofs/wowii61_draft.md 7.2 B):
  A   a maximum independent set, B = V \\ A, tau = |B|, e_B = |E(G[B])|
  K   the tau head entries, in removal order; survivors = the other alpha entries
  D_i value of the i-th head at removal;  g_i its original degree
  hs  := sum_i (g_i - D_i) = sum_{v in K} deg(v) - m   (decrements absorbed by heads)
  beta_j := #(later heads inside the decremented block of step j)

Claims under test:
  BO   sum_j beta_j = hs                                        (identity)
  ZERO if beta_j = 0 then every head removed after step j has value <= tau-j+1
       at the START of step j
  DEC  D_i <= tau - i + 2 + hs   for every i >= hs + 2
  KB   if every b in B has deg(b) >= tau+1 then K = B (hence hs = e_B)
  NP   THEOREM N' : if every b in B has deg(b) >= tau+1, e_B <= tau-2, and
       e_B * Delta < tau(tau-1)/2 + e_B(e_B+1)/2  then residue <= alpha - 1
  CNT  the counting bound
       m <= min(tau, hs+1)*Delta + sum_{i=hs+2}^{tau} (tau-i+2+hs)
       (the sum is empty when hs+2 > tau)

All labelled claims are tested under BOTH the canonical descending sort and
RANDOM adversarial tie-breaking among equal values (the multiset trajectory,
hence residue, is tie-independent; the labelling is not).

Run:  python3 w61_blockocc.py            (exhaustive n<=7, n=8 cover, random 9..12)
"""
import random

# ---------------------------------------------------------------- labelled HH
def hh_labelled(degs, rng=None):
    """Labelled Havel-Hakimi, literal transcription of residueAux.
    Returns (heads, survivors, snapshots, beta) where
      heads = [(label, g, D, h)] in removal order,
      snapshots[j] = list of (label, value) at the START of step j+1,
      beta[j] = #(entries decremented at step j+1 that are removed as a
                  head at some LATER step)."""
    n = len(degs)
    ent = [[d, i] for i, d in enumerate(degs)]
    g0 = {i: d for i, d in enumerate(degs)}
    dec = {i: 0 for i in range(n)}
    heads, snapshots, blocks = [], [], []
    while True:
        if rng is not None:
            rng.shuffle(ent)                    # adversarial tie-breaking
        ent.sort(key=lambda t: -t[0])
        if not ent:
            break
        if ent[0][0] == 0:
            break
        snapshots.append([(lab, v) for v, lab in ent])
        d, hl = ent[0][0], ent[0][1]
        heads.append([hl, g0[hl], d, dec[hl]])
        rest = ent[1:]
        blk = []
        for k in range(min(d, len(rest))):
            rest[k][0] = max(rest[k][0] - 1, 0)
            dec[rest[k][1]] += 1
            blk.append(rest[k][1])
        blocks.append(blk)
        ent = rest
    survivors = [lab for _, lab in ent]
    order = [h[0] for h in heads]
    pos = {lab: i for i, lab in enumerate(order)}
    beta = []
    for j, blk in enumerate(blocks):
        beta.append(sum(1 for lab in blk if lab in pos and pos[lab] > j))
    return heads, survivors, snapshots, beta


# ---------------------------------------------------------------- graph tools
def adj_masks(n, edges):
    a = [0] * n
    for (u, v) in edges:
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def is_connected(a, n):
    seen, stack = 1, [0]
    while stack:
        v = stack.pop()
        m = a[v] & ~seen
        while m:
            b = m & -m
            m ^= b
            seen |= b
            stack.append(b.bit_length() - 1)
    return seen == (1 << n) - 1


def max_indep_sets(a, n):
    best, sets = 0, []
    for S in range(1 << n):
        ok, m = True, S
        while m:
            b = m & -m
            m ^= b
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


# ---------------------------------------------------------------- the tests
class Res:
    def __init__(self):
        self.tested = 0
        self.resalpha = 0
        self.fail = {k: 0 for k in ("BO", "ZERO", "DEC", "KB", "NP", "CNT")}
        self.hit = {k: 0 for k in ("KB", "NP", "CNT", "NP_new", "N_old")}
        self.wit = {}

    def bad(self, key, payload):
        self.fail[key] += 1
        self.wit.setdefault(key, payload)


def check_traj(n, edges, degs, tau, al, m, isets, R, rng):
    heads, surv, snaps, beta = hh_labelled(degs, rng)
    s = len(heads)
    if n - s != al:
        return
    assert s == tau
    Delta = max(degs)
    hs = sum(g - D for (_, g, D, _) in heads)
    # BO
    if sum(beta) != hs:
        R.bad("BO", (n, edges, degs, tau, hs, beta))
    # also the closed form hs = sum_{v in K} deg(v) - m
    if hs != sum(degs[h[0]] for h in heads) - m:
        R.bad("BO", ("closedform", n, edges, degs, tau, hs))
    # ZERO
    for j in range(1, tau + 1):
        if beta[j - 1] != 0:
            continue
        val = dict(snaps[j - 1])
        for i in range(j + 1, tau + 1):
            lab = heads[i - 1][0]
            if val.get(lab, 0) > tau - j + 1:
                R.bad("ZERO", (n, edges, degs, tau, j, i, val.get(lab)))
    # DEC
    for i in range(1, tau + 1):
        if i >= hs + 2 and heads[i - 1][2] > tau - i + 2 + hs:
            R.bad("DEC", (n, edges, degs, tau, hs, i, heads[i - 1][2]))
    # CNT
    R.hit["CNT"] += 1
    bound = min(tau, hs + 1) * Delta + sum(tau - i + 2 + hs
                                           for i in range(hs + 2, tau + 1))
    if m > bound:
        R.bad("CNT", (n, edges, degs, tau, hs, m, bound))
    # KB / NP (per maximum independent set)
    headset = {h[0] for h in heads}
    for S in isets:
        B = [v for v in range(n) if not (S >> v & 1)]
        eB = sum(1 for u, v in edges if not (S >> u & 1) and not (S >> v & 1))
        if min(degs[b] for b in B) >= tau + 1:
            R.hit["KB"] += 1
            if headset != set(B):
                R.bad("KB", (n, edges, degs, tau, sorted(B), sorted(headset)))
            if hs != eB:
                R.bad("KB", ("hs!=eB", n, edges, degs, tau, hs, eB))


def test_graph(n, edges, R, rng):
    a = adj_masks(n, edges)
    if not is_connected(a, n):
        return
    degs = [bin(x).count('1') for x in a]
    m = len(edges)
    al, isets = max_indep_sets(a, n)
    tau = n - al
    R.tested += 1
    Delta = max(degs)

    # --- THEOREM N' tested on EVERY graph (hypothesis => residue <= alpha-1)
    for S in isets:
        B = [v for v in range(n) if not (S >> v & 1)]
        eB = sum(1 for u, v in edges if not (S >> u & 1) and not (S >> v & 1))
        if min(degs[b] for b in B) >= tau + 1 and eB <= tau - 2 and \
           eB * Delta < tau * (tau - 1) // 2 + eB * (eB + 1) // 2:
            R.hit["NP"] += 1
            if min(degs[b] for b in B) < 2 * eB + 3:
                R.hit["NP_new"] += 1        # covered by N' but NOT by Theorem N
            else:
                R.hit["N_old"] += 1
            hh, _, _, _ = hh_labelled(degs)
            if n - len(hh) >= al:                   # residue >= alpha : N' FALSE
                R.bad("NP", (n, edges, degs, tau, eB, Delta,
                             sorted(degs[b] for b in B)))

    hh, _, _, _ = hh_labelled(degs)
    if n - len(hh) != al:
        return
    R.resalpha += 1
    check_traj(n, edges, degs, tau, al, m, isets, R, None)      # canonical
    for _ in range(3):                                          # adversarial ties
        check_traj(n, edges, degs, tau, al, m, isets, R, rng)


def report(tag, R):
    print(f"[{tag}] tested={R.tested} residue=alpha:{R.resalpha} "
          f"fails={R.fail} hits={R.hit}")


def main():
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g
    rng = random.Random(20260818)
    R = Res()
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
        for mask in range(1, 1 << 7):
            e2 = list(edges) + [(7, v) for v in range(7) if mask >> v & 1]
            test_graph(8, e2, R, rng)
    report("+B n=8 exhaustive cover", R)

    for n in range(9, 13):
        for _ in range(2500):
            p = rng.choice([0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7])
            edges = [(u, v) for u in range(n) for v in range(u + 1, n)
                     if rng.random() < p]
            test_graph(n, edges, R, rng)
    report("+C random n=9..12", R)

    fam = []
    for k in range(2, 7):
        fam.append((k, [(i, j) for i in range(k) for j in range(i + 1, k)]))
    for a_ in range(1, 6):
        for b_ in range(1, 6):
            fam.append((a_ + b_, [(i, a_ + j) for i in range(a_)
                                  for j in range(b_)]))
    for c in range(2, 6):
        for lv in range(1, 5):
            e = [(i, j) for i in range(c) for j in range(i + 1, c)]
            e += [(c + t, t % c) for t in range(lv)]
            fam.append((c + lv, e))
    # Family I(tau,c) from 7.2 C : B independent, c universal A-vertices, 2 leaves
    for tau in range(3, 8):
        for c in range(2, 9):
            B = list(range(tau))
            e = []
            nxt = tau
            for _ in range(c):
                e += [(nxt, b) for b in B]
                nxt += 1
            e += [(nxt, 0), (nxt + 1, 1)]
            fam.append((nxt + 2, e))
    for n, e in fam:
        test_graph(n, e, R, rng)
    report("+D structured (incl. Family I)", R)

    for k, v in R.wit.items():
        print("  WITNESS", k, v)


if __name__ == "__main__":
    main()
