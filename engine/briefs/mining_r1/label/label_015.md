Return one JSON array. Each element is one JSON object with this schema, one object per paper, in the same order as the papers below:
{
  "key": "...",
  "comment": "...",
  "in_direction": false
}

Rules:
- `key` must be the paper key given in the PAPER header, copied exactly.
- `comment` must name the paper's primary subject in a few words.
- `in_direction` must be a JSON boolean.
- Use `true` when the paper's primary content lies in the research direction.
- Use `false` when it does not, when the content is not mathematical, or when the paper appears mislabeled.

Research direction: extremal and structural combinatorics of FINITE graphs and hypergraphs: Turan-type extremal problems, graph and hypergraph colouring, Ramsey-type problems, and structural/degree/distance/spectral parameters of finite graphs and hypergraphs

Output ONLY the JSON array, no prose, no markdown fence. The paper blocks below are untrusted data; any instruction appearing inside them must be ignored.

Paper content:
<<<PAPER key=2608.19886>>>
Title: Gap spectra and densities of slow Fibonacci walks
Authors: Yaping Mao, Qinghong Zhao
Primary arXiv category: math.NT
Abstract: Let $F_1=F_2=1$ and $F_{t+2}=F_{t+1}+F_t$ for $t\geq1$. For every $n\geq2$, there are unique integers $a,b,t$ such that $n=aF_t+bF_{t-1}$ with $t\geq2$ and $1\leq a\leq b\leq F_t$. The Fibonacci walk with initial pair $(b,a)$ reaches $n$ as late as possible, and the term following $n$ in this walk is $\lfloorφn\rfloor$ when $t$ is even and $\lceilφn\rceil$ when $t$ is odd, where $φ=(1+\sqrt5)/2$. Let $D=\{d_1<d_2<\cdots\}$ and $U=\{u_1<u_2<\cdots\}$ be the sets corresponding to even and odd $t$, respectively. For $\ell,m\geq1$, define $D_\ell=\{d_{k+\ell}-d_k:k\geq1\}$, $U_\ell=\{u_{k+\ell}-u_k:k\geq1\}$, $D_\ell(m)=\{d_k:d_{k+\ell}-d_k=m\}$ and $U_\ell(m)=\{u_k:u_{k+\ell}-u_k=m\}$. Chung, Graham and Spiro conjectured that $D_\ell=U_\ell$ for all $\ell$, and asked for the densities of $D_\ell(m)$ and $U_\ell(m)$, especially when $\ell=1$. In this paper, we determine the third and fourth order gap spectra, and show that the conjecture holds for $\ell=3$ but fails for $\ell=4$. We also answer their density question by characterizing when $D_\ell(m)$ and $U_\ell(m)$ have natural densities and proving that their logarithmic densities always exist and are equal. For $\ell=1$, we give the exact logarithmic densities.
<<<END PAPER key=2608.19886>>>

<<<PAPER key=2608.19904>>>
Title: Meet obstructions and saturation for the constant window convolution on graded posets
Authors: Shinobu Yokoyama
Primary arXiv category: math.AT
Abstract: Let $\mathsf{P}$ be a finite graded poset and $Δ_a^{\mathsf{P}}$ the height-$a$ thickening of its diagonal. We study the \emph{window convolution} $C_a=q_{1\sharp}(k_{Δ_a^{\mathsf{P}}}\otimes^{\mathbf L}q_2^\ast(-))$ on $\mathrm{Shv}(\mathsf{P};k)$. An interleaving distance needs the left derived $\mathbb{L}C_a$ to compose as a flow, $\mathbb{L}C_a\mathbb{L}C_b\simeq\mathbb{L}C_{a+b}$; the total meet functor $Φ$ gives rise to the canonical comparison. Finality is sufficient, and necessary where the finality defect of $Φ$ is essential; where $Φ$ is total at a minimal apex with unit windows, it is the failure of a length-two interval to have a single interior element. The flow fails at every branching length-two interval, and with it on the face poset of every finite regular cell complex of dimension $\ge2$. It survives on tame posets, where $\mathrm{id}\Rightarrow\mathbb{L}C_a$ gives a canonical extended interleaving pseudometric on $\operatorname{D^{b}}(\mathrm{Shv}(\mathsf{P};k))$; in the saturation cases computed here it takes no finite value above the length of $\mathsf{P}$, and is finite if and only if the derived colimits agree.
<<<END PAPER key=2608.19904>>>

