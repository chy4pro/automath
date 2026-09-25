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
<<<PAPER key=2608.10643>>>
Title: Zero transfer on mixed graphs
Authors: Xingkun Song, Huiqiu Lin
Primary arXiv category: quant-ph
Abstract: In this paper, we investigate zero transfer on mixed graphs. Zero transfer is a quantum walk phenomenon in which the transition amplitude between two vertices is identically zero for all times, so that no quantum state transfer occurs between them. Using the Hermitian adjacency matrix, we derive necessary and sufficient conditions for zero transfer in mixed graphs. We then specialize these criteria to oriented circulant graphs, obtaining nonexistence results for prime order, structural restrictions for even order, and exhaustive computational classifications for small orders.
<<<END PAPER key=2608.10643>>>

<<<PAPER key=2608.10654>>>
Title: Fixed forests in the minimum spanning tree and cubic volume growth
Authors: Luca Makowiec
Primary arXiv category: math.PR
Abstract: Let $M_n$ be the minimum spanning tree of the complete graph $K_n$ with i.i.d.\ uniform edge weights. For a fixed forest $F$ with connected components $T_1, \ldots, T_d$, we show that there exists a function $Ψ$ on finite trees such that $$ n^{|E(F)|} \mathbb{P}_n(F \subseteq M_n) \longrightarrow \prod_{i=1}^d Ψ(T_i). $$ We give a recursive description of $Ψ$ and calculate it explicitly for several small trees. For the star $S_k$ and the path $P_k$, we prove that $Ψ(S_k) \sim ζ(2)^k$ and $Ψ(P_k) \sim k^2/12$, respectively. We also show that the expected size of a ball of radius $r$ is asymptotic to $r^3/36$, and give exponential tail bounds.
<<<END PAPER key=2608.10654>>>

<<<PAPER key=2608.10661>>>
Title: Zero-sum Inverse Realization and Property~(P) under Join Operations
Authors: G. Arunkumar, Anubhab Pahari, Puja Samanta
Primary arXiv category: math.CO
Abstract: We introduce zero-sum inverse realization of property (P) of a graph $G$, obtained by imposing an additional condition \( \mathbf{1}^{\top}A^{-1}\mathbf{1}=0, \) on a matrix $A\in S(G)$ realizing property (P), where $\mathbf{1}$ is the all-ones vector. We prove that every graph of order at least three having property (P) admits such a zero-sum inverse realization. As applications, we prove that property~(P) is preserved under the join of two graphs of order at least $3$ and, more generally, under the $H$-join of a family of graphs of order at least $3$, where $H$ is arbitrary. Consequently, we obtain sufficient conditions for cographs and lexicographic products of graphs to possess property~(P). Throughout the paper, many examples are given.
<<<END PAPER key=2608.10661>>>

<<<PAPER key=2608.10687>>>
Title: Counterexamples to two conjectures on modular edge colorings of graphs
Authors: Chunqiang Guo, Baoyindureng Wu
Primary arXiv category: math.CO
Abstract: For an integer $k\geq2$, let $χ_k'(G)$ denote the minimum number of colors in an edge-coloring of a graph $G$ such that every nonzero degree in each color subgraph is congruent to $1\pmod{k}$. A graph is a $0_k$-graph if every vertex degree is divisible by $k$. We disprove a conjecture of Berthe et al.\ (On modular edge colorings of graphs, SIAM J. Discrete Math. 40 (2026) 897--904), which states that $χ_k'(G)\leq k+o(k)$ for every $0_k$-graph $G$. We prove a lower bound for $0_k$-graphs with degree set $\{k,2k\}$ and a specified vertex partition. With a suitable choice of the part sizes, if the number of edges inside one part is $o(k^2)$, then $χ_k'(G)\geq(4-2\sqrt2+o(1))k$. This gives connected bipartite and connected nonbipartite counterexamples. In particular, the same examples also disprove the earlier conjecture of Botler, Colucci, and Kohayakawa (The mod $k$ chromatic index of graphs is $O(k)$, J. Graph Theory 102 (2023) 197--200), which states that $χ_k'(G)\leq k+C$ for some absolute constant $C$.
<<<END PAPER key=2608.10687>>>

