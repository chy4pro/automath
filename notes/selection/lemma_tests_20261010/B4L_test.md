SURVIVED — no counterexample to B4-L in the specified coverage (batches 1–2 complete, no CPU-cap hit; 0 failures, 0 invalid fixtures). Numerical/exact-finite evidence only, not a proof. Smallest ρ = 100D/(u(u−1)) seen anywhere: 174.24 (batch 3, N=256); in batches 1–2: 227.87 (Singer q=5, N=512 class). The claim needs ρ ≥ 1.

# VER B4-L (AUT-67) — exact finite test of lemma B4-L, full orbits

Environment: Python 3 + numpy, all quantities exact int64 (u from exact big-int u^17 ≥ N^13; D, W, T integers; ρ floats only for ranking, the failure test is the integer inequality 100D < u(u−1)). One thread (OMP_NUM_THREADS=1). Code in this directory: `b4l_common.py` (u, B4 check, vectorised W, brute-force oracles), `fields.py` (finite fields by log tables), `batch1.py`, `batch2.py`, `batch3.py`, `mkreport.py` (this file's tables, `tables.md`); raw results `batch1_result_brute5.json`, `batch2_result.json`, `batch3_result.json`.

Definitions used: D = 4u(u−1) − W with W = Σ_{0<|x|<u} T_A(x)(u−|x|) (uses Σ_{1≤|x|<u}(u−|x|)=u(u−1)); F = W/(4u(u−1)) is the realised fraction; ρ = 100D/(u(u−1)) = 400(1−F). u(256)=70, u(512)=118, u(4096)=579. T_A computed via unordered pairs P,Q with index-disjointness and multiplicity weights (1 for {i,i}, 2 for i<j); this is identical to the ordered 4-tuple definition and was cross-checked against a literal ordered-4-tuple brute force (`brute_D`) on every set reported below (assert D equal). Translation invariance: all tuple differences are unchanged by a common shift, reflection maps x→−x with symmetric weights, so D depends only on the min-normalised shape and N (through u). Hence a result for a shape of span s at N covers N−s+1 ordinary translates in {0..N−1} and N−s+1 in {1..N} (counts below). Reflected shapes were verified to be in the unique set (closure assert, batch 1; batch 2 explicit).

Construction notes / deviations: field F_{p^n} built from the first monic polynomial (coefficients low→high, lexicographic) for which x is primitive, θ = x (instead of "first irreducible, then first primitive element"); the generator choice is absorbed because all b and all unit multipliers are enumerated. q=4 uses F_4 = {z: z^4 = z} inside F_{2^8} (Bose–Chowla) and F_{2^10} (Singer). Bose–Chowla b: θ^b of degree 4 over F_q (b·q² ≢ b mod M), set = log(θ^b+v), v∈F_q, size q. Singer b ∈ 1..M−1 (θ^b ∉ F_q), set = log(uθ^b+v) mod M over (u,v)≠0, size q+1. All assert cardinalities. Every full set and every subset was B4-validated at integer level (all 4-multiset sums distinct) before evaluation: 0 invalid.

t-enumeration: the reported run (`batch1.py 5`, flag brute_t) enumerates literally every t∈{0..M−1} for every (family,q,b,a): lifts (aD+t) mod M, sorts, normalises by minimum. Raw count 542,737,260 triples (b,a,t). A faster algebraic shortcut (the k cut-rotations of aD) was also implemented (`batch1.py 3`, used for q≥4) and gave identical unique-set counts and identical minima; no sampling anywhere. Dedup: unique normalised full sets, then all 2^k−1 subset masks of each, normalised by their minimum, deduplicated per size.

## Results tables
### Batch 1 (literal t-enumeration) per family, q, N-class

rho = 100 D/(u(u-1)) (claim needs rho >= 1); F = W/(4u(u-1)) realised weighted fraction; |A+A|; #x (0<|x|<u) in S-S out of 2(u-1). Every row recomputed by independent brute-force 4-tuple enumeration (b4l_common.brute_D).

| family | q | N-class | min rho | attaining set (min-normalised, any translate/reflection) | F | abs(A+A) | x realised by S-S |
|---|---|---|---|---|---|---|---|
| Bose-Chowla | 2 | 256 | 397.1843 | N=256, u=70, A=[0, 1]; D=19184 (4u(u-1)=19320, W=136) | 0.00704 | 3 | 4/138 |
| Bose-Chowla | 2 | 512 | 398.3196 | N=512, u=118, A=[0, 1]; D=54992 (4u(u-1)=55224, W=232) | 0.00420 | 3 | 4/234 |
| Bose-Chowla | 2 | 4096 | 399.6552 | N=4096, u=579, A=[0, 1]; D=1337494 (4u(u-1)=1338648, W=1154) | 0.00086 | 3 | 4/1156 |
| Singer | 2 | 256 | 376.0663 | N=256, u=70, A=[0, 2, 5]; D=18164 (4u(u-1)=19320, W=1156) | 0.05983 | 6 | 18/138 |
| Singer | 2 | 512 | 385.3687 | N=512, u=118, A=[0, 2, 5]; D=53204 (4u(u-1)=55224, W=2020) | 0.03658 | 6 | 18/234 |
| Singer | 2 | 4096 | 396.9169 | N=4096, u=579, A=[0, 2, 5]; D=1328330 (4u(u-1)=1338648, W=10318) | 0.00771 | 6 | 18/1156 |
| Bose-Chowla | 3 | 256 | 376.0663 | N=256, u=70, A=[0, 2, 5]; D=18164 (4u(u-1)=19320, W=1156) | 0.05983 | 6 | 18/138 |
| Bose-Chowla | 3 | 512 | 385.3687 | N=512, u=118, A=[0, 2, 5]; D=53204 (4u(u-1)=55224, W=2020) | 0.03658 | 6 | 18/234 |
| Bose-Chowla | 3 | 4096 | 396.9169 | N=4096, u=579, A=[0, 2, 5]; D=1328330 (4u(u-1)=1338648, W=10318) | 0.00771 | 6 | 18/1156 |
| Singer | 3 | 256 | 306.1698 | N=256, u=70, A=[0, 2, 10, 17]; D=14788 (4u(u-1)=19320, W=4532) | 0.23458 | 10 | 54/138 |
| Singer | 3 | 512 | 337.9690 | N=512, u=118, A=[0, 2, 10, 17]; D=46660 (4u(u-1)=55224, W=8564) | 0.15508 | 10 | 54/234 |
| Singer | 3 | 4096 | 385.8699 | N=4096, u=579, A=[0, 2, 10, 17]; D=1291360 (4u(u-1)=1338648, W=47288) | 0.03533 | 10 | 54/1156 |
| Bose-Chowla | 4 | 256 | 327.3706 | N=256, u=70, A=[0, 4, 23, 28]; D=15812 (4u(u-1)=19320, W=3508) | 0.18157 | 10 | 54/138 |
| Bose-Chowla | 4 | 512 | 345.3861 | N=512, u=118, A=[0, 4, 23, 28]; D=47684 (4u(u-1)=55224, W=7540) | 0.13653 | 10 | 54/234 |
| Bose-Chowla | 4 | 4096 | 386.1759 | N=4096, u=579, A=[0, 4, 23, 28]; D=1292384 (4u(u-1)=1338648, W=46264) | 0.03456 | 10 | 54/1156 |
| Singer | 4 | 256 | 270.8903 | N=256, u=70, A=[0, 18, 34, 41, 76]; D=13084 (4u(u-1)=19320, W=6236) | 0.32277 | 15 | 88/138 |
| Singer | 4 | 512 | 279.3858 | N=512, u=118, A=[0, 18, 34, 41, 76]; D=38572 (4u(u-1)=55224, W=16652) | 0.30154 | 15 | 124/234 |
| Singer | 4 | 4096 | 359.2484 | N=4096, u=579, A=[0, 18, 34, 41, 76]; D=1202268 (4u(u-1)=1338648, W=136380) | 0.10188 | 15 | 130/1156 |
| Bose-Chowla | 5 | 256 | 308.6542 | N=256, u=70, A=[0, 6, 15, 69, 88]; D=14908 (4u(u-1)=19320, W=4412) | 0.22836 | 15 | 62/138 |
| Bose-Chowla | 5 | 512 | 310.7055 | N=512, u=118, A=[0, 6, 15, 69, 88]; D=42896 (4u(u-1)=55224, W=12328) | 0.22324 | 15 | 98/234 |
| Bose-Chowla | 5 | 4096 | 361.0461 | N=4096, u=579, A=[0, 6, 15, 69, 88]; D=1208284 (4u(u-1)=1338648, W=130364) | 0.09738 | 15 | 130/1156 |
| Singer | 5 | 256 | 231.7184 | N=256, u=70, A=[0, 44, 58, 119, 125, 179]; D=11192 (4u(u-1)=19320, W=8128) | 0.42070 | 21 | 90/138 |
| Singer | 5 | 512 | 227.8719 | N=512, u=118, A=[0, 21, 46, 64, 72, 155]; D=31460 (4u(u-1)=55224, W=23764) | 0.43032 | 21 | 180/234 |
| Singer | 5 | 4096 | 309.8380 | N=4096, u=579, A=[0, 21, 46, 64, 72, 155]; D=1036910 (4u(u-1)=1338648, W=301738) | 0.22541 | 21 | 270/1156 |

### Batch 1 accounting

| family | q | M | #b | #units | raw (b,a,t) = #b*phi*M | unique full sets | unique nonempty subsets by size | invalid | failures | ordinary translates covered (per convention; N=256/512/4096 class) | CPU s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bose-Chowla | 2 | 15 | 12 | 8 | 1440 | 12 | {'1': 1, '2': 12} (total 13) | 0 | 0 | 3238/6566/53158 | 0.0 |
| Singer | 2 | 31 | 30 | 30 | 27900 | 90 | {'1': 1, '2': 30, '3': 90} (total 121) | 0 | 0 | 28651/59627/493291 | 0.0 |
| Bose-Chowla | 3 | 80 | 72 | 32 | 184320 | 264 | {'1': 1, '2': 72, '3': 264} (total 337) | 0 | 0 | 69312/155584/1363392 | 0.1 |
| Singer | 3 | 121 | 120 | 110 | 1597200 | 880 | {'1': 1, '2': 120, '3': 2310, '4': 880} (total 3311) | 0 | 0 | 574156/1421772/13288396 | 0.5 |
| Bose-Chowla | 4 | 255 | 240 | 128 | 7833600 | 1280 | {'1': 1, '2': 240, '3': 3456, '4': 1280} (total 4977) | 0 | 0 | 411192/1685304/19522872 | 2.0 |
| Singer | 4 | 341 | 340 | 300 | 34782000 | 2550 | {'1': 1, '2': 340, '3': 14040, '4': 10200, '5': 2550} (total 27131) | 0 | 0 | 1038523/7337052/104574556 | 10.0 |
| Bose-Chowla | 5 | 624 | 600 | 192 | 71884800 | 7080 | {'1': 1, '2': 600, '3': 27612, '4': 26184, '5': 7080} (total 61477) | 0 | 0 | 610732/5504712/224347552 | 20.7 |
| Singer | 5 | 781 | 780 | 700 | 426426000 | 21840 | {'1': 1, '2': 780, '3': 164010, '4': 218400, '5': 109200, '6': 21840} (total 514231) | 0 | 0 | 2544361/22617013/1810220886 | 142.1 |

Total raw (family,q,b,a,t) enumerated: 542737260.

### Batch 2

Dense: subsets of {0..31} of size 1..4: {'1': 32, '2': 496, '3': 4960, '4': 35960}; B4 kept {'1': 32, '2': 496, '3': 4186, '4': 6680} (11394), non-B4 rejected 30054; unique min-normalised shapes {'1': 1, '2': 31, '3': 416, '4': 1310}; failures 0; translates covered per convention (N=256/512/4096): 405186/855234/7155906.

| group | N-class | min rho | set | F | abs(A+A) | x realised |
|---|---|---|---|---|---|---|
| dense<=4 of {0..31} | 256 | 304.5135 | N=256, u=70, A=[0, 2, 12, 15]; D=14708 (4u(u-1)=19320, W=4612) | 0.23872 | 10 | 54/138 |
| dense<=4 of {0..31} | 512 | 337.3895 | N=512, u=118, A=[0, 2, 12, 15]; D=46580 (4u(u-1)=55224, W=8644) | 0.15653 | 10 | 54/234 |
| dense<=4 of {0..31} | 4096 | 385.8460 | N=4096, u=579, A=[0, 2, 12, 15]; D=1291280 (4u(u-1)=1338648, W=47368) | 0.03538 | 10 | 54/1156 |
| greedy prefix k=1 x dilates 1..16 (+reflections) | 256 | 400.0000 | N=256, u=70, A=[0]; D=19320 (4u(u-1)=19320, W=0) | 0.00000 | 1 | 0/138 |
| greedy prefix k=1 x dilates 1..16 (+reflections) | 512 | 400.0000 | N=512, u=118, A=[0]; D=55224 (4u(u-1)=55224, W=0) | 0.00000 | 1 | 0/234 |
| greedy prefix k=1 x dilates 1..16 (+reflections) | 4096 | 400.0000 | N=4096, u=579, A=[0]; D=1338648 (4u(u-1)=1338648, W=0) | 0.00000 | 1 | 0/1156 |
| greedy prefix k=2 x dilates 1..16 (+reflections) | 256 | 397.1843 | N=256, u=70, A=[0, 1]; D=19184 (4u(u-1)=19320, W=136) | 0.00704 | 3 | 4/138 |
| greedy prefix k=2 x dilates 1..16 (+reflections) | 512 | 398.3196 | N=512, u=118, A=[0, 1]; D=54992 (4u(u-1)=55224, W=232) | 0.00420 | 3 | 4/234 |
| greedy prefix k=2 x dilates 1..16 (+reflections) | 4096 | 399.6552 | N=4096, u=579, A=[0, 1]; D=1337494 (4u(u-1)=1338648, W=1154) | 0.00086 | 3 | 4/1156 |
| greedy prefix k=3 x dilates 1..16 (+reflections) | 256 | 376.2319 | N=256, u=70, A=[0, 1, 5]; D=18172 (4u(u-1)=19320, W=1148) | 0.05942 | 6 | 18/138 |
| greedy prefix k=3 x dilates 1..16 (+reflections) | 512 | 385.4266 | N=512, u=118, A=[0, 1, 5]; D=53212 (4u(u-1)=55224, W=2012) | 0.03643 | 6 | 18/234 |
| greedy prefix k=3 x dilates 1..16 (+reflections) | 4096 | 396.9193 | N=4096, u=579, A=[0, 1, 5]; D=1328338 (4u(u-1)=1338648, W=10310) | 0.00770 | 6 | 18/1156 |
| greedy prefix k=4 x dilates 1..16 (+reflections) | 256 | 313.6232 | N=256, u=70, A=[0, 1, 5, 21]; D=15148 (4u(u-1)=19320, W=4172) | 0.21594 | 10 | 54/138 |
| greedy prefix k=4 x dilates 1..16 (+reflections) | 512 | 340.5766 | N=512, u=118, A=[0, 1, 5, 21]; D=47020 (4u(u-1)=55224, W=8204) | 0.14856 | 10 | 54/234 |
| greedy prefix k=4 x dilates 1..16 (+reflections) | 4096 | 385.9775 | N=4096, u=579, A=[0, 1, 5, 21]; D=1291720 (4u(u-1)=1338648, W=46928) | 0.03506 | 10 | 54/1156 |
| greedy prefix k=5 x dilates 1..16 (+reflections) | 256 | 246.8737 | N=256, u=70, A=[0, 1, 5, 21, 55]; D=11924 (4u(u-1)=19320, W=7396) | 0.38282 | 15 | 102/138 |
| greedy prefix k=5 x dilates 1..16 (+reflections) | 512 | 262.8422 | N=512, u=118, A=[0, 1, 5, 21, 55]; D=36288 (4u(u-1)=55224, W=18936) | 0.34289 | 15 | 130/234 |
| greedy prefix k=5 x dilates 1..16 (+reflections) | 4096 | 358.5265 | N=4096, u=579, A=[0, 1, 5, 21, 55]; D=1199852 (4u(u-1)=1338648, W=138796) | 0.10368 | 15 | 130/1156 |
| greedy prefix k=6 x dilates 1..16 (+reflections) | 256 | 240.1656 | N=256, u=70, A=[0, 1, 5, 21, 55, 153]; D=11600 (4u(u-1)=19320, W=7720) | 0.39959 | 21 | 110/138 |
| greedy prefix k=6 x dilates 1..16 (+reflections) | 512 | 240.5331 | N=512, u=118, A=[0, 1, 5, 21, 55, 153]; D=33208 (4u(u-1)=55224, W=22016) | 0.39867 | 21 | 166/234 |
| greedy prefix k=6 x dilates 1..16 (+reflections) | 4096 | 311.6559 | N=4096, u=579, A=[0, 1, 5, 21, 55, 153]; D=1042994 (4u(u-1)=1338648, W=295654) | 0.22086 | 21 | 270/1156 |
| greedy prefix k=7 x dilates 1..16 (+reflections) | 256 | 235.3082 | N=369, u=92, A=[0, 1, 5, 21, 55, 153, 368]; D=19700 (4u(u-1)=33488, W=13788) | 0.41173 | 28 | 140/182 |
| greedy prefix k=7 x dilates 1..16 (+reflections) | 512 | 234.7965 | N=512, u=118, A=[0, 1, 5, 21, 55, 153, 368]; D=32416 (4u(u-1)=55224, W=22808) | 0.41301 | 28 | 176/234 |
| greedy prefix k=7 x dilates 1..16 (+reflections) | 4096 | 266.6332 | N=4096, u=579, A=[0, 1, 5, 21, 55, 153, 368]; D=892320 (4u(u-1)=1338648, W=446328) | 0.33342 | 28 | 470/1156 |
| greedy prefix k=8 x dilates 1..16 (+reflections) | 256 | 234.6667 | N=857, u=175, A=[0, 1, 5, 21, 55, 153, 368, 856]; D=71456 (4u(u-1)=121800, W=50344) | 0.41333 | 36 | 246/348 |
| greedy prefix k=8 x dilates 1..16 (+reflections) | 512 | 234.6667 | N=857, u=175, A=[0, 1, 5, 21, 55, 153, 368, 856]; D=71456 (4u(u-1)=121800, W=50344) | 0.41333 | 36 | 246/348 |
| greedy prefix k=8 x dilates 1..16 (+reflections) | 4096 | 256.4450 | N=4096, u=579, A=[0, 1, 5, 21, 55, 153, 368, 856]; D=858224 (4u(u-1)=1338648, W=480424) | 0.35889 | 36 | 542/1156 |
| greedy prefix k=9 x dilates 1..16 (+reflections) | 256 | 233.1837 | N=1425, u=259, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424]; D=155818 (4u(u-1)=267288, W=111470) | 0.41704 | 45 | 324/516 |
| greedy prefix k=9 x dilates 1..16 (+reflections) | 512 | 233.1837 | N=1425, u=259, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424]; D=155818 (4u(u-1)=267288, W=111470) | 0.41704 | 45 | 324/516 |
| greedy prefix k=9 x dilates 1..16 (+reflections) | 4096 | 245.9030 | N=4096, u=579, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424]; D=822944 (4u(u-1)=1338648, W=515704) | 0.38524 | 45 | 606/1156 |
| greedy prefix k=10 x dilates 1..16 (+reflections) | 256 | 235.0218 | N=2604, u=410, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603]; D=394108 (4u(u-1)=670760, W=276652) | 0.41245 | 55 | 492/818 |
| greedy prefix k=10 x dilates 1..16 (+reflections) | 512 | 235.0218 | N=2604, u=410, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603]; D=394108 (4u(u-1)=670760, W=276652) | 0.41245 | 55 | 492/818 |
| greedy prefix k=10 x dilates 1..16 (+reflections) | 4096 | 239.5719 | N=4096, u=579, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603]; D=801756 (4u(u-1)=1338648, W=536892) | 0.40107 | 55 | 632/1156 |
| greedy prefix k=11 x dilates 1..16 (+reflections) | 256 | 239.4301 | N=4968, u=671, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967]; D=1076406 (4u(u-1)=1798280, W=721874) | 0.40142 | 66 | 694/1340 |
| greedy prefix k=11 x dilates 1..16 (+reflections) | 512 | 239.4301 | N=4968, u=671, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967]; D=1076406 (4u(u-1)=1798280, W=721874) | 0.40142 | 66 | 694/1340 |
| greedy prefix k=11 x dilates 1..16 (+reflections) | 4096 | 239.4301 | N=4968, u=671, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967]; D=1076406 (4u(u-1)=1798280, W=721874) | 0.40142 | 66 | 694/1340 |
| greedy prefix k=12 x dilates 1..16 (+reflections) | 256 | 246.4726 | N=8195, u=984, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967, 8194]; D=2384060 (4u(u-1)=3869088, W=1485028) | 0.38382 | 78 | 974/1966 |
| greedy prefix k=12 x dilates 1..16 (+reflections) | 512 | 246.4726 | N=8195, u=984, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967, 8194]; D=2384060 (4u(u-1)=3869088, W=1485028) | 0.38382 | 78 | 974/1966 |
| greedy prefix k=12 x dilates 1..16 (+reflections) | 4096 | 246.4726 | N=8195, u=984, A=[0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967, 8194]; D=2384060 (4u(u-1)=3869088, W=1485028) | 0.38382 | 78 | 974/1966 |

