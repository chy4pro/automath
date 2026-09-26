OPEN — three transfer criteria and several obstructions are proved below; no criterion has been verified at a useful stage of the actual walks, and no unconditional Zaremba digit bound follows.

# Extending the central E1 estimate to walk measures

Task 018, 2026-09-26. Three distinct agents worked concurrently: S1 on Fourier scalarization, S2 on central envelopes, and S3 on approximate centrality. This task is ordinary integration work, not clean-room work. The prior isolated task019 audit passed the restricted theorem and identified its underlying central-Fourier argument as standard. Root checked the arguments and assembled this report. All costs here are mathematical reasoning and small bookkeeping/source checks; no new numerical campaign, dependency, git operation, or external message was run. STATUS is maintained by root.

The strongest useful implication obtained is a tensor-square bound: a small central pointwise envelope at **one** stage gives a spectral bound directly, with no additive uniform-mass error and no further flattening doublings. This improves the conditional transfer in R2_E1b and task015. The envelope itself remains unproved for the actual useful stages and is quantitatively impossible at their early stages. An all-coset cap alone cannot repair scalarization or imply relative centrality, even for positive Fourier correlations.

Task018's phrase “single gap” is too strong as a certification claim. Even after a useful extension, the exact actual seed and its integer length, coefficients, the downstream assembly, and a full prime onset still need certification. The ledgers below retain those conditions. None is a theorem for an unconditional numerical M.

## 1. Conventions and exact actual measures

Let p>=5 be prime, G=SL2(F_p), D=p(p^2-1), u=1/D, Z={I,-I}, and use counting-measure norms. Write

    t(mu)=||mu-u||_2^2,
    mu~(g)=conjugate(mu(g^-1)),
    muhat(rho)=sum_g mu(g)rho(g).

Convolution is (f*g)(x)=sum_y f(y)g(y^-1 x). Let P denote conjugacy averaging; it is the orthogonal projection onto central functions. All measures in this report are probability measures unless explicitly described as majorants. For a nontrivial irreducible rho put d=d_rho. The inputs audited in [REFEREE_E1](/work/campaigns/zaremba-M/phase1/REFEREE_E1.md) are

    d >= (p-1)/2,
    |chi_rho(g)| <= sqrt(2p) for g outside Z.

The latter follows from column orthogonality and the noncentral centralizer bound 2p. Thus, for every probability measure, including noncentral ones,

    z_rho := tr(muhat(rho))/d,
    |z_rho| <= mu(Z)+q_p(1-mu(Z)),
    q_p=2sqrt(2p)/(p-1) <=5/sqrt(p).                     (1)

For the actual Lemma-14 walk,

    U(t)=[[1,t],[0,1]], V(t)=[[1,0],[t,1]],
    s_j=V(2j)U(-2j), nu=N^-1 sum_{j=1}^N delta_{s_j},
    mu_r=(nu*nu~)^{*r}.                                 (2)

Here r counts alternating pairs; mu_r includes word multiplicities. For Lemma15, nu is uniform on h_(a,b)=U(-b)gU(a) for (a,b) in its specified S subset [N]^2, g_21!=0; its correlations likewise lie in SL2, including when det(g)=-1. The fixed determinant-coset translations in [R2_E1b, B.1](/work/campaigns/zaremba-M/phase1/R2_E1b.md) preserve the relevant correlation Fourier description. Each correlation block is M_rho^r with 0<=M_rho<=I. These actual laws and every positive power are noncentral in the application ranges, as proved in that report. Noncentrality alone is not an obstruction to flattening.

## 2. S1: the exact scalarization gap and a spectral-spread criterion

Plancherel gives

    t(mu)=D^-1 sum_{rho!=1} d_rho ||muhat(rho)||_HS^2,
    t(mu*mu)=D^-1 sum_{rho!=1} d_rho ||muhat(rho)^2||_HS^2.

Consequently, with s(mu)=max_{rho!=1}||muhat(rho)||_op,

    t(mu*mu) <= s(mu)^2 t(mu).                            (3)

Centrality supplies muhat(rho)=z_rho I, so (1) controls s(mu). Without centrality (1) bounds a normalized trace, not the needed operator norm. For positive semidefinite blocks, positivity supplies only z_rho<=||muhat(rho)||_op<=d_rho z_rho.

