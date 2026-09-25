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
<<<PAPER key=2608.15005>>>
Title: Spanning Structures in Multipartite Graph Traversals
Authors: Isabel McGuigan
Primary arXiv category: math.CO
Abstract: Let $G$ be an $r$-partite graph such that the edge density between any two parts is at least $α$. We consider the problem of determining how large $α$ must be in order to guarantee that $G$ has a Hamiltonian traversal (an $r$-cycle subgraph containing exactly one vertex from each part), and show that this critical density tends to $\frac 1 2$ as $r$ increases. This resolves a conjecture of Badakhshian, Falgas-Ravry, and Sharifzadeh. We also study the critical densities necessary to guarantee the existence of other spanning structures in traversals, particularly subgraph factors, and obtain asymptotically the critical densities for traversal $F$-factor subgraphs for several classes of graphs $F$. The proofs of our results involve the absorption method.
<<<END PAPER key=2608.15005>>>

<<<PAPER key=2608.15100>>>
Title: Lascoux series, parking functions and noncrossing partitions
Authors: Alice L. L. Gao, Xin-Bei Liu, Arthur L. B. Yang, James J. Y. Zhao
Primary arXiv category: math.CO
Abstract: In the study of the generating series of Demazure characters, Lascoux used isobaric divided differences to define a family of polynomials $\mathcal{E}_σ(t)$ indexed by permutations $σ$, and asked for a satisfactory expression of these polynomials. In this paper we obtain a combinatorial interpretation of $\mathcal{E}_σ(t)$ for the permutation $σ=[2,3,\ldots,n,1]$ or its inverse in terms of the descent statistic of parking functions of length $n-1$. Based on this progress on Lascoux's open problem, we find that the polynomial $\mathcal{E}_σ(t)$ for this special case coincides with the $h$-polynomial $h(Δ(\mathrm{NC}_W),t)$ of the order complex of the noncrossing partition lattice associated to the irreducible Coxeter group $W$ of type $A_{n-1}$. We are inspired by this coincidence to give an operator approach to $h(Δ(\mathrm{NC}_W),t)$ for any finite Coxeter group $W$. As an application, we completely solve an open problem on $h(Δ(\mathrm{NC}_W),t)$ which was proposed by Athanasiadis, Douvropoulos and Kalampogia-Evangelinou. For any $k$-divisible noncrossing partition poset $\mathrm{NC}^{(k)}_W$, we also obtain the interlacing symmetric decomposition property of the $h$-polynomial $h(Δ(\mathrm{NC}^{(k)}_W),t)$.
<<<END PAPER key=2608.15100>>>

<<<PAPER key=2608.15219>>>
Title: Algebraic geometric framework of Rogers--Ramanujan identities
Authors: Yifeng Huang, Kenny Lau, Ken Ono, Peter Paule
Primary arXiv category: math.NT
Abstract: The Rogers--Ramanujan identities equate a $q$-series whose exponents are governed by a quadratic form with an infinite product supported on two residue classes modulo~$5$. Identities of this shape are scarce, and a central problem is to identify the structures that produce them in families. Huang, Jiang, and Oblomkov have proposed a source of a new kind: to each pair of coprime integers $a,b>1$ they attach an infinite-rank $q$-series $Z_{a,b}(q)$, assembled from counts of commuting nilpotent matrix pairs $(A,B)$ with $A^a=B^b$ over finite fields, and they conjecture that it equals an explicit product of $(a-1)(b-1)/2$ modular units of level $a+b$. The $a=2$ cases are the Andrews--Gordon identities; no case with $a>2$ was known. We prove the conjecture for $(a,b)=(3,4)$, $(3,5)$, $(3,7)$, and $(3,8)$. Our proofs pass through a finer sum-to-sum identity, which we conjecture for all $b$ coprime to $3$ and establish for all $b$ when $q=1$. Lau and Ono have since proved that identity in general, and with it the full $a=3$ case. These identities have been formalized and verified in Lean by AxiomProver.
<<<END PAPER key=2608.15219>>>

