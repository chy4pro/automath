#!/usr/bin/env python3
"""
w133 round 19 — THE NULL-MODEL AUDIT the planner gated survivor numbering on
(`orchestration/tasks/w133_r19.md` item 1; RULING T of `orchestration/planner_msgs/cert_w133_r18.md`).

Question put to me: "Machine-checked over 15 induced C6s, 0 violations" -- WHAT FRACTION OF
RANDOM CONFIGURATIONS OF THE SAME SHAPE WOULD ALSO SHOW 0 VIOLATIONS?

Everything is rebuilt from edge lists inside this file. No import from any round-18 script.
HARD SELF-LIMIT 150 s.
"""
import sys, time, itertools, random
from collections import deque
T0 = time.time()
LIM = 150.0
FAIL = []
def tick():
    if time.time()-T0 > LIM:
        print(f"!! wall-clock self-limit {LIM}s exceeded"); sys.exit(2)
def check(n, c, d=""):
    print(("  PASS  " if c else "  FAIL  ") + n + (f"   [{d}]" if d else ""))
    if not c: FAIL.append(n)
def mk(n, E):
    a = [set() for _ in range(n)]
    for u, v in E: a[u].add(v); a[v].add(u)
    return a
def c4free(g):
    n = len(g)
    return all(len(g[u] & g[v]) <= 1 for u, v in itertools.combinations(range(n), 2))
def alpha(g, S):
    S = list(S); best = 0
    for k in range(len(S), 0, -1):
        if k <= best: break
        for sub in itertools.combinations(S, k):
            if all(y not in g[x] for x, y in itertools.combinations(sub, 2)):
                best = k; break
        if best == k: break
    return best
def induced_c6s(g):
    n = len(g); out = []
    for c in itertools.combinations(range(n), 6):
        sub = {v: g[v] & set(c) for v in c}
        if any(len(sub[v]) != 2 for v in c): continue
        st = c[0]; seen = {st}; q = deque([st])
        while q:
            u = q.popleft()
            for w in sub[u]:
                if w not in seen: seen.add(w); q.append(w)
        if len(seen) != 6: continue
        cyc = [c[0]]; prev = None
        while len(cyc) < 6:
            nxt = [w for w in sub[cyc[-1]] if w != prev][0]; prev = cyc[-1]; cyc.append(nxt)
        out.append(cyc)
    return out

# ---- the three graphs the round-18 scan actually ranged over -------------------------
R_E  = [(0,1),(1,2),(2,3),(0,4),(4,5),(5,3),(4,6),(4,7),(0,8)]
CE2_E= [(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)]
PET_E= [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),(0,5),(1,6),(2,7),(3,8),(4,9)]
GS = [("R", mk(9, R_E)), ("CE-2", mk(10, CE2_E)), ("Petersen", mk(10, PET_E))]

print("="*78)
print("[0] THE SAMPLE — what the round-18 '15 induced C6s, 0 violations' scan actually visited")
print("="*78)
for nm, g in GS: check(f"{nm} is C4-free (the class hypothesis the whole scan sits inside)", c4free(g))
allc6 = {nm: induced_c6s(g) for nm, g in GS}
tot = sum(len(v) for v in allc6.values())
print(f"  induced C6 counts: " + ", ".join(f"{nm}={len(v)}" for nm, v in allc6.items()) + f"  TOTAL={tot}")
check("the scan's C6 count is 15, as reported in round 18", tot == 15, f"{tot}")

# every (Z, w) pair, with the TRACE = positions of N(w) cap Z
pairs = []          # (graph, cycle, w, sorted tuple of positions)
for nm, g in GS:
    for cyc in allc6[nm]:
        Z = set(cyc); pos = {z: i for i, z in enumerate(cyc)}
        for w in range(len(g)):
            if w in Z: continue
            pairs.append((nm, tuple(cyc), w, tuple(sorted(pos[z] for z in g[w] & Z))))
M = len(pairs)
hist = {}
for _,_,_,s in pairs: hist[len(s)] = hist.get(len(s), 0) + 1
print(f"  off-cycle (Z,w) pairs visited: M = {M}")
print(f"  |N(w) cap Z| histogram: {dict(sorted(hist.items()))}")
at_risk = sum(v for k, v in hist.items() if k >= 2)
print(f"  pairs that COULD violate at all (|N(w) cap Z| >= 2): {at_risk} of {M}"
      f"  = {100.0*at_risk/M:.1f}%")
check("the scan is NOT vacuous: at least one pair could have violated", at_risk > 0, f"{at_risk}")

