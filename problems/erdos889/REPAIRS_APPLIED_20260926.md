DONE

# Erdős 889 referee repairs applied

2026-09-26. Task013. Exact N0=exp(exp(45.28)) and the exact uniform onset remain unchanged. Applied R1–R6 and the requested status line; the updated source is ready for the coordinator to compile. The published PDF was not recompiled or changed. No git command was run.

The model label in the requested status line is copied verbatim from task013; the referee report itself records that the exact model variant/reasoning setting was not exposed.

## Requested status line

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
# Erdős #889: an explicit threshold for the lowercase v₁ problem (Theorem A)
```

New:

```text
# Erdős #889: an explicit threshold for the lowercase v₁ problem (Theorem A)

Cross-vendor refereed 2026-09-26 (OpenAI Codex, GPT-6 Astra): PASS-WITH-REPAIRS, N0 unchanged; repairs applied — see REFEREE_ASTRA_20260926.md.
```

## Review-status consistency

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
Status (2026-09-25): refereed same-vendor (Claude Opus, adversarial, fresh context) —
PASS-WITH-REPAIRS, repairs R1–R6 applied; see REFEREE_CLAUDE_20260925.md. Not cross-vendor
refereed; no Lean.

Status: proof draft for a referee, 2026-09-25. Written by a Claude (Opus) worker for the automath
project. Same-vendor work only. One same-vendor referee report
(`REFEREE_CLAUDE_20260925.md`, PASS-WITH-REPAIRS); no cross-vendor or human referee yet, and nothing here is kernel-checked.
```

New:

```text
Historical status (2026-09-25): refereed same-vendor (Claude Opus, adversarial, fresh context) —
PASS-WITH-REPAIRS, repairs R1–R6 applied; see REFEREE_CLAUDE_20260925.md.

Written by a Claude (Opus) worker for the automath project. The same-vendor report was followed
by a Codex cross-vendor review on 2026-09-26 (`REFEREE_ASTRA_20260926.md`, PASS-WITH-REPAIRS).
No human referee or Lean verification is claimed; nothing here is kernel-checked.
```

## R1 correct side-condition expression

File: `/work/problems/erdos889/n0_compute.py`

Old:

```text
(c * L_ * iv.exp(iv.exp(l1)) - 67).a > 0
```

New:

```text
(c * L_ * iv.exp(l1) - 67).a > 0
```

## R2 exact uniform onset

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
2. An explicit uniform-in-l statement with C₀ = 10 and N(l) = max(exp(1.59 × 10²¹), ⌈e^l⌉), plus
   sharper per-l values for l ≤ 20.
```

New:

```text
2. An explicit uniform-in-l statement with C0=10 and N(l)=max(exp(exp(48.82)), ceil(exp(l))), plus sharper per-l values for l<=20. Here exp(48.82) is approximately 1.59315 × 10^21.
```

## R3 positive historical domain

File: `/work/publish/automath-papers/erdos889/main.tex`

Old:

```text
They showed that $v_0(n)>1$ for all $n$ except $n=1,2,3,4,7,8,16$, and wrote:
```

New:

```text
For positive integers $n$, they showed that $v_0(n)>1$ except when $n=1,2,3,4,7,8,16$. They wrote:
```

## R4 exact restricted-prime count

File: `/work/publish/automath-papers/erdos889/main.tex`

Old:

```text
recovers $p$ from $k_0(p)$, so the map is injective, and the $\pi(K)-\omega(n)$ primes $p\le K$ with $p\nmid n$
give that many distinct $k\in[1,K]$ with $P(n+k)\le K$.
```

New:

```text
recovers $p$ from $k_0(p)$, so the map is injective. The number of primes $p\le K$ with $p\nmid n$ is
$\pi(K)-\#\{p\le K:p\mid n\}$, which is at least $\pi(K)-\omega(n)$. By injectivity these yield at least
$\pi(K)-\omega(n)$ distinct $k\in[1,K]$ with $P(n+k)\le K$.
```

## R5 main

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
log N0 = e^45.28 = 4.62 × 10¹⁹ (4.6223 × 10¹⁹ to five figures).
```

New:

```text
log N0 = e^45.28 ≈ 4.62 × 10¹⁹ (4.6223 × 10¹⁹ to five figures).
```

## R5 uniform statement

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
e^48.82 = 1.59 × 10²¹.
```

New:

```text
e^48.82 ≈ 1.593 × 10²¹.
```

## R5 uniform proof

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
e^48.82 = 1.593 × 10²¹ for log n.
```

New:

```text
e^48.82 ≈ 1.593 × 10²¹ for log n.
```

## R5 refinement

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
log N0′ = e^44.96 = 3.356 × 10¹⁹.
```

New:

```text
log N0′ = e^44.96 ≈ 3.356 × 10¹⁹.
```

## R5 summary

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
log N0 = e^45.28 = 4.62 × 10¹⁹, for Theorem A.
```

New:

```text
log N0 = e^45.28 ≈ 4.62 × 10¹⁹, for Theorem A.
```

