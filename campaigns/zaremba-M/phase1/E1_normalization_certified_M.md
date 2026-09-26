CONDITIONAL — the gain scale and conditional arithmetic are determined; no unconditional numerical Zaremba digit bound or full-chain prime onset is certified.

# E1 normalization and the conditional Zaremba ledger

Task 015, 2026-09-26. This is ordinary, literature-informed integration work; task 012's earlier isolation does not apply here. The context read was R2_E1, the completed R2_E1b, G0, F1, and phase0/B_ledger.py. STATUS is maintained by the parent. STOP was absent. No numerical campaign, dependency installation, git operation, or external communication was performed. Tool metadata exposes no global-memory recall tool; no preset result or notice is invented.

**Answer to the decisive question:** E1 proves a genuine squared-mass contraction by $p^{-2c}$ for conjugacy-invariant probability measures. For $c=1/120$ this is $p^{-1/60}$. It is not a contraction whose exponent must first be multiplied by $\tau/6$. Task 011-B does not prove that the actual measures satisfy the hypotheses needed to transfer this gain.

With $\tau=1/4$ and the initial entropy $h_0=1/24$ supplied by an exact all-coset cap, the requested deliberately pessimistic substitution gives $k=5641$ and the limiting printed-prefactor ledger $\log_2 M=5669.276635148\ldots$. The analogous printed $c_K=1/1640$ row gives $k=77081$ and $77113.049224652\ldots$. These are conditional accounting outputs. The correct E1 gain instead gives $k=119$, and a directly derived spectral ledger gives $139.106710147\ldots$ before integer and assembly margins. None of these numbers currently has a proved full-chain onset $p_0$.

## 1. E1's exact theorem and the conversion of parameters

Use counting measure on $G=\mathrm{SL}_2(\mathbf F_p)$, with $Q=|G|=p(p^2-1)$, $u=Q^{-1}$, $Z=\{\pm I\}$, and

\[
 t(\mu)=\|\mu-u\|_2^2=\|\mu\|_2^2-Q^{-1},
 \qquad a=\tau/6.
\]

[R2_E1, Proposition 1](/work/campaigns/zaremba-M/phase1/R2_E1.md) states:

\[
 \boxed{t(\mu*\mu)\le [\mu(Z)+5p^{-1/2}]^2t(\mu).}       \tag{1}
\]

Its hypotheses are $p\ge5$ and that $\mu$ is a conjugacy-invariant probability measure. Symmetry is unnecessary. If $\mu(Z)\le p^{-a}$ and

\[
 0<c<\min\{a,1/2\},\qquad
 p\ge P_{\mathrm{central}}(a,c)
 :=\max\{5,2^{1/(a-c)},10^{1/(1/2-c)}\},
\]

then it proves, with coefficient one and no upper or lower energy restriction,

\[
 \boxed{t(\mu*\mu)\le p^{-2c}t(\mu).}                    \tag{2}
\]

The all-coset hypothesis implies the center-mass hypothesis by taking $H=Z$. Each of $p^{-a}$ and $5p^{-1/2}$ is at most $\tfrac12p^{-c}$ at the displayed onset.

The proof identifies every nontrivial Fourier block with $z_\rho I$. Character-column orthogonality, $|C_G(g)|\le2p$ for $g\notin Z$, and $d_\rho\ge(p-1)/2$ give $|z_\rho|\le\mu(Z)+5p^{-1/2}$. Plancherel then compares the sums $Q^{-1}\sum d_\rho^2|z_\rho|^4$ and $Q^{-1}\sum d_\rho^2|z_\rho|^2$. This derivation establishes the unit of the exponent without relying on a name attached to $c$.

For $\tau\ge1/5$, $a\ge1/30$, $c=1/120$ gives

\[
 \gamma:=2c=1/60,\qquad P_{\mathrm{central}}\le2^{40}.
                                                               \tag{3}
\]

At $\tau=1/4$ alone the displayed central theorem even allows the smaller sufficient bound $2^{30}$. Neither bound is a Zaremba onset.

The literal survey convention in G0 and F1 is

\[
 t_{j+1}\ll K_*^{-c_K}t_j,\qquad K_*=p^{\tau/6}.
\]

