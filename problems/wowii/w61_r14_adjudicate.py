#!/usr/bin/env python3
"""owner-w61 round 14 — INDEPENDENT reproduction harness for the Q34 adjudication.

Written from the SPECIFICATION ONLY (draft section 7.13 / the (C-1)..(C-5) conventions
now printed in prompts/w61_S3_GFAN_r14.md).  Nothing here is transcribed from any
engine report, from any engine's checker, or from the round-13 harness: the
Havel-Hakimi step routine, the partition generator, the alpha / forest-number
routines, the GFan clause checker and the FAN-6' predicate are all re-written.

Where the DRAFT prints data, this script parses the draft file and diffs against its
own recomputation, so a transcription slip in my own text surfaces rather than being
laundered.

Sections
  0  calibration (must print before any review number)
  1  (C-2) the E = 0 column: s0(lambda) for every partition of 2nu, nu <= 6
  2  (C-3) the boundary rows nu+1 <= L < lambda_1
  3  (C-4) the E >= 1 enumeration, by simulation and by closed form
  4  Lemma TAIL: formula vs direct simulation
  5  zero-padding inertness at full scope
  6  graph-level witness checker (alpha, f, diam, residue, GFan clauses) — used to
     re-verify any graph a judge constructs, and re-run on K_n as a standing control
"""
import itertools
import pathlib
import re
import sys

FAIL = 0


def check(label, got, want):
    global FAIL
    ok = got == want
    if not ok:
        FAIL += 1
    print(f"  [{'ok ' if ok else 'FAIL'}] {label}: got {got!r}" + ("" if ok else f" want {want!r}"))
    return ok


# ---------------------------------------------------------------- HH primitives
def hh_steps(values):
    """Number of head-deletions to reach all-zeros, or None if the run aborts.

    One step: sort non-increasingly, delete the largest entry d, subtract 1 from the
    next d entries.  Aborts if d exceeds the number of remaining entries, or if any
    entry that must be decremented is already 0 (it would go negative).
    """
    cur = sorted((v for v in values), reverse=True)
    n = 0
    while cur and cur[0] != 0:
        d = cur[0]
        rest = cur[1:]
        if d > len(rest):
            return None
        if any(x == 0 for x in rest[:d]):
            return None
        rest = [x - 1 for x in rest[:d]] + rest[d:]
        cur = sorted(rest, reverse=True)
        n += 1
    return n


def hh_residue(degrees):
    """Havel-Hakimi residue: number of zeros left when the largest entry is 0."""
    cur = sorted(degrees, reverse=True)
    while cur and cur[0] != 0:
        d = cur[0]
        rest = cur[1:]
        if d > len(rest):
            return None
        rest = [x - 1 for x in rest[:d]] + rest[d:]
        if any(x < 0 for x in rest):
            return None
        cur = sorted(rest, reverse=True)
    return len(cur)


def partitions(n, cap=None):
    """All partitions of n as non-increasing tuples."""
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def p(n):
    return sum(1 for _ in partitions(n))


def partitions_at_most_k_parts(n, k):
    return [lam for lam in partitions(n) if len(lam) <= k]


# ------------------------------------------------------------ the two predicates
def s0(lam):
    """s0(lambda) := steps([lam1]^{lam1+1} ∪ lambda)."""
    w = lam[0]
    return hh_steps([w] * (w + 1) + list(lam))


def fan6p_kills(lam):
    """Lemma FAN-6' predicate: unique maximum w >= 2, second-largest <= w-2.

    Convention (ii) of the lemma: a residue with a single positive part is read as
    having second-largest 0 whether or not a real zero entry is present.
    """
    if not lam:
        return False, None
    w = lam[0]
    second = lam[1] if len(lam) > 1 else 0
    return (w >= 2 and second <= w - 2), (w, second)


def clears_in(L, cpart, lam):
    """Does [c-part] ∪ lambda clear in exactly L steps?"""
    return hh_steps(list(cpart) + list(lam)) == L


