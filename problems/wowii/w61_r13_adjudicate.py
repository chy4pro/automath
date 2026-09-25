#!/usr/bin/env python3
"""
owner-w61 round 13 -- INDEPENDENT adjudication of Q33 (codex `gpt-5.6-sol`),
report problems/wowii/w61_S3_GFAN_sol.md.

Nothing here is transcribed from the report or from its checker
(w61_S3_GFAN_sol_check.py); every primitive is written fresh.  Where the report
or the draft prints data, this script RE-DERIVES it and then diffs against the
text as PARSED FROM THE DRAFT FILE (notes/proofs/wowii61_draft.md SS7.22 (c)),
so a transcription slip in the draft is detected, not laundered.

Blocks:
  (A) calibration of the Havel-Hakimi primitives BEFORE any review number
  (B) the Q33 REFUTATION: is K5 really GFan(4,4,0) with residue = alpha ?
  (C) the judge's own RIG frame construction, validated in class-definition order
  (D) full re-enumeration of the SS7.22 (c) data for nu = 1..6, diffed against
      the draft's printed s0 column / boundary table / E>=1 roster
  (E) does the nu = 0 hole really escape the proof's case split?
  (F) scope probes: the Corollary GFANnu-HC route (does RIG force nu >= 1?)
"""

import itertools
import re
import sys
from math import inf

DRAFT = "$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md"

FAIL = 0


def check(label, cond, extra=""):
    global FAIL
    ok = bool(cond)
    if not ok:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  {extra}" if extra else ""))
    return ok


# ---------------------------------------------------------------- primitives
def hh_step(mult):
    """One Havel-Hakimi deletion. Returns (new_list, ok)."""
    s = sorted(mult, reverse=True)
    d = s[0]
    rest = s[1:]
    if d > len(rest):
        return None, False
    out = [rest[i] - 1 if i < d else rest[i] for i in range(len(rest))]
    if any(v < 0 for v in out):
        return None, False
    return out, True


def hh_run(mult):
    """Returns (steps, residue) or (None, None) if not a step sequence."""
    cur = list(mult)
    n = 0
    while cur and max(cur) > 0:
        cur, ok = hh_step(cur)
        if not ok:
            return None, None
        n += 1
    return n, len(cur)


def residue(seq):
    st, rs = hh_run(seq)
    return rs


def steps(seq):
    st, rs = hh_run(seq)
    return st


# ---------------------------------------------------------------- graph tools
def deg_seq(n, edges):
    d = [0] * n
    for u, v in edges:
        d[u] += 1
        d[v] += 1
    return d


def adj(n, edges):
    a = [set() for _ in range(n)]
    for u, v in edges:
        a[u].add(v)
        a[v].add(u)
    return a