For a measure with positive semidefinite Fourier blocks define

    L(mu)=max_{rho!=1, muhat(rho)!=0}
           d_rho ||muhat(rho)||_op / tr(muhat(rho)),

and set L=1 if there are no such blocks. Then

    s(mu) <= L(mu)[mu(Z)+5/sqrt(p)],
    t(mu*mu) <= L(mu)^2[mu(Z)+5/sqrt(p)]^2 t(mu).           (4)

This follows directly from the definition, (1), and (3), including when t=0. If

    mu(Z)<=p^-a, L(mu)<=C p^beta, C>=1,
    0<c<min(a-beta,1/2-beta),

then s(mu)<=p^-c, hence t(mu*mu)<=p^-2c t(mu), for

    p>=max{5,(2C)^(1/(a-beta-c)),
               (10C)^(1/(1/2-beta-c))}.                 (5)

Each term in the bound for s(mu) is then at most p^-c/2. At a=1/30,c=1/120 this requires beta<1/40. No such bound has been proved for the actual walks.

Powering cannot improve this particular spectral-shape parameter. For a nonzero positive block M with eigenvalues lambda_i and largest eigenvalue lambda_max,

    L_rho(r)=d ||M^r||_op/tr(M^r)
             =d / sum_i (lambda_i/lambda_max)^r.          (6)

This is nondecreasing in r, and tends to d divided by the multiplicity of lambda_max. This observation concerns relative eigenvalue spread; absolute norms can still decrease.

### A full-coset counterexample to the unchanged E1 bracket

Let U be the upper-unipotent subgroup, let u_U=1_U/p, and fix 0<a<1/2. Set w=p^-a/2 and

    mu=(1-w)u+w u_U
       =nu*nu~, nu=(1-sqrt(w))u+sqrt(w)u_U.              (7)

Every proper subgroup H has [G:H]>= (p+1)/2: remove the constants from its coset permutation representation and use the irreducible-degree bound. Thus every proper coset C satisfies

    mu(C)<=2/(p+1)+w<=p^-a when p^(1-a)>=4.              (8)

Since u_U is convolution-idempotent,

    t(mu)=(1/4)p^(-1-2a)[1-1/(p^2-1)],
    t(mu*mu)/t(mu)=(1/4)p^-2a.                          (9)

But U intersect Z={I}, so mu(Z)=2(1-w)/D+w/p<=1/p and

    [mu(Z)+5/sqrt(p)]^2<=36/p.

The actual ratio in (9) exceeds this bracket if p^(1-2a)>144. This refutes extension of the unchanged center-mass bracket to all-coset-nonconcentrated correlations. The example lies in p^(-2+2c)<=t(mu)<=p^-h0 whenever h0<=1+2a, a+c<1/2, and p^(1-2a-2c)>=32/7. In particular a=h0=1/30,c=1/120,p>=2^40 meet all these conditions.

It does **not** refute the desired gain p^-2c for c<a: (9) already satisfies that gain.

In the dimension-p Steinberg constituent of the doubly transitive action on P1, U has a one-dimensional fixed space (there are two U-orbits on P1). Thus muhat=w times a rank-one projection, z=w/p, and L_rho=p. More generally any comparison s(mu)<=A(p)[mu(Z)+5/sqrt(p)] on this family requires A(p)>=p^(1/2-a)/12. A subpolynomial loss in the unchanged scalar bound is therefore impossible under these hypotheses alone.

### An unconditional low-energy estimate

For every probability measure,

    t(mu*mu)<=min{t(mu),2p(p+1)t(mu)^2}.                 (10)

Young proves the first term. For the second, put S_rho=||muhat(rho)||_HS^2, use ||muhat(rho)^2||_HS^2<=S_rho^2, and bound sum d S_rho^2 by (sum d S_rho)^2/d_min. Thus p^-2c contraction is unconditional once t(mu)<=p^-2c/[2p(p+1)]. This supplies no bridge from the original endpoint p^(-2+2c) to below p^-2.

## 3. S2: a tensor-square envelope theorem

Define the least central pointwise majorant F and its mass by

    F(g)=max_{x conjugate to g} mu(x),
    B(mu)=sum_g F(g).

