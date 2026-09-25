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
<<<PAPER key=2608.12607>>>
Title: A Quantum Latin Square of Order Six with Cardinality 29
Authors: Aishwarya P. Das, Durgesh Kumar
Primary arXiv category: math.CO
Abstract: We construct an explicit real quantum Latin square of order six with cardinality $29$, the last unresolved value in the order-six spectrum. We first construct a punctured $6 \times 6$ array in $\mathbb{R}^5$ whose punctured rows and columns are orthonormal bases, and then adjoin a common diagonal vector in an orthogonal one-dimensional summand. The six diagonal entries lie on one ray. Of the thirty off-diagonal entries, two rays occur twice and the other twenty-six occur once; exact support and coordinate-ratio comparisons establish this count. Together with the known constructions, this closes the cardinality spectrum of quantum Latin squares of order $6$.
<<<END PAPER key=2608.12607>>>

<<<PAPER key=2608.12673>>>
Title: Weakened Gallai-Ramsey Numbers for Books
Authors: Mark Budden, Adam Gregory
Primary arXiv category: math.CO
Abstract: For $1\le s<t$ and any graph $G$, the weakened Gallai-Ramsey number $gr^t_s(G)$ is defined to be the least $p\in \mathbb{N}$ such that every Gallai $t$-coloring of the edges of $K_p$ (i.e., a $t$-coloring that lacks rainbow triangles) contains a subgraph isomorphic to $G$ whose edges use at most $s$ of the colors. In the case of a book graph $B_n:=K_2+nK_1$, Jakhar and Moun determined the values $gr^3_2(B_3)=6$ and $gr^3_2(B_4)=7$. In this paper, we extend their results to $t>3$ colors, and we determine the values of $gr^3_2(B_n)$ for $5\le n\le 15$. General lower bounds for $gr^t_2(B_n)$ are also given.
<<<END PAPER key=2608.12673>>>

<<<PAPER key=2608.12678>>>
Title: On the Gap of Finite Posets
Authors: Alireza Haqi
Primary arXiv category: math.CO
Abstract: Let $P$ be a finite nonempty poset with $n$ elements, let $f:P\to\{1,\ldots,n\}$ be a uniformly random order-preserving bijection, and put $h_P(x)=\mathbb E[f(x)]$. Define $\operatorname{gap}(P)$ as the largest difference between consecutive values in the ordered list consisting of $0$, $n+1$, and all the expected ranks $h_P(x)$. Write $w(P)$ for the largest size of a pairwise incomparable subset. We prove three results. The first proves an old conjectural relation between width and expected-rank gaps that has appeared repeatedly, in increasingly general forms, in work of Brightwell and Trotter (2002), Biró and Trotter (2011), and Aires and Kahn (2025): $\operatorname{gap}(P)\le 2w(P)-1$. Second, for every $L>0$ we construct a width-two poset such that every maximal chain has an expected-rank gap of at least $L$, where the two endpoint spacings are included when computing this gap. Finally, for every $r\in\mathbb N$, we construct a poset $P_r$ for which the relative order induced on every nonempty selected set $X$ has base-two entropy below $3|X|$, while $\operatorname{gap}(P_r)\ge(3/2)^r$. Thus the gap can be arbitrarily large while the induced order on every selected set has relatively small entropy. The key ideas behind all three results were found by ChatGPT 5.6 Sol.
<<<END PAPER key=2608.12678>>>

<<<PAPER key=2608.12723>>>
Title: Tree-partitions of graphs with bounded tree-depth
Authors: Rong Chen, Huayue Liu
Primary arXiv category: math.CO
Abstract: Wood~ recently showed that every graph $G$ of pathwidth $h$ and $Δ(G)\ge1$ admits a $T$-partition of width at most $4(h+1)^2Δ(G)$ for some tree $T$ with $pw(T)\leq2h+1$. In this paper, we establish an analogous result for tree-depth, which is a stronger parameter than pathwidth. We prove that every connected graph with tree-depth $h$ admits a $T$-partition of width at most $\mathrm{max}\{1, (4h-10)Δ(G)+1\}$ for some tree $T$ with $\operatorname{rad}(T)\leq h-1$.
<<<END PAPER key=2608.12723>>>