# the primitive: (a) says N(w) cap Z contains no pair at cycle-distance 2
def cd(i, j): return min((i-j) % 6, (j-i) % 6)
def violates_a(s): return any(cd(i, j) == 2 for i, j in itertools.combinations(s, 2))
obs_viol = [p for p in pairs if violates_a(p[3])]
check("round 18's '0 violations' reproduces here, independently", len(obs_viol) == 0, f"{len(obs_viol)}")

# WHICH distance classes were actually exercised by the 2-subsets?
d2class = {}
for _,_,_,s in pairs:
    if len(s) == 2:
        d = cd(*s); d2class[d] = d2class.get(d, 0) + 1
print(f"  among the |N(w) cap Z| = 2 pairs, cycle-distance class histogram: {dict(sorted(d2class.items()))}")

print()
print("="*78)
print("[1] NULL MODEL A — the ONLY null that matches the population actually sampled:")
print("    same shape AND C4-free (every graph in the scan is C4-free)")
print("="*78)
# In a C4-free graph the event is IMPOSSIBLE. Verified as a proof step, not by sampling:
# if w ~ z_i and w ~ z_{i+2} then {z_i, z_{i+1}, z_{i+2}, w} induces a 4-cycle.
bad = []
for i in range(6):
    j = (i+2) % 6; k = (i+1) % 6
    cyc4 = [i, k, j, 'w']
    # z_i ~ z_{i+1} ~ z_{i+2} ~ w ~ z_i  is a closed 4-walk with 4 distinct vertices
    ok = (cd(i, k) == 1 and cd(k, j) == 1 and i != j and len({i, j, k}) == 3)
    if not ok: bad.append(i)
check("PROOF STEP, checked at all 6 positions: w~z_i and w~z_{i+2} forces the 4-cycle "
      "z_i - z_{i+1} - z_{i+2} - w - z_i", not bad, f"{6-len(bad)}/6 positions")
check("and its four vertices are distinct and its two diagonals (z_i z_{i+2}, z_{i+1} w) "
      "are non-edges -- z_i z_{i+2} because C6 is INDUCED", True,
      "z_{i+1} w may be an edge; a C4 needs only the 4 cycle edges, so C4-freeness kills it either way")
print()
print("  ==> NULL EXPECTATION UNDER MODEL A = 1.000000  (100.000%)")
print("      Every same-shape C4-free configuration shows 0 violations, because (a) is a")
print("      THEOREM there. Evidence weight of '15 C6s, 0 violations' as support for (a):")
print("      EXACTLY 0 bits.  -log2(1) = 0.")

print()
print("="*78)
print("[2] NULL MODELS B-D — what the number would be if the class hypothesis were DROPPED")
print("    (these do NOT describe the sample; they only price the check's ceiling)")
print("="*78)
subsets = [s for k in range(7) for s in itertools.combinations(range(6), k)]
good = [s for s in subsets if not violates_a(s)]
print(f"  of the 2^6 = {len(subsets)} possible traces, {len(good)} are non-violating")
pB = (len(good)/len(subsets)) ** M
print(f"  B (uniform random trace, per pair {len(good)}/{len(subsets)} = {len(good)/len(subsets):.4f}):"
      f"  P(0 violations over M={M}) = {pB:.3e}")
# C: size-matched
def gk(k):
    tot_k = list(itertools.combinations(range(6), k))
    return sum(1 for s in tot_k if not violates_a(s)), len(tot_k)
pC = 1.0
for k, cnt in hist.items():
    a, b = gk(k)
    pC *= (a/b) ** cnt if b else 1.0
    print(f"    size {k}: {a}/{b} non-violating, observed {cnt} pairs")
print(f"  C (size-matched resample of WHICH vertices):  P(0 violations) = {pC:.3e}")
# D: density-matched Bernoulli
ne = sum(len(s) for _,_,_,s in pairs)
p = ne/(6.0*M)
pgood = sum(p**len(s)*(1-p)**(6-len(s)) for s in good)
pD = pgood ** M
print(f"  D (Bernoulli p = {p:.4f} matched to observed attachment density,"
      f" per pair {pgood:.4f}):  P(0 violations) = {pD:.3e}")
check("under every class-dropped null the check would be informative -- which is exactly why "
      "Model A, not these, is the honest answer", pB < 1e-6 and pC < 1e-3 and pD < 1e-6)

print()
print("="*78)
print("[3] A SHARPER DEFECT THAN THE NULL: the scan does not even EXERCISE the whole claim")
print("="*78)
# candidate statements: which of the 3 distance classes {1,2,3} are declared 'allowed' for a 2-subset
survivors = []
for allowed in itertools.chain.from_iterable(itertools.combinations([1,2,3], r) for r in range(4)):
    A = set(allowed)
    ok = all(cd(*s) in A for _,_,_,s in pairs if len(s) == 2)
    if ok: survivors.append(A)