Greedy: raw (k,d) fixtures 192, unique shapes 177, failures 0, invalid 0. CPU dense 0.27s, total batch 2 0.30s.

### Batch 3 (hill climbing)

| N | u | best set | m | W | D | rho | F | moves |
|---|---|---|---|---|---|---|---|---|
| 256 | 70 | [3, 5, 43, 174, 200, 215, 246] | 7 | 10904 | 8416 | 174.2443 | 0.56439 | 920370 |
| 512 | 118 | [3, 54, 100, 173, 187, 220, 309] | 7 | 29816 | 25408 | 184.0359 | 0.53991 | 389923 |
| 1024 | 201 | [333, 371, 412, 441, 842, 926, 948, 985] | 8 | 81106 | 79694 | 198.2438 | 0.50439 | 163241 |

## CPU time (this process, `time.process_time`)
- Batch 1 (literal t-loop, q=2,3,4,5 both families, including construction, validation, subsets and evaluation): 0.0+0.0+0.1+0.5+2.0+10.0+20.7+142.1 ≈ 175.4 s (plus ~0.2 s field tables). The shortcut variant ran in ≈ 5.6 s total.
- Batch 2: 0.30 s.
- Batch 3: 3 × 290 s search budget ≈ 870 s (cap 900 s).
- Batches 1–2 total ≈ 176 s ≪ 3300 s cap.