<<<PAPER key=2608.12405>>>
Title: The Five Distance Theorem For A Convex Norm
Authors: Nikita A. Mironov, Oleg R. Musin
Primary arXiv category: math.MG
Abstract: The three gap theorem states that the points of the Kronecker sequence $α,2α,\ldots,Nα$, considered modulo one, divide the circle into intervals of at most three distinct lengths. In a two-dimensional nearest-neighbour analogue, Haynes and Marklof proved that the Kronecker sequence modulo an arbitrary unimodular lattice determines at most five distinct nearest-neighbour distances in the Euclidean norm, and that this bound is sharp. Dettmann subsequently constructed examples attaining five distinct distances for every $\ell_p$-norm, $1\leq p\leq\infty$. We prove the corresponding upper bound for every strictly convex norm on $\mathbb R^2$: for every unimodular lattice $L$, every $\boldsymbolα\in\mathbb R^2$, and every $N\in\mathbb N$, the number of distinct nearest-neighbour distances is at most five. In particular, this settles the conjectured bound for all $\ell_p$-norms with $1<p<\infty$, for which the bound is optimal. The proof extends the lattice-theoretic argument of Haynes and Marklof by replacing its Euclidean angular estimates with a cone lemma based on a proper Brass angular measure.
<<<END PAPER key=2608.12405>>>

<<<PAPER key=2608.10772>>>
Title: Differential equations for bipartite maps with bounded face degrees
Authors: Valentin Bonzom
Primary arXiv category: math.CO
Abstract: In recent years, integrable hierarchies have been used to great advantage for the enumeration of combinatorial maps. They have led to recurrence formulas with respect to the size and genus of the maps, e.g. for triangulations, bipartite quadrangulations and bipartite maps, and for constellations. These formulas are not only remarkably simple but also provide the fastest way of calculating these numbers of maps. With the exception of Louf's work on constellations, it has however remained a challenge to obtain recurrence formulas that control the degrees of the faces of the maps. Here we show how to achieve this for bipartite maps with bounded face degrees. By combining equations from the KP hierarchy and from the Virasoro constraints, a differentially algebraic system is obtained. It couples the generating functions of bipartite maps with bounded root face degrees while controlling the numbers of edges, black vertices, white vertices and number of faces of each degree (and in particular the genus). Finally, this system of ODEs is shown to give recurrence formulas that allows to calculate all the corresponding numbers of maps.
<<<END PAPER key=2608.10772>>>

<<<PAPER key=2608.10865>>>
Title: A nearcircumsphere-Ramsey Theorem for Solvable Transitive Configurations
Authors: Dömötör Pálvölgyi
Primary arXiv category: math.CO
Abstract: Let P be a finite spherical set. We prove that if P admits a solvable group of isometries acting transitively on it, then every r-coloring of a sufficiently high-dimensional sphere of radius slightly larger than the circumradius of P contains a monochromatic congruent copy of P. Our proof builds on the group-theoretic argument of Kriz and combines it with a topological method that may be of independent interest.
<<<END PAPER key=2608.10865>>>

<<<PAPER key=2608.10874>>>
Title: Complexity and algorithms for proper conflict-free coloring in graphs
Authors: Dinabandhu Pradhan, Vaishali Sharma
Primary arXiv category: cs.DM
Abstract: A proper conflict-free (PCF) $k$-coloring of a graph $G$ is a proper $k$-coloring such that there exists a color that appears exactly once in the neighborhood of every non-isolated vertex $v\in V(G)$. The PCF chromatic number, denoted by $χ_{pcf}(G)$, is the least integer $k$ such that there exists a PCF $k$-coloring of $G$. Given a graph $G$ and a positive integer $k$, PCF $k$-COLORABILITY is to decide whether $G$ admits a PCF $k$-coloring. Ahn et al. [Discrete Appl. Math. 377 (2025) 10-17] proved that PCF $k$-COLORABILITY is NP-complete for bipartite graphs. We strengthen this result by proving that PCF $k$-COLORABILITY is NP-complete for perfect elimination bipartite graphs, which is a proper subclass of bipartite graphs. We also show that the PCF chromatic number of a graph cannot be approximated within $O(n^{1-\varepsilon})$ unless P=NP, for any $\varepsilon>0$. On the positive side, we provide linear-time algorithms for PCF $k$-COLORABILITY in block graphs, proper interval graphs, chain graphs, and pseudo-split graphs. We show that $χ_{pcf}(G)\leq ω(G)+1$ for block graphs, proper interval graphs, and pseudo-split graphs (except $C_5$), and we characterize all graphs for which the equality holds.
<<<END PAPER key=2608.10874>>>