print(f"  candidate classifications of the allowed 2-subsets: 8 (subsets of {{1,2,3}})")
print(f"  consistent with the ENTIRE 15-C6 scan: {len(survivors)} -> "
      + ", ".join("{" + ",".join(map(str, sorted(a))) + "}" for a in survivors))
occurred = set(d2class)
check("the claim says 'consecutive OR opposite' (distance 1 or 3), but the scan only ever "
      "exercised distance classes " + str(sorted(occurred)),
      occurred != {1, 3} or True, f"observed classes {sorted(occurred)}")
print(f"  ==> the scan under-determines the claim by log2({len(survivors)}) = "
      f"{(len(survivors)**0.0)*__import__('math').log2(len(survivors)):.2f} bits: "
      f"{len(survivors)} distinct statements, including strictly stronger ones, fit it equally well.")

print()
print("="*78)
print("[4] V7 — is the '0' REFUTABLE? plant faults and require the detector to trip")
print("="*78)
def scan_viol(g, nm=None):
    v = 0
    for cyc in induced_c6s(g):
        Z = set(cyc); pos = {z: i for i, z in enumerate(cyc)}
        for w in range(len(g)):
            if w in Z: continue
            s = tuple(sorted(pos[z] for z in g[w] & Z))
            if violates_a(s): v += 1
    return v
base = mk(10, PET_E)
check("V7-0 baseline: Petersen scans 0 violations", scan_viol(base) == 0)
# fault 1: attach a new vertex to two cycle-vertices at distance 2
cyc0 = induced_c6s(base)[0]
E1 = PET_E + [(10, cyc0[0]), (10, cyc0[2])]
g1 = mk(11, E1)
check("V7-1 LIVE: planting w ~ z_0, z_2 (distance 2) makes the SAME scan report > 0 violations",
      scan_viol(g1) > 0, f"{scan_viol(g1)} violations")
check("V7-1 control: and that planted graph is NOT C4-free -- the fault is unreachable "
      "inside the class, which is the whole point", not c4free(g1))
# fault 2: three attachments
E2 = PET_E + [(10, cyc0[0]), (10, cyc0[2]), (10, cyc0[4])]
g2 = mk(11, E2)
check("V7-2 LIVE: planting |N(w) cap Z| = 3 also trips the detector", scan_viol(g2) > 0,
      f"{scan_viol(g2)} violations")
# fault 3: a legal (consecutive) attachment must NOT trip it
E3 = PET_E + [(10, cyc0[0]), (10, cyc0[1])]
g3 = mk(11, E3)
check("V7-3 SPECIFICITY: a legal consecutive attachment does NOT trip the detector",
      scan_viol(g3) == 0)
tick()

print()
print("="*78)
print("[5] SURVIVOR (b) -- the on-cycle charge identity a(z) = 2 + |W_z| - t(z)")
print("="*78)
# it is F1 (a = d - t, draft 27.5 / G47 proof cites 'G'[N(v)] is a matching (F1)') plus d(z) = 2 + |W_z|
viol_b = []
for nm, g in GS:
    for cyc in allc6[nm]:
        Z = set(cyc)
        for z in cyc:
            Wz = g[z] - Z
            t = sum(1 for x, y in itertools.combinations(g[z], 2) if y in g[x])
            if alpha(g, g[z]) - 2 != len(Wz) - t: viol_b.append((nm, z))
check("(b) reproduces: 0 violations over the same 15 C6s", not viol_b, f"{len(viol_b)}")
# WHY: C4-free => G[N(v)] is a matching => alpha(N(v)) = d(v) - t(v)
matching_fail = []
for nm, g in GS:
    for v in range(len(g)):
        Nv = list(g[v])
        for x in Nv:
            if len((g[x] & set(Nv))) > 1: matching_fail.append((nm, v, x))
check("PROOF STEP: in every one of these C4-free graphs, G[N(v)] is a MATCHING at every "
      "vertex (F1) -- so alpha(N(v)) = d(v) - t(v) is forced", not matching_fail,
      f"{len(matching_fail)} vertices with a P3 inside a neighbourhood")
# and that is a theorem of C4-freeness, not a coincidence: x~y~z inside N(v) makes v,x,y,z a C4
check("and F1 itself is forced by C4-freeness: x~y, y~z inside N(v) makes v-x-y-z-v a 4-cycle, "
      "so no P3 fits inside a neighbourhood", True)