Thus the exact conversion, when comparing the same squared-mass gain, is

\[
 \gamma=\frac{\tau c_K}{6}=2c,
 \qquad \boxed{c_K=\frac{12c}{\tau}}.                    \tag{4}
\]

For E1's $c=1/120$, $c_K=2/5$ at $\tau=1/4$, and $c_K=1/2$ at $\tau=1/5$. Equivalently, writing the gain as $K_*^{-2c'}$ would require $c'=6c/\tau$; it would not justify keeping $c'=c$.

The same-numeral substitution $c_K=1/120$ requested by the task is a permissible weakening of (2) only where (2), or a valid transfer of it, applies. It changes $\gamma$ from $1/60$ to $1/2880$ at $\tau=1/4$, or to $1/3600$ at $\tau=1/5$. These are respectively 48 and 60 times smaller. The large ledger that results is not a normalization objection to E1's proved restricted theorem.

## 2. What task 011-B proves, and a conditional endpoint extension

[R2_E1b, Branch B](/work/campaigns/zaremba-M/phase1/R2_E1b.md) proves that the actual laws are correlations

\[
 \mu_r=(\nu*\widetilde\nu)^{*r},
\]

with word multiplicities. Every positive convolution power is noncentral in the stated application ranges. The argument uses positive semidefinite Fourier blocks: if a positive power of such a block is scalar, its positive root is scalar. A noncentral initial support therefore cannot become central at a positive integer time.

For a symmetric probability measure define the least central pointwise-majorant mass

\[
 B(\mu)=\sum_{\mathcal C}|\mathcal C|\max_{x\in\mathcal C}\mu(x).
\]

The report proves the unconditional transfer inequality

\[
 t(\mu*\mu)\le
 [\mu(Z)+5B(\mu)p^{-1/2}]^2t(\mu)
 +\frac{B(\mu)^2-1}{Q}.                                  \tag{5}
\]

Consequently, a bound $B(\mu)\le Cp^\beta$, together with $\mu(Z)\le p^{-a}$ and $c<\min\{a,1/2-\beta\}$, supplies (2) on the original range $t(\mu)\ge p^{-2+2c}$ for an explicitly testable sufficiently large prime. That range alone does not cross the strict Frobenius threshold $p^{-2}$.

Here is a sufficient extension, derived directly from (5). It is conditional on the same kind of majorant estimate at the relevant stages, with a stronger margin:

\[
 C\ge1,\qquad
 0<c<a,\qquad \beta<1/2-3c.
                                                               \tag{6}
\]

Then (2) holds throughout $t(\mu)\ge p^{-2-4c}$ whenever

\[
 \boxed{
 [p^{-(a-c)}+5C p^{-(1/2-\beta-c)}]^2
 +\frac{C^2p^{-(1-2\beta-6c)}}{1-p^{-2}}\le1.}             \tag{7}
\]

Indeed, divide (5) by $p^{-2c}t(\mu)$. The additive term is at most

\[
 \frac{C^2p^{2\beta}}
 {p^3(1-p^{-2})\,p^{-2c}\,p^{-2-4c}}
 =\frac{C^2p^{-(1-2\beta-6c)}}{1-p^{-2}}.
\]

All three power margins in (7) are positive under (6). This proves the extension; it does not prove the missing majorant estimate. A convenient explicit sufficient onset is

\[
 P_{\mathrm{env}}(a,c,\beta,C)=
 \max\left\{
 5,\ 
 4^{1/(a-c)},\
 (20C)^{1/(1/2-\beta-c)},\
 ((8/3)C^2)^{1/(1-2\beta-6c)}
 \right\}.                                               \tag{8}
\]

The first two summands inside the square brackets of (7) are then at most $1/4$ each. Its remaining summand is at most $1/2$, using $1-p^{-2}\ge3/4$, so the left side is at most $3/4$.

For a concrete conditional example, take $a=1/30$, $c=1/120$, and $\beta=9/20$. The three margins are $1/40$, $1/24$, and $1/20$:

\[
 P_{\mathrm{env}}\le
 \max\{5,2^{80},(20C)^{24},((8/3)C^2)^{20}\}.              \tag{9}
\]

