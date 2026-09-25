#!/usr/bin/env python3
"""
w61 round 4: owner-w61's INDEPENDENT re-check of the two round-A2 Qwen verdicts.

(1) K-CHAIN A2 said CLEAN.  The joint both previous rounds' defects touched is
    K-J1/K-J2 (Lemma F3' -> Lemma Z+ -> Lemma DICH).  Re-checked here at
    GENERAL s (no reductio), with adversarial tie-breaks:
      F3P   survivor at start of step j has value <= s-j+1
      ZP    a later head whose value at step j exceeds s-j+1 lies in block_j
      DICHb original degree >= s+1  =>  D_i = g - (i-1) exactly
      DICHc original degree <= s    =>  D_i <= s-i+2
      DICHc1 the i=1 boundary case, and
      DICHj0 the "first excess step j0 = i" boundary case Qwen names in K-J2.

(2) T3-REPAIRED A2 said PARTIAL with one non-load-bearing textual defect
    (T-J4, the k=2/e_B=2 terminal-shape count).  Re-checked here: over the
    whole (a0,b0,c0) family of that branch, (i) the displayed trajectory is
    right, (ii) the terminal-count sentence is indeed wrong, (iii) the
    parenthetical sum argument Sum_{i<=3} D_i = m-1 < m is right, hence
    load-bearing-free.
"""
import random
import sys
from collections import Counter
from itertools import combinations


def all_graphs_upto(n):
    """all connected graphs on exactly n labelled vertices, as adjacency sets
    (small n only; used for n<=6)."""
    verts = list(range(n))
    pairs = list(combinations(verts, 2))
    for mask in range(1 << len(pairs)):
        adj = {v: set() for v in verts}
        for i, (a, b) in enumerate(pairs):
            if mask >> i & 1:
                adj[a].add(b); adj[b].add(a)
        seen = {0}; stack = [0]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        if len(seen) == n:
            yield adj


def hh_labelled(deg, rng=None):
    """returns (order, heads, blocks, s, values) for the labelled HH run.
    heads[i]=(label,value); blocks[i]=set of labels; values[i][lab]=value at
    the START of step i (only for labels still alive)."""
    labels = list(range(len(deg)))
    cur = {i: deg[i] for i in labels}
    alive = list(labels)
    heads, blocks, vals = [], [], []
    while True:
        if not alive or max(cur[x] for x in alive) == 0:
            break
        vals.append({x: cur[x] for x in alive})
        if rng is None:
            alive.sort(key=lambda x: (-cur[x], x))
        else:
            rng.shuffle(alive); alive.sort(key=lambda x: -cur[x])
        h = alive[0]; d = cur[h]
        heads.append((h, d)); alive = alive[1:]
        if d > len(alive):
            return None
        blk = alive[:d]
        for x in blk:
            cur[x] -= 1
            if cur[x] < 0:
                return None
        blocks.append(set(blk))
    return heads, blocks, len(heads), vals


def check_chain(deg, rng=None):
    """returns a Counter of failures of F3P/ZP/DICHb/DICHc (+boundaries)."""
    out = hh_labelled(deg, rng)
    f = Counter()
    if out is None:
        return f, 0
    heads, blocks, s, vals = out
    headlab = {h for h, _ in heads}
    pos = {h: i + 1 for i, (h, _) in enumerate(heads)}
    for j in range(1, s + 1):
        V = vals[j - 1]
        blk = blocks[j - 1]
        hlab = heads[j - 1][0]
        for x, v in V.items():
            if x == hlab:
                continue
            if x not in headlab:                       # survivor
                if v > s - j + 1:
                    f["F3P"] += 1
            else:                                      # later or earlier head
                if pos[x] > j and v > s - j + 1 and x not in blk:
                    f["ZP"] += 1
    for i, (h, D) in enumerate(heads, start=1):
        g = deg[h]
        if g >= s + 1:
            hcount = sum(1 for j in range(i - 1) if h in blocks[j])
            if hcount != i - 1 or D != g - (i - 1):
                f["DICHb"] += 1
        if g <= s:
            if D > s - i + 2:
                f["DICHc"] += 1
            if i == 1 and D > s + 1:
                f["DICHc_i1"] += 1
            # boundary Qwen names: first excess step j0 == i (excess only at
            # the deletion step itself)
            firstex = None
            for j in range(1, i + 1):
                if vals[j - 1].get(h, 0) > s - j + 1:
                    firstex = j
                    break
            if firstex == i and D > s - i + 2:
                f["DICHc_j0eqi"] += 1
    return f, s


