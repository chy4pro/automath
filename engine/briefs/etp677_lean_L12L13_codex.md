# CODEX TICKET (sol tier, Lean 4 + Mathlib) — L12 inverse-map lemma + no-5-cycle, L13 the
# automatic pattern coincidences. Repo: $HOME/workspace/claudecode/automath; project
# lean/etp677_ext/ (reuse Ext677.lean: E677, E255, E255At, ldiv, key_identity, L1). English.
# lake build only. Time box 2.5 h. Source of the informal proofs:
# engine/out/codex/etp677_pattern_existence_report.md (sections "Which coincidences are
# automatic", "New inverse-map lemma") and problems/etp677/ext/fibre3/pattern/notes.md.

## L12 (finite E677 magma with E255)
 (a) `F x := ldiv x (ldiv x (ldiv x (ldiv x x)))` (= L_x^{-4} x) and `H x := op (op x x) (op (op x x) x)`
     satisfy `F (H x) = x` and `H (F x) = x` for all x (prove F∘H = id from KEY + E255 as in
     the report — with s = xx, q = (xx)x: qx = x by E255, KEY gives (sq)s = q\(s\q) = q\x = x,
     so xx = h\x with h = H x; then the "unique z with zz = h\z is F h" step must be PROVED
     (the report cites a structural Theorem 3 — derive it: from zz = h\z get h(zz) = z, and
     with E677/KEY show z = L_h^{-4}(h)); finiteness gives the other composite).
 (b) Cycle restriction: for the L_x-cycle through x (define `Lpow x k := (op x)^[k] x`),
     E255 excludes `Lpow x 5 = x ∧ (∀ k < 5, 0 < k → Lpow x k ≠ x)` (no cycle of exact
     length 5). Also formalize the toolkit's (Cyc): no cycle of exact length 2 or 3 (E677
     alone; the toolkit records it as proved — reprove).
## L13 (finite E677 + E255, any a; the eight terms)
 With u = (aa)a, p = a\u, b = a\p, d = bb, v = db, c = bv, w = au (ldiv for \): prove
 `u*a = a`, `v*b = b`, `p*a = b`, `a*d = b`, `b*c = b`, `d*v = a` (the last via L12(a):
 b = F a and H b = d*v). State each as a separate theorem.
## L14 (optional) the disequality package: under idempotent-freeness (∀ x, op x x ≠ x) prove
 the "automatic" distinctness claims of the report: a ≠ u, a ≠ p, …, i.e. that the eight
 terms are pairwise distinct IFF the six X_6 disequalities hold (prove the "automatic"
 direction: each of the other 22 inequalities follows from E677 + E255 + idempotent-free +
 the cycle facts). Deliver what you can; list what remains.

## Deliverables
`lean/etp677_ext/Ext677Pattern.lean` (library root), `lake build` clean, `#print axioms`
appended to AXIOMS.txt (propext / Classical.choice / Quot.sound only), and
`engine/out/codex/etp677_lean_L12L13_report.md` with exact statements, deviations, build
tail, ending with DONE-LEANPAT.