<<<PAPER key=2608.15226>>>
Title: On the damage number of graphs
Authors: Valentin Gledel, William B. Kinnersley, Balázs Patkós, Milo\vs Stojaković
Primary arXiv category: math.CO
Abstract: We study a variant of Cops and Robbers in which the robber attempts to visit as many vertices of the graph as possible without being captured, while the cop aims to keep the robber confined to a small set of vertices. The \textit{damage number} of a graph $G$, introduced by Cox and Sanaei in 2019, is the maximum number of vertices the robber can visit in a game of Cops and Robbers on $G$. In this paper, we determine damage numbers for several classes of graphs, including hypercubes, Hamming graphs, Johnson graphs, incidence graphs of projective planes, and Erdős-Rényi random graph $G(n,p)$, for $p \gg \log^{2/5}(n) / n^{1/5}$. We also show that the problem of determining the damage number of a graph is {\sf PSPACE}-complete.
<<<END PAPER key=2608.15226>>>

<<<PAPER key=2608.15257>>>
Title: A Proof of the Chen--Raspaud Conjecture
Authors: Qi Wu, Yong Lu
Primary arXiv category: math.CO
Abstract: For every integer $k\ge2$, Chen and Raspaud conjectured that each graph $G$ with odd girth $\og(G)\ge2k+1$ and maximum average degree $\mad(G)<2+1/k$ has a $(2k+1:k)$-coloring. In this paper, we prove the conjecture.
<<<END PAPER key=2608.15257>>>

<<<PAPER key=2608.15281>>>
Title: A Ten-Vertex Counterexample to a Conjecture on Unstable Graphs
Authors: Prateek R. Srivastava
Primary arXiv category: math.CO
Abstract: Mizzi conjectured that every nontrivially unstable graph contains cycles C_k and C_{2k} for some odd k. We give a connected, nonbipartite, vertex-determining counterexample on ten vertices. Its instability is certified by an explicit nontrivial two-fold automorphism, and its complete set of simple-cycle lengths is {5,5,6}.
<<<END PAPER key=2608.15281>>>

<<<PAPER key=2608.15287>>>
Title: Hamiltonian paths in the permutation digraphs $P(n,n-2)$
Authors: Jiaxin Guo, Ming Duan, Jie Xue
Primary arXiv category: math.CO
Abstract: For $1\leq k<n$, let $P(n,k)$ be the directed overlap graph whose vertices are the $k$-permutations of $[n]$ and whose arcs are the $(k+1)$-permutations. Isaak proved that $P(n,n-2)$ has no directed Hamiltonian cycle for $n\geq4$ and asked whether it nevertheless has a directed Hamiltonian path. We answer this question affirmatively by showing that $P(n,n-2)$ has a Hamiltonian path.
<<<END PAPER key=2608.15287>>>

<<<PAPER key=2608.15302>>>
Title: Odd minors or odd immersions in graphs with independence number two
Authors: Antonia Bermúdez, Bruno L. Netto, Daniel A. Quiroz
Primary arXiv category: math.CO
Abstract: Kühn, Sauermann, Steiner and Wigderson recently disproved the Odd Hadwiger Conjecture, even for graphs with independence number 2. For this class of graphs the conjecture is known to be equivalent to the following: every $n$-vertex graph $G$ with independence number 2 contains $K_{\lceil \frac n2 \rceil}$ as an odd minor. While this does not hold, we prove that every graph $G$ with independence number 2 contains $K_{\lceil \frac n2 \rceil}$ as an odd minor or as a totally odd immersion.
<<<END PAPER key=2608.15302>>>

