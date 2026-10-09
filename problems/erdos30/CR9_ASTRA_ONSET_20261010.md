PROVED — Route A and Route B both certify onset N₁ = 4,600,000. For every integer N ≥ N₁ and every Sidon set A ⊆ {1,…,N}, |A| < √N + (2√2/3)N^(1/4) + 1. Route A proves P_ε(y) > (4/1089)x² for every real x ≥ N₁^(1/4). Route B proves η < (667/3300)x² < x²/2 at this onset; its scalar lemma holds for every real x ≥ 1.

This is a clean-room derivation from the two inequalities supplied in the brief. No repository mathematics, other agents' work, web pages, or literature was consulted. The Paperclip skill was read solely for report submission and issue administration. No subagents were used.

There is a numerical typo in the brief: the correct bracket is

\[
\frac{4631}{100}<x_1=(4\,600\,000)^{1/4}<\frac{4632}{100},
\]

because

\[
4631^4=459\,937\,821\,637\,921
<460\,000\,000\,000\,000
<460\,335\,219\,019\,776=4632^4.
\]

The proof below uses the slightly weaker rational lower bound
\(u=463/10<x_1\). Indeed,
\(463^4=45\,954\,068\,161<46\,000\,000\,000\).
All powers and roots are positive real ones. Every decimal implicit in a displayed rational is exact. There are no asymptotic error terms.

## (i) Replacement final section for Route A

### 6. The explicit additive constant and onset

Put \(N_1=4\,600\,000\) and \(x_1=N_1^{1/4}\). Let \(N\ge N_1\) be an integer and let \(A\subseteq\{0,\ldots,N-1\}\) be a Sidon set. Write \(k=|A|\). Set

\[
x=N^{1/4},\qquad T=\sqrt2\,x^3,\qquad
\gamma=\frac{2\sqrt2}{3},\qquad
\alpha=\log(4/3),\qquad
\varepsilon=200e^{-\alpha x/\sqrt2}.
\tag{6.1}
\]

The estimates below hold, in fact, for every real \(x\ge x_1\), regardless of whether \(x^4\) is integral. Put \(s=\sqrt2\), \(\beta=\alpha/s\), and \(u=463/10\). Since \(463^4=45\,954\,068\,161<46\,000\,000\,000=10^4N_1\), we have \(x\ge x_1>u>46>2>s>0\). Here \(u>46\) follows from \(463>460\), and \(2>s\) follows from \(2<4=2^2\). Consequently
\(L=N/T=x/s>1\) and \(0<T<N\). Thus the interval parameter in Lemma 7 is admissible.

Expanding Lemma 7 gives \(P_\varepsilon(k)\le0\), where, exactly as before,

\[
P_\varepsilon(z)=
z^2-\left(\gamma x+\frac89+\frac43\varepsilon\right)z
-x^4-\gamma x^3-\sqrt2\,\varepsilon x^3.
\tag{6.2}
\]

Indeed, \((4/3)(x/s+2/3+\varepsilon)=\gamma x+8/9+(4/3)\varepsilon\), and \((x/s+2/3+\varepsilon)sx^3=x^4+\gamma x^3+s\varepsilon x^3\).

Here are exact elementary bounds for the exponential. Substitution in the logarithm integral gives

\[
\alpha=2\int_0^{1/7}\frac{dt}{1-t^2}
>2\left(\frac17+\frac{1}{3\cdot7^3}\right)
=\frac{296}{1029}>\frac{719}{2500}.
\]

The first strict inequality follows from \(1/(1-t^2)>1+t^2\) for \(0<t\le1/7\). The last comparison is \(740000>739851\). Also \(s<99/70\), since \(99^2=9801>9800=2\cdot70^2\). Therefore

\[
\beta u>
\frac{719}{2500}\frac{463}{10}\frac{70}{99}
>\frac{941}{100}>1.
\tag{6.3}
\]

The middle comparison is exactly
\(2\,330\,279\,000>2\,328\,975\,000\), obtained by multiplying the positive denominators; the last is \(941>100\).

The positive-term exponential series yields

