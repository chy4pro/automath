OPEN — target not proved; three independent clean-room attempts complete. Elementary cancellation excludes every fixed ordinary power r≤59 at N=floor(p^(1/20)); explicit upper and lower bounds proved.

# Central envelopes for the full-grid W walk

Task020, 2026-10-02. This report concerns **ordinary convolution powers** of the precise full-grid measure in the task, not automatically all Lemma15 subset correlations. Fresh attempts A, B and C received only the task's problem statement, definitions and target; none used web sources, papers, campaign files, numerical tests or other-agent results. All three independently found the cancellation obstruction. A and B independently proved the endpoint upper bound; A additionally supplied the logarithmically sharp two-step obstruction, B the sharp first-step exponent, and C the uniform-envelope bound. Root checked these written arguments.

The platform repeatedly rejected additional concurrent agents with `agent thread limit reached`, even when the nominal active-agent cap was not filled. A fresh seat became available after a producer completed, permitting sequential isolated attempts. No old context was relabelled fresh. These are independent attempts within one model/vendor, not cross-vendor review or kernel formalisation.

## 1. Definitions and the correct equivalence

Let p be an odd prime, G=SL2(F_p), D=p(p²−1), 2≤N≤p, I={1,…,N},

\[
U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},\quad
W=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
h_{a,b}=U(-b)WU(a)=\begin{pmatrix}-b&-1-ab\\1&a\end{pmatrix}.
\]

The endpoint map (a,b)↦h_{a,b} is injective, so μ assigns mass N^-2 to each of these N² matrices. Convolution uses counting measure. Write μ^{*r} for r ordinary factors and

\[
\mathcal B(f)=\sum_{\mathcal C}|\mathcal C|\max_{g\in\mathcal C} f(g)
\]

for any nonnegative measure f, summing over conjugacy classes. This functional is homogeneous, monotone and subadditive. For a probability f, **it is exactly the least central-envelope constant**: if f≤Bν with ν central probability, the classwise maximum gives 𝓑(f)≤B. Conversely,

\[
\nu(g)=\frac{\max_{x\in\mathcal C_g}f(x)}{\mathcal B(f)}
\]

is central probability and attains equality. No symmetry assumption is required.

If m_C=f(C), the exact equivalent formulation is

\[
\mathcal B(f)=\sum_{m_C>0}m_C
 \frac{|C|\max_C f}{m_C}.
\tag{1}
\]

It is the mass-weighted average of concentration inside classes. The task's proposed separate class-mass/spread equivalence is not correct as stated. A bound on every within-class concentration suffices, without a separate mass condition. For example δ_I has 𝓑=1 although its singleton class has all the mass. Bounds m_C≤A|C|/D and max_C f≤S m_C/|C| give f≤AS/D, with the *product* AS, not either factor separately.

Every noncentral class has size between (p²−1)/2 and p(p+1). Indeed the centralizer of a nonscalar matrix is the determinant-one part of its two-dimensional matrix algebra. It has size p−1 for split semisimple elements, p+1 for nonsplit semisimple elements (the norm-one subgroup in F_{p²}), and 2p for noncentral repeated eigenvalues. Orbit–stabilizer gives the claimed bounds. Nonidentity U(t) occupy at most two classes, since diagonal conjugation multiplies t by a square. Each such class has size (p²−1)/2.

## 2. Uniform endpoint upper bound

For all r≥1,

\[
\boxed{\mathcal B(\mu^{*r})\le
 \frac{(2N-1)p(p+1)}{N^2}<\frac{2p(p+1)}N.}
\tag{2}
\]

Fix a middle matrix K=[[x,y],[c,z]]∈G and let λ_K be the law of U(-b)KU(a) for independent uniform a,b∈I. If c≠0, its top-left and bottom-right entries x−bc and z+ac determine b,a, respectively. Partition I² by the integer difference a−b. Each of its 2N−1 diagonals consists of conjugate matrices: increasing both endpoints by s conjugates the product by U(-s). On one diagonal the submeasure has maximum atom N^-2 and support in one class, hence envelope mass at most p(p+1)/N². Subadditivity proves (2) for λ_K in this case; coinciding modular traces between different diagonals cause no difficulty.