<<<PAPER key=2608.15358>>>
Title: Stability of Shifted Complexes via the Second-Moment Defect of the Up-Laplacian
Authors: Vinayak Gupta
Primary arXiv category: math.CO
Abstract: Let $K$ be a finite pure $k$-dimensional simplicial complex, with $k\ge1$, on the vertex set $[n]$ and with facet family $K_k$. Let $λ_1(K)\geλ_2(K)\ge\cdots>0$ be the nonzero eigenvalues of its $(k-1)$-dimensional up-Laplacian, and, after ordering the vertices so that $°_K(1)\ge\cdots\ge°_K(n)$, let $\dvT{r}(K)$ be the number of vertices contained in at least $r$ facets. A complex is \emph{shifted} if replacing a vertex of a face by a smaller vertex outside the face always yields another face. We prove that there is a shifted family $\HH$ of $(k+1)$-element subsets of $[n]$, with the same number of members as $K_k$, such that \[ \tfrac12\bigl|K_k\,\triangle\,\HH\bigr| \;\le\; \tfrac12\left[\sum_{r\ge1}\bigl(\dvT{r}(K)\bigr)^{2}-\sum_{r}λ_r(K)^{2}\right]. \] The left-hand side counts the facets that have to be exchanged to reach $\HH$; thus one half of the gap between the second power sums of the two sequences bounds the distance of $K_k$ to a shifted family. The characterization $λ(K)=\dv(K)^{\mathsf T}\iff K$ is isomorphic to a shifted complex was established in \cite{Gupta} from the identity that this gap equals twice the number of failed elementary shifts. The present paper converts that identity into a quantitative stability statement and recovers the equality characterization at zero defect. For $k=1$ this bounds the number of edge exchanges needed to reach a threshold graph with the same number of edges.
<<<END PAPER key=2608.15358>>>

<<<PAPER key=2608.15398>>>
Title: On the Laplacian spectral gap of generalized pancake graphs
Authors: Saúl A. Blanco
Primary arXiv category: math.CO
Abstract: The generalized pancake graph $P(m,n)$ is the Cayley graph of the group of colored permutations $\mathbb{Z}_m\wr S_n=(\mathbb{Z}_m)^n\rtimes S_n$ generated by generalized prefix reversals. In this paper, we establish that, for all $m,n\geq2$, the spectral gap $γ(P(m,n))$ of the normalized Laplacian satisfies $α_m/n\leqγ(P(m,n))\leq1/n$, where $α_m$ is a positive constant that depends only on $m$. As a consequence, for every fixed $m\geq2$, $γ(P(m,n))$ is $Θ_m(1/n)$ as $n\to\infty$. The proof combines Cesi's semi-recursive spectral-gap inequality with a Fourier decomposition of the appropriate operators associated with a coset Schreier graph of color-position pairs. For fixed $n\geq2$, we also establish that $γ(P(m,n))$ is $Θ_n(m^{-2})$ as $m\to\infty$. This disproves a conjecture of Blanco and Buehrle asserting that, for fixed $n$, the corresponding undirected generalized pancake graphs form an expander family.
<<<END PAPER key=2608.15398>>>

<<<PAPER key=2608.15422>>>
Title: Borel graphs generated by commuting functions
Authors: Su Gao, Xiangxi Hu, Jie Zou
Primary arXiv category: math.LO
Abstract: In this paper we study Borel graphs generated by finitely many commuting Borel functions. We give a geometric analysis of the free part of such graphs based on marker sets and marker regions. Assuming the existence of $r$-forward-independent hitting sets with bounded syndeticity, we obtain marker decompositions of the free part into rootless and rooted regions with controlled geometry. As applications, we derive finite Borel asymptotic dimension and hyperfiniteness, and obtain upper bounds for Borel edge chromatic numbers which improve previously known results. For the case in which each of the commuting Borel functions is bounded-to-one, we verify the existence of $r$-forward-independent hitting sets with syndeticity $Cr$ for some constant $C$. This gives another proof of a recent theorem of Naryshkin-Shinko-Weilacher-Yu, and is used to show that if one of the commuting Borel functions is injective and another one is bounded-to-one and exactly even-to-one, then the graph has a Borel perfect matching.
<<<END PAPER key=2608.15422>>>

