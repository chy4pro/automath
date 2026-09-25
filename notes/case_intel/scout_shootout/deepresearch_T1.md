# Deep Research probe T1 — verbatim harvest

- Probe: T1 (recent AI-assisted conjecture resolutions, last 8 weeks)
- Driver round: deepresearch-r3
- URL: https://gemini.google.com/app/38d9b4c4d367905b
- Prompt sent (real `date`, successful attempt): Sat Aug 22 10:45:01 CDT 2026 — NOTE: an earlier attempt at ~10:42-10:44 CDT in the same tab appeared to send (user bubble + loading dots visible) but the conversation silently reset to a blank new-chat state with no Recents entry and no persistent URL; this was detected and the prompt was re-sent cleanly in the same tab, which then produced a persistent conversation URL. Treat 10:45:01 as the effective dispatch time.
- Research plan approved ("Start research" clicked, real `date`): Sat Aug 22 10:46:53 CDT 2026
- Completion confirmed (real `date`, polling): Sat Aug 22 10:59:54 CDT 2026 (Gemini's own in-UI timestamp on the report: "Aug 22, 10:59 AM")
- Wall-clock, prompt-send to completion: ~14m (10:45:01 -> ~10:59:00)
- Wall-clock, plan-approval to completion: ~12m (10:46:53 -> ~10:59:00)
- Mode confirmed: "Deep research" chip active, model "Pro", entry point = "+" (Upload & tools) -> "More tools" -> "Deep research" (menuitemcheckbox). Not in the model/mode picker, not in the sidebar.

## Prompt (verbatim, as sent)

List AI-assisted resolutions (proofs or disproofs) of named mathematics conjectures from the last 8 weeks, with sources/links for each.

## Research plan (as generated and approved verbatim)

Recent AI Math Breakthroughs
Research Websites
(1) Search academic preprint databases and mathematics news repositories for announcements of solved or disproved named mathematical conjectures between late June 2026 and August 22, 2026.
(2) Filter the identified mathematical breakthroughs to isolate cases where artificial intelligence, machine learning models, or automated theorem provers were explicitly utilized in the research.
(3) For each relevant case, determine the exact name of the conjecture and verify whether the final result was a definitive proof or a disproof.
(4) Review the associated research papers or official announcements to extract a brief understanding of how AI was applied to achieve the resolution.
(5) Collect direct URLs, DOIs, or academic citation links corresponding to the primary research papers or institutional press releases for each resolution.
(6) Compile the findings into a structured list presenting the conjecture name, the type of resolution, a summary of the AI methodology, and the verified source links.
Analyze Results
Create Report

## Final report (verbatim)

### The Algorithmic Resolution of Mathematical Conjectures: A Landscape Analysis

The period spanning late June to late August 2026 represents an unprecedented epoch in the history of mathematics. Over this narrow eight-week window, artificial intelligence models transitioned from acting as computational assistants to functioning as autonomous research partners capable of resolving deep, decades-old conjectures. The discipline has witnessed a barrage of AI-assisted discoveries that have either definitively proved or refuted standing problems across algebraic geometry, probability, combinatorial optimization, and analytic number theory. This rapid acceleration mirrors the foundational crisis of mathematics seen between 1900 and 1930, but rather than stress-testing the logical frameworks of truth, current developments are stress-testing the sociological and epistemological values of human mathematical practice.

This analysis details the specific named conjectures resolved by AI systems during this period, dissecting the mathematical mechanisms of the proofs and disproofs, the AI architectures utilized, and the broader epistemological crisis these developments have precipitated within the mathematical community. To satisfy immediate reference requirements, the major conjectures resolved during this period, alongside their primary source literature and associated URLs, are cataloged below.

**Summary table (verbatim):**

| Conjecture / Problem | AI Model | Mathematical Outcome | Source Link(s) |
|---|---|---|---|
| Jacobian Conjecture (1939) | Claude Fable 5 | Disproof (Counterexample for n>=3) | https://arxiv.org/abs/2608.00222 |
| Cycle Double Cover Conjecture (1973) | GPT-5.6 Sol Ultra | Proof (Reduced to cubic graphs via flows) | https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf |
| Dinitz-Garg-Goemans Conjecture (1999) | GPT-5.6 Pro | Disproof (Cost-aware fractional routing) | https://www.datacamp.com/blog/gpt-5-6-dinitz-garg-goemans-conjecture |
| Feige's 1/e Conjecture (2004) | ChatGPT 5.6 Pro / Codex | Proof (Optimal bound for delta>=1) | https://guanyangwang.github.io/blog/feige-conjecture.html |
| Riemann Zeta Function Zeros (1859) | Claude (Unreleased rh-E2-pontryagin) | Improvement (Lower bound raised to 67.25%) | https://www.anthropic.com/research/riemann-zeta , https://github.com/anthropics/zeta-23-lean |
| Zhao's Vanishing Conjecture | Claude Fable 5 (via Thompson/MacFarlane) | Disproof (40-variable homogeneous quartic) | https://arxiv.org/abs/2608.12543 |
| Erdős Unit Distance Problem (1946) | Internal OpenAI Model | Disproof (High-dimensional grid projection) | https://www.sciencenews.org/article/ai-guardrails-erdos-math-problem |
| Unbounded Elliptic Curve Ranks | Claude (Assisted) | Discovery (Explicit curve of rank 30) | https://www.reddit.com/r/math/comments/1vp6ng9/ai_in_mathematics_august_15_2026/ |

#### Affine Algebraic Geometry and the Jacobian Refutation

The Jacobian conjecture, formally codified by Ott-Heinrich Keller in 1939, posits that any polynomial map F: C^n -> C^n whose Jacobian determinant detJ(F) is a nonzero constant must possess a polynomial inverse. This deceptively simple hypothesis assumes that a locally invertible polynomial endomorphism of complex spaces is always globally invertible. For eighty-seven years, this conjecture stood as one of the most stubborn and tantalizing problems in affine algebraic geometry, verified only for degree maps up to 100 in two dimensions by Moh.

On July 19, 2026, mathematician Levent Alpöge announced that an AI model, Claude Fable 5, had successfully discovered an explicit counterexample to the Jacobian conjecture in dimension three, definitively settling the problem in the negative for all dimensions n>=3. The resulting counterexample shattered a century of human geometric intuition by exploiting topological boundaries previously thought to be constrained by classical algebraic identities.

**The Mathematical Mechanism: The Tangent Sweep**

The counterexample generated by Fable 5 operates on an intricate geometric mechanism that was isolated and theoretically expanded shortly after by David Speyer, and subsequently generalized to all higher dimensions by Shuhong Gao. The core conceptual engine relies on a "tangent sweep" mechanism. Classical projective duality forces the tangent sweep of a parametrized plane curve K: w -> (p(w),q(w))^T to map multiple points to the exact same image, inherently violating global invertibility.

In the specific three-dimensional counterexample provided by Fable 5, the map F=(a,b,c): C^3 -> C^3 is defined through the following system of polynomial equations (as rendered in the report, with subscript/superscript formatting lost in extraction):

a = (1+xy)^3 z + y^2 (1+xy)(4+3xy)
b = y + 3x(1+xy)^2 z + 3xy^2 (4+3xy)
c = 2x - 3x^2 y - x^3 z

This mapping successfully yields a constant Jacobian determinant detJ(F) = -2, perfectly satisfying the Keller condition. Despite this local invertibility, the map is generically three-to-one.

The ingenuity of the AI's discovery lies in its exploitation of a topological loophole regarding properness. A structural theorem by Białynicki-Birula and Rosenlicht dictates that an injective polynomial map C^n -> C^n is unconditionally bijective with a polynomial inverse; thus, any counterexample to the Jacobian conjecture must fail injectivity. Because Keller maps are étale (everywhere unramified local biholomorphisms), non-injectivity cannot occur through the direct collision of preimages over a finite target point. Instead, preimages can only escape to infinity. The Fable 5 map perfectly executes a monomial twist on the tangent sweep, cancelling the Jacobian factor exactly. The price of this precise mathematical cancellation is that the ramification of the sweep is pushed entirely to the boundary at infinity, yielding a Keller map that is everywhere unramified but fundamentally improper, allowing distinct points to escape along the Jelonek hypersurface.

**Generalizations, Verifications, and Downstream Refutations**

Following Fable 5's initial output, the result was immediately absorbed and generalized by the human mathematical community. Gallagher demonstrated a uniform one-variable construction producing counterexamples of any geometric degree d>=3, while Shuhong Gao extended the tangent sweep mechanism from planar curves to complex direction fields on parametrized hypersurfaces. By routing these direction fields through discrete sets of scalings and characteristic-invariance loci, Gao produced a recursive family of explicit counterexamples in higher dimensions.

Reported table of generalized counterexample maps (Map Identifier / Dimension / Jacobian Determinant / Geometric Degree (Fiber Size) / Underlying Topology):

- Fable 5 Original — 3D — ≡ -2 — 3 — Monomial twist on a cuspidal cubic
- Gao's G Map — 3D — Non-constant scaling — 4 — Rational quartic curve with node/cusps
- Gao's F4 Map — 4D — ≡ -44/9 — 5 — Tangent sweep on non-cylindrical ruled surface
- Gao's F5 Map — 4D — Constant — 10 — M-branch specialization
- Gao's F6 Map — 5D — ≡ -290 — 6 — Mixed direction field
- Gao's F7 Map — 5D — Constant — 12 — Curve-type direction field

The validity of the Alpöge-Fable counterexample was rapidly sealed by the automated theorem proving community. Independent verification was achieved in Isabelle/HOL within days, definitively closing the problem without requiring decades of manual peer-review parsing.

Furthermore, the mechanisms pioneered by Fable 5 precipitated the resolution of adjacent open problems. Leveraging the generated collision topologies, Thomas Prellberg produced a 40-variable counterexample to Zhao's Vanishing Conjecture. Zhao's conjecture had posited that if a homogeneous quartic P satisfies the Laplacian condition Delta^m P^m = 0 for all m>=1, then Delta^m P^(m+1) = 0 for sufficiently large m. Prellberg applied a symmetric cotangent lift to a 20-variable cubic-homogeneous Keller map (itself derived from the Jacobian counterexample architecture), yielding an explicitly specified homogeneous quartic P in Q(i)[x1,...,y20] with 350 monomials. This quartic possessed a nilpotent Hessian and directly refuted Zhao's condition, proving that the generative capabilities of the initial AI discovery cascaded into highly dimensional matrix algebra.

#### Graph Theory and Combinatorial Optimization

**The Cycle Double Cover Conjecture**

In topological graph theory, the Cycle Double Cover (CDC) conjecture, formulated independently by George Szekeres (1973) and Paul Seymour (1979), dictates that every bridgeless graph contains a multiset of cycles such that every edge belongs to exactly two cycles. Topologically, this asserts that every bridgeless multigraph can be embedded in a pseudosurface such that every face is a disc, and every edge occurs exactly twice among the boundary walks. Prior to 2026, the conjecture had been proven only for highly specific subsets of graphs, such as cubic graphs of oddness at most four or locally connected graphs.

On July 10, 2026, OpenAI released a three-page proof of the CDC conjecture generated entirely by GPT-5.6 Sol Ultra. The computational architecture for this proof was notably complex, utilizing 64 concurrent, independent sub-agents operating adversarially over an eight-hour computational window. Crucially, the prompt specifically instructed the model to assume a complete affirmative proof existed, preventing the AI from hedging or abandoning the search tree.

The mathematical architecture of the AI's proof, which was subsequently simplified and distilled in expositions by Sang-il Oum and Jim Geelen, relies on an intricate fusion of nowhere-zero flows and linear algebra over the finite field F2.

- Topological Reduction: The AI initiates the proof by invoking Fleischner's splitting lemma and the Tutte-Nash-Williams Tree-Packing theorem, establishing that a minimal counterexample to the CDC conjecture must be a cubic, 3-edge-connected graph. Any vertices of higher degree can be systematically "uncontracted".
- Nowhere-Zero Flows: Leveraging François Jaeger's 1979 flow theorem, the AI establishes that every bridgeless graph admits a nowhere-zero F2^3-flow. The AI assigns non-zero flow values f: E -> F2^3 such that at each vertex, the flow-values of incident edges sum to strictly zero.
- Linear Systems over F2: The core analytical innovation generated by GPT-5.6 Sol Ultra is the construction of a rigid consistency criterion. The AI established that finding a valid edge-bicolouring (and thus a cycle double cover) is algebraically equivalent to finding vertex potentials p: V -> F2^3 and edge scalars z: E -> F2 that satisfy the linear system p_u + p_v + f_e*z_e = alpha_{u,e} + alpha_{v,e} for every edge e=uv, where alpha represents specific flow values derived from adjacent edges.
- Contradiction via Orthogonality: The AI proves that if no such cover exists, the linear system must have no solution, meaning a subset of those equations must sum to the absurd equation 0=1. By applying the elementary principle that the column space of a matrix is the orthogonal complement of its left nullspace, the AI constructs a subgraph G+ that algebraically violates this orthogonality condition. This logical contradiction proves that the required vertex vectors must exist, collapsing the conjecture.

The proof was simultaneously formalized in the Lean theorem prover, marking a watershed moment for machine-generated, machine-verified combinatorial mathematics.

**The Dinitz-Garg-Goemans Conjecture**

Operating in the realm of combinatorial optimization, the Dinitz-Garg-Goemans conjecture (dating to 1999) hypothesized that if a valid fractional flow exists in a network, it can always be converted into an unsplittable flow without exceeding capacity constraints by more than the maximum single demand, and without increasing the total routing cost. While the congestion bound of this theorem had been mathematically secured years prior, the cost-bound conjecture remained a frustratingly elusive target for nearly three decades.

On July 22, 2026, researcher Dmitry Rybin utilized GPT-5.6 Pro to systematically search for a counterexample. The language model required a mere four prompts — totaling fewer than 60 words — to successfully output a structured, irrefutable counterexample. The AI generated a small, directed graph consisting of a single source, three delivery terminals, seven points, and nine connections.

The AI's construction brilliantly exploited the structural tension inherent in network topologies. It arranged cheap paths such that pairs of terminals fought over their own private bottleneck roads. In a splittable (fractional) flow, each terminal sends exactly 2/5 of its demand down the cheap path and 3/5 down the expensive path. This perfectly distributes the load to slip under every capacity constraint simultaneously, resulting in a minimal cost of 58. However, forcing the network into an unsplittable routing immediately overflows the shared spine roads, forcing all but one terminal onto expensive, direct detours. The AI proved that any valid unsplittable routing in this specific topology costs at least 60, exposing a permanent, two-point mathematical gap that definitively sank Goemans' cost conjecture.

#### Probability, Statistics, and Prompt Epistemology

**Feige's 1/e Conjecture for Anticoncentration**

In probability theory, Uriel Feige conjectured in 2004 that for any collection of independent nonnegative random variables X1,...,Xn with expectations bounded by E[Xi]<=1, the sum Sn=X1+...+Xn must satisfy the lower bound P(Sn < E[Sn]+1) >= 1/e. For over twenty years, this bound was only proven under highly restrictive assumptions — such as identically distributed variables or discrete log-concave distributions — with universal bounds slowly creeping from 1/13 to roughly 0.1798, far short of the optimal 1/e ~ 0.3678 limit.

On July 26, 2026, a collaboration of mathematicians published a paper resolving the conjecture, openly stating that the initial proof was generated by ChatGPT 5.6 Pro. The model's proof was remarkably elegant, acting as a synthetic bridge between two distinct mathematical disciplines. The AI recognized that Feige's conjecture could be solved by combining convex geometry with a non-parametric test statistic. Specifically, it linked the classical Grünbaum centroid theorem (1960) and its recent generalization by Letwin and Yaskin (2024) with the exact Dirichlet calibration theorem of Vlassis and Thomas (2026) — which had itself recently resolved Gaffke's statistics conjecture.

By projecting the random variables onto the probability n-simplex using uniform Dirichlet weights, the AI utilized the Letwin-Yaskin inequality to establish a bound on P(S < E[S]+delta) that, for delta>=1, evaluates to exactly >= 1/e, resolving the conjecture optimally. The entire mathematical argument, including the integration of the Dirichlet calibration, was seamlessly formalized in Lean via Codex.

*The Epistemology of the Prompt*

The discovery of the Feige proof provided researchers with a rare opportunity to study the epistemology of large language model interaction in high-stakes mathematical environments. Mathematician Guanyang Wang conducted a controlled experiment using GPT-5.6 Sol Ultra in Codex, rigorously testing two nearly identical prompts to isolate the exact linguistic trigger that resulted in mathematical success.

Prompt B simply asked the model to prove the conjecture and "make a breakthrough." Across four independent sessions, Prompt B failed entirely to close the proof. Prompt A contained one additional sentence: "You need to first search the literature extensively to identify potentially useful results, without restricting yourself to the original area". This single metalinguistic directive drastically altered the model's behavior, causing it to succeed in three out of four runs. The experiment definitively proved that current frontier AI models possess the latent deductive reasoning capacity to resolve top-tier conjectures, but frequently require explicit meta-cognitive instructions to access and synthesize out-of-domain knowledge repositories.

#### Analytic Number Theory: Advancing the Riemann Zeta Bound

While artificial intelligence successfully resolved several longstanding conjectures this summer, its application to arguably the most famous unsolved problem in mathematics — the Riemann hypothesis — yielded an unexpected and profound improvement in bounding theory.

On August 10, 2026, Anthropic reported that an unreleased research build of the Claude model, tasked initially with a prompt to "Take a real stab at the Riemann hypothesis," successfully improved the lower bound for the fraction of nontrivial zeros of the Riemann zeta function residing exactly on the critical line (Re(s)=1/2). Building on the foundational techniques of Montgomery (1973) and the more recent constraint relaxations by Aryan, Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh, the model pushed the confirmed boundary from 41.6% to an unprecedented 67.25%.

*The Multi-Agent Architecture and Pontryagin Spaces*

The breakthrough was achieved not by a single, monolithic model query, but via a highly coordinated campaign involving multiple interacting sub-agents. During a session supervised by a human researcher, an orchestration agent tasked a specific sub-agent (named rh-E2-pontryagin) to evaluate the "density of states" and build an upper bound on off-line zeros.

The agent's initial attempt relied heavily on the Kreĭn–Langer principle situated within a Pontryagin space. The AI formulated a suitable finite-dimensional space of test functions, restricting the pairing induced by the Guinand-Weil explicit formula to this space. Within this framework, zeros located exactly on the critical line generated positive-definite subspaces (the (1,0) part), while zeros located off the line generated negative-definite, hyperbolic plane subspaces (the (1,1) part).

The AI agent quickly determined through iterative testing that attempting to bound the negative index directly was a mathematically empty route, noting it was "identically zero in every computable range". Displaying remarkable autonomy, the agent executed a mathematical pivot it labeled "THE DUAL USE OF INERTIA". Instead of attempting to count negative squares, it inverted the entire strategy to lower-bound the positive index using prime-side traces, double-counting the off-line pairs against the Riemann–von Mangoldt zero-counting formula.

*The Rank-Trace Inequality*

To push the boundary to 67.25%, the agent known as E2-pairs derived a novel rank-trace inequality using extremal experiments over vector configurations, ultimately arriving at a lower bound of rank(W_on)/N_all(T) >= 3/2 - (1/sqrt(2))*cot(1/(2*sqrt(2))) ~ 0.6725..., unconditionally proving that at least 67.25% of the zeros of the Riemann zeta function are distinct and lie strictly on the critical line.

The entire argument, including the Weil explicit formula evaluated via contour integration, the Chebyshev-Mertens prime-sum estimates, the Montgomery-Vaughan generalized Hilbert inequality, and the final 67.25% certificate, was formally verified in the Lean 4 theorem prover (hosted in repository anthropics/zeta-23-lean). The verification utilized strictly standard axioms (propext, Classical.choice, Quot.sound), rendering the proof completely free of unproven `sorry` assumptions.

Adjacent to this discovery, Claude was also utilized in August 2026 to assist an anonymous researcher in discovering an elliptic curve over the rationals with a rank of exactly 30 (assuming the generalized Riemann hypothesis and Birch and Swinnerton-Dyer conjecture). This discovery called previous heuristics into question and heavily bolstered John Tate's 1970s prediction that elliptic curve ranks are mathematically unbounded.

#### The Industrialization of Discovery: The Pipeline-Math Paradigm

The isolated breakthroughs by individual models operating on singular problems have catalyzed a systemic shift toward the automated, industrial-scale resolution of open mathematical problems. The most prominent architectural example of this in August 2026 is the pipeline-math project utilizing GPT-5.5 Pro, a framework described by researchers as the FAR (Find, Attempt, Recommend) pipeline.

Rather than targeting a single famous conjecture, the FAR pipeline completely reverses the traditional mathematical workflow. It operates on broad research directions, autonomously scouring vast literature corpora to identify, extract, and triage open problems before attempting to solve them.

In a pilot run focused specifically on combinatorics, the pipeline ingested an initial corpus of 51,110 mathematics papers, identified 5,245 relevant combinatorics papers, and subsequently extracted 6,453 candidate conjectures. Because open problems are frequently scattered haphazardly inside texts — appearing as numbered statements, rhetorical questions, remarks, or embedded within highly localized notation — the AI verified the current status of these candidates against global web resources, accurately filtering the pool down to 4,717 well-posed, unresolved open problems.

Reported pipeline stage table (Stage / Action / Volume remaining):
- Initial Corpus — Ingest literature — 51,110 papers
- Domain Filter — Isolate combinatorics — 5,245 papers
- Extraction — Pull candidate conjectures — 6,453 candidates
- Verification — Filter out solved/invalid problems — 4,717 open problems
- Attempt — AI attacks the pool computationally — 598 resolutions
- Triage — Output artifacts for human review — 77 artifacts

The system then deployed GPT-5.5 Pro to mathematically attack all 4,717 problems as a constrained optimization exercise, maximizing expected value over the compute budget. The AI rigorously tested statements against degenerate boundaries, diagnosed structural formulation defects, proposed minimal natural repairs to flawed statements, and generated checkable proofs.

The automated triage surfaced 598 potential resolutions, ultimately recommending 77 polished items for human expert review. Among the verified outputs, the pipeline successfully proved the Ikenmeyer-Pak-Panova conjecture concerning symmetric-group characters, answered an open divisibility question by Erdős and Straus on binomial coefficients, and constructed rigorous, irrefutable counterexamples to the conjectures of Davies–Jenssen–Perkins–Roberts and Lund–Saraf–Wolf. Similar industrialized systems, such as the Rethlas-Archon framework developed at Peking University, successfully formalized tens of thousands of lines of code to resolve highly specific bounds, pointing toward an imminent future where human intellectual effort is solely conserved for the final stage of artifact validation. This follows in the footsteps of OpenAI's internal models, which earlier in 2026 successfully refuted the 80-year-old Erdős unit distance problem by generating complex grid arrangements in high-dimensional space and projecting them onto flat planes.

#### Epistemological Turbulence and the Leiden Declaration

The sudden, overwhelming influx of AI-generated proofs and refutations in the summer of 2026 has induced a state of profound epistemological turbulence within the professional mathematical community. Mathematics has historically operated on a framework where the visceral practice of solving a problem is inextricably linked to the generation of human understanding. As William Thurston famously observed, the ultimate goal of mathematics is not simply to produce verified strings of logic, but to impart and expand human comprehension.

**The Decoupling of Practice and Measurement**

The arrival of frontier models like Fable 5 and GPT-5.6 Sol Ultra has effectively and permanently decoupled the generation of a proof from human intellectual practice. Critics, notably Max Weinreich, argue that AI acts as a fundamentally "anti-intellectual technology," generating vast swaths of literature that remain completely untethered to fixed human understanding. When Fable 5 successfully refuted the Jacobian conjecture, it produced a mathematically flawless mapping that humans could verify via brute-force number crunching, yet the genesis of the counterexample remained an utterly opaque, black-box leap of intuition.

Furthermore, the exponential increase in these autonomous outputs has begun to strain the peer-review infrastructure to a breaking point. Researcher Daniel Litt observed that the production of combinatorics papers has skyrocketed artificially, while human engagement metrics on discussion platforms like MathOverflow have significantly atrophied. The mathematical literature is rapidly filling with duplicated, machine-generated labor; for instance, multiple AI groups independently reproduced the Feige 1/e conjecture and Fable's Jacobian counterexample almost simultaneously simply because the models optimize for identical probability paths. This flood of algorithmically generated papers threatens to irreparably break the academic journal system, eventually necessitating the deployment of AI to referee AI — a scenario that completely removes human agency and intellectual oversight from the evaluation loop.

**The Leiden Declaration**

In direct response to this unprecedented crisis of values, an international coalition of mathematicians — endorsed by the International Mathematical Union (IMU) — published the "Leiden Declaration on Artificial Intelligence and Mathematics" on June 2, 2026.

The declaration serves as a political, ethical, and professional framework, attempting to reassert human values in an increasingly automated discipline. It mandates that mathematicians must transparently disclose all use of AI tools in their publications, retain absolute and unyielding responsibility for the correctness of AI-generated proofs, and adhere to strict principles of open science to combat the privatization of mathematical discovery by for-profit tech conglomerates. The declaration emphasizes that artificial intelligence "may obscure, but does not replace, the collective human labor behind a result," explicitly affirming the necessary humanity of authorship.

Prominent mathematicians, including Fields Medalist Peter Scholze, strongly endorsed the declaration, arguing that mathematical ideas, much like children, must be carefully nurtured over time, and that the fundamental goal of the field is to foster a communal, shared spirit of human understanding. Conversely, others argue that actively resisting AI integration is a form of "ivory tower privilege," noting that in applied fields, the pure utility of a theorem often supersedes the aesthetic desire for human comprehension. If a machine can provide the optimal spectral-gap bound for a binary-matrix problem or calculate network flow routing limits, the engineering and economic applications of that bound remain perfectly valid regardless of whether a human mathematician experienced the psychological joy of its discovery.

#### Conclusion

The eight weeks of Summer 2026 will likely be recorded in academic history as the exact inflection point where mathematics ceased to be a strictly human endeavor. Through highly sophisticated models like Claude Fable 5, GPT-5.6 Sol Ultra, and the industrialized FAR pipeline, artificial intelligence has definitively proven its capability to transcend basic textbook exercises. It is now autonomously searching literature, bridging disparate disciplines through topological embeddings and finite field algebras, and effortlessly dismantling century-old conjectures.

The algorithmic refutation of the Jacobian and Erdős conjectures, the topological proof of the Cycle Double Cover conjecture, and the advancement of the Riemann zeta bound via Pontryagin spaces and rank-trace inequalities collectively establish that large language models now possess genuine, rigorous deductive reasoning capabilities. However, as the Leiden Declaration makes acutely clear, the primary challenge facing the discipline is no longer about assessing the capability of machines, but about preserving the core epistemological values of humans. The community must now navigate a new, uncharted reality where formal proof is overwhelmingly abundant, but human understanding remains painfully scarce.

### Sources used in the report (verbatim list, ~46 entries incl. duplicates as rendered)

digg.com (Feige's 1/e), happymag.tv (layman's guide ChatGPT), arxiv.org (Advancing Mathematics Research with AI-Driven Formal Proof Search), guanyangwang.github.io (LLMs for Proof Generation and Verification), gwern.net ('math' directory), arxiv.org (Mathematics in the age of AI), alphaxiv.org (Mathematics in the age of AI), arxiv.org (The crisis of AI-generated mathematics), leidendeclaration.ai (Leiden Declaration), arxiv.org (Counterexamples to the Jacobian conjecture in dimensions greater, x2 dup), en.wikipedia.org (Cycle double cover), mathworld.wolfram.com (Cycle Double Cover Conjecture), arxiv.org (unlabeled), datacamp.com (GPT-5.6 and the Dinitz-Garg-Goemans Conjecture), guanyangwang.github.io (Prompting Toward a Conjecture), explainx.ai (Claude Riemann Result), anthropic.com (Learning more about Claude's mathematical capabilities), researchgate.net (Collision-Hull Compression for Homogeneous Keller Maps), arxiv.org (Collision-Hull Compression, x2), sciencenews.org (AI cracked an Erdős math problem), reddit.com (AI In Mathematics: August 15, 2026), smithsonianmag.com (A.I. Disproves a Decades-Old Mathematical Idea), arxiv.org (Counterexamples to Jacobian, dup), arxiv.org (Graded Keller maps and the Jacobian Conjecture), isa-afp.org (Formal Verification of an Explicit Counterexample to the Jacobian), arxiv.org (crisis of AI-generated math, dup), youtube.com (87 Years Later, AI Found the Jacobian Counterexample), arxiv.org (weak Markus–Yamabe conjecture fails in dimension 14), functor.network (proof of the cycle double cover conjecture), matroidunion.org (The cycle double cover theorem), dev.to (GPT-5.6 Claims to Solve a 50-Year-Old Math Problem), aiweekly.co (OpenAI Attributes Cycle Double Cover Proof to GPT-5.6 Sol Ultra), arxiv.org ([2607.15399] OpenAI's proof of the Cycle Double Cover Theorem), 4m4.it (AI Mathematics Crosses the Systems Boundary), mathoverflow.net (Purported proof of the cycle double cover conjecture [closed]), kingy.ai (OpenAI's 64-Subagent Cycle Double Cover Conjecture), note.com (Whose Thoughts Is an LLM Articulating?), aiweekly.co (Anthropic says Claude improved a Riemann zeta lower bound), arxiv.org (Towards Scalable Mathematical Discovery, x2), academicjobs.com (Peking Univ AI Math Breakthrough — Anderson Conjecture), arxiv.org (unlabeled), daniellitt.com (The End of Mathematics), en.wikipedia.org (Leiden Declaration), mathunion.org (June 2, 2026 — IMU), leidendeclaration.ai (News — Leiden Declaration), reddit.com (Leiden Declaration r/math)

### Sources read but not used (count: ~20, list preserved in raw capture — mostly tangential Bluesky/Wikipedia/social posts and duplicate arXiv hits; omitted here for brevity, not substantive to shootout scoring)

## Adjudication note (NOT part of the harvest — flagged for scorer)

This is the "recent AI conjecture resolutions" survey probe (no known trap/ledger answer to check against — this is a completeness/coverage probe, not a binary-verdict trap probe like T2). Coverage is broad (Jacobian, CDC, Dinitz-Garg-Goemans, Feige, Riemann zeta, Zhao's Vanishing, Erdős unit distance, elliptic curve ranks) with a named-model attribution table, technical mechanism sections per result, and a meta-commentary section on the Leiden Declaration / epistemological debate. Left as raw evidence for scoring against the other engines' T1 harvests, not adjudicated here.