<<<PAPER key=2608.10926>>>
Title: A higher-connectivity spectral Ore theorem for triangle-free graphs
Authors: Joyentanuj Das, Sayan Gupta
Primary arXiv category: math.CO
Abstract: Let $B_{n,k}$ be the graph obtained from the balanced complete bipartite graph on $n$ vertices by deleting a matching of size $k$. If $G$ is an $n$-vertex triangle-free graph with $κ(\comp G)\geq k$, we prove that $\rhoA(G)\leq\rhoA(B_{n,k})$ for $n\geq4k+2$, with equality precisely when $G\cong B_{n,k}$, and we compute $\rhoA(B_{n,k})$ explicitly. We also solve the bipartite problem for every $n\geq2k+1$, determine the boundary value $\operatorname{spex}_κ(2k,K_3;k)=k-1$, and settle the full problem for $k=2$. In particular, $B_{n,2}$ is uniquely extremal exactly from order $6$ onward. For $k=1$, equivalently when the complement is connected, $B_{n,1}=K_{\ceil{n/2},\floor{n/2}}-e$ is uniquely extremal for every $n\geq3$.
<<<END PAPER key=2608.10926>>>

<<<PAPER key=2608.11005>>>
Title: Minimal Bridges and a Rotation-Based Bijection
Authors: Benjamin Lou, Lucas Augustus Brown
Primary arXiv category: math.CO
Abstract: A classical problem in lattice path enumeration counts paths that remain on one side of a boundary line. We study several classes of paths where this boundary is porous and show that they are related through a single half-turn rotation bijection. As a first application, we enumerate minimal bridges by relating them to excursions: for positive integers $k$ and $n$, the number of paths from $(0,0)$ to $(kn,n)$ with unit right and up steps that avoid all other lattice points on the line $y=x/k$ is $\frac{k}{kn+n-1}\binom{kn+n}{n}$. The same bijection yields a relation between the ordinary generating functions for binomial coefficients and $k$-Catalan numbers through a dual edge-forbidden model, extends to forbidden strips containing the diagonal, and handles a rational-slope case involving Duchon paths. Finally, our bijection also proves that the number of bridges from $(0,0)$ to $(2n,2n)$ that avoid even diagonal points is $C_{2n}+4C_{2n-1}$, with $C_n$ the $n$th Catalan number. This complements a result of Shapiro.
<<<END PAPER key=2608.11005>>>

<<<PAPER key=2608.11007>>>
Title: Degree Game for Special Regular Graphs
Authors: Lajos Győrffy
Primary arXiv category: math.CO
Abstract: For a given $d$-regular graph $G$, a Maker-Breaker degree game is played by two players who alternately claim previously unclaimed edges of $G$. In the standard variant, the goal of Maker is to maximize the maximum degree of their induced subgraph, while Breaker aims to minimize it, or equivalently, to guarantee a certain minimum degree in their own subgraph. A classic pairing strategy shows that Breaker can secure at least $\lfloor d/4 \rfloor$ edges at every vertex of any $d$-regular graph. Breaking this bound for general or even for specific classes of graphs has been a long-standing open problem in combinatorial game theory; indeed, J. Beck characterized this challenge in his monograph as the first among the seven most humiliating open problems of positional game theory. In this paper, we improve the $d/4$ bound for some infinite graph families, such as the hypercube graph $Q_d$, grids and tori. We first show that Breaker can secure a degree of one at every vertex in $Q_3$, then lift this to higher dimensions, where Breaker can guarantee a degree of at least $\lfloor d/3 \rfloor$.
<<<END PAPER key=2608.11007>>>

