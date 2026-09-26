OPEN — the unrestricted SE(1/20,1) estimate remains unproved and unrefuted by these attempts.

# Three independent clean-room attacks on the set-energy estimate

Task 017, 2026-09-26. All three independent outputs have been checked and assembled; STATUS records completion. Three fresh agents received only the task's supplied text and clean-room restrictions. They did not read files, web sources, papers, route reports, or one another's results. The supplied text itself mentioned a weaker estimate; none of its proof was supplied, and no agent used it as an established input. Root comparison and checking take place after independent delivery.

Let G=SL2(F_p), D=p(p^2-1), A a nonempty symmetric set, n=|A|, and

\[
 E(A)=\#\{(a,b,c,d)\in A^4:ab^{-1}=cd^{-1}\},\qquad
 \alpha(A)=\max_{x,H<G}|A\cap xH|/n.
\]

All quadruples are ordered and diagonals are retained. The target is an absolute C such that, for all sufficiently large primes and every such A,

\[
 E(A)/n^3\le C\{n^{-1/20}+\alpha(A)+n/D\}.                 \tag{SE}
\]

## Attempt A

### A.1. A complete affine-hyperplane theorem

For every odd prime and every nonempty A contained in an affine hyperplane of Mat_2(F_p), this attempt proves

\[
 \boxed{E(A)/n^3\le2\{\alpha(A)+n^{-1/2}\}.}               \tag{A1}
\]

Thus (SE) holds with C=2 under this extra hypothesis, without symmetry. For an invertible defining functional, the coefficient of alpha can be sharpened to one as proved below. A independently derived the general spectral bound (B1) too, by the same unipotent-weight degree argument followed by fourth-moment Plancherel; its dense-range constant is 8/3. We give the distinct hyperplane proof in full.

Put M=alpha(A)n. When n>=2, any two different points a,b lie in the coset a< a^{-1}b > of a proper cyclic subgroup of G, so M>=2. Every affine line in matrix space contains at most M points of A: if it contains three, its determinant polynomial of degree at most two is identically 1. Writing the line as g(I+tN) gives tr N=det N=0, so N is nonzero nilpotent and the line is a coset of the unipotent subgroup {I+tN}. Lines with at most two points are already covered. The case n=1 is trivial in all estimates below.

First assume tr(a)=tau!=0 for all a in A. Write S_x={b in A:xb in A}, r_x=|S_x|. If x!=I and tr x=2, then x=I+N with N nonzero nilpotent, and tr(Nb)=0 for b in S_x. After changing basis this says b_{21}=0; hence S_x lies in a proper Borel subgroup and r_x<=M.

An ordered noncollinear triple b_1,b_2,b_3 belongs to at most one S_x with tr x!=2. Indeed, the three b_i are linearly independent: a linear relation has coefficient sum zero by taking traces, so it would be an affine dependence. The independent equations tr(xb_i)=tau define an affine line I+tV. On it,

\[
 \det(I+tV)=1+t\operatorname{tr}V+t^2\det V.
\]

If this polynomial is not constant, at most one solution other than t=0 has determinant 1. If it is constant, every point on the line has trace 2, and none is in the stated nonexceptional range. This proves triple uniqueness.

The number of ordered noncollinear triples in S_x is at least r_x(r_x-1)(r_x-M), by first choosing two distinct points and excluding their line for the third. This lower bound may be negative, which causes no problem. The trace-two exceptions have r_x<=M, so their summands are nonpositive. Therefore

\[
 \sum_{x\ne I}r_x(r_x-1)(r_x-M)\le n(n-1)(n-2).           \tag{A2}
\]

Set S_j=sum_{x!=I}r_x^j. Then S_1=n(n-1), S_2=E(A)-n^2 and S_3 S_1>=S_2^2 by Cauchy–Schwarz. Writing z=S_2/S_1, expansion of (A2) gives

\[
 z^2-(M+1)z+M\le n-2,
 \qquad z\le\frac{M+1+\sqrt{(M-1)^2+4(n-2)}}2
 \le M+\sqrt{n-2}.
\]

Consequently E(A)<=n^2+n(n-1)(M+sqrt(n-2)), and

\[
 E(A)/n^3\le\alpha+n^{-1/2}+n^{-1}.                       \tag{A3}
\]

If instead tr(a)=0 on A, Cayley–Hamilton gives b^{-1}=-b and (xb)^{-1}=-xb for b in S_x. Thus bxb^{-1}=x^{-1}. For noncentral x, the possible b lie in a single coset of the proper centralizer C_G(x), giving r_x<=M. Only x=+/-I remain, each with r_x<=n, whence