<<<PAPER key=2608.15458>>>
Title: Five-Term and Higher Congruences Involving Arbitrary Sets and Short Intervals Modulo a Prime
Authors: Yao Zhi
Primary arXiv category: math.CO
Abstract: We obtain asymptotic formulas for additive congruences \[ \sum_{i=1}^r m_i x_i^{-s}\equiv λ\pmod p, \] where the \(m_i\) range over arbitrary subsets of \(\mathbb F_p^\ast\) and the \(x_i\) over shifted intervals. For five terms, in the balanced case of common cardinality \(N\), the asymptotic holds uniformly in \(λ\) whenever \[ N>p^{14/29+\varepsilon}, \] giving a genuine sub-square-root range. The main input is a centered fourth-moment estimate for the associated double exponential sums. The same method yields sub-square-root thresholds for every fixed \(r\ge 5\), including \(N>p^{8/17+\varepsilon}\) for six terms, with \[ α_r=\frac13+\frac{4}{9\sqrt r}+O(r^{-1}) \] as \(r\to\infty\).
<<<END PAPER key=2608.15458>>>

<<<PAPER key=2608.15513>>>
Title: Extremal graphs for disjoint union of stars and paths
Authors: Wenqian Zhang
Primary arXiv category: math.CO
Abstract: Let $F$ be a graph. A graph $G$ is called $F$-free if $G$ does not contain $F$ as a subgraph. Let ${\rm EX}(n,F)$ denote the set of $F$-free graphs of order $n$ with the maximum edges. In this paper, we characterize the graphs in ${\rm EX}(n,F)$ for large $n$, where $F$ is the disjoint union of paths and stars. This generalizes a result in \cite{LLP}.
<<<END PAPER key=2608.15513>>>

<<<PAPER key=2608.15521>>>
Title: On two conjectures concerning special kinds of descents on permutations
Authors: Taifeng Ding, Sherry H. F. Yan
Primary arXiv category: math.CO
Abstract: In this paper, we prove the continued fraction conjecture posed by Han, Mao and Zeng for the generating function of permutations with respect to the number of descents of type $2$ and the number of cycles, thereby settling their reformulation of a conjecture originally due to Baril and Kirgizov. We further establish the symmetry of the bistatistic $(\des_2, \ear)$ over $\mathfrak{S}_n$ as conjectured by Han, Mao and Zeng and strengthen this result by exhibiting five equidistributed companions for $(\des_2, \ear)$. Here the statistic $\des_2$ denotes the number of descents of type $2$, and the statistic $\ear$ denotes the number of exclusive antirecord cycle peaks originally introduced by Sokal and Zeng.
<<<END PAPER key=2608.15521>>>

<<<PAPER key=2608.15525>>>
Title: New lower bounds on domination--packing ratios in connected subcubic and cubic graphs
Authors: JiSun Huh, Juho Kim
Primary arXiv category: math.CO
Abstract: For a graph \(G\), let \(γ(G)\) and \(ρ(G)\) denote its domination number and packing number, respectively. Let \(c_{\mathrm{sub}}\) and \(c_{\mathrm{cub}}\) denote the respective limsups of \(γ(G)/ρ(G)\) over connected subcubic and connected cubic graphs as \(ρ(G)\to\infty\). We prove \[ c_{\mathrm{sub}}\geq\frac{13}{6}, \qquad c_{\mathrm{cub}}\geq\frac{17}{8}, \] by constructing two explicit binary branching families. The connected noncubic subcubic graphs \(\widehat B_t^\star\) satisfy \[ |V(\widehat B_t^\star)|=76\cdot2^t-12,\qquad γ(\widehat B_t^\star)=26\cdot2^t-4,\qquad ρ(\widehat B_t^\star)=12\cdot2^t-2, \] whereas the connected cubic graphs \(\widehat B_t^\bullet\) satisfy \[ |V(\widehat B_t^\bullet)|=108\cdot2^t-14,\qquad γ(\widehat B_t^\bullet)=34\cdot2^t-4,\qquad ρ(\widehat B_t^\bullet)=16\cdot2^t-2. \] The constructions use the same binary connector composition and closing lemma, with different connectors and initial assemblies. As a consequence, both families give unbounded additive violations of \(γ(G)\leq2ρ(G)+1\), disproving the proposed inequality even for connected cubic graphs.
<<<END PAPER key=2608.15525>>>