<<<PAPER key=2608.11009>>>
Title: Square root crystals and the square root of $B(\infty)$
Authors: Eric Marberg, Travis Scrimshaw
Primary arXiv category: math.RT
Abstract: We introduce a general monoidal category of $\mathbf{N}$-root crystals and then study the special case of square root $\mathfrak{gl}_n$-crystals. The latter objects include Yu's crystals on semistandard set-valued tableaux. Prior work of the first author, Tong, and Yu showed that regular square root $\mathfrak{gl}_n$-crystals can be a useful tool for proving Grothendieck positivity results. The objects studied here go beyond the regular case and allow us to construct a square root analog of the direct limit crystal $B(\infty)$. We give several descriptions of our square root of $B(\infty)$, using marginally large tableaux, the Lusztig or PBW parameterization, and the Nakashima--Zelevinsky polyhedral model. We show that this crystal has a simple character formula, exhibits a nontrivial Demazure filtration, and recovers Yu's semistandard set-valued tableau crystals after taking appropriate tensor products. We also investigate a number of differences between square root crystals and classical crystal constructions.
<<<END PAPER key=2608.11009>>>

<<<PAPER key=2608.11012>>>
Title: An interlacing pattern between the types $C_n$ and $D_n$ coordinator polynomials
Authors: Jun-Ying Liu, Shi-Mei Ma
Primary arXiv category: math.CO
Abstract: The study of coordinator polynomials of Weyl group lattices was initiated by Conway and Sloane. In 2013, by using a trigonometric substitution approach, Wang and Zhao proved the real-rootedness of the type $D$ coordinator polynomials. Subsequently, Xie and Zhang proved the compatibility between the types $C_n$ and $D_n$ coordinator polynomials. In this paper, we discover the interlacing pattern between the types $C_n$ and $D_n$ coordinator polynomials, which may be named as the second pattern of interlacing zeros.
<<<END PAPER key=2608.11012>>>

<<<PAPER key=2608.11035>>>
Title: Chooser-Picker Degree Games for Regular Graphs
Authors: Lajos Győrffy
Primary arXiv category: math.CO
Abstract: In the unbiased Chooser-Picker (also known as Client-Waiter) game played on the edge set of a graph, Picker offers a pair of unclaimed edges in each turn, Chooser claims one, and the remaining edge goes back to Picker. We study the Chooser-Picker (C-P) degree game played on $d$-regular graphs, where Chooser aims to maximize the maximum degree of their induced subgraph, and Picker's objective is to defend every vertex by securing a certain minimum degree in Picker's own subgraph. While classical static pairing strategies guarantee a minimum degree of at least $\lfloor d/4 \rfloor$ for Breaker on general $d$-regular graphs in Maker-Breaker (M-B) games and for Picker in C-P games, outperforming this threshold has been a major open challenge in both frameworks. According to the foundational monograph of J. Beck, this challenge stands as the first among the seven most humiliating problems in combinatorial game theory. Our main result is that Picker can beat the $d/4$ bound. First, we prove that Picker can always guarantee a degree of at least one at every vertex on any $3$-regular graph. Based upon this we introduce a direct strategy to prove that Picker can secure a degree of at least $\lfloor d/3 \rfloor$ at every vertex for any $d$-regular graph. This highlights a fundamental structural advantage that Picker usually possesses over Breaker in sparse local games.
<<<END PAPER key=2608.11035>>>