## R5 finite set

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
{n | v_l 1 n = 1} ⊆ {0, 1, …, N0 − 1}
```

New:

```text
{n | v_l 1 n = 1} ⊆ {n ∈ ℕ : n < N0}
```

## R5 decimal approximation e^{45.28}=4.6223\cdot10^{19}

File: `/work/publish/automath-papers/erdos889/main.tex`

Old:

```text
e^{45.28}=4.6223\cdot10^{19}
```

New:

```text
e^{45.28}\approx4.6223\cdot10^{19}
```

## R5 decimal approximation e^{48.82}=1.593\cdot10^{21}

File: `/work/publish/automath-papers/erdos889/main.tex`

Old:

```text
e^{48.82}=1.593\cdot10^{21}
```

New:

```text
e^{48.82}\approx1.593\cdot10^{21}
```

## R5 decimal approximation e^{44.96}=3.356\cdot10^{19}

File: `/work/publish/automath-papers/erdos889/main.tex`

Old:

```text
e^{44.96}=3.356\cdot10^{19}
```

New:

```text
e^{44.96}\approx3.356\cdot10^{19}
```

## R6 remove uncertified threshold comparison

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
The threshold from this route is effective but astronomically larger. Langevin's example constants
are C = exp 10⁶ and c = 2000 when k > exp 10⁴. With them, the condition log n/log K ≥ r(ε) already
forces log log n ≳ 10⁶(1 + 2001/ε). Letting ε grow instead makes the factor (1 + c + ε) in (8)
large. Either way log log N0 is at least of order 10⁶. This is our rough estimate and has not been
verified. Here, log log N0 = 45.28.
```

New:

```text
Langevin's constants are effective. We have not computed a certified numerical onset for this alternative route and use it only to establish the qualitative consequence.
```

## R6 remove uncertified threshold comparison

File: `/work/publish/automath-papers/erdos889/main.tex`

Old:

```text
With his example constants
($C=\exp10^6$, $c=2000$ when $k>\exp10^4$) a rough estimate, which we have not verified, suggests that the
condition $\log n/\log k^*\ge r(\eps)$ alone forces $\log\log n$ to be at least of order $10^6$.
```

New:

```text
Langevin's constants are effective. We have not computed a certified numerical onset for this alternative
route and use it only to establish the qualitative consequence.
```

## R6 section title

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
### 7.1 The Langevin route: qualitative, with a much larger threshold
```

New:

```text
### 7.1 The Langevin route: qualitative
```

## Review-status consistency

File: `/work/publish/automath-papers/erdos889/main.tex`

Old:

```text
are incorporated here. This is a same-vendor review; no cross-vendor or human referee has checked the proof.
```

New:

```text
are incorporated here. A subsequent cross-vendor review by OpenAI Codex on 26 September 2026 gave
PASS-WITH-REPAIRS with $N_0$ unchanged; its repairs are incorporated here (see
\texttt{REFEREE\_ASTRA\_20260926.md}). No human referee or kernel formalization is claimed.
```

## Historical execution record

File: `/work/problems/erdos889/PROOF_THEOREM_A.md`

Old:

```text
The script's sha256 is recorded in `CHECKS.md`. The run used Python 3.12 and mpmath 1.3.0, and took
about 6 s on one core.
```

New:

```text
This is the historical output before the 2026-09-26 R1 side-check correction, not a new execution.
The script's historical sha256 is recorded in `CHECKS.md`. The run used Python 3.12 and mpmath 1.3.0, and took
about 6 s on one core. The corrected side condition was independently checked in the cross-vendor report;
Python is unavailable in the repair environment, so this transcript has not been regenerated.
```

## Items without a verbatim counterpart

R1 is executable code in n0_compute.py; neither prose source embeds that erroneous expression. R2’s smaller exact exp(1.59e21) occurred only in PROOF §8; main.tex already defined the exact exp(exp(48.82)) correctly. R3’s faulty historical sentence and R4’s exact-count wording occurred only in main.tex; the internal proof already had the correct n>=0 lemma and restricted-prime count. Their correct counterparts were retained. TeX replacements preserve the exact mathematical content of the referee wording using TeX notation. R6 was optional in the referee report and has now been applied to both sources.

The old Appendix A numerical transcript was retained as a historical record, explicitly labelled as predating the repair. CHECKS.md and its old hash/run record were not modified because task013 did not authorize that path. Python was unavailable, so the patched Python script was not rerun; the correct inequality had already passed the independent interval certificate. No new mathematical claim was added.

## File hashes after repair

- `/work/problems/erdos889/PROOF_THEOREM_A.md`: `7e705ecc3247f0db8688980455ff357c335af545a648dde9e4ebbf52b8aa317c`
- `/work/publish/automath-papers/erdos889/main.tex`: `1d617952e2a5932c12de2726b79eb38d6fd8ae146db717adaca4857df56a6f11`
- `/work/problems/erdos889/n0_compute.py`: `159b4a076998158450ab7a05c627f2a021fb64fa46caf38ab025431afc13406f`
- `/work/publish/automath-papers/erdos889/main.pdf`: `52de225dc23795d330af49336595cee92575a03288b61ad7533b4fbd5b962ea0`