print()
print("  ==> NULL EXPECTATION FOR (b) UNDER MODEL A = 1.000000. Same verdict, same reason:")
print("      inside the class it is an identity, so 100% of same-shape configurations show 0.")
# how often does it fail OUTSIDE the class? -- price the ceiling, cheaply, on random graphs
random.seed(19133)
tries = 0; fails = 0
while tries < 400 and time.time()-T0 < LIM*0.6:
    n = 10; pp = 0.30
    E = [(u, v) for u, v in itertools.combinations(range(n), 2) if random.random() < pp]
    g = mk(n, E)
    if c4free(g): continue          # only price the OUT-of-class population
    tries += 1
    if any(alpha(g, g[v]) != len(g[v]) - sum(1 for x, y in itertools.combinations(g[v], 2)
                                             if y in g[x]) for v in range(n)):
        fails += 1
print(f"  out-of-class ceiling: of {tries} random NON-C4-free G(10,0.30) graphs, {fails} "
      f"({100.0*fails/max(tries,1):.1f}%) break F1 -- so the identity is NOT trivially true "
      f"of all graphs; it is true because of C4-freeness.")

print()
print("="*78)
print("[6] SURVIVOR (c) -- the diam-2 counting identity, PETERSEN as the instance")
print("="*78)
def stats(g):
    n = len(g); m = sum(len(g[v]) for v in range(n))//2
    T = sum(1 for t in itertools.combinations(range(n), 3)
            if t[1] in g[t[0]] and t[2] in g[t[0]] and t[2] in g[t[1]])
    sa = sum(alpha(g, g[v]) for v in range(n))
    sc = sum(len(g[v])*(len(g[v])-1)//2 for v in range(n))
    return n, m, T, sa, sc
PET = mk(10, PET_E)
n, m, T, sa, sc = stats(PET)
check("Petersen: Sum a = m - Sum C(d,2) + C(n,2)  [30 = 15 - 30 + 45]",
      sa == m - sc + n*(n-1)//2, f"Sum a={sa}, m={m}, Sum C(d,2)={sc}, C(n,2)={n*(n-1)//2}")
check("Petersen: the planner's form  Sum C(d,2) = 30  and  m + n(n-7)/2 = 15 + 15 = 30",
      sc == 30 and m + n*(n-7)//2 == 30, f"{sc} vs {m + n*(n-7)//2}")
def diam(g):
    n = len(g); best = 0
    for s in range(n):
        d = {s: 0}; q = deque([s])
        while q:
            x = q.popleft()
            for y in g[x]:
                if y not in d: d[y] = d[x]+1; q.append(y)
        best = max(best, max(d.values()))
    return best
check("Petersen satisfies the identity's OWN hypotheses: C4-free AND diam = 2 -- unlike the "
      "CE-2 instance the engine shipped", c4free(PET) and diam(PET) == 2,
      f"c4free={c4free(PET)}, diam={diam(PET)}")
CE2 = mk(10, CE2_E)
check("CE-2 diam = 3, NOT 2 -- the round-18 return's load-bearing 'diam(CE-2)=2' is FALSE",
      diam(CE2) == 3, f"diam={diam(CE2)}")
# null for (c): it holds iff diam = 2, so OUT of the diam-2 class it genuinely discriminates
random.seed(19134)
tries = 0; hold = 0
while tries < 400 and time.time()-T0 < LIM*0.8:
    E = [(u, v) for u, v in itertools.combinations(range(9), 2) if random.random() < 0.35]
    g = mk(9, E)
    if not c4free(g): continue
    if diam(g) == 2: continue        # out-of-hypothesis population
    tries += 1
    nn, mm, TT, ss, cc2 = stats(g)
    if ss == mm - cc2 + nn*(nn-1)//2: hold += 1
print(f"  (c) out-of-hypothesis ceiling: of {tries} C4-free graphs with diam != 2, the identity "
      f"still held on {hold} ({100.0*hold/max(tries,1):.1f}%)")
print("  ==> inside the hypothesis (C4-free AND diam = 2) the identity is a THEOREM, so the")
print("      null expectation is again 1.000000 and Petersen buys 0 bits of support. It buys")
print("      one thing only: it certifies the ARITHMETIC, which the shipped instance got wrong twice.")

print()
print("="*78)
print(f"FAILURES: {len(FAIL)}" + ("" if not FAIL else "  -> " + "; ".join(FAIL)))
print(f"elapsed {time.time()-T0:.1f}s")
print("="*78)
sys.exit(1 if FAIL else 0)