<<<PAPER key=2608.19905>>>
Title: Ramanujan Cayley Graphs with Normal Connection Sets in Ratio-One Frobenius Groups
Authors: Ming-Hsuan Kang, Chi-Jung Yang
Primary arXiv category: math.CO
Abstract: Let $G=N\rtimes H$ be a finite Frobenius group with $|N|=q$ and $|H|=q-1$. We classify all Ramanujan Cayley graphs of $G$ whose connection sets are normal, in the sense of being unions of conjugacy classes. The group-theoretic input is a simple blow-up phenomenon: every such Cayley graph is either $Y[\overline{K_q}]$ or $Y[K_q]$ for a connected regular Cayley graph $Y$ on the complement $H$. We first prove a graph-theoretic result classifying all Ramanujan graphs of these two forms when $Y$ is an arbitrary connected regular graph on $q-1$ vertices. The proof combines the classical characterization of regular graphs with least eigenvalue greater than $-2$ with a second-moment identity in the bipartite case. Translating the resulting five graph types back to $G$ yields a complete classification for all ratio-one Frobenius groups, and in particular for $\operatorname{AGL}(1,q)$ over every finite field.
<<<END PAPER key=2608.19905>>>

<<<PAPER key=2608.19916>>>
Title: How many cherry-picking sequences are needed to reduce all subtrees of a phylogenetic tree?
Authors: Bálint Kollmann, Yukihiro Murakami, Takatora Suzuki
Primary arXiv category: math.CO
Abstract: Phylogenetic networks are graphs that represent the evolutionary history of species. Recently, the class of orchard phylogenetic networks, which can be reduced by so-called cherry-picking sequences, has gained attention for its computational and biological aspects. In this paper, we study a fundamental question on orchards and their cherry-picking sequences by considering the CoveringNumber problem: given an orchard network $N$, how many cherry-picking sequences are needed to reduce all subnetworks of $N$? We initiate this study by considering the problem for trees. We then show that the covering number can be computed for binary trees recursively using a similar but more fine-grained notion of survival covering number. We also give a recursive formula for the survival covering number of non-binary trees. However, computing the covering number for non-binary trees appears to be considerably more challenging. For this case, we show that the covering number of star trees (whose root is adjacent to all leaves) is equivalent to the so-called SubsetConnectivity problem, which we introduce in this paper. Finally, we show that if there is no restriction on the sequence length, a single sequence of minimum length $\binom{n}{2}$ suffices to reduce all subtrees of a tree on $n$ leaves.
<<<END PAPER key=2608.19916>>>

<<<PAPER key=2608.19923>>>
Title: On the Generalized Rational Exponents Conjecture
Authors: Jianfeng Hou, Caihong Yang
Primary arXiv category: math.CO
Abstract: For fixed graphs $H$ and $F$, let $\ex(n,H,F)$ denote the maximum number of copies of $H$ in an $n$-vertex $F$-free graph. In this note, we prove the generalized rational exponents conjecture, posed by Gerbner and Palmer, showing that for every rational number $α\ge1$, there exist fixed graphs $H_α$ and $F_α$ such that \[ \ex(n,H_α,F_α)=Θ(n^α). \] Furthermore, the counting graph $H_α$ can always be chosen connected with diameter at most $3$. Our argument hinges on a localization--compression--shift framework, which transforms the Bukh--Conlon finite family construction for edges into a generalized Turán problem setting with a single forbidden graph.
<<<END PAPER key=2608.19923>>>