\[
 E(A)\le2n^2+Mn^2,\qquad E(A)/n^3\le\alpha+2/n.          \tag{A4}
\]

This proves the stated fixed-trace bound alpha+2n^{-1/2}.

### A.2. All affine hyperplanes and the degeneracies

Write the hyperplane as tr(La)=tau, L!=0. If L is invertible and tau!=0, the preceding triple argument still applies: the b_i are linearly independent and the functionals x->tr(Lxb_i) are independent because right multiplication by L is invertible under the trace pairing. Their solution line passes through I.

For the exceptional x=I+N of trace 2, the condition is tr(LNb)=0. Here LN has rank one; write LN=uv^T. The condition means bu belongs to ker(v^T), a fixed projective line. The matrices b form a coset of the proper stabilizer of the line spanned by u. Thus r_x<=M and (A3) follows.

If L is invertible and tau=0, put B=Lb, X=LxL^{-1}, delta=det L. Both B and XB have trace zero and determinant delta, so their inverse formulas give BXB^{-1}=X^{-1}. For noncentral x, solutions b lie in one coset of C_G(X); hence (A4) follows again.

If L has rank one, write L=uv^T. Choose determinant-one matrices P,Q with first row v^T and first column u, respectively. The change a->PaQ turns the equation into a_{11}=tau and preserves energy and alpha: right multiplication cancels from ab^{-1}, left multiplication conjugates it, and subgroup cosets map to subgroup cosets.

For tau=0 this set is in one Borel coset, so alpha=1. For tau!=0, let H be the lower unipotent subgroup. If x=[[r,s],[t,u]] is outside H, the condition (xb)_{11}=tau either has no solutions (s=0,r!=1) or fixes b's first column (s!=0). A fixed first column is a coset of a proper unipotent subgroup. Thus r_x<=M outside H. Moreover

\[
 S:=\sum_{x\in H}r_x=\sum_{Hy}|A\cap Hy|^2\le Mn.
\]

Right cosets Hy are left cosets of conjugate subgroups, so the given alpha applies. Since M<=n,

\[
 E(A)\le nS+M(n^2-S)\le2Mn^2-M^2n,
 \qquad E(A)/n^3\le2\alpha-\alpha^2.                      \tag{A5}
\]

Equations (A3)–(A5) prove (A1) in every case.

For a partition into k hyperplane pieces A_i, the proved consequence is only

\[
 E(A)/n^3\le2k^2(\alpha+n^{-1/2}).                       \tag{A6}
\]

To justify the loss, the Fourier Schatten-four norm gives E(sum_i1_{A_i})^{1/4}<=sum_iE(A_i)^{1/4}. Each piece has maximal coset intersection at most M and size n_i<=n, so (A1) yields E(A_i)<=2(M+sqrt(n))n_i^2. Cauchy–Schwarz gives sum_i sqrt(n_i)<=sqrt(kn); raising to the fourth power proves (A6). The factor k^2 prevents using an unrestricted trace partition to obtain an absolute linear coefficient of alpha.

## Attempt B: large sets and conjugacy-invariant sets

This attempt proves (SE) with C=3 for n>=p^{40/19}, and with C=1 for every conjugacy-invariant A when p>=37. These results do not require A to be symmetric. The complete proofs use finite-group Fourier identities and an elementary proof of the representation-degree bound; no growth or BSG theorem is used.

### B.1. Minimum representation degree

Every nontrivial irreducible complex representation of G, for odd prime p, has degree at least d_0=(p-1)/2. To prove this, use the unipotents U(t)=[[1,t],[0,1]]. A nontrivial irreducible must contain a nontrivial U-character. Otherwise its kernel contains U and every conjugate, including the lower unipotents, which generate G. Generation follows by Gaussian elimination and

\[
 U(s)\begin{pmatrix}1&0\\-s^{-1}&1\end{pmatrix}U(s)
 =\begin{pmatrix}0&s\\-s^{-1}&0\end{pmatrix}.
\]

Multiplication by the inverse of the value at s=1 also yields diag(s,s^{-1}), completing the elementary generation claim.

The U-characters are t->exp(2 pi i kt/p). Conjugation by diag(s,s^{-1}) permutes the nonzero parameters by the nonzero squares (possibly through their inverses, which gives the same orbit). A nontrivial parameter therefore forces (p-1)/2 distinct weight spaces. This proves the degree bound.

