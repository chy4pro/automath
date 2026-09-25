# CODEX TICKET (Lean 4; sol tier) — formalise the FIBRE-2 EXCLUSION THEOREM (registry R46
# STEP 48). Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext
# (conventions of Ext677Window.lean / Ext677Quot.lean: E677 op, [Finite M], ldiv, X6U/X6W,
# L13 terms, IsMagmaHom, window_left_unit = L-A, window_map_ldiv = homs preserve ldiv).
# 0 sorry; own `#print axioms` for every theorem appended to AXIOMS.txt. Heavy ≤ 2 (lake build).
# DONE marker: DONE-LEANF2.

## Theorem
Let M, B be finite magmas, E677 opM, E677 opB, E255 opB, φ : M → B a surjective magma
homomorphism, and x : B with `Nat.card {m // φ m = x} = 2`. Then False.

## Proof to formalise (all steps elementary; see STEP 48 for the derivation)
F1 Fibre transport: for every m : M and y : B, `opM m` maps {m' // φ m' = y} bijectively onto
   {m' // φ m' = φ m * y} (injective by E677 left-cancellation in M, surjective by finiteness /
   E677). Hence fibres over y and over (φ m)*y have equal cardinality, and iterating with
   left division, the fibres over x, W x, U x, P x, F x, S x = x*x all have cardinality 2.
F2 The F2-form of a 2-element fibre action: for base elements y, y' := φ(m)*y with both fibres
   of size 2, the bijection fibre(y) → fibre(y') induced by m ∈ fibre(z) is one of two
   bijections; choose an enumeration e_y : Fin 2 ≃ fibre(y) for every base element once, and
   define A_{z,y} m := (the induced map is the swap) as a Bool; show the induced map on Fin 2
   is t ↦ t + a(m) with a(m) ∈ ZMod 2, and that a depends on m ∈ fibre(z) affinely:
   a(m) = A_{z,y}·s(m) + B_{z,y} where s(m) ∈ ZMod 2 is m's coordinate — over ZMod 2 EVERY
   function Fin 2 → ZMod 2 is affine (state and prove this tiny lemma: f t = f 0 + (f 1 − f 0) t).
F3 Coefficient identities: for base elements r, q and a = q*r, b = a*q, c = r*b, lifting E677
   at ((r,s),(q,t)) for all s t : ZMod 2 gives
   (I) A_{a,q} + A_{r,b} = 1 and (II) A_{q,c} + A_{a,q}·A_{q,r} = 1 in ZMod 2
   (extract by evaluating at (s,t) = (0,0),(1,0),(0,1) — in ZMod 2 the affine identity in
   two variables has coefficients determined by those three evaluations).
F4 The four instances at x with u = U x, w = W x, p = P x, f = F x, s₀ = x*x and the base
   products opB u x = x (E255), opB x u = w (L-A), opB x w = x, opB s₀ x = u, opB x p = u,
   opB p x = f (from KEY(x,p): (x*p)*x = p\(x\p) — derive it from E677 as in the Ext677
   library or via ldiv lemmas), opB x f = p:
   (x,u): (II) ⟹ A_{u,x} = 1 ∧ A_{x,u} = 0; (I) ⟹ A_{x,w} = 1.
   (x,x): (I) ⟹ A_{s₀,x} = 1; (II) ⟹ A_{x,x} = 0.   [so A_{z,z} = 0 for all z, in particular f]
   (p,x): (I) ⟹ A_{p,x} = 0.
   (f,x): (I) ⟹ A_{p,x} + A_{f,f} = 1 — contradiction.
   (ZMod 2 arithmetic: `decide` on the finitely many cases after `revert`, or `fin_cases`.)
Corollary (state it): for a finite E677 magma M with a congruence (setoid with compatible op,
or a surjective hom φ) whose quotient satisfies E255, every fibre has cardinality ≠ 2.

## Deliverables
lean/etp677_ext/Ext677Fibre2.lean, AXIOMS.txt appended, engine/out/codex/etp677_lean_fibre2_report.md
ending with DONE-LEANF2. If F2's enumeration bookkeeping is heavy, an acceptable intermediate
is: assume an explicit bijection M ≃ Σ y : B, Fin (card fibre y) and prove the theorem for the
"pair-indexed" form (x,s)*(y,t) = (x*y, t + A x y * s + B x y) over ZMod 2 directly (Theorem′),
plus the F1 transport lemma separately; say clearly which form you proved.
