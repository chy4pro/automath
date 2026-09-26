DONE — Codex (GPT-6); exact model variant and reasoning setting are not exposed in this session.

# Independent referee: Erdős 889

2026-09-26. Task 008. Verdict: **PASS-WITH-REPAIRS**. The proof establishes the stated lowercase finiteness theorem, with the exact main threshold

`N0 = exp(exp(45.28))`.

No change to that threshold is required. The uniform threshold remains `log log n >= 48.82`, together with `1 <= l <= log n`. The stronger optional threshold `44.96` also survives the algebra and independent numerical checks described below. This is an independent paper-level review by Codex after reading the Claude report; it is neither a blind review nor kernel formalization. It proves neither the largest-exception claim 330 nor the full divergence conjecture.

The required changes are one erroneous side-condition expression in the computation script, one rounded-down exact onset in the internal notes, an omitted zero in a historical statement, and an exact-count wording error in the published Langevin lemma proof. Exact replacement text is in §9. Other decimal equalities should be printed as approximations.

## 1. Definitions — VERIFIED, with the historical zero repaired in §9

I read the complete local Lean statement file. For `k >= 1`, `n+k >= 1`, and its filtered `primeFactors` definition equals the number of primes `p>k` dividing `n+k`: for `p<=k`, take `i=k-p`; for `p>k`, any earlier divisibility would imply `p | k-i` with `1<=k-i<=k`. Distinct primes, rather than prime powers or multiplicities, are essential here.

The supremum defining `v_l` takes values in extended naturals. One witness `k>=l` with `v(n,k)>=2` therefore suffices. For `n=0`, all `k>=1` give zero, so zero causes no problem in Corollary A1. At positive `n`, `v(n,1)=omega(n+1)>=1`; this also justifies the note's implication from lowercase finiteness to uppercase finiteness. The main proof does not assert a result about all levels of `v_l` or identify the complete finite exceptional set.

The introductory historical sentence uses the domain `n>=0` but omits zero from the exceptional list for `v_0(n)>1`. The local Lean file includes zero. Restrict that sentence to positive `n`, as in repair R3.

## 2. Lemma R — VERIFIED

All five parts hold with the stated domain `n>=2`, `l>=1`, and integer `Y=floor(y)>=l+2`.

1. If `p<=y` does not divide `Pi_l(n)`, then `p>l`, and the unique residue `k0` in `[0,p-1]` with `p | n+k0` lies in `[l,p-1]`. It is covered by (H). Since `p>k0` and (H) allows at most one such prime, every other prime factor is at most `k0`; thus `P(n+k0)=p`. This proves injectivity and the exact count `|J|=pi(y)-omega_{l,y}(n)`.
2. Fix a prime and choose an index of maximal valuation; ties can be resolved arbitrarily. At every other index the prime-power component divides the nonzero difference of indices. Summing valuations is bounded by those of `(j_p-l)!(Y-1-j_p)!`, which divides `(Y-l-1)!`. Multiplying these primewise inequalities proves the factorial bound. Primes with zero valuation contribute the factor one and cause no problem.
3. On `J0`, `W_j=n+j>n`, so `|J0| log n <= log((Y-l-1)!)`. Since the sets of primes assigned to different indices are disjoint, `sum s(j)<=pi(y)`. Combining this with `|J|=pi(y)-omega_{l,y}` gives `|J1|>=pi(y)-2omega_{l,y}-2|J0|>=A`. No ordered-pair or multiplicity factor is missing.
4. On `J1`, precisely one prime has a positive assigned valuation. Its prime power is `U_j`, it does not divide `W_j`, and the assignment makes these primes distinct between indices.
5. `A>1` forces `|J1|>=2`. If the cofactor logarithms are ordered increasingly, the second smallest times `|J1|-1` is at most their total, which is at most the logarithm of the factorial. The denominator is consequently `A-1`, as printed. Using `A` here would be unjustified; the proof does not do so.

These are integer and real inequalities, not conclusions inferred from the finite check.

## 3. Baker step and Matveev — VERIFIED

