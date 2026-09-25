# PRO BRIEF (GPT-5.6 Sol + Pro; use your code sandbox for every check) — R46: X_6 on U-cycles.
# No internet needed. Label every statement PROVED / CONJECTURED / REFUTED; PROVED means a full
# derivation (every E677/KEY instance named) or an explicit verified construction.

## Setting (PROVED, use freely)
Finite magma (M,*) with E677: x = y*(x*((y*x)*y)); left translations L_y are bijections
(y\z their inverse); KEY: (y*x)*y = x\(y\x); also E255: ((xx)x)x = x. Maps: S(x) = xx,
W(x) = x\x, U(x) = (xx)x = x\W(x), P(x) = x\U(x), F(x) = x\P(x), H(x) = S(x)*U(x); F,H are
mutually inverse permutations; x idempotent ⟺ F(x) = x ⟺ U(x) = x ⟺ W(x) = x.
L-A: u*x = x ⟹ x*u = W(x) and U(x) = u; hence Fix(L_u) = U^{-1}(u) and x*U(x) = W(x).
c = p ⟺ p*p = a (notation below). v = u ⟺ c = p holds in every known model (no proof).
For a ∈ M write u = U(a), p = P(a), b = F(a), d = bb, v = db (= U(b)), c = W(b), w = W(a), and
   X_6(a) :⟺ v ≠ w, v ≠ u, c ≠ a, c ≠ w, c ≠ u, c ≠ p      (c ≠ a is a theorem; v ≠ p automatic).
THE TARGET OF THE PROGRAMME (open): every finite idempotent-free E677+E255 magma has SOME a
with X_6(a). (A Lean/DRAT-certified chain then gives "no minimal counterexample to 677→255
has a congruence with all classes of size 3".)

## What is known (all verified by code on the models below)
- X_6 can FAIL at some points of an idempotent-free magma: M217ε = Z7 × Z31,
  (q,s)*(r,t) = (4q+r mod 7, 5s−4t+ε mod 31), ε = 1 iff q = r = 0, is E677+E255, has no
  idempotent, and X_6 fails at all 186 points with q ≠ 0 (there v = u and c = p — a "window")
  and HOLDS at all 31 points with q = 0.
- Three idempotent-free models are known: F31 (x*y = 5x−4y+1 mod 31; X_6 everywhere), M217κ
  (same as M217ε but with κ = 2 instead of 0 off the hub; X_6 everywhere), M217ε. In all
  three, the set of X_6 points contains Im(U) = {U(x)} and the U-cycle points (a = U^k(a) for
  some k ≥ 1); in F31 and M217ε the X_6 points are EXACTLY Im(U).
- Switching construction (PROVED): for any two E677 magmas ⋆, ∘ on a set X, Z7 × X with
  (q,s)*(r,t) = (4q+r, s⋆t) for (q,r) ≠ (0,0) and (0, s∘t) for q = r = 0 is E677; E255 iff ⋆,∘
  are; idempotent-free iff ∘ is; the fibre q = 0 is a submagma ≅ (X,∘); at (0,s) all unary maps
  are computed inside that fibre, so X_6 at (0,s) ⟺ X_6 at s in (X,∘); at q ≠ 0 the first
  coordinates give v ≠ w, c ≠ w, c ≠ u automatically and X_6 ⟺ (v⋆ ≠ u⋆ at s in (X,⋆)), which
  fails e.g. when ⋆ is all-idempotent (5s−4t). Also Im(U) ⊆ fibre q = 0 in these products.
- Models WITH idempotents behave differently: there X_6 fails at every non-idempotent point
  in all benchmarks (so any proof must use idempotent-freeness essentially).

## CONJECTURE (E)
In a finite idempotent-free E677+E255 magma, X_6 holds at every point of every U-cycle
(equivalently at every a with a = U^k(a) for some k ≥ 1). Weaker sufficient form (E'): X_6
holds at some point of Im(U). Either would close the programme's existence step, since U has
cycles in any finite magma.

## TASKS (in this order)
1. Try to PROVE (E) or (E'). Handles: for a on a U-cycle there is x with U(x) = a, i.e.
   a*x = x (L-A), so Fix(L_a) ≠ ∅; if v = u at a then L_u fixes the six window elements
   (STEP-37 rigid block: u*k = k for k ∈ {a,w,p,b,d,e}); chase the U-chain a → U(a) → …
   around the cycle using x*U(x) = W(x), U(x)*x = x, S(x)*x = U(x), W(x)*S(x) = U(x), and
   E677/KEY at pairs (U(a), a), (a, x), (x, a). Look for a contradiction between "a is a
   U-image AND a is a window" and idempotent-freeness (in M217ε the windows are exactly the
   non-images, so this is the sharpest possible dichotomy).
2. Or CONSTRUCT a finite idempotent-free E677+E255 magma with a window at a point of Im(U)
   (or on a U-cycle) — e.g. a two-level switching product Z7 × (Z7 × X) or a non-product
   extension where the hub fibre itself is a window-bearing magma. Verify by code (E677 on
   all pairs, E255, no idempotent, name the point, show it is U(x) for an explicit x and that
   v = u or c = p there). This would refute (E) and (E') and would be equally valuable.
3. If neither: prove whatever partial results you can (e.g. "a ∈ Im(U) ∧ window at a ⟹ …"),
   and give the exact obstruction.
Mandatory: test every asserted identity by code on F31, M217κ, M217ε, T7 (x*y = 4x+y+6 mod 7)
and M49ε ((x,s)*(y,t) = (4x+y, 4s+t+[x=y=0]) on F7×F7); print the checks.
