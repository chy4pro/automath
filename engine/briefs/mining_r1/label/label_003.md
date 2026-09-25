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
<<<PAPER key=2608.12430>>>
Title: Metropolis-Hastings Sampling of Phylogenetic Networks: Correcting for Symmetries
Authors: Leo van Iersel, Remie Janssen, Mark Jones, Yukihiro Murakami, Christopher Reichling
Primary arXiv category: cs.DM
Abstract: In phylogenetics, Metropolis-Hastings methods are commonly used to sample phylogenetic trees or networks, for example from Bayesian posteriors. These methods generally use transitions that distinguish all nodes involved, and thus require fully labelled representations of phylogenetic networks. We argue that sampling leaf-labelled phylogenetic networks demands a correction for the number of fully labelled representatives of a leaf-labelled network, or, equivalently, for its internal symmetry. Without correction, there is a danger of undersampling networks with internal symmetries. We show that this correction can be realized by a quotient construction on the Metropolis-Hastings Markov chain, which, in practice, requires the calculation of the size of the network's automorphism group. Using $μ$-vectors, we show that the automorphism group is trivial for orchard networks, and thus also for tree-child networks and trees. This implies that a correction for symmetry is not needed when sampling only from such network classes. More generally, using our Python implementation of the algorithms in this paper, we show that using $μ$-vectors can significantly speed up calculations of automorphism group sizes and thus of Metropolis-Hastings sampling of leaf-labelled networks.
<<<END PAPER key=2608.12430>>>

<<<PAPER key=2608.11990>>>
Title: On spanning trees whose degrees are congruent to one modulo $\ell$
Authors: Zhidan Yan, Wei Wang
Primary arXiv category: math.CO
Abstract: An $\ell$-congruent spanning tree of a nontrivial connected graph is a spanning tree in which every vertex has degree congruent to one modulo $\ell$. This notion provides a common generalization of classical spanning trees and odd spanning trees. We show, via a constructive greedy algorithm, that every $n$-vertex graph $G$ satisfying $n\equiv2\pmod{\ell}$ and $δ(G)>\frac{(\ell-1)n}{\ell}$ has an $\ell$-congruent spanning tree. For the special case of odd spanning trees ($\ell=2$), our algorithmic approach simplifies the original proof by Zheng and Wu. We also derive formulas for the numbers of $\ell$-congruent spanning trees in complete graphs and complete bipartite graphs. These formulas specialize to the classical spanning-tree formulas when $\ell=1$ and to the corresponding odd-spanning-tree formulas when $\ell=2$.
<<<END PAPER key=2608.11990>>>

<<<PAPER key=2608.11992>>>
Title: Perfect State Transfer on Oriented Circulant Graphs: A Complete Classification
Authors: Xingkun Song
Primary arXiv category: quant-ph
Abstract: The continuous-time quantum walk on an oriented circulant graph is determined by the Fourier eigenvalues of its Hermitian adjacency matrix. We classify perfect state transfer (PST) between distinct vertices in every nonempty oriented circulant graph. We show that each such graph is described by an odd primitive quadratic Dirichlet character of conductor $Δ$, a set of gcd-classes, and a choice between the two orientations of each selected class. For a graph of order $n$, we derive an explicit formula for every Fourier eigenvalue without assuming that $n/Δ$ is coprime to $Δ$. We prove that PST occurs only for $Δ\in\{3,4,8\}$ and give necessary and sufficient conditions on the connection set for each conductor. Equivalently, the square-free radicands of oriented circulant graphs with PST are exactly $1$, $2$, and $3$. More generally, when $λ_j=\sqrt{D}η_j$ with $η_j\in\mathbb{Z}$, congruences satisfied by the integers $η_j$ determine all PST pairs and times, the minimum period, and the largest vertex sets supporting multiple state transfer (MST). In this class, pretty good state transfer is equivalent to PST. We also determine the connected orders and enumerate the resulting graphs.
<<<END PAPER key=2608.11992>>>