<<<PAPER key=2608.15558>>>
Title: A Counterexample to the Tang Zhang Schatten Norm Conjecture and Sharp Positive Results
Authors: Zijian Zeng, Houde Liu, Kurunathan Ratnavelu
Primary arXiv category: math.CO
Abstract: For $m\geq 2$, let $c_p(m)$ be the all-dimensional best constant in $$ \left\|\sum_{k=1}^m A_k\right\|_p \leq c_p(m)\left\|\sum_{k=1}^m |A_k|\right\|_p. $$ Tang and Zhang conjectured an explicit formula for every finite $p>1$. We disprove the conjecture with two explicit real $2\times 2$ rank-one matrices at $p=3/2$. The comparison is certified by seven strict rational inequalities and, in particular, places the attained ratio above $207/200$, while the conjectured constant lies below $207/200$. On the positive side, we prove the conjectured sharp bound for every family of rank-at-most-one summands when $2\leq p<\infty$, and classify all equality cases. We also prove the corresponding endpoint statement for $p=\infty$. Finally, for arbitrary complex matrices, we establish the conjectured sharp constant in the case $m=2$, $p=4$.
<<<END PAPER key=2608.15558>>>

<<<PAPER key=2608.15561>>>
Title: Sharp asymptotics for triangle independence and covering numbers
Authors: Zhen Liu, Qinghou Zeng
Primary arXiv category: math.CO
Abstract: For a graph $G$, let $α_1(G)$ be the maximum size of an edge set containing at most one edge from every triangle, and let $τ_1(G)$ be the minimum size of an edge set meeting every triangle. Erdős, Gallai, and Tuza proved that $α_1(G)+τ_1(G)=Ω(m^{2/3})$ for every $m$-edge graph and asked for the optimal asymptotic constant. We prove $$\lim_{m\to\infty} \min_{G,\,|E(G)|=m} \frac{α_1(G) + τ_1(G)}{m^{2/3}} = \frac{3}{2},$$ thereby establishing that the sharp constant is $3/2$ and solving the problem.
<<<END PAPER key=2608.15561>>>

<<<PAPER key=2608.15568>>>
Title: The equality between the Erdős-Ginzburg-Ziv constant and the short product-one constant for finite nonabelian groups
Authors: Yongke Qu, Guoqing Wang, Yuanlin Li
Primary arXiv category: math.CO
Abstract: Let $G$ be a finite group, and let $\exp(G)$ denote its exponent. The Erdős-Ginzburg-Ziv constant $s(G)$ is the least integer forcing a product-one subsequence of length $\exp(G)$, while the short product-one constant $η(G)$ is the least integer forcing a nonempty product-one subsequence of length at most $\exp(G)$. The natural nonabelian extension of a conjecture [W. Gao, \emph{On zero-sum subsequences of restricted size II}, Discrete Math. 2003] on the Erdős-Ginzburg-Ziv constant in finite abelian groups predicts that $s(G)=η(G)+\exp(G)-1.$ We confirm this equality for every finite nonabelian group $G$ having a cyclic subgroup of index $p$, where $p$ is the smallest prime divisor of $|G|$. As further consequences, we determine all generalized Erdős-Ginzburg-Ziv constants $s_{m\exp(G)}(G)$ for this family of groups.
<<<END PAPER key=2608.15568>>>

