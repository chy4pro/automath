OPEN — no unconditional explicit digit bound is established by these attempts.

# Three independent clean-room attempts at prime-denominator Zaremba

Task 010, 2026-09-26. Each of the three agents received a fresh context containing only the task's problem statement and clean-room restrictions. They were forbidden to read files, papers, web sources, or other agents' output. Their results are compared here only after delivery. No route report was supplied to them. The root's checks below are elementary deductions, not a literature or priority audit.

## Attempt A: an explicit M=2 correlation reduction

This attempt proves an elementary supply lemma and an exact-denominator lifting lemma. It does not prove the needed correlation estimate. Its conditional digit value 2 is therefore a target under a strong unproved hypothesis, not a new unconditional bound.

### A.1. An elementary supply lemma

For real Q>=297, let R(Q) consist of the reduced pairs (q,r), 1<=r<q<=Q, for which r/q has a canonical finite simple continued fraction with digits in {1,2} (last digit 2). Then

\[
 |R(Q)|>(Q/297)^{201/200}.                                      \tag{A1}
\]

Here is a complete proof. The consecutive denominator pair evolves by (q,t)->(a q+t,q). A block of five digits multiplies q by an increasing affine function of t/q in [0,1]. Its maximum is attained at t/q=1. The 32 maxima, calculated by the same integer recurrence starting at (1,1), are

```
13,21,18,31,19,30,27,46,19,31,26,45,29,46,41,70,
18,29,25,43,26,41,37,63,27,44,37,64,41,65,58,99.
```

Call these integers d_j. Integer division gives sum_j floor(10^6/d_j)=1026138, whence sum_j 1/d_j>41/40. Also

\[
 (41/40)^{40}>1+1+780/1600+9880/64000>13/5,
 \qquad (13/5)^5>99.
\]

Thus, with s=201/200,

\[
 \sum_j d_j^{-s}\ge99^{-1/200}\sum_jd_j^{-1}>1.                \tag{A2}
\]

Start with denominator pair (1,0). Build the 32-branch block tree, stopping each branch the first time its denominator exceeds T=Q/297. Every block has multiplier between 8 and 99; hence the tree is finite and every leaf has T<q<=Q/3. Give each node weight q^{-s}. By (A2) replacing any nonterminal node by its children strictly increases total weight, so the leaf weights sum to more than 1. Each is less than T^{-s}, yielding more than T^s leaves.

Distinct leaves represent distinct rationals: the Euclidean algorithm gives at most two finite simple continued-fraction expansions of a rational, and their lengths differ by one via [...,a,1]=[...,a+1]. All leaf lengths are multiples of five. Append digit 2 to every leaf. The resulting denominator is 2q+t<=3q<=Q, all resulting words are canonical, and different words give different fractions. They are reduced because the digit matrices have determinant -1. This proves (A1).

Root correction: the delivered attempt allowed terminal digit 1. Canonicalizing an ending [...,2,1] would introduce digit 3. Appending 2 instead preserves the claimed cap M=2; it changes the original counting denominator 99 to 297 and the later constant 198 to 594. All formulas here use the repaired canonical convention.

### A.2. An incidence whose lift has denominator exactly p

For prime p>=100000 put Q_p=floor(sqrt(p-1)) and

\[
 D_p=\{r/q\pmod p:(q,r)\in R(Q_p)\}\subset\mathbb F_p^*,
 \qquad N_p=|D_p|.
\]

The reduction is injective: if p divides rq'-r'q, its absolute value is strictly below Q_p^2<p, so it is zero; equality of reduced fractions gives equality of pairs. Since Q_p>=sqrt(p)/2, (A1) implies

\[
 N_p>p^{201/400}/594^{201/200}.                               \tag{A3}
\]

If x,y in D_p satisfy xy=-1, their pairs obey p | qq'+rr'. Positivity and the height bound give 0<qq'+rr'<2Q_p^2<2p, so

\[
 qq'+rr'=p.                                                  \tag{A4}
\]

