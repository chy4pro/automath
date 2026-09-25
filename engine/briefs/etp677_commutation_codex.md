# CODEX TICKET (sol tier, mathematics, MINIMUM 2 h) — the COMMUTATION LEMMAS behind X_6:
# prove F∘U = U∘F and F∘W = W∘F (and F∘P = P∘F) in every finite E677+E255 magma.
# Repo: $HOME/workspace/claudecode/automath. English. No internet. Pure Python only
# (benchmarks: problems/etp677/R8_invariants.py loaders; the audits in
# problems/etp677/ext/fibre3/pattern/x6b/scripts/orbit_window_audit.py).
# Read first: engine/out/codex/etp677_X6_existence2_report.md and x6b/notes.md.

## Definitions (finite E677 magma with E255; L_x(z) = x*z is a permutation)
  U(x) = (xx)x = L_x^{-2}(x)      [toolkit: (xx)x = x\(x\x), Lean diagonal_candidate]
  W(x) = x*U(x) = L_x^{-1}(x)     [since x*(x\ (x\x)) = x\x]
  P(x) = x \ U(x) = L_x^{-3}(x)
  F(x) = L_x^{-4}(x)              [Lean L12F; F is a permutation, inverse H(x) = (xx)((xx)x)]
So U, W, P, F are the iterates L_x^{-2}, L_x^{-1}, L_x^{-3}, L_x^{-4} applied to x ITSELF
(each element walks its own L-cycle backwards). Certified facts: no exact L-cycle of
length 2, 3, 5 (Lean), and 4 (toolkit (Cyc): a 4-cycle forces E255 to fail at that
element — under E255 excluded); F(x) = x ⟺ x idempotent (x6b, proved from the cycle facts).
VERIFIED ON 21 MODELS (x6b): F∘U = U∘F, F∘W = W∘F, F∘P = P∘F, with zero failures.

## Why it matters
With FU = UF: v = U(F(a)) = U(a) = u would give F(U(a)) = U(a), so U(a) idempotent —
impossible in an idempotent-free magma; hence v ≠ u. With FW = WF: c = W(F(a)) = W(a) = w
gives W(a) idempotent — hence c ≠ w. Two of the five X_5 conditions then hold for EVERY a
in an idempotent-free E677+E255 magma. (The remaining three — v ≠ w, c ≠ u, c ≠ p — have
model-verified idempotent witnesses a, d, u; see the x6b table.)

## Task
 T1 Prove F(U(x)) = U(F(x)) from E677 + E255. Concretely: let y = U(x) = L_x^{-2}(x), so
    x*(x*y) = x. Want L_y^{-4}(y) = U(F(x)) = L_{F(x)}^{-2}(F(x)). Use KEY (y*x)*y = x\(y\x)
    (Lean key_identity), the inverse-map lemma (F∘H = id: x = F(H(x)) with H(x) = (xx)((xx)x)),
    and the "master division" identity (Lean e677_master_division in Ext677Pattern.lean —
    read it). Work with the ELEMENTS of the L_x-cycle: x, x1 = xx, x2 = x x1, … and
    express U(x), W(x), P(x), F(x) as x_{m−2}, x_{m−1}, x_{m−3}, x_{m−4} (m = cycle length).
    The claim FU = UF relates the L_x-cycle to the L_{U(x)}-cycle — find the KEY-derived
    map between them (the R7-C unique-witness formula and the T1' singleton {w : x*w = x}
    = {L_x^{-1}(x)} = {W(x)} may help: W(x) is the unique right unit of x).
 T2 Same for F∘W = W∘F and F∘P = P∘F.
 T3 Then the two closed cases (v ≠ u, c ≠ w) as corollaries, stated for idempotent-free
    E677+E255 magmas.
 T4 The other three: is v = w (i.e. U(F(a)) = W(a)) forced to make a idempotent? is
    c = u (W(F(a)) = U(a)) forced to make d = bb idempotent? is c = p (W(F(a)) = P(a))
    forced to make u idempotent? Try to derive each from the commutations + KEY.
 Test every intermediate identity on the benchmark set FIRST (m77D, m385canon, m176, m496,
 M9, F7 models, F31, the db tables) and print the outputs; a claim failing on any E677+E255
 model is dead.

## Deliverables
`problems/etp677/ext/fibre3/pattern/comm/{notes.md, scripts, outputs}` and
`engine/out/codex/etp677_commutation_report.md` ending with DONE-COMM. Labels PROVED /
VERIFIED-ON-MODELS / CONJECTURED. If T1 is PROVED, write the derivation so that it can be
formalized (each step an equation with its justification). Do not stop before 2 h.