<<<PAPER key=2608.15627>>>
Title: Dual Weight and Monodromy of Dual Affine RS Correspondence
Authors: Yifeng Zhang
Primary arXiv category: math.CO
Abstract: The dual affine Robinson--Schensted correspondence and the affine matrix-ball construction give two related parametrizations of extended affine permutations. From the stable-window data of the dual correspondence, we introduce a dual weight \(β\) and prove that it is consistent with the original pair \((λ,N_0)\). We prove that \(β\) and the AMBC weight \(ρ\) have identical monodromy along affine Knuth paths. We further give an explicit relation between \(β\) and \(ρ\), showing that their difference depends only on the associated tabloids.
<<<END PAPER key=2608.15627>>>

<<<PAPER key=2608.15629>>>
Title: A proof of Bickle's conjecture on collapsible graphs
Authors: Xingzhi Zhan
Primary arXiv category: math.CO
Abstract: A graph $G$ is said to be $k$-collapsible if $G$ has minimum degree $k$ and every non-null proper induced subgraph of $G$ has minimum degree less than $k.$ In 2018, Bickle conjectured that the minimum number of vertices of degree $k$ in a $k$-collapsible graph of order $n$ with $k\ge 3$ is ${\rm max}\{\lceil 2n/(2k-1)\rceil,\, k^2-k-2-(k-3)n\}.$ We prove this conjecture.
<<<END PAPER key=2608.15629>>>

<<<PAPER key=2608.15670>>>
Title: Repetition Avoidance in Curling-Number Transforms
Authors: Geoffrey Caveney,  Haoxuan,  Dong, Jeffrey Shallit
Primary arXiv category: math.CO
Abstract: We study repetition avoidance in a word ${\bf w}$ and its curling-number transform $C({\bf w})$. For alphabets of sizes $2$, $3$, and $4$, we use Thue-Morse-based morphic constructions and exhaustive finite searches. A ternary word for which both ${\bf w}$ and $C({\bf w})$ are overlap-free has length at most $84$, whereas over four letters an infinite example exists. Hence $4$ is the smallest alphabet size admitting simultaneous infinite overlap-freeness. The infinite constructions are verified in Walnut; the finite maxima are obtained by exhaustive breadth-first search and checked independently.
<<<END PAPER key=2608.15670>>>

<<<PAPER key=2608.15672>>>
Title: Uniformity without Projective Consistency: An Exact Counterexample for a Nested Binary Term Grammar
Authors: Ivan Khalamendyk
Primary arXiv category: math.CO
Abstract: Let T_0={L} and T_{r+1}={L} union {N(a,b):a,b in T_r}. On the nonleaf terms E_r, require each event N(a,b) to occur after its nonleaf children, and let mu_r be the uniform measure on the linear extensions of this poset. We study the restriction rho_43 that deletes the new level-4 events while preserving the relative order of the level-3 events. We prove that the pushforward of mu_4 under rho_43 is not mu_3. Two explicit orders on the 25 level-3 events have different numbers of level-4 extensions. If b_i is the number of T_2 terms, including the leaf, seen in a prefix of length i, the number of newly released events is (i+1)^2-b_i^2. The release profile of a depth-priority order dominates that of a level order pointwise and is strictly larger for 3<=i<=15. An explicit injection between admissible interleavings therefore gives a strict analytic fiber inequality. Two algorithmically independent exact computations reproduce both 1557-digit fiber counts; their reduced ratio is 614690215260160000/479048686862260621, approximately 1.2831476885707443. The analogous restrictions through level 3 are consistent, so 4-to-3 is the first failure in this grammar. The result is specific to this grammar, uniform measures, and restriction map.
<<<END PAPER key=2608.15672>>>