For C(a)=[[a,1],[1,0]], a word w representing r/q=[0;w] has matrix W_w with first column (q,r)^T. The product W_w^T W_u is the digit word reverse(w) followed by u, and its upper-left entry is (A4). All digits are 1 or 2, and its determinant is +/-1; thus its numerator and denominator are coprime. Consequently any such incidence produces an exact prime denominator p. Merely obtaining a multiple of p would not suffice; the strict height bound is essential here.

### A.3. The unproved estimate and its exact consequence

For each multiplicative character chi of F_p^*, define F_p(chi)=sum_{x in D_p}chi(x), and define the real sum

\[
 T_p=\sum_{\chi\ne1}\chi(-1)F_p(\chi)^2.
\]

Character conjugation pairs show that T_p is real. If I_p counts ordered pairs (x,y) in D_p^2 with xy=-1, including the diagonal, orthogonality gives

\[
 I_p=(N_p^2+T_p)/(p-1).                                      \tag{A5}
\]

Indeed, the indicator is (p-1)^{-1}sum_chi chi(-xy). No absolute square replaces F_p(chi)^2 in this identity.

**Unproved hypothesis H_A.** For every prime p>=100000,

\[
 T_p\ge-\frac{99}{100}N_p^2-N_pp^{401/800}.                   \tag{A6}
\]

**Conditional theorem.** Under H_A every prime

\[
 p>100^{800}\,594^{804}                                      \tag{A7}
\]

is a denominator with digit cap M=2. In fact (A3),(A7) give N_p>100p^{401/800}, and (A5),(A6) then give (p-1)I_p>=N_p(N_p/100-p^{401/800})>0. Apply the exact-lifting lemma.

More generally, T_p>=-(1-kappa)N_p^2-CN_pp^{401/800} for all primes p>=P_0, with specified positive kappa,C, suffices for p>max{100000,P_0,(C/kappa)^800 594^804}. The root explicitly retains 100000 in this general form because the construction above was stated on that domain. Unknown kappa,C,P_0 leave the onset unknown.

The unresolved content is (A6), not the counting or lifting. It allows a real-height bias through the factor 99/100; square-root cancellation around the uniform main term is not assumed. Parseval gives only |T_p|<=(p-1)N_p-N_p^2, which is inadequate. Cardinality alone cannot force an incidence: for p=3 mod 4 the involution x->-1/x has no fixed point, and choosing one point from each two-cycle gives a set of size (p-1)/2 with none. No evidence here shows that (A6) is easier than the original arithmetic distribution problem.

Finally, M=1 cannot work for all sufficiently large primes. Its denominators are Fibonacci numbers, whose reciprocals sum to a finite value (the recurrence gives exponential growth). The reciprocals of the primes diverge: otherwise their finite Euler products would stay bounded, although those products include the partial harmonic sums over integers up to their cutoff. Therefore the conditional value 2 is the smallest possible integer digit cap. This observation supplies no proof of H_A.

## Attempt B

### B.1. A complete elementary logarithmic bound

This attempt proves, for every prime p, a reduced numerator with digit cap ceil(2 log p), where log is natural. The cap depends on p, so it does not settle the fixed-cap target.

For 1<=a<p let a/p=[0;b_1,...,b_r] be canonical, b_r>=2, and put A=max b_j. Define

\[
 m_p(a)=\min_{1\le d<p,\ c\in\mathbb Z}d|ad-pc|.
\]

The exact useful bounds are

\[
 \frac p{A+2}<m_p(a)\le\frac pA.                             \tag{B1}
\]

To prove them, write P_n/Q_n for the convergents, with (P_{-1},Q_{-1})=(1,0),(P_0,Q_0)=(0,1). Their recurrence gives |P_{n+1}Q_n-P_nQ_{n+1}|=1. If xi_{n+1}=[b_{n+1};...;b_r] and epsilon_n=Q_n a/p-P_n, substitution gives

\[
 |\epsilon_n|=(Q_n\xi_{n+1}+Q_{n-1})^{-1}\quad(0\le n<r).
\]

Successive nonzero errors have opposite signs and epsilon_r=0. Given d<p, choose the largest n with Q_n<=d. Then d<Q_{n+1}. Express (c,d)=u(P_n,Q_n)+v(P_{n+1},Q_{n+1}) in this integral basis. If v=0 then u>=1. If v>=1 then u<=-1; if v<=-1 then u>=1. Therefore |d a/p-c|=|u epsilon_n+v epsilon_{n+1}|>=|epsilon_n|. It follows that

