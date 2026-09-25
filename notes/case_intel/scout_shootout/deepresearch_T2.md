# Deep Research probe T2 — verbatim harvest

- Probe: T2 (Kourovka 19.25 + OEIS A114831 open-problem status check, trap probe)
- Driver round: deepresearch-r3
- URL: https://gemini.google.com/app/dd56b89ee8816e3a
- Prompt sent (real `date`): Sat Aug 22 10:42:44 CDT 2026
- Research plan approved ("Start research" clicked, real `date`): Sat Aug 22 10:45:56 CDT 2026
- Completion confirmed (real `date`, polling): Sat Aug 22 10:56:34 CDT 2026 (Gemini's own in-UI timestamp on the report: "Aug 22, 10:54 AM")
- Wall-clock, prompt-send to completion: ~11m50s (10:42:44 -> ~10:54:30, using Gemini's own stamp)
- Wall-clock, plan-approval to completion: ~8m34s (10:45:56 -> ~10:54:30)
- Mode confirmed: "Deep research" chip active, model "Pro", entry point = "+" (Upload & tools) -> "More tools" -> "Deep research" (menuitemcheckbox). This path is NOT in the model/mode picker (Flash-Lite/Flash/Pro/Extended thinking/Deep Think) and NOT in the left sidebar — it is nested two levels deep in the plus-button tools menu. Round-1 and round-2 both stopped short of finding it.
- Note: this is a RE-DISPATCH from a fresh, purpose-built Deep Research session (not a reused/pre-existing user tab — none was found in the MCP tab group in this round; see RESOURCES.md lease log for the full search).

## Prompt (verbatim, as sent)

For each of these two statements, state whether it is still an open problem as of today, with evidence: (1) Kourovka Notebook problem 19.25 (equal order-element-sum groups, simplicity transfer); (2) the conjecture that a(n+1)/a(n) converges to sqrt(3) for OEIS A114831.

## Research plan (as generated and approved verbatim)

Status of Two Math Problems
Research Websites
(1) Search for the current status of Kourovka Notebook problem 19.25 concerning equal order-element-sum groups and simplicity transfer.
(2) Review mathematical databases, recent journal publications, and preprint archives up to August 2026 for any formal proofs, counterexamples, or partial solutions resolving Kourovka Notebook problem 19.25.
(3) Look up sequence A114831 in the On-Line Encyclopedia of Integer Sequences (OEIS).
(4) Analyze the comments, formulas, and references within the OEIS entry for A114831 to check the documented status of the conjecture that the ratio of successive terms converges to the square root of 3.
(5) Search for recent number theory papers or literature referencing OEIS A114831 to determine if the convergence conjecture has been formally proven or disproven by the mathematical community.
(6) Synthesize the gathered evidence to conclude whether each of the two problems remains an open problem as of today.
Analyze Results
Create Report

## Final report (verbatim)

### Resolution of Simplicity Transfer and Asymptotic Behaviors in Recursive Integer Sequences: A Formal Analysis

The intersection of abstract algebra and computational number theory increasingly relies on both classical heuristic methods and modern formal verification to resolve longstanding conjectures. Within the rigid frameworks of pure mathematics, propositions are generally tested through empirical computation, generalized via structural theorems, and ultimately subjected to rigorous logical proof. The contemporary mathematical landscape is undergoing a paradigm shift, characterized by the integration of autonomous reasoning agents and formal proof assistants capable of resolving discrete problems that have eluded human researchers for decades.

This comprehensive report investigates the contemporary status of two specific mathematical propositions that occupy distinct domains within this landscape. The first is Problem 19.25 from the Kourovka Notebook, an algebraic hypothesis proposing that group simplicity can be transferred between finite groups sharing an identical order and totient sum. The second is an asymptotic conjecture regarding the integer sequence OEIS A114831, a problem in discrete dynamical systems which proposes that the ratio of successive terms defined by a floor-bounded harmonic mean recurrence converges precisely to the square root of three. By analyzing the current formal literature, computational evidence, and recent milestones in automated theorem proving, this analysis provides an exhaustive evaluation of whether these problems remain open today, detailing the mathematical mechanisms and proofs underpinning their respective statuses.

#### Part I: The Kourovka Notebook and Algebraic Characterizations

**History and Function of the Kourovka Notebook**

To understand the significance of Problem 19.25, it is imperative to establish the historical and functional context of the repository in which it was published. The Kourovka Notebook represents one of the most significant and enduring collaborative repositories of unsolved problems in group theory. The initiative was proposed in February 1965 by M. I. Kargapolov during the Problem Day of the First All-Union (All-USSR) Symposium on Group Theory, held in the small village of Kourovka near Sverdlovsk. Since its inception, the Notebook has been updated and published every two to four years, serving as a critical communication mechanism for group theorists worldwide. During the Cold War, it famously bridged the gap between researchers across the Iron Curtain, facilitating an international exchange of ideas in highly theoretical domains.

The success of the Kourovka Notebook in driving algebraic research is highly demonstrable; over three-quarters of the problems presented in the first and second issues have been solved. Today, the Notebook is in its 21st edition, which was released in early 2026, continuing to archive solved problems while introducing 150 new challenges proposed by hundreds of mathematicians globally. The Notebook serves not merely as a list of curiosities, but as an authoritative register defining the frontier of group theory research.

**The Genesis of Problem 19.25: Simplicity and Group Invariants**

Problem 19.25 was formally introduced in the 19th issue of the Kourovka Notebook (published in 2018) by researchers B. Curtin and G. R. Pourgholi. The problem asks a fundamental question about the characterization of finite simple groups based on highly compressed numerical invariants.

Specifically, the problem states: Let G and H be finite groups of the same order such that their totient sums are equal — sum over g in G of phi(|g|) = sum over h in H of phi(|h|) — where phi denotes Euler's totient function and |g| denotes the order of the element g in the group. If G is a simple group, must H also necessarily be a simple group?

To fully understand the motivation behind Problem 19.25, it is necessary to contextualize it within the broader historical effort to characterize finite simple groups. Following the monumental Classification of Finite Simple Groups (CFSG) — a theorem tens of thousands of pages long establishing that every finite simple non-abelian group belongs to one of several well-defined families (alternating groups, groups of Lie type, or the 26 sporadic groups) — researchers immediately sought minimalist criteria to uniquely identify these groups without relying on their exhaustive structural definitions.

A direct and vital predecessor to Problem 19.25 is Wujie Shi's Conjecture, recorded as Kourovka Problem 12.39 in 1987. Shi hypothesized that a finite simple group is uniquely determined in the class of all groups by its order and its spectrum (the precise set of its element orders, denoted omega(G)). Shi's conjecture was rigorously proven in the affirmative through a series of papers culminating in the early 21st century; a finite group and a finite simple group sharing identical orders and identical sets of element orders are definitively isomorphic.

Problem 19.25 represents an ambitious attempt by Curtin and Pourgholi to compress the invariant even further. Instead of requiring the entire set of element orders omega(G) to match, the authors hypothesized that the mere sum of the totient values of these orders, combined with the group order, might suffice to force simplicity. The sum enumerates the total number of generators for all cyclic subgroups within the group, serving as a heavily aggregated statistical signature of the group's internal cyclic architecture. If proven true, it would mean that the simplicity of a group could be dictated by a single scalar integer representing cyclic density, rather than a full set of orders.

**The Resolution of Problem 19.25**

As of mid-2026, Kourovka Notebook Problem 19.25 is no longer an open problem. It has been definitively and formally disproved.

The resolution was achieved in the negative by demonstrating that the group order and the totient sum are excessively lossy compressions of a group's mathematical structure. These two integers alone do not contain sufficient structural rigidity to enforce simplicity transfer between groups.

*The Counterexample Construction*

The disproof relies on the explicit construction of a counterexample consisting of two distinct finite groups, G and H, which perfectly satisfy the prerequisites of the problem but flagrantly violate the conclusion.

- Shared Invariants: Both groups possess an identical finite order of 6,048.
- Shared Totient Sum: For both groups, the cyclic statistic evaluated over all elements in the group evaluates exactly to 23,984.
- Divergent Simplicity: The group G is a simple group, whereas the corresponding group H is not simple.

The specific simple group G utilized in this definitive counterexample is the projective special unitary group denoted as PSU(3,3). The construction of PSU(3,3) and the rigorous proof of its simplicity rest on classical linear algebraic group theory over finite fields. The group is derived from a 3-dimensional vector space V over the finite field F_9. The field F_9 possesses a nontrivial involutory automorphism defined by a -> a^3, which acts analogously to complex conjugation in the complex plane. The vector space V is equipped with a nondegenerate Hermitian form f relative to this specific automorphism.

Within this three-dimensional space, there exist exactly 28 isotropic one-dimensional subspaces (subspaces spanned by a nonzero vector v such that the Hermitian form evaluates to zero, f(v,v)=0). This set of 28 isotropic one-dimensional subspaces is denoted by Omega. The classical group SU(3,3) is defined as the set of linear automorphisms of V that simultaneously preserve the Hermitian form f and possess a determinant of 1. Because these automorphisms strictly preserve the form, they naturally permute the 28 isotropic subspaces within Omega. The projective variant of this group, PSU(3,3), is defined as the central quotient SU(3,3)/Z(SU(3,3)), which continues to act faithfully on the set of 28 isotropic points.

The simplicity of PSU(3,3) can be established via Iwasawa's criterion, a highly powerful theorem in algebraic geometry and group theory. Iwasawa's criterion states that a perfect finite group G is simple if it acts faithfully and primitively on a set X such that the stabilizer of a specific point contains an abelian normal subgroup whose conjugates generate the entire group G. Under this natural action on its 28 isotropic points, PSU(3,3) perfectly satisfies these rigorous conditions.

Conversely, the counter-group H, while possessing the exact same cyclic generator density (the totient sum of 23,984) and the exact same cardinality (6,048), possesses proper non-trivial normal subgroups, rendering it non-simple and thus entirely breaking the Curtin-Pourgholi conjecture.

*Formal Verification and the Role of Autonomous AI Agents*

A highly notable and historically significant aspect of the resolution of Problem 19.25 is its provenance. The elegant counterexample was not found through traditional manual mathematical exploration or brute-force human coding, but was autonomously discovered and formally verified in mid-2026 by "Aristotle," an artificial intelligence formal reasoning agent developed by the technology firm Harmonic.

This milestone represents a profound paradigm shift in the resolution of discrete algebraic conjectures. According to the disclosure from the researchers, Aristotle developed the proof strategies entirely without human guidance regarding which specific mathematical steps to take to find the counterexample. The human authors served primarily in a supervisory and editorial capacity; they monitored Aristotle's progress, intervened when system clarifications were needed, worked alongside the AI to build a library of relevant algebraic concepts, and finally informalised the proof by translating the machine's code into conventional natural language mathematical prose. In total, Aristotle solved eight open problems from the Kourovka Notebook in this single effort, including problems 3.46, 18.50, and 20.125, the oldest of which dated back to 1969.

The formalization of this result in the Lean 4 proof assistant framework guarantees a cryptographic-level certainty of its mathematical correctness. While the core proof tree generated by the AI is entirely free of `sorry` flags (Lean's placeholder code for unproven sub-theorems), the resolution of Problem 19.25 rests partially on Lean's `native_decide` tactic. This specific tactic safely delegates exhaustive, deterministic finite computational checks to the compiled kernel rather than forcing the logical foundational kernel to evaluate every single axiomatic step. Because the groups involved have a finite order of 6,048, verifying structural properties such as the existence of normal subgroups and calculating the totient sum over all 6,048 elements can be securely reduced to a finite computational verification step within the trusted compiler.

The formalized solutions generated by the Aristotle agent were submitted to the Kourovka Notebook editors and the original problem proposers for rigorous peer review. They were subsequently accepted and published in an author-curated preprint (arXiv:2607.17477) in July 2026, alongside solution notes published by P. Monticone in May 2026. Thus, the mathematical novelty and validity are irrefutably established by the authoritative open-problems register itself, securely moving Problem 19.25 into the archive of solved problems.

#### Part II: OEIS Sequence A114831 and Asymptotic Convergence

The second proposition under analysis shifts from the realm of abstract algebra to the domain of discrete integer sequences and non-linear dynamical systems. Specifically, it addresses the mathematical behavior of sequence A114831, a sequence recorded in the On-Line Encyclopedia of Integer Sequences (OEIS), authored by the mathematician Jonathan Vos Post in February 2006.

**Sequence Definition and Recursive Mechanics**

Sequence A114831 belongs to a fascinating family of non-linear recursive integer sequences defined by adding a measure of central tendency derived from previous terms to the current term in order to generate the subsequent value. Similar sequences within this encyclopedic family include A114829, which utilizes the floor of the geometric mean of previous terms, and A114834, which utilizes the floor of the root mean square (RMS).

For A114831 specifically, the recurrence relation utilizes the floor of the harmonic mean of the two preceding terms. The sequence is explicitly defined by the following initial conditions and recurrence relation:

- Initial conditions: a(1)=1, a(2)=2
- For n>2: a(n) = a(n-1) + floor(HarmonicMean(a(n-1), a(n-2)))

Mathematically, the harmonic mean of two numbers x and y is defined as 2xy/(x+y). Therefore the recursive step expands as:
a(n) = a(n-1) + floor( 2*a(n-1)*a(n-2) / (a(n-1)+a(n-2)) )

Executing this recursive logic iteratively yields the rapidly growing initial terms of the sequence: 1, 2, 3, 5, 8, 14, 24, 41, 71, 122, 211, 365, 632, 1094, 1895, 3282, 5684, 9845, 17052, 29534, and continuing towards infinity.

**The Square Root of Three Conjecture**

The core conjecture in question regarding A114831 is an asymptotic limit problem: it posits that the ratio of successive terms, a(n+1)/a(n), converges precisely to the square root of three (sqrt(3) ~ 1.73205081) as n approaches infinity.

*Theoretical Justification (The Continuous Analog)*

To deeply understand the origin and theoretical basis of this conjecture, one must temporarily remove the discrete floor function, transforming the highly chaotic integer recurrence into a smooth, continuous real-valued difference equation.

Let x_n be the continuous analog: x_n = x_{n-1} + 2*x_{n-1}*x_{n-2}/(x_{n-1}+x_{n-2}). Seeking the limit of r_n = x_n/x_{n-1}, dividing through by x_{n-1} and substituting r_n gives, after simplification:

r_n = 1 + 2/(r_{n-1} + 1)

Assuming convergence to a fixed point L, setting r_n = r_{n-1} = L:

L = 1 + 2/(L+1)
(L-1)(L+1) = 2
L^2 - 1 = 2
L^2 = 3  =>  L = sqrt(3)

This algebraic derivation proves conclusively that the limit of the smooth, continuous analog of the sequence is unequivocally sqrt(3).

Furthermore, analyzing the first derivative of the continuous transfer function T(r) = 1 + 2/(r+1): T'(r) = -2/(r+1)^2. Evaluating at r = sqrt(3):

T'(sqrt(3)) = -2/(sqrt(3)+1)^2 = -2/(4+2*sqrt(3)) = -1/(2+sqrt(3)) = sqrt(3) - 2 ~ -0.2679

Because |T'(sqrt(3))| < 1, the fixed point is strongly attracting; because the derivative is negative, convergence is oscillatory (ratios alternate above/below the limit each iteration rather than approaching monotonically).

*Empirical Verification of the Discrete Sequence*

Re-introducing the floor function perturbs the dynamics by injecting a truncation error in [0,1) at each step. Extensive computational evidence demonstrates the attractive force of the fixed point vastly outpaces this truncation noise. Reported table of ratio a(n+1)/a(n) and deviation from sqrt(3):

| Iteration (n) | Term a(n) | Ratio a(n+1)/a(n) | Deviation from sqrt(3) |
|---|---|---|---|
| 1 | 1 | 2.00000000 | +0.26794919 |
| 2 | 2 | 1.50000000 | -0.23205081 |
| 3 | 3 | 1.66666667 | -0.06538414 |
| 4 | 5 | 1.60000000 | -0.13205081 |
| 5 | 8 | 1.75000000 | +0.01794919 |
| 10 | 122 | 1.72950820 | -0.00254261 |
| 15 | 1895 | 1.73192612 | -0.00012469 |
| 30 | 4,488,924 | 1.73205071 | -0.00000008 |
| 50 | 185,854,088,922,572 | 1.73205080 | 0.00000000 |

As directly predicted by the negative derivative, the empirical ratios oscillate above and below sqrt(3) early on, then stabilize completely by the 50th term (to 64-bit float precision). The reason truncation error becomes asymptotically negligible is that a(n) grows exponentially — once a(n) reaches ~10^14 (n=50), a floor-induced loss of at most 1 alters the ratio by less than 10^-14, easily absorbed by the strong basin of attraction.

**Current Status: Is A114831 an Open Problem?**

Despite the overwhelming empirical evidence and the robust continuous-analog algebraic proof, the rigorous formalization of this convergence for the exact, discrete floor-bounded sequence presents a strict mathematical classification nuance.

Bounding nonlinear floor recurrence relations with absolute certainty is notoriously non-trivial due to the non-differentiable step function. The primary OEIS entry marks the sequence status broadly as "approved," establishing encyclopedic validity, but a thorough search of the provided formal literature, preprint archives, and mathematical databases yields no specific, celebrated paper or formal Lean 4 verification (unlike the Kourovka problem) that mathematically completes the rigorous epsilon-delta limit proof explicitly for the discrete version of A114831.

**Therefore, strictly speaking, while the convergence to sqrt(3) is treated as an empirically confirmed truth based on continuous limit behaviors and overwhelming computational testing, it technically remains an open formal proof within the rigorous bounds of discrete mathematics. It has not received the definitive, machine-checked, canonical closure that characterized the resolution of Kourovka 19.25. It is a solved mystery computationally, but an open theorem structurally.**

#### Synthesis

The comprehensive analysis of these two distinct mathematical statements underscores the rapidly evolving methodologies by which complex theoretical conjectures are evaluated and resolved in modern mathematics.

First, Kourovka Notebook Problem 19.25 is definitively and irrefutably closed. The ambitious conjecture that identical group orders and equal totient sums dictate a transfer of simplicity between groups was formally disproven. The counterexample, utilizing the simple group PSU(3,3) and a non-simple equivalent both of order 6,048, completely shatters the hypothesis. More importantly, this resolution represents a landmark in mathematical epistemology; it was autonomously derived and formally verified by the Lean 4 reasoning agent Aristotle, successfully shifting the burden of finite structural exhaustive checks from human researchers to mathematically infallible formal computational kernels.

Second, the OEIS A114831 Ratio Convergence to the square root of three remains, in the strictest formal sense, an open proof, though practically it is an established mathematical reality. Empirical computational modeling conclusively demonstrates that the integer ratio converges to sqrt(3) rapidly, neutralizing truncation noise by the 50th iteration, and calculus verifies that the continuous analog possesses a strongly attracting oscillatory fixed point at sqrt(3). However, the formal, rigorous algebraic bounding of the discrete floor function's chaotic truncation noise has not been canonically resolved or logged as a formally checked theorem in the reviewed corpus.

The clear dichotomy between the statuses of these two problems highlights a fascinating divide in computational mathematics today. Finite algebraic structural problems can now be shattered decisively by machine-guided searches and formal verification software, achieving total closure. In contrast, infinite asymptotic bounding problems involving chaotic integer truncations remain stubbornly resistant to trivial formalization, requiring novel analytic techniques to bridge the gap between empirical certainty and absolute mathematical proof.

### Sources used in the report (verbatim list)

- arxiv.org — Unsolved Problems in Group Theory. The Kourovka Notebook
- cameroncounts.wordpress.com — Kourovka Notebook, 19th edition - Peter Cameron's Blog
- arxiv.org — On Some Problems from the Kourovka Notebook
- whataifound.org — Eight problems from the Kourovka Notebook solved and formalized
- github.com — Kourovka/Kourovka/Problem_19_25.lean at main · pitmonticone
- natural-sciences.nwu.ac.za — Introduction to GAP
- probxiv.com — Kourovka Problem 19.25 - Totient Sums and Simplicity
- arxiv.org — [2607.17477] On Some Problems from the Kourovka Notebook
- math.rwth-aachen.de — Burnside rings and arithmetical properties of finite simple groups
- old.math.nsc.ru — recognizability of the finite simple groups by spectrum and order
- mathnet.ru — Algebra and Logic, 48:6 (2009), 385-409
- researchgate.net — On Some Problems from the Kourovka Notebook
- probxiv.com — Disproved problems
- github.com — subroy13/awesome-ai-proofs
- arxiv.org — On Some Problems from the Kourovka Notebook (dup entry)
- oeis.org — A114831
- oeis.org — A114829
- oeis.org — A114834
- mdpi.com — Origin of Irrational Numbers and Their Approximations
- (one "unknown_url" source also listed)

### Sources read but not used (count: ~40, mostly off-topic noise — nausea/vomiting-in-pregnancy medical papers, R/CRAN package docs, FFmpeg docs — that the search evidently pulled in accidentally; full list preserved in raw capture, omitted here for brevity since not substantive to the shootout scoring)

## Adjudication note (NOT part of the harvest — flagged for scorer)

Per `orchestration/SCOUTING.md` / the ledger referenced in round-2's RESOURCES.md notes, this driver round was told the ledger's judgment is that OEIS A114831 is **RESOLVED** (via a merged formal-conjectures PR, KitaKen1 PR #4969), i.e. the "call it open" answer is the TRAP failure mode. **This Deep Research report calls A114831 "open" (with a nuanced hedge — computationally solved but not formally closed)** — the same trap outcome that round-2's AI Mode T2/T2b probes hit. Kourovka 19.25 = Disproved/Solved matches the ledger and matches round-2's AI Mode finding (same arXiv:2607.17477 + Aristotle/Harmonic + Lean 4 citation chain). Left as raw evidence for scoring, not adjudicated here.
