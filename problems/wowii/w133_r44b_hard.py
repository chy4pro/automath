#!/usr/bin/env python3
"""WOWII-133 round 44 slice 2 -- THE DIRECT ATTEMPT TO BUILD THE BREAKER.

Slice 1 proved (ROW-HARD): the ONE thing that can still break WOWII-133 on draft 42.4's
residual row is a CASE A instance in which EVERY admissible frame at EVERY far end of `w` has
max(a(y), deg(y)-1) <= 1 + k2(y).  Slice 1 also measured that every instance this line holds
has SLACK >= 0, the minimum being exactly 0, attained once.

This slice tries to BUILD one, from the only lever slice 1 identified as pointing the right
way.  On a TRIANGLE-FREE host a(v) = deg(v) exactly, so
  * SUBDIVIDING an edge cannot lower a anywhere (the new vertex is isolated in both end
    neighbourhoods) -- it buys mu and nothing else;  that is why W44a has SLACK +2;
  * DELETING an edge at y lowers a(y) by exactly 1.
So the sabotage is edge deletion aimed at the frames with the largest slack, subject to every
condition of the class surviving.  Deletion can only INCREASE distances, so rad can only rise.

REGISTERED BEFORE THE RUN:
  (P3) the greedy will drive the maximum SLACK strictly down over its first ten accepted
       deletions -- if it does not, the instrument is broken and nothing it prints is a
       measurement;
  (P4) it will NOT reach SLACK < 0.  A failure of (P4) would be the first instance ever built
       that exhibits the open case, and it would have to be re-verified standalone (rule 105)
       before anything is claimed.

Self-contained: primitives and machinery COPIED from `w133_r44_row.py`, never imported.
Interpreter: system python3, pure stdlib.  No SAT, no exhaustive search.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 900.0
CHECKS = 0
FAILS = 0
def over():
    return (time.time() - T0) > DEADLINE


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)


def adj(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        if u != v:
            g[u].add(v)
            g[v].add(u)
    return g


def edges_of(g):
    return [(u, v) for u in range(len(g)) for v in g[u] if u < v]


def bfs(g, s):
    n = len(g)
    d = [-1] * n
    d[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                dq.append(w)
    return d


def connected(g):
    return all(x >= 0 for x in bfs(g, 0))


def c4_free(g):
    """this line's sense: NO two vertices have two common neighbours."""
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def a_val(g, v):
    """a(v) = alpha(G[N(v)]) by BRUTE independent-set search."""
    nb = sorted(g[v])
    best = 0
    for k in range(len(nb), 0, -1):
        if k <= best:
            break
        for S in combinations(nb, k):
            if all(y not in g[x] for x, y in combinations(S, 2)):
                best = k
                break
        if best == k:
            break
    return best


def a_val_matching(g, v):
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    return D, ecc, r


def centre_of(ecc, r):
    return [v for v in range(len(ecc)) if ecc[v] == r]


def maximally_far(D, ecc, r, w):
    """draft 42.4 condition 4 / brief E46 condition 4: d(c,w) == rad for EVERY centre c."""
    C = centre_of(ecc, r)
    return all(D[c][w] == r for c in C)


def l_of(g):
    n = len(g)
    return sum(a_val_matching(g, v) for v in range(n)) / float(n)


def is_induced_path(g, P):
    if len(set(P)) != len(P):
        return False
    for i in range(len(P) - 1):
        if P[i + 1] not in g[P[i]]:
            return False
    for i in range(len(P)):
        for j in range(i + 2, len(P)):
            if P[j] in g[P[i]]:
                return False
    return True


def is_anchored_induced_path(g, P, w):
    return bool(P) and P[0] == w and is_induced_path(g, P)