\[
e^3>\sum_{j=0}^{9}\frac{3^j}{j!}
=\frac{22471}{1120}>\frac{1003}{50},
\qquad
e^{41/100}>
\sum_{j=0}^{3}\frac{(41/100)^j}{j!}
=\frac{9033221}{6000000}>\frac32.
\]

The rational comparisons are \(1\,123\,550>1\,123\,360\) and \(9\,033\,221>9\,000\,000\). Hence

\[
e^{\beta u}>e^{941/100}
=(e^3)^3e^{41/100}
>\frac{3\cdot1003^3}{2\cdot50^3}>12100,
\qquad
200e^{-\beta u}<\frac{2}{121}.
\tag{6.4}
\]

The penultimate comparison is exactly
\(3\,027\,081\,081>3\,025\,000\,000\).

Put \(y=x^2+\gamma x+1\). Since \(\gamma^2=8/9\), the unchanged polynomial identity is

\[
P_0(y)=\frac{10}{9}x^2+\frac{\gamma}{9}x+\frac19\ge x^2.
\tag{6.5}
\]

We retain the full leading term \((10/9)x^2\) in what follows. In particular \(P_0(y)\ge(10/9)x^2\). Also \(0<\gamma<1\), because \(0<\gamma^2=8/9<1\).

Normalize the error by \(x^2\):

\[
F(x):=\frac{\varepsilon((4/3)y+sx^3)}{x^2}
=200e^{-\beta x}
\left(sx+\frac43+\frac{4\gamma}{3x}+\frac{4}{3x^2}\right).
\]

This function is strictly decreasing on \([u,\infty)\). To see this without any estimate on an unspecified remainder, its four summands are positive constant multiples of \(xe^{-\beta x}\), \(e^{-\beta x}\), \(x^{-1}e^{-\beta x}\), and \(x^{-2}e^{-\beta x}\). The first derivative is \(e^{-\beta x}(1-\beta x)<0\), by (6.3). For \(j=0,1,2\), the derivative of \(x^{-j}e^{-\beta x}\) is
\(-e^{-\beta x}(j x^{-j-1}+\beta x^{-j})<0\).

At the rational endpoint \(u\),

\[
su<\frac{99}{70}\frac{463}{10}
=\frac{45837}{700}<\frac{131}{2},
\qquad
\frac43\left(1+\frac\gamma u+\frac1{u^2}\right)
<\frac43\left(1+\frac1{46}+\frac1{46^2}\right)
=\frac{721}{529}<\frac32.
\]

These comparisons are \(45837<45850\), \(463>460\), and \(1442<1587\). Combining them with (6.4) gives, uniformly for \(x\ge x_1>u\),

\[
F(x)\le F(u)
<\frac{2}{121}\left(\frac{131}{2}+\frac32\right)
=\frac{134}{121}.
\tag{6.6}
\]

Finally, (6.2), (6.5), and (6.6) give

\[
\begin{aligned}
P_\varepsilon(y)
&=P_0(y)-\varepsilon\left(\frac43y+sx^3\right)\\
&>\left(\frac{10}{9}-\frac{134}{121}\right)x^2
=\frac4{1089}x^2>0.
\end{aligned}
\tag{6.7}
\]

Here \(10\cdot121-134\cdot9=1210-1206=4>0\). This proves the requested real-variable assertion for every real \(x\ge x_1\).

The quadratic \(P_\varepsilon\) has leading coefficient 1 and strictly negative constant term. Its discriminant is positive, and its two roots have negative product, so precisely one root is positive. Since \(k\ge0\) and \(P_\varepsilon(k)\le0\), \(k\) is at most that positive root. Since \(y>0\) and \(P_\varepsilon(y)>0\), the positive root is strictly smaller than \(y\). Consequently

\[
k<x^2+\gamma x+1
=\sqrt N+\frac{2\sqrt2}{3}N^{1/4}+1.
\]

Translation from \(A\subseteq\{1,\ldots,N\}\) to \(A-1\subseteq\{0,\ldots,N-1\}\) preserves the given Sidon condition. This proves the stated non-strict theorem, and indeed its strict version, for every integer \(N\ge4\,600\,000\). The root argument also includes \(k=0\). ∎