<<<PAPER key=2608.12731>>>
Title: The multiplicity sequence of monomial ideals
Authors: Sudipta Das, Jonathan Montaño, Aniketh Sivakumar
Primary arXiv category: math.AC
Abstract: We give a convex-geometric formula for the multiplicity sequence of a monomial ideal in terms of mixed volumes of polytopes constructed from its Newton polyhedron. We also construct a counterexample to a conjecture of Achilles and Manaresi proposing a different volume formula for the multiplicity sequence. Finally, we derive a mixed-volume formula for the mixed multiplicities of arbitrary monomial ideals.
<<<END PAPER key=2608.12731>>>

<<<PAPER key=2608.12758>>>
Title: Cyclic permutations of large subsets with polynomial values in multiplicative subgroups of finite fields
Authors: Hai-Liang Wu, He-Xia Ni
Primary arXiv category: math.NT
Abstract: Let $f(t)\in\mathbb{Z}[t]$ be a nonconstant polynomial with nonzero discriminant and let $k\ge2$ be an integer. For every sufficiently large prime $p\equiv1\pmod{k}$, by applying mixed exponential sums over finite fields, discrete Fourier analysis and the spectral graph theory, we establish a threshold $c(p,k,f)$ such that any subset $A\subseteq\mathbb F_p$ with $\#A\ge c(p,k,f)$ admits a permutation $a_1, a_2,\cdots, a_{\#A}$ of $A$ satisfying $f(a_i+a_{i+1})\in\{x^k: x\in\mathbb{F}_p^*\}$ for any $1\le i \le \#A$, where $a_{\#A+1}=a_1$. Also, we give lower and upper bounds for the least possible threshold.
<<<END PAPER key=2608.12758>>>

<<<PAPER key=2608.12782>>>
Title: Full homomorphisms to graph classes
Authors: Pavol Hell, César Hernández-Cruz
Primary arXiv category: math.CO
Abstract: Given a family of graphs $\mathcal{F}$, we define a graph $G$ to be fully $\mathcal{F}$-colourable if $G$ admits a full homomorphism to some $F$ in $\mathcal{F}$. We approach the problem of determining when a graph is fully $\mathcal{F}$-colourable in terms of minimal forbidden induced subgraphs. We provide general results which allow to obtain the exact families of forbidden induced subgraphs for full $\mathcal{F}$-colouring when $\mathcal{F}$ is among some well-known families, such as threshold, trivially perfect, split, chordal, interval and strongly chordal graphs, as well as forests. Traditionally, these questions have been studied for a single graph $H$, not a family. Motivated by our results on the family of forests, we contribute to this research by focusing on the case of a single centipede.
<<<END PAPER key=2608.12782>>>

<<<PAPER key=2608.12817>>>
Title: Necessary and sufficient conditions of a class of bipartite graphs with local antimagic chromatic number 2 - an algebraic approach
Authors: Gee-Choon Lau, Wai Chee Shiu
Primary arXiv category: math.CO
Abstract: For a connected graph $G = (V, E)$, a bijective edge labeling $f:E \to\{1,\ldots ,|E|\}$ is a local antimagic labeling of $G$ if it induces a vertex labeling $f^+$ such that for any pair of adjacent vertices $x$ and $y$, $f^+(x)\not= f^+(y)$, where the induced vertex label $f^+(x)= \sum f(xu)$, with $u$ ranging over all the vertices adjacent to $x$. The minimum number of distinct induced vertex labels over all local antimagic labelings of $G$ is the local antimagic chromatic number of $G$, denoted $χ_{la}(G)$. In this paper, we make use of algebraic analysis to obtain necessary and sufficient conditions for every bipartite graph with all vertices of degree 2 except exactly three vertices of degree at least 3 to have local antimagic chromatic number 2. Moreover, we showed that the consecutive edge labels of every induced path of each case is unique.
<<<END PAPER key=2608.12817>>>

