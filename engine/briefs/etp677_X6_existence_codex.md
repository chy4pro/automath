# CODEX TICKET (sol tier, mathematics, MINIMUM 2 h) — the last step to a fibre-3 theorem for
# minimal counterexamples: prove that every idempotent-free finite E677+E255 magma has an
# element a with X_6(a). Repo: $HOME/workspace/claudecode/automath. English. No
# internet. Pure Python only (benchmarks via problems/etp677/R8_invariants.py loaders; the
# pattern scripts problems/etp677/ext/fibre3/pattern/scripts/).
# Read first: engine/out/codex/etp677_pattern_existence_report.md and
# problems/etp677/ext/fibre3/pattern/notes.md (the exact remaining collision problem).

## Setting (PROVED, R46 STEP 15–16)
B finite E677 magma, E255 holds on B (it is the quotient of a minimal counterexample, L8/L9),
B idempotent-free (class size 3 forces it, L11). For a ∈ B put
   u = (aa)a, p = a\u, b = a\p, d = bb, v = db, c = bv, w = au.
Automatic under E677+E255: ua = a, vb = b, pa = b, ad = b, bc = b, dv = a (the last via the
inverse-map lemma F(x) = L_x^{-4}(x), H(x) = (xx)((xx)x), F∘H = H∘F = id). The eight terms
form an injective typed copy of the pattern P* iff
   X_6(a):  v ≠ w, v ≠ u, c ≠ a, c ≠ w, c ≠ u, c ≠ p,
and then (shape-only Core-7 theorem) B admits no pair-indexed extension with a 3-element
fibre. Known cycle facts: the L_a-cycle length m(a) is never 2, 3, 4 (toolkit (Cyc)), never
5 (new, under E255), never 1 (idempotent-free). F31 (5x−4y+c): X_6 holds for ALL 31 a.

## Task
Prove: in every idempotent-free finite E677+E255 magma some a satisfies X_6(a). Routes:
 R1 Suppose every a violates X_6. Each violation is an equation between two of the eight
    terms; there are six kinds. Show a violation at a propagates (via E677/KEY and the
    automatic identities) to structural consequences — e.g. c = a means bv = a, i.e. …;
    v = u means db = (aa)a; c = p means bv = a\u — and derive from "for ALL a some
    violation" a contradiction with finiteness/left-cancellation (count orbits of the
    permutations F, H, L_a; use that a ↦ u = (aa)a is the left-unit map, which has no
    fixed point in an idempotent-free magma, and its inverse H∘… structure).
 R2 Each violation kind defines a subset V_i ⊆ B; you need ∪ V_i ≠ B. Bound |V_i|: e.g.
    show each V_i is the fixed-point set of a fixed-point-free-ish permutation composed
    of L's, or is in bijection with a set of "bad" a whose L_a-cycle has a forced length.
    Compute |V_i| on the benchmark magmas WITH idempotents (m77D, m385canon, M9, F7, F13,
    order-13 db table: report per kind which a violate which disequality) — these are the
    negative controls the report mentioned (u = v, p = c; c = w; c = u).
 R3 If a proof does not close: give the smallest hypothetical structure (a partial
    multiplication table on the eight terms + their L-cycles, n ≤ 20) in which every a
    violates X_6 while every finite consequence of E677+E255 you can check locally holds;
    state exactly what global fact is missing.
Every claimed identity must be tested on the benchmark set before use (pattern_audit.py
shows how the terms are computed); label PROVED / VERIFIED-ON-MODELS / CONJECTURED.

## Deliverables
`problems/etp677/ext/fibre3/pattern/x6/{notes.md, scripts, outputs}` and
`engine/out/codex/etp677_X6_existence_report.md` ending with DONE-X6. If proved, state the
resulting THEOREM verbatim: "no minimal counterexample to 677→255 has a congruence all of
whose classes have size 3". Do not stop before 2 h.