\[
 d|d a/p-c|\ge(Q_n|\epsilon_n|)
 =\frac1{\xi_{n+1}+Q_{n-1}/Q_n}>\frac1{A+2}.
\]

The last inequality uses xi_{n+1}<A+1 and Q_{n-1}/Q_n<=1. Taking j with b_j=A and (c,d)=(P_{j-1},Q_{j-1}) gives d|ad-pc|=p/(xi_j+Q_{j-2}/Q_{j-1})<=p/A. This proves (B1), including the possible initial equal denominators Q_0=Q_1=1, which the largest-n convention handles.

For real T>=2 define the set of residues

\[
 \mathcal H_T(p)=\{\pm u v^{-1}\pmod p:u,v\ge1,\ uv\le p/T\}.
\]

All inverses exist. Directly from its definition,

\[
 a\notin\mathcal H_T(p)\quad\Longleftrightarrow\quad m_p(a)>p/T. \tag{B2}
\]

Indeed, a representation gives |av-pc|=u, while a minimizing pair gives v=d,u=|ad-pc|>0. One may restrict to coprime u,v by dividing both coordinates by their gcd. For every integer M>=1, (B1),(B2) yield

\[
 \mathcal H_{M+1}(p)\ne\mathbb F_p^*
 \ \Longrightarrow\ \exists a:A\le M
 \ \Longrightarrow\ \mathcal H_{M+2}(p)\ne\mathbb F_p^*.       \tag{B3}
\]

Now choose M=ceil(2 log p), B=M+1. If B>p, then M>=p and a=1 suffices. Otherwise B<=p, and this case has p>=5 and B>e. The number D(X) of positive ordered pairs uv<=X obeys

\[
 D(X)\le X\sum_{v\le X}1/v\le X(1+\log X)\quad(X\ge1).
\]

Consequently

\[
 |\mathcal H_B(p)|\le2D(p/B)
 \le\frac{2p}{B}(1+\log(p/B))
 <\frac{2p\log p}{B}\le\frac{pM}{B}
 =p-p/B\le p-1.
\]

The strict inequality uses log B>1. Thus some nonzero residue is omitted, and (B3) proves the claimed cap ceil(2 log p). In particular M=2^150 works for every prime p<=exp(2^149). This is a finite range, not the assertion for all sufficiently large primes.

### B.2. The missing fixed-cap step

The explicit hypothesis H_B is that, for some p_0, every prime p>=p_0 has H_{2^150+1}(p) different from F_p^*. By (B3), H_B implies the requested digit cap 2^150 with no further loss. It is essentially a reformulation, since the converse holds with the one-unit parameter shift in (B3). No proof of H_B is provided.

For a fixed T the available counting bound is of order (2p/T)log p and eventually ceases to show a missing residue. A successful argument must exploit collisions or another structural restriction; merely counting representations cannot finish this route.

The attempt also identifies the height obstruction to a purely modular argument. A bounded-digit word whose denominator is zero modulo p can be multiplied on the right by arbitrarily long bounded-digit words congruent to the identity modulo p, preserving that denominator congruence while increasing the integer height. Such identity words exist by taking powers of a fixed invertible digit matrix in the finite group. An additional bound such as 0<q(word)<2p is required to force the multiple to equal p.

## Attempt C

### C.1. A sharper elementary counting lemma

Let V_M(X) be the set of primitive vectors (x,y), 0<y<x<=X, with y/x=[0;a_1,...,a_n], digits 1<=a_i<=M and last digit at least 2. For every integer M>=22 put s=2-24/(M+2). Then

\[
 |V_M(X)|\ge\left(\frac X{3(M+1)}\right)^s
 \quad\text{for }X>3(M+1).                                  \tag{C1}
\]

Here is the complete proof, independent of A's five-digit calculation. For consecutive denominator ratio r=Q_{n-1}/Q_n in [0,1], appending a changes the denominator by a+r and the ratio to 1/(a+r). Define

