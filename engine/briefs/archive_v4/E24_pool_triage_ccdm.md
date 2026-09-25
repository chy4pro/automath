# Task: triage a raw list of 40 conjecture-stating papers (cs.CC / cs.DM) — rank and flag, not solve

This is a TRIAGE task, not a proof task: we have sourced a raw list of arXiv papers that each
state a new conjecture in their abstract, and 5 leads to curated "open problems" columns. Nothing
below has been ranked or scored yet. We want your judgment on which of these are worth a solver's
time, using the four axes defined below, plus two specific flags. This is not a request to solve
any of the conjectures — it is a request to assess and rank them, and to be honest when you don't
have enough information to judge one (say "insufficient information to rank" rather than guessing
a plausible-sounding rank).

## The four ranking axes (apply these to every candidate)

1. **`certkind`** — what KIND of thing would a proof/refutation look like? We care most about
   candidates with a **finite, machine-checkable certificate** (Kind-1: e.g. a finite search space,
   a decidable combinatorial statement, something a computer could in principle verify end-to-end)
   over candidates that are open-ended "prove a general theorem for all n" statements requiring
   genuinely novel unbounded mathematics (Kind-2), because Kind-1 problems are far more tractable
   for our pipeline. For each candidate, say which kind it looks like, or state you cannot tell
   from the abstract alone.
2. **`verifroute`** — if someone claimed a proof, how would we independently verify it? Is there a
   clear, checkable route (a formal proof assistant statement, a finite computation, a well-known
   reduction to something else) or is verification itself going to be hard/expensive/subjective?