<<<PAPER key=2608.11038>>>
Title: A 5/4 bound for graphic $s$-$t$ path TSP on subcubic graphs
Authors: Junho Hwang
Primary arXiv category: cs.DS
Abstract: We study the graphic $s$-$t$ path TSP on subcubic graphs (maximum degree 3): given two vertices $s,t$, find a shortest walk from $s$ to $t$ that visits every vertex. Our main result is that the optimal $5/4$ coefficient is attained for every terminal pair -- including the difficult case where deleting both $s$ and $t$ disconnects the graph. Concretely, every pair of distinct vertices $s,t$ in a simple 2-connected subcubic graph $G$ admits a spanning $s$-$t$ walk of length at most $\lfloor(5n+n_2(G))/4\rfloor-1$, where $n=|V(G)|$ and $n_2(G)$ is the number of degree-2 vertices; the asymptotic coefficient $5/4$ cannot be improved, and a simple $O(n^2)$ algorithm finds a walk of length at most $\lfloor(5n+n_2(G))/4\rfloor$. An edge-rooted even-cover theorem of Wigal, Yoo, and Yu, combined with a short conversion lemma proved here, gives a bound of this form only when $s$ and $t$ are the two endpoints of a given edge; we remove that adjacency restriction. For cubic graphs ($n_2(G)=0$) the bound reads $\lfloor 5n/4\rfloor-1$, to our knowledge the first $5/4$ bound for cubic path TSP proved directly rather than through the general path-to-tour reduction.
<<<END PAPER key=2608.11038>>>

<<<PAPER key=2608.11056>>>
Title: Twisted Conjugacy and the Classification of Induced Centrosymmetric Alternant Codes
Authors: Ousmane Ndiaye, Massamba Sow
Primary arXiv category: cs.IT
Abstract: This paper presents a classification of induced centrosymmetric alternant codes through the study of the automorphism structures inherited from Generalized Reed--Solomon (GRS) codes. We introduce the twisted conjugation action naturally associated with projective semilinear transformations and establish its correspondence with ordinary conjugacy in the projective semilinear group. This correspondence enables the application of Shintani's theorem to classify the $γ_{p^j}$-similarity classes of involutions. As a consequence, we obtain necessary and sufficient conditions for an alternant code to admit a centrosymmetric structure induced by a projective semilinear automorphism. The resulting classification unifies the different families of induced centrosymmetric alternant codes within a common automorphism-based framework.
<<<END PAPER key=2608.11056>>>

<<<PAPER key=2608.11078>>>
Title: A Fourier-analytic Uniqueness Theorem for Lattice-point Enumerators
Authors: António Rocha-Neves
Primary arXiv category: math.CO
Abstract: We consider a bounded set $P \subset \mathbb{R}^d$ and the lattice-point enumerator $L_P(t) = |tP \cap \mathbb{Z}^d|$ for real $t > 0$. We show that if two bounded measurable sets with boundary of measure zero have the same real-parameter lattice-point enumerators for all integer translates, then their indicator functions agree almost everywhere. As a corollary, any convex body is uniquely determined by this data. Our proof is short and Fourier-analytic, where the key device is a periodic point-counting function whose Fourier coefficients recover the Fourier transform of the indicator function on a dense set. This recovers and extends, with a unified argument, the uniqueness results for rational polytopes and symmetric convex bodies established by Royer [arXiv:1712.01973, arXiv:1712.03937], whose proofs relied on intricate case-specific geometric constructions.
<<<END PAPER key=2608.11078>>>

<<<PAPER key=2608.11085>>>
Title: Bijections between pattern-avoiding derangements and desarrangements
Authors: Alyssa G. Henke, Derek H. Stephens, Yan Zhuang
Primary arXiv category: math.CO
Abstract: Derangements are permutations without fixed points, and are in bijection with desarrangements: permutations whose first non-descent is even, or equivalently, permutations without ``pixed points''. Bsila, Cox, Hugo, Styron, and Zhuang recently proved a theorem characterizing all $Π\subseteq\mathfrak{S}_{3}$, such that $1\leq\left|Π\right|\leq3$, for which the number of derangements avoiding all patterns in $Π$ is equal to the number of desarrangements avoiding all patterns in $Π$. They left finding a bijective proof of this theorem as an open problem, and posed a related conjecture concerning the distributions of fixed points and pixed points over pattern avoidance classes. In this paper, we give bijective proofs of this theorem and conjecture.
<<<END PAPER key=2608.11085>>>

