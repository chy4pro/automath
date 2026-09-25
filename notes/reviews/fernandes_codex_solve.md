# Two generators for the equal-parity subgroup of \(S_m\times S_n\)

Permutations are composed from right to left.  For every \(r\geq 2\), define

\[
 a_r=
 \begin{cases}
 (1\ 2\ \cdots\ r),&r\text{ odd},\\
 (1\ 2\ \cdots\ r-1),&r\text{ even},
 \end{cases}
 \qquad
 b_r=
 \begin{cases}
 (1\ 2),&r\text{ odd},\\
 (r-1\ r),&r\text{ even}.
 \end{cases}
\]

Thus \(a_2=1\) (the displayed one-cycle is omitted).  In every degree,
\(a_r\) is even and \(b_r\) is odd.

Here are the promised generating pairs.

* If \(m>n\) and \((m,n)\neq(4,3)\), take
  \[
  \boxed{\quad (a_m,a_n),\qquad (b_m,b_n).\quad}
  \]
* If \(m=n=r\geq5\), put \(d_r=b_ra_r\) and take
  \[
  \boxed{\quad (a_r,a_r),\qquad (b_r,d_r).\quad}
  \]
  Written entirely in cycle notation, the second component \(d_r\) is
  \[
  d_r=
  \begin{cases}
  (2\ 3\ \cdots\ r),&r\text{ odd},\\
  (1\ 2\ \cdots\ r-2\ r\ r-1),&r\text{ even}.
  \end{cases}
  \]

These formulas cover exactly all \(m\geq n\geq2\) outside
\[
\{(2,2),(3,3),(4,3),(4,4)\}.
\]

## Preliminary facts

First, for every \(r\geq2\),
\[
\langle a_r,b_r\rangle=S_r. \tag{1}
\]
Indeed, if \(r\) is odd, conjugating \((1\ 2)\) by powers of
\((1\ 2\ \cdots\ r)\) gives the transpositions along the cyclic chain; in
particular it gives \((1\ 2),(2\ 3),\ldots,(r-1\ r)\), which generate
\(S_r\).  If \(r\) is even, conjugating \((r-1\ r)\) by powers of
\((1\ 2\ \cdots\ r-1)\) gives all the star transpositions
\((i\ r)\), \(1\leq i<r\), and these generate \(S_r\).  This also includes
\(r=2\).

We will use the following standard consequence of Goursat's lemma.

**Subdirect-product lemma.**  Let \(H\leq G\times K\) project onto both
factors.  Then there are normal subgroups \(N_G\mathrel{\triangleleft}G\)
and \(N_K\mathrel{\triangleleft}K\), and an isomorphism
\(\phi:G/N_G\longrightarrow K/N_K\), such that
\[
H=\{(g,k):\phi(gN_G)=kN_K\}. \tag{2}
\]

For completeness, take
\[
N_G=\{g:(g,1)\in H\},\qquad N_K=\{k:(1,k)\in H\}.
\]
Surjectivity of the projections shows that these subgroups are normal.
If \((g,k)\in H\), send \(gN_G\) to \(kN_K\).  The definitions of
\(N_G,N_K\) show that this is well-defined, is an isomorphism, and gives
(2).

We also recall the normal quotients of the symmetric groups which occur
here:

\[
\begin{array}{c|c}
G&\text{nontrivial quotients of }G\text{, up to isomorphism}\\ \hline
S_2&C_2\\
S_3&S_3,\ C_2\\
S_4&S_4,\ S_3,\ C_2\\
S_r\ (r\geq5)&S_r,\ C_2.
\end{array} \tag{3}
\]