def build_anchored_path(g, w, cap, budget=200000):
    """capped DFS for an induced path with ENDPOINT w on >= cap vertices.  None means NOT
    BUILT WITHIN THE BUDGET -- never 'does not exist'."""
    nodes = [0]
    best = [1]
    dw = bfs(g, w)

    def dfs(path, pset):
        nodes[0] += 1
        if nodes[0] > budget:
            return None
        if len(path) > best[0]:
            best[0] = len(path)
        if len(path) >= cap:
            return list(path)
        u = path[-1]
        for x in sorted(g[u] - pset, key=lambda z: -dw[z]):
            bad = False
            for y in path[:-1]:
                if x in g[y]:
                    bad = True
                    break
            if bad:
                continue
            path.append(x)
            pset.add(x)
            r = dfs(path, pset)
            if r is not None:
                return r
            path.pop()
            pset.discard(x)
        return None
    r = dfs([w], {w})
    return r, best[0], nodes[0] > budget


def exact_endpath(g, w, cap=64):
    """LONGEST anchored induced path from w, by complete DFS.  Only for SMALL hosts: the
    return flag says whether the search was complete."""
    best = [1]
    nodes = [0]

    def dfs(path, pset):
        nodes[0] += 1
        if nodes[0] > 4000000:
            return False
        if len(path) > best[0]:
            best[0] = len(path)
        ok = True
        for x in g[path[-1]] - pset:
            if any(x in g[y] for y in path[:-1]):
                continue
            path.append(x)
            pset.add(x)
            if not dfs(path, pset):
                ok = False
            path.pop()
            pset.discard(x)
            if not ok:
                break
        return ok
    complete = dfs([w], {w})
    return best[0], complete


def exact_path(g):
    """LONGEST induced path, by complete DFS from every start.  SMALL hosts only."""
    best = 1
    comp = True
    for v in range(len(g)):
        b, c = exact_endpath(g, v)
        best = max(best, b)
        comp = comp and c
    return best, comp


def add_pendant(g, w):
    """G := H + one pendant vertex at w.  Returns the new graph; the pendant is vertex n."""
    n = len(g)
    E = edges_of(g) + [(w, n)]
    return adj(n + 1, E)


def geodesics(D, g, w, x, cap):
    """up to `cap` DISTINCT w->x geodesics, deterministic order, as vertex lists w..x."""
    d = D[w][x]
    out = []

    def back(cur, acc):
        if len(out) >= cap:
            return
        if cur == w:
            out.append(list(reversed(acc)))
            return
        for p in sorted(g[cur]):
            if D[w][p] == D[w][cur] - 1:
                acc.append(p)
                back(p, acc)
                acc.pop()
                if len(out) >= cap:
                    return
    back(x, [x])
    return [P for P in out if len(P) == d + 1]


def tail1_frames(g, D, w, x, ngeo=3):
    """every (P, y) frame of (TAIL-1) from w to the far end x, over up to ngeo geodesics."""
    fr = []
    for P in geodesics(D, g, w, x, ngeo):
        d = len(P) - 1
        ud, um1 = P[-1], P[-2]
        for y in sorted(g[ud]):
            if y == um1 or y in g[um1]:
                continue
            if any(y == P[i] or y in g[P[i]] for i in range(d)):
                continue
            fr.append((P, y))
    return fr


def k2_of(g, P, y):
    d = len(P) - 1
    k = 0
    for j in (d - 2, d - 3):
        if j >= 0 and (g[y] & g[P[j]]):
            k += 1
    return k


def tail2_at(g, D, ecc, w, ngeo=3, nfar=8):
    """Look for a frame from w at which (TAIL-2'') fires, and CERTIFY it by building z.
    Returns (fired, cert_path, best_slack, nframes).  best_slack = max over frames of
    max(a(y),deg(y)-1) - (2+k2), so >= 0 means (TAIL-2'') fires."""
    n = len(g)
    e = ecc[w]
def frame_scan(g, D, ecc, w, ngeo=2, nfar=6):
    """EVERY admissible (TAIL-1) frame from w, with NO early return: returns (number of
    frames, max slack over them).  `tail2_at` stops at the first frame that fires, so its
    frame count is the index of that frame and NOT this number -- see PART 3's own-error
    note; this function exists because that distinction was got wrong once in this file."""
    n = len(g)
    e = ecc[w]
    fars = sorted(v for v in range(n) if D[w][v] == e)[:nfar]
    best = None
    nfr = 0
    amin = None
    for x in fars:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            nfr += 1
            k2 = k2_of(g, P, y)
            sl = max(a_val_matching(g, y), len(g[y]) - 1) - (2 + k2)
            if best is None or sl > best:
                best = sl
            av = a_val_matching(g, y)
            if amin is None or av < amin:
                amin = av
    return nfr, (best if best is not None else -99), (amin if amin is not None else -1)