### B.2. A general density-sensitive fourth-moment bound

For every nonempty A and every odd prime,

\[
 \boxed{\frac{E(A)}{n^3}
 \le\frac nD+\frac{2p(p+1)}n(1-n/D)^2.}                  \tag{B1}
\]

Let f=1_A, tilde f(x)=f(x^{-1}), and F_rho=sum_x f(x)rho(x), with unnormalized convolution. The convolution f*tilde f counts ab^{-1}, so Plancherel gives

\[
 E(A)=D^{-1}\sum_\rho d_\rho\|F_\rho F_\rho^*\|_{HS}^2,
 \qquad
 \sum_{\rho\ne1}d_\rho\|F_\rho\|_{HS}^2=Dn-n^2.
\]

Set z=n-n^2/D. For every nontrivial rho,

\[
 \|F_\rho\|_{op}^2\le\|F_\rho\|_{HS}^2\le Dz/d_\rho\le Dz/d_0.
\]

The singular-value inequality sum sigma_j^4<=(max sigma_j^2)sum sigma_j^2 then gives E(A)<=n^4/D+(D/d_0)z^2. Substitute d_0=(p-1)/2 and divide by n^3 to obtain (B1).

If n>=[2p(p+1)]^{20/19}, the error in (B1) is at most n^{-1/20}, so (SE) holds with C=1. More simply, if n>=p^{40/19}, then for p>=3

\[
 \frac{2p(p+1)}n\le\frac83\frac{p^2}n
 \le\frac83n^{-1/20}.
\]

Thus C=3 is a valid convenient constant in (SE) on this size range (indeed 8/3 suffices).

### B.3. Conjugacy-invariant sets

If A is invariant under conjugation, Schur's lemma makes F_rho=lambda_rho I. Hence sum_{rho!=1}d_rho^2|lambda_rho|^2=Dz and |lambda_rho|^2<=Dz/d_0^2. The fourth-moment calculation improves to

\[
 \boxed{\frac{E(A)}{n^3}
 \le\frac nD+\frac{4p(p+1)}{(p-1)n}(1-n/D)^2.}           \tag{B2}
\]

A noncentral g has centralizer size at most 2p. Indeed choose v such that v,gv are independent. Any matrix commuting with g is determined by its value on v and is aI+bg. For each b the determinant equation a^2+ab tr(g)+b^2=1 has at most two roots a. Thus a noncentral conjugacy class has size at least D/(2p)=(p^2-1)/2.

If A contains any noncentral element, n>=(p^2-1)/2. The error in (B2) is at most 8p/(p-1)^2<=13/p for p>=5. For p>=37, p^{17/20}>=13 (for example p^{17/20}>=p^{3/4} and 37^3>13^4). As n<D<p^3,

\[
 13/p\le p^{-3/20}\le n^{-1/20}.
\]

This proves (SE) with C=1. If A is entirely central, alpha(A)=1 by taking the proper subgroup Z(G); the elementary bound E(A)<=n^3 proves the same conclusion. Thus every conjugacy-invariant set is covered.

The loss in (B1) is explicit: its error has size p^2/n. The scalar Fourier blocks in (B2) save an additional factor of roughly p. No argument in this attempt controls non-scalar blocks for arbitrary A through the required linear alpha(A) term. That is a missing step, not a consequence of these estimates.

## Attempt C

### C.1. Independent dense-range proof

C also proved (B1), this time by a regular-representation trace argument. For symmetric A let Tf(x)=sum_{a in A}f(a^{-1}x). It is self-adjoint and commutes with the right regular action. Its constant eigenvalue is n. Every eigenspace in the complement of constants is a representation with no invariant vectors, so the elementary unipotent-weight argument gives multiplicity at least d_0=(p-1)/2. If lambda_i are all nonconstant eigenvalues, counted with multiplicity,

\[
 \sum_i\lambda_i^2=Dn-n^2,\quad
 \max_i\lambda_i^2\le(Dn-n^2)/d_0,\quad
 \sum_i\lambda_i^4\le(Dn-n^2)^2/d_0.
\]

The identities tr T^2=Dn and tr T^4=D E(A) follow by counting identity products; symmetry makes the latter identical to the ordered quotient-energy convention. This proves (B1) again, and hence (SE) with C=3 for n>=p^{40/19}. More generally, n>=p^{2+epsilon} gives E(A)/n^3<=n/D+3n^{-epsilon/(2+epsilon)}. No growth assertion is used.

### C.2. A subgroup-sensitive family

