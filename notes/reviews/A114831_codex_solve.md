# Solution

Write (A_n=a(n)), and for (n\ge 2) define

\[
R_n=\frac{A_n}{A_{n-1}}.
\]

We will prove that (R_n\to \sqrt 3), with an explicit error bound.

First observe that for any positive integers (x,y),

\[
2xy-x-y=x(y-1)+y(x-1)\ge 0.
\]

Consequently,

\[
\frac{2xy}{x+y}\ge 1.
\]

Thus the integer appearing inside the recurrence is always at least (1).
It follows that (A_n\ge A_{n-1}+1) for (n\ge3), and hence, using
(A_1=1,A_2=2),

\[
A_n\ge n \qquad(n\ge1).
\tag{1}
\]

In particular (R_n>1) for every (n\ge2).

For (n\ge3), let

\[
\theta_n=
\frac{2A_{n-1}A_{n-2}}{A_{n-1}+A_{n-2}}
-
\left\lfloor
\frac{2A_{n-1}A_{n-2}}{A_{n-1}+A_{n-2}}
\right\rfloor .
\]

Then (0\le\theta_n<1). Since (R_{n-1}=A_{n-1}/A_{n-2}), we have

\[
\frac{2A_{n-1}A_{n-2}}{A_{n-1}+A_{n-2}}
=\frac{2A_{n-1}}{R_{n-1}+1}.
\]

After dividing the defining recurrence by (A_{n-1}), this gives the exact
ratio recurrence

\[
R_n=1+\frac{2}{R_{n-1}+1}-\frac{\theta_n}{A_{n-1}}.
\tag{2}
\]

Define

\[
F(x)=1+\frac{2}{x+1}.
\]

The positive number (s=\sqrt3) is a fixed point of (F), because
((s-1)(s+1)=2), so

\[
F(s)=1+\frac{2}{s+1}=1+(s-1)=s.
\tag{3}
\]

Moreover, whenever (x,y\ge1),

\[
|F(x)-F(y)|
=\frac{2|x-y|}{(x+1)(y+1)}
\le \frac12|x-y|.
\tag{4}
\]

Put (E_n=|R_n-s|). Using (1)--(4), (R_{n-1}>1), and
(0\le\theta_n<1), we obtain for every (n\ge3)

\[
\begin{aligned}
E_n
&\le |F(R_{n-1})-F(s)|+\frac{\theta_n}{A_{n-1}}\\
&\le \frac12E_{n-1}+\frac1{A_{n-1}}\\
&\le \frac12E_{n-1}+\frac1{n-1}.
\end{aligned}
\tag{5}
\]

Iterating (5), and noting that (R_2=2), yields

\[
E_n\le 2^{-(n-2)}(2-\sqrt3)
+\sum_{j=3}^{n}\frac{2^{-(n-j)}}{j-1}.
\tag{6}
\]

For completeness, the sum in (6) can be bounded explicitly. Set
(K=\lfloor (n-2)/2\rfloor). For (n\ge4), after putting (k=n-j),

\[
\sum_{j=3}^{n}\frac{2^{-(n-j)}}{j-1}
=\sum_{k=0}^{n-3}\frac{2^{-k}}{n-k-1}.
\]

When (0\le k\le K), we have (n-k-1\ge n/2); when (k\ge K+1),
we use (n-k-1\ge2). Therefore

\[
\begin{aligned}
\sum_{k=0}^{n-3}\frac{2^{-k}}{n-k-1}
&\le \frac2n\sum_{k=0}^{K}2^{-k}
+\frac12\sum_{k=K+1}^{\infty}2^{-k}\\
&\le \frac4n+2^{-K-1}\\
&\le \frac4n+2^{-(n-2)/2}.
\end{aligned}
\tag{7}
\]

Combining (6) and (7), we have the fully explicit estimate

\[
\boxed{
\left|\frac{A_n}{A_{n-1}}-\sqrt3\right|
\le (2-\sqrt3)2^{-(n-2)}+\frac4n+2^{-(n-2)/2}
}
\qquad(n\ge4).
\tag{8}
\]

Every term on the right of (8) tends to (0). Hence (R_n\to\sqrt3).
Replacing (n) by (n+1) gives the requested limit:

\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{a(n+1)}{a(n)}=\sqrt3.}
\]
