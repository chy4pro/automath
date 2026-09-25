# PRO BRIEF (GPT-5.6 Sol + Pro; code sandbox mandatory; internet allowed for literature only) —
# NEW METHOD M1: the SIMPLE case of a minimal counterexample to 677 ⟹ 255 through its
# left-multiplication group. Label PROVED / CONJECTURED / REFUTED; every PROVED step named.

## What is now known (verified; see the previous briefs for definitions)
A minimal finite counterexample M to 677 ⟹ 255 is SIMPLE (no non-trivial congruence) or every
congruence class has ≥ 5 elements. In a simple finite E677 magma the left-multiplication group
G = ⟨L_x : x ∈ M⟩ (each L_x a permutation of M) acts primitively on M (a G-invariant partition
would be a congruence: L_x maps blocks to blocks — check and prove this "dictionary" statement
precisely; it is used by us but re-derive it). Known finite E677 magmas: affine x*y = αx+βy+γ
over F_q (q = 5, 7, 9, 11, 13, 16, 19, 31, 37, 41, 43, 49; α, β must satisfy αβ(1+β²) = 1 and
α + α²β² + β³ = 0) — their G is an affine group AGL-type (regular normal elementary abelian
subgroup, G = V ⋊ ⟨β⟩ roughly) and they satisfy E255; the all-idempotent simple non-affine
magmas of orders 21, 25, 29, 41 whose G is A_n or S_n (primitive, not affine) — they satisfy
E255 trivially (x*x = x). Group-action rows x*y = a_x y b_x⁻¹ over a group S give E677 only in
the abelian/one-sided case (exponent-7 affine); over S3, D8, Q8, A4, S4, F21, A5 no E677 section
exists (DRAT-certified). E677 alone forces: L_x bijective; all fibres of a homomorphism equal;
KEY (y*x)*y = x\(y\x); the L_x-cycle through x has length ≥ 6 unless x is idempotent, and with
E255 the maps F = L_x^{-4}(x), H = S(x)U(x) are mutually inverse.

## TASKS (choose the order; report all partial results)
1. AFFINE TYPE. Suppose M is a finite E677 magma whose G contains a regular normal elementary
   abelian subgroup V (so M ≅ V as a set and every L_x is an affine map y ↦ A_x y + c_x with
   A_x ∈ GL(V)). Prove E255 for such M, or find a counterexample: E677 becomes, for all x, y,
   A_y A_x A_{y*x}? — write the exact operator identity (E677 in operator form: L_y L_x L_{(y*x)*y}?
   careful: E677 says x = y*(x*((y*x)*y)), i.e. L_y L_x L_{y*x}(y) = x with the inner argument y;
   derive the constraints on (A_x, c_x) as functions of x, e.g. is x ↦ A_x forced to be constant
   (A_x = β) on a primitive affine G? then E677 forces the affine-model equations and E255
   follows as in the F_q models). If A_x need not be constant, characterise the solutions on
   small V (F_2^k, F_3^k, F_5^2, F_7^2) by exhaustive or SAT search in your sandbox and test
   E255 on each. A theorem "E677 + affine G ⟹ E255" would reduce the problem to the non-affine
   primitive types.
2. NON-AFFINE PRIMITIVE TYPES (O'Nan–Scott: almost simple, diagonal, product, twisted wreath).
   Which structural facts of E677 (the U-map, equal fibres, the L-cycle lengths ≥ 6, KEY) are
   incompatible with which types? E.g. in the all-idempotent examples G = A_n; can a
   non-idempotent simple E677 magma have G ⊇ A_n (n = |M|)? Show that E255 failing at x
   forces a specific non-trivial structure on the point stabiliser or on the orbits of L_x —
   anything that excludes a type is progress. Use the A5-template negative as data.
3. State the sharpest reduction you can prove: "a minimal counterexample is simple with G of
   type … and |M| ≥ …" (using: no E677 magma of order 2, 3, 4, 6, 8, 10, 12; all orders ≤ 12
   exhausted by the community; monogenic exclusion at 9, 10; class sizes ≥ 5 ⟹ non-simple
   |M| ≥ 5·|B| ≥ 25).
Mandatory: every identity tested by code on F31, T7 (4x+y+6), 4x+3y, F13, the F9/F16/F49
affine models (fit them yourself from the conditions), and on the order-25 all-idempotent
model if you can construct one (the E677 idempotent magmas: x*y = ? — find the family).