<<<PAPER key=2608.12011>>>
Title: $m$-Bell and $m$-Stirling numbers: Iterated binomial transforms, hyper-Bessel functions, and moments of the Conway--Maxwell--Poisson distribution
Authors: Vencislav Popov
Primary arXiv category: math.CO
Abstract: We introduce a natural generalization of the Bell numbers: the $m$-Bell numbers $B^{(m)}_{n}$, characterized by the property that $m$ applications of the binomial transform reproduce the original sequence shifted $m$ places to the left. Their exponential generating functions satisfy $m$-th order ordinary differential equations whose solutions are hypergeometric (hyper-Bessel) functions, specializing to the exponential function when $m=1$ (classical Bell numbers) and to modified Bessel functions when $m=2$ (yielding "Bessel-Bell" numbers). Mirroring the Bell-Stirling correspondence, we construct $m$-Stirling triangular arrays from the two-term recurrence $S_m (n+1,k) = m \left\lfloor k/m \right\rfloor S_m(n,k)+S_m(n,k-1)$ and prove an elementary shift identity from which the central structure theorem follows: the row sums of the $m$-Stirling triangle reproduce $B^{(m)}_{n}$, and, more finely, the residue-class row sums are precisely the $m$ primitive $m$-Bell sequences. The $m$-Stirling numbers come in dual pairs (with first-kind partners, generalized falling factorials, and Lah-type companions), serve as conversion operators between polynomial bases, admit Dobiński-like formulas, and count congruence-constrained partitions in an urn model as well as restricted permutation insertion histories. Finally, we show that the $m$-Bell numbers govern the moments of the Conway-Maxwell-Poisson distribution with integer dispersion parameter $ν=m$: the scaled moments are combinations of fixed hyper-Bessel carrier ratios whose integer coefficients are precisely the primitive $m$-Bell sequences, recovering for $m=1$ the classical fact that the moments of the Poisson distribution are the Bell numbers.
<<<END PAPER key=2608.12011>>>

<<<PAPER key=2608.12013>>>
Title: Layer barriers for colour-biased tight Hamilton cycles
Authors: Zijian Deng, Qinfei Tang, Caihong Yang
Primary arXiv category: math.CO
Abstract: We construct a family of layer barriers for colour-biased tight Hamilton cycles in uniform hypergraphs. For every $k\ge 3$ and every $a\in\{0,\ldots,k-1\}$, we give a red--blue coloured $k$-graph that contains a tight Hamilton cycle, while every tight Hamilton cycle in the construction is perfectly colour-balanced. The construction underlying the higher-uniformity threshold conjectured by Behague, Clemen, Hyde and Morrison corresponds to the boundary case $a=0$ of this family. We show that interior choices of $a$ can yield strictly denser barriers. In particular, for $k=17$ and $a=8$, the asymptotic relative minimum vertex degree of our construction is \[ \frac{5761}{8192}\approx 0.703247, \] which exceeds the conjectured value $d_{17}\approx 0.699277$. This provides a counterexample to the proposed higher-uniformity threshold in Conjecture~6.1 of Behague, Clemen, Hyde and Morrison. Moreover, by choosing the layer appropriately as $k\to\infty$, the family contains barriers whose asymptotic relative minimum vertex degree is \[ 1-O\bigl(k^{-1/2}\bigr). \] Thus the interior members of the layer-barrier family exhibit substantially different behaviour from the previously considered boundary construction in large uniformity.
<<<END PAPER key=2608.12013>>>

<<<PAPER key=2608.12069>>>
Title: On ${\rm b}^{\ast}$-Coloring and $z$-Coloring of graphs with high girth
Authors: Zahra Ahmadidahr, Manouchehr Zaker
Primary arXiv category: math.CO
Abstract: In a proper vertex coloring $c$ of a graph $G$, a vertex $u$ is called a b-vertex if $u$ is adjacent to a vertex in every other color class. A ${\rm b}^{\ast}$-coloring is a proper coloring in which a b-vertex is adjacent to a b-vertex in every other color class. A Grundy coloring is a proper coloring obtained by the First-Fit (greedy) coloring procedure. A $z$-coloring of $G$ is a ${\rm b}^{\ast}$-coloring that is also a Grundy coloring. The ${\rm b}^{\ast}$-chromatic number (resp., $z$-chromatic number), denoted by ${\rm b}^{\ast}(G)$ (resp., $z(G)$), is the maximum number of colors used in a ${\rm b}^{\ast}$-coloring (resp., $z$-coloring) of $G$. Every graph admits a ${\rm b}^{\ast}$-coloring and a $z$-coloring that can be found using a polynomial-time coloring heuristic. Let ${\rm m}^{\ast}(G)$ be the largest integer $k$ such that a vertex of degree at least $k$ in $G$ has $k$ neighbors of degree at least $k$. We employ list-coloring techniques to prove that if $G$ has a girth of at least $7$, then ${\rm b}^{\ast}(G) = {\rm m}^{\ast}(G)+ 1$. A similar result is obtained for graphs of girth at least $6$ when ${\rm m}^{\ast}=3$. Finally, we obtain some results for the $z$-chromatic number. We prove that if the girth is at least $2m^{\ast}(G)+4$ and $G$ contains a specific tree as an ordinary subgraph, then $z(G)= m^{\ast}(G)+1$.
<<<END PAPER key=2608.12069>>>

