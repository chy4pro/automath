# CODEX TICKET (sol tier, mathematics, MINIMUM 2 h) — SECOND ATTACKER on X_6 existence, from
# the counting / orbit-window angle (a parallel ticket works the equational propagation
# angle; do NOT coordinate — independent attempts are the point).
# Repo: $HOME/workspace/claudecode/automath. English. No internet. Pure Python only.
# Read first: engine/out/codex/etp677_pattern_existence_report.md ("Exact remaining
# collision problem"), problems/etp677/ext/fibre3/pattern/notes.md, and the Lean file
# lean/etp677_ext/Ext677Pattern.lean (what is already certified: F = L_x^{-4} and
# H = (xx)((xx)x) inverse permutations under E255; no exact L-cycles of length 2, 3, 5;
# the coincidences u*a = a, v*b = b, p*a = b, a*d = b, b*c = b, d*v = a).

## The statement
B finite E677 magma, E255 holds, no idempotents. For a ∈ B: u = (aa)a, p = a\u, b = a\p,
d = bb, v = db, c = bv, w = au. Windows: (a,w,u,p,b,d) = (a_0,…,a_5) along the L_a-orbit
(a_{k+1} = a_k * a? — check the report: w = au, u = (aa)a … the report indexes the
L-cycle of a as a_i and the L-cycle of b as b_j with d = b_{-1}, b = b_0, c = b_1, v = b_2).
CLAIM to prove: some a satisfies X_6(a) := [v≠w, v≠u, c≠a, c≠w, c≠u, c≠p].

## Angle for this ticket
 A1 The two windows are pieces of two L-cycles (of a and of b = F(a), the inverse-map
    lemma): within each window the elements are distinct (cycle length ≥ 6 by the cycle
    facts). The six bad identifications are cross-window coincidences between the
    L_a-orbit window and the L_b-orbit window. Think of the map a ↦ b = F(a) = L_a^{-4}(a)
    (a permutation) and its "window shift": show that if EVERY a has a cross-window
    coincidence, then summing over a (or following the permutation F around a cycle) gives
    an impossible count — e.g. each coincidence type i forces a specific equation between
    F-iterates or L-powers; count how many a can satisfy each type using the fact that
    L_x are permutations and F, H are permutations (each type's solution set is the
    fixed-point set of some explicit permutation built from L's and F; a permutation
    without fixed points … ).
 A2 Compute, on the benchmark magmas with idempotents (m77D, m385canon, M9, F7 models,
    the order-13 table), for each non-idempotent a WHICH of the six coincidences hold and
    what the corresponding elements are (the report says the profiles are (u=v, p=c),
    (c=w), (c=u)); find the structural reason each profile occurs (an idempotent nearby?
    e.g. is c = w equivalent to some element on the windows being idempotent, or being
    the left unit of another?). If every violation type forces an idempotent somewhere on
    the two windows — or forces a short cycle — you are done. Test that hypothesis
    exhaustively on the benchmarks (every violating a: exhibit the idempotent/short cycle
    it produces).
 A3 Refutation attempt: try to build, by pure-Python backtracking on a small carrier
    (n ≤ 15), a table satisfying E677 + E255 + no idempotent in which every a violates X_6
    — or prove that the constraints already contradict at n ≤ 15 (report the search
    scope honestly; ≤ 10 min CPU).

## Deliverables
`problems/etp677/ext/fibre3/pattern/x6b/{notes.md, scripts, outputs}` and
`engine/out/codex/etp677_X6_existence2_report.md` ending with DONE-X6B. Labels PROVED /
VERIFIED-ON-MODELS / CONJECTURED; benchmark output for every claimed identity; do not stop
before 2 h.
