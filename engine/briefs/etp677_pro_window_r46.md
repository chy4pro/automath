# PRO BRIEF (GPT-5.6 Sol + Pro; use your code sandbox for every check) — R46 "window" problem.
# No internet needed. Answer in English or Chinese. Label every statement PROVED / CONJECTURED
# / REFUTED and, for anything PROVED, give the derivation in full (every E677/KEY instance named).

## Setting (all PROVED, use freely)
Finite magma (M,*) satisfying E677: x = y*(x*((y*x)*y)). Then every left translation
L_y: z ↦ y*z is a bijection; y\z denotes its inverse. KEY: (y*x)*y = x\(y\x). We also assume
E255: ((xx)x)x = x for all x. Unary maps: S(x) = xx, W(x) = x\x (x*W(x) = x), U(x) = (xx)x =
x\W(x), P(x) = x\U(x), F(x) = x\P(x), H(x) = S(x)*U(x); F and H are mutually inverse
permutations; F(x) = x ⟺ U(x) = x ⟺ W(x) = x ⟺ x idempotent. The L_x-cycle through x
(x, xx, x(xx), …) has length ≥ 6 unless x is idempotent.
Lemma L-A (PROVED): if u*x = x then x*u = W(x) and U(x) = u. [E677 at (y,x) = (u,x):
x = u*(x*((u*x)*u)) = u*(x*(x*u)); cancel L_u: x*(x*u) = x = x*W(x); cancel L_x: x*u = W(x);
so U(x) = x\W(x) = u.] With E255 (U(x)*x = x): Fix(L_u) = {x : U(x) = u} for every u, and
x*U(x) = W(x) for every x.
Lemma (PROVED): c = p ⟺ p*p = a, in the notation below (E677 at (a,p) with p*a = b).

## The window
Fix a non-idempotent a; write u = U(a), p = P(a), b = F(a), d = b*b, v = d*b (= U(b)),
c = W(b), w = W(a), e = a*a. The WINDOW is the hypothesis  v = u and c = p.  (In a finite
idempotent-free E677+E255 magma we need to show the window never occurs — it is one of the
five residual conditions of the X_6 programme; on every known model with a window the model
has an idempotent, and on every known idempotent-free model there is no window.)
FACT (rigid block): under the window the seven elements a,w,u,p,b,d,e are distinct and
              a  w  u  p  b  d  e
        a  |  e  a  w  u  p  b  d
        w  |  p  b  d  e  a  w  u
        u  |  a  w  ?  p  b  d  e        (? = u*u is the only undetermined product)
        p  |  b  d  e  a  w  u  p
        b  |  w  u  p  b  d  e  a
        d  |  d  e  a  w  u  p  b
        e  |  u  p  b  d  e  a  w
Status of the 48 entries: PROVED by first-order provers from E677+division+E255+window:
aw,au,ap,ab,ad, ua,ub,up, pa,pp,pd,pe,pu, bb,bp,bu, db, ea, wa, and du (this last one used
F∘H = H∘F = id). The other 28 hold in all 864 window instances of our model database (0
failures) but have no written proof — proving them is a sub-task (they are all consequences
of E677/KEY/E255 + finiteness at the seven points; some may need F,H inverse or L_x-cycle
arguments). With u*u = u the block is exactly the affine magma x*y = 4x + y + 6 on Z/7
(a..e ↦ 0..6) — call it T7; it satisfies E677 and E255, and u is its idempotent.
Consequences you may read off: L_u fixes the six elements K = {a,w,p,b,d,e} pointwise, so
U(k) = u and k*u = W(k) for k ∈ K (L-A); F(b) = a, F(w) = p, F(d) = e (F has 2-cycles here);
W acts on K as (a w d)(p e b).