<<<PAPER key=2608.12126>>>
Title: Two Relaxations of the Dominating Hadwiger's Conjecture
Authors: António Girão, Sergey Norin, Youri Tamitegama, Jane Tan
Primary arXiv category: math.CO
Abstract: Illingworth and Wood recently proposed the Dominating Hadwiger's Conjecture, a strengthening of Hadwiger's Conjecture which asserts that every graph with no dominating $K_t$-model is $(t-1)$-colorable. We prove two relaxations of this conjecture. First, we show that every graph with average degree $Ct (\log t)^2$ contains a dominating $K_t$-model for some absolute constant $C$. This bound improves on the $2^{t-2}$ due to Illingworth and Wood and is within an $O(\log t)$ factor from optimal. Second, we prove that the vertices of every graph with no dominating $K_t$-model can be partitioned into $t-1$ parts such that the subgraph induced by each part has bounded maximum degree.
<<<END PAPER key=2608.12126>>>

<<<PAPER key=2608.12202>>>
Title: Parallel covering a rhombus with equilateral triangles
Authors: Jingjing Wang, Yanxun Chang
Primary arXiv category: math.MG
Abstract: Suppose that ${R}^α$ is a rhombus with side length $1$ and with an interior angle $α$, where $0<α\leq \fracπ{2}$. Let $\triangle$ be an equilateral triangle with a side parallel to a side of ${R}^α$ and let $\{\triangle_{n}\}$ be a collection of homothetic copies of $\triangle$. In this paper, we show the following two results: if $0<α\leq\fracπ{3}$ and the sum of the areas of equilateral triangles from $\{\triangle_{n}\}$ is at least $\frac{\sqrt{3}}{4}(1+\cosα+\frac{\sqrt{3}}{3}\sinα)^{2}$, then these equilateral triangles can parallel cover the rhombus ${R}^α$; if $\fracπ{3}<α\leq\fracπ{2}$ and the sum of the areas of equilateral triangles from $\{\triangle_{n}\}$ is at least $\frac{\sqrt{3}}{4}(1+\frac{2\sqrt{3}}{3}\sinα)^{2}$, then they can parallel cover the rhombus ${R}^α$. Furthermore, these bounds are optimal on their respective intervals.
<<<END PAPER key=2608.12202>>>

<<<PAPER key=2608.12207>>>
Title: The Hajnal-Szemerédi theorem in digraphs revisited
Authors: Louis DeBiasio, Hal Kierstead
Primary arXiv category: math.CO
Abstract: Treglown conjectured (in a complementary form) that for every positive integer $k$, every digraph $D$ satisfying $\min\{d^+(v),d^-(v)\}\le k-1$ for all $v\in V(D)$ has an equitable acyclic $k$-coloring. If true, this would imply the acyclic coloring versions of the Hajnal-Szemerédi theorem for digraphs proved by Czygrinow, DeBiasio, Kierstead, and Molla (which in turn imply the original Hajnal-Szemerédi theorem for graphs). As it turns out, there is a simple reduction implicit in Aboulker, Oijid, Petit, Rocton, and Simon which surprisingly shows that Treglown's conjecture (and thus the results of Czygrinow, DeBiasio, Kierstead, and Molla) follows directly from the original Hajnal--Szemerédi theorem for graphs. We slightly modify the reduction in order to show that there exists a polynomial time algorithm for finding an equitable acyclic $k$-coloring in such a digraph.
<<<END PAPER key=2608.12207>>>

