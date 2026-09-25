# CODEX TICKET (Lean 4; math, sol tier) — formalise the R46 window/switching lemmas.
# Repo: $HOME/workspace/claudecode/automath. Project: lean/etp677_ext (Lean 4.34.0-rc1
# + Mathlib path already configured; build with `lake build` inside lean/etp677_ext; existing
# modules Ext677.lean … Ext677X6.lean show the conventions: a magma is `op : M → M → M` with
# hypotheses `E677 : ∀ x y, op y (op x (op (op y x) y)) = x`, `[Finite M]`, left division via the
# bijectivity lemmas already proved there (see Ext677.lean / Ext677X6.lean X1_* / X3_*). Reuse
# them; do NOT re-prove bijectivity. 0 sorry; run `#print axioms` on every new theorem and
# append the lines to lean/etp677_ext/AXIOMS.txt. English only in code.
# Heavy processes: ≤ 2 (lake build). DONE marker: DONE-LEANWIN.

## New module `Ext677Window.lean` — all under E677 (+ E255 where stated), M finite
Notation as in Ext677X6.lean: W x = x\x, U x = (x*x)*x (= x\W x), P x = x\U x, F x = x\P x.
L1 (L-A):  op u x = x → op x u = W x  ∧  U x = u.
    [E677 at (y,x) := (u,x): x = u*(x*((u*x)*u)) = u*(x*(x*u)); cancel L_u (injective) to get
    x*(x*u) = x = x*W x; cancel L_x: x*u = W x; then U x = x\W x = u.]
L2 (E255):  op (U x) x = x   (this is E255 rewritten; state it) and hence
    `Fix(L_u) = U⁻¹(u)`:  op u x = x ↔ U x = u.
L3:  op x (U x) = W x  (from L1 with u := U x and L2).
L4 (c = p ⟺ p² = a): with u = U a, p = P a, b = F a, c = W b:
    c = p ↔ op p p = a.   [E677 at (a,p): a = p*(a*((p*a)*p)); p*a = b (already in
    Ext677Pattern.lean as L13 p*a = b); so a = p*(a*(b*p)). (⇒) c = p means b*p = b, so
    a = p*(a*b) = p*p since a*b = p. (⇐) p*p = a gives p*p = p*(a*(b*p)); cancel L_p, then
    a*b = p = a*(b*p), cancel L_a: b = b*p, so p = W b = c.]
L5 (quotient lifting): for a surjective magma hom φ : M → B between finite E677 magmas,
    φ (x\z) = φ x \ φ z (uniqueness of left division in B), hence φ commutes with W, U, P, F;
    and if a = U_B x satisfies X6 in B (the six disequalities of Ext677X6.lean's X3_* / L14X6)
    then for any lift x̃ of x, U_M x̃ satisfies X6 in M. State X6 with the existing L14X6
    predicate if it fits, else define `X6Pred`.
L6 (the 20 proved window entries): under the WINDOW hypothesis (v = u ∧ c = p, where
    d = b*b, v = d*b, and a not needed idempotent-free) prove as many of these as go through
    by rewriting + cancellation (each is a short E677/KEY chain; the first-order provers proved
    them from E677 + division + E255 + window; du = a additionally used F∘H = H∘F = id which is
    L12 in Ext677Pattern.lean):
    aw=a au=w ap=u ab=p ad=b | ua=a ub=b up=p | pa=b pp=a pd=u pe=p pu=e | bb=d bp=b bu=p |
    db=u | ea=u | wa=p | du=a, with e := W p. Report which ones resisted.
## New module `Ext677Switch.lean` — the switching construction (no finiteness needed)
Given types X with two ops `star circ : X → X → X` both satisfying E677, define on
`Fin 7 × X`: (q,s)*(r,t) = (4q+r, if q = 0 ∧ r = 0 then circ s t else star s t) (arithmetic in
ZMod 7 or Fin 7 — use ZMod 7). Prove: (S1) E677 holds; (S2) if star, circ satisfy E255 then
so does the product; (S3) (q,s) idempotent ↔ q = 0 ∧ circ s s = s; (S4) the same three
statements for the rotating base (4q+3r) (the proof is the same case analysis: in an E677
instance with (q,r) ≠ (0,0) no intermediate product has both first coordinates 0 — do the
7×7 = 49 first-coordinate cases by `decide` on ZMod 7, then the second coordinate is the
E677 instance of star). If (S4) is short, also state the general "isolation" lemma.
## Deliverables
lean/etp677_ext/Ext677Window.lean, Ext677Switch.lean, AXIOMS.txt appended, and
engine/out/codex/etp677_lean_window_report.md (what is proved, what resisted, axioms) ending
with DONE-LEANWIN.
