'use strict';
// Read-only aggregation of saved experiments; writes the two task007 deliverables.
const fs=require('fs'),path=require('path');
const names=['grid_20260926.jsonl','refinement_20260926.jsonl','large_T1_1000003_20260926.jsonl','large_T1_1999993_20260926.jsonl','last_T1_1999993_N256_padded_invalid_20260926.jsonl','last_T1_1999993_N256_20260926.jsonl'];
const runs=names.map(name=>({name,rows:fs.readFileSync(path.join(__dirname,name),'utf8').trim().split('\n').map(JSON.parse)}));
const best=new Map();
for(const run of runs)for(const r of run.rows){if(run.name.includes("invalid")||!r.p||r.p<1009)continue;if(!(r.iterations>0)||!Number.isFinite(r.sigma_lower_estimate)||!Number.isFinite(r.residual_tstar_t)||(r.dimension!==undefined&&r.dimension!==r.p+1))throw Error("invalid numerical row");const key=[r.p,r.kind,r.N].join(',');if(!best.has(key)||r.sigma_lower_estimate>best.get(key).sigma_lower_estimate)best.set(key,{...r,source:run.name});}
const rows=[...best.values()].sort((a,b)=>a.p-b.p||a.kind.localeCompare(b.kind)||a.N-b.N);
if(rows.length!==40)throw Error('incomplete 40-point grid');
for(const p of[1009,10007,100003,1000003,1999993])for(const kind of['T1','T2'])for(const N of[4,16,64,256])if(!best.has([p,kind,N].join(',')))throw Error('missing expected grid point');
const cols=['p','kind','N','sigma_lower_estimate','residual_tstar_t','iterations','seed','free_T1_comparator','source'];
fs.writeFileSync(path.join(__dirname,'best_grid_20260926.csv'),cols.join(',')+'\n'+rows.map(r=>cols.map(k=>r[k]).join(',')).join('\n')+'\n');
let table='| Prime p | Operator | N=4 | N=16 | N=64 | N=256 | Largest residual in row | Certified upper bound |\n|---:|:---|---:|---:|---:|---:|---:|---:|\n';
for(const p of[1009,10007,100003,1000003,1999993])for(const kind of['T1','T2']){const rr=[4,16,64,256].map(N=>best.get([p,kind,N].join(',')));table+='| '+[p,kind,...rr.map(r=>r.sigma_lower_estimate.toFixed(9)),Math.max(...rr.map(r=>r.residual_tstar_t)).toExponential(2),'1'].join(' | ')+' |\n';}
const dense=runs[0].rows.filter(r=>r.sigma_svd);
let dt='| p | Operator | N | Dense SVD | Power estimate | Absolute difference |\n|---:|:---|---:|---:|---:|---:|\n';
for(const r of dense)dt+='| '+[r.p,r.kind,r.N,r.sigma_svd.toFixed(12),r.sigma_lower_estimate.toFixed(12),Math.abs(r.sigma_svd-r.sigma_lower_estimate).toExponential(2)].join(' | ')+' |\n';
const completed=runs.flatMap(run=>run.rows.filter(r=>r.complete).map(r=>({name:run.name,...r})));
const lower=completed.reduce((s,r)=>s+r.cpu_seconds,0)+1250;
const upper=completed.reduce((s,r)=>s+r.cpu_seconds,0)+1260;
const maxRSS=Math.max(...runs.flatMap(run=>run.rows.map(r=>r.rss_bytes||0)));
const e=1645+Math.log2(9840);
let ct='| N | Free N-involution comparator | log10(1 - N^(-kappa_app)), first-order |\n|---:|---:|---:|\n';
for(const N of[4,16,64,256])ct+='| '+[N,(2*Math.sqrt(N-1)/N).toFixed(12),(Math.log10(Math.log(N))-e*Math.LOG10E*Math.LN2).toFixed(6)].join(' | ')+' |\n';
let report=String.raw`DONE — the finite numerical grid is complete; the results are numerical lower estimates of the largest mean-zero singular value, not certified spectral upper bounds or an asymptotic theorem.

# N8: bounded-resource operator numerics

Task 007, 2026-09-26. Five primes from 1009 to 1999993 and four interval lengths N=4,16,64,256 were run for each of two operators (40 grid points), with eight separate dense-SVD rechecks at p=31,101. No new unconditional Zaremba bound follows.

## 1. Exact operators and conventions

The task calls its two-parameter family “Lemma 14.” In the primary source, Lemma 14 is the one-parameter involution family; Lemma 15 supplies the two-parameter family used for inversion in Corollary 16. Both have therefore been computed:

    T1 f(x) = (1/N) sum_{j=1}^N f(1/(x+2j)-2j),
    T2 f(x) = (1/N^2) sum_{a,b=1}^N f(1/(x+a)-b).

The space is P^1(F_p), with p finite residues and an extra infinity point, 1/0=infinity, 1/infinity=0, and infinity+t=infinity. Norms use counting measure. See [Shkredov Lemmas 14–15, (32)–(35)](https://arxiv.org/html/2603.14116v2#S2), and the original [MMS Lemma 4, (14)–(15)](https://arxiv.org/html/2212.14646v1#S2). All digits/parameters range over the complete interval [N]; T2 uses S=[N]^2.

T1 is an average of involutive permutations. With U_+ f(x)=N^{-1}sum_a f(x+a), U_-=U_+^*, and Jf(x)=f(1/x), one has T2=U_+ J U_-. Hence both operators are real symmetric and doubly stochastic. The mean-zero subspace has dimension p, and the target norm is max of the absolute values of its eigenvalues. Centering by subtracting the mean removes the constant singular value 1. The harness's older even-step T2e option remains available but is not part of this grid.

## 2. Numerical method and limitations

The environment has Node.js 22.23.1 but no Python interpreter. The authorized Python files were extended and inspected; they were not executed. The experiments used a dependency-free Node implementation saved alongside the data, with no installations.

T1 applies each permutation directly, caching at most 64 MiB of permutation indices and otherwise streaming them. T2 uses the factorization above and compensated cyclic sliding sums, so one application takes O(p) operations and linear storage, rather than constructing N^2 permutations. All finite inverse-table entries were checked against a*x_inv=1 mod p; all selected primes passed integer trial division. Arithmetic products used for those inverses are below 2^53.

Power iteration is on T^*T=T^2. For each mean-zero unit vector f, the recorded value is ||Tf||_2, a Rayleigh lower bound for ||T|| in exact arithmetic. The recorded residual is ||T^2 f - ||Tf||_2^2 f||_2. A small residual places an eigenvalue nearby; it does not certify that the largest eigenvalue has been found. Floating-point rounding prevents treating even the lower-bound direction as an interval certificate.

Initial grid runs used seed 12345 and 100–150 iterations. A second independent starting vector, seed 987654321, used 1600 iterations at p<=10007 and 800 at the larger T2 points and p=100003 T1 points. The two largest T1 families used 200 iterations, except the final N=256 point, whose exact iteration count and CPU termination status are in the final JSON. The table takes the larger recorded Rayleigh estimate across available starts. This improves a lower estimate and is not an upper-bound procedure.

## 3. Results

{{TABLE}}

The full precision values, individual residuals, iteration counts, seeds, and source files are in [best_grid_20260926.csv](N8_data/best_grid_20260926.csv). All raw JSONL files retain iteration histories. Displaying nine decimals in the table is a data-format choice, not a claim of nine correct digits for the unknown largest singular value. In particular, the large T1 residuals remain visibly nonzero within the CPU budget.

The comparison requested in the task is 2 sqrt(N-1)/N, the free model for N involutions. It is an appropriate reference for T1, not a proved finite-quotient equality. T2 is a different measure with algebraic relations; the same numbers are shown only as a numerical comparison.

{{COMPARATOR}}

Several T1 estimates exceed this reference: at p=1009,N=64 the value is approximately 0.264980536 rather than 0.248039185, and at p=100003,N=256 it is approximately 0.126697309 rather than 0.124755620. These are finite numerical deviations. Values below the comparator, especially unconverged large T1 values, do not establish an upper bound below it. Large-p T2 values near 0.896 at N=4 and 0.518 at N=16 exceed the same reference values 0.866 and 0.484; this is not a contradiction of a free-model theorem for T2, since none is asserted.

## 4. What the “proven bound” comparison permits

The certified coefficient-one bound used in the results table is ||T_i||_{1-perp}<=1. Proof: each permutation is an isometry, an average has norm at most one, and the invariant mean-zero restriction cannot increase it. For T2 one can also apply ||U_+ J U_-||<=1 directly.

The cited incidence lemmas assert qualitative savings with unspecified coefficients/onsets. They do not, as cited, supply the coefficient-one operator inequality ||T||<=N^(-2^-1656) at these finite primes. The G0 and isolated F1 audits also leave the appendix's numerical normalization, symmetry, BSG extraction, and final assembly unclosed. It would be misleading to label that printed exponent a certified finite operator bound.

For scale only, keeping the appendix's stipulated c=1/1640,k=1641 and its own extraction gives kappa_app=1/(9840*2^1645), so log2(kappa_app^-1)=1658.2644426002. The comparator table shows the first-order logarithm of 1-N^(-kappa_app), namely log10(log N)-log2(kappa_app^-1)*log10(2). The omitted relative correction is O(kappa_app log N). The bare power rounds to 1 in double precision. This column suppresses the unknown coefficient and is an explicitly conditional arithmetic diagnostic, not another upper bound. Correcting the literal doubling normalization makes the exponent still smaller.

The old standalone script's comparator sqrt(2N-1)/N was replaced by 2 sqrt(N-1)/N. Its claim of a proved coefficient-one N^(-2^-1656) norm bound was removed. The pre-existing free_T2.jsonl is a separate model calculation, not a verified prediction for this T2, and was not used to certify the results.

## 5. Independent dense-SVD recheck

At p=31,101 the full centered matrix was constructed from the definition, using Euclidean inverses independently of the sparse inverse recurrence. Its top singular value was computed by one-sided cyclic Jacobi SVD. Every sparse operator column was compared with the independently constructed centered matrix. These are independent floating-point constructions, not an exact-arithmetic proof.

{{DENSE}}

All eight sparse/dense entry differences and symmetry differences were zero at the recorded floating precision. Row sums were checked. Jacobi column correlations were below 1e-13 after 9–14 sweeps. The largest power/SVD discrepancy was about 6.62e-7 at p=101,T1,N=4; its nonzero residual correctly signaled incomplete convergence. The predeclared acceptance limits were 1e-10 for entry agreement, 1e-12 for symmetry, and 3e-4 for the power/SVD comparison. No failure was hidden by tightening those limits after seeing the data.

## 6. Resource accounting and reproduction

{{COSTS}}

The first p=1999993 T1 run completed N=4,16,64, then reached its 1250-CPU-second software budget during N=256. Its partial N=256 iterate was not emitted by that original implementation. The run had a 1260-second kernel CPU cap; its consumption is reported as an interval [1250,1260] seconds rather than an invented exact figure. The final point was rerun alone after fixing budget termination to return the last completed Rayleigh estimate. That rerun had a 1000-second software budget and a 1030-second kernel cap. An independent code review then caught a vector-length error in that first rerun: it used 2000000 coordinates instead of p+1=1999994. That output is preserved as last_T1_1999993_N256_padded_invalid_20260926.jsonl, excluded from the spectral table, and included in CPU accounting (435.642998 seconds). The final correction uses O.n exactly, 100 iterations, a 600-second software budget, and a 700-second kernel cap. The previously consumed upper bound 2800.999057 seconds plus the new hard cap is at most 3500.999057 CPU seconds (0.9725 CPU hours), below the task's one-hour limit. No more than two numerical processes ran concurrently.

The process heap option was --max-old-space-size=768; typed-array storage was separately kept linear and RSS monitored. The largest RSS value in saved records is reported above; this is an observed measurement, not a claim that every instant was sampled. No observed process approached 2 GB. No SAT, new package, paid cloud resource, or external publication was used. Monetary model/tool cost is not exposed and is not estimated.

Files changed or created for this task:

- [N8_harness.py](N8_harness.py): residual-bearing NumPy power mode, streaming large T1, bounds terminology and interval caps. Existing SciPy modes remain optional; the actual runs do not depend on SciPy.
- [zaremba_kappa_numerics.py](../zaremba_kappa_numerics.py): compatibility entry point into the harness, corrected comparator, and accurate bound labels.
- [run_n8.js](N8_data/run_n8.js), [refine_n8.js](N8_data/refine_n8.js), [last_n8.js](N8_data/last_n8.js): dependency-free actual experiment code; raw data under N8_data/.
- [build_report.js](N8_data/build_report.js): aggregation of saved data, with no new spectral calculation.

Each experiment refuses to overwrite its existing output file. To reproduce in a fresh data directory, copy the three experiment files and run the initial grid, refinement, and large-prime commands with the documented CPU caps, keeping at most two processes active. Historical large-prime rows were produced before the change from throwing at the budget to returning a partial estimate; this difference concerns termination and does not alter the operator or iteration. The current scripts stop on the inbox STOP sentinel. The report builder requires every expected grid point, positive iteration counts, finite outputs, and matching recorded dimensions before writing the CSV/report. Operator calls now reject wrong vector lengths, and an already exhausted budget cannot emit an uncomputed zero-iteration row. The final corrected run used the correct dimension; these subsequent guard additions do not change its arithmetic.

To regenerate this exact report, use the supplied original JSONL files, including the excluded padded run for resource accounting. The report builder is for this recorded campaign; a fresh experiment has its own resource ledger. An independent same-model code review checked the operator formulas, saved dense comparisons, and accounting; it found the repaired dimension and zero-iteration issues. The two guards were then exercised directly and passed. Python callers now charge imports and operator construction against an absolute process-CPU deadline, but remain unexecuted in this environment; timing is checked between iterations.

The primary operator displays were checked as stated above; the dependency reports A/B/N1/N3/N9 and the G0/F1 audits were read for scope. This numerical task did not independently reprove Helfgott, Bourgain–Gamburd, Zhang, Murphy/BSG, the survey, or the full final Zaremba argument. No finite grid is presented as such a proof.
`;
const costs='Completed runs: '+completed.map(r=>r.name+': '+r.cpu_seconds.toFixed(6)+' CPU seconds').join('; ')+'. Including the capped incomplete run, the saved/accounted numerical CPU total lies in ['+lower.toFixed(6)+', '+upper.toFixed(6)+'] seconds. Maximum recorded RSS: '+maxRSS+' bytes ('+(maxRSS/1024**2).toFixed(2)+' MiB).';
report=report.replace('{{TABLE}}',table).replace('{{COMPARATOR}}',ct).replace('{{DENSE}}',dt).replace('{{COSTS}}',costs);
fs.writeFileSync(path.join(__dirname,'..','N8_numerics.md'),report);
console.log(JSON.stringify({points:rows.length,cpu_lower:lower,cpu_upper:upper,rss:maxRSS}));