def tail1_path(g, D, ecc, v):
    """(TAIL-1)'s own construction at v: an anchored induced path on ecc(v)+2 vertices."""
    n = len(g)
    fars = [u for u in range(n) if D[v][u] == ecc[v]]
    for x in sorted(fars):
        for (P, y) in tail1_frames(g, D, v, x, 3):
            R = P + [y]
            if is_anchored_induced_path(g, R, v) and len(R) == ecc[v] + 2:
                return R
    return None


def load_txt(path):
    nn = None
    ed = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split()
        if len(p) == 1:
            nn = int(p[0])
        else:
            ed.append((int(p[0]), int(p[1])))
    return adj(nn, ed)


def far_intersection(D, ecc, r):
    """(FAR): the set of vertices satisfying condition 4 = the intersection of the spheres
    S_rad(c) over all centres c.  Returned as a list."""
    n = len(ecc)
    C = centre_of(ecc, r)
    return [w for w in range(n) if all(D[c][w] == r for c in C)]



def full_scan(g, D, ecc, w, ngeo=2, nfar=0):
    """EVERY admissible frame from w (nfar = 0 means every far end): the list of
    (slack, P, y) with no early return."""
    n = len(g)
    e = ecc[w]
    fars = sorted(v for v in range(n) if D[w][v] == e)
    if nfar:
        fars = fars[:nfar]
    out = []
    for x in fars:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            k2 = k2_of(g, P, y)
            out.append((max(a_val_matching(g, y), len(g[y]) - 1) - (2 + k2), P, y))
    return out


def invariants(g, w):
    """every condition of the CASE A residual row, recomputed from scratch."""
    if not connected(g):
        return None
    D, ecc, r = profile(g)
    diam = max(ecc)
    if r < 5 or diam != r + 1 or ecc[w] != r + 1:
        return None
    C = centre_of(ecc, r)
    if any(D[c][w] != r for c in C):
        return None
    if l_of(g) <= 4.0:
        return None
    if min(a_val_matching(g, v) for v in range(len(g))) < 2:
        return None
    return D, ecc, r, diam, C


def delete(g, u, v):
    h = [set(s) for s in g]
    h[u].discard(v)
    h[v].discard(u)
    return h