## What is known about the hole u*u (data from all 252 model instances where u is NOT idempotent)
The L_u-cycle through u, c_0 = u, c_{i+1} = u*c_i, c_m = u, has length m = 6 or 7 and ALWAYS
contains an idempotent: m = 6 ⟹ c_1 = u*u is idempotent; m = 7 ⟹ c_5 = U(u) is idempotent.
Two concrete witnesses (both E677+E255, unique idempotent):
 (i) M49ε on F7×F7: (x,s)*(y,t) = (4x+y, 4s+t+ε(x,y)), ε = 1 iff x = y = 0 else 0. At a = (1,0):
     w = (4,0), u = (0,0), p = (3,0), b = (6,0), d = (2,0), e = (5,0), v = u, c = p; the L_u-cycle
     has length 7, U(u) = (0,5) is the idempotent, u*u = (0,1) is not.
 (ii) a database model of order 49 (table available: it is an extension of T7 = quotient with 7
     classes of size 7, whose hub submagma Im(U) has order 7 with L-cycle type [6,1]) where at
     every window element the L_u-cycle has length 6 and u*u is the idempotent, U(u) is not.
So the sharpest LOCAL statement consistent with all data is
   (W')  window at a  ⟹  u idempotent  ∨  u*u idempotent  ∨  U(u) idempotent,
and neither disjunct can be dropped. First-order provers (prover9, E; 15 min) find no proof of
(W') from the local data even with the cycle length fixed to 6, 7 or 8 — a proof needs a real
idea (a counting/permutation argument, or a quotient).
GLOBAL PICTURE (PROVED): (α) for ANY two finite E677 magmas ⋆ and ∘ on the same set X, the
magma on Z7 × X with (q,s)*(r,t) = (4q+r, s⋆t) if (q,r) ≠ (0,0) and (0, s∘t) if q = r = 0
is E677; it satisfies E255 iff ⋆ and ∘ do; it is idempotent-free iff ∘ is; and it has a
window at (q,s) with q ≠ 0 iff ⋆ has a window at s. (β) Both witnesses above have exactly one
non-trivial congruence, with quotient T7 and all classes of size 7. (γ) In a translation
magma x*y = y + g(x) over an abelian group, U(x) is idempotent for every x; affine
translation-type E677 magmas exist only over (Z/7)^k.

## TASKS (in this order; stop and report whatever you get)
1. PROVE the theorem  "window at a ⟹ M has an idempotent"  — via (W') or any other route.
   Suggested handles: (a) the T7 block is an almost-submagma whose only leak is u*u — study the
   submagma N generated by the block, or the smallest congruence identifying the block with a
   point; (b) Fix(L_u) = U^{-1}(u) ⊇ K and the counting identity Σ_u |Fix(L_u)| = |M|;
   (c) the L_u-cycle: c_i*(c_{i+1}*u) = c_{i−1} for all i (KEY at (u,c_i)), S(u)*u = U(u),
   W(u)*S(u) = U(u), u*U(u) = W(u); (d) E677/KEY at the pairs (c_i, k) and (k, c_i), k ∈ K;
   (e) show U(u) ∈ Fix(L_{U(u)}) … a U-chain argument; (f) the switching structure (α) suggests
   an induction on |M| through a T7-quotient: prove the window forces a congruence with T7
   quotient, then the class over T7's idempotent is a smaller E677+E255 submagma carrying the
   same problem or an idempotent.
2. OR CONSTRUCT a finite idempotent-free E677+E255 magma with a window (this would refute the
   X_6 programme's hypothesis and is equally valuable). By (α) a twisted product needs a window
   in ⋆; look for non-product constructions, e.g. extensions of T7 whose idempotent class is
   an idempotent-free E677+E255 magma N (smallest known: F31 with x*y = 5x−4y+1, order 31; the
   order-217 model (q,s)*(r,t) = (4q+r, 5s−4t+κ), κ = 1 iff q = r = 0 else 2) with non-uniform
   fibre rules. Any construction must be verified by your own code (E677 on all pairs, E255,
   no idempotent, and the window at a named point); print the formula and the checks.
3. If neither: prove as many of the 28 unproved block entries as you can (full derivations),
   and give the exact closed partial table on K ∪ {c_0,…,c_{m−1}} for m = 6 and m = 7 that
   E677/KEY/E255 force, stating precisely which products remain free — that is the obstruction.
Mandatory tests: every identity you assert must be checked by code on T7 (4x+y+6 mod 7), on
M49ε, on F31 (5x−4y+1 mod 31) and on the order-217 model above (all four are E677+E255).