## (ii) Route B: finite tail and scalar lemma

Let \(x\ge x_1\) be real with \(N=x^4\) an integer. Define

\[
s=\sqrt2,\quad T=\lceil sx^3\rceil,\quad
r=\left\lfloor\frac{N-1}{T}\right\rfloor,\quad
q=\frac34,\quad \eta=29Tq^r,\quad \gamma=\frac{2s}{3}.
\]

Then \(T\ge1\) and \(sx^3\le T\le sx^3+1\).

### B3 at onset 4,600,000

For all these \(x,N,T,r\),

\[
r\ge r_1:=32,\qquad
\left(\frac34\right)^{32}<\frac1{9900},\qquad
0<\eta<\frac{667}{3300}x^2<\frac{x^2}{2}.
\tag{B3-new}
\]

First,

\[
x-32s>\frac{463}{10}-32\frac{99}{70}
=\frac{73}{70}>1,
\qquad x^3>46^3=97336>33.
\]

Thus \(x^3(x-32s)>33\), so

\[
N-1=x^4-1>32(sx^3+1)\ge32T.
\]

It follows that \((N-1)/T>32\), and therefore \(r\ge32\). The comparisons used here are \(73>70\) and \(97336>33\).

We next control the interaction of the changing ceiling and floor. Since \(x>1\),

\[
\frac{x^4-1}{sx^3+1}-\left(\frac{x}{s}-1\right)
=\frac{2x^3-x}{s(sx^3+1)}>0.
\]

The numerator is positive because \(x>1\) implies \(2x^2-1>1>0\). Also \(x^4-1>0\) and \(T\le sx^3+1\). For any real \(z\), \(\lfloor z\rfloor>z-1\). Hence

\[
r>\frac{N-1}{T}-1
\ge\frac{x^4-1}{sx^3+1}-1
>\frac{x}{s}-2,
\qquad x<s(r+2).
\tag{B3.1}
\]

No monotonicity of \(r\) as a function of \(N\) is asserted or needed. Using (B3.1), \(s^2=2\), and \(x>1\), we obtain

\[
\frac{\eta}{x^2}
=29\frac{T}{x^2}q^r
\le29\left(sx+\frac1{x^2}\right)q^r
<29(2r+5)q^r.
\tag{B3.2}
\]

For each integer \(r\ge32\),

\[
\frac{(2(r+1)+5)q^{r+1}}{(2r+5)q^r}
=\frac{3(2r+7)}{4(2r+5)}<1,
\]

because \(4(2r+5)-3(2r+7)=2r-1\ge63>0\). Thus the integer sequence \((2r+5)q^r\) is decreasing for \(r\ge32\). Finally,

\[
3^{32}=1\,853\,020\,188\,851\,841,\quad
4^{32}=18\,446\,744\,073\,709\,551\,616,
\]

\[
9900\cdot3^{32}
=18\,344\,899\,869\,633\,225\,900
<18\,446\,744\,073\,709\,551\,616=4^{32}.
\tag{B3.3}
\]

This is the requested rational certificate with \(p=1\), denominator \(9900\). Equations (B3.2) and (B3.3) give

\[
\frac{\eta}{x^2}
<29\cdot69\left(\frac34\right)^{32}
<\frac{2001}{9900}
=\frac{667}{3300}<\frac12.
\tag{B3.4}
\]

The last comparison is \(1334<3300\). In particular, the uniform normalized slack in B3 is strictly greater than
\(1/2-667/3300=983/3300>0\). ∎

### B4 at onset 4,600,000, with a stronger scalar range

**Scalar lemma.** For every real \(x\ge1\), every real \(\gamma\) with \(0<\gamma<1\) and \(\gamma^2=8/9\), every real \(0\le\eta<x^2/2\), and every real \(k\ge0\), if

\[
k^2\le(x^4+\gamma x^3+\eta)
\left(1+\frac\gamma{x^3}(k-1)\right),
\]

then \(k<x^2+\gamma x+1\). In particular the requested non-strict conclusion holds for every \(x\ge x_1\).