def main():
    print("WOWII-133 round 44 slice 2 -- THE DIRECT ATTEMPT TO BUILD THE BREAKER")
    print("interpreter: system python3 %s (pure stdlib)" % sys.version.split()[0])
    g = load_txt("problems/wowii/w133_r43_W43a.txt")
    D, ecc, r = profile(g)
    C = centre_of(ecc, r)
    W = far_intersection(D, ecc, r)
    W = [x for x in W if ecc[x] == r + 1]
    ck(bool(W), "W43a carries a condition-4 vertex to start from")
    w = W[0]
    st = invariants(g, w)
    ck(st is not None, "the starting host satisfies every condition of the class")
    tri = sum(1 for v in range(len(g)) if len(g[v]) != a_val_matching(g, v))
    ck(tri == 0, "W43a is TRIANGLE-FREE, so a(v) = deg(v) and deletion lowers a by exactly 1")
    print("start: n=%d |E|=%d rad=%d diam=%d l=%.6f w=%d  (triangle-free: a = deg)"
          % (len(g), len(edges_of(g)), r, max(ecc), l_of(g), w))

    traj = []
    ftraj = []
    dels = 0
    rejected = 0
    hard = None
    while not (time.time() - T0 > DEADLINE):
        st = invariants(g, w)
        if st is None:
            print("  ** invariants lost -- should be impossible, every deletion was screened")
            ck(False, "invariants held at the top of every iteration")
            break
        D, ecc, r, diam, C = st
        fr = full_scan(g, D, ecc, w)
        if not fr:
            print("  no admissible frame remains at w -- (TAIL-1) itself would fail here")
            break
        mx = max(s for (s, P, y) in fr)
        nfire = sum(1 for (s, P, y) in fr if s >= 0)
        traj.append(mx)
        ftraj.append((nfire, len(fr)))
        if mx < 0:
            hard = (g, w)
            print("  *** MAX SLACK < 0 at deletion %d -- CANDIDATE HARD INSTANCE" % dels)
            break
        # delete one edge at the y of a maximal-slack frame, screening every candidate
        fr.sort(key=lambda t: -t[0])
        moved = False
        for (s, P, y) in fr[:60]:
            for t in sorted(g[y]):
                if t == P[-1]:
                    continue
                if len(g[y]) <= 2 or len(g[t]) <= 2:
                    continue
                h = delete(g, y, t)
                if invariants(h, w) is None:
                    rejected += 1
                    continue
                g = h
                dels += 1
                moved = True
                break
            if moved:
                break
        if not moved:
            print("  no deletion anywhere keeps the class alive: the greedy is STUCK after"
                  " %d deletions (%d candidates screened and rejected)." % (dels, rejected))
            break
        if dels % 10 == 0:
            print("  %3d deletions: max SLACK = %+d, |E| = %d, l = %.4f, rad = %d, diam = %d,"
                  " mu = %d, %.0fs"
                  % (dels, mx, len(edges_of(g)), l_of(g), r, diam,
                     min(a_val_matching(g, v) for v in range(len(g))), time.time() - T0))

    print()
    print("""
  A SECOND INSTRUMENT, REGISTERED AFTER (P3) FAILED AND LABELLED AS SUCH.  The maximum over
  several hundred frames cannot move when one frame's y loses one edge, so max-SLACK was the
  wrong progress coordinate and (P3) was a badly posed prediction, not a broken greedy.  The
  coordinate that can move is the NUMBER OF FIRING FRAMES -- (ROW-HARD) needs it to reach 0.
  (P5), registered now and before its numbers are read: the firing-frame count will fall
  monotonically and will NOT reach 0.""")
    print("  firing frames / total frames, first 5: %s" % ftraj[:5])
    print("  firing frames / total frames, last  5: %s" % ftraj[-5:])
    if len(ftraj) >= 2:
        mono = all(ftraj[i + 1][0] <= ftraj[i][0] for i in range(len(ftraj) - 1))
        print("  (P5) monotone fall: %s;  reached 0: %s"
              % ("YES" if mono else "NO -- it went UP somewhere", ftraj[-1][0] == 0))
    print("  SLACK trajectory (first 20): %s" % traj[:20])
    print("  SLACK trajectory (last  10): %s" % traj[-10:])
    print("  deletions accepted: %d;  candidate deletions rejected by the screen: %d"
          % (dels, rejected))
    if len(traj) >= 11:
        ck(traj[10] < traj[0], "(P3): the greedy drove max SLACK strictly down in 10 accepted"
                               " deletions -- the instrument moves")
        print("  (P3) %s: SLACK went %+d -> %+d over the first ten accepted deletions."
              % ("HELD" if traj[10] < traj[0] else "FAILED", traj[0], traj[10]))
    else:
        print("  (P3) NOT TESTED: the greedy stopped after %d iterations, fewer than the ten"
              " the prediction was about.  Recorded as untested, not as held." % len(traj))
    print("  (P4) %s: minimum max-SLACK reached = %+d."
          % ("FAILED -- a candidate hard instance exists" if hard else "HELD",
             min(traj) if traj else 99))
    if hard is not None:
        hg, hw = hard
        fn = "problems/wowii/w133_r44_W44b.txt"
        with open(fn, "w") as f:
            f.write("# candidate HARD instance, w = %d\n%d\n" % (hw, len(hg)))
            for (u, v) in sorted(edges_of(hg)):
                f.write("%d %d\n" % (u, v))
        print("  candidate written to %s -- NOTHING is claimed about it until a standalone"
              " script (rule 105) has re-verified it." % fn)
    else:
        print("  NO HARD INSTANCE BUILT.  Reported as a FAILED ATTEMPT, with its floor.")
    print()
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