3. **Novelty / crowding** — is this a genuinely fresh, uncrowded conjecture, or is it already
   well-studied / likely to have many people working on it? (A rough proxy: how established is the
   named conjecture or the subfield; note explicitly that raw frequency/mention-count is NOT the
   same as importance — a conjecture nobody has attacked could be uncrowded because it's
   unimportant OR because it's a genuine gap.)
4. **Fit** — does the conjecture's mathematical content look like something within reach of a
   competent but not research-frontier-specialist attacker (i.e., does it require deep specialized
   machinery from a narrow subfield, or is it closer to elementary/intermediate combinatorics,
   complexity theory, or discrete math that a strong general mathematician could engage with)?

## The raw candidate list (40 papers stating a new conjecture in-abstract, 2024-08 to 2026-08, arXiv cs.CC and cs.DM; source: `orchestration/results/field_sweep_r1.md`, quoted verbatim below)

### cs.CC (15)
| date | arXiv id | title | conjecture (verbatim snippet) |
|---|---|---|---|
| 2026-07-31 | 2607.29453 | Quantum Algorithms for Modular Factorials | "the condition q\|(p-1) is a technical limitation... rather than an inherent obstruction" |
| 2026-06-23 | 2606.25121 | Intractability of Hilbert's Nullstellensatz implies algebraic hardness of permanent | "VNP_C not⊆ VP_C-bar implies P_C(nu) ≠ NP_C(nu)" |
| 2026-04-20 | 2604.17935 | How Much Cache Does Reasoning Need? | depth lower bound L=Ω(⌈k/s⌉·⌈log2 n/(Hmp)⌉) for KV-compressed transformers |
| 2026-04-14 | 2604.13026 | A complexity phase transition at the EPR Hamiltonian | "EPR* is in BPP" |
| 2026-04-05 | 2604.03947 | Uniform Sampling of Proper Graph Colorings via Soft Coloring and Partial Rejection Sampling | mixing parameter L bounded independently of n |
| 2025-12-26 | 2512.21922 | Poincaré Duality and Multiplicative Structures on Quantum Codes | nontrivial logical actions ⟹ fault-tolerant non-Clifford gates on qLDPC sheaf codes |
| 2025-11-11 | 2511.08515 | On the Computational Power of Extensional ESO | extensional ESO captures NP-intermediate problems |
| 2025-09-22 | 2509.17926 | Sketching approximations and LP approximations for finite CSPs are related | dichotomy: LP integrality gap ⟺ streaming lower bound / roundable LP ⟺ sublinear algorithm |
| 2025-06-26 | 2506.21084 | Timed Prediction Problem for Sandpile Models | (extensions of P-completeness/timed-crossover classification) |
| 2025-04-20 | 2507.12469 | Perfect diffusion is TC0 — Bad diffusion is Turing-complete | extension of results to imperfect-diffusion case |
| 2025-02-09 | 2502.06045 | Hardness of Hypergraph Edge Modification Problems | hardness result extends to all k-graphs F other than a fixed-size matching |
| 2024-12-27 | 2412.19623 | An unholy trinity: TFNP, polynomial systems, and the quantum satisfiability problem | low-error construction also works ⟹ SFTA ⊆ MHS |
| 2024-11-07 | 2411.04972 | Uniformity testing when you have the source code | O(min{d^{1/3}/ε^{4/3}, d^{1/2}/ε}) is optimal |
| 2024-10-24 | 2410.18650 | Counting Locally Optimal Tours in the TSP | true bound on locally-optimal tours is O(√(n!)) |
| 2024-10-10 | 2410.08051 | The Space Just Above One Clean Qubit | "½BQP cannot solve 3-Forrelation" |

### cs.DM (25)
| date | arXiv id | title | conjecture (verbatim snippet) |
|---|---|---|---|
| 2026-07-19 | 2607.18334 | Signed circulants at the Ramanujan bound | ρ_-(n) global minimum holds for all even n |
| 2026-06-26 | 2606.28315 | Pairwise Reflection Symmetry in Generalized Latin Rectangles | underlying group-theoretic structure may be unavoidable |
| 2026-06-26 | 2606.27961 | Transversal Difference Numbers in Finite Abelian Quotients | δ(G,H)=(2p-1)^2 for all odd primes p |
| 2026-04-25 | 2604.23188 | Binary Words Containing Few Abelian Squares | construction attains least-possible abelian-square count |
| 2026-03-16 | 2603.16004 | A Permutation Avoidance Game with Reverse Replies and Monotone Traps | winning strategy for all k, n sufficiently large |
| 2026-03-09 | 2603.08876 | Hierarchical threshold structure in Max-Cut with geometric edge weights | isolated cuts globally optimal among 2^{n-1} cuts for n≥7 |
| 2026-02-03 | 2602.04034 | Clonoids over vector spaces | finitely many clonoids A→B ⟺ |A|,|B| coprime order |
| 2026-01-26 | 2601.18715 | Additive sink subtraction | duality between additive sink subtraction and classical wall subtraction |
| 2026-01-26 | 2601.18071 | Remarks about Connection and Dirac matrices | L dominates both D and L^{-1} in weak Loewner sense |
| 2025-11-11 | 2511.08515 | On the Computational Power of Extensional ESO | (dup of cs.CC row above — cross-listed) |
| 2025-11-04 | 2511.02983 | Towards a geometric characterization of unbounded integer cubic optimization via thin rays | thin-ray characterization holds in all dimensions |
| 2025-09-12 | 2509.10070 | Toward Minimum Graphic Parity Networks | graphs belong to a newly-defined graph class |
| 2025-09-01 | 2509.01428 | Large induced subgraphs with prescribed degree parity | f_oe(G) ≥ f_o(G)/2 for all graphs G |
| 2025-08-05 | 2508.02985 | Chromatic discrepancy of locally s-colourable graphs | φ(G) ≥ χ(G)-s |
| 2025-07-19 | 2507.14473 | Graphs With the Same Edge Count in Each Neighborhood | fine-grained characterization is the correct answer generally |
| 2025-07-14 | 2507.10266 | (Δ-1)-dicolouring of digraphs | dichromatic number ≤ Δ-1 except two named exceptions |
| 2025-06-14 | 2506.12424 | Layered tree-independence number and clique-based separators | fractionally tree-independence-fragile ⟹ bounded independence degeneracy |
| 2025-05-07 | 2505.04543 | New bounds for proper h-conflict-free colourings | χ^h_pcf(G) ≤ hΔ+1, tight |
| 2025-04-27 | 2504.19201 | Expanding vertices to triangles in cubic graphs | T(G) ≤ (1/10)|V(G)|, tight for the Petersen graph |
| 2025-04-08 | 2504.05930 | Totally equimodular matrices: decomposition and triangulation | uncovered cases do not exist |
| 2025-02-25 | 2502.18065 | Merge-width and First-Order Model Checking | bounded merge-width ≡ bounded flip-width |
| 2024-12-30 | 2501.00157 | Alon-Tarsi for hypergraphs | bound holds for every hypergraph polynomial w/o permuting coefficients |
| 2024-11-25 | 2411.16548 | Bow Metrics and Hyperbolicity | (λ,μ)-bow metric ⟹ hyperbolicity, in general graphs |
| 2024-10-24 | 2410.18650 | Counting Locally Optimal Tours in the TSP | (dup of cs.CC row above — cross-listed) |
| 2024-10-11 | 2410.09257 | Two-person Positive Shortest Path Games Have Nash Equilibria... | terminal NE exists given a directed path to a terminal |

### 5 SURV/CONF leads (curated open-problems columns, NOT yet opened/read past their titles)
1. **"Nine lower bound conjectures on streaming approximation algorithms for CSPs"** (Noah Singer,
   SIGACT News Vol 56, 2025; arXiv:2510.10714, cs.CC, Oct 2025) — a column collating nine
   conjectural lower bounds against streaming algorithms for CSPs, "some of which appear for the
   first time." (Note: this specific column already has a SEPARATE, DIFFERENT pre-chew task
   dispatched elsewhere this round via a different engine — do not duplicate deep work on it here;
   a one-line note on its priority relative to the other 4 leads is enough.)
2. "Monochromatic Unit Squares" (Gasarch/Gezalyan/Parker, 2025) — combinatorial geometry.
3. "How hard is it to detect *some* cliques?" (Josh Burdick, 2024) — cs.CC, clique-detection
   hardness.
4. "Constructive Lower Bounds on Ramsey Numbers" (Cherukuri & Gasarch, 2025) — cs.DM-adjacent.
5. "The Complexity of the Shortest Vector Problem" (H. Bennett, 2023) — cs.CC, lattice problems.

## What we want from you

For EACH of the 38 distinct candidates above (2 are cross-listed duplicates — treat each arXiv id
once), produce a compact ranking table with columns: `arXiv id`, `certkind` (Kind-1 / Kind-2 /
unclear), `verifroute` (one short phrase), `crowding` (fresh / moderate / crowded / unclear), `fit`
(good / marginal / poor / unclear), and a 1-line overall recommendation (`PURSUE` / `HOLD` /
`DROP`, with a one-clause reason). For the 4 non-duplicate SURV leads, give the same treatment at
the level the title alone supports (explicitly note you have not read the columns themselves).

Be honest about uncertainty: if the title+snippet alone genuinely isn't enough to judge an axis,
write "unclear" rather than guessing — a wrong confident rank costs us more than an honest
"unclear." End with a short summary: how many `PURSUE`, how many `HOLD`, how many `DROP`, and
which 3–5 candidates you'd personally look at first if you could only pick a few, with one
sentence each on why.
