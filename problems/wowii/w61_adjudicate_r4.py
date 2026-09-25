"""owner-w61 round 4 — adjudication of the S3 round-A (Qwen) findings.

Two reported GAPs, reproduced from scratch (owner's own HH implementation).

G1 (T3-REPAIRED, joint T-J2, branch (ii-b) of draft §7.3 5bis).  Attacked line:
   "u 在第 2 步未被减 -- 否则 u 的 L^1 值为 D_3+1 = Z >= 4, 而 L^1\\{H_2} 中值 >= 4
    的项不存在 (A-项 <= 3, 唯一的 B-项 w 值为 Z-1 < Z)."
   Reviewer: the parenthetical "no entry of value >= 4 exists" is FALSE once
   Z >= 5, because w itself has value Z-1 >= 4.
   Reviewer's repair: the exclusion actually needed is "no entry of value = Z",
   which follows from the very same two facts.
   TEST A1: exhibit an L^1 with two entries >= 4 (reviewer's witness
            [5,5,5,3,3,3,2]) -- confirms the stated justification is false.
   TEST A2: over all tau=3 k=3 configurations in a bounded box, check the
            REPAIRED claim: no entry of L^1\\{H_2} has value exactly Z.

G2 (K-CHAIN, joints K-J1/K-J5).  Lemma Z+ (draft §7.5) is stated for general s
   ("no reductio needed") but its proof cites Lemma F3, which draft §7.2 B states
   only under the standing hypothesis residue=alpha (s=tau), and with threshold
   tau-j+1 rather than s-j+1.
   TEST B1: K_{2,3} has alpha=3, tau=2 but s=3, so s != tau -- F3 as stated is
            unavailable there.
   TEST B2: the general-s survivor decay ("at the start of step j every survivor
            has value <= s-j+1") holds with no reductio hypothesis at all.
   TEST B3: Lemma Z+ itself holds on graphs with s != tau (i.e. the statement is
            true in the generality claimed; only its proof cited the wrong lemma).
"""
import random
from itertools import combinations
from collections import Counter

import networkx as nx
from networkx.generators.atlas import graph_atlas_g


def hh_seq(seq, rng=None):
    """Unlabelled HH on a degree sequence; returns (heads, lists_before_each_step)."""
    cur = list(seq)
    heads, snaps = [], []
    while cur and max(cur) > 0:
        if rng is not None:
            rng.shuffle(cur)
        cur.sort(reverse=True)
        snaps.append(list(cur))
        D = cur[0]
        rest = cur[1:]
        for i in range(min(D, len(rest))):
            rest[i] -= 1
        heads.append(D)
        cur = rest
    return heads, snaps


def hh_lab(deg, rng=None):
    cur = dict(deg)
    heads, hvals, blocks, snaps = [], [], [], []
    while cur and max(cur.values()) > 0:
        items = list(cur.items())
        if rng is not None:
            rng.shuffle(items)
        items.sort(key=lambda kv: -kv[1])
        snaps.append(dict(cur))
        h, D = items[0]
        del cur[h]
        blk = {lab for lab, _ in items[1:][:D]}
        for lab in blk:
            cur[lab] -= 1
        heads.append(h)
        hvals.append(D)
        blocks.append(blk)
    return heads, hvals, blocks, snaps


def max_ind(G):
    nodes = list(G.nodes())
    for r in range(len(nodes), 0, -1):
        for S in combinations(nodes, r):
            if all(not G.has_edge(u, v) for u, v in combinations(S, 2)):
                return r
    return 0


# ---------------------------------------------------------------- TEST A1
def testA1():
    seq = [5, 5, 5, 3, 3, 3, 2]
    heads, snaps = hh_seq(seq)
    L1 = snaps[1] if len(snaps) > 1 else []
    ge4 = [x for x in L1 if x >= 4]
    print(f"[A1] reviewer witness seq={seq} graphical={nx.is_graphical(seq)}")
    print(f"[A1] L^1 (list before step 2) = {L1}; entries >= 4: {ge4}")
    print(f"[A1] draft's parenthetical 'no entry >= 4 in L^1' is "
          f"{'FALSE (gap CONFIRMED)' if len(ge4) >= 2 else 'not contradicted here'}"
          f"  [H_2 is one of them, so L^1 minus H_2 still has {max(0,len(ge4)-1)}]")
    seq2 = [5, 5, 5, 3, 3, 3, 3, 3]                       # K_{3,5}
    h2, s2 = hh_seq(seq2)
    print(f"[A1] second witness K_(3,5) seq={seq2} L^1={s2[1] if len(s2)>1 else []}")


