DONE — Task 044: bounded literature/status screen; no proof campaign or new bound.

# Old elementary records: selection audit, 2026-10-03

**Correction during task 045 (2026-10-03).** The direct forum check found July 2026 claims of 7/27 and 6/23 for #1066, missed by this report's initial search. [July 10 claim](https://www.erdosproblems.com/forum/thread/1066#post-7426), [July 12 claim](https://www.erdosproblems.com/forum/thread/1066#post-7461). The claims require proof review; the unchanged problem-page baseline does not establish that 8/31 is the current frontier. **No strict survivor is confirmed by this scan.** #1066 is downgraded to a source/claim-audit HOLD, and the earlier proposed 7/27 gate must first be checked against these manuscripts. No mechanical transfer from #708/#889 was established. The requested 15–30 positive hits are not supported: below are **18 ranked screened records**, all of which are now HOLD/LOW-FIT/NO-GO, followed by five adjacent families. Age alone does not establish unused slack.

**Coverage and evidence.** Retrieved the live [OPEN catalog](https://www.erdosproblems.com/range/1-end/open): 635 OPEN cards, from a site total of 1,221 problems. Screened quantitative statements, tag groupings and OEIS links; split follow-up among additive/Sidon/basis, graphs/geometry/probability, arithmetic, and #708/#889 neighbors. This is a systematic metadata pass plus selective primary-source reading, **not 635 full proof audits**. Recent papers were searched through 2026-10-03, including 2015–2026 improvements. “None located” always means this bounded search, never a proof of absence. Site OPEN labels and their numerical summaries sometimes lag or conflict with primary sources.

**Labels.** READ means the specified theorem/proof portion was inspected; it is not independent verification of an entire paper. SECONDARY means the original proof or exact record status remains unverified. Recent author computation reports establish activity only; their outputs were not replayed. All proposed gains below are HEURISTIC sensitivities or test targets, not probability estimates or proved achievable improvements. Implied constants and “sufficiently large” onsets remain unspecified unless explicitly stated. Rank is qualitative: visibility, an identifiable loss, and feasibility of verifying a change; no invented numerical score.

## Part A: ranked screened records

### 1. #1066 — independence in penny graphs: HOLD after missed 2026 claims

For $n$ planar points at pairwise distance at least 1, join pairs at distance exactly 1. Swanepoel (2002) proves $\alpha(G)\ge8n/31$; the quoted constructions give an asymptotic upper coefficient 5/16. This is a contact/minimum-distance graph, not an arbitrary unit-distance graph. [Problem](https://www.erdosproblems.com/1066), [original, §§3–4](https://link.springer.com/content/pdf/10.1007/s00454-002-2897-y.pdf), [author survey, §4.3](https://arxiv.org/pdf/1702.00066).

READ: the minimal-counterexample reduction with coefficient $m/(4m-1)$ forces any three consecutive closures to start at $a\ge2m-10$; Euclidean geometry forces such a start with $a\le4$ for the cases m = 7, 8 considered here. Taking $m=8$ contradicts this. At $m=7$, the boundary case $a=4$ remains. The proof uses elementary graph/angle arguments; the basic four-color bound here has a greedy proof. The initial search missed the live forum claims of 7/27 and 6/23; task 045 is auditing their primary manuscripts. The following old-proof analysis remains a source summary, not an originality assessment.

Tool/gain HEURISTIC: exact local adjacency and Euclidean compatibility, possibly a finite certificate. Excluding the remaining configuration could permit $7/27$, a gain $1/837\approx0.001195$; **the needed exclusion is unproved**. Improving angle estimates alone has not been shown to remove it. First gate: determine whether that boundary configuration is realizable and whether the reduction retains enough information.

### 2. #156 — smallest maximal Sidon set: HOLD, recent computation

Let $s(N)$ be the minimum size of an inclusion-maximal strong Sidon subset of $[1,N]$, including diagonal sums. Ruzsa (1998): $N^{1/3}\ll s(N)\ll(N\log N)^{1/3}$. [Original, pp.55–58](https://rexresearch1.com/ErdosMath/Analytic%20and%20Elementary%20Number%20Theory%20A%20Tribute%20to%20Mathematical%20Legend%20Paul%20Erdos.pdf), [2022 primary restatement](https://arxiv.org/html/2109.00292).

READ original construction: greedy extraction gives at least $p/8$ triple representations with pairwise disjoint supports (repetitions within a triple are allowed), modulo $p^2+p+1$. A point-miss estimate of the form $\exp[-cp/(8M)]$, followed by a union bound over the interval, produces the logarithm. Tool HEURISTIC: correlated coverage/alteration. Reducing log exponent $1/3$ to $1/4$ would save a factor $120^{1/12}\approx1.49$ at $N=e^{120}$, but no route proves this; improving $p/8$ alone changes only a hidden coefficient.

Freshness: no asymptotic improvement located, but [2026 author report](https://erdosproblemaday.com/day/156-maximal-sidon-log-factor) describes finite optimization through $N=136$. Thus this fails a literal no-recent-computation condition and is not an untouched record.

### 3. #1082 — distinct distances with no three collinear: HOLD, recent computation

For $n$ planar points with no three collinear, let $M$ be the maximum number of distances from one point, and $D$ the total distinct distances. Szemerédi's old bound gives $M\ge\lceil(n-1)/3\rceil$, hence a leading coefficient $1/3$ for $D$. Do not add a no-four-concyclic assumption. [Problem](https://www.erdosproblems.com/1082), [Nivasch–Pach–Pinchasi–Zerbib 2013, §2](https://arxiv.org/pdf/1207.1266).

READ proof exposition: count isosceles triangles by apex; each base has at most two apexes on its perpendicular bisector. The lower count already uses the exact integer class sizes 2 and 3 in the relevant range, so another Jensen/rounding pass is not a new improvement. Tool HEURISTIC: joint geometric compatibility of saturated bases. If one could prove $Z\le0.95n^2+O(n)$, the same lower count would give $M\ge7n/20-O(1)$, a gain $n/60$; no such estimate is proved here.

Freshness: [2026 author report](https://erdosproblemaday.com/report/1082) records finite optimization and rounding work, not an improved asymptotic coefficient. The pinned $\lfloor n/2\rfloor$ conjecture is already false; do not confuse it with the global-distance conjecture.

### 4. #902 — tournaments with a common dominator: LOW-FIT

Let $f(k)$ be the smallest order of a tournament on at least k vertices in which every $k$-set has a common outside vertex pointing to every vertex of that set. The quoted bounds are $(k+2)2^{k-1}-1\le f(k)\le(\log2+o(1))k^2 2^k$, Szekeres–Szekeres (1965) and Erdős (1963). [Original upper proof, §3](https://www.renyi.hu/~p_erdos/1963-08.pdf), [Simon 2022, §3](https://arxiv.org/pdf/2205.08357), [Jeffries 2026 introduction](https://arxiv.org/html/2604.08790v1).

READ: the random-tournament first moment is $\binom nk(1-2^{-k})^{n-k}<1$. Retaining the factorial or exponential remainders changes lower-order terms, not the leading $\log2$. The 2026 primary restatement retains the old leading record; nearby small-parameter constructions are active. Tool HEURISTIC: dependent bad-event analysis or a different random model. No supported positive leading-coefficient gain from mechanical accounting.

### 5. #1033 — a triangle with large degree sum: source-gate HOLD

For $n$-vertex graphs with more than $n^2/4$ edges, minimize the maximum sum of the degrees of the three vertices of a triangle. The quoted interval is $21n/16\le h(n)\le2(\sqrt3-1)n+O(1)$. [Problem](https://www.erdosproblems.com/1033), [Fan 1988](https://onlinelibrary.wiley.com/doi/10.1002/jgt.3190120216).

SECONDARY full proof; READ primary abstract gives the stronger density-dependent statement $f(n,e)\ge21e/(4n)$. No same-record improvement located in the quick freshness search. Exact degree marginals/weighted counting is only a tool guess: the loss in Fan's proof has not been read, and no numerical gain is defensible. Fetch the full proof before classifying it as an elementary optimization opportunity.

### 6. #1182 — sparse connected graphs that are 3-good: HOLD, baseline collision

Let $F(n)$ be the largest edge threshold such that **every** connected $n$-vertex graph with at most F$n$ edges has $R(K_3,G)=2n-1$. Do not substitute an existential extremal function. The site repeats a 1980 threshold $(17n+1)/15$. [Problem](https://www.erdosproblems.com/1182), [Burr–Erdős–Faudree–Rousseau–Schelp 1980](https://www.renyi.hu/~p_erdos/1980-04.pdf).

READ Lemmas 1.1–1.4 and Theorem 1(a): leaf/suspended-path reductions shrink an $n+k$-edge graph, for k ≥ 1, to a core of at most $5k$ vertices, and this core estimate is sharp. A [2003 thesis abstract](https://www.xueweilunwen.com/doc/1200412) already claims the stronger sufficient condition $q\le(7n-1)/6$, $n\ge4$. That claim is SECONDARY/unverified, but makes the old baseline unsafe.

Freshness/source gate: retrieve the thesis and match current surveys before any attack. Tool HEURISTIC: sharper core Ramsey input rather than reoptimizing the sharp $5k$ reduction. No gain forecast; a proposed transfer may already be in the literature.

### 7. #509 — covering polynomial lemniscates: source-gate HOLD

For any monic nonconstant complex polynomial, cover $\{z:|f(z)|\le1\}$ by disks with total radii at most $2.59$; the conjectured constant is 2. [Problem](https://www.erdosproblems.com/509), [Eremenko–Hayman, Lemma 3 and reference 9](https://www.math.purdue.edu/~eremenko/dvi/erdos23.pdf).

SECONDARY original proof: Eremenko–Hayman identify Pommerenke's **1960 Satz 3**, whereas the site's bibliography points to his 1961 polynomial paper. [1960 bibliographic record](https://eudml.org/doc/160803). The full Satz 3 was not obtained. No improvement located in the bounded 2015–2026 search. Cartan's weaker $2e$ argument being elementary does not establish that the $2.59$ proof is elementary. Tool HEURISTIC: exact covering/merging costs; no verified loss or gain size. Resolve the original source first.

### 8. #790 — no element is a sum of other distinct elements: source-gate HOLD

For every $n$-element set of integers, seek a large subset containing no relation $a_1=a_2+\cdots+a_r$ with all terms distinct and $r\ge3$. The quoted worst-case bounds are $\sqrt{n\log n/\log\log n}\ll\ell(n)\ll n/\log n$, Choi–Komlós–Szemerédi (1975). [Problem](https://www.erdosproblems.com/latex/790), [original DOI](https://doi.org/10.1090/S0002-9947-1975-0376594-1).

SECONDARY bound; original abstract inspected but full proof not obtained. This is not ordinary three-term sum-freeness. No matching 2015–2026 improvement located. No verified lossy step or identified mechanical tool. HEURISTIC sensitivity only: removing $\sqrt{\log\log n}$ would save a factor $\sqrt{\log100}\approx2.146$ at $n=e^{100}$; this is not an improvement forecast.

### 9. #789 — equal subset sums force equal sizes: source/domain HOLD

For arbitrary $n$-element sets of **nonzero** integers, let $h(n)$ be the worst guaranteed size of a subset in which any two nonempty equal-sum subsets have equal cardinality. Summands are not repeated. Choi (1974) supplies the lower bound and Straus (1966) the upper bound in $(n\log n)^{1/3}\ll h(n)\ll\sqrt n$. [Original abstract](https://doi.org/10.1016/0022-314X(74)90048-1), [problem](https://www.erdosproblems.com/789).

SECONDARY lower-bound proof. READ [Deshouillers–Freiman 1999, Theorem 1](https://www.numdam.org/article/AST_1999__258__141_0.pdf): the interval extremal problem has upper bound $\lfloor2\sqrt{n+1/4}-1\rfloor$ for large $n$. This does not resolve extraction from an arbitrary integer set. The site's domain needs matching to the original nonzero convention. No later matching improvement located. Tool HEURISTIC: exact subset-sum multiplicity accounting; no verified loss or numerical gain.

### 10. #187 — avoiding long monochromatic progressions: LOW-FIT

For every $\varepsilon>0$, there are $k_0$ and a two-coloring of the integers with no monochromatic progression of length $k\ge k_0$ and positive integer common difference $d<2^{(1-\varepsilon)k}$, Beck (1980). [Original DOI](https://doi.org/10.1016/0097-3165(80)90035-7), [proof exposition, Theorem 6.2.11](https://yufeizhao.com/pm/6.pdf).

READ exposition: an asymmetric local lemma bounds overlapping progressions using a count of order $k\ell2^{(1-\varepsilon)\ell}$, then compactness produces the infinite coloring. No same-conclusion 2015–2026 improvement located. Tool HEURISTIC: more precise event dependencies. Constant savings in this count primarily affect the onset; the bad-event probability $2^{1-k}$ already supplies the leading exponential scale in this framework. No supported positive exponent gain.

### 11. #336 — exact-order asymptotic bases: HOLD, not a short elementary proof

For each integer $r\ge2$, let $h(r)$ be the largest finite exact order of a set $A\subseteq\mathbb N$ whose weak asymptotic order is at most r: every sufficiently large integer is a sum of at most r elements of A, while the exact order is the least k for which every sufficiently large integer is a sum of exactly k elements of A. Summands may repeat. The safe quoted bounds are $1/3\le\liminf h(r)/r^2\le\limsup h(r)/r^2\le1/2$. Grekos (1988), Nash (1993), and Plagne (2004) supply the classical bounds/refinements. **Existence of a limit is not established.** [Problem](https://www.erdosproblems.com/336), [Plagne](https://doi.org/10.5802/aif.2064), [2023 primary survey, §1](https://home.olemiss.edu/~leth/papers/additive_bases_in_infinite_abelian_semigroups.pdf).

READ modern restatement; SECONDARY original proof loss. The method uses asymptotic density and Kneser theory; it is not a free finite-capacity optimization. No later matching leading improvement located. Tool HEURISTIC: exact density allocation. Changing $1/2$ to $0.49$ would be a 2% coefficient gain, but no mechanism or prediction supports it.

### 12. #222 — gaps between sums of two squares: LOW-FIT

For successive sums of two integer squares, the best quoted upper exponent is $1/4$, Bambah–Chowla (1947), with leading coefficient $2\sqrt2$. [Problem/OEIS link](https://www.erdosproblems.com/222), [Shiu 2019, §§1,4–5](https://math.colgate.edu/~integers/t48/t48.pdf).

READ: round $u=\lfloor\sqrt n\rfloor$, then $v=\lceil\sqrt{n-u^2}\rceil$. Separate worst-case rounding gives excess below $2\sqrt2\,n^{1/4}+1$. Jameson (2019) already improves the additive $+1$ to $-2$ by also testing $(u+1,0)$; Shiu proves infinitely many inputs where those choices cannot achieve $-3$. This is a barrier for that choice set, not all lattice points. Later large-gap lower bounds concern the opposite direction. Tool HEURISTIC: coupled rounding across more points; no supported positive leading-coefficient gain. The boundary loss has already received direct attention.

### 13. #304 / #18 — short Egyptian fractions: HOLD/LOW-FIT

Let $N(b)=\max_{1\le a<b}N(a,b)$, where $N(a,b)$ is the shortest distinct-unit-fraction representation with denominators greater than 1. Vose (1985): $N(b)\ll\sqrt{\log b}$. The related divisor-subset length satisfies $h(m)\ll\sqrt{\log m}$ for infinitely many practical $m$, not every practical $m$. [Modern primary, v2 (2026-05-24), §3](https://arxiv.org/html/2512.22083v2) still identifies the uniform #304 record.

READ modern restatement; SECONDARY Vose's original proof/loss. READ [Yokota 1992, Corollary 1](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/422DDD1972CEF8DC6A7DF98EB7060A79/S0008439500010882a.pdf/on_a_sum_of_divisors.pdf): $h(N_K)\asymp\sqrt{\log N_K}$ for Vose's particular sequence. This is not a barrier for arbitrary Egyptian fractions. Van Doorn–Tang's 2025/2026 work improves neighboring #293, not this uniform exponent. Tool HEURISTIC: different divisor families/representation accounting; optimizing a hidden big-O coefficient does not improve the displayed exponent. No defensible numerical gain.

### 14. #295 — unit fractions with denominators at least $N$: HOLD

Let $k(N)=\min\{t:1=\sum_{i=1}^t1/n_i,\ N\le n_1<\cdots<n_t\}$. Erdős–Straus (1971): $-c<k(N)-(e-1)N\ll N/\log N$, with unspecified constants. [Problem/bibliography](https://www.erdosproblems.com/latex/295).

SECONDARY: the original two-page proof was not obtained. Harmonic capacity explains the lower baseline, not the arithmetic correction cost in the upper bound. [2026 author report](https://www.erdosproblemaday.com/day/295-k17-exact) describes finite exact optimization, not an asymptotic improvement. Tool HEURISTIC: exact residual-denominator accounting; no verified upper-bound loss or gain size. Fails original-proof access and the literal no-recent-computation condition.

### 15. #887 — divisors just above the square root: source/domain HOLD

The quoted Erdős–Rosenfeld (1997) bound is at most $1+C^2$ divisors in $(\sqrt n,\sqrt n+C n^{1/4})$, eventually for each fixed $C$. [Problem](https://www.erdosproblems.com/887), [primary indexed extract, Propositions 4.1–4.2](https://bibliotekanauki.pl/articles/1390928.pdf).

SECONDARY/full PDF unavailable: the extract uses distinct integer sums $a_i+b_i$, for $a_ib_i=n$, and their minimum unit spacing. The site's claim of four divisors infinitely often for $C=1$ conflicts with its own eventual upper bound of two. Proposition 4.2 instead uses factor differences up to $16n^{1/4}$; it does not justify that sentence. Chan's 2014/2015 restricted cases and recent source/finite audits require a domain-level freshness check. Tool HEURISTIC: congruence/exact marginal accounting; no proven gain. Repair the source statement first.

### 16. #17 — cluster primes: analytic-input HOLD

Let $C(x)$ count primes $p\le x$ for which every positive even $2r\le p-3$ is a difference of primes at most $p$. [Elsholtz 2003](https://www.math.tugraz.at/~elsholtz/WWW/papers/papers13clusteractarith.pdf), READ, proves $C(x)\ll_c x\exp[-c(\log\log x)^2]$ for every fixed $c<1/8$. The displayed $1/60$ in the paper is already improved to $1/8-\varepsilon$ in its final paragraph.

Loss: separate short prime-pattern counts, $\binom ts\le t^s$, and a uniform sieve estimate. PNT and Montgomery–Vaughan large sieve enter, failing the strict elementary screen. No better same asymptotic coefficient located, but recent finite cluster-prime computations exist. Tool HEURISTIC: pattern/residue correlations. Restoring the factorial alone does not change the leading quadratic-log coefficient; no justified gain beyond $1/8$.

### 17. #33 — additive complements to squares: LOW-FIT, recently active

For $W\subseteq\mathbb Z_{\ge0}$ such that $W+\{1^2,2^2,\ldots\}$ contains all sufficiently large integers, writing $W(N)=|W\cap[0,N]|$, the old leading bound is $\liminf W(N)/\sqrt N\ge4/\pi$, attributed to Cilleruelo (1993), Habsieger (1995), and Balasubramanian–Ramana (2001). [Ding–Sun–Wang–Xia, equation (1.1)](https://arxiv.org/html/2211.16810).

READ modern restatement/theorem, SECONDARY old proof. The 2023 preprint/2026 journal work studies repeated representations and retains this leading record; its excess estimate is not automatically an improvement of $4/\pi$. Tool HEURISTIC: exact multiplicity versus boundary accounting. No verified leading gain; recent direct attention makes “unused old loss” unsupported.

### 18. #1109 — squarefree sumsets: NO-GO elementary screen

For $A\subset[1,N]$ with **all** $A+A$, including $2a$, squarefree, Konyagin (2004) gives $(\log N)^2\log\log N\ll f(N)\ll N^{11/15+o(1)}$. [Problem](https://www.erdosproblems.com/1109), [author's 2003 announcement](https://publications.mfo.de/bitstream/handle/mfo/2759/Report_03_12.pdf?isAllowed=y&sequence=1), [2004 paper](https://www.mathnet.ru/links/07197a2b13c7b0f47f59a3a41bf24b15/im486_eng.pdf).

SECONDARY full proof: the announcement identifies a large sieve over prime squares using Bombieri–Zannier rational-point bounds. [Recent finite optimization](https://www.erdosproblemaday.com/day/1109-squarefree-sumset) does not update the exponent. Higher moments/cluster estimates would alter substantial analytic input; no mechanical loss or plausible numerical gain identified.

## Part B: five neighboring families; no confirmed mechanical transfer

The #708 hinge/duality method can certify a specified finite counting inequality. It does not create a missing uniform arithmetic estimate. The #889 result includes a Matveev input; calling the complete argument elementary would be inaccurate.

**B1. #1181 — missing prime in a short block: highest HOLD.** Put $k=\lfloor\log n\rfloor$, and let $q$ be the least prime not dividing $\prod_{i=1}^k(n+i)$. The [page, citing Erdős 1979](https://www.erdosproblems.com/1181) retains $q\le(1+o(1))(\log n)^2$; it asks for a fixed factor $1-c$. SECONDARY record citation; the elementary product accounting can be checked directly: $\prod_{k<p<q}p\mid\binom{n+k}{k}$, hence $\theta(q^-)-\theta(k)\le\log\binom{n+k}{k}$. The omitted prime $q$ must not be included. Translating this to the asymptotic coefficient uses prime asymptotics. Factorial savings are only $O(\log n\log\log n)$. Tool: carrier/prime-power budget as in #889, with a finite dual certificate only after a valid inequality exists. HEURISTIC $1\to0.99$ needs an additional $0.01(\log n)^2$ budget uniformly; no evidence supplies it. No credible matching recent improvement located.

**B2. #1093 — positive deficiency of good binomial coefficients: source-gate HOLD.** For $n\ge2k$, deficiency is defined only if $\binom nk$ has no prime factor $p\le k$; it counts the $k$-smooth terms of $n,n-1,\ldots,n-k+1$. The quoted Erdős–Lacampagne–Selfridge (1993) result is $n\ll2^k\sqrt k$ when the deficiency is defined and positive. [Definition/page](https://www.erdosproblems.com/latex/1093), [original DOI](https://doi.org/10.1090/S0025-5718-1993-1199990-6). SECONDARY original proof/loss, full text unavailable. Tool guess: valuation/carrier allocation; HEURISTIC $2^k\to1.99^k$ is a 0.5% base reduction, with no established route. A [2026 preprint, Theorem 1.1/Lemma 4.1](https://arxiv.org/html/2609.25042v1), READ, claims an infinite deficiency-one construction, but **its construction fails at $k=2$**: $M=\prod_{p\le k}p^{\lfloor\log_p k\rfloor+1}=4$, $n=M+k-1=5$, and $\binom52=10$ has factor 2. Exact integer arithmetic was independently checked. This claim neither solves #1093 nor supersedes the old bound. No external correction was sent.

**B3. #650/#709/#711/#860 — distinct multiples: updated family; one source HOLD.** [Van Doorn–Li–Tang 2026, Theorem 2.1](https://arxiv.org/html/2603.28636v1), READ, gives the exact guarantee $\min(m,\lceil2\sqrt m\rceil)$ for matching distinct multiples of a set of m distinct positive integers of maximum M inside any open interval $(x,x+2M)$. Thus the old #650 target is closed. [Chen 2026, Theorems 1.1,1.4 and §§3,5](https://arxiv.org/html/2607.26450v1), READ, replaces the 1980 bounds in #711/#860 by $F(n)\le n^{\beta+o(1)}$, $\beta<1.4031$, and $h_P(n)\ll n^{7/5}/(\log n)^{2/5}$; $\beta\in(1,2)$ solves $2\beta^3-8\beta^2+8\beta-1=0$. **INFERENCE, not a separately published record:** applying the same Hall/AP-union argument to arbitrary moduli of maximum $M$ appears to give #709 interval factor $f(n)\ll_\varepsilon n^{\beta-1+\varepsilon}$. It requires a complete domain check before citation as a theorem. A remaining source-audit lead is interval factor 3 for **prime** moduli: [Erdős 1986, p.238](https://www.renyi.hu/~p_erdos/1986-16.pdf), READ, balances incidence/collision counts at about $\sqrt6\,k$ for $k^2$ primes. Current-best status, endpoints and union-versus-matching must be settled. HEURISTIC joint collision accounting could target $2.5k$, a 2.06% increase, but no transfer is proved.

**B4. #375/#962 — Grimm and large-prime blocks: NO-GO elementary transfer.** Grimm asks for distinct prime representatives for consecutive composite integers. The old guaranteed length $g(n)\gg(\log n/\log\log n)^3$ (Ramachandra–Shorey–Tijdeman 1975) uses transcendence theory. [Laishram–Murty (2012; arXiv 2013)](https://arxiv.org/pdf/1306.0765), relevant lemmas/Theorem 1 READ, retains this lower bound and gives an upper bound $g(n)<n^\alpha$ for some $\alpha\in(0.45,0.46)$, eventually. For #962, primes greater than block length $k$ in separate terms are automatically distinct, so an old square-root upper estimate is not a safe current target. Smooth-number/multiplicative-dependence control is the missing input, not a Hall or factorial bookkeeping identity. No recent universal lower improvement located, but no supported HEURISTIC gain either; an exponent target $3.01$ would be arbitrary.

**B5. #687/#970 — Jacobsthal: NO-GO, computationally developed.** Distinguish primorial $h(k)$ from the worst Jacobsthal function over arbitrary integers with $k$ prime factors. The old Iwaniec (1978) order $O((k\log k)^2)$ comes from linear sieve. [Costello–Watts 2015](https://researchrepository.ucd.ie/server/api/core/bitstreams/75644f16-719c-426a-8174-5192a721a8d2/content), READ, already uses recursive interval counts and exact congruence intersections. Its $h(k)\le0.27749612254k^2\log k$ is verified only for $50\le k\le10000$, not all $k$; no certificates were replayed here. This is adjacent to #708 but fails the no-recent-optimization screen. HEURISTIC finite coefficient $0.27$ would save 2.70%; an infinite-parameter theorem still needs sieve input, not extrapolation from finite checks.

## Exclusions and freshness corrections

| Region/item | Why it does not provide another strict hit |
| --- | --- |
| #901, property B | Old random-hypergraph upper coefficient $(e\log2/4+o(1))k^2 2^k$ is a poor mechanical target: [Duraj–Kozik–Shabanov 2021](https://arxiv.org/pdf/2102.12968), Theorem 1 READ, makes the relevant random-model threshold sharp. A different model is needed. |
| #104, unit circles | Old $n(n-1)/3$ pair-capacity upper bound for distinct radius-one circles containing at least three input points; [recent finite optimization](https://siddhartha-mahajan.github.io/math/a003829-unit-circles/) means the strict screen fails. No certificates replayed. |
| #812/#1030, Ramsey increments | Old page bounds already lag [1989 primary bounds](https://www.renyi.hu/~p_erdos/1989-21.pdf) and [Xu–Shao–Radziszowski 2011](https://epubs.siam.org/doi/10.1137/10080868X); not untouched pre-2005 records. Match parameter ranges before transferring an increment. |
| #167 | Recent stronger primary claims [Yi 2026](https://arxiv.org/abs/2608.23010), [Wang 2026](https://arxiv.org/abs/2609.13831) make the old Haxell $66/23$ target stale. Full proofs not audited; exclusion is based on current claims, not certified correctness. |
| #170/#530/#272 | [Bernshteyn–Tait 2019](https://arxiv.org/abs/1901.09411) and Yang–Liao 2022 update old difference-basis bounds; [Bailleul–Riblet 2026](https://arxiv.org/abs/2605.03181) and [Yang 2026](https://arxiv.org/abs/2607.23004) update their respective targets. Do not blend interval or starred variants. |
| #817/#866 | [Costa 2026](https://arxiv.org/abs/2609.06303) changes #817's status; [van Doorn 2026](https://arxiv.org/abs/2605.00040) concerns five arbitrary integers, while [van Doorn–Erlbacher 2026](https://arxiv.org/abs/2609.39314) concerns four positive integers. New claims/domain distinctions defeat an old-record selection. |
| #876 | The 2000 upper coefficient 403 holds for arbitrarily large $n$, not necessarily all large $n$. [Original Theorem 3](https://matwbn.icm.edu.pl/ksiazki/aa/aa95/aa9532.pdf), [Lev 2003 appendix](https://www.impan.pl/shop/en/publication/transaction/download/product/82600), and [Conlon–Fox–Pham 2021](https://www.its.caltech.edu/~dconlon/subset_sums.pdf) require a fresh quantified comparison. Do not present 403 as a verified current constant. |
| #201 | The Komlós–Sulyok–Szemerédi comparison $c_kR_k(n)\le G_k(n)\le R_k(n)$ has no explicit $c_k$ or read proof-loss in this audit. [Original DOI](https://doi.org/10.1007/BF01895954). An unspecified coefficient is not an explicit optimization target. |
| #1221 | [Korsky 2026 v2](https://arxiv.org/html/2609.07196v2), abstract/Theorem 1.1 READ, claims all three requested divergence statements for sequential circle-point spacings. The live OPEN card is stale; the full proof is unaudited here. Do not copy the page's conflicting normalization. |
| #1184 | **INFERENCE from a read primary theorem:** [Younis 2024, Theorem 1.1](https://arxiv.org/html/2409.05761v1), with $x=n,h=y=k$, gives the Dickman-density conclusion for fixed $1<\alpha<30/17$, $n=k^{\alpha+o(1)}$. It does not settle $\alpha\ge30/17$, and uses modern zero-density input. |
| Product prime factors / small sieve | Hanson-type old bounds have later improvements: [Shorey–Tijdeman 2016](https://arxiv.org/html/1612.05438). The general-divisor version of #784 also has a [Weingartner update](https://arxiv.org/html/2310.13038); distinguish it from prime-only questions. |
| Sidon/B3/B2[g], cube C4, subset sums | The prior 042/043 gates already exposed recent optimization or structural obstructions. No repeated attack or new solver run was performed to fill this list. |

**Empty regions.** No strict positive in additive combinatorics/bases, discrepancy/probabilistic methods, or #708/#889 arithmetic transfer was established. The strongest additive lead (#156) has a specific logarithmic union-bound loss but fails the recent-computation screen. Arithmetic leads mostly fail proof access, elementary-input, current-baseline, or domain gates. This is evidence against launching many old-constant campaigns on the present dossier, not a theorem that other opportunities do not exist.

**Next useful order.** First, review the already posted #1066 claims before any configuration audit; second, source acquisition for #509/#1033/#1093; only if the coordinator relaxes the literal computation condition, reassess #156/#1082. For #1181, require an actual fixed-proportion prime-budget inequality before scheduling proof work. No claims of priority, no original conjecture solved, and no full campaign recommended by this report.

**Execution and limits.** Root plus three existing source-review seats; no fresh clean-room agents, solver, Lean build, new dependency, cloud job, commit/push, or external message. Only source reading and small exact arithmetic checks were performed. The global-memory recall tool/skill was unavailable; no notice was invented and no preset was changed. Three same-vendor read-only integration reviews completed with the stated scope; all requested definition, endpoint, attribution and formatting repairs were applied. The root separately inspected #1066 Theorem 4/Lemma 10 and the #1093 counterexample. Wall time and check scope, not unobserved model token/cost claims, are reported there.

## Freshness addendum 2026-10-09 — OpenAI math release (coordinator, keyword screen)

OpenAI's 2026-10-06 catalogue (719 manuscripts, 372 families; see `openai_math_release_20261009.md`)
touches this audit as follows; a scout G2 sweep (G2_OPENAI_RELEASE_20261009.md) will finalize each row.

- Row 13 (#304/#18 short Egyptian fractions): family 025 claims N(b) = O(log log b), Erdős's conjecture,
  with a Lean link → **CLAIMED-CLOSED 2026-10-06**; remove from the candidate pool until the claim fails.
- Row 3 (#1082): family 167 (weak pinned planar distances, n^{1−ε} from all but o(n) points) and family
  183 (halving lines, no three collinear) are ADJACENT, not the exact-coefficient statement; HOLD stands,
  any future #1082 G2 must cite them.
- Exclusion row #167 (unit distances): family 167 also claims O(n^{4/3−δ}) unit distances → the
  coefficient game on the 4/3 exponent is moot.
- All other rows: no title/abstract hit on the keyword screen (Sidon, B₃, penny, hypercube C₄, Zaremba,
  binomial/Selfridge, divisors, sum of two squares, cluster primes, asymptotic bases: 0 hits).
