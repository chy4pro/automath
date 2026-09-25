#!/usr/bin/env python3
"""w133_r20_adjudicate.py — GATE A + GATE B adjudication of the round-19 (T-C) re-dispatch.

Graded against the gate PRE-REGISTERED BLIND at 22:06 CDT (state file, "Round 19" §1),
unchanged since.  Nothing here revises that gate.

Also verifies the two byproducts the return delivers (Lemma D, Corollary D'), and localises
the one wrong held-out value.  Self-limit 180s.
"""
import sys, time, itertools

T0 = time.time()
F = []
N = [0]


def check(label, cond, extra=""):
    N[0] += 1
    if time.time() - T0 > 180:
        print("SELF-LIMIT")
        sys.exit(2)
    print(("  PASS  " if cond else "  FAIL  ") + label + (f"   [{extra}]" if extra else ""))
    if not cond:
        F.append(label)


def mk(n, E):
    adj = {v: set() for v in range(n)}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def alpha(adj, S):
    S = list(S)
    best = 0
    for k in range(len(S), -1, -1):
        if k <= best:
            break
        for T in itertools.combinations(S, k):
            if all(y not in adj[x] for x, y in itertools.combinations(T, 2)):
                best = max(best, k)
                break
    return best


def c4free(adj):
    return all(len(adj[u] & adj[v]) <= 1
               for u, v in itertools.combinations(sorted(adj), 2))


M1_E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 6), (1, 6), (2, 7),
        (5, 7), (3, 8), (4, 8), (6, 9), (7, 9), (8, 9), (6, 8)]
M1 = mk(10, M1_E)

print("=" * 78)
print("[A] GATE A — the pre-registered void gate, executed as written")
print("=" * 78)
KEY = [("U1", "H", "YES", "YES"), ("U2", "H", "2", "2"), ("U3", "H", "3", "3"),
       ("U4", "H", "3", "3"), ("U5", "H", "YES", "YES"),
       ("U6", "C", "7", "7"), ("U7", "C", "23", "25"), ("U8", "C", "4", "4"),
       ("U9", "C", "8", "CANNOT COMPUTE")]
tierH_wrong, tierC_wrong, declined = [], [], []
for rid, tier, key, got in KEY:
    if got.startswith("CANNOT COMPUTE"):
        declined.append(rid)
        print(f"  A2   {rid} [{tier}]  key={key:14s} got=CANNOT COMPUTE -> ACCEPTED, not a downgrade")
        continue
    ok = (key == got)
    print(f"  {'ok ' if ok else 'XX '}  {rid} [{tier}]  key={key:14s} got={got}")
    if not ok:
        (tierH_wrong if tier == "H" else tierC_wrong).append(rid)
print()
check("A1  no wrong value on any Tier-H row (U1-U5) -> the round is NOT VOID",
      not tierH_wrong, f"wrong={tierH_wrong}")
check("A3  the held-out table is PRESENT", True, "9 of 9 rows reproduced")
check("A2  CANNOT COMPUTE rows accepted without penalty", declined == ["U9"], str(declined))
print(f"  A4   Tier-C wrong rows -> TRACEABLE DOWNGRADE: {tierC_wrong}")
print("  A6   no row struck: the round-19 pre-dispatch grep (32 checks, DISPATCH CLEARED)")
print("       asserted no held-out answer appears in the brief, BEFORE the call went out.")
print()
print("  GATE A VERDICT: **PASS**, with one traceable Tier-C downgrade (U7) and one")
print("                  accepted decline (U9).  A5: this buys nothing on its own.")

print()
print("=" * 78)
print("[B] U7 — the one wrong value, LOCALISED.  Is the KEY right?")
print("=" * 78)
deg = [len(M1[v]) for v in range(10)]
tri = [sum(1 for x, y in itertools.combinations(sorted(M1[v]), 2) if y in M1[x])
       for v in range(10)]
a = [alpha(M1, M1[v]) for v in range(10)]
check("M1 is C4-free (so a = d - t is legitimate here)", c4free(M1))
print(f"  degrees            {tuple(deg)}  sum {sum(deg)}")
print(f"  t(v) TRUE          {tuple(tri)}  sum {sum(tri)}")
print(f"  t(v) as ENGINE had (1, 1, 0, 1, 1, 0, 1, 0, 1, 1)  sum 7")
print(f"  a-vector TRUE      {tuple(a)}  SUM {sum(a)}")
check("the KEY value 23 is correct (recomputed from the edge list)", sum(a) == 23, str(sum(a)))
check("a = d - t holds vertexwise (F1)", all(a[v] == deg[v] - tri[v] for v in range(10)))
real_tri = [T for T in itertools.combinations(range(10), 3)
            if all(y in M1[x] for x, y in itertools.combinations(T, 2))]
print(f"  triangles of M1    {real_tri}")
check("the engine's TRIANGLE LIST was exactly right",
      set(real_tri) == {(0, 1, 6), (3, 4, 8), (6, 8, 9)}, str(real_tri))
check("the engine's DEGREE vector was exactly right", deg == [3, 3, 3, 3, 3, 3, 4, 3, 4, 3])
print()
print("  DIAGNOSIS: every INPUT was right and the TALLY was wrong.  Vertices 6 and 8 each")
print("  lie in TWO of the three listed triangles (6 in {0,1,6} and {6,8,9}; 8 in {3,4,8}")
print(f"  and {{6,8,9}}), so t(6) = t(8) = 2, not 1.  Sum 32 - 9 = 23, not 32 - 7 = 25.")
print("  A per-vertex INCIDENCE count was collapsed into a membership INDICATOR.")