<<<PAPER key=2608.11289>>>
Title: How Difficult Is It to Recognize CIS Graphs?
Authors: Rongchuan Tao, Mengxi Yang, Wenan Zang
Primary arXiv category: cs.DM
Abstract: A graph $G$ is called $CIS$ if each maximal clique intersects each maximal stable set of $G$, with maximality taken with respect to set inclusion. CIS graphs resemble perfect graphs in several respects and have interesting applications in game theory. The complexity of recognizing CIS graphs was posed as an open problem by Chvátal in the 1990s and has since led to conflicting conjectures. We settle the problem by showing that recognizing CIS graphs is $\mathsf{coNP}\text{-complete}$.
<<<END PAPER key=2608.11289>>>

<<<PAPER key=2608.11290>>>
Title: Solutions to Five Challenge Problems in Enumerative and Algorithmic Combinatorics, with an Account of the Human-Machine Methodology Employed
Authors: Jaideep Sai Padhi
Primary arXiv category: math.CO
Abstract: We report solutions to five challenge problems posed by Doron Zeilberger and his collaborators, together with substantial partial progress on two further problems, and we describe the method by which they were obtained. The solved problems are: the Second Computational Chomp Challenge of Ekhad and Zeilberger, for which we exhibit a bar with three winning opening moves; the third challenge of Spahn and Zeilberger, asking whether the restricted permutation counts a_{r,s} and b_{r,s} are holonomic for all r,s>1, answered affirmatively; the First Rigorous Solid Standard Young Tableaux Challenge, for which we prove the conjectured second-order recurrence; the five-dimensional Geode Challenge of Amdeberhan, Kauers and Zeilberger; and Conjectures 2a and 2b of Kauers and Zeilberger, which we obtain from a local limit theorem for excursions of Markov-modulated random walks in cones. Several results of independent interest arise along the way: a staircase theorem constraining the winning opening moves of any Chomp bar, together with a parity theorem for square bars; an explicit algebraic generating function for reverse-Kreweras diagonal walks and a closed form for their diagonal-endpoint counts; a one-dimensional integral representation for diagonal Geode coefficients; and the identity that each Kauers-Zeilberger constant is a universal factor times the square of the apex value of a discrete cone-harmonic function. All of the work reported here was carried out in collaboration with a large language model. The paper sets out the division of labour, records the verification protocol this mode of work required, and documents the failures, which we regard as an essential part of the report.
<<<END PAPER key=2608.11290>>>

<<<PAPER key=2608.11132>>>
Title: Kohayakawa's conjecture and clique coverings of complements of paths and cycles
Authors: Bo Ning
Primary arXiv category: math.CO
Abstract: For $s\ge1$, let $G_s$ be the bipartite graph between the $s$-subsets and the $(s-1)$-subsets of $[2s]$, where adjacency means disjointness, and let $w(s)$ be the maximum number of $s$-subsets on an induced path in $G_s$. We prove $w(s)\ge \frac{4^s}{2048s^{5/2}}$ for all $s\geq 6$. This implies $\sup_{s\ge1}w(s)^{1/s}=4$, as conjectured by Kohayakawa (1991). His recursive construction then gives induced paths of order $Ω(4^r/r^{5/2})$ in the Kneser graph $KG(2r+1,r)$ and yields \[ \max\{\cc(\overline{P_n}),\ \cc(\overline{C_n})\} \le \log_2 n+\frac52\log_2\log_2 n+O(1). \] Together with the known lower bounds, this settles a conjecture of de Caen, Gregory, and Pullman (1985) and gives \[ \cc(\overline{P_n})=\log_2 n+Θ(\log_2\log_2 n), \qquad \cc(\overline{C_n})=\log_2 n+Θ(\log_2\log_2 n). \] We also give an independent proof of the latter order estimates. It uses a Hamiltonicity result of Kneser graphs and a key lemma proved by the Lovász local lemma.
<<<END PAPER key=2608.11132>>>