<<<PAPER key=2608.15682>>>
Title: Variations of colored multiset Eulerian polynomials and applications
Authors: Xue Yan
Primary arXiv category: math.CO
Abstract: Deligeorgaki, Han and Solus introduced colored multiset Eulerian polynomials, derived a generating function identity which generalizes MacMahon's identity, proved their self-interlacing under suitable parameter conditions, and identified these polynomials as the h^*-polynomials of direct products of dilated lattice simplices. In this paper, we introduce an ascent analogue of the colored multiset Eulerian polynomial, derive an explicit generating function identity for this polynomial, show that it is equal to the h^*-polynomial of a family of half-open lattice polytopes, and verify that this ascent polynomial also satisfies self-interlacing under the same parameter conditions. By establishing recurrence relations, we prove that both polynomials are real-rooted for all positive integer parameters. The obtained identities are further applied to interpret combinatorially the h^*-polynomials of Pitman--Stanley polytopes, composition polytopes and a family of reflexive lattice polytopes defined from preorders.
<<<END PAPER key=2608.15682>>>

<<<PAPER key=2608.15701>>>
Title: Arboricity Nearly Bounds Degeneracy
Authors: Michał Lasoń, Bartłomiej Bosek, Grzegorz Gutowski, Jakub Przybyło
Primary arXiv category: math.CO
Abstract: Arboricity and degeneracy are two fundamental and closely related graph parameters that measure the sparsity of a graph. Every $k$-degenerate graph is $k$-arboric, but some $k$-arboric graphs are only $(2k-1)$-degenerate. However, every maximal $k$-arboric multigraph with $n$ vertices and every maximal $k$-degenerate multigraph with $n$ vertices has exactly $k(n-1)$ edges. These basic observations lead to a natural structural question: How far are $k$-arboric graphs from being $k$-degenerate? We answer this question by showing that: By at most a $(k-1)$-bounded-degree graph apart. More specifically, we prove that a $k$-arboric multigraph admits a $(k,k-1)$-decomposition, that is, its edges can be partitioned into two multisets such that one spans a $k$-degenerate multigraph and the other spans a multigraph with every vertex having degree at most $k-1$. Moreover, we provide a complete characterisation of all possible such decomposition types. Namely, for any integers $k \ge 1$ and $d,h \ge 0$ we show that every $k$-arboric multigraph admits a $(d,h)$-decomposition if and only if $d\geq k$ and $d+h\geq 2k-1$. Our proofs are constructive and we present a polynomial time algorithm that produces such decompositions. By contrast, we show that related decision problems for general graphs (without constraints on the arboricity) are NP-complete.
<<<END PAPER key=2608.15701>>>

<<<PAPER key=2608.15724>>>
Title: A method to identify the ordinary edges for symmetric traveling salesman problem based on frequency $K_i$s
Authors: Yong Wang
Primary arXiv category: math.CO
Abstract: The frequency $K_i$s ($i\in[4,n]$) are studied for symmetric traveling salesman problem ($TSP$) to characterize the structure properties of the edges inside and outside the optimal Hamiltonian cycle ($OHC$). Given a $K_i$ in $K_n$ where $i\in [4,n]$, the frequency $K_i$ is computed with the set of ${{i}\choose{2}}$ optimal $i$-vertex paths with fixed endpoints (optimal $i$-vertex paths) in the $K_i$. Given an $OHC$ edge in a $K_i$, it has a frequency bigger than $\frac{1}{2}{{i}\choose{2}}$ in the frequency $K_i$, and that of an ordinary edge outside the $OHC$ is smaller than $\frac{1}{2}{{i}\choose{2}}$. As the frequency of an edge is computed with the frequency $K_i$s, an $OHC$ edge of $K_n$ has an average frequency bigger than $\frac{1}{2}{{i}\choose{2}}$. It indicates an $OHC$ edge of $K_n$ is also one $OHC$ edge of a $K_i$ containing it. It also found that the probability that an $OHC$ edge has the frequency bigger than $\frac{1}{2}{{i}\choose{2}}$ increases according to $i\in [4, n]$ based on the frequency $K_i$s. For an ordinary edge outside the $OHC$, the probability that it has a frequency smaller than $\frac{1}{2}{{i}\choose{2}}$ increases according to $i$. Based on the findings, a method is given to identify the ordinary edges for $TSP$.
<<<END PAPER key=2608.15724>>>