# ---------------------------------------------------------------- TEST A2
def testA2():
    """tau=3, k=3 box scan: is 'no entry of L^1 minus H_2 equals Z' always true?"""
    rng = random.Random(11)
    bad = 0
    tested = 0
    for _ in range(200000):
        X = rng.randint(4, 12)
        Y = rng.randint(4, X)
        Z = rng.randint(4, Y)
        p = rng.randint(0, 6)            # number of degree-3 A-entries
        q = rng.randint(0, 6)
        r = rng.randint(0, 6)
        seq = sorted([X, Y, Z] + [3] * p + [2] * q + [1] * r, reverse=True)
        if not nx.is_graphical(seq):
            continue
        heads, snaps = hh_seq(seq)
        if len(snaps) < 2:
            continue
        L1 = snaps[1]
        tested += 1
        # L^1 minus the step-2 head
        rest = L1[1:]
        if any(v == Z for v in rest):
            # the repaired exclusion would fail
            bad += 1
            if bad == 1:
                print(f"[A2] WITNESS repaired-claim failure: seq={seq} L1={L1} Z={Z}")
    print(f"[A2] tau=3 k=3-shaped degree sequences tested={tested}; "
          f"repaired claim 'no entry of L^1 minus H_2 equals Z' violations={bad}")


# ---------------------------------------------------------------- TEST B1
def testB1():
    G = nx.complete_bipartite_graph(2, 3)
    deg = dict(G.degree())
    alpha = max_ind(G)
    heads, hvals, blocks, snaps = hh_lab(deg)
    n = G.number_of_nodes()
    s = len(heads)
    print(f"[B1] K_(2,3): n={n} degrees={sorted(deg.values(), reverse=True)} "
          f"alpha={alpha} tau={n-alpha} s={s} residue={n-s}")
    print(f"[B1] s == tau ? {s == n - alpha}  -> Lemma F3 as stated "
          f"({'available' if s == n - alpha else 'NOT available'}); gap "
          f"{'refuted' if s == n - alpha else 'CONFIRMED'}")


# ------------------------------------------------------------ TESTS B2 / B3
def testB23():
    rng = random.Random(99)
    R = Counter()
    corpus = []
    for G in graph_atlas_g():
        if G.number_of_nodes() >= 2 and nx.is_connected(G):
            corpus.append(G)
    for n in range(8, 13):
        for _ in range(900):
            G = nx.gnp_random_graph(n, rng.uniform(0.2, 0.8),
                                    seed=rng.randrange(1 << 30))
            if nx.is_connected(G):
                corpus.append(G)
    for G in corpus:
        deg = dict(G.degree())
        n = G.number_of_nodes()
        alpha = max_ind(G)
        for heads, hvals, blocks, snaps in [hh_lab(deg)] + [hh_lab(deg, rng)
                                                            for _ in range(3)]:
            s = len(heads)
            R['traj'] += 1
            if s != n - alpha:
                R['traj_no_reductio'] += 1
            survivors = set(deg) - set(heads)
            # B2: general-s survivor decay
            for j in range(1, s + 1):
                for v in survivors:
                    if snaps[j - 1].get(v, 0) > s - j + 1:
                        R['B2_fail'] += 1
            # B3: Lemma Z+ in the generality claimed
            for j in range(1, s + 1):
                for i in range(j + 1, s + 1):
                    lab = heads[i - 1]
                    val = snaps[j - 1].get(lab, 0)
                    if val > s - j + 1 and lab not in blocks[j - 1]:
                        R['B3_fail'] += 1
                        if R['B3_fail'] == 1:
                            R['B3_wit'] = (n, sorted(G.edges()), j, i, val, s)
    print(f"[B2/B3] trajectories={R['traj']} of which s != tau: "
          f"{R['traj_no_reductio']}")
    print(f"[B2] general-s survivor decay (value <= s-j+1) failures = {R['B2_fail']}")
    print(f"[B3] Lemma Z+ failures on the same corpus            = {R['B3_fail']}")
    if 'B3_wit' in R:
        print(f"     WITNESS {R['B3_wit']}")


if __name__ == '__main__':
    testA1()
    testA2()
    testB1()
    testB23()
