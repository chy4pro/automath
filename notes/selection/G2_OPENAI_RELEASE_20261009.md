DONE — Bounded catalogue sweep completed at the pinned release snapshot below. NO-HIT is a search result, not a proof of absence, openness, or priority; no manuscript or formal proof is verified by this report.

**Evidence and coverage.** READ = primary text inspected; SECONDARY = a record carried from our catalogues without reopening its original paper; LIVE CLAIM = a mathematical assertion in the release, including assertions accompanied by Lean documentation; NOT ACCESSIBLE = an attempted source could not be obtained. Classification abbreviations: C = CLOSED-BY-CLAIM, A = ADJACENT, N = NO-HIT. A C verdict concerns the specified target or bound, never automatic acceptance of the proof. All comparisons below are READ textual comparisons; every release theorem they reference remains a LIVE CLAIM.

READ: snapshot [fd4aeeb2](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), commit dated 2026-10-08 05:20 UTC; the downloaded README, history, CONTENTS, overview and formalization YAML were byte-compared with that commit. [README][readme] reports 719 manuscripts / 372 families. [History][history] reports three withdrawals, fourteen repairs and 300/719 top-line results with formalizations (about 42%). These are repository metadata, not an independent correctness count.

READ: all 372 titles; full description paragraphs and every abstract in **001–031, 087–101, 155–192** (83 extant families: 163 is absent). Additionally read full family entries 047, 049, 072, 073, 074, 076, 084, 132, 196, 197, 266 and 375. Other families received title screening and whole-CONTENTS keyword searches, not a full abstract read. The overview's discipline grouping was checked. Selected TeX introductions/statements and the scope notes linked below were read; no OpenAI Lean source was read or run. This is a statement/coverage audit, not a proof-loss audit or a new literature-priority search.

READ: both coordinator files were read first: [first screen](/work/notes/selection/openai_math_release_20261009.md), [372-title list](/work/notes/selection/openai_math_families_20261009.txt). All requested catalogues are accounted for below; the 133-file formal-conjectures catalogue was screened at title/description level as authorized. Historical discussion in the long famous-watch and pool files was selectively read; all target rows/cards/headings and supplementary target lists were checked. Truncated staging statements remain title-level comparisons.

**Corrections that matter for selection (READ comparisons; all new mathematics LIVE CLAIM).**

- **Erdős #167 is Tuza's triangle packing/covering conjecture. OpenAI family 167 is a different identifier.** Neither the Tuza shelf nor its old Haxell coefficient is closed by a planar-distance claim. The source distinction is explicit in [shortlist row 2](/work/notes/selection/shortlist_0908.md:22) and [old-record exclusions](/work/notes/selection/old_records_20261003.md:150).
- **Old-record B5 was missed:** family 021 claims the uniform bound h(k) ≤ Ck²/(log log(3k))² for arbitrary moduli with at most k prime factors, not merely primorial moduli. It supersedes the old O((k log k)²) bound and answers the quadratic-bound subquestion; it does not determine optimal order or supply a numerical C/onset for beating a finite table.
- **Old-record row 13 must split #304 from #18.** Family 025 claims the optimal order of unrestricted short Egyptian expansions (#304). The practical-number/factorial version #18 restricts the available divisors of the original integer. Neither its main statement nor its Lean scope preserves that restriction. #18 is A, not C; a small unrestricted unit-fraction expansion is not the requested divisor-subset statement.
- **#1082 is A, not C.** Family 167 gives n^(1−ε) distances for almost every pin, for each fixed ε>0, without an explicit convergence rate. It does not improve the linear coefficient for global distances in the no-three-collinear target. SECONDARY: the catalogue already records the stronger pinned floor(n/2) variant as false; it must not be reopened by conflating it with the global-distance question. Family 183 counts halving pairs/k-sets, not pinned distinct distances. Conversely, family 167's separate unit-pair bound does asymptotically supersede the positive n^(4/3) coefficient target in targets card 6, with no effective replacement coefficient/onset extracted here.
- Other C matches outside the initial keyword shortlist: Brennan 072; strong sensitivity 132; the De Giorgi dimension-eight endpoint 375. Hadwiger–Nelson 158 improves the lower bound to six but leaves six versus seven undecided. Family 179's manuscript classifies all Barker lengths, while its selected additional Lean statement covers only even lengths.

**Release evidence register.** Each row supplies the manuscript title/date, precise matched assertion, and the scope documented for Lean. “Full” below means the scope note claims the displayed theorem, not that this scout checked its implementation or kernel output. Every mathematical statement in this register is **LIVE CLAIM**; source/scope/history observations are **READ**. Abstract means an unnumbered abstract statement, not an invented theorem number. Numbered locators are taken from TeX statement environments/counters. H0 applies individually to every row: **history.md lists no withdrawal or named repair for these selected manuscripts**; that is not a claim that they never changed. Unlisted companion claims are not implicitly formalized.

