# Task: triage a raw list of 20 conjecture-stating papers (cs.LO / math.AC) plus curated leads — rank and flag, not solve

This is a TRIAGE task, not a proof task: we sourced a raw list of arXiv papers (cs.LO = logic in
computer science, math.AC = commutative algebra) that each state a new conjecture in their
abstract, plus several leads pointing at curated "open problems" surveys/columns/seminars. Nothing
below has been ranked or scored yet. We want your judgment on which are worth a solver's time,
using the four axes below, plus two specific flags. This is NOT a request to solve any conjecture —
it is a request to assess and rank, and to be honest when you don't have enough information (say
"unclear" rather than guessing a plausible-sounding rank — an honest "I cannot tell from this" is
worth more to us than a confident-sounding rank; inventing a rank is the failure we are guarding
against).

**IMPORTANT — frequency/prominence is NOT value.** Where a name below is a famous, long-studied
conjecture, that is a crowding signal working AGAINST pursuit, not a quality signal for it. We flag
two such items explicitly below (Lech's conjecture, Evans–Griffith Small Syzygy conjecture) —
please still triage them by the axes, but weight fame as a negative for `crowding`, not a positive.

## The four ranking axes (apply these to every candidate)

1. **`certkind`** — what KIND of thing would a proof/refutation look like? We care most about
   candidates with a **finite, machine-checkable certificate** (Kind-1: e.g., a finite search
   space, a decidable combinatorial/algebraic statement, an explicit object a computer could in
   principle verify end-to-end) over candidates that are open-ended "prove a general theorem"
   statements requiring genuinely novel unbounded mathematics (Kind-2). Say which kind it looks
   like, or say you cannot tell from the abstract/title alone.
2. **`verifroute`** — if someone claimed a proof, how would we independently verify it? A clear,
   checkable route (a formal proof-assistant statement, a finite computation, a well-known
   reduction) is good; verification itself being hard/expensive/subjective is bad. **Hard
   constraint you must flag explicitly**: our infrastructure FORBIDS local brute-force search / SAT
   solving / exhaustive local computation as a verification method. If a candidate's only plausible
   verification route is local exhaustive search over a space too large to reason about
   structurally, flag that explicitly — such a candidate is unusable to us regardless of how
   "checkable" it looks on paper.
3. **Novelty / crowding** — is this fresh and uncrowded, or already well-studied? Note explicitly
   that raw mention-frequency or fame is NOT the same as importance, and a famous conjecture should
   be marked more crowded, not more valuable.
4. **Fit** — is the mathematical content within reach of a competent generalist attacker, or does
   it require deep specialized machinery from a narrow subfield (e.g., model-theoretic graph
   sparsity, F-singularity theory, moduli-space machinery)?

## Part A — 20 ABS-class papers (each states a NEW conjecture in its own abstract, 2024-08 to 2026-08)

### cs.LO (5)

| date | arXiv id | title | conjecture (verbatim snippet) |
|---|---|---|---|
| 2025-11-27 | 2511.22382 | Comparing State-Representations for DEL Model Checking | "For the other direction we conjecture the same." |
| 2025-11-11 | 2511.08515 | On the Computational Power of Extensional ESO | "extensional ESO captures NP-intermediate problems" |
| 2025-05-01 | 2505.00594 | Decomposing graphs into stable and ordered parts | dependent hereditary graph classes admit a monadically-stable/bounded-treewidth modelization |
| 2025-02-25 | 2502.18065 | Merge-width and First-Order Model Checking | bounded merge-width ≡ bounded flip-width |
| 2024-08-27 | 2408.14999 | The equational theory of the Weihrauch lattice with (iterated) composition | PSPACE-hardness problem solvable in PSPACE |

### math.AC (15)

| date | arXiv id | title | conjecture (verbatim snippet) |
|---|---|---|---|
| 2026-08-19 | 2608.18519 | The radial derivative on the graded Möbius algebra | $H_\beta$ log-concave and top-heavy in differential degree |
| 2026-08-18 | 2608.17771 | A $k$-Dimensional Version of the Largest Intersection Problem | exact formula for largest $\mathbb{F}_q$-rational-point intersection, $q\ge d+1$ |
| 2026-06-01 | 2606.02921 | Syzygies of Isotropic Kalman Varieties | long exact sequence relating structure sheaves |
| 2026-04-30 | 2604.27341 | Syzygies of the transfer ideal of the symmetric group | determinantal presentation of the elimination ideal |
| 2026-03-31 | 2603.29978 | The van der Waerden Simplicial Complex and its Lefschetz Properties | $A(vdw(n,k))$ fails Weak Lefschetz Property for $n\gg k\ge3$, $k$ odd |
| 2025-11-27 | 2511.22346 | Switching rook polynomial of collections of cells | correspondence holds in general (proved for convex cell collections) |
| 2025-09-15 | 2509.11977 | Polymatroidal ideals and their asymptotic syzygies | $i$th homological shift algebra generated in degrees $\le i$ |
| 2025-03-24 | 2503.18827 | Depth of Artin-Schreier defect towers | these are the only depth-one Artin-Schreier defect towers |
| 2025-03-03 | 2503.01647 | Volume Rigidity of Simplicial Manifolds | result extends to $k=d-2$ (verified $d=4,5,6$) |
| 2025-02-27 | 2502.19998 | Symbolic powers of polymatroidal ideals | every symbolic power $I^{(k)}$ componentwise linear, $\mathrm{reg}\,I^{(k)}=\mathrm{reg}\,I^k$ |
| 2025-01-13 | 2501.07319 | Edge ideals and their asymptotic syzygies | if $I(G)$ has linear resolution then $HS_i(I(G)^k)$ does too, $k\gg0$ |
| 2024-12-04 | 2412.03507 | Twisted Derivations in Algebraic Number Fields | necessary/sufficient condition for inner $(\sigma,\tau)$-derivations |
| 2024-12-04 | 2412.03500 | $(\sigma,\tau)$-Derivations of Number Rings with Coding Theory Applications | solution in $p^{th}$-cyclotomic ring of integers |
| 2024-10-23 | 2410.18008 | Birational geometry of blowups via Weyl chamber decompositions | answer affirmative for $X^3_8$ and $X^5_9$ |
| 2024-09-25 | 2409.17009 | The Hilbert scheme of points on a threefold | broken-Gorenstein-structure result is exhaustive |

## Part B — cs.LO curated leads (SURV/CONF, NOT yet opened/read past title+one-line description)

| source | year | open items named |
|---|---|---|
| arXiv:2407.18006 — "The Existential Theory of the Reals as a Complexity Class: A Compendium" | 2024 | NP vs ∃ℝ gap; oracle separations between NP/∃ℝ/PSPACE; boundary classification for geometric thickness, realization spaces, continuous game equilibria |
| arXiv:2504.04416 — "Meta-Mathematics of Computational Complexity Theory" | 2025 | whether P≠NP / circuit lower bounds are unprovable in weak arithmetic (PV₁, S¹₂) |
| arXiv:2402.03069 — "Fixed Point Theorems in Computability Theory" | 2024 | open questions in generalized numbering theory, Weihrauch degrees |
| arXiv:2603.05055 — "Modal Fragments: Expressive Power, Complexity, and Learning" | 2026 | finite-basis teachability, dichotomy theorems for generalized modal connectives |
| Dagstuhl Seminar 25211 — "The Constraint Satisfaction Problem: Complexity and Approximability" | 2025 | complexity/approximation limits of Quantified CSPs (QCSP), infinite-domain CSPs definable by FO formulas |
| Dagstuhl Seminar 25061 — "Logic and Neural Networks" | 2025 | provable strict satisfaction of logical constraints in neural architectures vs. soft-penalty loss; formal explanation/verification of continuous-model decision boundaries |

## Part C — math.AC curated leads (SURV/CONF, NOT yet opened/read past title+one-line description)

| source | year | open items named |
|---|---|---|
| Fields Institute "Recent Trends in Commutative Algebra" thematic program | 2024-2025 | Gröbner geometry/degeneration questions; multigraded-module homological invariants (Castelnuovo–Mumford regularity boundaries); positive-characteristic F-singularity/F-pure-threshold/test-ideal questions |
| "Open Problems in Commutative Ring Theory" (Cahen, Fontana, Frisch, Glaz) — numbered problem book | ongoing | numbered problems, actively being resolved 2023-2026; the specific unresolved-problem numbers were NOT enumerated by our sourcing pass — judge only that this is a live, numbered, actively-worked problem list as a class, not any specific problem from it |
| SLMath "Recent Developments in Commutative Algebra" program problem sessions; commalg.org tracking hub | 2024-2026 | F-regularity of cluster algebras in char p; **Lech's conjecture** (low-dim cases / universal e(S)/e(R) bounds) — famous, well-known, treat crowding as high/negative, not a discovery; **Evans–Griffith Small Syzygy conjecture** in mixed characteristic — also famous, same caveat; Conca–Herzog Koszul-property conjectures; linear-syzygy combinatorial classification for edge/hypergraph ideals; Boij–Söderberg extension to complete intersections/exterior algebras |

Caution disclosed to you: this last table's source (a browser AI-search tool) was less specifically
sourced (program names, not paper/seminar ids) than the others, and the Conca–Herzog /
linear-syzygy / Boij–Söderberg-extension items are not independently verified beyond that tool's
say-so — factor that uncertainty into your confidence, and feel free to mark axes "unclear" for
these sub-items if the one-line description isn't enough.

## Part D — one item explicitly OUT OF SCOPE for you (context only, do not analyze in depth)

arXiv:2604.03789 + arXiv:2605.25259 (a math.AC "AI resolves an open problem, Lean-4 verified"
pipeline paper pair, informally: Rethlas+Archon) is **already dispatched to a separate engine for
deep pre-chew** (a different task, asking specifically which open problems remain in the two
numbered problem lists these papers reference). Please do NOT duplicate that work. If you want to
comment on it at all, a single line noting its priority relative to the rest of this list is
enough — no table row needed.

## What we want from you

For EACH of the 20 Part A candidates, produce a compact table with columns: `arXiv id`, `certkind`
(Kind-1 / Kind-2 / unclear), `verifroute` (one short phrase, with an explicit YES/NO on whether
local-exhaustive-search-only is the only route), `crowding` (fresh / moderate / crowded / unclear),
`fit` (good / marginal / poor / unclear), and a 1-line verdict (`PURSUE` / `HOLD` / `DROP`, with a
one-clause reason).

For the Part B and Part C curated leads (10 total items/rows — treat each named open-item cluster
as one row, e.g. "Lech's conjecture" is its own row even though it's inside a larger source), give
the same treatment at the level the title/description alone supports, explicitly noting you have
not read the underlying survey/seminar/column in full.

End with a short summary: how many `PURSUE`, `HOLD`, `DROP` (across Parts A+B+C combined); which
3-5 candidates you'd personally look at first if you could only pick a few, with one sentence each
on why.