## Reading of the numbers (diagnostics, not proofs)
- Exact coverage for SURVIVED: Bose–Chowla q=2,3,4,5 (M=15,80,255,624) and Singer q=2,3,4,5 (M=31,121,341,781); every permitted b; every unit multiplier; every t; full sets and all nonempty subsets; N ∈ {max(256,s), max(512,s), max(4096,s)}; both conventions and all ordinary translates and reflections via invariance (counts in accounting table). Greedy prefixes k=1..12 × dilates d=1..16 (+reflections), same N rule; all B4 subsets of {0..31} with ≤4 elements at 256/512/4096. Not covered: q>5, other B4 sets, N≥256 in general.
- The attaining sets are always the full or near-full algebraic sets (largest cardinality, smallest span), with F up to 0.43 (batches 1–2) and up to 0.564 (batch 3). So even adversarially chosen B4 sets realise about half the baseline 4u(u−1) at best in this range; the lemma requires F ≤ 399/400 and the observed maximum is far below. Because T_A(x) ≤ 4·1[x∈S−S] was requested as a diagnostic: for the best sets S−S covers up to 270/1156 (Singer q=5, N=4096) and 180/234 (N=512) of the 2(u−1) small x. At these N, |A+A| ≤ 78 (batch 2) so S−S is small; small-N margins are uninformative about large N where m ≈ cN^{1/4} grows.
- Batch 3 (hill climbing over maximal B4 sets, moves = delete 1–3 elements and refill randomly, plateau moves accepted, 2% restarts; best sets independently recomputed by brute force): smallest ρ found 174.24 (N=256), 184.04 (N=512), 198.24 (N=1024). It measures closeness only; the search is heuristic and not exhaustive.
