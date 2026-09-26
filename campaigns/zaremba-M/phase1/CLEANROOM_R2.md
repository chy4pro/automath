OPEN — c=1/468 and c=1/120 remain unresolved. The target c=1/40 is disproved at tau=1/24 by an explicit family satisfying every nonempty admissible h-range.

# Three clean-room attempts at the R2 inequality

Task009, 2026-09-26. Three agents were started with fresh contexts and the exact supplied mathematical statement. They received no papers, route reports, other agents' mathematics, or web results. Attempts B and C accessed no workspace mathematics. Attempt A reported reading the mandatory OPERATIONS governance entry point before receiving the explicit no-file constraint; it read no campaign or proof material. This limited procedural departure is disclosed rather than describing A as literally receiving only the problem text. All three attempts are same-vendor work, and root checked their arguments after completion. Nothing here is kernel formalized.

The supplied task uses the coset exponent tau itself, not tau/6. In this report fix tau=1/24 when evaluating the three numerical targets.

| Attempt | Complete output | Limitation |
|---|---|---|
| A | Explicit counterexample for tau/2<c<(1-tau)/2, at E(mu)=p^(-2+2c), for every h<=2-2c | Does not refute c=1/120 or 1/468 |
| B | Universal constant contraction E(mu*mu)<0.991582 E(mu), under the target hypotheses for large p | A constant contraction is not p^(-2c) for fixed positive c |
| C | Independent random-support obstruction c>tau/2 when h<tau; exact return-atom lower bound | Its construction alone does not cover larger h |

The strongest justified conclusion is to remove c=1/40 as a target under these hypotheses, retain the two smaller targets as OPEN, and preserve h explicitly. No Zaremba bound follows from these results alone. The two counterexamples were found independently; the agents were not told of each other's findings.

## 1. Conventions and standard group facts

Let G=SL2(F_p), D=|G|=p(p^2-1), and u_G=1/D. Norms use counting measure. Convolution is (f*g)(x)=sum_y f(y)g(y^(-1)x), and check f(x)=f(x^(-1)) for real measures. Write E(mu)=||mu-u_G||_2^2.

The standard subgroup-classification consequences used below, valid for prime p>=13, are stated explicitly:

- A proper subgroup with order divisible by p is contained in a Borel subgroup (a point stabilizer in P1(F_p)).
- Proper subgroups not contained in Borels have order prime to p. Maximal possibilities are torus normalizers of orders 2(p-1), 2(p+1), or exceptional groups of orders at most 120; some types are absent at some primes.
- Every proper subgroup therefore has order at most p(p-1), hence index at least p+1.

These are permitted standard inputs, not proved classification theorems in this report. No literature was searched in the clean-room attempts. All deductions below are given explicitly.

## 2. Attempt A: counterexample at the lower energy endpoint

**Proposition.** Fix 0<tau<1/2, tau/2<c<(1-tau)/2, and 0<h<=2-2c. For all sufficiently large primes p there is a symmetric probability measure satisfying

    mu(gH)<=p^(-tau) for every proper subgroup H and every left coset,
    E(mu)=p^(-2+2c),
    E(mu*mu)/E(mu)>=p^(-tau)/4096>p^(-2c).

A sufficient explicit onset for the construction and strict failure is

    p > max(32, 64^(1/(1-tau-2c)), 4096^(1/(2c-tau))).          (2.1)

Thus at tau=1/24, c=1/40 fails for every admissible h<=39/20. For example p>2^1440 is sufficient. The onset is only a sufficient bound for this counterexample, not optimized.

**Construction.** Put a=1-tau-2c>0, r=ceil(p^tau), and let m be the largest odd integer at most p^a/16. Under (2.1),

    p^a/32 <= m <= p^a/16,       p^tau <= r <= 2p^tau.

Choose a generator q of F_p^*, let

    S={q^j: -(m-1)/2 <= j <= (m-1)/2},
    U={u(v)=[[1,v],[0,1]]:v in F_p},
    d(s)=[[s,0],[0,s^(-1)]],
    A={u(v)d(s):v in F_p, s in S}.

Then |S|=m, S=S^(-1), |SS|<=2m-1. Since the diagonal subgroup normalizes U, A=A^(-1), |A|=pm, and A^2 has size at most 2pm. Let xi be uniform on A. It is symmetric and Cauchy–Schwarz gives

    ||xi*xi||_2^2 >= 1/(2pm).                                 (2.2)

Choose distinct finite t_1,...,t_r and x_i=[[t_i,-1],[1,0]], and let nu_X be uniform on these r matrices. Define

    mu0=(nu_X*xi + xi*check(nu_X))/2.

This is symmetric. Set P=rpm. The sets x_i A lie in distinct x_i B_infinity because x_i(infinity)=t_i. Thus ||nu_X*xi||_2^2=1/P. Convexity gives an upper bound on ||mu0||_2^2, while its support has at most 2P elements and gives a lower bound:

    1/(2P) <= ||mu0||_2^2 <= 1/P.                             (2.3)