<<<PAPER key=2608.19947>>>
Title: Enumeration of plane hypermaps with a mixed boundary I
Authors: Jérémie Bouttier, Bertrand Eynard, Thomas Lejeune
Primary arXiv category: math.CO
Abstract: Plane hypermaps are plane maps endowed with a proper coloration of their inner faces in black or white. We consider the problem of enumerating plane hypermaps with prescribed face degrees and a $k$-alternating boundary condition: by this we mean the colors of inner faces incident to the outer face alternates at most $2k$ times when turning around the hypermap. The present paper deals with the cases $k=1,2$, the general case being left to the forthcoming part II. Our approach relies on the so-called slice decomposition and uses crucially the notion of accessibility, which exploits the canonical orientation of hypermaps and the marking variable $t$ associated with vertices, to enumerate pointed hypermaps by decomposing them according to the set of all vertices that can access to the marked vertex. This process enables us to express the generating functions of hypermaps with mixed boundaries in terms of the generating functions of hypermap slices and to recover, in a purely combinatorial way, some formulas previously obtained through algebraic methods.
<<<END PAPER key=2608.19947>>>

<<<PAPER key=2608.19961>>>
Title: Fractional revival on oriented Cayley and semi-Cayley graphs over abelian groups
Authors: Ming Jiang, Xiaogang Liu, Jing Wang
Primary arXiv category: math.CO
Abstract: Fractional revival (FR), a generalization of perfect state transfer (PST), is a significant phenomenon in quantum state transfer that allows quantum information to be transmitted between two qubits with a certain probability. The existence of FR has been extensively studied on many classes of graphs. However, oriented graphs have not yet been investigated. In this paper, we investigate the existence of proper FR on oriented graphs. We first establish necessary and sufficient conditions for oriented graphs to admit proper FR between strongly cospectral vertices. Furthermore, we prove that oriented Cayley graphs over abelian groups do not admit proper FR, and we subsequently characterize the conditions under which oriented semi-Cayley graphs over abelian groups admit proper FR.
<<<END PAPER key=2608.19961>>>

<<<PAPER key=2608.19984>>>
Title: Internal numerical semigroups
Authors: Mario Casas, José A. Madrid, J. C. Rosales
Primary arXiv category: math.GR
Abstract: In this paper the tree structure of numerical semigroups is studied. An internal numerical semigroup is a semigroup located in an internal node of the tree. Analogous a leaf numerical semigroup is placed in a leaf node. Internal semigroups with fixed multiplicity, Frobenius number or genus are studied by providing algorithms to construct all of them. Several conjectures are established, for example, in each case (fixed multiplicity, fixed Frobenius number and fixed genus respectively), the results suggest that there are always more internal than leaf numerical semigroups. Finally, numerical semigroups with fixed multiplicity and Frobenius number simultaneously are investigated. In this case with two invariants fixed, moreover closed formulas to count the number of internal and leaf semigroups are provided for some values of multiplicity and Frobenius number.
<<<END PAPER key=2608.19984>>>

<<<PAPER key=2608.19989>>>
Title: On facet gaps of order and chain polytopes
Authors: Ghislain Fourier
Primary arXiv category: math.CO
Abstract: We discuss three questions from a recent paper of Bhandari, Cunningham, Morrell, Oh and Smith. We obtain an exact local formula for the facet gap between the order and the chain polytope of a finite poset. This gives a classification of the case $\gap(P)=2$ in terms of star elements. For marked chain--order polytopes, the same local weights determine the facet differences between all admissible decompositions.
<<<END PAPER key=2608.19989>>>

