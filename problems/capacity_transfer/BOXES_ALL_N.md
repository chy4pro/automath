PROVED — informed finite supplement to task 039b. The square-window argument, rounding estimates and rational splice below were checked independently. This is not a new Lean formalisation or a novelty verdict.

# A two-dimensional Sidon bound for every positive integer N

## Statement and conventions

Let \(N\ge1\) be an integer. A set \(A\subseteq\{0,\ldots,N-1\}^2\) is strong Sidon if

\[
 a+b=c+d,\qquad a,b,c,d\in A,
\]

implies equality of the unordered pairs, including multiplicities. Repeated elements within each pair are allowed. Addition is ordinary addition in \(\mathbb Z^2\), not modular addition. Translation gives the same statements in \(\{1,\ldots,N\}^2\).

**Theorem.** Every such set satisfies

\[
 \boxed{
 |A|\le N+\left(\frac83\right)^{1/3}N^{2/3}+18N^{1/3}
 }\qquad(N\ge1).
 \tag{A1}
\]

The proof uses the established \(d=2\) case of [BOXES.md, Theorem (B1)](BOXES.md) only when \(N^{1/3}\ge120\). That theorem, together with [COMMON_CAPACITY.md](COMMON_CAPACITY.md), contains the full analytic argument. For smaller parameters, the discrete argument below is independent of the capacity lemma. No source comparison is asserted here.

## Nonzero vector differences

Every nonzero ordered difference vector has at most one representation by points of \(A\). Indeed, if \(a-b=c-d\ne0\), then \(a+d=c+b\). Strong Sidonicity gives either \(a=c,d=b\), as required, or \(a=b,d=c\), which would make the difference zero. This includes cases in which one of the displayed sums is diagonal.

In particular, vectors with one zero coordinate remain subject to uniqueness. Zero vectors are excluded from this uniqueness statement and contribute exactly \(|A|\) diagonal pairs.

## Exact finite square-window inequality

Fix an arbitrary positive integer \(T\), set

\[
 W_T=\{0,\ldots,T-1\}^2,\qquad M=N+T-1,\qquad k=|A|.
\]

For each \(z\in\mathbb Z^2\), define the integer occupancy

\[
 r(z)=\#\{a\in A:z\in a+W_T\}.
\]

It is supported on \(\{0,\ldots,M-1\}^2\), including its boundary. Counting each translated window gives

\[
 \sum_z r(z)=kT^2.
 \tag{A2}
\]

For an integer \(u\), write \((T-|u|)_+=\max\{T-|u|,0\}\). Two translated windows have intersection size

\[
 |(a+W_T)\cap(b+W_T)|
 =(T-|a_1-b_1|)_+(T-|a_2-b_2|)_+.
\]

Consequently

\[
 \sum_z r(z)^2
 =kT^2+
 \sum_{\substack{a,b\in A\\a\ne b}}
 (T-|a_1-b_1|)_+(T-|a_2-b_2|)_+.
 \tag{A3}
\]

Every summand is nonnegative, and each nonzero vector difference appears at most once. Therefore the second term is at most the sum over all nonzero vectors of \(\mathbb Z^2\). The one-dimensional identity

\[
 \sum_{u\in\mathbb Z}(T-|u|)_+
 =T+2\sum_{u=1}^{T-1}(T-u)=T^2
\]

shows that this full nonzero-vector sum is \(T^4-T^2\): the origin has weight \(T^2\), not \(1\). Hence

\[
 \sum_z r(z)^2\le T^4+(k-1)T^2.
 \tag{A4}
\]

This remains valid for the empty set: then the right side is \(T^4-T^2\ge0\).
Applying Cauchy–Schwarz to the \(M^2\) positions in the containing square, including zero occupancies, gives

\[
 k^2T^4\le M^2\sum_z r(z)^2.
\]

Together with (A4), this is the exact finite bound

\[
 \boxed{
 k^2\le M^2\left(1+\frac{k-1}{T^2}\right).
 }
 \tag{A5}
\]

There is no omitted factor of two: (A3) and the complete lattice sum both use ordered vectors.

## A uniform elementary estimate

Put \(x=N^{1/3}\ge1\), and take the integer scale