**Proof.** Set \(C=x^4+\gamma x^3+\eta>0\), \(y=x^2+\gamma x+1\), and

\[
Q(z)=z^2-C\left(1+\frac\gamma{x^3}(z-1)\right).
\]

Keep the given algebraic identity unchanged:

\[
y^2-(x^4+\gamma x^3)
\left(1+\frac\gamma{x^3}(y-1)\right)
=\frac{10}{9}x^2+\frac{10}{9}\gamma x+1.
\tag{B4.1}
\]

Since

\[
1+\frac\gamma{x^3}(y-1)
=1+\frac\gamma x+\frac{\gamma^2}{x^2}>0,
\]

the strict upper bound on \(\eta\) and (B4.1) imply

\[
\begin{aligned}
Q(y)
&>\frac{10}{9}x^2+\frac{10}{9}\gamma x+1
-\frac{x^2}{2}\left(1+\frac\gamma x+\frac{\gamma^2}{x^2}\right)\\
&=\frac{11}{18}x^2+\frac{11}{18}\gamma x+\frac59>0.
\end{aligned}
\tag{B4.2}
\]

Here \(10/9-1/2=11/18\) and \(1-\gamma^2/2=1-4/9=5/9\). This exact subtraction removes the need for the old \((x-120)^2\) step altogether. If its auxiliary estimate is retained in a formal proof, its replacement at the present onset is simply

\[
\frac{\gamma^2}{x^2}
<\frac{8}{9\cdot46^2}=\frac2{4761}<\frac12,
\tag{B4.3}
\]

using \(x>46\), \(46^2=2116\), and \(4<4761\). Inequality (B4.2) does not require this auxiliary estimate.

The leading coefficient of \(Q\) is 1. Its constant term is
\(-C(1-\gamma/x^3)<0\), because \(x\ge1\) gives \(\gamma/x^3\le\gamma<1\). Hence \(Q\) has exactly one positive root. The hypothesis is \(Q(k)\le0\); (B4.2) and \(y>0\) put \(y\) strictly above that root. It follows that \(k<y\), as claimed. ∎

### Combining the supplied finite certificate with B3 and B4

The two supplied estimates remain unchanged:

\[
N+\frac23(T-1)\le x^4+\gamma x^3,
\tag{B1}
\]

\[
a_T=\frac{2(2T+1)}{3T(T+1)}\le\frac\gamma{x^3}.
\tag{B2}
\]

For completeness concerning signs, if \(k=0\), the desired cardinality bound is immediate. If \(k\ge1\), both factors in the given finite certificate are positive, and \(k-1\ge0\). Thus B1 and B2 can be applied to the first and second factors, respectively, to give exactly the hypothesis of the scalar lemma. B3 supplies \(0\le\eta<x^2/2\). Translation gives the same strict Sidon-set bound as Route A for every integer \(N\ge4\,600\,000\).

Therefore 4,600,000 works for both routes; no fallback onset is needed.

## (iii) Elementary facts used and their proofs

The table collects the numerical certificates. Ordinary identities and differentiation rules for positive real powers, the exponential, and the logarithm are standard real calculus; the table supplies the bounds rather than assuming numerical approximations to those functions.