| Family / manuscript (dated as indexed) | LIVE CLAIM: matched statement and locator | READ: documented Lean scope; history |
|---|---|---|
| [003][F003] — [The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane \Re s\gt 7/8 ](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) (2026-09-30) | All Dirichlet L-functions (including ζ) and finite-order Hecke L-functions over Q(√−3) have no zero with Re(s)>7/8; the principal pole at 1 is allowed. No conductor/height restriction. The displayed assertion is the abstract, not a least-prime theorem. | [Scope][L003]: Full displayed zero-free assertion documented; separate comparator entries for Dirichlet and Hecke statements. No effective Linnik/powers corollary certified here. YAML: listed comparators registered. H0. |
| [012][F012] — [The joint Dickman law for consecutive integers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf) (2026-09-24) | For every 0<a,b<1, natural density of n with P⁺(n)≤n^a and P⁺(n+1)≤n^b is ρ(1/a)ρ(1/b). Each strict ordering of the two largest prime factors has density 1/2. Abstract/scope; no uniform long-block guarantee. | [Scope][L012]: Full joint-density and ordering-density statements documented. YAML: none of these comparators registered; JointDickman absent. H0. |
| [020][F020] — [Squarefree values of quartics and power-free values of polynomials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf) (2026-09-24) | For every irreducible integer polynomial f of degree d≥4, k=d−2, if no prime kth power divides all f-values, the positive integers n≤X with f(n) k-free number c_f X+o_f(X), c_f>0 the local Euler product. Zero excluded, negative values allowed. Quartics give squarefree values. | [Scope][L020]: Full all-d≥4 conclusion documented, incorporating the cited higher-degree input; no coefficient-height, monicity or primitivity restriction. YAML: listed comparators registered. H0. |
| [021][F021] — [A quadratic bound for Jacobsthal's function](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) (2026-09-25) | [Theorem 1.1, thm:main][S021]: ∃ absolute C>0, ∀ integer k≥1, h(k)≤Ck²/(log log(3k))². h is the worst guaranteed coprime interval length over positive moduli with ≤k distinct primes and all signed starting positions. Natural logs. C not numerical. | [Scope][L021]: Full strengthened bound and the weaker quadratic comparator documented; optimal order explicitly not determined. YAML: Jacobsthal registered; JacobsthalImproved absent. H0. |
| [025][F025] — [Short Egyptian fractions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf) (2026-09-25) | [Theorem 1.1, thm:main][S025]: ∃ absolute c₁,c₂>0,b₀, ∀ integers b≥b₀, c₁ log log b≤N(b)≤c₂ log log b, where N(b)=max over 1≤a<b of the minimum number of distinct positive unit fractions summing to a/b. No gcd restriction. Constants/onset unspecified. | [Scope][L025]: Full short-expansion statement documented; also exact-k expansion counts and prescribed-denominator statements. No restriction to divisors of the original b or a factorial. YAML: EgyptianFractions registered; ShortEgyptianFractions absent. H0. |
| [029][F029] — [Primitive roots for every admissible integer base](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf) (2026-10-04) | For every integer a that is neither −1 nor a square, ∃c_a>0,x₀(a), ∀x≥x₀, at least c_a x/(log x)² primes in (x,2x) have primitive root a. Abstract. No uniform a-constant or numerical onset. | No family Lean link or matching YAML manuscript entry located. H0. |
| [047][F047] — [An explicit failure of complex affine-space cancellation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf) (2026-09-23) | [Theorem 1.1, thm:main][S047]: ∃ integral complex affine algebra A of dimension four with A[w]≅C[x₁,…,x₅] and A≄C[x₁,…,x₄]. This refutes unrestricted affine-space cancellation over C in dimension four. | [Scope][L047]: Main dimension-four counterexample documented. Stable-coordinate and fibration consequences are not all included in that scope. YAML: listed comparators registered. H0. |
| [072][F072] — [Brennan's conjecture and sharp inverse-square integral means](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf) (2026-09-24) | [Theorem 1.1, thm:main][S072]: for every simply connected plane domain W with ≥2 boundary points on the Riemann sphere, every conformal bijection φ:W→D and every 4/3<s<4, ∫_W abs(φ′)^s dA<∞. Also B_S(−2)=1. | [Scope][L072]: Brennan and sharp endpoint failures documented, with inverse-square means; not a verification of all family companions. YAML: listed comparators registered. H0. |
| [091][F091] — [The logarithmic Brunn–Minkowski conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf) (2026-09-23) | For every n≥1, full-dimensional origin-symmetric convex bodies K,L⊂R^n and 0≤t≤1, their logarithmic Wulff combination has volume ≥vol(K)^(1−t)vol(L)^t. Paper also claims additive L_p Brunn–Minkowski for 0<p<1 and the even-log-concave-measure scalar B-conjecture. Abstract/scope. | [Scope][L091]: Logarithmic volume inequality documented without smoothness/unconditionality; scope does not list every measure/L_p consequence as a separate formal theorem. YAML: listed comparators registered. H0. |
| [132][F132] — [A superquadratic separation between sensitivity and block sensitivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf) (2026-09-25) | [Theorem 1.1, thm:main][S132]: ∀C>0 ∃n≥1 and nonconstant total Boolean f with bs(f)>C s(f)². More precisely ∀integer d≥1 a construction has bs(f)/s(f)²≥2^d/[4(d+2)²]. | [Scope][L132]: Full ratio separation documented; also a fixed α>2 and a sequence with s(f)^α≤bs(f,0)→∞. YAML: listed comparators registered. H0. |
| [155][F155] — [A translational tile with no fully periodic tiling in dimension three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/paper.pdf) (2026-09-23) | ∃ finite tile T⊂Z³ admitting a translational tiling but no tiling complement invariant under a finite-index subgroup. Its unit-cube thickening tiles R³ almost everywhere but has no fully periodic tiling, even with arbitrary real translations. Abstract/scope. | [Scope][L155]: Full lattice/Euclidean counterexample and least lattice dimension three documented. No spectral-set or weak-tiling equivalence. YAML: listed comparators registered. H0. |
| [158][F158] — [The Euclidean plane is not five-colorable](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf) (2026-09-23) | [Theorem 1.1, thm:main][S158]: every map R²→{1,…,5} has a monochromatic unit-distance pair; no regularity assumption. Thus 6≤χ(R²)≤7. | [Scope][L158]: Full arbitrary-coloring lower bound and seven-color upper bound documented; no choice between six and seven. YAML: listed comparators registered. H0. |
| [159][F159] — [Quasipolynomial Bounds for Arithmetic Progressions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) (2026-09-23) | For each integer k≥3, ∃C_k,c_k,ε_k>0 with r_k(N)≤C_k N exp(−c_k(log N)^ε_k); constants depend only on k. Abstract does not give numerical values/onset. Every positive-integer set with divergent reciprocal sum contains APs of every finite length. | [Scope][L159]: Reciprocal-sum conclusion documented. Scope explicitly does not include the displayed quantitative Szemerédi estimate as the selected statement. YAML: none of these comparators registered; ErdosReciprocal absent. H0. |
| [160][F160] — [Quantitative Superexponential Bounds for van der Waerden Numbers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf) (2026-09-23) | ∃ absolute c>0 and K₀ such that ∀integers k≥K₀ and r≥2, W_r(k)>k^(c k floor(log₂r)). In particular W_r(k)^(1/k)→∞ for each fixed r≥2. Abstract; no numerical c,K₀. | [Scope][L160]: Uniform quantitative lower bound and fixed-r superexponential conclusion documented. YAML: listed comparators registered. H0. |
| [164][F164] — [Monochromatic finite sums and products in the positive integers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/paper.pdf) (2026-09-23) | For every finite coloring of positive integers and every k≥1, ∃a k-element set for which all nonempty subset sums and all nonempty subset products have one common color. Abstract; no finite interval-size bound. | No family Lean link or matching YAML manuscript entry located. H0. |
| [166][F166] — [The higher-dimensional Erdős distinct-distances conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/paper.pdf) (2026-09-23) | For every fixed integer d≥3, ∃c_d>0 such that every set of n≥2 distinct points in R^d determines ≥c_d n^(2/d) distinct distances. Abstract; c_d not numerical. | No family Lean link or matching YAML manuscript entry located. H0. |
| [167][F167] — [The weak pinned planar distance theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf) (2026-09-23)<br>[A power saving for planar unit distances](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf) (2026-09-23) | [Pinned Theorem 1.1 / Corollary 1.2][S167p]: ∀fixed ε>0, sup over all n-point planar P of #{x∈P: abs(D_x(P))<n^(1−ε)}/n→0. No separation or general-position assumption, no explicit rate. [Unit-pair Theorem 1.1][S167u]: ∃C>0, 1≤β<4/3, ∀integer n≥0, u(n)≤Cn^β. C,β not numerical. | [Scope][L167]: Both statements separately documented, with PinnedDistances and PlanarUnitDistances comparators. Neither is the #1082 linear-coefficient theorem. YAML: PinnedDistances registered; PlanarUnitDistances absent. H0. |
| [170][F170] — [The sharp logarithmic exponent of r(5,t)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/paper.pdf) (2026-09-24)<br>[Sharp logarithmic exponents for fixed off-diagonal Ramsey numbers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/paper.pdf) (2026-09-24) | For every fixed integer s≥5, ∃C_s>0 and ∀ε>0 ∃t₀(s,ε), ∀t≥t₀: t^(s−1)/(log t)^(s−2+ε)≤r(s,t)≤C_s t^(s−1)/(log t)^(s−2). Equivalently logarithmic exponent s−2+o(1). The first companion is s=5. | [Scope][L170]: Fixed-s logarithmic exponent, including s=5, documented. Constants/onsets depend on s; no diagonal uniformity. YAML: none of these comparators registered; RamseyFive, SharpLogRamsey absent. H0. |
| [171][F171] — [The hypercube Ramsey number has linear order](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/paper.pdf) (2026-09-23) | ∃absolute C>0, ∀n≥0, two-color R(Q_n)≤C2^n. Abstract gives linear order in the cube’s vertex count; no numerical C. | No family Lean link or matching YAML manuscript entry located. H0. |
| [173][F173] — [A proof of Seymour’s second-neighborhood conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf) (2026-09-23) | Every nonempty finite oriented graph has a vertex v with abs(N₁⁺(v))≤abs(N₂⁺(v)); N₂⁺ is directed distance exactly two, no loops/opposite pairs. The directed-triangle corollary assumes δ⁺,δ⁻≥n/3 together. | [Scope][L173]: Full second-neighborhood statement documented; corollary package not advertised as the selected formal theorem. YAML: listed comparators registered. H0. |
| [175][F175] — [Integral and fractional expectation thresholds are equivalent](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/paper.pdf) (2026-09-23)<br>[Talagrand’s discrete-convexity conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/paper.pdf) (2026-09-23)<br>[Graph Decompositions at the Integral Expectation Threshold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/graph-threshold-decompositions.pdf) (2026-10-05) | Scope gives q_f(F)≤25·512⁴ q(F) for every nonempty proper increasing family on a finite nonempty ground set, both cover budgets 1/2. Discrete convexity: k=2⁷⁵, 0<p<1, μ_p(F)≥1−1/k implies subsets not contained in a union of k members are p-small (cover cost ≤1/2), with repeated members allowed. Graph companion asserts universally bounded fixed edge pieces and universal threshold factor; no common embedding required. | [Scope][L175]: Two Talagrand statements documented. Graph-decomposition companion is not in the scope/YAML source list. No general Conjecture 6(a) booster statement. YAML: listed comparators registered. H0. |
| [176][F176] — [The second Kahn–Kalai conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf) (2026-09-24) | For every n≥2 and finite simple H with h≥1 edges and ≤n vertices, p_c(n,H)≤min{1,2048e⁵⁰ p_E(n,H)(1+log₂h)} in the source statement; p_E requires expected copies ≥1/2 for every subgraph of H. | [Scope][L176]: Actual containment/expectation-threshold comparison documented; no arbitrary monotone-family small-set booster. YAML: listed comparators registered. H0. |
| [179][F179] — [The circulant Hadamard conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf) (2026-09-23) | [Theorem 1.1][S179]: ∀positive integer n, a real circulant Hadamard matrix of order n exists iff n∈{1,4}. The manuscript consequence says Barker sequences of length n>1 exist iff n∈{2,3,4,5,7,11,13}. | [Scope][L179]: Full circulant classification with witnesses; additional Barker comparator only positive even lengths {2,4}. Odd-length classification not included in that additional statement. YAML: CirculantHadamard registered; EvenBarker absent. H0. |
| [181][F181] — [A linear cycle-and-edge decomposition of every graph](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/main.pdf) (2026-09-24) | ∃absolute C>0 such that every finite simple undirected graph on n vertices has an edge partition into ≤Cn simple cycles or singleton edges, including edgeless/small graphs. Abstract/scope; optimal C not determined. | [Scope][L181]: Full cycle/single-edge decomposition documented. No double-cover multiplicity or total cycle-length bound. YAML: listed comparators registered. H0. |
| [183][F183] — [A power saving for planar halving lines](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf) (2026-09-25) | ∃absolute ε>0,C,n₀ such that every even n≥n₀ and every n-point planar set with no three collinear have ≤Cn^(4/3−ε) halving pairs. Description also claims O(n(k+1)^(1/3−ε₀)) strictly separable k-subsets for 1≤k≤n/2, ε₀>0. Constants/exponents/onset nonquantitative. | [Scope][L183]: Halving pairs and level-switch bounds under additional generic-position assumptions documented; do not label the entire k-set companion package formalized. YAML: none of these comparators registered; HalvingLines absent. H0. |
| [184][F184] — [Correspondence coloring graphs with a forbidden clique](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf) (2026-10-05)<br>[A logarithmic independence bound for clique-free graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/paper.pdf) (2026-09-25) | For fixed r≥4, ∃c_r>0, ∀K_r-free n-vertex graphs of average degree d≥2, α(G)≥c_r n log d/d. Companion: for every fixed excluded ordinary subgraph F, correspondence χ≤C_F Δ/logΔ for sufficiently large Δ; no numeric C_F or onset in abstract. | [Scope][L184]: Independence theorem only documented. Correspondence/list/ordinary-coloring companion not listed in scope/YAML. YAML: listed comparators registered. H0. |
| [186][F186] — [A uniform influence bound for hypergraph properties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf) (2026-10-05)<br>[A Sharp Threshold Bound for Monotone Graph Properties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf) (2026-09-25) | Graph scope: ∀n≥2, nontrivial increasing relabeling-invariant graph property, 0<ε<1/2, p_(1−ε)−p_ε≤2¹⁹ log(1/(2ε))/(log n)². Hypergraph abstract: fixed r≥3, relabeling-invariant Boolean f, 0<p<1, Var_p(f)≤C_r I_p(f)/(log n)^(r/(r−1)), without monotonicity. | [Scope][L186]: Graph threshold-width bound documented with constant 2¹⁹; hypergraph/nonmonotone companion not listed in scope/YAML. YAML: none of these comparators registered; SharpThreshold absent. H0. |
| [189][F189] — [Cycle--clique Ramsey numbers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cycle-clique-Ramsey-numbers-September-25-2026/Cycle-clique-Ramsey-numbers-September-25-2026.pdf) (2026-09-25) | Theorem 1.1 / abstract: ∀integers m≥n≥3, (m,n)≠(3,3), R(C_m,K_n)=(m−1)(n−1)+1; R(C₃,K₃)=6. No large-size onset. | [Scope][L189]: Complete displayed parameter range and exceptional value documented. YAML: none of these comparators registered; CycleCliqueRamsey absent. H0. |
| [196][F196] — [A Torsion-Free Group Algebra with Zero Divisors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf) (2026-09-23) | [Theorem 1.1, thm:main][S196]: ∃finitely presented torsion-free G and nonzero α,β∈F₂[G] with αβ=0; G has a finite two-dimensional classifying space. | [Scope][L196]: Full counterexample documented, including torsion-freeness and nonzero factors; not merely a finite multiplication comparator. YAML: listed comparators registered. H0. |
| [375][F375] — [A positive resolution of De Giorgi's conjecture in dimension eight](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf) (2026-09-26) | [Theorem 1.1][S375]: any C² u:R⁸→(−1,1) with Δu=u³−u and ∂₈u>0 has u(x)=tanh((e·x−c)/√2), e∈S⁷,e₈>0,c∈R. Theorem 1.2: every stable C² v:R⁷→[−1,1] solving that equation is ±1 or a planar transition; no energy-growth assumption. | No family Lean link or matching YAML manuscript entry located; requested docs/375.md returned 404. H0. |

READ scope caution: [167 Lean notes][L167] say the unit-distance theorem “is not included” in the pinned-result paragraph, then explicitly describe the separate unit-distance formalization and list a second comparator. The [YAML][yaml] registers PinnedDistances but does **not** register PlanarUnitDistances at this same commit. The notes claim two formalizations, with an index mismatch; no code was inspected to resolve it. The same mismatch affects all listed comparators for 012, 159, 170, 183, 186 and 189, and selected additional comparators for 021, 025 and 179 (enumerated in the register). YAML is a declaration/configuration index, not proof-check output. Do not silently promote a documentation claim into a replayed formal result.

**A1. Famous-watch: all 18 rows** ([source](/work/notes/selection/famous_watch.md)). Evidence on every row: READ comparison; cited release assertions LIVE CLAIM.

| Row | Target | Verdict | Exact distinction / hit |
|---|---|---|---|
| 1 | Complex structure on S⁶ | N | No complex-atlas/integrability claim located; the S⁶ in family 375 is a sphere of real direction vectors. |
| 2 | Kaplansky zero divisors | C 196 | Torsion-free group and nonzero F₂-group-ring factors with zero product. |
| 3 | Lonely runner | N | No matching runner theorem located. |
| 4 | Agrawal | N | No matching primality/polynomial-congruence counterexample located. |
| 5 | Kourovka 20.76 | N | No matching p-group abelian-subgroup bound located. |
| 6 | Erdős #699 | N | No matching binomial-gcd theorem located. |
| 7 | Erdős #982, convex pinned distances | A 167,183 | Weak sublinear pin guarantee; halving-pair count. Neither gives the convex floor(n/2) target. |
| 8 | Erdős #617, balanced coloring | N | No matching all-r balanced-coloring statement located. |
| 9 | Erdős #779, Deaconescu | N | No primorial-plus-prime assertion located. |
| 10 | Zariski cancellation | C 047 | Counterexample over C in dimension four; no claimed resolution of the dimension-three residual question. |
| 11 | Casas–Alvero | N | No common-root-with-every-derivative result located. |
| 12 | Circulant Hadamard | C 179 | Positive orders exactly 1 and 4. |
| 13 | Jacobian conjecture, dimension two | N | Abelian-variety Jacobians in 032 and analytic Jacobian determinants elsewhere are not polynomial invertibility. |
| 14 | Five-cycle double cover | A 181 | Cycle/single-edge partition covers each edge once, with O(n) pieces; no five-color double cover. |
| 15 | Kalai/Kahn–Kalai Conjecture 6(a) | A 175,176,186 | Expectation-threshold comparison, graph containment, and symmetric-property threshold widths differ from the general monotone-family small-coordinate booster assertion. |
| 16 | Andrews–Curtis | N | No matching balanced-presentation moves result located. |
| 17 | Conway 99 | N | No strongly regular (99,14,1,2) graph resolution located. |
| 18 | Collatz | N | No matching universal integer-orbit statement located. |

READ: for row 15, the original [Kahn–Kalai paper, Conjecture 6(a)](https://arxiv.org/html/math/0603218v2) asks, for each C, for constants K,δ>0 and a coordinate set of size ≤K log(1/μp(F)) boosting conditional measure by 1+δ for every (C log(1/p),p)-optimal monotone F. None of the three displayed release statements asserts this. The general label “Kahn–Kalai” is not a closure match. Additional shelf exclusions: Kourovka 19.25 N; Erdős #307 N; other WOWII items N; Kaplansky's already-refuted unit conjecture A 196 (different group-ring assertion, not a new unit-conjecture resolution).

**A2. Old records: all 18 rows, Part B and exclusions** ([source](/work/notes/selection/old_records_20261003.md)). Evidence: READ comparison; release assertions LIVE CLAIM.

| Row | Target | Verdict | Difference |
|---|---|---|---|
| 1 | #1066 penny-graph independence | A 158,167,184 | Plane coloring/unit-pair exponents and general clique-free independence do not give a new explicit linear penny-graph independence coefficient. |
| 2 | #156 smallest maximal Sidon set | N | No matching minimum-maximal-size statement. |
| 3 | #1082 no-three-collinear pins | A 167,183 | Fixed-ε sublinear pin guarantee / halving statistic; no requested linear improvement. |
| 4 | #902 common dominators in tournaments | A 173 | One vertex with a large second out-neighborhood is not a common dominator for each prescribed vertex set. |
| 5 | #1033 triangle degree sum | N | No matching degree-sum guarantee. |
| 6 | #1182 connected 3-good graphs | A 189 | Cycle–clique formula includes the cycle subclass; it does not classify arbitrary sparse connected 3-good graphs. |
| 7 | #509 polynomial lemniscate covers | N | No corresponding covering-count bound located. |
| 8 | #790 no element sums from other distinct elements | A 164 | Monochromatic finite sums/products in a coloring supplies no extremal upper bound for this forbidden-sum family. |
| 9 | #789 equal subset sums/equal cardinalities | N | No matching subset-cardinality assertion. |
| 10 | #187 long monochromatic APs | A 160 | Finite van der Waerden interval growth, not the infinite coloring/common-difference control asked here. |
| 11 | #336 exact-order asymptotic bases | N | No matching exact-order construction. |
| 12 | #222 gaps between sums of two squares | N | Prime gaps and polynomial power-free values are different sets. |
| 13a | #304 unrestricted short Egyptian fractions | C 025 | Uniform maximum over numerators has order log log b. |
| 13b | #18 practical numbers / n! divisor sums | A 025 | Original divisor/factorial restrictions are absent. |
| 14 | #295 Egyptian denominators ≥N | A 025 | Short length at fixed rational denominator and one prescribed denominator do not give the all-denominators-lower-bounded optimization. |
| 15 | #887 divisors above square root | N | No matching short-divisor-interval statement. |
| 16 | #17 cluster primes | N | No matching cluster-prime extremal guarantee. |
| 17 | #33 additive complements to squares | N | No matching complement-size theorem. |
| 18 | #1109 squarefree A+A | A 020 | One polynomial's squarefree-value density is not a set whose every pair sum, including doubles, is squarefree. |
| B1 | #1181 missing prime in short block | N | No displayed bound for that least missing prime. |
| B2 | #1093 positive binomial deficiency | N | No matching deficiency bound/construction. |
| B3 | #650,#709,#711,#860 distinct multiples | N each | No matching interval SDR/matching theorem. |
| B4 | #375 Grimm; #962 large-prime blocks | A 012 each | Natural density for two consecutive integers, not distinct representatives / uniform control of an arbitrary long block. |
| B5 | #687/#970 Jacobsthal | C 021 for old upper-bound target; A for full optimal-order questions | Arbitrary-modulus theorem subsumes the primorial upper bound; no sharp order or new certified small table. |

| Exclusion-table entry | Verdict | Difference |
|---|---|---|
| #901 property B | N | No matched extremal minimum-edge/non-2-colorable-hypergraph coefficient. |
| #104 unit circles | A 167 | Unit pairs of input points differ from counting radius-one circles incident with ≥3 input points. |
| #812/#1030 Ramsey increments | A 170 each | Fixed-s asymptotic r(s,t), not finite increments or their requested constants. |
| #167 Tuza | N | Identifier collision with family 167; triangle transversal/packing remains unmatched. |
| #170/#530/#272 | N each | No matching catalogue difference-basis / respective variant statement. |
| #817; #866 | A 159; N | AP-free cardinality bounds do not settle #817's subset-sum restriction; no #866 match. |
| #876 subset sums | A 164 | A finite coloring existence theorem does not give the catalogue's quantified extremal coefficient. |
| #201 | A 159 | A bound on r_k(N) does not supply an explicit comparison constant c_k in c_kR_k≤G_k≤R_k. |
| #1221 circle spacings | N | No matching sequential-spacing divergence assertion. |
| #1184 smooth blocks | A 012 | Two-shift natural density is not uniform smooth-number density in short translated blocks. |
| Product prime factors / #784 | N | No matching general-divisor or prime-only bound located. |
| Sidon/B₃/B₂[g]; cube C₄; subset sums | N; A 171; A 164 | Respectively unmatched constants; Ramsey of Q_n versus C₄-free subgraphs of Q_n; finite-color existence versus extremal subset sums. |

**A3. Twelve target cards and five retained extras** ([source](/work/notes/selection/targets_20261003.md)). Evidence: READ comparison; release assertions LIVE CLAIM.

| Card | Target | Verdict | Difference |
|---|---|---|---|
| 1 | Hypercube C₄ density | A 171 | Ramsey number of the whole cube in a complete host, not extremal edge density inside the cube. |
| 2 | Union-closed frequency | A 175 | A p-small cover/discrete-convexity assertion is not an element-frequency ≥c assertion for each union-closed family. |
| 3 | Caccetta–Häggkvist / directed triangles | A 173 | Seymour's theorem concerns second neighborhoods. Its directed-triangle corollary requires both δ⁺≥n/3 and δ⁻≥n/3; the target assumes only the out-degree bound. |
| 4 | Infinite-sequence star discrepancy | N | No matching sequence discrepancy constant. |
| 5 | Minimum overlap | N | No matching autocorrelation/overlap constant. |
| 6 | Planar unit-distance coefficient | C 167, asymptotically | β<4/3 beats any positive n^(4/3) leading coefficient eventually; β,C and comparison onset are unspecified. No finite-n numerical replacement certified. |
| 7 | Finite B₃ | N | No matching leading constant. |
| 8 | B₂[6] unordered sums | N | No matching leading constant or rational certificate. |
| 9 | Binary Sidon / distance-five codes | N | No matching binary-code/Sidon capacity statement. |
| 10 | Linnik exponent | A 003 | A zero-free half-plane does not itself state the catalogue's least-prime exponent with its dependencies/onset. No deduction attempted. |
| 11 | Restricted sum–difference exponents | N | No matching form-specific projection/cardinality exponent. Kakeya-family abstracts were checked as a possible false friend. |
| 12 | Diagonal Ramsey base | A 170 | Fixed s, t→∞ does not allow s=t→∞. |
| Extra | Real sum–product | A 164 | Monochromatic subset sums/products are not a cardinality inequality for AA and A+A. |
| Extra | Almost primes between squares | N | No all-n P₂/P₃ statement matched. |
| Extra | Primes between consecutive powers | A 003 | No explicit all-n replacement of the 86th-power theorem displayed. |
| Extra | Hadwiger–Nelson | C 158 for six-color lower bound; A for exact χ | Claim 6≤χ(R²)≤7 does not choose six or seven. |
| Extra | Four MOLS of order 22 | N | No four-square construction; family 266's mutually unbiased bases are different objects. |

READ locator for card 3: [Seymour source, cor:directed-cycle-consequences, part (ii)][S173cycle]. Its two-sided degree hypothesis is explicit. The Lean scope documents Seymour's main theorem, not this entire corollary package.

**A4. Transfer targets** ([ranked rows](/work/notes/selection/transfer_targets_20261002.md:34), [additional candidates](/work/notes/selection/transfer_targets_20261002.md:56)). Every entry below is **READ / N**, meaning no matching displayed release statement or quantitative replacement was located.

| Ranked entry | Verdict | Extra Part-1 candidates, each N |
|---|---|---|
| 1 Sonar sequences | N | Modular sonar; Costas arrays |
| 2 Weak Sidon | N | Infinite Sidon (title screen here; skipped in the original transfer study) |
| 3 g-thin Sidon / g-Golomb | N | Sum-version B₂[g] separately; k-fold Sidon |
| 4 Difference triangle sets / strict OOCs | N | Cyclic OOCs separately |
| 5 Manhattan-diameter DDC | N | Difference bases (covering, not distinct differences) |
| 6 Sidon boxes / Golomb rectangles | N | Sidon in Z_N; Sidon in arbitrary finite abelian groups |
| 7 Sidon in unions of intervals | N | B_h, h≥3 |
| 8 Hexagonal-grid / Euclidean-diameter DDC | N | LM rulers |
| Unnumbered Golomb-ruler row | N | Repeated appearances in the derivation sections have the same verdict. |

**A5. September shortlists.** Evidence: READ comparison; release assertions LIVE CLAIM. Grouped N lists assign N to every explicitly named item.

| Source / rows | Verdict and difference |
|---|---|
| [shortlist_0908](/work/notes/selection/shortlist_0908.md): 1 #375 | A 012: typical consecutive largest-prime factors do not prove Grimm for every composite block. |
| Same: 2 #167; 3 #128; 4 #23; 5 #779; 6 #458 | N each: Tuza, sparse halves, triangle-free bipartization, Deaconescu, and lcm inequality respectively. |
| [thin_screen](/work/notes/selection/thin_screen_0908.md): 1 #377 | N: missing-prime reciprocal sum for central binomials not matched. |
| Same: 2 #859 | A 025: Egyptian fractions/divisor sums are related, but no density-of-representing-integers exponent or explicit constant is stated. |
| Same: 3 #1084 | A 167,166: planar unit pairs / total distinct distances in dimension ≥3 do not give the three-dimensional contact-number constant. |
| Same: 4 #1109 | A 020: squarefree polynomial values, not pairwise squarefree sumsets. |
| Same rejected: #160 | A 159,160: monochromatic-AP avoidance does not require three colors on every 4-AP. |
| Same rejected: #302 | A 025: expansions of a rational differ from the largest subset avoiding 1/a=1/b+1/c. |
| Same rejected: #817; #961; #100 | A 159; A 012; A 167 respectively: subset-sum restriction; long smooth runs; diameter/linear-distance target, not the displayed weak pin theorem. |
| Same rejected: #1063,#872,#945,#1095,#535 | N each. |
| [full_closure](/work/notes/selection/full_closure_shortlist_0907.md): #375,#982,#1082,#556 | A 012; A 167/183; A 167/183; A 189 respectively. #556 is a three-color cycle Ramsey problem, not two-color cycle–clique Ramsey. |
| Same screen: #19,#64,#167,#398,#628,#743,#993,#114,#1041,#580,#742,#475,#488,#617,#699,#287,#506,#307 | N each; no closure asserted from a generic graph/cycle/circle keyword. |
| Same decision: #708,#324,#23,#128,#68 | N each: lcm-type counting, polynomial Sidon, bipartization, sparse halves, factorial-series irrationality. |

**A6. Orchestration pool** ([TARGETS](/work/orchestration/TARGETS.md)). Evidence: READ comparison; release assertions LIVE CLAIM. Repeated ranking/evidence rows inherit their target's verdict.

| Pool component | Per-target verdict |
|---|---|
| Main ranked pool and gates | Kaplansky C196; #982 A167/183; Lonely Runner N; Agrawal N; Kourovka20.76 N; #699 N; #617 N; #779 N; #307 N. |
| Watch list, lines 426ff | #97 A167 (convex equidistance condition differs from weak pin count); #107 A183 (convex-n-gon threshold f(n)=2^(n−2)+1 differs from counting halving pairs); #128 N; #647 N; #835 N; #1082 A167/183; Fuglede dimensions 1–2 A155 (aperiodic tiling in dimension 3 is not spectral iff tiling in dimensions 1–2); Babai–Seress N; Brennan C072; Moser's worm N. |
| Excluded, lines 435ff | Dickson N; Oppermann N; first Hardy–Littlewood N; #855 N; Lemoine N; Hall N; Lehmer/Mahler N; general Hadamard existence A179 (circulant classification only); Wall–Sun–Sun N; Collatz N; Andrews–Curtis N; second Hardy–Littlewood N; Conway99 N; WOWII160/100/141/19/198a/314/40 N each. |
| Ambiguous exclusion “Catalan related” | N at supplied-title level only: family 005 claims irrationality of Catalan's constant; the pool does not identify a constant question. Do not silently equate it with Catalan's exponential equation. |
| Historic active lines, 443ff | ETP677→255 N; WOWII133 N; WOWII61 N. |
| MINED STAGING rows 1–5, 503ff | 2608.12425#3 N; 2608.15525#1 N; 2608.11578#2 N; 2608.15525#0 N; 2608.11578#1 N. Comparisons are limited to the truncated regularity/domination/digraph statements supplied in the pool. |
| S′, 528ff | A100434 conjectures1/2/3 N; A211417 general_divisibility_strong N and thirty_mul_sub_one_dvd_a N; Fernandes conjecture1 N. |
| Selection0824 appendix | Kourovka16.95 N; total-domination target arXiv:2606.27961 N; ZC1 for A₇ N. |

**A7. Formal-conjectures catalogue: all 133 file titles** ([fc_catalog](/work/notes/fc_catalog.md)). Evidence: READ title/description comparison, not a formal-statement equivalence audit. Entries below specify C/A individually; the subsequent grouped lists assign N separately to every remaining file. No OpenAI Lean code was inspected.

| File (path relative to catalogue headings) | Verdict | Difference / scope |
|---|---|---|
| Arxiv/2104.00502/BarkerSequence.lean | C179 | Full manuscript length classification; Lean additional statement even lengths only. |
| Arxiv/2208.14736/ZariskiCancellation.lean | C047 | Refutes general characteristic-zero cancellation in dimension four, not every residual dimension. |
| Arxiv/2402.13202/CirculantHadamard.lean | C179 | Same positive-order classification. |
| Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean; Paper/WeakTiling.lean | A155 each | Periodic translational tiling differs from spectrality and weak tiling. |
| Arxiv/2605.02731/DeanCycles.lean | A181 | Linear cycle/edge decomposition does not force a cycle of length 0 mod k under minimum degree k. |
| Arxiv/2606.03696/BondyLongestCycles.lean | A181 | No conclusion about paths remaining outside each longest cycle. |
| Arxiv/2607.03582/LpRogersShephard.lean | A091 | L_p Brunn–Minkowski for 0<p<1 is not the planar p>1 Rogers–Shephard equality-case classification. |
| Arxiv/2607.06396/AlonTarsi.lean | A181 | Counting pieces with singleton edges is not a bound on the total length of a cycle cover. |
| OEIS/239957.lean | A029 | Fixed base, infinitely many primes differs from every prime having a primitive root of the form k²+1 below that prime. |
| OEIS/34693.lean | A003 | No displayed least-k bound for kn+1 prime or resolution of its competing growth variants. |
| Paper/DeGiorgi.lean | C375 at title-level, specifically the n=8 endpoint | Manuscript's normalized bounded Allen–Cahn statement matches the named endpoint; equivalence with every encoded variant, including n≥9 counterexamples, was not audited. |
| Paper/ReedOmegaDeltaChi.lean | A184 | Fixed forbidden-subgraph O(Δ/logΔ) bounds do not assert χ≤ceil((Δ+ω+1)/2). |
| Paper/StrongSensitivityConjecture.lean | C132 | Refutes every universal quadratic block-sensitivity bound. |

| Remaining file titles — each separately READ / N | Files (.lean suffix omitted) |
|---|---|
| Arxiv | 0912.2382/CurlingNumberConjecture; 1102.4662/AtiyahSutcliffe; 1104.1579/CunninghamChain; 1601.03081/UniqueCrystalComponents; 1609.08688/sIncreasingrTuples; 2107.00295/IndependentDomination; 2107.12475/CollatzLike; 2303.01089/FurstenbergTimesPTimesQ; 2501.03234/ArithmeticSumS; 2504.17644/Margulis |
| Arxiv (continued) | 2604.08040/Conjecture5_5; 2605.12342/Conjecture1; 2607.05349/MicroscopicWeighting; 2607.05739/TanArctanSum; 2607.08366/MinModulus; math.0110202/BanachMazurRotation |
| Mathoverflow | 17560; 1973; 21003; 235893; 31809; 339137; 34145; 347178; 434111; 75792 |
| OEIS | 100434; 100474; 100475; 100800; 101779; 102847; 103151; 103425; 103662; 103885 |
| OEIS (continued) | 104320; 105020; 105210; 105720; 105751; 107247; 108081; 108129; 108211; 108301 |
| OEIS (continued) | 108569; 108864; 108866; 109074; 109227; 109671; 109845; 109905; 109908; 109909 |
| OEIS (continued) | 110475; 110566; 110835; 110854; 111114; 111291; 113010; 113019; 113213; 113257 |
| OEIS (continued) | 113258; 113271; 113609; 114137; 114216; 114362; 1146; 114831; 115257; 115366 |
| OEIS (continued) | 11545; 1157; 116150; 117027; 167604; 211417; 228828; 231201; 232174; 237271 |
| OEIS (continued) | 280831; 281976; 287616; 303656; 306477; 308734; 357513; 37274; 41; 56777 |
| OEIS (continued) | 63880; 67720; 81091; 945 |
| Paper | CardinalityLindelof; CasasAlvero; CatchUpConjecture; Chvatal; ConjugacyClassSizes; Dubner; FusibleNumber; HartshorneConjecture; Homogenous; KotzigConjecture |
| Paper (continued) | Kurepa; LatinSquare; LatinTableau; MonochromaticQuantumGraph; PrimeTuples; RingelConjecture; VoronovskajaTypeFormula; WeaklyFirstCountable; ZagierMZV |

**A8. Active portfolio reconciliation** ([OPERATIONS](/work/notes/OPERATIONS.md:27) and the task's named portfolio). Evidence: READ comparison, not re-verification of our existing results. “No direct overlap” is confirmed at the stated reading depth for every line; “no related family” is false for several lines.

| Line | Verdict | Consequence for the coordinator's no-overlap statement |
|---|---|---|
| #30 Sidon second order | N | No matching second-order or stronger finite-Sidon bound. |
| #156 minimum maximal Sidon | N | No matching size-order improvement. |
| #241 B₃ | N | No matching B₃ leading constant. |
| #86 hypercube C₄ | A171 | Cube Ramsey concerns a complete host; our extremal density is unaffected by its displayed theorem. |
| #1066 penny graphs | A158/167/184 | No explicit penny-graph independence improvement follows as a stated result. |
| #1082 | A167/183 | Weak pinned distances / halving lines do not close or improve the exact coefficient target. |
| #708 | N | No matching 12n/11n counting statement. |
| #377 | N | No central-binomial missing-prime reciprocal-sum bound. |
| #859 | A025 | No representing-divisor density theorem; its already-subsumed status in OPERATIONS is independent of this release. |
| #624 | N | No matching certified H_L/H_EH small-value table. |
| #889 | A012 | Largest-prime-factor distribution is related multiplicative territory, but no v₁ finiteness or uniform v₀ growth theorem is displayed. |
| Zaremba M | N | No bounded-partial-quotient denominator theorem or explicit M improvement. |
| Capacity-transfer paper | N | No matching capacity inequality or stated sonar/weak-Sidon/g-thin/DTS/DDC consequence. Generic Fourier/convexity techniques are not subsumption. |

**B. New-target intelligence (bounded; referee candidates only).** DECISION 2026-10-09 (AUT-47, owner): NO referee programme and no capability probe on these families; referee seats stay on automath lines. The table below is kept as intelligence only. READ metadata and LIVE CLAIM statements. “Unformalized” here means no family Lean link and no matching manuscript registration in the read formalization YAML; it does not certify the nonexistence of all possible formal artifacts. Elementary-looking refers to the statement, not its proof or plausibility. No proof has been evaluated.

| Unformalized family | Elementary-looking statement to referee | Manuscript date / source |
|---|---|---|
| 011 | For every ε>0, infinitely many n have more than n^(1−ε) totient preimages; a companion asserts infinitely many primes p with μ(p−1)=1. | Weighted dilation graphs, smooth shifted primes and totient fibers, 2026-09-24; Prime Predecessors with an Even Number of Prime Factors, 2026-09-17. [Abstracts][F011] |
| 022 | For each real γ and finite-valued ψ≥0, divergence of Σφ(q)ψ(q)/q gives distance(qx−γ,Z)<ψ(q) infinitely often for almost every x; unrestricted numerators. | The Weak Inhomogeneous Duffin–Schaeffer Conjecture, 2026-09-25. [Abstract][F022] |
| 029 | Every integer a other than −1 or a square is a primitive root for ≥c_a x/(log x)² primes in (x,2x), for all sufficiently large x. | Primitive roots for every admissible integer base, 2026-10-04. [Abstract][F029]; simultaneous-base companion explicitly assumes four inputs. |
| 164 | Every finite coloring of positive integers and every k≥1 admit a k-element set whose nonempty subset sums and products have a single common color. | Monochromatic finite sums and products in the positive integers, 2026-09-23. [Abstract][F164] |
| 166 | For each d≥3, every n≥2 points in R^d determine ≥c_d n^(2/d) distances, c_d>0. | The higher-dimensional Erdős distinct-distances conjecture, 2026-09-23. [Abstract][F166] |
| 171 | R(Q_n)≤C2^n with universal C; no explicit C given in the abstract. | The hypercube Ramsey number has linear order, 2026-09-23. [Abstract][F171] |
| 178 | For each fixed d≥3 and every sufficiently large even n, a deterministic polynomial-bit-time construction of a simple nonbipartite d-regular graph with all nonconstant eigenvalues strictly inside ±2√(d−1). | Deterministic nonbipartite Ramanujan graphs in every fixed degree, 2026-09-23. [Abstract][F178] |
| 101 (convex-geometry edge of scope) | Simplices uniquely maximize the isotropic constant in every dimension. | A sharp entropy bound and the simplex inequality for isotropic constants, 2026-10-05. [Abstract][F101] |

READ: partial-formalization referee leads are distinct from whole unformalized families: 159's quantitative r_k(N) estimate versus its documented reciprocal-sum theorem; 175's graph-decomposition companion versus the two Talagrand statements; 184's correspondence-coloring companion versus the independence theorem; 186's hypergraph/nonmonotone influence companion versus the graph threshold-width theorem. The YAML and scope notes do not advertise these companion conclusions as the selected formalized theorem. Do not mark the entire families unformalized.

**B2. Quantitative targets not supplied by a matching release statement.** These are **SECONDARY** catalogue-held records, not a fresh claim of global current best. “Absent” means no matching statement found in this bounded sweep; A families above may share the area. Existing catalogue caveats about proofs and effective constants persist.

| Target | Record we hold / exact limitation |
|---|---|
| Finite Sidon #30 | OPERATIONS: F(N)≤√N+(2√2/3)N^(1/4)+1 for N≥120⁴; our 2026-10-02 result. |
| Minimum maximal Sidon #156 | Old-record row 2: N^(1/3)≪s(N)≪(N log N)^(1/3), Ruzsa 1998; constants not explicit in the catalogue. |
| B₃ / #241 | Targets card 7: limsup F₃(N)/N^(1/3)≤1.51546116978633, White 2023/24 and Rechnitzer 2026 certificate refinement; no finite-N onset supplied there. |
| B₂[6] / general B_h constants | Targets card 8: Λ(6)<4.289880000, Costa 2026-09-10 **LIVE CLAIM carried SECONDARY**; no release replacement. Other h/g records are not conflated with this normalization. |
| Ordinary sum-free extremal problems | No ordinary sum-free numerical record is specified in the requested catalogues. Old-record #790 has a different “no element is a sum of other distinct elements” condition; it is not a substitute record. |
| Zaremba | OPERATIONS: Shkredov 2026, M=2²⁰⁰⁰ for all sufficiently large primes; onset not made explicit there. |
| #1082 exact linear coefficient | Old-record row 3: at least (n−1)/3 pinned distances (integer ceiling implicit), attributed to Szemerédi through the 2013 source; the global floor(n/2) question is unmatched. The stronger pinned version is recorded as false in that catalogue. |
| Penny graphs #1066 | Old-record row 1: 8n/31, Swanepoel 2002; later 7/27 and 6/23 forum claims (July 2026) remain **LIVE CLAIM / SECONDARY**, not independently accepted here. |
| Hypercube C₄ #86 | Targets card 1: limiting C₄-free edge-density upper bound 0.60318, Baber 2012; flag-algebra certificate not replayed. |
| Diagonal Ramsey | Targets card 12: R(k,k)≤3.69507^k for every sufficiently large integer k, Lu–Wang 2026-09-13 **LIVE CLAIM / SECONDARY**; fixed-s family 170 does not replace it. |
| Union-closed frequency | Targets card 2: 0.3828852549667978 lower frequency, Costa–Sadhu 2026-09-12 **LIVE CLAIM / SECONDARY**; no full 1/2 resolution located. |
| Sequence star discrepancy | Targets card 4: limsup N D_N*/log N≥0.065664679, Larcher–Puchhammer 2016; sequence convention, not a single finite point set. |
| Minimum overlap | Targets card 5: 0.3803953≤μ≤0.380859056614806899, both bounds from the Zanghi July 2026 v4 LIVE CLAIM; domain/normalization as in that card. |

**B3. Described techniques, without proof assessment.** READ: none of the description paragraphs in the 83 mandatory families explicitly identifies an elementary proof technique and asserts a reusable improvement for our Sidon/capacity, penny-graph, cube-density or Zaremba lines. Family 169's “elementary-basis positivity” names a symmetric-function basis, not an elementary proof. Family 025's short-expansion theorem and 021's uniform interval theorem are new claimed inputs worth knowing, but the description paragraphs alone do not license a transfer lemma. No elementary-method recommendation is made from an abstract's technical vocabulary. This is a bounded negative finding, not an assertion that the manuscripts contain no useful method.

READ statement-source supplement: local [#18 comments](/work/problems/formal-conjectures/FormalConjectures/ErdosProblems/18.lean) explicitly define the practical-divisor restriction; [#970 comments](/work/problems/formal-conjectures/FormalConjectures/ErdosProblems/970.lean) separate optimal order from the quadratic subquestion; [#1082 comments](/work/problems/formal-conjectures/FormalConjectures/ErdosProblems/1082.lean) separate global from pinned distances. These local sources were read, not their proofs checked.

READ / LIVE CLAIM small exact values available without computation: family 179 asserts circulant orders {1,4} and Barker lengths >1 exactly {2,3,4,5,7,11,13}; family 189 explicitly includes R(C₃,K₃)=6 and its all-m≥n≥3 formula outside that exception. No new exact values for our active extremal quantities were computed or inferred, and no certificate was run.

READ limitations / next action: the coordinator can update catalogue status to **claimed closure / adjacent claim** at the precise scopes above, preserving existing proof and publication gates. Any verification campaign should first audit the mathematical statement and the actual formalization independently; this report authorizes none. NOT ACCESSIBLE: direct erdosproblems.com requests for #167/#556 returned access errors during this session; #167's identity is independently explicit in the local shortlist, while #556's three-cycle-color interpretation was cross-checked at SECONDARY search-result level. Repository TeX was accessible, so PDF text-extraction failure did not block the main matched statements. OpenAlex/Semantic Scholar, Zulip and live Mathlib PR activity were not refreshed: this assigned release sweep is not a comprehensive 2015–2026 literature/status dossier.

[readme]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/README.md
[history]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/history.md
[yaml]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/formalization.yaml
[F003]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L66
[L003]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/003.md
[F011]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L266
[F012]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L300
[L012]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/012.md
[F020]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L554
[L020]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/020.md
[F021]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L570
[L021]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/021.md
[F022]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L586
[F025]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L634
[L025]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/025.md
[F029]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L698
[F047]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L1258
[L047]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/047.md
[F072]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L1806
[L072]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/072.md
[F091]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L2254
[L091]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/091.md
[F101]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L2486
[F132]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3168
[L132]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/132.md
[F155]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3702
[L155]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/155.md
[F158]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3768
[L158]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/158.md
[F159]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3784
[L159]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/159.md
[F160]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3804
[L160]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/160.md
[F164]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3861
[F166]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3906
[F167]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3922
[L167]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/167.md
[F170]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L3979
[L170]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/170.md
[F171]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4008
[F173]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4040
[L173]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/173.md
[F175]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4081
[L175]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/175.md
[F176]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4115
[L176]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/176.md
[F178]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4147
[F179]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4163
[L179]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/179.md
[F181]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4195
[L181]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/181.md
[F183]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4245
[L183]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/183.md
[F184]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4261
[L184]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/184.md
[F186]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4302
[L186]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/186.md
[F189]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4359
[L189]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/189.md
[F196]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L4475
[L196]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/196.md
[F375]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md#L9025
[S021]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/sections/introduction.tex#L24
[S025]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/introduction.tex#L16
[S047]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/01-introduction.tex#L59
[S072]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/00-introduction.tex#L52
[S132]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/sections/00-introduction.tex#L53
[S158]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/build/sections/introduction.tex#L62
[S167p]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/build/sections/introduction.tex#L30
[S167u]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/build/sections/00-introduction.tex#L12
[S173cycle]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/build/source/05-directed-cycle-consequences.tex#L15
[S179]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-circulant-Hadamard-conjecture-September-23-2026/build/sections/introduction.tex#L21
[S196]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/paper.tex#L52
[S375]: https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/sections/00-introduction.tex#L59