**Every proper-subgroup coset is controlled.** A Borel coset is an action fiber {g:g(z)=w}. Under xi, infinity is fixed and every finite input has a uniform image in F_p: conditional on s, u(v)d(s) acts by x -> s^2 x+v with v uniform. Hence:

- delta(x_i)*xi sends infinity to t_i, and a finite input uniformly to P1 minus {t_i};
- xi*delta(x_i^(-1)) sends t_i to infinity, and every other input uniformly to F_p.

The distinctness of the t_i therefore implies

    mu0{g:g(z)=w} <= max(1/p, 1/(2r)+1/(2p)) <= p^(-tau).     (2.4)

This covers subgroups contained in any Borel. If H has order prime to p, any bUd intersects any gH in at most one point: two intersection points would give a nonidentity element of d^(-1)Ud in H, of order p. The measure mu0 is an average of 2rm uniform measures on sets bUd of size p. Therefore mu0(gH)<=1/p<=p^(-tau). These arguments handle all left cosets, not just H itself.

**Inverse pairs retain energy.** Positivity and the diagonal terms give

    check(nu_X)*nu_X >= delta_e/r,
    mu0*mu0 >= (xi*xi)/(4r).

Consequently, by (2.2),

    E(mu0*mu0) >= 1/(32r^2pm)-1/D = 1/(32rP)-1/D.             (2.5)

Write L=p^(-2+2c). The choices of r,m yield

    p^(2-2c)/32 <= P <= p^(2-2c)/8.

Thus E0=E(mu0) satisfies

    3L <= E0 <= 32L,                                          (2.6)

because 1/(2P)>=4L and 1/D<=L. Also 64rP<=16p^(2+tau-2c)<=D under (2.1): 2c>tau and p>32 suffice since D>=p^3/2. Equations (2.3) and (2.5) now imply

    E(mu0*mu0)/E0 >= 1/(64r).                                 (2.7)

**Match the precise endpoint.** Set t=sqrt(L/E0) and

    mu=(1-t)u_G+t mu0.

Equation (2.6) gives 1/32<=t^2<=1/3. Uniform measure assigns every proper coset mass at most 1/(p+1)<=p^(-tau), so the mixture preserves (2.4). It is symmetric. Centering and convolution give exact identities

    E(mu)=t^2 E0=L,
    E(mu*mu)=t^4 E(mu0*mu0).

Using (2.7) and r<=2p^tau,

    E(mu*mu)/E(mu) >= 1/(2048r) >= p^(-tau)/4096.

The last quantity exceeds p^(-2c) by (2.1). The upper energy condition follows from h<=2-2c. If h>2-2c the original interval p^(-2+2c)<=E<=p^(-h) is empty. This completes the proof for every nonempty admissible h-range in the proposition.

At tau=1/24,c=1/40, 2c-tau=1/120, a=109/120, and 4096^(1/(2c-tau))=2^1440. No unspecified coefficient is hidden in the contradiction.

## 3. Attempt B: a complete constant-contraction theorem

**Proposition.** In any finite group of order D, let mu be a symmetric probability measure. Put s=sqrt(2/3). If every proper-subgroup coset has mass at most s and M=||mu||_2^2>1/(sD), then

    E(mu*mu) <= rho E(mu),    rho=(7+2sqrt(6))/12<0.991582.    (3.1)

**Proof.** Let r=mu*mu, Q=||r||_2^2, delta=1-Q/M, and

    d(g)=||L_g mu-mu||_2/sqrt(M),     L_g mu(x)=mu(g^(-1)x).

Symmetry gives <L_g mu,mu>=r(g), so 0<=r(g)<=M and

    d(g)^2=2-2r(g)/M,
    sum_g r(g)d(g)^2=2delta.                                 (3.2)

Translations are isometries, hence d(g^(-1))=d(g) and d(gh)<=d(g)+d(h). Suppose delta<delta0=(1-s)^2/4. Put t=(1-s)/2 and A={g:d(g)^2<=t}. Equation (3.2) implies

    r(A)>=1-2delta/t>s,        |A|>s/M.

A is symmetric and contains e. For g in A^2, d(g)^2<=4t and r(g)>=(1-2t)M=sM. Thus

    |A^2|<=1/(sM)<|A|/s^2=3|A|/2.                           (3.3)

Here is the elementary subgroup step. For x=a^(-1)b in A^2,

    |A intersect xA|=|aA intersect bA|>=2|A|-|A^2|>|A|/2.

For x,y in A^2, the two subsets A intersect xA and A intersect yA intersect. Writing a common element xa=yb gives x^(-1)y=ab^(-1) in A^2. Hence H=A^2 is a subgroup. It is proper, since otherwise r(g)>=sM on G would imply 1>=DsM, contrary to the hypothesis. But

    r(H)=sum_x mu(x)mu(x^(-1)H)<=s,

whereas r(A)>s and A is contained in H. Contradiction. Therefore delta>=delta0, and

    E(mu*mu)<= (1-delta0)M-1/D
             = (1-delta0)E(mu)-delta0/D
             <= rho E(mu).

This proves (3.1).