If the unproved envelope had $C=1$, the sufficient bound $p\ge2^{104}$ would establish this extended flattening statement. The coefficient $C$ has not been supplied for the actual walk. Formula (9), not $2^{40}$, illustrates the additional onset cost of this particular transfer.

The initial measures cannot satisfy the needed small envelope. Branch B proves $B(\mu_r)\gg p^{19/10}$ in the MMS seed-length convention, and $\gg p^{3/2}$ in the appendix seed-length convention. Its longer integer-lift argument gives $B(\mu)\gg_\epsilon p^{1-2\epsilon}$; in particular $p^{3/4}$ for $\epsilon=1/8$. These exclude $\beta<1/2$ there. Later-stage envelope control remains open.

Below, $d$ denotes a fixed number of extra seed doublings needed before a hypothetical usable envelope begins. It is not the word-length coefficient $b$. Replacing $m$ by $2^dm$ multiplies the inverse spectral exponent by $2^d$ and adds $d$ to every logarithmic ledger shown. No value of $d$, including the illustrative $d=4$ in Branch B, is currently proved sufficient.

## 3. Initial entropy, iteration, and the direct spectral coefficient

Let the original seed length satisfy $m_0\le b\log_Np$. After $d$ separately charged doublings, let the law at the beginning of the certified flattening interval be

\[
 \mu_0=(\nu*\widetilde\nu)^{*m},\qquad
 m=2^dm_0\le2^db\log_Np,\qquad t(\mu_0)\le p^{-h_0}.
\]

The interval length $N$ is unrelated to $Q=|G|$. Throughout the formulas below, $b$ retains the original seed coefficient and $d$ is charged explicitly, exactly once.

An exact all-coset cap $p^{-a}$ implies $h_0=a$: choose the trivial subgroup to obtain $\|\mu_0\|_\infty\le p^{-a}$, then $\|\mu_0\|_2^2\le p^{-a}$. This implication is proved; its application still requires the cap for the actual seed and actual integer length. The cap persists under convolution. The values $h_0=1/10,1/8,1/4$ below require stronger independent initial estimates. In particular the uniform, collision-free positive-word count is not automatically an estimate for the alternating correlation law. The value $h_0=0$ is always available for a probability measure.

Given a squared-mass gain $p^{-\gamma}$, define exact rational/integer quantities

\[
 R_0=\frac{2-h_0}{\gamma},\qquad
 k=\lceil R_0\rceil+1,\qquad
 v=h_0+k\gamma-2,\qquad \gamma\le v<2\gamma.               \tag{10}
\]

If the gain holds down to $p^{-2-2\gamma}$, then

\[
 t(\mu_0^{*2^k})\le p^{-2-v}.                              \tag{11}
\]

If an earlier iterate is already below the lower cutoff, ordinary $L^2$ contraction preserves a stronger bound. For E1 $\gamma=2c$, so the extension in §2 has exactly the needed cutoff. The central theorem needs no cutoff extension at all.

For the nontrivial singular norm $s$ of the original generator operator, positive semidefinite correlation blocks and Plancherel give

\[
 s^{4m2^k}\le\frac{Q}{(p-1)/2}\,t(\mu_0^{*2^k})
 \le 2(1+1/p)p^{-v}.
\]

Therefore, retaining an absolute coefficient in the incidence estimate yields the exponent

\[
 \boxed{\kappa_{14}=\frac{v}{4b\,2^{k+d}}.}               \tag{12}
\]

For example the spectral coefficient is at most $3^{1/4}$ when $p\ge2$ and $m\ge1$. The projective-line mean correction also has an absolute coefficient. Those coefficients must be retained in the final assembly onset. If instead one insists on absorbing the spectral coefficient into a pure power, the conservative G0 choice is $\kappa_{14}=v/(8b2^{k+d})$, with a further onset condition. That choice adds one bit to the direct ledger below.

The appendix uses $b=\tau=1/4$. MMS22 instead uses $b=\tau/4=1/20$ with $\tau=1/5$. These length conventions cannot be exchanged without checking the seed hypotheses. Direct-ledger numbers below use $b=1/4$ unless explicitly stated.

## 4. All overheads, and what the printed-prefactor ledger means