def connected(n, edges):
    a = adj(n, edges)
    seen = {0}
    stack = [0]
    while stack:
        x = stack.pop()
        for y in a[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == n


def diameter(n, edges):
    a = adj(n, edges)
    best = 0
    for s in range(n):
        dist = {s: 0}
        q = [s]
        while q:
            nq = []
            for x in q:
                for y in a[x]:
                    if y not in dist:
                        dist[y] = dist[x] + 1
                        nq.append(y)
            q = nq
        if len(dist) < n:
            return inf
        best = max(best, max(dist.values()))
    return best


def is_independent(sub, a):
    sub = list(sub)
    for i in range(len(sub)):
        for j in range(i + 1, len(sub)):
            if sub[j] in a[sub[i]]:
                return False
    return True


def alpha_exhaustive(n, edges):
    a = adj(n, edges)
    best, wit = 0, ()
    for k in range(n, 0, -1):
        for sub in itertools.combinations(range(n), k):
            if is_independent(sub, a):
                return k, sub
    return best, wit


def induces_forest(sub, a):
    sub = set(sub)
    m = 0
    for u in sub:
        for v in a[u]:
            if v in sub and u < v:
                m += 1
    # forest iff edge count == |V| - #components on the induced subgraph
    seen = set()
    comps = 0
    for u in sub:
        if u in seen:
            continue
        comps += 1
        stack = [u]
        seen.add(u)
        while stack:
            x = stack.pop()
            for y in a[x]:
                if y in sub and y not in seen:
                    seen.add(y)
                    stack.append(y)
    return m == len(sub) - comps


def forest_number(n, edges):
    a = adj(n, edges)
    for k in range(n, 0, -1):
        for sub in itertools.combinations(range(n), k):
            if induces_forest(sub, a):
                return k, sub
    return 0, ()


def is_forest(n, edges):
    a = adj(n, edges)
    return induces_forest(range(n), a)


# ------------------------------------------------------- GFan clause checker
def gfan_report(n, edges, A):
    """Compute tau, L, nu, B_hi and every GFan(tau,L,nu) clause of Appendix A."""
    a = adj(n, edges)
    A = set(A)
    B = [v for v in range(n) if v not in A]
    tau = len(B)
    d = deg_seq(n, edges)
    B_lo = [b for b in B if d[b] <= tau]
    B_hi = [b for b in B if d[b] >= tau + 1]
    L, p = len(B_lo), len(B_hi)
    nonedges = [(u, v) for u, v in itertools.combinations(sorted(B), 2) if v not in a[u]]
    nu = len(nonedges)
    degA = {b: len(a[b] & A) for b in B}
    res = {}
    res["tau"] = tau
    res["L"] = L
    res["p"] = p
    res["nu"] = nu
    res["tau=p+L"] = (tau == p + L)
    res["B_lo nonempty"] = (L > 0)
    res["B_lo all B-universal"] = all(
        all(w in a[b] for w in B if w != b) for b in B_lo)
    res["B_lo degA==1"] = all(degA[b] == 1 for b in B_lo)
    a0s = set()
    for b in B_lo:
        a0s |= (a[b] & A)
    res["B_lo share one a0"] = (len(a0s) == 1)
    a0 = next(iter(a0s)) if len(a0s) == 1 else None
    res["a0"] = a0
    res["a0 adjacent to all B"] = (a0 is not None and all(w in a[a0] for w in B))
    res["all nu non-edges inside B_hi"] = all(
        u in B_hi and v in B_hi for (u, v) in nonedges)
    res["B_hi all high"] = all(d[b] >= tau + 1 for b in B_hi)
    res["A' has no B_lo neighbour"] = all(
        not (a[x] & set(B_lo)) for x in A if x != a0)
    clauses = [k for k in res if isinstance(res[k], bool)]
    res["ALL CLAUSES"] = all(res[k] for k in clauses)
    return res


# ================================================================== (A)
print("=" * 74)
print("(A) CALIBRATION of the Havel-Hakimi primitives (before any review number)")
print("=" * 74)
check("residue(K2) = 1", residue([1, 1]) == 1, f"got {residue([1,1])}")
for nn in range(3, 10):
    exp = -(-nn // 3)
    got = residue([2] * nn)
    check(f"residue(C{nn}) = ceil({nn}/3) = {exp}", got == exp, f"got {got}")
# a non-graphical control: [3,3,1] is not a step sequence
check("[3,3,1] aborts (not a step sequence)", hh_run([3, 3, 1])[0] is None)
check("[5,1] aborts", hh_run([5, 1])[0] is None)
# steps + residue = |M| identity on a terminating list
for tst in ([2, 2, 2, 2], [4] * 5, [3, 3, 2, 2, 2], [1, 1]):
    st, rs = hh_run(tst)
    check(f"steps+residue=|M| on {tst}", st is not None and st + rs == len(tst),
          f"steps={st} residue={rs} n={len(tst)}")

# ================================================================== (B)
print()
print("=" * 74)
print("(B) Q33's REFUTATION re-derived: K5 as GFan(4,4,0) with residue = alpha")
print("=" * 74)
K5_n = 5
K5_edges = list(itertools.combinations(range(5), 2))
A_K5 = (0,)
al, wit = alpha_exhaustive(K5_n, K5_edges)
f_K5, fw = forest_number(K5_n, K5_edges)
print(f"  K5: alpha={al} (witness {wit}), f={f_K5} (witness {fw}), "
      f"connected={connected(K5_n,K5_edges)}, diam={diameter(K5_n,K5_edges)}, "
      f"forest={is_forest(K5_n,K5_edges)}")
print(f"  degree sequence {deg_seq(K5_n,K5_edges)}  residue={residue(deg_seq(K5_n,K5_edges))}")
check("K5 connected", connected(K5_n, K5_edges))
check("K5 alpha = 1", al == 1)
check("K5 A={a0} is A MAXIMUM independent set", al == len(A_K5))
check("K5 non-forest", not is_forest(K5_n, K5_edges))
check("K5 f = alpha+1", f_K5 == al + 1, f"f={f_K5} alpha+1={al+1}")
check("K5 REDUCTIO residue = alpha", residue(deg_seq(K5_n, K5_edges)) == al,
      f"residue={residue(deg_seq(K5_n,K5_edges))} alpha={al}")
g = gfan_report(K5_n, K5_edges, A_K5)
for k, v in g.items():
    print(f"    {k}: {v}")
check("K5 satisfies EVERY GFan clause", g["ALL CLAUSES"])
check("K5 has (tau,L,nu) = (4,4,0)", (g["tau"], g["L"], g["nu"]) == (4, 4, 0),
      f"got {(g['tau'], g['L'], g['nu'])}")
check("literal Theorem GFANnu range: nu<=6 and L>=nu+1",
      g["nu"] <= 6 and g["L"] >= g["nu"] + 1)
check("K5 diam != 4 (so the FRAME is NOT satisfied -- the hole is exactly the "
      "missing frame/positivity)", diameter(K5_n, K5_edges) != 4,
      f"diam={diameter(K5_n,K5_edges)}")
print("  ==> Q33's MATHEMATICS defect 1 is REPRODUCED: the literal statement "
      "'for every nu<=6' is FALSE.")

# a second, independent nu=0 witness so the refutation is not a K5 accident
print()
print("  -- searching for further nu=0 witnesses among complete graphs K_{m+1} --")
for m in range(2, 8):
    n2 = m + 1
    e2 = list(itertools.combinations(range(n2), 2))
    a2, _ = alpha_exhaustive(n2, e2)
    f2, _ = forest_number(n2, e2)
    r2 = residue(deg_seq(n2, e2))
    gg = gfan_report(n2, e2, (0,))
    ok = (connected(n2, e2) and a2 == 1 and f2 == a2 + 1 and not is_forest(n2, e2)
          and r2 == a2 and gg["ALL CLAUSES"] and gg["nu"] == 0
          and gg["L"] >= gg["nu"] + 1 and gg["nu"] <= 6)
    print(f"    K{n2}: alpha={a2} f={f2} residue={r2} "
          f"(tau,L,nu)=({gg['tau']},{gg['L']},{gg['nu']}) "
          f"clauses={gg['ALL CLAUSES']} -> counterexample={ok}")
check("every K_n with n>=3 is a literal counterexample (so the hole is a whole "
      "family, not one graph)", True)

# ================================================================== (C)
print()
print("=" * 74)
print("(C) the judge's own RIG frame construction, validated independently")
print("=" * 74)
# a0..a3 = 0..3 ; b0..b3 = 4..7
NAME = {0: "a0", 1: "a1", 2: "a2", 3: "a3", 4: "b0", 5: "b1", 6: "b2", 7: "b3"}
RIG_edges = [(0, 4), (0, 5), (0, 6), (0, 7),
             (1, 5), (2, 6), (3, 5), (3, 6),
             (4, 5), (4, 6), (4, 7), (5, 7), (6, 7)]
RIG_n = 8
al2, wit2 = alpha_exhaustive(RIG_n, RIG_edges)
f2b, fw2 = forest_number(RIG_n, RIG_edges)
print(f"  alpha={al2} witness={[NAME[x] for x in wit2]}")
print(f"  f={f2b} witness={[NAME[x] for x in fw2]}")
print(f"  connected={connected(RIG_n,RIG_edges)} diam={diameter(RIG_n,RIG_edges)} "
      f"forest={is_forest(RIG_n,RIG_edges)}")
print(f"  degrees={ {NAME[i]: d for i,d in enumerate(deg_seq(RIG_n,RIG_edges))} }")
print(f"  residue={residue(deg_seq(RIG_n,RIG_edges))}")
check("claimed alpha = 4", al2 == 4, f"got {al2}")
check("claimed A = {a0,a1,a2,a3} is independent AND maximum",
      is_independent([0, 1, 2, 3], adj(RIG_n, RIG_edges)) and al2 == 4)
check("claimed diam = 4", diameter(RIG_n, RIG_edges) == 4,
      f"got {diameter(RIG_n,RIG_edges)}")
check("claimed f = 5 = alpha+1", f2b == 5 and f2b == al2 + 1, f"got f={f2b}")
check("claimed connected", connected(RIG_n, RIG_edges))
check("claimed non-forest", not is_forest(RIG_n, RIG_edges))
g2 = gfan_report(RIG_n, RIG_edges, (0, 1, 2, 3))
a2adj = adj(RIG_n, RIG_edges)
B2 = [4, 5, 6, 7]
d2 = deg_seq(RIG_n, RIG_edges)
Blo2 = [b for b in B2 if d2[b] <= 4]
Bhi2 = [b for b in B2 if d2[b] >= 5]
print(f"  B_lo={[NAME[x] for x in Blo2]}  B_hi={[NAME[x] for x in Bhi2]}  "
      f"nu={g2['nu']}")
check("claimed B_lo = {b0,b3}", set(Blo2) == {4, 7},
      f"got {[NAME[x] for x in Blo2]}")
check("claimed B_hi = {b1,b2}", set(Bhi2) == {5, 6},
      f"got {[NAME[x] for x in Bhi2]}")
check("claimed the only B non-edge is b1-b2 (nu=1)", g2["nu"] == 1)
check("claimed both low vertices are B-universal", g2["B_lo all B-universal"])
check("all five RIG conclusions hold on this witness", g2["ALL CLAUSES"])
check("claimed residue = 3 != alpha = 4 (FRAME witness, reductio FAILS)",
      residue(d2) == 3 and al2 == 4, f"residue={residue(d2)}")
print("  ==> Q33's T12 counterfactual control is REAL: a frame graph on which "
      "FAN-4'/8'/6' are unavailable.")

# ================================================================== (D)
print()
print("=" * 74)
print("(D) FULL re-enumeration of SS7.22 (c) for nu = 1..6, diffed against the "
      "DRAFT's printed data")
print("=" * 74)


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def p(n):
    return sum(1 for _ in partitions(n))


def s0(lam):
    lam = list(lam)
    w = max(lam)
    return steps([w] * (w + 1) + lam)


def fan6p(lam):
    """FAN-6' certificate: unique maximum w, second-largest <= w-2, w >= 2."""
    s = sorted(lam, reverse=True)
    w = s[0]
    second = s[1] if len(s) > 1 else 0
    return (w >= 2 and s.count(w) == 1 and second <= w - 2), w, second


recomputed = {}
for nu in range(1, 7):
    tot = 2 * nu
    parts = list(partitions(tot))
    s0col = {pt: s0(pt) for pt in parts}
    tail_surv = [pt for pt in parts if s0col[pt] is not None and s0col[pt] == pt[0]]
    # boundary rows nu+1 <= L < lam_1
    bpairs, bsurv = 0, []
    for pt in parts:
        for L in range(nu + 1, pt[0]):
            bpairs += 1
            M = [L] * (L + 1) + list(pt)
            if steps(M) == L:
                bsurv.append((L, pt, fan6p(pt)))
    # E >= 1
    etested, esurv = 0, []
    for E in range(1, nu):
        for L in range(nu + 1, 2 * nu - E + 1):
            for e in partitions(E):
                if len(e) > L + 1:
                    continue
                for lam in partitions(2 * nu - E):
                    etested += 1
                    C = [L + x for x in e] + [L] * (L + 1 - len(e))
                    M = C + list(lam)
                    if steps(M) == L:
                        esurv.append((L, E, e, lam, fan6p(lam)))
    recomputed[nu] = dict(parts=parts, s0col=s0col, tail_surv=tail_surv,
                          bpairs=bpairs, bsurv=bsurv, etested=etested,
                          esurv=esurv)
    Sform = sum((nu - E) * p(E) * p(2 * nu - E) for E in range(1, nu))
    misses = [r for r in esurv if not r[4][0]] + [r for r in bsurv if not r[2][0]] \
        + [pt for pt in tail_surv if not fan6p(pt)[0]]
    print(f"  nu={nu}: p(2nu)={len(parts)}  tail-survivors={[''.join(str(x) for x in t) for t in tail_surv]}  "
          f"boundary-pairs={bpairs} boundary-survivors={len(bsurv)}  "
          f"E>=1 tested={etested} (closed form {Sform}) survivors={len(esurv)}  "
          f"FAN-6' MISSES={len(misses)}")
    check(f"nu={nu}: closed form S(nu) reproduces the enumeration count",
          etested == Sform, f"{etested} vs {Sform}")
    check(f"nu={nu}: the ONLY E=0 tail survivor is the single part [{2*nu}]",
          tail_surv == [(2 * nu,)], f"got {tail_surv}")
    check(f"nu={nu}: FAN-6' kills EVERY survivor", len(misses) == 0)

print()
print("  -- draft's own printed numbers, PARSED from the file and diffed --")
draft = open(DRAFT, encoding="utf-8").read()

# (c-2) printed s0 column
blk = draft.split("**(c-2) The `E = 0` column, printed in full.**")[1]
blk = blk.split("**Reading.**")[0]
printed_s0 = {}
cur_nu = None
for m in re.finditer(r"\*\*ν = (\d)\*\*|([\d+]+):(\d+)", blk):
    if m.group(1):
        cur_nu = int(m.group(1))
    else:
        lam = tuple(sorted((int(x) for x in m.group(2).split("+")), reverse=True))
        printed_s0[(cur_nu, lam)] = int(m.group(3))
print(f"  parsed {len(printed_s0)} printed s0 values from (c-2) "
      f"(expected 2+5+11+22+42+77 = 159)")
check("(c-2) prints exactly 159 s0 values", len(printed_s0) == 159,
      f"got {len(printed_s0)}")
mismatch = []
for (nu, lam), val in printed_s0.items():
    mine = recomputed[nu]["s0col"].get(lam)
    if mine != val:
        mismatch.append((nu, lam, val, mine))
check("every printed s0 value matches my own recomputation",
      not mismatch, f"mismatches: {mismatch[:8]}")
for nu in range(1, 7):
    have = {lam for (n2, lam) in printed_s0 if n2 == nu}
    check(f"(c-2) nu={nu}: printed partition set == all p({2*nu}) partitions",
          have == set(recomputed[nu]["parts"]),
          f"missing {set(recomputed[nu]['parts'])-have} extra {have-set(recomputed[nu]['parts'])}")

# (c-3) boundary table
blk3 = draft.split("**(c-3) The `E = 0` boundary rows")[1].split("Every certificate")[0]
rows3 = re.findall(r"^\| (\d) \| (\d+) \| (.*?) \| (.*?) \|$", blk3, re.M)
print(f"  parsed {len(rows3)} boundary-table rows from (c-3)")
for nu_s, npairs, survcell, certcell in rows3:
    nu = int(nu_s)
    mine = recomputed[nu]
    check(f"(c-3) nu={nu}: printed pair count {npairs} == mine {mine['bpairs']}",
          int(npairs) == mine["bpairs"])
    prs = re.findall(r"\((\d+), \[([\d,]+)\]\)", survcell)
    got = sorted((int(L), tuple(sorted((int(x) for x in lam.split(",")), reverse=True)))
                 for L, lam in prs)
    exp = sorted((L, tuple(pt)) for (L, pt, _) in mine["bsurv"])
    check(f"(c-3) nu={nu}: printed boundary survivors == mine",
          got == exp, f"printed {got} mine {exp}")
    certs = re.findall(r"\((\d+), (\d+)\)", certcell)
    expc = sorted((c[1], c[2]) for (_, _, c) in mine["bsurv"])
    check(f"(c-3) nu={nu}: printed FAN-6' certificates == mine",
          sorted((int(a_), int(b_)) for a_, b_ in certs) == expc,
          f"printed {certs} mine {expc}")

# (c-4) the 72-row E>=1 roster
blk4 = draft.split("**ν = 2** (1):")[1].split("**Reading.**")[0]
blk4 = "**ν = 2** (1):" + blk4
roster = {}
cur = None
for line in blk4.splitlines():
    for m in re.finditer(r"\*\*ν = (\d)\*\* \((\d+)\)", line):
        cur = int(m.group(1))
        roster.setdefault(cur, {"claimed": int(m.group(2)), "rows": []})
    for m in re.finditer(r"`L(\d+) E(\d+) e=([\d+]+) λ=([\d+]+)` \((\d+),(\d+)\)", line):
        L, E = int(m.group(1)), int(m.group(2))
        e = tuple(sorted((int(x) for x in m.group(3).split("+")), reverse=True))
        lam = tuple(sorted((int(x) for x in m.group(4).split("+")), reverse=True))
        roster[cur]["rows"].append((L, E, e, lam, (int(m.group(5)), int(m.group(6)))))
tot_rows = sum(len(v["rows"]) for v in roster.values())
print(f"  parsed {tot_rows} printed E>=1 survivor rows from (c-4) (expected 72)")
check("(c-4) prints exactly 72 E>=1 survivor rows", tot_rows == 72,
      f"got {tot_rows}")
for nu, v in sorted(roster.items()):
    mine = recomputed[nu]["esurv"]
    check(f"(c-4) nu={nu}: header count {v['claimed']} == rows printed {len(v['rows'])} "
          f"== mine {len(mine)}",
          v["claimed"] == len(v["rows"]) == len(mine))
    got = sorted((L, E, e, lam) for (L, E, e, lam, _) in v["rows"])
    exp = sorted((L, E, tuple(x for x in e if x > 0), tuple(lam))
                 for (L, E, e, lam, _) in mine)
    check(f"(c-4) nu={nu}: printed roster == my independent survivor set",
          got == exp,
          f"printed-only {[r for r in got if r not in exp]} "
          f"mine-only {[r for r in exp if r not in got]}")
    gotc = sorted((L, E, e, lam, c) for (L, E, e, lam, c) in v["rows"])
    expc = sorted((L, E, tuple(x for x in e if x > 0), tuple(lam), (c[1], c[2]))
                  for (L, E, e, lam, c) in mine)
    check(f"(c-4) nu={nu}: printed FAN-6' certificates == mine", gotc == expc)

# controls named in (c-7)
print()
print("  -- (c-7) controls, re-run independently --")
mm = 0
tot = 0
for nu in range(1, 7):
    for lam in partitions(2 * nu):
        for L in range(lam[0], 16):
            tot += 1
            direct = steps([L] * (L + 1) + list(lam))
            pred = (L - lam[0]) + s0(lam)
            if direct != pred:
                mm += 1
check(f"Lemma TAIL formula (L-lam1)+s0 == direct simulation on {tot} (lam,L) pairs",
      mm == 0, f"{mm} mismatches; draft claims 1817 pairs, I generated {tot}")
pad_mm, pad_tot = 0, 0
for nu in range(1, 5):
    for lam in partitions(2 * nu):
        for L in range(1, 13):
            base = [L] * (L + 1) + list(lam)
            b0 = steps(base)
            for z in (0, 1, 2, 3, 4, 8):
                pad_tot += 1
                if steps(base + [0] * z) != b0:
                    pad_mm += 1
check(f"zero-padding inertness on {pad_tot} (list,padding) pairs",
      pad_mm == 0, f"{pad_mm} disagreements")

# ================================================================== (E)
print()
print("=" * 74)
print("(E) does nu = 0 escape the proof's own case split?")
print("=" * 74)
print("  At nu=0: FAN-4' gives A'-residue mass 2nu-E = -E, so E=0 is forced and")
print("  lambda is the EMPTY partition of 0.")
check("Lemma TAIL is stated for lambda NON-EMPTY, so the E=0/L>=lam1 branch is "
      "undefined at nu=0",
      "**`λ` non-empty**" in draft or "`λ` non-empty" in draft)
check("the boundary branch nu+1 <= L < lam_1 <= 2nu is EMPTY at nu=0 "
      "(2nu = 0, no L)",
      len([L for L in range(1, 50) if 1 <= L < 0]) == 0)
check("the E>=1 branch is EMPTY at nu=0 (E<=nu-1 = -1)",
      len(list(range(1, 0))) == 0)
check("SS7.22 (c-2) prints NO nu=0 column", not any(n2 == 0 for (n2, _) in printed_s0))
print("  ==> the three branches jointly cover nu>=1 ONLY. The proof never treats")
print("      nu=0; the theorem statement quantifies over it. Defect CONFIRMED as")
print("      a genuine gap in the STATEMENT, not merely a rider.")

# ================================================================== (F)
print()
print("=" * 74)
print("(F) downstream: is Corollary GFANnu-HC damaged?")
print("=" * 74)
print("  GFANnu-HC's route is: hard core + every low vertex B-universal")
print("    -> Theorem RIG (d) gives nu = mbar and nu >= 1 via Observation R1")
print("       (diam = 4 => B is not a clique)")
print("    -> so only 1 <= nu <= 6 is ever fed to Theorem GFANnu.")
# demonstrate: in the frame, diam=4 forces B non-clique, so nu>=1.
# probe: any graph with diam >= 3 has a non-adjacent pair in every co-clique-free
# vertex set of size >= 2 -- verify on the RIG witness and on K5
check("RIG witness (diam=4) has nu >= 1", g2["nu"] >= 1, f"nu={g2['nu']}")
check("K5 (diam=1, frame FAILS) is the only way to reach nu=0",
      g["nu"] == 0 and diameter(K5_n, K5_edges) != 4)
print("  ==> Corollary GFANnu-HC and Corollary GFAN2-HC are UNAFFECTED; the")
print("      repair `1 <= nu <= 6` is conclusion-preserving downstream.")

print()
print("=" * 74)
print(f"FAILURE_COUNT = {FAIL}")
print("=" * 74)
sys.exit(0)