Under the supplied SL2 hypotheses, p^(-tau)<=s for all large p, and D M>=D E(mu)>=p^(1+2c)(1-p^(-2)) tends to infinity, so the theorem applies. However rho is constant: it does not give p^(-2c) for any fixed c>0 as p grows. Iterating a constant contraction a number of times proportional to log p does not establish the requested *one-convolution* theorem.

Attempt B also independently found the weaker subgroup-mixture ceiling c<=tau: with b=1/(p+1), epsilon=p^(-tau), a=(epsilon-b)/(1-b), and H proper, mu=a u_H+(1-a)u_G has every proper-coset mass at most epsilon and exact ratio E(mu*mu)/E(mu)=a^2. Taking H=U gives E(mu) asymptotic to p^(-1-2tau). This does not rule out the task's three numerical targets, but all constants and conventions match the construction.

## 4. Attempt C: return atom and independent random-support counterexample

For f=mu-u_G, symmetry gives (f*f)(e)=||f||_2^2=E(mu), and sum(f*f)=0. Cauchy–Schwarz on the remaining D-1 coordinates therefore yields the exact universal lower bound

    E(mu*mu)>=D/(D-1) E(mu)^2.                               (4.1)

Thus the target itself would force E(mu)<p^(-2c). Coset non-concentration alone does not enforce that when 2c>tau.

Here is an independent existence proof at tau=1/24. Choose n=ceil(12p^tau) independent uniform X_i in G and set

    mu=(1/(2n)) sum_i (delta(X_i)+delta(X_i^(-1))).

Every maximal proper subgroup of SL2(F_p) is generated by two elements. For Borels and torus normalizers this follows directly from the types in §1. The exceptional projective groups A4,S4,A5 have two generators; their lifts generate the full preimage, because otherwise the lift subgroup would embed the projective group, impossible since those groups have multiple involutions while SL2(F_p) has only one nonidentity involution, -I. Maximal proper subgroups contain the center; a proper supplement to the center would similarly embed PSL2(F_p), which is impossible. Hence there are at most D^2 maximal subgroups and D^3 of their cosets.

For a fixed maximal-subgroup coset C, each event X_i in C union C^(-1) has probability at most 2/(p+1). The probability that any such coset is hit by twelve distinct sample indices is at most

    D^3 * binom(n,12) * (2/(p+1))^12
    <= 26^12 p^(9+12tau-12)=26^12 p^(-5/2),                  (4.2)

using n<=13p^tau. If this bad event fails, each coset has mass at most 11/n<p^(-tau); each index can contribute at most 1/n even if both inverse points lie in the coset. All smaller subgroup cosets are covered by containment.

The probability that the 2n sampled inverse points are not all distinct is at most (n^2+n)/D: a self-inverse sample is I or -I, and cross-sample inverse/equality collisions have the indicated union bound. This also tends to zero. Therefore for every sufficiently large prime a choice avoids both bad events. Its energy obeys

    p^(-tau)/52 <= E(mu)=1/(2n)-1/D <= p^(-tau)/24.            (4.3)

For any fixed 0<h<tau and tau/2<c<1-tau/2, these measures satisfy both energy bounds for sufficiently large p. Equations (4.1) and (4.3) give ratio at least p^(-tau)/52>p^(-2c). At tau=1/24 this independently refutes c=1/40 when h<1/24. Attempt A supplies the additional arbitrary-admissible-h construction; the random argument alone does not.

## 5. The elementary positive route stops at the wrong norm scale

Both B and C derive the same representation-theoretic bound. The standard minimum dimension of a nontrivial complex irreducible representation of SL2(F_p), p>=5, is at least (p-1)/2. With unnormalized Fourier transforms and counting norms, Plancherel gives

    E(mu*mu)<= (D/d_min) E(mu)^2 <= 2p(p+1) E(mu)^2.           (5.1)

Indeed each nontrivial Fourier block has squared Hilbert–Schmidt norm at most D E(mu)/d_min, and ||F^2||_HS^2<=||F||_HS^4. Summing gives (5.1). Young's inequality also gives E(mu*mu)<=E(mu).

To derive the target from (5.1) would require E(mu)<=p^(-2c)/(2p(p+1)), a scale of p^(-2-2c), while the supplied lower endpoint is p^(-2+2c). Thus (5.1) is weaker than ordinary contraction throughout the requested range. No rearrangement of the same inequality can turn it into the desired exponent.

The complete positive output is the constant contraction (3.1). A positive polynomial contraction at 1/468 or 1/120 remains an unproved step. The report does not infer that no such theorem exists, and does not claim a smaller Zaremba M.

## 6. Review and coordination record

Root checked the subgroup-coset formulas, all support sizes, the exact centered-mixture identities, the explicit onset (2.1), the small-doubling subgroup argument, and the random-set union bound. No finite computation was used as proof. No source searches, dependency installations, SAT calls, publication actions, or paid compute were used for these three mathematical attempts. The shared-session mathematical content from other routes was available to root but was never supplied to the clean-room agents. The first counterexample was sent to the coordinator only after root checked it and while explicitly withholding it from the other clean-room agents.