Equivalently, B is the least possible L for which mu<=L sigma with sigma a central probability measure. Indeed every such L sigma dominates F and has mass L, whereas sigma=F/B realizes equality. Also F(Z)=mu(Z), where the notation means summed mass on the two singleton classes.

**Theorem.** For arbitrary probability mu on SL2(F_p), p>=5,

    s(mu)^2 <= mu(Z)+5B(mu)/sqrt(p),                     (11)
    t(mu*mu) <= [mu(Z)+5B(mu)/sqrt(p)] t(mu).             (12)

No symmetry, positivity of Fourier blocks, or energy cutoff is required.

**Proof.** Fix a nontrivial unitary irreducible rho of dimension d and unit vectors v,w. Jensen and mu<=F give

    |sum_g mu(g)<rho(g)v,w>|^2
      <=sum_g mu(g)|<rho(g)v,w>|^2
      <=sum_g F(g)|<rho(g)v,w>|^2.                       (13)

Use rho tensor conjugate(rho) on V tensor conjugate(V). Its invariant line is generated by Omega=d^-1/2 sum_i e_i tensor conjugate(e_i); Schur's lemma gives exactly one copy. The invariant components of v tensor conjugate(v) and w tensor conjugate(w) both have coefficient d^-1/2 along Omega. Since F is central, its operator on this line is B, and its operator on every nontrivial irreducible constituent tau is scalar with modulus at most

    F(Z)+q_p[B-F(Z)] <=mu(Z)+q_p B.

The two complementary vectors have norm at most one. The right side of (13) is therefore at most

    B/d+mu(Z)+q_p B
      <=mu(Z)+B(2+2sqrt(2p))/(p-1)
      <=mu(Z)+5B/sqrt(p).                               (14)

For the last inequality, multiplying by sqrt(p) gives
2sqrt(p)/(p-1)+2sqrt(2)p/(p-1); both summands decrease for p>1, and their sum at p=5 is less than 5. Supremize over v,w and apply (3). This proves (11) and (12). QED.

The theorem improves the earlier envelope transfer's additive term (B^2-1)/D: there is no additive floor here. It pays one power rather than two in the bracket, but one useful envelope stage already supplies a direct spectral saving.

If

    mu(Z)<=p^-a, B(mu)<=C p^beta, C>=1,
    0<2c<min(a,1/2-beta),

then s(mu)<=p^-c and t(mu*mu)<=p^-2c t(mu) whenever

    p>=max{5,2^(1/(a-2c)),
                 (10C)^(1/(1/2-beta-2c))}.              (15)

For the concrete parameters a=1/30, beta=9/20, c=1/120,

    p>=max{5,2^60,(10C)^30}                             (16)

suffices. The bound B<=Cp^(9/20) at an actual useful stage has not been proved. In particular (16) is not a Zaremba onset.

The prior support and integer-lift obstructions remain valid. If the support has size at most R, then

    B(mu)>=(p^2-1)[1-mu(Z)]/(2R).                       (17)

For the actual correlations with n generator points and no opposite pair, mu_r(Z)<=1/n: Fourier inversion over representations on which -I acts trivially expresses this mass as a sum of traces of positive blocks M^r, decreasing with r. Consequently the MMS seed m0<=(1/20)log_N p has B of order at least p^(19/10), and the appendix seed bound m0<=(1/4)log_N p gives at least p^(3/2). The explicit integer-lift argument in R2_E1b further gives B>>_epsilon p^(1-2epsilon) while that lift condition holds. These are lower bounds, and exclude beta<1/2 at those stages.

### A sharper obstruction without an integer-lift restriction

For the actual Lemma14 law, 2<=N<p and every r>=1,

    B(mu_r)>=(1-1/N)(p^2-1)/(4r N^(2r-1)).              (17a)

To prove this, write a length-2r alternating word as

    W=s_(i1)s_(j1)^-1 ... s_(ir)s_(jr)^-1.