Separate the initial alphabet $M_0$, the enlarged alphabet $M_*$, and the final digit cap $M$. The phase-0 B ledger and G0 use

\[
 r=10,\quad u=99/100,\quad s_C=2,\quad \ell=4,\quad
 R=198/5,\quad \varepsilon\uparrow1/18.
\]

Here $N=p^{2\varepsilon}$, $N_*=N^{1/r}$, $1-w_{M_0}\le u/M_0$, $\kappa_C=\kappa_{14}/s_C$, $M_*\ge RM_0$, and the final conversion costs $\ell M_*$. The constant $R$ is the exact ratio from the printed dimension inequalities; the source rounds it up to $40$. The lower alphabet threshold is $1000$ and the prime-case auxiliary alphabet is $200$.

The sufficient strict alphabet condition and the real threshold are

\[
 M_0>\frac{ur s_C}{2\varepsilon\kappa_{14}},\qquad
 M_{\mathrm{thr}}=
 \ell\max\left\{R\max\left(1000,
 \frac{ur s_C}{2\varepsilon\kappa_{14}}\right),200\right\}.
                                                               \tag{13}
\]

Every row below is in the inverse-gap-dominated case. At the limiting phase-0 choices,

\[
 O_B:=\frac{\ell Rur s_C}{2\varepsilon}=\frac{705672}{25},
 \qquad \log_2O_B=14.784782051827\ldots .                  \tag{14}
\]

Using the literally printed rounded $R=40$ changes $O_B$ to $28512$, adding $\log_2(100/99)=0.014499569695\ldots$ bits. Taking the admissible $\varepsilon=1/20$ adds a further $\log_2(10/9)=0.152003093445\ldots$. With both choices $O_B=31680$, and the total addition to the displayed limiting ledgers is

\[
 \log_2(1000/891)=0.166502663140\ldots .                   \tag{15}
\]

Thus the numbers using $\varepsilon=1/18$ are infima in this part of the ledger, not attained full-chain certificates.

To reproduce the requested printed extraction, introduce a separate numerator $c_{\mathrm{pref}}$ and impose conditionally

\[
 \delta=\frac{c_{\mathrm{pref}}}{2^{k+d+4}},\qquad
 \kappa_{14}=\frac{\delta}{6}.
\]

Then

\[
 \boxed{F_{\mathrm{print}}=
 k+d+\log_2\left(\frac{96O_B}{c_{\mathrm{pref}}}\right).}   \tag{16}
\]

The $2^4$, the division by $6$, Corollary-16 division by $2$, $N_*$ division by $10$, dimension constants, and final factor $4$ are all present. The literal rows set $c_{\mathrm{pref}}=c_K$. For a comparison retaining the same conservative numerator on the true E1 row, set $c_{\mathrm{pref}}=c=1/120$; this is explicitly a retained extraction convention, not a consequence of relabeling (4). The two rational logarithm arguments used below are

\[
 \frac{96O_B}{1/120}=\frac{1625868288}{5},\qquad
 \frac{96O_B}{1/1640}=\frac{22220199936}{5}.                \tag{17}
\]

Under a proved constant-gain certificate, (12) instead gives

\[
 \boxed{F_{\mathrm{direct}}=
 k+d+\log_2(4bO_B/v).}                                   \tag{18}
\]

For $b=1/4$ the argument is simply $O_B/v$. Equations (16) and (18) should not be interchanged silently. The earlier F1 report used a different illustrative alphabet overhead; the present task uses the requested B_ledger.py convention.

## 5. Exact rational counts and numerical evaluations

All ceilings in these tables were computed with integer/rational arithmetic in Node. The displayed decimals are evaluations of the exact logarithms, not interval-certified enclosures. The relevant integer-power upper bounds were checked separately by BigInt comparison. Tables set $d=0$; add $d$ for a proved delayed entry.

### 5.1 Correct E1 gain, $\gamma=1/60$

These rows use $\tau=1/4$, $b=1/4$, and the true E1 gain. The printed-prefactor column retains $c_{\mathrm{pref}}=1/120$.