<<<PAPER key=2608.12832>>>
Title: Bricks that every removable edge is solitary
Authors: Jinxin Xue, Jun Ge, Fuliang Lu, Yaxian Zhang
Primary arXiv category: math.CO
Abstract: A brick is a 3-connected graph $G$ such that $G-u-v$ has a perfect matching for any two distinct vertices $u,v\in V(G)$. An edge $e$ in a matching covered graph $G$ is removable if $G-e$ is matching covered. We say that a removable edge $e$ in a brick $G$ is $b$-invariant if $b(G-e)=b(G)=1$, where $b(H)$ denotes the number of bricks in the tight cut decomposition of a matching covered graph $H$. An edge of a graph is solitary if it lies in precisely one perfect matching. Lucchesi and Murty proposed the problem of characterizing bricks, distinct from $K_4$, $\overline{C_6}$ and the Petersen graph, in which every $b$-invariant edge is solitary. Note that every $b$-invariant edge is removable. In this paper, we strengthen the condition by requiring that every removable edge is solitary. We show that every nonsolid brick satisfying this strengthened condition can be obtained by repeatedly splicing odd wheels (up to multiple edges). Moreover, properties of such bricks imply that "repeatedly splicing odd wheels" cannot be replaced by "repeatedly splicing copies of $K_4$".
<<<END PAPER key=2608.12832>>>

<<<PAPER key=2608.12848>>>
Title: Characterizing forbidden induced subgraphs that force top vertices to be Gallai vertices
Authors: Yurui Tang
Primary arXiv category: math.CO
Abstract: A vertex of a graph is called a top vertex if it has maximum degree in the graph. A vertex of a graph is called a Gallai vertex if it belongs to every longest path of the graph. Golan and Shan proved that every top vertex of any connected induced-$2P_2$ free graph is a Gallai vertex. Long, Milans, and Munaro subsequently showed that if every connected induced-$H$ free graph has a Gallai vertex, then $H$ must be a linear forest of order at most nine. They also proved that, for every linear forest $H$ of order at most four, every top vertex of any connected induced-$H$ free graph is a Gallai vertex. In this paper, we determine the graphs $H$ for which every top vertex of any connected induced-$H$ free graph is a Gallai vertex. Our result shows that this holds precisely when $H$ is a linear forest of order at most four or $H=P_3+2P_1$.
<<<END PAPER key=2608.12848>>>

<<<PAPER key=2608.12910>>>
Title: Enumeration of measurable functions between finite measurable spaces
Authors: D. Kinoti Gikunda, J. Kiprop Tanui, Benard Kivunge
Primary arXiv category: math.CO
Abstract: Let \(X\) and \(Y\) be finite sets with \(|X|=n\), \(|Y|=m\), equipped with sigma algebras \(\mathcal A\) and \(\mathcal B\). For arbitrary sigma algebras \(\mathcal A\) on \(X\) and \(\mathcal B\) on \(Y\), we enumerate measurable functions \(f\colon X\to Y\). When \(\mathcal B\) is discrete, the number of pairs \((\mathcal A,f)\) is the Touchard polynomial \(T_n(m)=\sum_k S(n,k)m^k\). For general \(\mathcal B\) with atom sizes \(b_1,\dots,b_r\), the number of pairs \((\mathcal A,f)\) over all sigma algebras \(\mathcal A\) on \(X\) is the complete Bell polynomial \(N_{\mathcal B}(n)\) in the power sums \(p_a=\sum_j b_j^a\), with exponential generating function \(\exp(\sum_j(e^{b_jx}-1))\). This specialises to the Touchard polynomial in the discrete case and is maximised by the trivial codomain sigma algebra. We further show that \(N_{\mathcal B}(n)=\mathbb E[Z^n]\) for a compound Poisson random variable \(Z\), and we discuss basic asymptotic growth of \(N_{\mathcal B}(n)\).
<<<END PAPER key=2608.12910>>>