Each pair equals V(2i)U(2(j-i))V(-2j). Merge adjacent V factors and, using cyclic invariance of trace, the final and initial V factors. The trace is thus a polynomial of total degree at most 2r in the 2r indices. For any target tau, tr(W)-tau is a nonzero polynomial: setting all indices except i1,j1 formally to zero leaves 2-4(i1-j1)^2-tau, nonzero in odd characteristic. The elementary grid polynomial bound gives at most 2r N^(2r-1) tuples of any prescribed trace. One proves that bound by induction on the number of variables, separating zeros of the leading coefficient in the last variable from the remaining slices, which have at most its degree many roots.

Every conjugacy class has fixed trace, so its support occupancy is at most 2r N^(2r-1), including when many tuples collide. Divide its probability mass by this occupancy to bound its maximum atom, multiply by the minimum noncentral class size (p^2-1)/2, and sum. The already proved mu_r(Z)<=1/N gives (17a). Thus an envelope B(mu_r)<=Cp^beta necessarily requires

    N^(2r-1)>=(1-1/N)(p^2-1)/(4Cr p^beta).              (17b)

This also disposes of small central minorants at stages where 2r N^(2r-1)<(p^2-1)/2. Each noncentral class then has a missing support point. Any central 0<=F_minus<=mu_r must vanish on that entire class, so its mass is at most mu_r(Z)<=1/N. A normalized nonzero such minorant is supported on Z and acts as the identity in representations factoring through PSL2. It supplies no general spectral contraction.

### Four doublings fail in an actual capped family

Take N=floor(p^(1/25)) and m0=1. This satisfies the MMS length bound m0<=(1/20)log_N p. At the explicit large onset below, the right side is between 1 and 2, so its only possible positive integer seed length is 1. Four doublings give r=16. Equation (17a), N<=p^(1/25), 1-1/N>=1/2, and 1-p^-2>=24/25 yield

    B(mu_16)>=(3/400)p^(19/25).                         (17c)

Consequently B(mu_16)<=Cp^(9/20), for any fixed C, fails when p>(400C/3)^(100/31).