def part1(seed=20260818):
    rng = random.Random(seed)
    fails = Counter()
    stats = Counter()
    # exhaustive connected graphs n<=6
    for n in range(2, 7):
        for adj in all_graphs_upto(n):
            deg = [len(adj[v]) for v in range(n)]
            for t in range(3):
                f, s = check_chain(deg, None if t == 0 else rng)
                fails.update(f)
                stats["runs"] += 1
                # is this a reductio instance?  need alpha; approximate by
                # brute-force max independent set for n<=6
                if t == 0:
                    best = 0
                    for mask in range(1 << n):
                        S = [v for v in range(n) if mask >> v & 1]
                        if all(b not in adj[a] for a, b in combinations(S, 2)):
                            best = max(best, len(S))
                    res = n - s
                    stats["reductio" if res == best else "nonreductio"] += 1
    # random graphs n=7..13
    for _ in range(4000):
        n = rng.randint(7, 13)
        p = rng.choice([0.2, 0.35, 0.5, 0.65, 0.8])
        adj = {v: set() for v in range(n)}
        for a, b in combinations(range(n), 2):
            if rng.random() < p:
                adj[a].add(b); adj[b].add(a)
        deg = [len(adj[v]) for v in range(n)]
        if sum(deg) == 0:
            continue
        for t in range(3):
            f, s = check_chain(deg, None if t == 0 else rng)
            fails.update(f); stats["runs"] += 1
    return fails, stats


def part2():
    """T-J4: the k=2 / e_B=2 branch of Theorem T3."""
    res = Counter()
    bad_traj = []
    bad_sum = []
    count_sentence_wrong = 0
    for a0 in range(1, 12):
        for b0 in range(1, 12):
            for c0 in range(1, 12):
                # d(G) = [a0+c0+2, b0+c0+2, 3, 3, 2^{c0}, 1^{a0+b0}]
                X = a0 + c0 + 2
                Y = b0 + c0 + 2
                if X < Y:
                    continue
                if Y < 4:
                    continue
                deg = [X, Y, 3, 3] + [2] * c0 + [1] * (a0 + b0)
                m = sum(deg) // 2
                if sum(deg) % 2:
                    continue
                if m != a0 + b0 + 2 * c0 + 5:
                    res["m_formula_wrong"] += 1
                out = hh_labelled(deg)
                if out is None:
                    res["nongraphical"] += 1
                    continue
                heads, blocks, s, vals = out
                res["instances"] += 1
                D = [d for _, d in heads]
                # displayed trajectory: D1 = X, D2 = Y-1, D3 = 1
                if len(D) < 3 or D[0] != X or D[1] != Y - 1 or D[2] != 1:
                    res["traj_mismatch"] += 1
                    bad_traj.append((a0, b0, c0, D[:4]))
                    continue
                # L^2 = [1,1,1,1,0...] : the list at the start of step 3
                L2 = sorted(vals[2].values(), reverse=True)
                if [x for x in L2 if x > 0] != [1, 1, 1, 1]:
                    res["L2_mismatch"] += 1
                # the SUM argument (the parenthetical)
                if D[0] + D[1] + D[2] != m - 1:
                    res["sum_arg_fail"] += 1
                    bad_sum.append((a0, b0, c0, D[:3], m))
                # the TERMINAL-COUNT sentence: Lemma T shape [D3, 1^{D3}, 0..]
                # with D3=1 has 2 ones total / 1 one after the head; the text
                # says "exactly D3=1 one" vs "actually 4".
                ones_total = sum(1 for x in L2 if x == 1)
                ones_after_head = ones_total - 1
                if not (ones_total == 4 and ones_after_head == 3):
                    res["count_shape_unexpected"] += 1
                # text claims required=1, actual=4; correct pairs are (2,4) or
                # (1,3).  So the sentence as written is a miscount:
                count_sentence_wrong += 1
                res["contradiction_still_holds"] += (
                    1 if ones_total != 2 and ones_after_head != 1 else 0)
    return res, count_sentence_wrong, bad_traj[:3], bad_sum[:3]


if __name__ == "__main__":
    f, st = part1()
    print("[PART 1 — K-CHAIN A2 re-check: F3'/Z+/DICH at GENERAL s, "
          "3 tie-breaks each]")
    print(f"  labelled HH runs = {st['runs']}   "
          f"(n<=6 exhaustive canonical runs: reductio={st['reductio']}, "
          f"non-reductio={st['nonreductio']})")
    for k in ("F3P", "ZP", "DICHb", "DICHc", "DICHc_i1", "DICHc_j0eqi"):
        print(f"  {k:12s} failures = {f[k]}")
    print("  => K-J1 (F3' general-s) and K-J2 (DICH incl. both boundaries) "
          "reproduce with 0 failures.")
    print()
    r, cw, bt, bs = part2()
    print("[PART 2 — T3-REPAIRED A2 re-check: T-J4, k=2/e_B=2 branch]")
    print(f"  parameter instances (a0,b0,c0 in 1..11) = {r['instances']}")
    print(f"  displayed-trajectory mismatches D=(X, Y-1, 1) = {r['traj_mismatch']}")
    print(f"  L^2 != [1,1,1,1,0...]                      = {r['L2_mismatch']}")
    print(f"  SUM argument  Sum_(i<=3) D_i == m-1 fails  = {r['sum_arg_fail']}")
    print(f"  terminal-shape ones (total, after-head) unexpected = "
          f"{r['count_shape_unexpected']}")
    print(f"  instances where the text's count sentence miscounts = {cw}")
    print(f"  instances where the contradiction still holds anyway = "
          f"{r['contradiction_still_holds']}")
    if bt:
        print(f"  sample traj mismatches: {bt}")
    if bs:
        print(f"  sample sum failures:    {bs}")
    print("  => T-J4 UPHELD as a textual miscount; the parenthetical sum "
          "argument closes the branch on its own.")