\[
 T=\lceil x^2\rceil,\qquad M=N+T-1,\qquad
 \eta=\frac{M^2}{T^2}.
\]

Then (A5) reads \(k^2\le M^2+\eta k-\eta\). Since \(\eta\ge0\), dropping its negative constant term gives \(k^2-\eta k-M^2\le0\). The positive-root bound and \(\sqrt{1+u}\le1+u/2\) for \(u\ge0\) imply

\[
 k\le\frac{\eta+\sqrt{\eta^2+4M^2}}2
 \le M+\frac{\eta}{2}+\frac{\eta^2}{8M}.
 \tag{A6}
\]

Here \(M>0\), so every division is valid. The ceiling choice gives

\[
 T\ge x^2,\qquad x^3\le M\le x^3+x^2,\qquad
 \eta\le\frac{(x^3+x^2)^2}{x^4}=(x+1)^2.
\]

The estimate for \(M\) follows from \(\lceil x^2\rceil-1\le x^2\); it also holds when \(x^2\) is an integer. Insert the upper bounds for the numerators and the lower bound \(M\ge x^3\) for the last denominator in (A6). We obtain

\[
\begin{aligned}
 k
 &\le x^3+x^2+\frac{(x+1)^2}{2}
                   +\frac{(x+1)^4}{8x^3}\\
 &=x^3+\frac32x^2+\frac98x+1
                +\frac3{4x}+\frac1{2x^2}+\frac1{8x^3}\\
 &\le x^3+\frac32x^2+\frac72x.
\end{aligned}
 \tag{A7}
\]

For the last inequality, multiplication of the difference by \(8x^3>0\) gives the explicit nonnegative polynomial

\[
 19x^4-8x^3-6x^2-4x-1
 =(x-1)(19x^3+11x^2+5x+1)\ge0.
 \tag{A8}
\]

Thus (A7) is proved for every real \(x=N^{1/3}\ge1\), with no finite scan or asymptotic rounding convention.

## Splicing with the capacity estimate

Set \(c=(8/3)^{1/3}\). For \(x\ge120\), Theorem (B1) of [BOXES.md](BOXES.md), with \(d=2\), states

\[
 k\le x^3+\frac32(8/9)^{2/3}x^2+8x
     =x^3+cx^2+8x.
 \tag{A9}
\]

Indeed the positive number \(\frac32(8/9)^{2/3}\) has cube \(8/3\); the onset there is \(x\ge\max\{120,8\}=120\). This proves (A1) in that range.

For \(1\le x<120\), the integer comparison

\[
 83^3=571787<576000=\frac83\,60^3
\]

gives \(c>83/60\). Consequently

\[
 \left(\frac32-c\right)x^2
 <\frac7{60}x^2<14x.
\]

Combine this with (A7):

\[
 k<x^3+cx^2+\left(14+\frac72\right)x
   =x^3+cx^2+\frac{35}{2}x
   <x^3+cx^2+18x.
\]

This includes \(N=1\). The boundary \(x=120\), equivalently \(N=120^3=1728000\), belongs to (A9), so there is no uncovered parameter. Together the two ranges prove (A1). ∎

## Exact check and verification scope

Run the dependency-free script:

    node check_boxes_all_n.js

It uses BigInt arithmetic to check the square-window energy identity, Cauchy–Schwarz bound, diagonal term and nonzero-vector budget for every subset of the grids with \(1\le N\le3\), at every integer \(1\le T\le6\). It independently tests strong sum uniqueness, including diagonal sums, against uniqueness of nonzero ordered vector differences. It also checks the two polynomial identities in (A7)–(A8), the exact ceiling rule \(T^3\ge N^2>(T-1)^3\), and every rational splice margin. No floating-point root or fitted numerical constant is used.

The finite checks supplement the all-parameter proof; they do not replace the analytic proof in BOXES.md or establish a literature priority claim. No Lean compilation, installation, solver, git operation or publication was performed for this supplement.

Actual run on 2026-10-02: exit 0, PASS; 530 grid subsets, including 199 strong Sidon subsets; 3,180 exact square-window energy identities; 1,194 Sidon energy inequalities; 1,004 exact ceiling checks; both polynomial identities and all rational splice comparisons passed.
