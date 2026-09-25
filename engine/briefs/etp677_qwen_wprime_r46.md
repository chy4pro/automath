# QWEN3.8-MAX BRIEF — R46: ONE local lemma about the "hole" of the window. No internet.
Finite magma (M,*) with E677: x = y*(x*((y*x)*y)); every left translation L_y: z ↦ y*z is a
bijection (y\z = its inverse); KEY: (y*x)*y = x\(y\x); assume E255: ((xx)x)x = x for all x.
Maps: S(x) = xx, W(x) = x\x (x*W = x), U(x) = (xx)x = x\W(x) (U(x)*x = x, and U(x) is the
ONLY z with z*x = x), P(x) = x\U(x), F(x) = x\P(x), H(x) = S(x)*U(x); F,H are mutually inverse
permutations; F(x) = x iff x idempotent; U(x) = x iff x idempotent.
PROVED general lemma L-A: if u*x = x then x*u = W(x) and U(x) = u (E677 at (u,x) and cancel).

THE WINDOW (PROVED facts). Fix a with a*a ≠ a and suppose v = u and c = p, where u = U(a),
p = P(a), b = F(a), d = bb, v = db (= U(b)), c = W(b), w = W(a); put e = a*a. Then the seven
elements a,w,u,p,b,d,e are distinct and their products are FORCED to be (row * column):
              a  w  u  p  b  d  e
        a  |  e  a  w  u  p  b  d
        w  |  p  b  d  e  a  w  u
        u  |  a  w  ?  p  b  d  e
        p  |  b  d  e  a  w  u  p
        b  |  w  u  p  b  d  e  a
        d  |  d  e  a  w  u  p  b
        e  |  u  p  b  d  e  a  w
(20 entries have machine proofs; the rest are verified on 864 instances in real models; you may
use the whole table). The ONLY product not determined is the hole u*u. Note: u*k = k for the six
k ≠ u, so by L-A U(k) = u for all six and k*u = W(k). With u*u = u the table is the affine magma
x*y = 4x + y + 6 on Z/7 (a..e = 0..6), which satisfies E677 and E255 and has u as its idempotent.

TARGET (holds in every known model; no proof):
   (W')  u is idempotent,  OR  u*u is idempotent,  OR  U(u) is idempotent.
Two real models with u NOT idempotent show BOTH remaining cases occur, so neither disjunct can
be dropped: (i) in (x,s)*(y,t) = (4x+y, 4s+t+ε) on F7×F7, ε = 1 iff x = y = 0 (E677+E255,
unique idempotent (0,5)), at a = (1,0): u = (0,0), the L_u-cycle u, uu, u(uu), … has length 7
and U(u) = (0,5) is the idempotent while u*u = (0,1) is not; (ii) in another order-49 model
the L_u-cycle through u has length 6 and u*u is the idempotent while U(u) is not.
So the claim is really: the L_u-cycle through u (length m ≥ 6, since u is not idempotent)
contains an idempotent at position 1 or m−2. What you know about that cycle: c_0 = u,
c_1 = uu, c_{i+1} = u*c_i, c_m = u, W(u) = c_{m−1}, U(u) = c_{m−2}, P(u) = c_{m−3},
F(u) = c_{m−4}; the general E677 consequences c_i*(c_{i+1}*u) = c_{i−1} (KEY at (u, c_i)),
S(u)*u = U(u), W(u)*S(u) = U(u), u*U(u) = W(u); L_u fixes a,w,p,b,d,e pointwise and no c_i
(i ≠ 0 mod m) is among them.
TASK: prove (W'), or derive as much as possible about the products u*u = c_1, c_1*c_1,
c_{m−2}*c_{m−2}, and the products between {c_i} and the six window elements (E677 at every
pair (c_i, k) and (k, c_i), KEY likewise), and report the exact closed partial table you reach
and where it stops. Every claimed identity must be tested on model (i) above (compute
explicitly; all maps are affine there) and on x*y = 4x + y + 6 mod 7. Say precisely where
finiteness (the cycle closing, c_m = u) is used. Label PROVED / CONJECTURED.