\[
 L_s f(r)=\sum_{a=1}^M(a+r)^{-s}f(1/(a+r)).
\]

Take f(r)=1/(1+r), epsilon=24/(M+2), so s=2-epsilon. Telescoping gives L_2f(r)=f(r)-1/(M+1+r). Since all (a+r)^epsilon>=1, the a=2 term alone gives

\[
 \frac{L_sf(r)}{f(r)}
 \ge1-\frac{1+r}{M+1+r}
 +(2^\epsilon-1)\frac{1+r}{(2+r)(3+r)}
 \ge1-\frac2{M+2}+\frac\epsilon{12}=1.                     \tag{C2}
\]

The last step uses log 2>=1/2, e^t>=1+t, and (1+r)/((2+r)(3+r))>=1/6, equivalent to r(1-r)>=0.

For T>1, grow the entire digit tree and stop each branch when Q_n>=T for the first time. The tree is finite since Q_{n+2}>=2Q_n. Its leaves obey T<=Q_n<(M+1)T. Give a node weight Q_n^{-s}f(r). By (C2) the leaf weight sum is at least the root weight 1. Each leaf weight is at most T^{-s}, so there are at least T^s leaves. Append digit 2. These distinct canonical words have denominators 2Q_n+Q_{n-1}<3(M+1)T. Taking T=X/[3(M+1)] proves (C1), without a terminal-digit ambiguity.

For M=2 there is the sharper specialized bound

\[
 |V_2(X)|\ge(X/9)^{41/40}\quad(X>9).                       \tag{C3}
\]

Take f(r)=1/(2+r). Direct substitution gives

\[
 L_1f(r)=\frac1{3+2r}+\frac1{5+2r},\qquad
 \frac{L_1f(r)}{f(r)}=1+\frac1{(3+2r)(5+2r)}\ge\frac{36}{35}.
\]

As a+r<=3, L_{41/40}f>=3^{-1/40}L_1f>f. The strict numerical inequality follows by the binomial theorem:

\[
 (36/35)^{40}\ge1+40/35+780/35^2+9880/35^3
 =3+430/42875>3.
\]

The same tree has root weight 1/2 and each leaf weight at most (1/2)T^{-41/40}, so it has at least T^{41/40} leaves. Appending 2 gives height below 9T and proves (C3).

### C.2. Exact lifting and one precise correlation hypothesis

