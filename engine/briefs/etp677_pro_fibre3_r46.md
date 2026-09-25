# PRO BRIEF (GPT-5.6 Sol + Pro; code sandbox mandatory) — R46: extend the FIBRE-2 exclusion to
# FIBRE 3 with the gauge-free local-core method. No internet needed. Label PROVED / CONJECTURED /
# REFUTED; every PROVED step names its E677/KEY instance; every computation printed.

## What you proved last round (verified by us, now a theorem of the programme)
Finite E677 magma M, surjective homomorphism π: M → B with B satisfying E255, some fibre of
size 2 ⟹ contradiction. Method: the fully general fibre-2 extension (x,s)*(y,t) =
(xy, t + A_{x,y}s + B_{x,y}); lift E677 at ((r,s),(q,t)); the s/t-coefficient identities (I)
A_{a,q} + A_{r,b} = 1, (II) A_{q,c} + A_{a,q}A_{q,r} = 1 (a = qr, b = aq, c = rb); the four
instances (x,u), (x,x), (p,x), (f,x) at x and the diagonal fact A_{z,z} = 0 applied at z = f
(u = U(x), w = W(x), p = P(x), f = F(x); universal products ux = x, xu = w, xw = x,
(xx)x = u, xp = u, px = f, xf = p). We machine-checked it gauge-free: with σ[x,y][s] ∈ Sym(2)
free for the 19 base pairs of those 8 instances (4 at x, 4 at f), the CNF is UNSAT (DRAT);
with only the 4 instances at x it is SAT.

## The target: fibre 3
Same setting with a fibre of size 3. General form (x,s)*(y,t) = (xy, σ_{x,y}(s)(t)) with
σ_{x,y}: F3 → Sym(3) arbitrary (NO gauge fixed — this is what made the fibre-2 proof
base-independent). Lifting E677 at ((r,s),(q,t)) gives, for all s,t ∈ F3:
   σ_{q,c}(t) ∘ σ_{r,b}(s) ∘ σ_{a,q}(σ_{q,r}(t)(s)) (t) = s.        (†)
FACT (our computation): the 8-instance local core above (12 named symbols x, S,U,W,P,F of x,
S,U,W,P,F of f, S(F(f)); 19 pairs; all symbols distinct) is SATISFIABLE for m = 3 (also m = 4,
5), and stays SAT when we add the same 4 instances at further F-levels F²(x), F³(x), …
So fibre 3 needs MORE than the fibre-2 argument. Known in our programme (Lean + DRAT): if the
eight terms a, w, u, p, b = F(a), d = bb, v = db, c = W(b) of some a ∈ B are pairwise distinct
(the "X_6" disequalities), then the seven E677 instances of the pattern P* at those terms have
no fibre-3 solution (the Core-7 lemma — but that instance FIXES a gauge per fibre and so
needs the fibres to be distinct). Whether X_6 holds at some point of every idempotent-free
E677+E255 magma is open (it holds at every point of Im(U) in all known examples; it fails at
"window" points where v = u ∧ c = p, and at points with c = u).

## TASKS
1. Find a set of lifted E677 instances (and KEY-derived universal products) whose gauge-free
   fibre-3 core is UNSAT WITHOUT any distinctness assumption — i.e. a fibre-3 exclusion
   theorem in the style of fibre 2. Strategy: write (†) for a large candidate set of named
   pairs (all products among {x, S,U,W,P,F,H of x and of F(x), F²(x), and the "window" terms
   b, d, v, c}), let a SAT solver (your sandbox; encode σ as permutation matrices) find the
   minimal unsatisfiable core (drop instances greedily), then turn the core into a written
   proof: for Sym(3) the trick is that (†) with s = t or with the diagonal pairs forces
   specific permutations; look for an analogue of A_{z,z} = 0 (e.g. σ_{z,z}(s) is a
   specific involution / has a fixed point) and of the chain (2)–(8). Report the core, the
   proof, and an exhaustive verification (all σ assignments of the core's pairs, or the
   solver's UNSAT with an independent check).
2. If the gauge-free core is SAT for every instance set you try: exhibit the satisfying
   σ-assignment for the largest set and say what it looks like (e.g. whether it is realised
   by an actual E677 magma of order 3|B| — try to complete it over B = F31 or T7 with your
   CSP; a completion would be a fibre-3 extension, which for B = F31 we have shown impossible
   by DRAT, so a local solution must fail globally — identify which additional instance
   kills it: that instance is the missing ingredient). Also test whether adding the
   distinctness of only SOME terms (which ones?) makes the core UNSAT — the minimal
   distinctness set is exactly what the programme must prove.
3. Same question for fibre 4 and 5 if 1 succeeds.
Mandatory: all claims checked by code; a positive control that your encoding accepts the
direct-product extension (σ_{x,y}(s) = left translation of the order-5 magma s∘t = 2s−t mod
5 when m = 5) and rejects m = 2 (must be UNSAT).
