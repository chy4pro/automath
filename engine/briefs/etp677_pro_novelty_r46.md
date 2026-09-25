# PRO BRIEF (GPT-5.6 Sol + Pro; INTERNET REQUIRED — literature search) — gate G2 (novelty /
# prior art) for Paper 1 of problems/etp677/pub/PLAN_0830.md. Report facts with URLs; no
# mathematics of your own beyond what is needed to compare statements. Label each claim
# NEW / KNOWN / PARTIALLY KNOWN with the source.

## The claims to check (Equational Theories Project context; equation numbers are the ETP's)
E677: x = y ◇ (x ◇ ((y ◇ x) ◇ y)); E255: ((x ◇ x) ◇ x) ◇ x = x. The finite implication 677 ⟹ 255
(every finite 677-magma satisfies 255) was, as of our last information, an open "finite
implication" of the ETP; the infinite implication is false (greedy/other infinite counterexample).
C1 In a finite 677-magma every left translation is a bijection; every congruence of a finite
   677-magma has all classes of the same size (equal fibres of a surjective homomorphism).
C2 A finite 677-magma with a surjective homomorphism onto a 677+255-magma has no congruence
   class of size 2 (proof: F2-linear pair-indexed form + four E677 instances + KEY).
C3 … no congruence class of size 3 (proof: the seven-instance "Core-7" pattern, a finite
   Sym(3) classification with a bridge lemma / or a parity argument).
C4 If moreover E255 fails at m₀, the class of m₀ has size ≠ 4 (no-hole lemma + a finite lemma
   on four points).
C5 Corollary (the paper's headline; exact phrasing): a minimal finite counterexample to
   677 ⟹ 255 is simple, or every class of every proper non-trivial congruence has at least
   five elements. (Paper title: "Small congruence classes cannot occur in a minimal finite
   counterexample to the implication 677 ⟹ 255".) Also check specifically whether the ETP or
   anyone has published: (i) any lower bound on the order of a finite counterexample beyond the
   exhaustive small-order searches (which orders are exhausted, by whom, when), (ii) any
   congruence/quotient/"class size" argument for 677 or for the sister implication 1485 ⟹ 151,
   (iii) any pair-indexed-extension or "fibre" method in the ETP finite chapters.
C6 Sharpness: the ten-instance local system with the defect is satisfiable on five points (so
   the local method stops at 5); explicit local witness; products give 5^k.
C7 No 677-magma on A5 (60 points) has rows x ◇ y = a_x y b_x⁻¹; likewise none of that form over
   S3, D8, Q8, A4, S4, F21; one-sided rows x ◇ y = f(x) y force exponent 7 and E255.
C8 The switching construction over the two order-7 affine bases (4q+r, 4q+3r): E677 for any
   two E677 fibre operations; idempotent-free examples of order 217 with X_6-type failures
   (windows); the unary-map identities (U(x)x = x, xU(x) = W(x), c = p ⟺ p² = a, etc.).
C9 E255-density multiplicativity: E(M×N) = E(M)×E(N); a uniform positive lower bound on the
   density would prove the implication.

## Where to look
The ETP repository and blueprint (equational_theories on GitHub; the "finite" chapters and the
677 / 255 pages; the Lean file names for these equations), the ETP Zulip archive (public), the
arXiv paper "The Equational Theories Project: …" and follow-ups (2024–2026), MathOverflow /
Terence Tao's blog posts on the project, any 2025–2026 arXiv preprints on 677, on "finite
implications", on magma congruences/"class size" arguments, on Kisielewicz-type greedy
constructions, and on SAT/DRAT-certified magma results. Check specifically whether the
finite 677 ⟹ 255 question has been RESOLVED (either direction) — that changes everything.

## Deliverables (in the response)
A table claim → status (NEW / KNOWN / PARTIAL) → source URL(s) → one line on the relation;
a paragraph on the current status of finite 677 ⟹ 255 with dates; the correct citation keys
(BibTeX) for the ETP paper, the blueprint, and any directly relevant preprint.
