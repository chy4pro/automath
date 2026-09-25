#!/usr/bin/env python3
"""owner-w61 round 5, post-A2: exhaust the general-s species on the remaining
two §7.2 B tools (Lemma T and Lemma H).  Own code; reuses this round's own
graph/HH routines only.

  Lemma T'  : for every k, the run has exactly k steps  <=>  the list at the START
              of step k is [D_k, 1^{D_k}, 0^...].     (tested at k = s)
  Lemma H'  : for 2 <= i <= s, with g_i the head's original degree, D_i its value
              at deletion and h_i := g_i - D_i, if h_i <= i-2 then
              D_i <= s - i + 2 + h_i.                 (tau replaced by s throughout)

Both are tested ON RUNS WITH s != tau (off the reductio), which is the regime where
the tau-stated versions have no content.
"""
import random, sys
from itertools import combinations
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w61_r5_rig import G, random_graphs, atlas_graphs


def labelled_run(g, tiebreak=None):
    """returns (s, list of (g_i, D_i, list_at_start_of_step))"""
    n = g.n
    vals = {v: g.deg(v) for v in range(n)}
    orig = dict(vals)
    alive = set(range(n))
    rnd = tiebreak
    steps = []
    while any(vals[v] > 0 for v in alive):
        order = sorted(alive, key=lambda v: (-vals[v], rnd.random() if rnd else v))
        head = order[0]
        d = vals[head]
        snapshot = sorted((vals[v] for v in alive), reverse=True)
        steps.append((orig[head], d, snapshot))
        alive.discard(head)
        for v in order[1:1 + d]:
            vals[v] -= 1
        if d == 0:
            break
    return len(steps), steps


def check(graphs, label, tiebreaks=3):
    tT = fT = tH = fH = 0
    nonred = 0
    for g in graphs:
        alpha, _ = g.independent_sets_max()
        tau = g.n - alpha
        for t in range(tiebreaks):
            rnd = random.Random(1000 * t + g.n) if t else None
            s, steps = labelled_run(g, rnd)
            if s != tau:
                nonred += 1
            # ---- Lemma T' at k = s: list at start of step s is [D_s, 1^{D_s}, 0^...]
            if s >= 1:
                Ds, snap = steps[-1][1], steps[-1][2]
                want = [Ds] + [1] * Ds
                got = [x for x in snap if x > 0]
                tT += 1
                if got != want:
                    fT += 1
                    if fT <= 3:
                        print(f"   T' FAIL n={g.n} s={s} tau={tau} want={want} got={got}")
            # ---- Lemma H' for 2 <= i <= s
            for i in range(2, s + 1):
                gi, Di, _ = steps[i - 1]
                hi = gi - Di
                if hi <= i - 2:
                    tH += 1
                    if not (Di <= s - i + 2 + hi):
                        fH += 1
                        if fH <= 3:
                            print(f"   H' FAIL n={g.n} s={s} tau={tau} i={i} "
                                  f"g={gi} D={Di} h={hi}")
    print(f"[{label}] runs with s != tau (off the reductio): {nonred}")
    print(f"   Lemma T' tested {tT} terminal steps, failures = {fT}")
    print(f"   Lemma H' tested {tH} (head, step) pairs, failures = {fH}")


if __name__ == '__main__':
    ga = atlas_graphs(7)
    if ga:
        check(ga, "exhaustive connected n<=7 (atlas)")
    check(random_graphs(700, 8, 11, seed=515151), "random connected n=8..11")
    print("done")