<<<PAPER key=2608.12919>>>
Title: Constructions of almost controllable graphs determined by their generalized spectra
Authors: Wei Wang, Manjin Shi, Fenjin Liu
Primary arXiv category: math.CO
Abstract: Identifying and constructing graphs that are determined by their generalized spectrum (DGS) is a significant and challenging problem in spectral graph theory. Recently, a simple criterion for almost controllable graphs to be DGS was proposed by Lin et al. (2026), utilizing the modified walk matrix. In this paper, we investigate the evolution of the modified walk matrix under disjoint union and join operations with a singleton vertex. We establish an exact algebraic identity for the determinant of the modified walk matrix of the resulting graph. Based on this identity and the DGS-criterion of Lin et al., we construct infinite families of almost controllable graphs that are DGS, extending the previous construction of Liu et al. (2019), which was restricted to controllable graphs.
<<<END PAPER key=2608.12919>>>

<<<PAPER key=2608.12948>>>
Title: A relaxation of the Bermond-Thomassen conjecture
Authors: Stéphane Bessy, Matthijs Muis, Jean-Sébastien Sereni, Raphael Steiner, Sebastian Wiederrecht
Primary arXiv category: math.CO
Abstract: The well-known Bermond-Thomassen conjecture states that every digraph of minimum out-degree at least $2k-1$ contains $k$ vertex-disjoint directed cycles. Despite being posed in 1981, this conjecture remains unresolved for all $k \ge 4$. We prove a relaxation of this conjecture: every digraph $D$ of minimum out-degree at least $2k-1$ contains $k$ vertex-disjoint cycles, each of which either is directed or can be made directed by reversing one of its arcs. This bound is sharp and answers a question raised by Cames van Batenburg during the online workshop "Entropy Compression and Related Methods" in $2021$.
<<<END PAPER key=2608.12948>>>

<<<PAPER key=2608.13002>>>
Title: Characterization of graphs $G$ where $G \in \mathrm{obs}^*(H)$ for some graph $H$
Authors: Zahra Rahimi, M. H. Shirdareh Haghighi, Asma Namazi
Primary arXiv category: math.CO
Abstract: A full-homomorphism from a graph $G$ to a graph $H$ is a function on vertex sets that preserves adjacency and non-adjacency of vertices. A graph $G$ is called a minimal $H$-obstruction if it has no full-homomorphism to $H$ but every proper vertex induced subgraph of $G$ does. Such graphs can have at most $|V(H)|+1$ vertices. The set of minimal $H$-obstructions on $|V(H)|+1$ vertices is denoted by $\mathrm{obs*}(H)$. In question 2 of the paper "Santiago Guzm{á}n-Pro, Full-homomorphisms to paths and cycles, Discrete Mathematics, 347(3):113800, 2024" it is asked if there is a characterization of those graphs $G$ that lie in $\mathrm{obs*}(H)$ for some graph $H$. In this paper, we give a complete answer to this question.
<<<END PAPER key=2608.13002>>>

<<<PAPER key=2608.13015>>>
Title: On the Restricted Edge-Cuts of Optimal 1-Planar Graphs
Authors: Licheng Zhang, Zhangdong Ouyang, Yuanqiu Huang, Guiping Wang
Primary arXiv category: math.CO
Abstract: The restricted edge-connectivity of a graph is the minimum size of an edge-cut whose removal leaves every component with at least two vertices. In 2024, Zhang et al. showed that the restricted edge-connectivity of any optimal $1$-planar graph belongs to $\{8,10,12\}$. In this paper, we exclude $8$ as a possible value, thereby proving that the restricted edge-connectivity is either $10$ or $12$, and both values are attainable. Furthermore, we show that the restricted edge-connectivity of a 6-connected optimal 1-planar graph equals $10$ if and only if the graph contains an edge whose two endvertices both have degree $6$. As a key ingredient, we characterize the structure of vertex-induced subgraphs on $n$ vertices with $4n-9$ edges in optimal 1-planar graphs, and use this characterization to establish a connection between restricted edge-cuts and vertex-cuts in optimal 1-planar graphs.
<<<END PAPER key=2608.13015>>>

