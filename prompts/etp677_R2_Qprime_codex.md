# Round 2 critical lemma: (Q') right-cancellativity of finite 677-magmas

Context: finite magma (M,*) satisfying E677: x = y*(x*((y*x)*y)). Known
(proved, you may use freely):
- Every L_y (z -> y*z) is a bijection; write Λ_y = L_y^{-1}, y\v = Λ_y(v).
- (★) v*y = Λ_{Λ_y(v)}(Λ_y²(v)) for all v,y — the product is determined by
  left division; E677 ⟺ the single law u\((y\u)\(y\(y\u))) = y in (M,\).
- Lemma B: (y\u)*(u*y) = y\(y\u) for all u,y.
- Lemma F: y*v = v ⟹ v*y = Λ_v(v) =: e(v) (the unique right unit of v).
- Lemma G (diagonal case, proved): distinct L_y, L_{y'} share no FIXED point:
  y*v = v = y'*v ⟹ y = y'.
- Theorem: E255 (x = ((x*x)*x)*x) holds at y iff y has a left unit; the
  finite implication "E677 ⟹ E255" is EQUIVALENT to "every element has a
  left unit", and is IMPLIED by:

  (Q') For all t: a*t = b*t ⟹ a = b   (i.e. every R_t injective;
       equivalently {L_y} is a sharply transitive permutation set;
       equivalently |Fix(L_t ∘ R_v)| ≤ 1 for all t,v).

YOUR TASK: prove (Q') or construct a finite 677-magma violating it.
This is the whole game: (Q') true ⟹ the last open finite implication of the
Equational Theories Project is resolved affirmatively (finite 677 ⟹ 255).
A finite non-quasigroup 677-magma would be equally revolutionary (all known
finite models are affine quasigroups over Z_n, orders 1,5,7,11,13,19,31,35,37
and products).

Promising route (from Round 1): given a*t = b*t = v, set A = Λ_t(a),
B = Λ_t(b); Lemma B gives A*v = Λ_t(A) and B*v = Λ_t(B). Study
Θ_t(X) := X\(t\X) = Λ_X(Λ_t(X)): (Q') ⟺ every Θ_t is injective. Iterate
Lemma B (e.g. Λ_v(A)*Λ_t(A) = Λ_v²(A)) hunting an invariant of (A,t,v)
forced to be L-injective — the analogue of e(v) in Lemma F's proof. Also
try: counting (Σ_u |Fix(L_u ∘ R_v)| double counts?), finite-order pumping
(each Λ_y has finite order), and the mirror form. If proof resists, attempt
small counterexample construction: a non-quasigroup finite 677-magma needs
some column with a repeated value — use (★) to propagate consequences of a
single collision a*t = b*t, a ≠ b, and either derive a contradiction
(= proof of (Q') by contradiction!) or complete a finite table (verify by
program). Persist through at least three structurally different mechanisms.
Computational experiments allowed (python3) but the goal is the full lemma.

Write your complete report to problems/etp677/R2_Qprime_codex_report.md.
Do not read other files in problems/etp677/ or notes/. Do not search the internet.
