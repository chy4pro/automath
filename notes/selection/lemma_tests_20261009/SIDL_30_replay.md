# SID-L counterexample CR-7: replay report (verifier, AUT-60)
STATUS: CONFIRMED

## Part 1 - exact replay of the displayed 68-point set

| item | value |
|---|---|
| k = |A| | 68 |
| distinct | True |
| sorted | True |
| min, max | 0, 3956 |
| all in [0,4095] | True |
| k^2 = 4624 >= 4096 | True |
| #positive differences / #distinct | 2278 / 2278 |
| #sums a_i+a_j (i<=j) / #distinct | 2346 / 2346 |
| strong Sidon (both conventions) | True |
| T (N=4096) | 719 |
| 10000*718^4 < 38809*4096^3 <= 10000*719^4 | 2657649945760000 < 2666934172647424 <= 2672486755210000 : True |
| missing differences in {1..T-1} | [601, 615, 624, 638, 671, 685] (count 6); bitmask and set methods agree: True |
| expected missing {601,615,624,638,671,685} | True |
| S | 180279588 |
| 100*S | 18027958800 |
| 3*k*T^3 | 75825771636 |
| 100*S < 3*k*T^3 (counterexample) | True |
| rho = M(A)/(k/100) = 100S/(3kT^3) | 1502329900/6318814303 = 0.237755 |
| span N' = max-min+1 | 3957 |
| N' >= 4096 ? | False |
| hyp at N'=3957: k^2>=N' | True |

Span convention: N' = 3957 < 4096, so the hypothesis N >= 4096 is NOT met under the span convention; the counterexample stands under the interval convention A subset {0..N-1}, N = 4096 (the lemma's own convention).

Part 1 CPU: 0.00 s

## Part 2 - Singer dilation-orbit diagnostic

Instances: for each unit u, 1<=u<=m/2, gcd(u,m)=1, dilate the Singer set B (k=p+1) by u mod m, sort, and take all k cyclic cuts translated to min 0. N=m always tested; N=4096 tested iff max A <= 4095 (p=67 only). Counterexample iff 100S < 3kT^3; rho = 100S/(3kT^3).

| p | m | k | convention | units covered/total | eligible instances | counterexamples | min rho (exact = decimal) | argmin (u, cut) | S at min | T | #missing at min | CPU s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 67 | 4557 | 68 | N=4096 | 39/1260 | 39 | 21 | 1502329900/6318814303 = 0.237755 | (109, 42) | 180279588 | 719 | 6 | 3.7 |
| 67 | 4557 | 68 | N=m | 1260/1260 | 85680 | 3 | 14192846000/24109186089 = 0.588690 | (109, 42) | 567713840 | 779 | 12 | 3.7 |
| 71 | 5113 | 72 | N=m | 2556/2556 | 184032 | 9 | 8146728800/16522921323 = 0.493056 | (754, 59) | 651738304 | 849 | 7 | 8.4 |
| 79 | 6321 | 80 | N=m | 1764/1764 | 141120 | 3 | 83474387/118208985 = 0.706159 | (124, 65) | 1669487740 | 995 | 11 | 7.7 |

p=67, N=4096: counterexamples (u, cut, S): [(109, 42, 4096, 180279588), (328, 23, 4096, 632509812), (481, 23, 4096, 632509812), (502, 19, 4096, 667797332), (563, 56, 4096, 600115784), (629, 13, 4096, 374507020), (764, 18, 4096, 504880820), (809, 46, 4096, 632509812), (1061, 18, 4096, 504880820), (1130, 13, 4096, 374507020), (1265, 56, 4096, 600115784), (1450, 39, 4096, 599644116), (1453, 39, 4096, 599644116), (1654, 39, 4096, 599644116), (1702, 42, 4096, 180279588), (1735, 19, 4096, 667797332), (1759, 56, 4096, 374507020), (1811, 27, 4096, 180279588), (1825, 51, 4096, 504880820), (1828, 13, 4096, 600115784), (2237, 50, 4096, 667797332)]
Minimum at N=4096: S=180279588 (attacker S=180279588): reproduced = True; minimizing set equals displayed 68-set: True; displayed set found as orbit instance (u, cut): (1702, 42)
p=67, N=m=4557: counterexamples (u, cut, S): [(109, 42, 4557, 567713840), (1702, 42, 4557, 567713840), (1811, 27, 4557, 567713840)]

Total CPU time: 19.8 s

Notes: (1) u values are relative to MY Singer base set B (generator-dependent); the attacker's u=353 refers to its own B, so u differs (here the displayed set appears at (u,cut)=(109,42),(1702,42),(1811,27) up to equal S; the exact displayed set is at (1702,42)). (2) N=4096 row: "units covered 39/1260" = units having at least one cut with max A<=4095; eligible instances = those (u,cut) pairs. (3) AUT-57 used s in {1,-1,2,3,5,7} x 900 cuts; the orbit has 1260 units x 68 cuts, and N=4096 eligible instances are rare (39 instances), so the frozen test never reached them. (4) p=71, p=79 completed within the cap (all units, N=m only); they also contain counterexamples at N=m (9 and 3) - note these are N=m instances with N>=4096 under the interval convention. (5) Evidence type: exact integer computation of finite certificates, not a proof of anything beyond the displayed instances.