<<<PAPER key=2608.13025>>>
Title: A counterexample to the Foregger-Sinkhorn tie-point conjecture
Authors: Yair Lavi
Primary arXiv category: math.CO
Abstract: The Foregger-Sinkhorn tie-point conjecture asserts that if a nearly decomposable doubly stochastic matrix minimizes the permanent on a face and the permanental cofactor at a prescribed zero is larger than its permanent, then that zero is a tie point. We give a counterexample in dimension eight.
<<<END PAPER key=2608.13025>>>

<<<PAPER key=2608.13071>>>
Title: The Erdos-Mullin Five-Edge Intersection Problem
Authors: Chengrui Fang, Jianfeng Hou
Primary arXiv category: math.CO
Abstract: For an $n$-vertex graph $G$ and a permutation $π$ of its vertex set, let $I_G(π)=|E(G)\cap E(πG)|$, and let $μ(G)=\min_π I_G(π)$. Let $f(n,k)$ be the minimum number of edges in an $n$-vertex graph $G$ satisfying $μ(G)\ge k$. Erdős recorded a construction of Mullin showing $f(n,5)\le 2n-2$ and asked whether equality holds for sufficiently large $n$. We prove that it does: $f(n,5)=2n-2$ for all sufficiently large $n$. Equivalently, every sufficiently large $n$-vertex graph with at most $2n-3$ edges admits a relabelling with at most four common edges. The proof combines a quantitative exclusion of almost-universal vertices, a finite high-degree core with low-degree buffer vertices, list packing, and a sparse permutation version of the Lovász local lemma.
<<<END PAPER key=2608.13071>>>

<<<PAPER key=2608.13074>>>
Title: One Empty Locker and Two Inspections: An Exact Optimal Team Strategy
Authors: Igor Kleiner, David Perry
Primary arXiv category: math.CO
Abstract: We study a cooperative search game with $N$ lockers, $N-1$ labelled objects, one empty locker, and $N-1$ players. Player $i$ seeks object $i$ and may inspect at most two lockers; the second inspection may depend on the content of the first. The players may coordinate beforehand but receive no information about the searches of other players after play begins. We prove that the maximum probability that every player finds the assigned object is $I_N/N!$, where $I_N$ is the number of involutions of $N$ elements. An optimal strategy represents the blank by the common fictitious symbol $N$ and follows pointers: player $i$ first opens locker $i$, then opens the locker whose number was observed. The upper bound holds for every deterministic or randomized adaptive strategy and follows from a deletion lemma and two recurrences. We give explicit examples, identify the three-door case with an isomorphic "Return of Monty Hall" game, and report a reproducible mixed-integer verification for $N=2,3,4,5$. The computation is independent of, and not needed for, the proof.
<<<END PAPER key=2608.13074>>>

<<<PAPER key=2608.13089>>>
Title: Infinite series of Deza graphs with strongly regular children
Authors: Mikhail P. Golubyatnikov
Primary arXiv category: math.CO
Abstract: A graph $Γ$ is called a Deza graph with parameters $(n, k, b, a)$ if it has exactly $n$ vertices, is $k$-regular, and for any two distinct vertices $u$ and $v$, the number of common neighbors of $u$ and $v$ is either $a$ or $b$. The graphs $Δ_1$ and $Δ_2$, which have the same vertex set as $Γ$, and in which two vertices are adjacent if they have $a$ or $b$ common neighbours, respectively, are called the children of the Deza graph. If, for a Deza graph $Γ$, both $Δ_1$ and $Δ_2$ are strongly regular graphs, then $Γ$ is called a strongly Deza graph. In this work, we present a construction of an infinite family of strongly Deza graphs, for which the children $Δ_1$ and $Δ_2$ are strongly regular graphs with the same parameters as the graphs $NO^{\varepsilon \perp}_n(5)$ and $\overline{NO^{\varepsilon \perp}_n(5)}$.
<<<END PAPER key=2608.13089>>>