For prime q set X=floor(sqrt(q-1)), S_M(q)={y/x mod q:(x,y) in V_M(X)}, and m=|S_M(q)|. The determinant argument from A.2 proves injectivity, so m=|V_M(X)|. If two slopes t,u satisfy tu=-1, their vectors have xx'+yy'=q. The product G(w)^T G(w') has this denominator. Here the last digit of w' is at least 2 and the first digit of reverse(w) is at least 2; the output is canonical with numerator strictly between 0 and q. All digits are at most M.

For multiplicative characters set T_chi=sum_{t in S_M(q)}chi(t) and

\[
 E_M(q)=\sum_{\chi\ne\chi_0}\chi(-1)T_\chi^2.
\]

As in (A5), the number of ordered incidences, including diagonal ones, is (m^2+E_M(q))/(q-1). This identity and its lifting proof were delivered independently in both attempts.

**Unproved hypothesis H_C(M,C,eta,q_0).** For every prime q>=q_0,

\[
 E_M(q)\ge-Cm q^{1-\eta},\qquad C\ge1,\quad0<\eta\le1.      \tag{C4}
\]

For M>=22, if eta>12/(M+2), this implies digit cap M for every prime q>=q_0 with

\[
 q>\left(C[6(M+1)]^{2-24/(M+2)}\right)^{1/(\eta-12/(M+2))}. \tag{C5}
\]

Indeed X>=sqrt(q)/2: integrality gives q<=(X+1)^2<=4X^2. Equation (C1) gives

\[
 m\ge q^{1-12/(M+2)}/[6(M+1)]^{2-24/(M+2)}.
\]

The onset (C5) makes m>Cq^{1-eta}; hence m^2+E_M(q)>0. It also validates X>3(M+1), since eta-12/(M+2)<=s/2 and C>=1. Thus no additional hidden height-onset condition is required.

One simple choice is M=ceil(24/eta), for which eta-12/(M+2)>eta/2. The stronger sufficient onset

\[
 q>\left(C[6(M+1)]^2\right)^{2/\eta}                       \tag{C6}
\]

then suffices. Specifically eta=2^{-145} gives M=3*2^{148}<2^{150}; eta=2^{-495} gives M=3*2^{498}<2^{500}. The assumed saving must hold at that very alphabet. An unspecified positive exponent depending arbitrarily on M does not verify either inequality.

For the two-digit case, (C3) gives m> C sqrt(q) once q>C^{80}18^{82}. Consequently the unproved hypothesis E_2(q)>=-Cm sqrt(q) implies M=2 beyond that explicit onset and its own hypothesis threshold.

Root clarification: (C4) compares with the uniform main term m^2 and may be stronger than the useful arithmetic statement if the real height restriction produces a different main coefficient. The valid weaker variant

\[
 E_M(q)\ge-(1-\kappa)m^2-Cm q^{1-\eta},\quad0<\kappa\le1,
\]

has exactly the same proof with C replaced by C/kappa in (C5),(C6) and in the two-digit onset. This is an additional conditional deduction, not a claim that either correlation estimate is true. It places C's counting improvement alongside A's explicit allowance for a height bias.

### C.3. Another unconditional logarithmic bound

Independently, C proves the cap floor((2q/(q-1))H_{q-1}) for every prime q, where H_n=sum_{v=1}^n1/v. If a digit b>=B+1 occurs, let u/v be the preceding convergent and h/k the remaining tail. The continuant identities give q=vh+v_prev k and |av-uq|=k, with h>=bk. Thus 1<=k<=q/((B+1)v). Each pair (v,k) accounts for at most two residues a, through av=+/-k mod q. The number of bad a is therefore at most

\[
 2\sum_{v\le q/(B+1)}\left\lfloor\frac q{(B+1)v}\right\rfloor
 \le\frac{2q}{B+1}H_{q-1}.
\]

Taking B=floor((2q/(q-1))H_{q-1}) makes this strictly less than q-1. This is a complete growing-cap result; B's ceil(2 log p) is the cleaner bound for the comparison below.

## Comparison and status

| Attempt | Complete partial result | Precise missing input | Fixed cap conditional on that input |
|---|---|---|---|
| A | Canonically repaired two-digit count exponent 201/200; exact prime lifting | One-sided signed character correlation (A6) | 2, onset (A7) with repaired constant 594 |
| B | Every prime has digit cap ceil(2 log p); exact hyperbola-avoidance criterion | A missing residue from H_{M+1}(p) for all large primes | 2^150 in its stated example; essentially a reformulation |
| C | Count exponent 2-24/(M+2), and two-digit exponent 41/40; exact prime lifting | Height-restricted signed correlation with a quantified saving | Below 2^150 from eta=2^{-145}; or 2 from the stronger two-digit estimate |

C gives the strongest proved counting lemma and the clearest numerical tradeoff between a missing analytic saving and a digit cap. A's one-sided formulation usefully allows a nonuniform real-height main term. Their independently shared incidence reduction confirms the exact-denominator bookkeeping, not the unresolved correlation estimate. B proves an unconditional bound for every prime but its cap grows, and its fixed-cap hypothesis closely restates the target.

No attempt proves any positive saving in the relevant height-restricted correlation. Parseval only gives |E_M(q)|<=(q-1)m-m^2, and congruence expansion without height control does not force denominator exactly q. Thus no route in this report currently supplies an unconditional M<=2^500, M<=2^150, or any other fixed M. The numerical targets are proved implications with unproved premises, not evidence that those premises hold.

All three attacks used only supplied definitions and pre-existing standard mathematics; no web, literature, campaign files, numerical campaigns, or other attempts were consulted by the attacking agents. The root checked the algebra, onset inequalities, continued-fraction convention, ordered-pair identity, and canonical repair while assembling the report. This is a same-model mathematical check, not cross-vendor review or kernel formalization. No paid resources, dependency installation, or external publication occurred; monetary usage was not exposed by the tools.