If c=0 and x≠z, all outputs have distinct eigenvalues and lie in one split class. The upper-right entry xa+y−bz has at most N representations (fix a, solve uniquely for b), so every atom is at most 1/N. This gives 𝓑(λ_K)≤p(p+1)/N.

If c=0 and x=z=ε∈{±1}, the outputs have off-diagonal entry y+ε(a−b), again with atoms at most 1/N. Their classes comprise at most two noncentral unipotent classes and one central singleton, of total size p². Thus 𝓑(λ_K)≤p²/N. Both c=0 bounds are no larger than the right side of (2).

Finally each product of r generators has the form

\[
U(-b_1)[WU(a_1-b_2)W\cdots U(a_{r-1}-b_r)W]U(a_r).
\]

The two outer endpoints remain independent uniform variables after conditioning on the bracketed middle matrix. Averaging the λ_K bounds proves (2).

This bound is of order p²/N and does not achieve the requested saving. It is a theorem for every r, not a claim that increasing r never improves the true minimum.

C's additional bound is 𝓑(μ^{*r})≤D/N², since ||μ||∞=N^-2 and convolution contracts the maximum atom. Thus one may take the minimum of this and (2). At N≥3,p>2N, B also obtains the first-step lower bound

\[
\mathcal B(\mu)\ge
\frac{(2N-3)p(p-1)+(p^2-1)}{N^2}.
\]

Indeed the 2N−1 distinct traces a−b each represent one class, with atom N^-2. Exactly two traces are ±2, with class sizes (p²−1)/2; every remaining class has size at least p(p−1). This confirms sharp p,N exponents in (2) already at r=1.

## 3. Cancellation lower bounds at every fixed power

For k≥1 and k≥0, respectively,

\[
\boxed{\mathcal B(\mu^{*2k})\ge
 \frac{p^2-1}{4kN^{k+1}},\qquad
\mathcal B(\mu^{*(2k+1)})\ge
 \frac{p^2-1}{2N^{k+1}}.}
\tag{3}
\]

Let σ be uniform on U(I), σ⁻ its inversion, ρ=σ*σ⁻, z=−I and τ=δ_W*ρ*δ_{W^{-1}}. Then

\[
\mu=\sigma^-*\delta_W*\sigma,\qquad
\rho(I)=\tau(I)=1/N,
\]

and W²=z gives

\[
\mu^{*2k}=\delta_{z^k}*\sigma^-*\tau*
 (\rho*\tau)^{*(k-1)}*\sigma.
\tag{4}
\]

In this alternating product, retain only the event that each of its k lower-unipotent factors τ is the identity. Positivity and commutativity of upper-unipotent factors imply the pointwise measure inequality

\[
\mu^{*2k}\ge N^{-k}\delta_{z^k}*\rho^{*k}.
\tag{5}
\]

Every atom of ρ is at most 1/N, as is every atom of ρ^{*k}. Hence its nonidentity mass is at least 1−1/N. Its nonzero upper-unipotent parameters lie among sums of k differences from I, at most 2k(N−1) possible nonzero residues. Wrapping modulo p can only decrease this support count. At least one nonzero t has

\[
\rho^{*k}(U(t))\ge\frac{1-1/N}{2k(N-1)}=\frac1{2kN}.
\]

Equation (5) therefore gives an atom at z^kU(t) of mass at least 1/(2kN^{k+1}); multiplying by its class size (p²−1)/2 proves the even bound.

For the odd bound, convolve (5) with μ. After removing the factor N^-k and central sign, the retained probability has the form

\[
\lambda=\text{law of }U(s)WU(a)
 =\begin{pmatrix}s&sa-1\\1&a\end{pmatrix},
\]

where a is uniform on I and s has the upper-unipotent law ρ^{*k}*σ⁻, independently. A fixed trace s+a determines s for each a, so each conjugacy class meets this support in at most N elements. All are noncentral. Thus for every class C,

\[
|C|\max_C\lambda\ge\frac{p^2-1}{2N}\lambda(C).
\]

Sum over C, restore N^-k, and use invariance of 𝓑 under central translation. The k=0 odd case follows directly from the same λ argument.

### Consequence for short intervals