Here is a source-checked verification that these actual laws satisfy the full cap at a=1/30. The needed prime-field subgroup classification says that a proper subgroup of size greater than 120 is contained in a Borel or in the normalizer of a maximal torus. Root verified the exact statement in [Helfgott, Growth in SL3(Z/pZ), Proposition8.3, p830](https://ems.press/content/serial-article-files/31776#page=70). S2 initially left this as a standard but unverified input; this source check closes that specific dependency.

For nonzero projective vectors (u,v) and (w1,w2), the condition that s_j maps the first line to the second is

    w2(u-2jv)-w1(2ju+v-4j^2 v)=0.                       (17d)

This polynomial has degree at most two and is nonzero: its quadratic coefficient would force w1 v=0, and in either case simultaneous vanishing of the other coefficients would force one representing vector to be zero. The argument is valid over F_(p^2) as well. A Borel coset therefore contains at most two generators. A torus coset contains at most two, by fixing an eigenline over F_(p^2); a torus-normalizer coset is a union of at most two such cosets, so contains at most four. A remaining subgroup has order at most 120 and hence at most 120 generators in any coset. Thus

    nu(xH)<=120/N

for every proper-subgroup coset. Such a uniform coset cap persists under convolution with any probability measure on either side: translations on the other side can be rewritten as cosets of conjugate subgroups. It therefore holds for all mu_r.

For p>=240^150, N>=p^(1/25)/2 and

    mu_r(xH)<=240 p^(-1/25)<=p^(-1/30).                 (17e)

This onset also ensures (1/20)log_N p<2: use log N>=log(p)/25-log 2 and log(p)>(200/3)log 2. Combining (17c)-(17e) proves that four doublings cannot uniformly establish the illustrative envelope among actual capped MMS-admissible seeds. It does not exclude five or more doublings. In particular a formal earlier d=4 ledger must not be promoted to a proved entry time.

### Eventual envelope with an explicit, but p-dependent, delay

There is an elementary eventual bound that illustrates why finiteness is not the needed uniform statement. Suppose nu is uniform on n points in one determinant coset and the support of mu_1=nu*nu~ generates G. A cap strictly below 1 at any positive power implies this generation assumption. Each positive atom of mu_1 is at least n^-2. Set

    delta=1/[n^2(D-1)^2].

Every nontrivial eigenvalue lambda of a correlation block lies in [0,1-delta]. For a unit eigenvector v,

    sum_s mu_1(s)||rho(s)v-v||^2=2(1-lambda).

Thus each support generator moves v by at most n sqrt(2(1-lambda)). Since the support is symmetric and generates G, every element has a word of length at most D-1. The triangle inequality bounds its displacement by (D-1)n sqrt(2(1-lambda)). Averaging the square over G gives 2 on the left, because this representation has no invariant vector, and proves the stated gap. Fourier inversion now gives

    |mu_r(g)-1/D| <= (D-1)(1-delta)^r/D,
    B(mu_r)<=1+(D-1)(1-delta)^r.

In particular

    r>=R=ceil(n^2(D-1)^2 log(D-1)) implies B(mu_r)<=2.   (17f)

One may take d=max(0,ceil(log2(R/m0))) to reach this stage by doubling. This displayed sufficient delay grows with p; substituting it into a spectral/alphabet ledger does not prove an absolute digit bound. The useful assertion would require a prime-independent delay and explicit envelope constants.

## 4. S3: the precise relative-centrality criterion

Put sigma=Pmu, Delta=||mu-sigma||_2, t=t(mu), and q=mu(Z)+5/sqrt(p). Then, for arbitrary probability mu,

    sqrt(t(mu*mu))<=q sqrt(t)+Delta.                     (18)

Indeed, sigma has nontrivial Fourier scalars of modulus at most q, and

    mu*mu-u = sigma*(mu-u)+mu*(mu-sigma).

The first term has norm at most q sqrt(t); Young bounds the second by Delta. Thus a sufficient condition is Delta<=(p^-c-q)sqrt(t), with q<=p^-c.

For symmetric mu one has the stronger proved estimate

    t(mu*mu)<=q^2 t+(1+2q+2q^2)Delta^2.                 (19)

To prove it, diagonalize each Hermitian block M with eigenvalues lambda_i in [-1,1], and let z=tr(M)/d. Its central projection is zI and |z|<=q. The exact identity

    lambda^4=z^2 lambda^2+2z^3(lambda-z)
              +(lambda-z)^2(lambda^2+2z lambda+2z^2)

and sum_i(lambda_i-z)=0 give

    tr(M^4)<=q^2 tr(M^2)+(1+2q+2q^2)||M-zI||_HS^2.

Sum by weighted Plancherel to prove (19). When t=0 all statements are trivial; otherwise the necessary scale of the sufficient distance estimate is explicit:

    Delta^2 <= [p^-2c-q^2]t/(1+2q+2q^2).                (20)

In particular, at a>=1/30,c=1/120,p>=2^40, the hypotheses

    mu(Z)<=p^-a,
    Delta<= (1/2)p^-c sqrt(t)                            (21)

imply coefficient-one gain p^-2c. In fact q<=0.51p^-c: p^(-(a-c))<=1/2 and 5p^(-(1/2-c))<1/100. Equation (19) then has coefficient at most

    2601/10000 + (1/4)(1+102/100+5202/10000)
      =17903/20000<1.

The same reasoning works at a=1/24,p>=2^30. On the ledger's range t>=p^(-2-4c), an absolute bound Delta<=(1/2)p^(-1-3c) would suffice. Merely Delta tending to zero does not suffice. None of these distance estimates is proved for the useful actual walk stages.

### A counterexample to relative centrality at every power

Use (7), now allowing 0<a<1. The full-coset and correlation conclusions still hold for p>=max{5,4^(1/(1-a))}. Every positive integer r satisfies

    mu^{*r}=(1-w^r)u+w^r u_U.

The conjugacy average Pu_U equals 1/p at I, equals 1/[p(p+1)] on each of the two nonidentity trace-two classes, and is zero elsewhere. Each such class has size (p^2-1)/2 and meets U in (p-1)/2 points. Therefore

    ||u_U||_2^2=1/p, ||Pu_U||_2^2=2/[p(p+1)],
    t(u_U)=(p^2-2)/D,
    ||u_U-Pu_U||_2^2=(p-1)^2/D.

Orthogonality, or direct subtraction, gives for every r>=1

    ||mu^{*r}-Pmu^{*r}||_2^2/t(mu^{*r})
      =(p-1)^2/(p^2-2).                                 (22)

This tends to one and is independent of r. Since P is the orthogonal projection, no other central measure is closer in L2. Thus even an arbitrarily large positive power cannot ensure relative centrality from the all-coset cap alone. Absolute closeness can improve, and this example already flattens: its energy ratio at a doubling is w^(2r).

The obstruction also occurs within the needed energy range. Here

    t(mu^{*r})>= (1/2)4^-r p^(-1-2ar).

For a=1/30,c=1/120 and fixed 1<=r<=15, it lies in p^(-2-4c)<=t<=p^-a whenever p^((31-2r)/30)>=2*4^r. This is not solely a below-threshold phenomenon.

### Actual initial laws and bounded powers

If rho has support S meeting each noncentral class in at most a fraction theta of that class, classwise Cauchy-Schwarz proves

    ||rho-Prho||_2^2>=(1-theta)sum_{g outside Z}rho(g)^2. (23)

For rho=nu*nu~ with nu uniform on n>=2 distinct points with no opposite pair, rho(I)=1/n,rho(-I)=0, and the noncentral support size is at most n(n-1). Its noncentral squared mass q_nc is at least (n-1)/n^3. Since each noncentral class has size at least (p^2-1)/2, (23) yields

    ||rho-Prho||_2^2/t(rho)
      >=[1-2n(n-1)/(p^2-1)]_+ (n-1)/(2n-1).             (24)

Indeed t<=q_nc+1/n^2, and q_nc/(q_nc+1/n^2) is increasing in q_nc. For Lemma14, n=N; for Lemma15, n=|S|<=N^2. At the assembly scale N=p^(2epsilon),epsilon<1/18, both n=o(p), so (24) prevents a vanishing relative-distance estimate at the first correlation. For Lemma14 the relation tr(x)=2-x_12^2 gives the sharper occupancy theta<=4N/(p^2-1): a noncentral trace admits at most two nonzero differences i-j and N pairs per difference.

There is a bounded-power obstruction for Lemma14 while

    N>=2, (2N+1)^(2r+1)<p.                              (25)

Let C_r=binom(2r,r)/(r+1). Then

    ||mu_r-Pmu_r||_2^2/t(mu_r)
      >=[1-2N^(2r)/(p^2-1)]/(4C_r^2+1)
      >=1/[2(4C_r^2+1)].                                (26)

Here are the needed group and counting details. Set A=U(2), B=V(2). Nonzero powers of A map |y|>|x| into |x|>|y|; nonzero powers of B map the latter into the former. Ping-pong gives a free group on A,B. With T=BA^-1, B,T are also a free basis. The elements T_j=B^(j-1)TB^(-(j-1)) freely generate: expanding a reduced word leaves nonzero intervening B powers between distinct adjacent indices. Since s_j=T_j T_(j-1)...T_1, the triangular inverse substitutions T_j=s_j s_(j-1)^-1 show that s_1,...,s_N freely generate as well (s_0=I).

The height estimate in (25), proved in R2_E1b, bounds every entry in the alternating length-2r integer word by a number strictly less than p. Reduction to I therefore forces both off-diagonal entries to vanish; determinant one forces both diagonal entries to be 1 or both -1, and reduction distinguishes the signs. Reduction to -I similarly forces the integer matrix -I, excluded by freeness and torsion-freeness. A freely trivial alternating word of length 2r admits a noncrossing cancellation pairing; there are C_r pairings and at most N^r labels per pairing. Thus

    mu_r(I)<=C_r N^-r, mu_r(-I)=0.

Also ||mu_r||_infinity<=||mu_1||_infinity=1/N. Its noncentral mass is at least 1-1/N and its support has at most N^(2r) points. Its central squared mass is at most C_r^2 N^(-2r), whereas its noncentral squared mass is at least (1-1/N)^2 N^(-2r). Their ratio gives at least 1/(4C_r^2+1) noncentral share. Apply (23). Condition (25) implies N^(2r)<p, hence 2N^(2r)/(p^2-1)<1/2, completing (26). In particular r=2 gives a lower bound 1/34 when (2N+1)^5<p.

For each fixed R this rules out relative p^-c closeness for r<=R in the indicated lift range as p grows. It does not cover arbitrary later powers, growing r without its Catalan loss, or arbitrary Lemma15 data.

## 5. Conditional spectral and alphabet ledgers

Let the actual identified seed have length m0<=b log_N p. If a useful stage is mu=(nu*nu~)^{*m} with m=2^d m0, d counts extra seed doublings exactly once. The singular norm s(nu) then obeys s(mu)=s(nu)^(2m).

Both (4)-(5) and (11)-(15) give the **operator** bound s(mu)<=p^-c, not just energy flattening. Therefore either criterion at one such stage directly implies

    s(nu)<=p^(-c/(2m))<=N^(-kappa14),
    kappa14=c/(2b*2^d).                                 (27)

No later flattening stages are needed: k=0 after that useful stage. This avoids unnecessarily applying the task015 iteration ledger to a stronger spectral premise. Neither the required spectral-spread nor envelope premise has been proved for a useful actual stage.

For comparison, S3's relative-distance criterion yields energy contraction only. If it holds at every required dyadic stage after a justified delay d, throughout t>=p^(-2-4c), the exact all-coset cap supplies h0=a. At a=1/30,c=1/120,

    gamma=2c=1/60,
    k=ceil((2-h0)/gamma)+1=119,
    v=h0+k gamma-2=1/60,
    kappa14=v/(4b*2^(119+d))=1/(240b*2^(119+d)).          (28)

This is the native p-scale gain, not a K-scale same-numeral substitution. A bound at only one stage does not justify these 119 iterations. If an iterate falls below the lower cutoff, ordinary contraction preserves a sufficient stronger bound.

Use the exact overhead conventions of [task015](/work/campaigns/zaremba-M/phase1/E1_normalization_certified_M.md): O_B=705672/25 is a limiting overhead with epsilon approaching 1/18. Its limiting log2 alphabet threshold is log2(O_B/kappa14). The admissible concrete choices R=40,epsilon=1/20 instead give O_B=31680 and the strict integer rule

    M0>198/kappa14, M=160 M0

in the inverse-gap-dominated rows below. The stated integer M0 exceeds this threshold by one; smaller auxiliary alphabet bounds are then automatic.

| Conditional input, c=1/120 | Original seed coefficient b | Further flattening k | Limiting log2 threshold | Concrete integer cap |
|---|---:|---:|---:|---:|
| One useful S1 or S2 stage | 1/20 | 0 | 18.369744553+d | M=380160*2^d+160 <2^(19+d) |
| One useful S1 or S2 stage | 1/4 | 0 | 20.691672647+d | M=1900800*2^d+160 <2^(21+d) |
| S3 at all required stages | 1/20 | 119 | 137.369744553+d | M=380160*2^(119+d)+160 <2^(138+d) |
| S3 at all required stages | 1/4 | 119 | 139.691672647+d | M=1900800*2^(119+d)+160 <2^(140+d) |

For example, the first row uses kappa14=1/(12*2^d), M0=2376*2^d+1. The second uses kappa14=1/(60*2^d), M0=11880*2^d+1. These are conditional arithmetic outputs, not newly certified alphabets. The b=1/20 and b=1/4 conventions have distinct seed requirements and cannot be exchanged silently. A non-dyadic entry power q costs log2(q), or may conservatively be charged d if q<=2^d.

The onset still includes validity of the actual seed and useful-stage hypothesis, the explicitly displayed transfer onset, and every downstream assembly coefficient and onset. No numerical value for that maximum is established here.

## 6. What is established and what remains

S1 identifies the precise failure of scalarization, proves a spectral-spread extension, and gives an admissible rank-one Fourier obstruction to a small formal loss. S2 proves a tensor-square envelope extension with no energy cutoff. S3 proves two perturbative transfers and rules out the required relative centrality from nonconcentration alone, as well as at the actual early stages described above. None disproves the target c=1/120 flattening estimate for general nonconcentrated walk laws.

The next useful mathematical input must exploit the actual later walks: a proved small envelope or spectral-spread estimate at a charged stage, a sufficiently strong relative-distance estimate at every necessary stage, or a direct noncentral energy inequality. Repeating the restricted central theorem or presuming a fixed delay supplies none of those inputs. No full effective M or original conjecture is claimed solved.