<<<PAPER key=2608.12237>>>
Title: On the Turán Density of $C_{10}$ in the Hypercube
Authors: Marko Pejić
Primary arXiv category: math.CO
Abstract: The $n$-dimensional hypercube $Q_n$ is the graph with vertex set $\{0,1\}^n$ in which two vertices are adjacent if they differ in exactly one coordinate. For a graph $H$, let $\operatorname{ex}(Q_n,H)$ be the maximum number of edges in an $H$-free subgraph of $Q_n$. The hypercube Turán density of $H$ is defined by $π_{\square}(H) = \lim_{n \rightarrow \infty} \operatorname{ex}(Q_n,H)/|E(Q_n)|$. In this short note, we prove \[ π_{\square}(C_{10})\leq π_{\square}(C_6). \] Combined with Baber's upper bound on $π_{\square}(C_6)$, this yields $π_{\square}(C_{10})\leq 0.36577$. Our proof first bounds the number of copies of $C_6$ in $C_{10}$-free subgraphs of $Q_n$, and then applies an averaging argument over the subcubes of $Q_n$.
<<<END PAPER key=2608.12237>>>

<<<PAPER key=2608.12266>>>
Title: Normalized skew Schur polynomials are Lorentzian
Authors: Philip B. Zhang
Primary arXiv category: math.CO
Abstract: We prove the conjecture of Huh, Matherne, Mészáros, and St.~Dizier that the normalization of every skew Schur polynomial in finitely many variables is Lorentzian. We first realize every nonzero skew Schur polynomial in finitely many variables as a specialization of a Schubert polynomial and prove that it is dually Lorentzian. The dual Jacobi--Trudi identity then identifies its normalization with the finite dual of a skew Schur polynomial obtained by rectangular complementation. As a consequence, skew Kostka numbers satisfy log-concavity inequalities along the root directions.
<<<END PAPER key=2608.12266>>>

<<<PAPER key=2608.12284>>>
Title: The finite basis problem for the flat semirings $S(W)$
Authors: Zidong Gao, Miaomiao Ren, Xianzhong Zhao
Primary arXiv category: math.CO
Abstract: We focus on the finite basis problem for flat semirings of the form $S(W)$, where $W$ is an arbitrary set of nonempty words. We prove that $S(W)$ generates a Cross variety (and hence is finitely based) whenever every word in $W$ has length at most $3$, whereas it is nonfinitely based whenever there exists $k \geq 3$ such that $W$ is $x^{k+2}$-free but not $x^{k+1}$-free. In particular, if $W_k$ denotes the set of all words of length $k$, then $S(W_k)$ is finitely based if and only if $k \leq 3$. Moreover, $S(W)$ is nonfinitely based whenever $W$ is finite and not $x^4$-free. These results provide a partial answer to an open problem raised by Jackson et al.~(J Algebra 611: 211--245, 2022).
<<<END PAPER key=2608.12284>>>

<<<PAPER key=2608.12449>>>
Title: A Graph Theoretical Approach to Optimizing Minimum Italian Domination Sets
Authors: Muhammad Zeeshan, Nahid Akhtar, Muhammad Faisal Nadeem
Primary arXiv category: math.CO
Abstract: A classical problem in graph theory known as the Italian domination number(also called Roman 2-domination number), involves assigning labels of 0, 1,or 2 to each node v. The goal is to ensure that every node with a label of 0 has a sum of labels of the nodes in its closed neighborhood that is 2 or greater. In computer systems, it is coined encompassing a robust cyber security strategy that will protect networks from potential threats, such as hacking, malware, and unauthorized access, by deploying security measures to provide the highest level of protection while reducing the misuse of resources. Toeplitz graphs are a special kind of graphs built over Toeplitz matrices from linear algebra, which are matrices with constant straight diagonal members. In this paper, we provide a detailed analysis regarding the Italian domination numbers for every Toeplitz graph family. We provide comprehensive results on Italian domination numbers across multiple graph families and identify the specific values at which the Italian domination number alters with increasing generator values.
<<<END PAPER key=2608.12449>>>

<<<PAPER key=2608.12310>>>
Title: A Multiplicative Fourier Proof of the Length-Four Index Conjecture
Authors: Hongjian Li, Pingzhi Yuan, Shijie Yuan, Weilin Zhang
Primary arXiv category: math.NT
Abstract: Let $C_n$ be a cyclic group of order $n$. The index conjecture in zero-sum theory asserts that if $(n,6)=1$, then every minimal zero-sum sequence of length four over $C_n$ has index one. Ge proved the conjecture for all sufficiently large $n$, and Pendleton reduced the known explicit threshold to $4.6\cdot 10^{13}$. We give a different argument based on multiplicative Fourier analysis on $(\mathbb{Z}/n\mathbb{Z})^\times$. Starting from the exact index-two residue identity, we take its multiplicative Fourier transform and express the odd Fourier coefficients through first moments of Dirichlet characters. The imprimitive characters for which this moment vanishes form an exceptional spectrum of cardinality at most $157\varphi(n)/1440$, hence strictly less than $\varphi(n)/9$. A finite-group support uncertainty inequality then forces the four-term multiset to be invariant under negation, contradicting minimality. We also give a minimal-modulus reduction, using the theorem of Shen-Xia-Li, from the general conjecture to the unit case. This proves the length-four index conjecture for every $n$ coprime to $6$.
<<<END PAPER key=2608.12310>>>