| Fact | Exact proof or integer comparison |
| --- | --- |
| \(u=463/10<x_1\) | \(463^4=45\,954\,068\,161<46\,000\,000\,000=10^4N_1\); positive fourth powers preserve order. |
| \(4631/100<x_1<4632/100<47\) | The two fourth powers are displayed at the beginning; \(4632<4700\). |
| \(x_1^2>2144\) | \(2144^2=4\,596\,736<4\,600\,000\). |
| \(0<s=\sqrt2<99/70<2\) | \(9800<9801\) and \(99<140\); compare positive squares. |
| \(0<\gamma<1\), \(\gamma^2=8/9\) | \(\gamma=2s/3>0\); its square is \(8/9\), and \(8<9\). |
| \(\alpha=296/1029+R\), \(0<R<1/41160\) | Substitute \(t=(v-1)/(v+1)\) in \(\int_1^{4/3}dv/v\). Then \(R=2\int_0^{1/7}t^4/(1-t^2)\,dt\). Positivity gives the lower bound. Since \(1/(1-t^2)\le49/48\), strict on the interior, \(R<(49/24)\int_0^{1/7}t^4dt=1/41160\). |
| \(\alpha>719/2500\) | \(296\cdot2500=740000>739851=719\cdot1029\). |
| \(\beta u>941/100\) | \(719\cdot463\cdot70\cdot100=2\,330\,279\,000>2\,328\,975\,000=941\cdot2500\cdot10\cdot99\). |
| \(e^3>1003/50\) | The series through degree 9 is \(22471/1120\), with strictly positive tail; \(22471\cdot50-1003\cdot1120=190>0\). |
| \(e^{41/100}>3/2\) | The series through degree 3 is \(9033221/6000000\), with strictly positive tail; \(9033221-9000000=33221>0\). |
| \(e^{941/100}>12100\) | The exponential addition identity follows by the Cauchy product of its absolutely convergent series. Use the preceding two rows and \(3\cdot1003^3-12100\cdot2\cdot50^3=2\,081\,081>0\). |
| Endpoint bracket in \(F(u)\) is less than \(67\) | \(45837<45850\), \(463>460\), and \(2\cdot721=1442<1587=3\cdot529\); the two summands are less than \(131/2\) and \(3/2\). |
| \(10/9-134/121=4/1089>0\) | \(10\cdot121-134\cdot9=4\), and \(9\cdot121=1089\). |
| \(q^{32}<1/9900\) | The full integer comparison is (B3.3); its positive gap is \(101\,844\,204\,076\,325\,716\). |
| \(2001/9900=667/3300<1/2\) | Divide numerator and denominator by 3, then compare \(1334<3300\). |
| \(e<3\), used only to diagnose a discarded bound | In \(e=\sum_{j\ge0}1/j!\), \(j!\ge2^{j-1}\) for \(j\ge2\), strictly for \(j\ge3\). Hence \(e<2+\sum_{j=2}^{\infty}2^{-(j-1)}=3\). The geometric tail after degree \(m\ge2\) is \(2^{1-m}\), so this comparison has an explicit convergent tail bound. |

Only positivity of the omitted exponential-series tails is used in lower bounds; no unstated remainder approximation is used.

## (iv) Exact rational slack certificates at the onset

The true differences at \(x_1\) involve radicals and, in Route A, an exponential. The following are exact rational lower bounds for those differences, not an assertion that the differences themselves are rational.

For Route A, (6.7) and \(x_1^2>2144\) give

\[
\frac{P_\varepsilon(y)}{x_1^2}>\frac4{1089},
\qquad
P_\varepsilon(y)>\frac{8576}{1089}>0.
\tag{S-A}
\]

The rational comparison closing the endpoint certificate has slack exactly \(4/1089\): it is the difference between the retained normalized main term \(10/9\) and the rational error bound \(134/121\).

For Route B, the uniform normalized B3 slack is

\[
\frac12-\frac{\eta}{x^2}>\frac{983}{3300}.
\tag{S-B-global}
\]

An additional exact check at \(N=N_1\) gives the larger onset-specific absolute certificate. Since

\[
140469^4=389\,333\,669\,232\,539\,881\,521
<4N_1^3=389\,344\,000\,000\,000\,000\,000
<389\,344\,756\,029\,676\,810\,000=140470^4,
\]

we have \(140469<s x_1^3<140470\), so \(T=140470\). Also

\[
32T=4\,495\,040\le4\,599\,999<4\,635\,510=33T,
\]

so \(r=32\) at the onset. Thus

\[
\eta_1=29\cdot140470\left(\frac34\right)^{32}
=\frac{3\,774\,259\,315\,956\,262\,526\,415}
{9\,223\,372\,036\,854\,775\,808},
\]

\[
\frac{x_1^2}{2}-\eta_1
>1072-\eta_1
=\frac{6\,113\,195\,507\,552\,057\,139\,761}
{9\,223\,372\,036\,854\,775\,808}>0.
\tag{S-B-onset}
\]

The numerator is a displayed positive integer. This onset check is supplementary: uniformity was already proved by (B3.1)–(B3.4), not inferred from this one value of \(N\).