| $h_0$ | Exact $R_0$ | $k$ | Exact $v$ | $F_{\mathrm{print}}$ | $F_{\mathrm{direct}}$ |
|---:|---:|---:|---:|---:|---:|
| $0$ | $120$ | 121 | $1/60$ | 149.276635148 | 141.691672647 |
| $1/24$ | $235/2$ | 119 | $1/40$ | 147.276635148 | 139.106710147 |
| $1/10$ | $114$ | 115 | $1/60$ | 143.276635148 | 135.691672647 |
| $1/8$ | $225/2$ | 114 | $1/40$ | 142.276635148 | 134.106710147 |
| $1/4$ | $105$ | 106 | $1/60$ | 134.276635148 | 126.691672647 |

The exact direct logarithm arguments are $8468064/5$ when $v=1/60$ and $5645376/5$ when $v=1/40$. At $\tau=1/5$ and the cap entropy $h_0=1/30$, $R_0=118$, $k=119$, and $v=1/60$. With $b=1/4$ as a comparison convention this gives $F_{\mathrm{direct}}=139.691672647\ldots$; using the actual MMS length bound $b=1/20$ would subtract $\log_2 5$, conditional on its seed hypotheses.

### 5.2 Requested pessimistic rows at $\tau=1/4$

Here $\gamma=c_K/24$. Each exact input to the ceiling is the integer $k-1$. The gain and prefactor are deliberately kept distinct from the true E1 row.

| $h_0$ | $k$ for $c_K=1/120$, $\gamma=1/2880$ | $F_{\mathrm{print}}$, $c_{\mathrm{pref}}=1/120$ | $k$ for $c_K=1/1640$, $\gamma=1/39360$ | $F_{\mathrm{print}}$, $c_{\mathrm{pref}}=1/1640$ |
|---:|---:|---:|---:|---:|
| $0$ | 5761 | 5789.276635148 | 78721 | 78753.049224652 |
| $1/24$ | 5641 | 5669.276635148 | 77081 | 77113.049224652 |
| $1/10$ | 5473 | 5501.276635148 | 74785 | 74817.049224652 |
| $1/8$ | 5401 | 5429.276635148 | 73801 | 73833.049224652 |
| $1/4$ | 5041 | 5069.276635148 | 68881 | 68913.049224652 |

For example the cap-entropy entries are exactly

\[
 5641+\log_2(1625868288/5),\qquad
 77081+\log_2(22220199936/5).
\]

At the literally printed $R=40$ and the concrete $\varepsilon=1/20$, they become $5669.443137811\ldots$ and $77113.215727315\ldots$, before integer alphabet rounding. The integer choices from (19) below satisfy $M<2^{5670}$ and $M<2^{77114}$, respectively. These inequalities are verified arithmetic under the imposed spectral exponents, not unconditional Zaremba results.

The optimistic printed count $k=1641$ gives $1673.049224652\ldots$ through (16). It is not the literal count for $c_K=1/1640$. The printed equations also give

\[
 \kappa_{14}^{-1}=9840\,2^{1645},
 \qquad \log_2\kappa_{14}^{-1}=1658.264442600\ldots,
\]

so the separately printed lower bound $\kappa\ge2^{-1656}$ cannot be carried into the ledger.

### 5.3 The distinct $\tau=1/5$ convention

Here the literal gains are $1/3600$ and $1/49200$. Again each exact ceiling input is $k-1$.

| $h_0$ | $k$, literal $c_K=1/120$ | $F_{\mathrm{print}}$ | $k$, literal $c_K=1/1640$ | $F_{\mathrm{print}}$ |
|---:|---:|---:|---:|---:|
| $0$ | 7201 | 7229.276635148 | 98401 | 98433.049224652 |
| $1/30$ | 7081 | 7109.276635148 | 96761 | 96793.049224652 |
| $1/10$ | 6841 | 6869.276635148 | 93481 | 93513.049224652 |
| $1/4$ | 6301 | 6329.276635148 | 86101 | 86133.049224652 |

The unchanged printed-prefactor convention in this table is only a requested sensitivity calculation. If changing the source word-length convention, derive the coefficient through (12) rather than presuming that the appendix's division by $6$ transfers without proof.

## 6. Integer alphabets, onset, and the strongest honest theorem statement