For p>=5 and nonempty X subset P^1(F_p), let

\[
 A_X=\{g:gX\cap X\ne\varnothing\}.
\]

This is a nonempty symmetric set, and the attempt proves

\[
 \boxed{E(A_X)/|A_X|^3\le16\{\alpha(A_X)+|A_X|/D\}.}       \tag{C1}
\]

Put q=p+1, m=|X|, F(g)=|X intersect gX|, mu=m^2/q, and sigma=m(1-m/q). The action is doubly transitive: it is transitive and the stabilizer of infinity contains all translations. A prescribed point mapping therefore has D/q realizations; a prescribed mapping of two ordered distinct points has D/[q(q-1)]. Counting these gives

\[
 D^{-1}\sum_gF(g)=\mu,\qquad
 D^{-1}\sum_gF(g)^2=\frac{m^2}q+\frac{m^2(m-1)^2}{q(q-1)}
 =\mu^2+\sigma^2/p.                                      \tag{C2}
\]

For unnormalized convolution, F(h)F(h^{-1}g) counts x,y,u,v in X satisfying hy=x and hu=gv. If y=u, there are m F(g)D/q choices. If y!=u, there are m(m-1)(m^2-F(g))D/[q(q-1)] choices. Thus

\[
 (F*F)(g)=D\{\mu^2+(\sigma/p)(F(g)-\mu)\},
 \qquad\sum_g(F*F)(g)^2=D^3\{\mu^4+\sigma^4/p^3\}.        \tag{C3}
\]

Write n=|A_X| and x=n/D (the scalar x here is a density). Since F is supported on A_X and F>=1 there, Cauchy–Schwarz yields

\[
 x\ge\frac{\mu^2}{\mu^2+\sigma^2/p}
 =\frac{m^2p}{m^2p+(q-m)^2},\qquad x\le\mu.              \tag{C4}
\]

Both 1_{A_X} and F are symmetric, and 1_{A_X}<=F pointwise. Nonnegative convolution and (C3) imply

\[
 E(A_X)/n^3\le(\mu^4+\sigma^4/p^3)/x^3.                  \tag{C5}
\]

For any fixed u,v in X, the entire coset {g:gv=u}, of size D/q, lies in A_X. Therefore

\[
 \alpha(A_X)\ge1/(qx)\ge1/(q\mu)=1/m^2.                 \tag{C6}
\]

If m^2<=p, then q-m<=p and (C4) gives x>=m^2/(m^2+p)>=mu/2. Hence

\[
 \mu^4/x^3\le16x,\qquad
 \sigma^4/(p^3x^3)\le8(q/p)^3/m^2
 \le1728/(125m^2)\le16\alpha(A_X).
\]

This proves (C1). If m^2>p, (C4) instead gives x>1/2, and E(A_X)<=n^3 immediately implies (C1). The family includes natural sparse unions of full Borel cosets, but the proof does not extend to arbitrary subsets of those unions: it uses the exact moment identities of F.

## Comparison and remaining gap

| Proven domain | Bound or target constant | Independent attempt |
|---|---|---|
| All sets, arbitrary size | Density-sensitive spectral bound (B1), possibly vacuous | A, B, C independently |
| n>=p^{40/19} | (SE), C=8/3, or convenient C=3 | A, B, C |
| Every conjugacy-invariant set, p>=37 | (SE), C=1 | B |
| Every set in an affine hyperplane, odd p | (SE), C=2; explicit stronger formulas (A3)–(A5) | A |
| Bounded k hyperplane pieces | (A6), with its k^2 loss | A |
| A_X={g:gX intersects X}, p>=5 | (C1), C=16 without an n^{-1/20} term | C |

No attempt proves or refutes (SE) for unrestricted symmetric A. Around n of order p^2, the general spectral error is of constant size while the desired right side may tend to zero. The hyperplane proof needs independent linear constraints on rich intersections and cannot discard its partition loss. The conjugacy-invariant proof uses scalar Fourier blocks. The A_X proof relies on a very specific complete coset-incidence structure. None supplies the missing subgroup-sensitive estimate for arbitrary sets.

These are complete ordinary proofs of restricted cases, not an extraction of the target coefficient for every set. No unproved growth or sum-product input, or the copied weaker estimate, was used. Root checked the trace-zero and rank-one degeneracies, left/right coset conventions, moment identities, and constants. The independent attempts and root review are same-model work; no cross-vendor referee or kernel formalization is claimed. No numerical process, paid resource, dependency installation, or external publication was used for this task; monetary usage was not exposed.