<<<PAPER key=2608.12316>>>
Title: Near optimal three-fold additive energy bound for points on convex curves
Authors: Adam Cushman, Ciprian Demeter, Shukun Wu
Primary arXiv category: math.CA
Abstract: Let $X\subset\mathbb{R}$ be finite and let $γ(t)=(t,f(t))$, where $f$ is strictly convex. We show that \[ J_3(γ(X)) =\#\{(x_1,\ldots,x_6)\in X^6:\sum_{i=1}^3γ(x_i)=\sum_{i=4}^6γ(x_i)\} \ll_{\varepsilon}|X|^{3+\varepsilon}. \] As applications, we prove that $|A-A|\gg_{\varepsilon}|A|^{5/3-\varepsilon}$ and $|A+A|\gg_{\varepsilon}|A|^{8/5-\varepsilon}$ for any convex sequence $A\subset \mathbb{R}$.
<<<END PAPER key=2608.12316>>>

<<<PAPER key=2608.12484>>>
Title: Monodromy of plane curve singularities and quiver mutation
Authors: Roger Casals
Primary arXiv category: math.AG
Abstract: The main result of this article shows that the quiver mutation class of a malleable real Morsification uniquely determines the integral monodromy module of a plane curve singularity. In particular, we show that the quiver mutation class of a malleable divide determines the complex topological type of an irreducible plane curve singularity. This establishes the algebraic-to-topological implication of a conjecture of S.~Fomin, P.~Pylyavskyy, E.~Shustin and D.~Thurston in the malleable irreducible case. The result is proven by developing representation-theoretic techniques based on an equivariant Euler pairing in the derived category of continuous finite-dimensional dg modules over a differential bigraded Ginzburg algebra. A key step uses these techniques to show that the quiver mutation class of a plabic fence uniquely recovers the torsion part of the Alexander module of the associated smooth link.
<<<END PAPER key=2608.12484>>>

<<<PAPER key=2608.12490>>>
Title: Online balancing of vectors with small coordinates
Authors: Antonios Hmadi
Primary arXiv category: math.CO
Abstract: Let $v_1,\ldots,v_T\in B_2^m$ be fixed in advance and revealed sequentially, and assume that $\|v_t\|_\infty\leqslant d^{-1/2}$ for some $d\geqslant 1$ and every $1\leqslant t\leqslant T$. There are absolute constants $L,C,c>0$ and a randomized online signing such that $$\mathbb{P}\left\{\max_{k\leqslant T}\left\|\sum_{t=1}^k\varepsilon_t v_t\right\|_\infty>6L\right\} \leqslant CT\exp\left(-\frac{cd}{\ln^2(ed)}\right).$$ Consequently, constant prefix discrepancy holds with probability at least $1-\varepsilon$ once $d$ is at least $C\ln\frac{3T}{\varepsilon}\left[\ln\left(e+\ln\frac{3T}{\varepsilon}\right)\right]^2$. In particular, every fixed sequence of vectors $a_t\in[-1,1]^m$ with at most $d$ nonzero coordinates admits an online signing with prefix discrepancy $O(\sqrt d)$ and failure probability at most $CT\exp[-cd/\ln^2(ed)]$. We also prove a nonuniform version in which the failure probability depends on the individual parameters $d_t=\|v_t\|_\infty^{-2}$, and a lower bound showing that a universal constant prefix discrepancy is impossible when $d=o(\ln T)$. We identify the corresponding $\ln^2 d$ barrier for the compact-potential method and extend the argument to general symmetric target bodies admitting a quadratic smoothness estimate.
<<<END PAPER key=2608.12490>>>

<<<PAPER key=2608.12491>>>
Title: On the minimum vertex cover of snarks
Authors: Gustavo Fernandes, Atílio G. Luiz
Primary arXiv category: math.CO
Abstract: A vertex cover of a graph $G$ is a subset of vertices $C \subseteq V(G)$ such that every edge of $G$ is incident to at least one vertex in $C$. The vertex cover number of $G$ is the minimum cardinality of a vertex cover of $G$ and is denoted by $τ(G)$. A snark is a connected, bridgeless, cubic graph that has an edge chromatic number of four, meaning its edges cannot be properly colored with only three colors. In this work, we investigate the problem of determining the value of a minimum vertex cover for classes of snark graphs. Given a positive integer $k$, we firstly prove that determining whether an arbitrary snark has a vertex cover $C$ with size $|C| \leq k$ is an NP-complete problem. Secondly, we determine the vertex cover number $τ(G)$ for several subclasses of snark graphs, such as Flower snarks, Goldberg snarks, Generalized Blanuša snarks and Loupekine snarks.
<<<END PAPER key=2608.12491>>>

<<<PAPER key=2608.12507>>>
Title: Virasoro Recursions for Simplicially Stable Curves with Colliding Markings
Authors: You-Cheng Chou, Hsian-Hua Tseng
Primary arXiv category: math.AG
Abstract: We study descendant integrals on moduli stacks of simplicially stable curves. For each finite collision complex, we factor the reduction morphism into elementary wall crossings and obtain a reconstruction formula in terms of ordinary Witten-Kontsevich correlators. We use the formula to derive corrected Virasoro recursions. We then package all finite-support theories in a completed disjoint-support Fock space, where the extended potential is a cumulant translate of the Witten-Kontsevich potential.
<<<END PAPER key=2608.12507>>>

<<<PAPER key=2608.12516>>>
Title: The balanced upper chromatic number of linear hypergraphs and the $n$-cube over $t$ elements
Authors: Gabriela Araujo-Pardo, Silvia Fernández-Merchant, Adriana Hansberg, Dolores Lara, Amanda Montejano, Déborah Oliveros
Primary arXiv category: math.CO
Abstract: A coloring of the vertices of a hypergraph is called \emph{balanced} if the sizes of the color classes differ by at most one. We say that a hyperedge is \emph{rainbow} if its elements have pairwise distinct colors. In this paper, we provide a general upper bound on the \emph{balanced upper chromatic number} of arbitrary linear hypergraphs, that is, the largest integer $k$ such that there exists a balanced $k$-coloring of the vertices of the hypergraph without rainbow hyperedges. We focus on the cube $C_t^n$, defined as the linear hypergraph whose vertices are the lattice points in $[0,t-1]^n$, and whose hyperedges are the sets of $t$ collinear points. We determine the exact balanced upper chromatic number of $C_t^n$ for $t\geq 4n-2$. For smaller values of $t$, we present bounds and determine this parameter (with few exceptions) in dimensions $2$ and $3$.
<<<END PAPER key=2608.12516>>>

<<<PAPER key=2608.12526>>>
Title: Cyclic Shuffle Groups: Universal Two-Transitivity and Complete Classification
Authors: Benjamin Marsh
Primary arXiv category: math.CO
Abstract: Let \(k\geq 3\), \(n\geq 1\), and let \(H_{k,n}=\Sh(C_k,n)\) be the group generated by the standard \(k\) pile perfect shuffle and cyclic pile permutation on a deck of \(kn\) cards. We prove that \(H_{k,n}\) is \(2\)-transitive whenever \(n\) is not a power of \(k\). Residual commutators give translations supported on two pile labels, and a strongly connected digit digraph propagates these translations throughout the deck, a separate argument resolves the antipodal support case. We then combine this result with fixed point ratio bounds for primitive groups and explicit boundary calculations to determine \(H_{k,n}\) for all \(k\) and \(n\). If \(n=k^f\), then \(H_{k,n}\cong C_k\wr C_{f+1}\). If \(k=4\) and \(n=2\cdot4^j\), then \(H_{4,n}\cong\AGL(2j+3,2)\). In every other case, \(H_{k,n}\) is \(\Alt(kn)\) or \(\Sym(kn)\), according to the parity of its generators. This proves Conjecture~1.10 of Amarra, Morgan and Praeger and Conjecture~5.1 of Xia, Zhang, Zhang and Zhu. More generally, we classify \(\Sh(P,n)\) for every pile group \(P\) containing \(C_k\), and obtain the odd \(k\) part of their Conjecture~5.2.
<<<END PAPER key=2608.12526>>>

<<<PAPER key=2608.12531>>>
Title: An upper bound for the type of a numerical semigroup, and a reduction of Wilf's conjecture
Authors: Mohammad F. Marashdeh
Primary arXiv category: math.CO
Abstract: Let $S$ be a numerical semigroup with multiplicity $\mult$, conductor $\cc$, embedding dimension $\ee$, type $\typ$ and genus $\gnus$, and let $\nn=\cc-\gnus$. Wilf's conjecture asserts that $\ee\,\nn\ge\cc$; the inequality $\gnus\le\typ\,\nn$ of Fröberg, Gottlieb and Häggkvist settles it when $\typ\le\ee-1$. The Apéry set of $S$ with respect to any $s\in S\setminus\{0\}$ carries a partial order whose maximal elements are the pseudo-Frobenius numbers translated by $s$; for $s=\mult$ its minimal elements are the minimal generators other than $\mult$. Comparing the two extremal statistics bounds the type by $\typ\le\ee-1+\Xii(S)\le\ee-1+Θ(S)$, where $Θ(S)$ measures the redundancy of the covering of the gaps of $S$ by the pseudo-Frobenius numbers and $\Xii(S)$ refines it. With an exact decomposition of the Wilf number this yields the genus bound $\gnus\le\ee-1+\typ(\nn-1)$, strictly stronger than $\gnus\le\typ\,\nn$ precisely when $\typ\ge\ee$, and reduces Wilf's conjecture to an inequality free of $\cc$ and $\nn$. We determine the equality case of $\gnus\le\typ\,\nn$, recovering a classification of Singhal; answer a question of Moscariello and Sammartano whenever $\ee\ge\typ+1$; and correct Kaplan's classification of the equality case for $\cc\le2\mult$, from which an infinite family is missing.
<<<END PAPER key=2608.12531>>>

<<<PAPER key=2608.12561>>>
Title: An AI Generated Counterexample to Borsuk Problem in Dimension 63
Authors: Yibo Ji
Primary arXiv category: math.MG
Abstract: We construct a 321 point set in R^63 that cannot be partitioned into 64 subsets of smaller diameter, proving b(63)>=65. Starting from the G_2(4) Euclidean representation and the Jenrich Brouwer 320 point core in dimension 63, we add one projected and rescaled point while preserving the relevant clique obstruction. The example and proof were generated entirely by ChatGPT using GPT 5.6 Sol. The author has personally verified the result and assumes responsibility for that verification, but claims no credit for the originality of the construction.
<<<END PAPER key=2608.12561>>>

<<<PAPER key=2608.12595>>>
Title: On Nearly-Perfect Covering Codes Beyond Radius One
Authors: Gabriel Sac Himelfarb, Moshe Schwartz
Primary arXiv category: cs.IT
Abstract: We study (binary) nearly-perfect covering codes, which are codes that attain the Van Wee bound with equality. They act as the covering counterparts to nearly-perfect error-correcting codes, which attain the Johnson bound with equality. These codes have been completely classified for covering radius $R=1$. We prove that no code with $R\geq 2$ can attain the original Van Wee bound with equality, since it omits the dependence on the minimum distance of the code. We refine the bound to account for the minimum distance and show some nearly-perfect covering codes. By proving some structural properties of such codes, we prove all nearly-perfect covering codes with $R=2,3$ must be equivalent to the codes we showed. We also prove that for any $R\geq 3$, there are at most a finite number of nearly-perfect covering codes.
<<<END PAPER key=2608.12595>>>

<<<PAPER key=2608.12604>>>
Title: Density bounds for permutations avoiding monotone arithmetic progressions
Authors: Jesse Geneson
Primary arXiv category: math.NT
Abstract: For $X\in\{\mathbb{N},\mathbb{Z}\}$, let $α_X(\ell)$ and $β_X(\ell)$ denote the supremal upper and lower densities of subsets of $X$ admitting $ω$-permutations without monotone $\ell$-term arithmetic progressions. We strengthen the published lower bounds for the three-term upper-density parameters by proving \[ α_{\mathbb{N}}(3)\geq\frac23,\qquad α_{\mathbb{Z}}(3)\geq\frac23. \] We also prove $β_{\mathbb{Z}}(4)=1$ by constructing four-permutable subsets of the integers whose lower symmetric densities approach one.
<<<END PAPER key=2608.12604>>>