I fetched and read the English translation of [Matveev, Izvestiya Mathematics 64 (2000), Corollary 2.3](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng), including the definitions on pp.1218–1219. For a nonzero linear form in fixed nonzero logarithms, the corollary permits `A_j >= max(D h(alpha_j), |log(alpha_j)|, 0.16)` and expressly permits replacement of its weighted `B` by `B*`. In the real rational case, its constant is

`C1(t)=min((e*t/2)*30^(t+3)*t^(7/2), 2^(6t+20))`.

No linear-independence hypothesis is imposed by this corollary. The stronger earlier theorem must not be confused with this statement.

Here `Lambda=log(n+j1)-log(n+j2)` is nonzero because the indices are distinct. The mean value theorem gives the stronger bound `|Lambda|<Y/n`, hence also the requested `2y/n`. Both inequalities have the direction required when taking negative logarithms.

When `W1!=W2`, use the positive rationals `q1,q2,W1/W2` with coefficients `e1,-e2,1`. Reducing the rational quotient can only lower its numerator and denominator, so its height and absolute logarithm are both at most `max(log W1,log W2)<=T`. Thus `A1=log q1`, `A2=log q2`, and `A3=max(T,0.16)` satisfy all hypotheses, with real nonzero logarithms. Also `e_i log q_i < log(n+Y)`, whence `B* <= log(n+Y)/log 2`.

When `W1=W2`, omit the zero logarithm and use the two-logarithm corollary. Independently computed enclosures give

`139007316922.16412 < C1(3) < 139007316922.16414`,

`747318511.87413 < C1(2) < 747318511.87414`.

Both are the first branch of the minimum, and `C1(2)<0.16 C1(3)`. This verifies the domination of the two-logarithm case and Proposition B, including its strict inequality.

## 4. Prime-counting and omega inputs — VERIFIED

