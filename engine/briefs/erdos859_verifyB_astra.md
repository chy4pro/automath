# Erdős #859 — independent verification of the proved upper bound on B(t)

**SINGLE AGENT. Do not spawn sub-agents.** No time limit.
**Your job is to find the error if there is one, not to agree.**

## What to verify

`engine/harvest/erdos859_lemmaBprime_astra.md`, produced by another run on 2026-09-09, claims

> for every real `t >= 2`,  `B(t) <= 20 000 000 000 (log t)^theta`,
> `theta = 1 + log(3349/4000)/log 5 = 0.8896306804161379…`,

where `P(t) = {m practical : t < m <= 2t}` and `B(t) = sum over ordered pairs m, m' in P(t) of
1/lcm(m,m')`. Section 4 of that file is the proof; §5 lists its own verification scripts, all of
which are in `engine/harvest/`.

A publication is about to be built on this bound, so it needs a second pair of eyes that did not
write it.

## What has already been checked, so do not just repeat it

The dialogue seat has independently confirmed:

- The load-bearing reduction of §2 is correct: for `y > 0`, `sum_{y<k<=2y} 1/k <= 1` (at most
  `floor(y)+1` eligible integers, each `>= floor(y)+1`), hence `g·A_g <= 1`, hence
  `B = sum_g phi(g) A_g^2 <= sum_g (g A_g) A_g <= sum_g A_g = S(t)`.
- `B <= S` holds on all ten measured rows (0.469 <= 2.266 … 0.584 <= 3.304).
- The file's own verifier runs and passes, and reproduces all ten measured `A, B, S, H_phi` rows.
- The final bound is numerically true but extremely loose: at `t = 5·10^5` it reads `1.98·10^11`
  against a measured `B = 0.584`.

**Unchecked, and therefore your task: the whole of §4** — the derivation of the exponent `theta`
and the constant `2·10^10` from the reduction.

## Specific things to check

1. The one-block first-moment majorant: where the `3349/4000` and the base 5 come from, and
   whether the claimed contraction factor is actually attained rather than assumed.
2. The prime-prefix / first-crossing decomposition: does it cover every practical `m in (t,2t]`,
   including partial prime powers and the case where the crossing prime is the largest prime?
3. The interval certificate in §4.3: is the directed integer arithmetic sound, is the mesh fine
   enough for the claimed conclusion, and does the stated negative control (a certified lower bound
   on `F(2.35)` exceeding 0.8372) really demonstrate that the comparison can fail?
4. Whether `theta < 1` is genuinely proved or whether some step silently assumes a bound it is
   trying to establish.
5. The constant `20 000 000 000`: is it actually valid from `t = 2`, or only from some larger `t`
   with the small range unchecked?
6. Any place where a bound proved for one practical integer is applied to a pair without
   justification — §6 of that file admits the prefix decomposition "handles one practical integer
   at a time and has no control of how two such prefixes overlap", so check that this admission is
   consistent with what §4 actually uses.

## Output contract

Numbered findings, an explicit verdict per item: **CORRECT** / **ERROR** (state it precisely, and
say whether the theorem survives in weakened form, with the weakened exponent and constant) /
**UNVERIFIABLE** (state exactly what is missing). If you find an error, give the smallest exponent
and constant that DO survive. Every constant explicit. A check that cannot fail counts as no check.

Write to `engine/harvest/erdos859_verifyB_astra.md`.