<<<PAPER key=2608.13097>>>
Title: Graph-theoretic design of lasing networks for physical vision
Authors: Paul Obernolte, Jakub Dranczewski, Yixiu Yin, Tobias Farchy, Wai Kit Ng, Tobias Simonsen, Elias Großhauser, Alexis Arnaudon
Primary arXiv category: cond-mat.dis-nn
Abstract: Physical neural networks perform learning through the intrinsic nonlinear dynamics of matter. Optimising their design presents a considerable challenge: complex many-body physics can provide powerful computation, but are expensive to simulate and large experimental optimisation runs are impractical to fabricate. Hence, the high-dimensional space of possible network topologies cannot be effectively directly searched. Here, we show that this search can be efficiently performed in an abstract graph space that is vastly cheaper to explore. Using random lasing networks -- composed of interconnected nanoscale waveguides and hosting strongly coupled lasing modes -- as an exemplar physical vision system, we establish a quantitative three-layer link: simple graph-theoretic metrics predict the nonlinear lasing physics, which in turn predicts vision performance. After validating this relationship using physical simulations, we exploit it to drive an evolutionary algorithm using graph metrics, producing network topologies that outperform random designs at a fraction of the computational cost (3000$\times$ speed-up compared to physical simulation). On simulated image-classification tasks, graph-optimised networks substantially improve classification accuracy. As our framework operates on network topology rather than substrate-specific physics, we anticipate it can transfer to other network-based physical learning systems, providing an efficient route for the directed design and optimisation of complex, strongly-interacting physical neural networks.
<<<END PAPER key=2608.13097>>>

<<<PAPER key=2608.13130>>>
Title: A linear upper bound on the number of moves required for independent set reconfiguration with two sliding tokens
Authors: Nived J. M., Mathew C. Francis
Primary arXiv category: math.CO
Abstract: We consider the problem of shifting two tokens placed on nonadjacent vertices $u,v$ of a graph $G$ on $n$ vertices to two nonadjacent vertices $u',v'$ of $G$ using a sequence of token movements. In each step, a token is moved from the vertex it is on to a neighbour of that vertex, ensuring that the tokens remain on nonadjacent vertices after this move. We answer a question of Briański, Felsner, Hodor, and Micek [``Reconfiguring Independent Sets on Interval Graphs'', MFCS 2021] by showing that if the two tokens can be moved from their initial position to their final position, then it can be done using at most $4n$ moves.
<<<END PAPER key=2608.13130>>>

<<<PAPER key=2608.13162>>>
Title: A sharp asymptotic bound for odd cycles in planar graphs
Authors: Zhen Liu, Chuanshu Wu
Primary arXiv category: math.CO
Abstract: For graphs $G$ and $H$, let $\mathbf N(G,H)$ denote the number of unlabeled, not necessarily induced copies of $H$ in $G$, and let $\mathbf{N}_{\mathcal P}(n,H)$ be the maximum of $\mathbf N(G,H)$ over all $n$-vertex planar graphs $G$. We prove that, for every fixed integer $m\geq 3$, \[ \mathbf{N}_{\mathcal P}(n,C_{2m+1}) =2m\left(\frac{n}{m}\right)^m +O_m\!\left(n^{m-1/5}\right). \] Heath, Martin, and Wells reduced the determination of the leading term to a weighted optimization conjecture involving cycles and paths. We prove a stronger sharp cycle--path inequality for probability weights on the edges of a complete graph and characterize equality in their conjectured inequality. Together with their reduction lemma, this settles the conjecture and yields the formula above, including the stated error term. The cases $m\geq 5$ are new; combined with the known results for $C_3$ and $C_5$, this determines the leading term for every fixed odd cycle in planar graphs.
<<<END PAPER key=2608.13162>>>

