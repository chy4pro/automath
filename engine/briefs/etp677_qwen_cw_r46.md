# QWEN3.8-MAX BRIEF — R46: ONE small lemma. No internet.
Finite magma (M,*) with E677: x = y*(x*((y*x)*y)); left translations L_y are bijections
(y\z the inverse); KEY: (y*x)*y = x\(y\x); assume also E255: ((xx)x)x = x for all x.
Notation: S(x) = xx, U(x) = (xx)x = x\(x\x) (the unique left unit: U(x)*x = x),
W(x) = x\x (the unique right unit: x*W(x) = x), P(x) = x\U(x), F(x) = x\P(x) (so
W = L_x^{-1}x, U = L_x^{-2}x, P = L_x^{-3}x, F = L_x^{-4}x), H(x) = S(x)*U(x); F and H are
mutually inverse permutations; F(x) = x iff x is idempotent; W(x)*S(x) = U(x) (PROVED:
E677 at (y,x) := (x, W(x)) gives W = x(W(xx)), so x\W = W*S, and x\W = x\(x\x) = U).
For a fixed a put u = U(a), p = P(a), b = F(a), d = bb, v = U(b) = db, c = W(b), w = W(a).
Automatic: ua = a, aw = a, au = w, ap = u, ab = p, ad = b, pa = b, vb = b, bc = b, bv = c,
dv = a, cd = v (the last from W(b)S(b) = U(b)).
PROVED general lemma: if c = z for some element z then z*d = v (E677 at (y,x) = (b,z) using
bz = b: z = b(z((bz)b)) = b(z d), and b\z = v).

TARGET (observed on every known model, never failing; no proof):
   c = w  ⟹  w is idempotent (w*w = w).
Equivalently: W(F(a)) = W(a) ⟹ W(a)*W(a) = W(a). Under "no idempotents" this gives c ≠ w.
What you know when c = w: b*w = b (w is the right unit of b as well as of a), b*v = w,
w*d = v (general lemma), a*w = a, plus E677/KEY at every pair among {a,w,u,p,b,d,v}.
Find a derivation of w*w = w — or the exact obstruction (a partial table on
{a,w,u,p,b,d,v} closed under every E677/KEY consequence you can extract, with w*w ≠ w).
Test every intermediate identity on the order-7 model x*y = 4x+3y mod 7 and on the order-31
model x*y = 5x−4y+1 mod 31 (where c ≠ w always, so the implication is vacuous there — use
instead the order-45 or order-49 models if you can build one: the database model 45_0 has
c = w at every non-idempotent element with w = the idempotent; a formula-level example
with c = w somewhere: F7 × F7 with (q,s)*(r,t) = (4q+r, 4s+λt), λ = 3 if q=r=0 else 1).
Label PROVED / CONJECTURED.