I read the original printed page 69 of Rosser–Schoenfeld from the [OEIS scan](https://oeis.org/A000720/a000720_8102163510_1.jpg). Corollary 1, (3.5), gives `pi(x)>x/log x` for real `x>=17`. Theorem 2, (3.3), gives `pi(x)>x/(log x-1/2)` for `x>=67`. The stronger inequality is only needed for the optional refinement.

I fetched the [Robin 1983 original scan](https://matwbn.icm.edu.pl/ksiazki/aa/aa42/aa4242.pdf) and visually read pp.368–369 after extracting the embedded page image in memory. Théorème 11 has the coefficient `1.3841` and domain `n>=3`; Théorème 13 has the denominator correction `1.1714` and domain `n>=26`. The proof uses distinct-prime `omega`, as those statements do. The thresholds under review are well inside both domains.

The reduction `omega_{l,y}(n)<=sum_{i<l}omega(n+i)<=l R(L+1)/ell` follows by bounding the numerator upward and the positive denominator downward. It does not require a monotonicity claim for their quotient. For `l<=L`, the bound `log(n+l-1)<=L+1` is valid.

## 5. Numerical chain — REPAIRED script check; theorem VERIFIED

I read the entire script and attempted the requested command with the local-bin PATH prefix. Python is absent. I therefore independently implemented directed integer interval arithmetic in Node, with no downloaded package; the main certificate code is reproduced below. This is not a rerun of mpmath and is not based on the Claude report's displayed numbers.

The interval arithmetic uses scale `10^50`, exact BigInt integer products, and signed floor/ceiling on every multiplication and division. Logarithms are reduced to `[1,2]` and evaluated with the convergent atanh series, retaining 120 terms and an explicit geometric tail bound. Exponentials are reduced by 128, use 100 Taylor terms plus twice the next term as an upper tail bound, then square seven times. All reduced positive exponential arguments are at most 1/2. Square roots of 2 and 3 use exact integer square roots with adjacent endpoints. No floating-point transcendental function determines an inequality sign.

The following are widened enclosing intervals, not merely rounded point estimates:

| Certificate | K or Ku | phi |
|---|---:|---:|
| fixed l=1, 45.27 | (241103976314.5540, 241103976314.5542) | (-0.001716921625, -0.001716921623) |
| fixed l=1, 45.28 | (241092138022.6873, 241092138022.6874) | (0.007227817705, 0.007227817706) |
| uniform, 48.81 | (5734435598882.0865, 5734435598882.0868) | (-0.007186497716, -0.007186497715) |
| uniform, 48.82 | (5734271542485.3110, 5734271542485.3113) | (0.001817836352, 0.001817836354) |

At 45.28, the independently enclosed values are `kappa1≈1.05085214427990`, `kappa2≈1.03017917227433`, `kappa3≈1.52457710225535`, `eps2≈1.35404300089081e-16`. In particular,

`4.6222575508435408775e19 < exp(45.28) < 4.6222575508435408776e19`.

All numerical side conditions at these four endpoints pass, including the *correct* condition `10*l*exp(ell1)>67`. The original Python script mistakenly tests `10*l*exp(exp(ell1))>67`; this does not invalidate the paper's elementary proof of the correct condition, but the script's label is false. Apply R1.

I checked S1–S7 algebraically. In particular, with `F=log((Y-l-1)!)`, the integral bound gives `F<=clL(ell+m-1)+l+2`; the resulting `A-1` has the printed error term, including its final `+1`. The relative error is bounded by `eps2` using decreasing `ell^2 exp(-ell)`, and the ratio `(ell+m-1)/(ell-mu)` decreases because `m-1+mu>0`. Thus `T<=kappa3 ell^2`; no factor of `l` is dropped. The final added `kappa1/ell1^4` accounts for `log Y`.

For a chosen endpoint, freeze its K. Then `(ell-5 log ell)'=1-5/ell>0` for `ell>5`. This propagates the strict contradiction from 45.28 to every larger `ell`. Independently, K as a function of the trial endpoint decreases on its admissible domain for fixed `l`: each positive factor in its displayed formula decreases, while `1-eps2` increases. This supports the least-grid assertion, rather than merely checking two isolated endpoints.

I also evaluated every printed fixed-l row for `l=1,...,20` and its predecessor on the 0.01 grid. All selected endpoints pass and all predecessors fail. The sequence reproduced is

`45.28, 45.35, 45.39, 45.42, 45.44, 45.46, 45.48, 45.49, 45.50, 45.51, 45.52, 45.53, 45.54, 45.54, 45.55, 45.56, 45.56, 45.57, 45.57, 45.58`.

For the optional refinement, I checked the replacement denominator, the weighted B parameter, and the two-logarithm comparison. Independent interval evaluations give `1.002174797450<Q(44.95)<1.002174797451` and `0.993290452437<Q(44.96)<0.993290452438`. The stated side conditions pass. The claimed derivative bound applies to the sum because each positive summand has logarithmic derivative at most `4/ell+1/(ell-d')-1`; this upper bound is negative on the stated range. The refined result does not alter how Theorem A itself is stated.

## 6. Uniform-in-l version — VERIFIED; exact onset wording REPAIRED

The quantifiers are `for all integers l>=1 and n with ell>=48.82 and l<=L`. Since `log c<=m<=ell+log c`, the denominator changes from `c-2R` to `c-4R`. The proof correctly changes all corresponding factors, rather than simply reusing the fixed-l constants. In particular, `a>= (c-4R)(ell-mu_u)/(ell(2ell+log c))`, the factorial numerator uses `2ell+log c-1`, and the error coefficient starts at `4c`.

At 48.82 the interval calculation gives `kappa3_u≈9.57515341656`, `eps2_u≈2.86646425700e-17` and the positive phi in the table. Uniformity in `l` is preserved throughout. The exact onset is

`N(l)=max(exp(exp(48.82)), ceil(exp(l)))`,

with `1.593149774842546995184e21 < exp(48.82) < 1.593149774842546995185e21`.

The internal §8 replacement `exp(1.59e21)` is a smaller number and is not licensed by rounding. Use the exact expression above (R2). The published theorem already uses the correct exact expression.

For completeness, the general-c proposition's reused preliminary inequality `c L^2<n` is automatic from its certificate, although this is not spelled out. For `c>4R` and admissible `z>=10`, its factors give `kappa3_u>1`, `kappa2>1`, and `K_u>C1(3)(log c/z)^2`. Thus its phi condition forces `exp(z)>C1(3)(log c)^2 z^3>log c+2z`. Since `exp(ell)-2ell` increases for `ell>=z`, `log c+2ell<exp(ell)=L`. This establishes `cL^2<exp(L)` without silently assuming c is small. For the stated c=10 theorem, the much simpler preliminary estimate in the paper suffices.

## 7. Langevin route — VERIFIED statement and deduction; proof not re-refereed

I fetched [Langevin's original 1981 article](https://matwbn.icm.edu.pl/ksiazki/aa/aa39/aa3932.pdf) and visually read the original page images for pp.241–243. Theorem 1's parameter ranges, condition (1), the example parameters on p.242, and Corollary 1(8) match the note's use. In particular, the smooth-number branch has coefficient `1+c+epsilon` and its r-condition has exponent `(1+c)/epsilon`; confusing it with the adjacent branch would change the constants.

With `a=1`, `t1=1/2`, and `k=floor(10 log n)`, all arithmetic hypotheses hold for large n. The ratio `log n/log k` tends effectively to infinity, as does `X=log n/(log k)^2`. The upper bound divided by `pi(k)` tends to zero, while Lemma R(1), Robin and Rosser–Schoenfeld give a lower proportion at least `1-R/10-o(1)>0`. This is an effective contradiction; no ineffective prime-number theorem is needed.

Uniformly for `1<=l<=L`, take `k=floor(10lL)`. Then `log k<=2ell+log 10`, `X>=L/(2ell+log 10)^2`, and the missing-prime proportion is at most `2R/10+o(1)<1`. Thus the asserted qualitative uniform version also follows.

The proof of the published auxiliary lemma wrongly calls `pi(K)-omega(n)` the exact number of primes at most K not dividing n; the true count uses only prime divisors at most K. Its stated *lower bound* remains correct. R4 repairs this sentence without changing the deduction.

I did not reprove Langevin's theorem. I verified its statement and applicability, not every line of its proof. The note already labels its approximate comparison of Langevin's onset as unverified; that comparison is unnecessary and should be replaced by the modest wording in R6 if a fully audited exposition is desired.

## 8. Scope and novelty wording — REPAIRED historical sentence; no priority certification

The explicit exclusion of the original divergence conjecture and of the proposed largest exception 330 is appropriate. The note credits Langevin for the qualitative consequence and does not claim that it is a newly proved qualitative theorem. The explicit threshold is a mathematical output verified above; this review does not establish that no prior work contains the same or a stronger result.

The historical introduction should use positive n, and decimal approximations must not be used as exact defining onsets. The distinction between paper proof, finite computation, Claude review and formal verification must remain. This Codex report supplies a separate vendor's mathematical review, not a Lean proof.

I did not independently verify the exact 1967 quotation, all later historical citations, the Kitamura repository claim, or the absence of a stronger earlier threshold. Those are outside the mathematical certificate, and should not be promoted into a priority claim based on this review.

## 9. Exact repairs

These are proposed replacements; I edited only this report, not the paper or script.

**R1 — Python side check (`fixed_l`).** Replace

`(c * L_ * iv.exp(iv.exp(l1)) - 67).a > 0`

by

`(c * L_ * iv.exp(l1) - 67).a > 0`.

Keep the existing label `y = c l L >= 67 (so >= 17)`. Rerun the script when Python is available. The independently checked correct inequality has ample margin.

**R2 — exact uniform onset, PROOF §8, item 2.** Replace that item by:

> An explicit uniform-in-l statement with C0=10 and N(l)=max(exp(exp(48.82)), ceil(exp(l))), plus sharper per-l values for l<=20. Here exp(48.82) is approximately 1.59315 × 10^21.

**R3 — published introduction.** Replace the historical sentence beginning “They showed” by:

> For positive integers n, they showed that v0(n)>1 except when n=1,2,3,4,7,8,16.

Alternatively add zero to the exception list while retaining n>=0. The first version avoids applying the historical prime-factor wording to zero.

**R4 — published Lemma 7.1 proof, last sentence.** Replace the exact-count sentence by:

> The number of primes p<=K with p not dividing n is pi(K)-#{p<=K:p divides n}, which is at least pi(K)-omega(n). By injectivity these yield at least pi(K)-omega(n) distinct k in [1,K] with P(n+k)<=K.

**R5 — decimal displays.** Use `approximately` or `≈`, not an exact equality, in `exp(45.28)≈4.6223×10^19`, `exp(48.82)≈1.593×10^21`, and `exp(44.96)≈3.356×10^19`. Retain the exact exponential expressions in theorem definitions. To express the finite containing set in Corollary A1, `{n in N:n<N0}` is cleaner than the nonintegral endpoint notation `{0,...,N0-1}`.

**R6 — optional editorial replacement for unverified Langevin threshold comparison.**

> Langevin's constants are effective. We have not computed a certified numerical onset for this alternative route and use it only to establish the qualitative consequence.

## 10. Read/execution record and limitations

Read in full: PROOF_THEOREM_A.md, CHECKS.md, n0_compute.py, REFEREE_CLAUDE_20260925.md, the local Lean 889.lean, and main.tex. Read the nine-page local main.pdf by extracting all page text streams and comparing the mathematical content against main.tex; PDF mathematical font decoding was lossy, so I do not claim a visual typesetting audit. Primary sources actually fetched and inspected are identified above; Robin and Langevin page images were decoded in memory without writing extra files.

SHA256 of reviewed inputs:

| Input | SHA256 |
|---|---|
| n0_compute.py | 997fc1afb6c1ab848a09e7385523b604e7430d9ff65d27d81fe6976677f6de57 |
| PROOF_THEOREM_A.md | 1b49f8b7d4cfd57658a9b4f06c68af1c5548490bd896820fa70f940da347fc99 |
| main.tex | f0e4647f0d164188804a329a824a6fe8ad1ee825044adf8fc52839f24dc86d49 |
| main.pdf | 52de225dc23795d330af49336595cee92575a03288b61ad7533b4fbd5b962ea0 |

The original Python program and its finite-check mode were not executable in this environment. I did not rerun the published million-integer checks, the Claude report's independent finite program, or the claimed computation through 10^7. None is used to establish the theorem. I did not run Lean, reconstruct external theorem proofs, audit publication metadata, or exhaust the prior-art literature. No new dependencies, cloud jobs, external messages, commits, or publication changes were made. The Node certificate and supplemental 20-row/refinement checks took under two seconds of command wall time in total; tool/network/model work was not separately metered.

The mathematical verdict remains PASS-WITH-REPAIRS, with unchanged exact N0.

## Appendix: independent interval certificate

The following dependency-free Node program is part of this report.

```javascript
'use strict';
const S=10n**50n;
const floor=(a,b)=>{if(b<0n){a=-a;b=-b;}let q=a/b;return a<0n&&a%b?q-1n:q;};
const ceil=(a,b)=>-floor(-a,b);
const I=x=>{let s=String(x),neg=s.startsWith('-');if(neg)s=s.slice(1);let [a,b='']=s.split('.');if(b.length>50)throw Error('precision');let v=BigInt(a)*S+BigInt(b.padEnd(50,'0'));return neg?[-v,-v]:[v,v];};
const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
const neg=a=>[-a[1],-a[0]], sub=(a,b)=>add(a,neg(b));
const min=a=>a.reduce((x,y)=>x<y?x:y),max=a=>a.reduce((x,y)=>x>y?x:y);
const mul=(a,b)=>{let v=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]];return[floor(min(v),S),ceil(max(v),S)];};
const div=(a,b)=>{if(b[0]<=0n&&b[1]>=0n)throw Error('division by zero');let v=[...a.flatMap(x=>b.map(y=>[floor(x*S,y),ceil(x*S,y)]))];return[min(v.map(x=>x[0])),max(v.map(x=>x[1]))];};
const pow=(a,n)=>{let v=I(1);for(let j=0;j<n;j++)v=mul(v,a);return v;};
const abshi=a=>max([a[0]<0n?-a[0]:a[0],a[1]<0n?-a[1]:a[1]]);
function logNear(a){const r=div(sub(a,I(1)),add(a,I(1))),r2=mul(r,r);let term=r,sum=I(0);for(let j=0;j<120;j++){sum=add(sum,div(term,I(2*j+1)));term=mul(term,r2);}let bound=div(mul(I(2),[0n,abshi(term)]),mul(I(241),sub(I(1),r2)))[1];return add(mul(I(2),sum),[-bound,bound]);}
const LN2=logNear(I(2));
function logPoint(v){if(v<=0n)throw Error('log domain');let y=[v,v],k=0;while(y[1]>2n*S){y=div(y,I(2));k++;}while(y[0]<S){y=mul(y,I(2));k--;}return add(logNear(y),mul(I(k),LN2));}
const log=a=>[logPoint(a[0])[0],logPoint(a[1])[1]];
function exp(a){if(a[1]<0n)return div(I(1),exp(neg(a)));if(a[0]<0n)throw Error('exp straddles zero');let x=div(a,I(128));if(x[1]>S/2n)throw Error('exp reduction');let sum=I(1),term=I(1);for(let j=1;j<=100;j++){term=div(mul(term,x),I(j));sum=add(sum,term);}let next=div(mul(term,x),I(101));sum=add(sum,[0n,2n*next[1]]);for(let j=0;j<7;j++)sum=mul(sum,sum);return sum;}
function isqrt(n){if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));for(;;){let y=(x+n/x)/2n;if(y>=x)return x;x=y;}}
function sqrtInt(n){let v=isqrt(BigInt(n)*S*S);return[v,v*v===BigInt(n)*S*S?v:v+1n];}
const R=I('1.3841'),c=I(10),C13=mul(mul(mul(div(mul(exp(I(1)),I(3)),I(2)),I(30**6)),I(27)),sqrtInt(3));
const C12=mul(mul(mul(exp(I(1)),I(30**5)),I(8)),sqrtInt(2));
function certificate(zText,uniform=false,l=1){const z=I(zText),m=log(I(10*l)),em=exp(neg(z)),den=sub(c,mul(I(uniform?4:2),R));const k1=add(I(uniform?2:1),div(m,z)),k2=add(I(1),div(add(sub(I(1),log(LN2)),em),z)),mu=div(mul(mul(I(2),R),m),den),ratio=div(sub(add(mul(I(uniform?2:1),z),m),I(1)),sub(z,mu)),eps1=div(mul(I(3),em),mul(c,sub(add(z,m),I(1)))),beta=add(mul(I(uniform?4:2),c),div(add(add(add(mul(mul(I(2),c),sub(m,I(1))),div(mul(I(2),R),z)),mul(I(6),em)),I(1)),z)),eps2=div(mul(mul(mul(beta,k1),pow(z,2)),em),mul(den,sub(I(1),div(mu,z)))),k3=div(mul(mul(mul(div(c,den),ratio),k1),add(I(1),eps1)),sub(I(1),eps2)),K=add(mul(mul(mul(C13,pow(k1,2)),k2),k3),div(k1,pow(z,4))),phi=sub(sub(z,mul(I(5),log(z))),log(K));const checks={z_ge_10:z[0]>=10n*S,mu_lt_z:mu[1]<z[0],eps2_lt_1:eps2[1]<S,Tcap_gt_point16:mul(k3,pow(z,2))[0]>I('.16')[1],y_gt_67:mul(I(10*l),exp(z))[0]>67n*S};return{z:zText,uniform,l,C13,C12,K,phi,k1,k2,k3,mu,eps1,eps2,logN:exp(z),checks};}
function endpoint(v){let sg=v<0n?'-':'';if(v<0n)v=-v;return sg+(v/S).toString()+'.'+(v%S).toString().padStart(50,'0');}
const json=x=>JSON.stringify(x,(_,v)=>typeof v==='bigint'?endpoint(v):v);
for(const z of ['45.27','45.28'])console.log(json(certificate(z)));
for(const z of ['48.81','48.82'])console.log(json(certificate(z,true)));
if(C12[1]>mul(I('.16'),C13)[0])throw Error('two-log domination fails');
if(C13[1]>I(2**38)[0]||C12[1]>I(2**32)[0])throw Error('Matveev minimum branch');
console.log('All four side-condition sets: '+['45.27','45.28','48.81','48.82'].every((z,i)=>Object.values(certificate(z,i>1).checks).every(Boolean)));
```