<<<PAPER key=2608.11169>>>
Title: Released packing functions in graphs
Authors: Pablo Fekete, Erica Hinrichsen, Valeria Leoni, María Inés Lopez Pujato
Primary arXiv category: math.CO
Abstract: We introduce and start the study of a variant of packing functions in graphs. Given a graph $G$ with vertex set $V$ and nonnegative integer vectors $\mathbf{k}=(k_v)_{v\in V}$, $\boldsymbol\ell=(l_v)_{v\in V}$ and $\mathbf{u}=(u_v)_{v\in V}$, a function $f : V \rightarrow \mathbb{Z}_0^+$ is a Released $( \mathbf{k}, \boldsymbol\ell, \mathbf{u})$-packing function of $G$ if $l_v\leq f(v)\leq u_v$ for every $v\in V$ and the sum of the values of $f$ over the closed neighborhood of vertices $v$ with $f(v) = u_v$ is at most $k_v$. The weight of $f$ is the value $f(V) = \sum_{v\in V} f(v)$. We study the associated decision problem (RPP), which asks, given $G$, $\mathbf{k}$, $\boldsymbol\ell$, $\mathbf{u}$ and an integer number $x$, whether $G$ admits a Released $( \mathbf{k}, \boldsymbol\ell, \mathbf{u})$-packing function of weight at least $x$. We relate RPP to the $r$-dependent set problem, derive several NP-hardness results, model RPP as a compact (polynomial in size) Integer Linear Program, and take the first steps of a polyhedral study.
<<<END PAPER key=2608.11169>>>

<<<PAPER key=2608.11170>>>
Title: Eigenvalue growth of the discrete Hodge Laplacian across dimensions
Authors: Philipp Bartmann, Matthias Keller
Primary arXiv category: math.CO
Abstract: We prove several bounds on the largest and smallest eigenvalues of the combinatorial Hodge Laplacian $Δ^H_k$ of a finite simplicial complex $Σ.$ As a consequence, we obtain new vanishing criteria for cohomology groups $H^k(Σ,\mathbb{R)}$ and confirm a conjecture of O on the dimensional monotonicity of the largest eigenvalue.
<<<END PAPER key=2608.11170>>>

<<<PAPER key=2608.11183>>>
Title: A reformulation of the discrete Convexity Conjecture via $k$-thresholds
Authors: Ruben Ascoli, Xiaoyu He, Jinyoung Park, Michel Talagrand
Primary arXiv category: math.CO
Abstract: We introduce the notion of "$k$-thresholds'' and show that Talagrand's discrete convexity conjecture is equivalent to the assertion that, for some universal integer $k \ge 2$, the $k$-threshold of every increasing family is at most a universal constant times its expectation threshold. We prove a reduction theorem that bounds the $k$-threshold of any increasing graph property in terms of ordinary thresholds of graphs in suitable decompositions of its members. As a consequence, we determine, up to a constant factor, the $k$-threshold of every fixed graph in terms of a natural $k$-density parameter. We also prove that $k=2$ suffices for several classical spanning graph containment properties. More generally, we establish the conjectured comparison between $k$-thresholds and expectation thresholds for broad classes of graph containment properties whose target graphs have low degeneracy.
<<<END PAPER key=2608.11183>>>

<<<PAPER key=2608.12410>>>
Title: Finding all cospectral mates over a number field
Authors: Alexander Van Werde
Primary arXiv category: math.NT
Abstract: We investigate a notion of cospectrality for integer matrices that is parameterized by algebraic number fields. Given a number field and a symmetric integer matrix, we wonder when conjugating the integer matrix by an orthogonal matrix with entries in the given field can produce new integer matrices. Our results concern sufficient conditions for the associated notion of spectral determination, and we give constraints on the orthogonal matrices when the conditions are not applicable. The results use the discriminant of the characteristic polynomial and properties of Krylov subspaces. We leverage the theory to develop an algorithm to find all cospectral mates over a given (small) field. An implementation of the algorithm is made available.
<<<END PAPER key=2608.12410>>>
