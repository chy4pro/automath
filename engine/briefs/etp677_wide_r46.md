# WIDE-677 — a "widen the search" brief (R46, 2026-08-29). Web search ALLOWED for literature
# only (cite what you find with links; do not rely on memory for attributions).
# Seat: GPT-5.6 Sol + Pro (primary); Qwen3.8-Max acceptable as a second, independent seat.

## 0. The problem
Tao's Equational Theories Project (ETP), last open FINITE implication: does every FINITE
magma (M,*) satisfying
   E677:  x = y * (x * ((y * x) * y))       (for all x, y)
also satisfy
   E255:  x = ((x * x) * x) * x ?
Publicly: open; infinite counterexamples exist (ETP); the ETP paper's authors "tentatively
conjecture it to be false" (a finite counterexample exists); Google DeepMind's
formal-conjectures repo marks the negation as "probably true". A dedicated database of finite
677-magmas exists (github.com/memoryleak47/eq677, "db/<n>/<k>" tables, orders 5–99), plus an
open ETP PR (#1440 "Dedicated 677") carrying a finite conditional theorem "677 ∧ Eq8 ⟹ 255"
and 677-magmas at orders 11, 13, 16, 19, 21, 25, 29, 31, 249. We have spent ~46 rounds on it.
We want you to tell us WHICH OF OUR DEFAULT ASSUMPTIONS TO DROP and to name attack directions
ORTHOGONAL to everything below. Everything below is honest: PROVED means machine-verified or
Lean-certified; refuted means a verified witness exists.

## 1. Proved facts (finite E677 magmas throughout)
Basic: every left translation L_y : z ↦ y*z is a bijection (write y\z); KEY: (y*x)*y = x\(y\x)
(E677 ⟺ KEY in a left quasigroup). E255 at x ⟺ ∃ y: y*x = x (x lies in its own column) ⟺
N(x,x) = 1 where N(t,v) := #{a : a*t = v}. (T1) the sets Fix(L_z) are pairwise disjoint,
Σ_z |Fix(L_z)| ≤ n with equality iff E255. (T1') {w : x*w = x} is a singleton for every x.
(T3) two distinct rows agree on ≤ ⌊n/2⌋ columns and never on two L_p-consecutive points.
(N) N(t,v) = |Fix(L_t ∘ R_v)| cellwise (a theorem of E677; strictly weaker than KEY).
NEW-ID: Σ_z N(z*x, z) = n for every x. (Cyc) the L_y-cycle through y never has length 2 or 3;
length 1 ⟺ idempotent; length 4 ⟹ E255 fails at y (so under E255 excluded); NEW (2026-08-29):
under E255 length 5 is excluded. Quotient theorem: ⟨L_y⟩ is transitive, so every surjective
hom has equinumerous fibres and every quotient realises M as a pair-indexed extension
(x,s)*(y,t) = (x<>y, s <>_{x,y} t) of the quotient by fibre ops satisfying blueprint eq.(4):
s = t <>_{P1}(s <>_{P2}((t <>_{P3} s) <>_{P4} t)), P1=(y,y\x), P2=(x,(y<>x)<>y), P3=(y,x),
P4=(y<>x,y). Minimal-counterexample dichotomy: a counterexample of minimal order is SIMPLE
(no proper congruence) or a pair-indexed extension of a smaller E677+E255 base B with all
fibres of size m, 1 < m < n, and its E255 defect lies over a NON-idempotent base level a
(the diagonal fibre over an idempotent is a smaller 677-magma). The defect at (a,σ) ⟺ no s
has s <>_{(x_a,a)} σ = σ, x_a = (aa)a the unique left unit. All of this is Lean-certified
(lean/etp677_ext/, ≈130 theorems, axioms propext/Classical.choice/Quot.sound).
Linear/affine models: x*y = αx + βy + c over an abelian group is E677 iff αβ(1+β²) = 1,
α + α²β² + β³ = 0, c(αβ² + β² + β + 1) = 0; over prime fields two types (Φ₁₀-type with c = 0,
idempotent; "Type II" α a primitive cube root, p ≡ 1 mod 3: 7, 13, 19, 31, 37, 43, …); the
only idempotent-free affine models over prime fields live in characteristic 31 (5x − 4y + c,
c ≠ 0; resultant argument); none over fields of size ≤ 169 or over F_2², F_3² (census).
All affine models satisfy E255 (blueprint). Non-affine finite 677-magmas exist (extensions
with non-affine, non-separable fibre ops: orders 77 "m77D", 385, and the blueprint's 496);
all known finite 677-magmas satisfy E255 (WARN: "holds on all models" is zero evidence for
E677 ⟹ E255 itself). The Cayley table of a 677-magma need not be Latin (right translations
need not be injective): m77D, m176, m496, 35_x, 45_x, 49_x database models.
Certified negative facts: no 677-magma of order 2, 3, 4, 6 (and 8, 10?, 12, 14 for affine);
no idempotent-free 677-magma of order 5 or 7; no non-Latin one of order 5 or 7; none with
"every pair of rows collides in some column" (ρ = ∇) at order 7 (all DRAT-certified by two
independent encoders + exhaustive enumeration; labeled counts 1,0,0,0,6,0,1680 at orders 1–7,
i.e. one class at 5, two at 7). No pair-indexed extension of F31(5x−4y+1) by a fibre of size
2 or 3 (DRAT), and a human proof: a seven-instance sub-system of eq.(4) with 14 fibre ops on 3
points is unsatisfiable (Core-7; also in Lean). Order-9 exhaustive enumeration: not finished.
First-order fact (ATP, prover9 + E): with H(x) := (xx)((xx)x) and F(x) := L_x^{-4}(x),
F(H(x)) = x follows from E677 + E255 + division laws; H(F(x)) = x needs finiteness (F, H are
mutually inverse permutations in finite models). F(x) = x ⟺ x idempotent.
Extremal branch facts (the "(N-Prop)" sub-programme): if ρ = ∇ holds with every pair colliding
EXACTLY once, the column kernels form a projective plane of order q (n = q²+q+1); on that
branch we proved at q = 2 (exhaustively, 98.8 billion labelled objects) that no object
satisfies (N); a delta==0 "perfect-row" ladder of verified witnesses exists at q = 3,4,5,7
(records 4, 6, 8, 14 perfect rows) and EVERY cap conjecture of the form "≤ f(q) < n perfect
rows" was refuted at q = 3 or 4; the exact q = 3 verdict ("all 13 rows perfect" SAT/UNSAT)
is a running 85k-variable kissat job (no verdict after 7 h).

## 2. Refuted hypotheses / dead routes (each with a verified witness or exhaustion)
- Pure equational derivation of E255 from E677 + left cancellation (saturation: needs
  finiteness/global counting). Marginal counting on N (row/column sums, support): a matrix
  satisfies all margins yet isn't ≡ 1. Term-level "up-step" along L-orbits; congruence-block
  self-reference (circular); sign/parity/2-adic/Sylow-2 routes (sign identity uninformative).
- Transport law (T) a*t = b*t ⟹ (c*a)\(c*t) = (c*b)\(c*t) and kernel law (A): FALSE (m385,
  m77D). "Every non-right-cancellative 677-magma is idempotent": FALSE (m77 order 77). The
  diagonal map e(x) = x\x is neither a homomorphism nor injective in general (m77NT, M9).
  Odd-order conjecture: FALSE (order 16 exists). "Ψ₁ = n discriminates ρ = ∇ phantoms": no.
- Design-theoretic route to (Prop): killed by "phantom" left quasigroups A7/A7ψE (satisfy every
  design-level invariant, violate KEY); group-theoretic route: fine-T3 makes Jordan silent.
- The perfect-row-cap programme (four caps: rowcap q+1 full branch; trace-rowcap q on δ=0;
  CAP2; ROWCAP-D0 q+1 on δ=0) — all refuted by verified objects at q = 3, 4. The p-ary-code /
  "P is a line" route: refuted (near-pencil witness) and shown to be a renaming of its
  target (arity/moment analysis: every plane theorem is import-void).
- Simple case (S): "every finite simple 677-magma is a quasigroup" — open; sharp obstructions:
  generator transport for ϱ* being a congruence (B); heavy-collision exclusion under ρ = ∇
  (Σ_{t,v} N(t,v)² ≤ 2n² − n); pointwise collision-value lift refuted (m176); Pair Conservation
  C(a,b) = |F_ab| (C(x,y) := #{t : Ξ_t x = Ξ_t y}, Ξ_t(x) = x\(t\x)) verified on all models,
  underived.
- TODAY: "F commutes with U(x) = (xx)x" (FU = UF), "H is an endomorphism of every monogenic
  submagma", "every monogenic finite 677-magma is affine", and three implications of the form
  "term collision ⟹ some element idempotent" — all verified on 21 of our models and ALL
  FALSE on the eq677 database's order-49 models (E677+E255, monogenic, not affine over Z/49):
  our benchmark zoo was a narrow class. Survivors on the wider class: FW = WF, FP = PF
  (W(x) = x\x, P(x) = x\U(x)), (v = u ⟺ c = p), (c = w ⟹ w idempotent) — unproved.

## 3. Methods tried
SAT (kissat) + DRAT (drat-trim) certificates; cube-and-conquer (march_cu) with per-cube proofs
and cover certificates (works; the q = 3 target has a heavy tail); CP-SAT (dead for UNSAT);
simulated annealing for witnesses (searcher-blind — repeatedly "proved" caps that were false);
exact CNF encodings of pair-indexed extensions with an E255 defect (running on the cloud for
bases F7 ×2, M9, F13, F31 and fibres 5–9; no verdict yet after 8 h); ATP (prover9, E) and
mace4 (no counter-models ≤ 9 for the commutations); Lean 4 formalization of every reduction;
exhaustive enumerations ≤ 7; a fibre-3 programme (below); prose attacks by GPT-5.6 Pro,
codex-sol and Qwen3.8-Max with mandatory benchmark testing.
Fibre-3 programme (our most concrete partial theorem): if a minimal counterexample has a
congruence with all classes of size 3, its quotient B is E677+E255 and idempotent-free; if
some a ∈ B satisfies five explicit disequalities X_5(a) among the terms u=(aa)a, p=a\u,
b=a\p, d=bb, v=db, c=bv, w=au, then B contains a 7-instance pattern that (Core-7) forbids a
3-element fibre — contradiction. All links Lean-certified; the only open step is "some a
satisfies X_5(a)" in idempotent-free E677+E255 magmas, whose sole supporting model is F31.

## 4. The ask
Given all of the above (and anything you find in the literature — ETP blueprint chapters on
magma cohomology, translation-invariant and greedy constructions, the Zulip/commentary
history for 677; quasigroup/loop theory; combinatorial designs; universal algebra: Mal'cev
conditions, congruence lattices, decidability of finite implications; model theory /
pseudofinite structures; Ramsey/regularity; automorphism-group and permutation-group
methods; finite geometry):
 Q1 Which of our DEFAULT ASSUMPTIONS should be dropped? (Examples of assumptions we made:
    that a counterexample would be found near affine/extension structures; that quotient
    structure is the right decomposition; that "collision" combinatorics carries the
    information; that small orders are informative; that E255 is the right target rather
    than a stronger/weaker intermediate law; that the minimal counterexample is the object to
    study; that the finite case is TRUE.)
 Q2 Which machinery from other areas applies and HOW, concretely?
 Q3 Give THREE attack directions orthogonal to ours, each with the FIRST concrete lemma to
    prove or the FIRST concrete instance to compute (with the exact statement and, where
    computational, the exact object and size), and say what a positive/negative outcome
    would mean. Include at least one direction aimed at CONSTRUCTING a finite counterexample
    that is not a pair-indexed extension of an affine base, and at least one aimed at a
    proof that does not go through quotients.
Label everything PROVED / CITED (with link) / CONJECTURED / SPECULATIVE. Do not restate our
facts back to us; spend your effort on what we have NOT done.