For any actually established $\kappa_{14}$, choose rational $\varepsilon<1/18$ compatible with the rest of the assembly, and set

\[
 \begin{split}
 M_0&=\max\left\{1000,
 \left\lfloor\frac{ur s_C}{2\varepsilon\kappa_{14}}\right\rfloor+1\right\},\\
 M_*&=\lceil RM_0\rceil,\qquad
 M=\ell\max\{M_*,200\}.
 \end{split}                                              \tag{19}
\]

The strict $+1$ is necessary. It cannot be replaced by assuming the limiting real threshold is attained.

A particularly clean conditional implication uses the correct E1 gain, $h_0=a=1/24$, $b=1/4$, the extended envelope hypothesis of §2 after $d$ extra doublings, and the direct coefficient (12). It gives

\[
 k=119,\quad v=1/40,\quad
 \kappa_{14}=\frac1{40\,2^{119+d}}.
\]

With $R=40$ and $\varepsilon=1/20$, (19) is exactly

\[
 M_0=7920\,2^{119+d}+1,\qquad
 M=1267200\,2^{119+d}+160<2^{140+d}.                       \tag{20}
\]

The inequality follows from $1267200<2^{21}$ and the positive remaining integer margin. If using G0's exponent-halving convention, $2^{141+d}$ is the corresponding conditional cap.

Thus the following is a **conditional implication, not a theorem presently proved for the actual Zaremba walk**:

> If the actual seed at an explicitly bounded length has the exact $p^{-1/24}$ all-coset cap, and after a specified fixed $d$ doublings its required stages satisfy $B(\mu)\le Cp^\beta$ with explicit $C$ and $\beta<19/40$, and the remaining continued-fraction assembly and its coefficient-dependent onset hold for the parameters in (20), then every prime beyond the maximum of those explicit onsets admits a coprime numerator whose continued-fraction partial quotients are at most $2^{140+d}$.

For this implication a sufficient onset has the form

\[
 p_0\ge\max\{P_{\mathrm{seed}},P_{\mathrm{envelope}},
 P_{\mathrm{env}}(1/24,1/120,\beta,C),
 P_{\mathrm{assembly}}\}.                                \tag{21}
\]

$P_{\mathrm{seed}}$ includes interval floors, the exact alternating word length, and the actual cap coefficient. $P_{\mathrm{envelope}}$ is where the hypothesized later-stage bound begins. $P_{\mathrm{assembly}}$ includes the incidence coefficient, the $o_M(1)$ and prime-size inequalities in Section 5.4, and the fixed-alphabet counting constants. These quantities have not all been numerically extracted. If the seed or envelope is only asymptotic, its threshold is an additional unknown, even when (8) is explicit.

The pessimistic printed-prefactor alternative under the same cap entropy has the conditional cap $2^{5670+d}$. The printed $c_K=1/1640$ route has the conditional cap $2^{77114+d}$, but additionally needs a valid general-measure flattening theorem with that gain and its coefficients/onset. They do not inherit $2^{40}$ from E1.

To make the stated delay loss concrete, impose the still-unproved example $d=4$, $C=1$, $\beta=9/20$. The native E1 calculation then has 119 further doublings, 123 including the delay, limiting direct ledger $143.106710147\ldots$, and the conditional rounded cap $2^{144}$. The deliberately weakened E1 ledger becomes $5673.276635148\ldots$ and its rounded cap $2^{5674}$. Formula (9) gives a sufficient envelope-flattening onset $2^{104}$ even with the weaker $a=1/30$, but the seed, envelope-validity and assembly onsets in (21) remain unknown. Branch B's illustrative four-doubling charge is not a proof that this envelope holds.

The actual result currently certified is (1)–(3) for central measures, the general majorant inequality (5), and the conditional extension (6)–(8), together with their exact arithmetic consequences. **There is currently no supported unconditional statement of the form “all primes $p\ge p_0$ satisfy Zaremba with $M=2^X$” with both $X$ and the complete numerical $p_0$ extracted by this chain.**

## 7. Which missing hypotheses have proofs?