# =============================================================== 0  CALIBRATION
print("=" * 72)
print("SECTION 0 — CALIBRATION (printed before any review number)")
print("=" * 72)
check("residue(K2) [degrees 1,1]", hh_residue([1, 1]), 1)
for n in range(3, 10):
    check(f"residue(C{n}) [degrees 2^{n}]", hh_residue([2] * n), -(-n // 3))
check("steps([2,2,2,2])", hh_steps([2, 2, 2, 2]), 2)
check("steps([1,1,1,1])", hh_steps([1, 1, 1, 1]), 2)
check("abort: head exceeds remaining", hh_steps([3, 1, 1]), None)
check("abort: would drive a zero negative", hh_steps([2, 1, 0]), None)
print()

# ================================================ 1  (C-2) the E = 0 s0 column
print("=" * 72)
print("SECTION 1 — (C-2) the E = 0 column: s0(lambda), every partition of 2nu")
print("=" * 72)
s0_table = {}
for nu in range(1, 7):
    lams = list(partitions(2 * nu))
    check(f"nu={nu}: partition count = p({2*nu})", len(lams), p(2 * nu))
    s0_table[nu] = {lam: s0(lam) for lam in lams}
    survivors = sorted(lam for lam, v in s0_table[nu].items() if v == lam[0])
    print(f"    nu={nu}: {len(lams)} partitions, survivors (s0 = lam1) = "
          f"{[list(x) for x in survivors]}")
    check(f"nu={nu}: the ONLY E=0/TAIL-range survivor is [2nu]",
          survivors, [(2 * nu,)])
print()

# ------ diff the s0 column against the draft's own printed data
print("  -- diffing section 1 against the DRAFT's printed (c-2) column --")
draft_path = pathlib.Path("$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md")
draft = draft_path.read_text()
blk = draft[draft.index("**(c-2) The `E = 0` column, printed in full.**"):]
blk = blk[:blk.index("**(c-3)")]
printed = {}
blk_lines = blk.splitlines()
raw_blocks = []
i = 0
while i < len(blk_lines):
    m0 = re.match(r"> \*\*ν = (\d)\*\* — `p\(\d+\) = (\d+)`: (.*)$", blk_lines[i])
    if m0:
        nu_, cnt_, body_ = int(m0.group(1)), int(m0.group(2)), m0.group(3)
        j = i + 1
        while j < len(blk_lines) and blk_lines[j].startswith(">") \
                and not re.match(r"> \*\*ν = \d", blk_lines[j]):
            body_ += " " + blk_lines[j][1:]
            j += 1
        raw_blocks.append((nu_, cnt_, body_))
        i = j
    else:
        i += 1
for nu, cnt, body in raw_blocks:
    body = body.replace("**", "")
    entries = {}
    for item in body.split("·"):
        item = item.strip().strip("`").strip()
        if not item or ":" not in item:
            continue
        lhs, rhs = item.rsplit(":", 1)
        lhs, rhs = lhs.strip(), rhs.strip()
        if not re.fullmatch(r"\d+(\+\d+)*", lhs) or not re.fullmatch(r"\d+", rhs):
            continue
        lam = tuple(sorted((int(x) for x in lhs.split("+")), reverse=True))
        entries[lam] = int(rhs)
    printed[nu] = (cnt, entries)
for nu in range(1, 7):
    if nu not in printed:
        print(f"  [FAIL] draft (c-2) block for nu={nu} not parseable")
        FAIL += 1
        continue
    count, entries = printed[nu]
    check(f"draft nu={nu}: printed p(2nu) header", count, p(2 * nu))
    check(f"draft nu={nu}: printed partition SET equals p(2nu)",
          sorted(entries), sorted(s0_table[nu]))
    mism = {k: (v, s0_table[nu][k]) for k, v in entries.items()
            if k in s0_table[nu] and v != s0_table[nu][k]}
    check(f"draft nu={nu}: printed s0 values vs mine ({len(entries)} values)", mism, {})
print()

# =========================================== 2  (C-3) the boundary rows E = 0
print("=" * 72)
print("SECTION 2 — (C-3) boundary rows  nu+1 <= L < lambda_1 <= 2nu")
print("=" * 72)
bnd_counts, bnd_surv = [], []
for nu in range(1, 7):
    pairs, surv = [], []
    for lam in partitions(2 * nu):
        for L in range(nu + 1, lam[0]):
            pairs.append((L, lam))
            if clears_in(L, [L] * (L + 1), lam):
                surv.append((L, lam))
    bnd_counts.append(len(pairs))
    bnd_surv.append(surv)
    kills = [(L, lam, fan6p_kills(lam)[1]) for (L, lam) in surv]
    misses = [x for x in kills if not fan6p_kills(x[1])[0]]
    print(f"    nu={nu}: {len(pairs)} boundary pairs, {len(surv)} survivors "
          f"{[(L, list(lam)) for L, lam in surv]}, FAN-6' certificates "
          f"{[c for _, _, c in kills]}, FAN-6' MISSES {misses}")
    if misses:
        FAIL += 1
check("boundary pair counts nu=1..6", bnd_counts, [0, 1, 3, 7, 14, 26])
check("boundary survivor counts nu=1..6", [len(s) for s in bnd_surv],
      [0, 1, 1, 2, 2, 3])
check("closed form max(0, lam1-nu-1) reproduces the pair counts",
      [sum(max(0, lam[0] - nu - 1) for lam in partitions(2 * nu))
       for nu in range(1, 7)], [0, 1, 3, 7, 14, 26])
print()

# ================================================= 3  (C-4) the E >= 1 branch
print("=" * 72)
print("SECTION 3 — (C-4) the E >= 1 enumeration")
print("=" * 72)
shape_counts, surv_counts, all_surv = [], [], {}
for nu in range(1, 7):
    shapes = 0
    surv = []
    for E in range(1, nu):                       # FAN-8' + MB1 force E <= nu-1
        for L in range(nu + 1, 2 * nu - E + 1):  # FAN-8': L <= 2nu - E
            for e in partitions_at_most_k_parts(E, L + 1):
                cpart = sorted([L + x for x in e] + [L] * (L + 1 - len(e)),
                               reverse=True)
                for lam in partitions(2 * nu - E):
                    shapes += 1
                    if clears_in(L, cpart, lam):
                        surv.append((E, L, tuple(e), lam))
    shape_counts.append(shapes)
    surv_counts.append(len(surv))
    all_surv[nu] = surv
    misses = [r for r in surv if not fan6p_kills(r[3])[0]]
    print(f"    nu={nu}: {shapes} shapes, {len(surv)} survivors, "
          f"FAN-6' misses = {len(misses)}")
    for (E, L, e, lam) in surv:
        killed, cert = fan6p_kills(lam)
        print(f"        E={E} L={L} e={list(e)} lam={list(lam)} "
              f"FAN-6'{'KILLS' if killed else ' MISSES'} cert={cert}")
    if misses:
        FAIL += 1
check("S(nu) by enumeration", shape_counts, [0, 3, 24, 110, 397, 1211])
check("S(nu) by closed form",
      [sum((nu - E) * p(E) * p(2 * nu - E) for E in range(1, nu))
       for nu in range(1, 7)], [0, 3, 24, 110, 397, 1211])
check("total E>=1 shapes for nu<=6", sum(shape_counts), 1745)
check("E>=1 survivor counts nu=1..6", surv_counts, [0, 1, 4, 9, 20, 38])
check("total E>=1 survivors", sum(surv_counts), 72)
check("FAN-6' misses over ALL surviving rows (E=0 boundary + E>=1 + the six [2nu])",
      sum(1 for nu in range(1, 7)
          for r in all_surv[nu] if not fan6p_kills(r[3])[0])
      + sum(1 for nu in range(1, 7)
            for (L, lam) in bnd_surv[nu - 1] if not fan6p_kills(lam)[0])
      + sum(1 for nu in range(1, 7) if not fan6p_kills((2 * nu,))[0]), 0)
print()

# ============================================ 4  Lemma TAIL: formula vs run
print("=" * 72)
print("SECTION 4 — Lemma TAIL: predicted (L - lam1) + s0(lam) vs direct simulation")
print("=" * 72)
pairs = mismatch = 0
for nu in range(1, 7):
    for lam in partitions(2 * nu):
        for L in range(lam[0], 16):
            pairs += 1
            if hh_steps([L] * (L + 1) + list(lam)) != (L - lam[0]) + s0(lam):
                mismatch += 1
check("Lemma TAIL (lam,L) pairs tested", pairs, 1817)
check("Lemma TAIL mismatches", mismatch, 0)
print()

# =========================================== 5  zero-padding inertness, full scope
print("=" * 72)
print("SECTION 5 — zero-padding inertness at FULL scope (the repaired control)")
print("=" * 72)
PADS = [0, 1, 2, 3, 4, 8, 13]
e0_lists, e1_lists = [], []
for nu in range(1, 7):
    for lam in partitions(2 * nu):
        for L in range(nu + 1, 16):
            e0_lists.append(([L] * (L + 1), lam))
    for E in range(1, nu):
        for L in range(nu + 1, 2 * nu - E + 1):
            for e in partitions_at_most_k_parts(E, L + 1):
                cpart = sorted([L + x for x in e] + [L] * (L + 1 - len(e)),
                               reverse=True)
                for lam in partitions(2 * nu - E):
                    e1_lists.append((cpart, lam))
bad = 0
for cpart, lam in e0_lists + e1_lists:
    base = hh_steps(list(cpart) + list(lam))
    for z in PADS[1:]:
        if hh_steps(list(cpart) + list(lam) + [0] * z) != base:
            bad += 1
print(f"    E=0 lists: {len(e0_lists)} | E>=1 shapes: {len(e1_lists)} | "
      f"paddings: {len(PADS)} | (list,padding) pairs: "
      f"{(len(e0_lists) + len(e1_lists)) * len(PADS)}")
check("E>=1 shape count matches section 3", len(e1_lists), 1745)
check("padding-dependent step counts", bad, 0)
print()

# ================================================== 6  graph-level witness checker
print("=" * 72)
print("SECTION 6 — graph-level witness checker, and the K_n standing control")
print("=" * 72)


class G:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [set() for _ in range(n)]
        for u, v in edges:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def deg(self, v):
        return len(self.adj[v])

    def degseq(self):
        return sorted((self.deg(v) for v in range(self.n)), reverse=True)

    def connected(self):
        seen, stack = {0}, [0]
        while stack:
            x = stack.pop()
            for y in self.adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        return len(seen) == self.n

    def diam(self):
        best = 0
        for s in range(self.n):
            dist = {s: 0}
            q = [s]
            while q:
                nq = []
                for x in q:
                    for y in self.adj[x]:
                        if y not in dist:
                            dist[y] = dist[x] + 1
                            nq.append(y)
                q = nq
            if len(dist) < self.n:
                return None
            best = max(best, max(dist.values()))
        return best

    def is_independent(self, S):
        return all(v not in self.adj[u] for u, v in itertools.combinations(S, 2))

    def induces_forest(self, S):
        S = set(S)
        idx = {v: i for i, v in enumerate(sorted(S))}
        parent = list(range(len(S)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        m = 0
        for u, v in itertools.combinations(sorted(S), 2):
            if v in self.adj[u]:
                m += 1
                ru, rv = find(idx[u]), find(idx[v])
                if ru == rv:
                    return False
                parent[ru] = rv
        return True

    def alpha(self):
        """Exhaustive: largest independent set, plus one witness."""
        for k in range(self.n, 0, -1):
            for S in itertools.combinations(range(self.n), k):
                if self.is_independent(S):
                    return k, S
        return 0, ()

    def forest_number(self):
        for k in range(self.n, 0, -1):
            for S in itertools.combinations(range(self.n), k):
                if self.induces_forest(S):
                    return k, S
        return 0, ()

    def residue(self):
        return hh_residue(self.degseq())


def describe(name, g, A=None):
    a, Aw = g.alpha()
    f, Fw = g.forest_number()
    r = g.residue()
    print(f"    {name}: n={g.n} connected={g.connected()} degseq={g.degseq()} "
          f"diam={g.diam()} alpha={a} (witness {list(Aw)}) f={f} "
          f"non-forest={f < g.n} residue={r} residue==alpha={r == a} "
          f"f==alpha+1={f == a + 1}")
    return dict(alpha=a, f=f, residue=r, diam=g.diam(), conn=g.connected())


# the nu = 0 refutation family, re-verified from scratch as a standing control
for n in range(3, 9):
    kn = G(n, list(itertools.combinations(range(n), 2)))
    d = describe(f"K{n}", kn)
    check(f"K{n}: residue == alpha", d["residue"] == d["alpha"], True)
    check(f"K{n}: f == alpha + 1", d["f"] == d["alpha"] + 1, True)
    check(f"K{n}: alpha == 1", d["alpha"], 1)

print()
# ============================== 7  the two import-dependent identities, re-derived
print("=" * 72)
print("SECTION 7 — FAN-4' and FAN-8': the algebra Q33 could only check conditionally")
print("=" * 72)
print("  FAN-4': dec_A' = [sum_{j<=p} D_j] - C(p,2) - [p(L+1) - E], with")
print("          sum_{j<=p} D_j = sum_{B_hi} deg - C(p,2) = (p*tau - 2nu + R) - C(p,2)")
print("          claim: dec_A' = R - 2nu + E, hence A'-total = R - dec_A' = 2nu - E")
bad4 = bad8 = 0
grid = 0
for pp in range(0, 9):
    for L in range(1, 9):
        tau = pp + L
        for nu in range(0, 8):
            for E in range(0, 8):
                for R in range(0, 12):
                    grid += 1
                    c2 = pp * (pp - 1) // 2
                    sumD = (pp * tau - 2 * nu + R) - c2
                    dec_Ap = sumD - c2 - (pp * (L + 1) - E)
                    if dec_Ap != R - 2 * nu + E:
                        bad4 += 1
                    if (R - dec_Ap) != 2 * nu - E:
                        bad4 += 1
                    # FAN-8': the block-occupancy count, then the value chain
                    for t in range(1, max(pp, 1) + 1):
                        for e_t in range(1, 4):
                            lhs = (tau - t + 2) - (pp - t) - (L + 1) + e_t
                            if lhs != 1 + e_t:
                                bad8 += 1
check("FAN-4' mass identity over the parameter grid", bad4, 0)
check("FAN-8' block-occupancy identity |block_t ∩ A'| >= 1 + e_t", bad8, 0)
print(f"    grid points: {grid}")
print("  FAN-8' value chain, symbolic:")
print("     v_t(c) >= tau-(t-1) = tau-t+1   [c escapes at t, decremented <= t-1 times]")
print("     v_t(x) >= v_t(c)                [block is a prefix, c not in it, x in it]")
print("     v_{p+1}(x) >= v_t(x) - (p-t+1)  [x survives steps t..p, <=1 decrement each]")
print("     v_{p+1}(x) <= 2nu - E           [FAN-4' A'-mass]")
print("     => tau-t+1 <= (2nu-E) + (p-t+1) => tau-p = L <= 2nu-E   QED")
for tau_, pp_, L_, nu_, E_, t_ in [(9, 5, 4, 3, 1, 2), (12, 7, 5, 4, 2, 5), (6, 2, 4, 3, 1, 1)]:
    lo = tau_ - t_ + 1
    hi = (2 * nu_ - E_) + (pp_ - t_ + 1)
    implies = (tau_ - pp_) <= (2 * nu_ - E_)
    print(f"     spot tau={tau_} p={pp_} L={L_} nu={nu_} E={E_} t={t_}: "
          f"{lo} <= {hi} is {lo <= hi}; L<=2nu-E is {implies}; consistent="
          f"{(lo <= hi) == implies or not (lo <= hi)}")
print()

print("=" * 72)
print(f"FAILURE_COUNT = {FAIL}")
print("=" * 72)
sys.exit(1 if FAIL else 0)