<<<PAPER key=2608.13176>>>
Title: New Quantitative Bounds for the $(p,q)$-Theorem for Unions of Convex Sets
Authors: Chaya Keller, Shakhar Smorodinsky
Primary arXiv category: math.CO
Abstract: A set in $\mathbb{R}^d$ is $s$-convex if it is the union of at most $s$ convex sets. A family $F$ satisfies the $(p,q)$ property if among any $p$ sets in $F$, some $q$ intersect. Let $\mathrm{HD}_d^{(s)}(p,q)$ be the minimum number of points needed to pierce a finite family of $s$-convex sets that satisfies the $(p,q)$-property. Alon and Kalai (1995) proved that $\mathrm{HD}_d^{(s)}(p,q)$ exists for any $p \geq q \geq d+1$ and any $s \geq 1$, but the quantitative bounds they obtained are very loose. We present several improved upper and lower bounds, for a general $d$ and for $s$-intervals of the line (i.e., $\mathrm{HD}_1^{(s)}(p,q)$). In particular, we prove the following: (i) For every $d\ge2$, $s \geq 1$ and $δ>0$, if $p>q$ and $q\ge C_d\log(e sp)$, then $\mathrm{HD}_d^{(s)}(p,q) \le p-q+1 + O_{d,δ}((s \cdot \tfrac{p}{q} \cdot \log \tfrac{esp}{q})^{ρ_d+δ}),$ where $ρ_d<d$ is the exponent in the weak epsilon-net theorem of Rubin (2022). (ii) For $s \geq 1$, $p \geq q \geq 2$ and $q\ge C_0s\log(2s)\log(ep)$, $p-q+s \leq \mathrm{HD}_1^{(s)}(p,q) \leq p-q+2s+1$. This result provides the first near-tight estimate for $\mathrm{HD}_1^{(s)}(p,q)$ for $q>2$. (iii) For any fixed $s$, there are an integer $κ_s\in\{s,\ldots,2s\}$ and constants $C_s,p_s>0$ such that, whenever $p\ge p_s$ and $q\ge C_s\log(ep)$, $ \mathrm{HD}_1^{(s)}(p,q)\in\{p-q+κ_s,\;p-q+κ_s+1\}. $ Interestingly, this two-value concentration result holds, although the exact value of the threshold remains unknown. (iv) For any $s \geq 1$, $\mathrm{HD}_3^{(s)}(p,4) \geq sp^{2-o(1)}$. Already for families of convex sets, this significantly improves the best known lower bound on $\mathrm{HD}_d^{(1)}(p,d+1)$, for all $d \geq 3$.
<<<END PAPER key=2608.13176>>>

<<<PAPER key=2608.13192>>>
Title: Generalizations of the Christoffel-Darboux formula and congruences involving Apéry-like numbers
Authors: Zhi-Hong Sun
Primary arXiv category: math.NT
Abstract: In this paper, we first extend the Christoffel-Darboux formula for orthogonal polynomials to general three-term recurrence sequences, and then investigate the identities and congruences for $g_n(x)$ and $v_n(x)$ given by \begin{align*} &g_0(x)=1,\ g_1(x)=\frac{x+1}2,\ (n+1)^2g_{n+1}(x)=\Big(2n(n+1)+\frac{x+1}2\Big)g_n(x)-n^2g_{n-1}(x)\ (n\ge 1), \\&v_0(x)=1,\ v_1(x)=x,\ (n+1)^3v_{n+1}(x)=(2n+1)(n(n+1)+x)v_n(x)-n^3v_{n-1}(x)\ (n\ge 1).\end{align*}
<<<END PAPER key=2608.13192>>>

<<<PAPER key=2608.13199>>>
Title: Optimal local convergence criteria for integer and Gaussian integer continued fractions
Authors: Ian Short, Margaret Stanier, Matty van Son, Andrei Zabolotskii
Primary arXiv category: math.CO
Abstract: The objective of this work is to determine optimal local restrictions on the coefficients of integer and Gaussian integer continued fractions that imply convergence. We identify all minimal restrictions involving words of length two in the integer case, and we identify all reversible minimal restrictions of length two in the Gaussian integer case. In the integer setting, our classification is equivalent to a classification of minimal unavoidable words of length two in Conway--Coxeter quiddity sequences. We also construct a canonical set of restrictions of infinite cardinality that is strictly stronger than every finite set of restrictions.
<<<END PAPER key=2608.13199>>>
