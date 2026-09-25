#!/usr/bin/env python3
"""Erdos #287 counterexample search.

Look for distinct integers 1 < n_1 < ... < n_k, all consecutive gaps <= 2,
with sum of reciprocals exactly 1. Finding one DISPROVES the conjecture
(which asserts max gap >= 3 is forced).

DFS with exact rational arithmetic (num/den ints), dead-state memoization,
and a hard internal time cap. Reports coverage on exit.
"""
import sys
import time
from math import gcd

TIME_CAP_SEC = 480  # hard internal cap
START_MAX = 40      # try n_1 = 2 .. START_MAX (coverage reported)

t0 = time.time()
found = []
dead = set()  # (d, num, den) states proven fruitless
nodes = 0


def dfs(d, num, den, path):
    """State: last denominator d, remaining num/den to represent, path so far."""
    global nodes
    nodes += 1
    if num == 0:
        found.append(list(path))
        return True
    if time.time() - t0 > TIME_CAP_SEC:
        raise TimeoutError
    # must add at least one more term 1/v with v in {d+1, d+2};
    # overshoot check: need num/den >= 1/(d+2)  <=>  num*(d+2) >= den
    if num * (d + 2) < den:
        return False
    key = (d, num, den)
    if key in dead:
        return False
    for v in (d + 1, d + 2):
        # remaining - 1/v = (num*v - den) / (den*v)
        nn = num * v - den
        if nn < 0:
            continue
        nd = den * v
        g = gcd(nn, nd) if nn else 1
        path.append(v)
        if dfs(v, nn // g if nn else 0, nd // g if nn else 1, path):
            path.pop()
            return True
        path.pop()
    dead.add(key)
    return False


def main():
    sys.setrecursionlimit(100000)
    covered = []
    try:
        for a in range(2, START_MAX + 1):
            # first term 1/a, remaining = 1 - 1/a = (a-1)/a
            g = gcd(a - 1, a)
            if dfs(a, (a - 1) // g, a // g, [a]):
                print(f"COUNTEREXAMPLE with n1={a}: {found[-1]}")
                return
            covered.append(a)
            print(f"n1={a}: exhausted, no counterexample "
                  f"({nodes} nodes, {time.time()-t0:.1f}s)", flush=True)
    except TimeoutError:
        print(f"TIME CAP hit at {TIME_CAP_SEC}s")
    print(f"RESULT: no counterexample for n1 in {covered}")
    print(f"nodes={nodes} dead_states={len(dead)} elapsed={time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