For the scalar lemma, even using only \(\eta<x_1^2/2\), (B4.2) gives

\[
Q(y)>\frac{11}{18}x_1^2+\frac59
>\frac{11\cdot2144+10}{18}=\frac{11797}{9}>0.
\tag{S-B-scalar}
\]

## (v) Checks, discarded approaches, limits, and cost

**Exact checks run.** The final checker passed all 61 exact assertions. Node.js BigInt rational arithmetic was used on the following objects: the fourth powers of 463, 4631, and 4632; \(2144^2\); the logarithm/exponent cross products; exponential Taylor sums at 3 through degrees 8, 9, and 10, and at 41/100 through degree 3; the integer certificate for \(q^{32}\); the fourth powers bounding the onset ceiling \(T\); the products bounding the onset floor \(r\); and both exact onset fractions in (S-B-onset). The proof's polynomial identities and the floor-comparison numerator were also checked by exact coefficient arithmetic in \(\mathbb Q[s,x,x^{-1}]/(s^2-2)\). The checker additionally checked the large onset integers as transcribed in the report. These are arithmetic and algebra checks, not enumeration of Sidon sets or tests on a sample of large \(N\).

An initial floating-point evaluation was used only to locate useful rational constants and detect the incorrect bracket in the brief. No floating-point result is a premise of the proof. An early scratch command had a JavaScript Number/BigInt type mismatch and stopped without producing a certificate; it was corrected before the exact checks. All proof certificates are the displayed integer/rational comparisons.

**Discarded approaches and their exact obstructions.**

1. The old envelope \(200xe^{-x/6}<1/32\) cannot certify this onset. Since \(46<x_1<47\), \(x_1/6<8\), and \(e<3\), that envelope at the onset is greater than \(9200/6561>1/32\); the last comparison is \(294400>6561\). The present proof instead bounds the normalized actual error, using the logarithm integral.
2. Combining only \(P_0(y)\ge x^2\) with our new error bound \((134/121)x^2\) does not close the argument: \(134>121\). Retaining the unchanged identity's \((10/9)x^2\) term gives the positive difference \(4/1089\).
3. Freezing \(q^r\) at \(q^{32}\), while allowing the factor \(sx+x^{-2}\) to grow without relating it to \(r\), gives an unbounded upper envelope \(29(sx+x^{-2})q^{32}\) as \(x\to\infty\). The floor identity (B3.1) is what makes the bound uniform. Monotonicity of \(r(N)\) with a changing \(T\) was never assumed.
4. The degree-8 Taylor sum was insufficient for the chosen elementary bound \(e^3>1003/50\): its exact value is \(89641/4480\), and \(50\cdot89641-1003\cdot4480=-11390<0\). Degree 9 supplies the required positive gap 190. This was a failure of that truncation certificate, not a failure of the target onset.

**What is not proved.** No minimal onset is claimed, and no theorem for all integers below 4,600,000 is established. Lemma 7 and the finite Sidon certificate are used as supplied assumptions, not re-proved. No kernel formalisation or existing formalisation file was read or changed. The stronger scalar range \(x\ge1\) does not establish the finite-tail bound below the stated onset.

**Independent re-derivation before reporting.** After writing this report, the two polynomial expansions, the normalized-error monotonicity, both floor inequalities, the decreasing integer tail, the signs of both quadratic constant terms, and the endpoint certificates were re-derived from the written argument. An exact checker independently recomputed the polynomial coefficients and numerical certificates. This report's PROVED status rests on these derivations, not on numerical testing.

**Cost and next action.** One agent; no subagents, web searches, literature reads, SAT/ILP solvers, or paid compute. Computational checks use one arithmetic thread. The final 61-assertion check measured 943 microseconds of CPU time in the checker body, excluding interpreter startup. Each computational command completed in less than one second of wall time; the handful of commands is well below the one CPU-hour limit. No claim is made about unmeasured model-serving compute. Both requested proof routes are complete. Next action: the coordinator may review this report and transpose its constants and floor estimates into the existing formalisation; no additional work is needed to complete this assignment.