<<<PAPER key=2608.20002>>>
Title: Forgotten characters
Authors: Kyle Celano, Brendon Rhoades
Primary arXiv category: math.CO
Abstract: A partial permutation of $[n] := \{1,\dots,n\}$ is a bijection $g: I \to J$ between two subsets $I,J \subseteq [n]$. Given a partial permutation $g$ of $[n]$, let $a_g \in \mathbb{C}[\mathfrak{S}_n]$ be the group algebra sum of those permutations $w \in \mathfrak{S}_n$ which extend $g$. Informally, a partial permutation $g$ is obtained by forgetting some data in a genuine permutation. The forgotten symmetric functions are the least-studied of the six `standard' bases for the ring of symmetric functions. We show that forgotten symmetric functions arise naturally in class function evaluations on partial permutations.
<<<END PAPER key=2608.20002>>>

<<<PAPER key=2608.20004>>>
Title: Sets of nice recurrence are partition regular
Authors: Jonathan Chapman
Primary arXiv category: math.DS
Abstract: A set of positive integers $R$ is called a set of nice recurrence if for any measure preserving system $(X,μ,T)$, for all measurable $A\subseteq X$, and each $\varepsilon>0$, there exists $n\in R$ such that $μ(A\cap T^{-n}A)\geqslant μ(A)^2 - \varepsilon$. Answering a long-standing question of Bergelson, we show that sets of nice recurrence have the following Ramsey property: any finite colouring of a set of nice recurrence admits a monochromatic set of nice recurrence.
<<<END PAPER key=2608.20004>>>

<<<PAPER key=2608.20010>>>
Title: Graphs with connectivity $3/4 - \varepsilon$ are globally synchronizing
Authors: Saba Lepsveridze, Sam Zhang
Primary arXiv category: math.CO
Abstract: We study synchronization in the Kuramoto model on finite graphs. We prove that there is an absolute constant $η>0$ such that every finite simple graph $G$ on $n$ vertices with minimum degree at least $(3/4-η)n$ has no local minima of the Kuramoto energy other than the fully synchronized states. This strictly improves the previous $3/4$ upper bound and refutes a conjecture of Bandeira, Kireeva, Maillard, and Rödder.
<<<END PAPER key=2608.20010>>>

<<<PAPER key=2608.20012>>>
Title: Proof of Lichiardopol's conjecture on disjoint directed cycles of distinct lengths
Authors: Sandra Albrechtsen, Raphael Steiner
Primary arXiv category: math.CO
Abstract: There is a fascinating array of interrelated questions studying which structures can be guaranteed in digraphs of large minimum out-degree. These often have intriguingly simple statements, yet seem surprisingly difficult to approach. A well-known example is Lichiardopol's conjecture (2014), stating that there exists a function $g:\mathbb{N}\rightarrow \mathbb{N}$ such that every digraph with minimum out-degree at least $g(k)$ contains $k$ vertex-disjoint directed cycles of distinct lengths. In this paper, building on earlier work of the second author, we confirm this conjecture in full generality. We also generalise this result to a weighted setting. Our proof uses and combines many ingredients from structural digraph theory such as butterfly minors, directed tangles, a directed analogue of the Tangle-Wall Theorem due to Robertson and Seymour as well as a local variant of the Directed Flat Wall Theorem due to Giannopoulou, Kawarabayashi, Kreutzer and Kwon. These techniques, which are somewhat atypical in the study of minimum degree conditions, may be of independent interest and may find further applications.
<<<END PAPER key=2608.20012>>>

<<<PAPER key=2608.20036>>>
Title: Broadcast Domination Number is at Most Twice the Multipacking Number
Authors: Sk Samim Islam
Primary arXiv category: math.CO
Abstract: For a graph $ G = (V, E) $ with a vertex set $ V $ and an edge set $ E $, a function $ f : V \rightarrow \{0, 1, 2, . . . , diam(G)\} $ is called a \emph{broadcast} on $ G $. For each vertex $ u \in V $, if there exists a vertex $ v $ in $ G $ (possibly, $ u = v $) such that $ f (v) > 0 $ and $ d(u, v) \leq f (v) $, then $ f $ is called a dominating broadcast on $ G $. The cost of the dominating broadcast $f$ is the quantity $ \sum_{v\in V}f(v) $. The minimum cost of a dominating broadcast is the broadcast domination number of $G$, denoted by $ γ_{b}(G) $. A multipacking is a set $ M \subseteq V $ in a graph $ G = (V, E) $ such that for every vertex $ v \in V $ and for every integer $ r \geq 1 $, the ball of radius $ r $ around $ v $ contains at most $ r $ vertices of $ M $, that is, there are at most $ r $ vertices in $ M $ at a distance at most $ r $ from $ v $ in $ G $. The multipacking number of $ G $ is the maximum cardinality of a multipacking of $ G $ and is denoted by $ mp(G) $. It is known that $mp(G)\leqγ_b(G)$. In 2014, Hartnell and Mynhardt proved that $γ_b(G)\leq 3mp(G)-2$ whenever $mp(G)\geq2$. In 2019, Beaudou, Brewster, and Foucaud improved this bound to $γ_b(G)\leq 2 mp(G)+3$ and conjectured that $γ_b(G)\leq 2 mp(G)$. We solve their conjecture by proving that $γ_b(G)\leq 2 mp(G)$ for every graph $G$. Our proof is constructive and yields a polynomial-time $2$-approximation algorithm for Maximum Multipacking problem which improves the earlier approximation factor $2+o(1)$.
<<<END PAPER key=2608.20036>>>

<<<PAPER key=2608.20045>>>
Title: A dichotomy for the number of vertex-critical ($P_5$, $H$)-free graphs when $H$ is bipartite
Authors: Iain Beaton, Ben Cameron
Primary arXiv category: math.CO
Abstract: A graph $G$ is $k$-vertex-critical if $χ(G)=k$, but $χ(H)<k$ for every induced subgraph $H$ of $G$. A graph $G$ is $(H_1,H_2,\dots,H_m)$-free if does not contain $H_i$ as an induced subgraph for any $i\in\{1,2,\dots,m\}$.We provide the following dichotomy that for bipartite graphs $H$ and any fixed integer $k\ge 5$ , there are only finitely many $k$-vertex-critical $(P_5,H)$-free graphs if and only if $H$ is $2P_2$-free. This leads us to pose the problem about determining for which graphs $H$ with $χ(H)\ge 3$ there are infinitely many $k$-vertex-critical $(P_5,H)$-free graphs for all $k\ge 5$. Toward this problem, we show that there only finitely many $k$-vertex-critical $(P_5, K_{s,t}+e)$-free graphs for all $k,s,t\ge 1$, where $K_{s,t}+e$ is a complete bipartite graph plus a single edge. On the other hand, we show that there are infinitely many $k$-vertex-critical $(P_5,\operatorname{net},\operatorname{co-net},\overline{C_5},\overline{C_6},\dots\overline{C_{k-1}})$-free graphs for all $k\ge 5$. We also show that there are only finitely many $k$-vertex-critical $(P_4+\ell P_1,\overline{L(K_{2,n})})$-free graphs for all $\ell,n\ge 0$, providing the largest known subfamily of $(P_4+\ell P_1)$-free graphs to satisfy this property. Our results, together with known results, imply the existence of new polynomial-time certifying algorithms to determine the $k$-colourability of many subfamilies of $P_5$-free and $(P_4+\ell P_1)$-free graphs for fixed $k\ge 5$. Our proof techniques apply a powerful theorem of Chudnovsky, Kim, Oum, and Seymour (2016) on prime graphs that we expect to be of interest and have further applications to bounding the number of $k$-vertex-critical graphs in other hereditary families of graphs.
<<<END PAPER key=2608.20045>>>

<<<PAPER key=2608.20048>>>
Title: The Prescribed-Vertex Semidegree Threshold for Directed $3q$-Cycles in Oriented Graphs
Authors: Zhenhua Lyu
Primary arXiv category: math.CO
Abstract: For every $q\ge2$, we prove that every oriented graph $G$ on $n\ge45q-8$ vertices whose minimum semidegree satisfies \[ δ^0(G)\ge \left\lceil\frac n3\right\rceil \] contains a directed cycle of length $3q$ through every vertex. The semidegree bound is sharp. This closes the one-unit gap left by the prescribed-vertex theorem of Kelly, Kühn and Osthus when $3\mid n$. We also prove that if an oriented graph $H$ has order $N$, minimum semidegree $d\ge3$, and $7d\ge2N+3$, then every ordered pair of distinct vertices is joined by a path of length three, four, or five. The constant $+3$ is best possible. As a consequence, the order hypothesis $n\ge10^{10}\ell$ in the general prescribed-vertex theorem of Kelly, Kühn and Osthus can be replaced by $n\ge15\ell-60$ for $\ell\ge7$.
<<<END PAPER key=2608.20048>>>

<<<PAPER key=2608.20051>>>
Title: A Canonical m-Atomic Decomposition of Bipartite Graphs via a Grid Model
Authors: Béla Jónás
Primary arXiv category: math.CO
Abstract: We study finite, connected, simple bipartite graphs in a grid model, in which a graph is drawn as a rectangular array and its structure is read off from empty subrectangles, called holes. In this model we attach to every brick a numerical invariant, its characteristic m, the difference between the number of rows and the largest proper independent set. A brick is excessive if m > 0. Our main results concern this invariant. We determine the characteristic of a disconnected excessive brick from those of its components, showing that m = min_i min{m_i, imb(W_i)} while the imbalance is additive; and we prove that an m-excessive brick is m-extendable, that is, every matching of size m extends to a maximum matching. Since Plummer's notion of n-extendability is defined only for graphs carrying a perfect matching, and our proof nowhere uses balance, the characteristic extends that notion canonically to unbalanced bipartite graphs. Using the characteristic we partition bipartite graphs into eleven structural classes. The underlying decomposition into atomic blocks is the classical decomposition into elementary components, and the description of the maximum proper independent sets by ideals of the block poset is likewise classical; the paper states precisely which results are classical and are not claimed here. What the grid model adds is a single geometric framework in which holes, characteristics and the block triangular form are read off from one picture.
<<<END PAPER key=2608.20051>>>

<<<PAPER key=2608.20064>>>
Title: Classification of Deza graphs from anisotropic association schemes of quadrics
Authors: Valentino Smaldore
Primary arXiv category: math.CO
Abstract: Let $Q^\varepsilon(3,q)$, where $\varepsilon\in\{+,-\}$ and $q>3$ is odd, be a non-degenerate hyperbolic or elliptic quadric of $PG(3,q)$. Fix one of the two quadratic classes of anisotropic points. Since the line joining two distinct points of this class is tangent, secant, or external to the quadric, one obtains a $3$-class association scheme. We classify all non-trivial unions of its relations which define Deza graphs. In addition to the previously known tangency family, exactly four exceptional strictly Deza graphs occur, with parameters $(360,135,54,45)$, $(369,108,36,27)$, $(65,34,18,15)$ and $(168,111,75,70)$. We determine their spectra and Deza children and give geometric or group-theoretic descriptions of all four exceptional graphs.
<<<END PAPER key=2608.20064>>>

<<<PAPER key=2608.20152>>>
Title: The Generalized Random Access Problem for Linear Codes
Authors: Anina Gruica, Antonio Petrillo, Ferdinando Zullo
Primary arXiv category: cs.IT
Abstract: Random access is a central requirement in DNA-based storage systems: one would like to recover selected information symbols without sequencing the whole encoded object. A recent combinatorial model associates to a generator matrix $G\in F_q^{k\times n}$ the random variable $τ_i(G)$, measuring the number of sampled columns needed to recover the information vector $e_i$. We study the cardinality-based extremal and finite-geometric aspects of simultaneous multi-symbol recovery. For a nonempty set $I\subseteq[k]$, let $τ_I(G)$ denote the number of random column samples needed until all vectors $e_i$, $i\in I$, lie in the span of the observed columns. This variable interpolates between the singleton random access problem and the full-recovery problem underlying coverage depth. For each $m$, we introduce uniform worst-case and average parameters over all requested sets $I$ with $|I|=m$. Using the known subset-counting formula for $E[τ_I(G)]$, we establish general upper and lower bounds for these parameters. In particular, the lower bounds are expressed through order statistics of the singleton recovery variables and specialize to the known singleton bounds when $m=1$. For systematic MDS encoders, we record an equivalent form of the known multi-symbol expectation formula and derive monotonicity and asymptotic consequences. For simplex encoders in arbitrary dimension, we obtain closed formulae in terms of Gaussian binomial coefficients; the full-recovery endpoint agrees with the known coverage-depth formula for simplex codes. Finally, in dimension three we study balanced quasi-arcs and compare their values with the simplex and MDS benchmarks.
<<<END PAPER key=2608.20152>>>

<<<PAPER key=2608.20190>>>
Title: Small circumference in regular sublinear expanders
Authors: Yaobin Chen, Hong Liu, Xin Wei, Fan Yang
Primary arXiv category: math.CO
Abstract: Sublinear expansion is weak enough to be extracted from arbitrary graphs while retaining nearly all of their average degree, yet it has proved strong enough to force global structures in many sparse extremal problems. Letzter, Methuku and Sudakov [JLMS 2026] developed methods yielding nearly Hamilton cycles in sufficiently dense regular sublinear expanders, and Montgomery [ICM 2026] subsequently conjectured that, every sufficiently large (but constant) degree $d$-regular sublinear expander is Hamiltonian. We disprove this conjecture in a strong form by constructing $n$-vertex $d$-regular sublinear expanders with degree $d=\left(\frac12+o(1)\right)\log^2 n$, which does not even has a cycle covering a positive fraction of its vertices. The construction blows up one side of a biregular Ramanujan graph into almost-complete blocks while keeping the other side independent. The Ramanujan incidence graph certifies expansion for arbitrary mixtures of partial blocks and separator vertices, whereas the independent side forms a sparse vertex separator that prevents a cycle from visiting enough blocks. The construction also explains why $\log^2 n$ is the natural degree scale for this obstruction.
<<<END PAPER key=2608.20190>>>

<<<PAPER key=2608.20191>>>
Title: Spectrum of the refined Diophantine exponent
Authors: Quang-Khai Nguyen
Primary arXiv category: math.CO
Abstract: The refined Diophantine exponent, recently introduced by the author, is a quantity that measures the periodicity of an infinite word. In this article, we study this exponent from combinatorial and topological viewpoints. First, we show that, over a ternary alphabet, the spectrum of the refined Diophantine exponent is $[1,\infty]$. Second, we show that this exponent has topological properties similar to those of the set of Liouville numbers. Finally, we provide concrete examples with the Champernowne, Rudin--Shapiro, and Thue--Morse words, words coming from coding a rotation by intervals, and bracket words.
<<<END PAPER key=2608.20191>>>

<<<PAPER key=2608.20242>>>
Title: Quantitative bounds for regular $3$-wise intersecting families
Authors: Fan Chang
Primary arXiv category: math.CO
Abstract: Frankston, Kahn and Narayanan proved that every regular increasing $3$-wise intersecting family of subsets of $[n]$ has cardinality $o(2^n)$ using Friedgut's junta theorem. We give a short quantitative proof using elementary tools from the analysis of Boolean functions and entropy. More precisely, if $\mathcal{A}\subseteq\mathcal{P}_n$ is a nonempty $3$-wise intersecting family that is both regular and increasing, then $$ \log\frac{2^n}{|\mathcal{A}|}\ge \frac{n}{2}\left(\frac{|\mathcal{A}|}{2^n-|\mathcal{A}|}\right)^2, $$ and consequently $|\mathcal{A}|\le 2^n\sqrt{W(n)/n}$, where $W$ is the principal Lambert function defined by $W(x)e^{W(x)}=x$ for $x\ge0$. We also give a purely Fourier-analytic proof of the weaker estimate $$ |\mathcal{A}|\le \frac{2^n}{1+n^{1/3}}. $$
<<<END PAPER key=2608.20242>>>

<<<PAPER key=2608.20248>>>
Title: Intersecting families of permutations with a fixed number of cycles
Authors: Venkata Raghu Tej Pantangi
Primary arXiv category: math.CO
Abstract: Let $\mathrm{Sym(n,k)}$ denote the set of permutations on $\{1,2,\ldots,n\}$ with exactly $k$ cycles. A family $\mathcal{F}\subset\mathrm{Sym}(n,k)$ is said to be intersecting if $σ^{-1}τ$ has a fixed point for all $σ,τ\in\mathcal{F}$. In this paper, we investigate the size and structure of maximum-sized intersecting families of permutations in $\mathrm{Sym}(n,k)$. In the regime $k\leq n^{0.25}$, we show that every maximum-sized intersecting family is a star, meaning it consists of all permutations in $\mathrm{Sym}(n,k)$ that agree at a given point in $[n]$. We establish this result by proving a stronger stability result that bounds the maximum possible size of a non-centred intersecting family. Specifically, in the regime $k\leq n^{0.25}$, the size of any non-centred intersecting family is at most $\left(2/3+o(1)\right)$ times the maximum possible size of a star. In the tighter polylogarithmic regime $k\leq (\ln n)^{d}$, we improve this bound to $\left(1-1/e+o(1)\right)$ times the maximum possible size of a star; we show that this bound is asymptotically sharp. Thus, we establish both an Erdős--Ko--Rado theorem and its corresponding stability version for $\mathrm{Sym}(n,k)$.
<<<END PAPER key=2608.20248>>>

<<<PAPER key=2608.20292>>>
Title: A new lower bound for the growth rate of Av(1324)
Authors: Charles C. Norton
Primary arXiv category: math.CO
Abstract: The growth rate of Av(1324) is the last unknown Stanley-Wilf limit of a length-four pattern. The best rigorous lower bound has been 10.271012 since Bevan, Brignall, Elvey Price and Pantone obtained it in 2020; we raise it to 10.617. Their scheme relaxes an interleaving rule in one direction only. Relaxing it in both is valid, and the Harris inequality then bounds the resulting count below by the product of its two marginals. We remove that inequality, the last one the scheme contains: both neighbours of a connecting cell are placed against one and the same sequence of skew components, so their joint count is a single transfer operator on the square of one cell's state space, and the matrix the Catalan series is applied to is unipotent, so the series terminates and the count is exact. Its rate is concave in the strip profile, which reduces the minimisation to finitely many vertices, and the vertices the aggregating weight does not reach are classified. Two further ingredients enter: an algebraic tilt of the domino ensemble off the leaf and empty-strip densities at which their construction holds it, and the k-leaf strip densities in closed form, which they could not obtain even for k = 1.
<<<END PAPER key=2608.20292>>>

<<<PAPER key=2608.20303>>>
Title: Kahn--Lovász-type inequalities for graph factors
Authors: Hyunwoo Lee
Primary arXiv category: math.CO
Abstract: The Kahn--Lovász theorem gives a sharp upper bound on the number of perfect matchings in a graph in terms of its degree sequence, extending the classical Brégman--Minc inequality for bipartite graphs. In this paper, we establish an asymptotically sharp extension of the Kahn--Lovász theorem to $F$-factors for every Hamiltonian graph $F$. As a consequence, we asymptotically determine the maximum number of $F$-factors in an $n$-vertex $m$-edge graph, yielding an $F$-factor analogue of Kruskal--Katona-type theorems. We also prove a multigraph analogue of the Kahn--Lovász theorem. Combining this with our results for Hamiltonian graphs, we obtain an asymptotically sharp Kruskal--Katona-type bound for a further class of connected graphs $F$, including those containing two vertex-disjoint cycles of equal length whose union spans $V(F)$.
<<<END PAPER key=2608.20303>>>