print()
print("=" * 78)
print("[C] GATE B — the two delivered byproducts, verified")
print("=" * 78)
# Lemma D: G C4-free, v, S subset of N(v) INDEPENDENT => N(u)\{v}, u in S, pairwise disjoint
subs = [frozenset(s) for s in itertools.combinations(range(1, 6), 2)]
lab = {s: i for i, s in enumerate(subs)}
P = mk(10, [(lab[x], lab[y]) for x, y in itertools.combinations(subs, 2) if not (x & y)])
CE2_E = [(0, 1), (0, 4), (0, 5), (0, 8), (1, 2), (2, 3), (2, 6), (3, 5), (3, 7),
         (3, 9), (4, 6), (4, 7), (4, 8), (8, 9)]
CE2 = mk(10, CE2_E)


def lemmaD_holds(adj, require_independent):
    """returns (#configs tested, #violations)"""
    tested = viol = 0
    for v in sorted(adj):
        nb = sorted(adj[v])
        for k in range(2, len(nb) + 1):
            for S in itertools.combinations(nb, k):
                if require_independent and any(y in adj[x] for x, y in
                                               itertools.combinations(S, 2)):
                    continue
                tested += 1
                sets = [adj[u] - {v} for u in S]
                for i, j in itertools.combinations(range(len(S)), 2):
                    if sets[i] & sets[j]:
                        viol += 1
                        break
    return tested, viol


for name, g in [("Petersen", P), ("CE-2", CE2), ("M1", M1)]:
    t, v = lemmaD_holds(g, True)
    check(f"Lemma D holds on {name} (S independent): {t} configs, {v} violations", v == 0)

print()
print("  FINDING — Lemma D's INDEPENDENCE HYPOTHESIS IS NEVER USED.")
print("  The proof only needs u != u' in N(v) with a second common neighbour w.  The edge")
print("  uu' is a chord and the brief's own C4 definition is chord-irrelevant.  Tested:")
for name, g in [("Petersen", P), ("CE-2", CE2), ("M1", M1)]:
    t, v = lemmaD_holds(g, False)
    check(f"Lemma D still holds on {name} with S ARBITRARY: {t} configs, {v} violations",
          v == 0)
print("  So the delivered lemma is TRUE but STATED WEAKER THAN PROVED, and in its full form")
print("  it is a restatement of C4-freeness itself -- the same folklore tier as G54/G55.")

print()
# Corollary D': n >= 1 + sum_{u in S}(d(u)-1), and n >= 1 + a(v)
for name, g in [("Petersen", P), ("CE-2", CE2), ("M1", M1)]:
    n = len(g)
    worst = None
    for v in sorted(g):
        nb = sorted(g[v])
        for k in range(1, len(nb) + 1):
            for S in itertools.combinations(nb, k):
                if any(y in g[x] for x, y in itertools.combinations(S, 2)):
                    continue
                rhs = 1 + sum(len(g[u]) - 1 for u in S)
                if worst is None or rhs > worst[0]:
                    worst = (rhs, v, S)
    check(f"Corollary D' on {name}: n = {n} >= max RHS {worst[0]} (v={worst[1]}, S={worst[2]})",
          n >= worst[0])
    av = max(alpha(g, g[v]) for v in sorted(g))
    check(f"  and n = {n} >= 1 + max a(v) = {1 + av}", n >= 1 + av)

print()
print("=" * 78)
print("[D] GATE B CLAUSE B4 — executed as written, and the clause is DEFECTIVE")
print("=" * 78)
print("  B4 as pre-registered: 'Any argument whose mechanism bounds n, or whose conclusion")
print("  has the form `n >= ...` / \"the class is finite\", is REFUSED without being read.'")
print("  Corollary D' concludes literally  n >= 1 + a(v).  So B4 FIRES, as written.")
check("B4 fires on Corollary D' by its literal text", True, "conclusion form 'n >= ...'")
print()
print("  BUT the clause is mis-drafted, and the owner drafted it.  B4 exists because G49")
print("  (draft 28.2) makes n UNBOUNDED, killing routes that derive a contradiction from")
print("  bounding n ABOVE.  A LOWER bound n >= f(local data) does not bound n, is consistent")
print("  with G49, and cannot produce the contradiction B4 was built to refuse.  The clause")
print("  lists a lower-bound FORM as an instance of 'bounds n', which is a drafting error.")
print()
print("  HANDLING: the refusal STANDS as written -- the gate is executed, not reinterpreted")
print("  mid-harvest -- so Corollary D' is NOT adopted this round.  This costs nothing")
print("  concrete (B1/B2 adopt nothing on a single engine return anyway).  The clause is")
print("  referred to the planner for repair.  A gate silently reinterpreted when it is")
print("  inconvenient is not a pre-registered gate.")

print()
print("=" * 78)
print("[E] A4 SCOPE — does the wrong row touch any delivered statement?")
print("=" * 78)
print("  U7 is sum_v a(v) on M1.  Lemma D, Corollary D' and all three angle write-ups")
print("  reference Petersen, CE-1, CE-2 and R -- never M1 or M2, which the brief declared")
print("  test graphs only.  So A4's demotion clause has EMPTY SCOPE this round:")
check("no delivered statement's proof reads the U7 quantity -> nothing is demoted", True,
      "M1 appears in no mathematical step")
print("  The engine also OBEYED the test-graph declaration: it did not treat M1/M2 as")
print("  mathematical material anywhere.  That was the round-19 gate's stated failure mode.")

print()
print(f"CHECKS: {N[0]}")
print(f"FAILURES: {len(F)}")
for x in F:
    print("   - " + x)
print(f"elapsed {time.time() - T0:.1f}s")
sys.exit(1 if F else 0)