For N=floor(p^θ), the necessary condition for a bound 𝓑(μ^{*r})≤Cp^β, with fixed r,C, is

\[
\theta(\lfloor r/2\rfloor+1)\ge2-\beta.
\tag{6}
\]

Indeed (3) gives 𝓑≥c_r(p²−1)p^{-θ(floor(r/2)+1)}, where c_{2k}=1/(4k) and c_{2k+1}=1/2. If e=2−θ(floor(r/2)+1)−β>0, p≥3 and p^e>9C/(8c_r) already contradict the proposed upper bound, since 1−p^-2≥8/9.

At θ=1/20 and β=9/20, (6) requires floor(r/2)+1≥31. Therefore **r≥60 is necessary**. For every fixed r≤59 the lower exponent is at least 1/2, so no bound Cp^{1/2−δ}, δ>0, works either. This does not prove any target upper bound at r=60 or later. If θ is allowed arbitrarily small, no single r works for all θ at a fixed β<2.

## 4. A sharper obstruction at two steps

Let M=floor(N/2), H_M=∑_{j=1}^M1/j. If M²<p, then

\[
\boxed{\mathcal B(\mu^{*2})\ge
 \frac{(p^2-1)(N-M)M^2}{4H_MN^4}
 \ge\frac{p^2-1}{72NH_M}.}
\tag{7}
\]

Put d=a_1−b_2, b=b_1, a=a_2. Direct multiplication yields

\[
h_{a_1,b}h_{a,b_2}=
\begin{pmatrix}-1-bd&b-a-abd\\d&ad-1\end{pmatrix},
\qquad \operatorname{tr}=-2+d(a-b).
\tag{8}
\]

For each integer d∈[1,M], q∈[1,M], take b=1 and a=q+1. There are N−d choices of (a_1,b_2) with this integer difference. Thus the resulting noncentral matrix has probability **at least** (N−M)/N⁴. If 2N−1≤p the usual triangular-difference count gives equality (N−d)/N⁴; without that extra hypothesis wrapped differences may increase the probability. Only the lower bound is used here.

Different integer products dq give different traces modulo p because 1≤dq≤M²<p. Count the distinct products by their multiplicative energy E_M=#{(a,b,c,d)∈[M]^4:ab=cd}, with ordered variables. Write

\[
a=gx,\quad c=gy,\quad b=hy,\quad d=hx,\quad (x,y)=1.
\]

For m=max(x,y), at most 2m ordered coprime pairs occur and at most floor(M/m)² choices of g,h. Consequently E_M≤2M²H_M. Cauchy–Schwarz gives at least M²/(2H_M) distinct products. Each provides a different noncentral class and an atom of the preceding size. Multiplying by (p²−1)/2 proves the first bound in (7). Use M≥N/3 and N−M≥N/2 for the second.

At N=floor(p^{1/20}), (2) and (7) bound the two-step minimum between constant multiples of p²/(N log N) and p²/N. Thus at r=2 the obstruction is substantially stronger than (3), and sharp in its p,N exponent up to a logarithm.

## 5. Independent-attempt comparison and limitations

| Attempt | Established | Limitation |
|---|---|---|
| A, fresh isolated | Exact envelope functional; endpoint upper bound (2); both cancellation bounds (3); product-table lower bound (7) | No target envelope at r≥60 |
| B, fresh isolated | Independently derived the same functional, (2), (3), and r≤59 obstruction; sharp first-step exponent | No target envelope at r≥60 |
| C, fresh isolated | Independently derived the same functional and (3), using μ²≥N^-1δ_{−I}*ρ directly; supplied 𝓑≤D/N² | No target envelope at r≥60; no completed useful mixing-time bound |

The useful new constraint is on allowable stages, not an improved digit bound. Class-mass cancellation alone cannot remove positive mass concentrated on the retained unipotent events. These proofs do not rule out all later fixed stages, a different walk, or a non-pointwise spectral method.

No finite numerical test, external source, kernel formalisation, git operation or paid compute was used for these clean-room proofs. Actual coefficients are displayed; mathematical statements are written proofs checked by root, not model self-claims promoted to external verification. Task021 separately audits the bridge to actual correlation laws and the alphabet ledger; that ordinary route material was not supplied to the fresh attempts.