Moreover, whenever the quotient is \(C_2\), its kernel is \(A_r\).
Here is a quick justification.  For \(r\geq5\), simplicity of \(A_r\)
implies that the only normal subgroups of \(S_r\) are
\(1,A_r,S_r\): if \(N\mathrel{\triangleleft}S_r\), then
\(N\cap A_r\) is either \(1\) or \(A_r\); in the former case
\([N,A_r]=1\), and the centralizer of \(A_r\) in \(S_r\) is trivial.
For \(S_3\), the normal subgroups are \(1,A_3,S_3\).  For \(S_4\), its
conjugacy-class sizes \(1,6,3,8,6\) show (using Lagrange's theorem) that
the only normal subgroups are \(1,V_4,A_4,S_4\), where \(V_4\) is the
Klein four group of double transpositions.  This proves (3), including
the assertion about index two.

Finally, observe an immediate useful consequence.  Suppose
\(H\leq\Gamma_{m,n}\) is subdirect.  In (2), the common quotient cannot be
trivial, since a trivial common quotient would make \(H=S_m\times S_n\),
which is not contained in \(\Gamma_{m,n}\).  If its common quotient is
\(C_2\), then both kernels are the alternating groups, the only
automorphism of \(C_2\) is the identity, and (2) says precisely
\[
H=\{(\sigma,\tau):\operatorname{sgn}(\sigma)
=\operatorname{sgn}(\tau)\}=\Gamma_{m,n}. \tag{4}
\]

## Unequal degrees

Assume \(m>n\), with \((m,n)\neq(4,3)\), and set
\[
H=\langle (a_m,a_n),(b_m,b_n)\rangle.
\]
The displayed generators belong to \(\Gamma_{m,n}\), because their two
components have equal parity.  By (1), both projections of \(H\) are
surjective, so \(H\) is subdirect.

We claim that the only possible nontrivial common quotient of \(S_m\) and
\(S_n\) is \(C_2\).  If \(m\geq5\), (3) says that a nontrivial quotient of
\(S_m\) is either \(C_2\) or \(S_m\).  The latter cannot be a quotient of
\(S_n\), because \(|S_m|>|S_n|\).  If \(m=4\), then \(n=2\) or \(3\);
for \(n=2\) only \(C_2\) is common, while \(n=3\) is exactly the excluded
pair \((4,3)\), where the extra common quotient \(S_3\cong S_4/V_4\)
occurs.  The only remaining unequal case with \(m<4\) is \((3,2)\), and
again only \(C_2\) is common.

Thus the common quotient supplied by the subdirect-product lemma is
\(C_2\).  Equation (4) gives \(H=\Gamma_{m,n}\), proving the assertion for
all the stated unequal degrees.

## Equal degrees

Let \(m=n=r\geq5\), let \(d_r=b_ra_r\), and set
\[
H=\langle (a_r,a_r),(b_r,d_r)\rangle.
\]
Because \(a_r\) is even and both \(b_r,d_r\) are odd, we have
\(H\leq\Gamma_{r,r}\).  The first projection is \(S_r\) by (1).  The
second is also \(S_r\), since
\[
b_r=d_ra_r^{-1},
\]
so \(\langle a_r,d_r\rangle=\langle a_r,b_r\rangle=S_r\).  Hence \(H\)
is subdirect.

By (3), the nontrivial common quotient in Goursat's lemma is either
\(C_2\) or \(S_r\).  In the first case, (4) immediately gives
\(H=\Gamma_{r,r}\).

It remains to rule out the quotient \(S_r\).  If it occurred, both
Goursat kernels would be trivial, so (2) would make \(H\) the graph of an
automorphism \(\phi\) of \(S_r\).  From the two chosen generators we would
then have
\[
\phi(a_r)=a_r,\qquad \phi(b_r)=d_r.
\]
But \(b_r\) has order \(2\), whereas direct multiplication gives
\[
|d_r|=
\begin{cases}
r-1,&r\text{ odd},\\
r,&r\text{ even}.
\end{cases}
\]
Since \(r\geq5\), this contradicts preservation of element order by an
automorphism.  (Thus the argument also handles \(S_6\) without needing
any classification of its outer automorphisms.)  The \(S_r\)-quotient
case is impossible, so the quotient is \(C_2\), and once more (4) yields
\(H=\Gamma_{r,r}\).

Combining the unequal- and equal-degree arguments proves the result for
every pair requested in the problem.  No computational verification is
used anywhere in the proof.