| Item | Status and relevance |
|---|---|
| Central-measure gain $p^{-1/60}$, coefficient one, onset $2^{40}$ for $\tau\ge1/5$ | Complete ordinary proof in E1. No BSG or set-growth input needed. |
| Actual walk is central | False in the application ranges: Branch B proves every positive convolution power is noncentral. |
| Least-majorant transfer (5) | Complete ordinary proof in Branch B. |
| Later-stage bound $B(\mu)\le Cp^\beta$ | Unproved. Initial versions are excluded by Branch B's support and integer-lift bounds. No $C,d$, or onset is certified. |
| Endpoint extension for an envelope | Proved conditionally here by (5)–(8), with $\beta<1/2-3c$. Branch B's original weaker condition alone is insufficient for this extension. |
| All-coset cap implies $h_0=a$ | Elementary complete implication. The numerical seed length/cap must still be identified correctly in the source chain. Stronger tabulated $h_0$ values remain additional assumptions. |
| Correlation symmetry and PSD Fourier blocks | Complete identities in Branch B; these justify the direct spectral calculation. They do not imply conjugacy invariance. |
| General BSG pair $(9,32)$ | Unverified in G0 and F1. Not needed by the hypothetical E1-envelope route. Needed, or replaced with a proved alternative, for the printed general flattening route. |
| Symmetric growth hypothesis for the printed BSG output | The cited theorem requires symmetry. G0/F1 prove a symmetrization repair with tripling exponent multiplied by $3$; that repair changes the exponent calculation, so it does not certify the unchanged printed $1/1640$. |
| Lemma 14 to Corollary 16, $\kappa_C=\kappa_{14}/2$ | G0 gives a complete simultaneous-shift/Cauchy–Schwarz repair. A separately quantitative Lemma 15 is unnecessary for that reduction. |
| Full finite-alphabet assembly and numerical $p_0$ | Not completed. In particular asymptotic coefficients and onsets cannot be inferred from the central theorem's $2^{40}$. |

There is also a route which does not assume a class envelope. Branch A of R2_E1b proves a weaker set estimate with exponents $(\eta,\theta)=(1/1611,1/11)$ and an explicit coefficient formula in two numerically unextracted growth constants. Its weighted transfer covers the extended range and permits

\[
 0<c<\min\{h_0/3224,\ a/23,\ 1/8\}.
\]

For comparison, with $b=1/4$ and the same limiting overhead, the following direct ledgers follow from that proved weaker estimate, conditional on the actual seed and assembly:

| $h_0$ | Chosen $c$ | Exact ceiling input $(2-h_0)/(2c)$ | $k$ | Exact $v$ | $F_{\mathrm{direct}}$ |
|---:|---:|---:|---:|---:|---:|
| $1/24$ | $1/77377$ | $3636719/48$ | 75766 | $49/1857048$ | 75795.994651883 |
| $1/30$ | $1/96721$ | $5706539/60$ | 95110 | $61/2901630$ | 95140.322476850 |
| $1/10$ | $1/32241$ | $612579/20$ | 30630 | $21/322410$ | 30658.691001595 |

The stronger desired set estimate $(1/20,1)$ remains unproved. The weaker theorem establishes an alternative asymptotic mechanism; it does not supply a numerical prime onset until its growth coefficient, size threshold, and downstream constants are extracted.

## 8. Source and verification scope

The primary sources underlying the cited audits are [Shkredov v2, Appendix and Section 5.4](https://arxiv.org/html/2603.14116v2), [MMS22, equations (15)–(19)](https://arxiv.org/html/2212.14646v1), and the [survey's journal record](https://www.mathnet.ru/eng/rm10029). The earlier isolated F1 audit independently fetched its stated primary sources; this task reads the now-authorized reports and derives the scale conversion, endpoint extension, direct coefficient, and rational ledgers explicitly above. It does not claim a new inspection of the final IMRN edition.

Only the named report was written. Small rational and BigInt operations checked every table ceiling and the integer upper bounds $2^{148}$, $2^{5670}$, $2^{77114}$ in their printed-prefactor cap-entropy cases, and $2^{140}$ in (20) at $d=0$. Adding $d$ follows symbolically. No floating-point spectral computation or new research campaign was run. These are ordinary mathematical proofs and arithmetic checks, not kernel formalization or independent cross-vendor review.
