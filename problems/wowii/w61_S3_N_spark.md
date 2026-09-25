CLEAN: All five listed joints are supportable from the cited draft text, and no gap is required to conclude Theorem N/Corollaries as written.

## 1. Per-joint table

| Joint | Verdict | Justification |
| --- | --- | --- |
| N-J1 | OK | The count `|J| = i−1−h_i` is exact because each prior step either decrements the head (`h_i` times) or does not; in step `j∈J`, the block entries are the first `D_j` non-head entries after sorting, all nondecreasing against position, so each is at least the current value `v` of the target head. If `D_i > τ−j+1`, F3 removes survivors as candidates and the block must be filled by later heads, forcing `D_j ≤ τ−j−1`, contradicting head monotonicity `D_j ≥ D_i`. |
| N-J2 | OK | `K=B` follows from `(i)+Lemma S` and equal cardinality `|K|=|B|=τ` under `residue=α`. Then `Σ_i g_i` is exactly the `B`-degree sum because each edge in `G[B]` is counted twice and there are no `A`-internal edges, so `Σ_i g_i = m+e_B`. With Lemma 1(2), `Σ_i D_i = m`, hence `Σ_i h_i = e_B`; and non-negativity gives `h_τ ≤ e_B`. |
| N-J3 | OK | Hypothesis (ii) gives `e_B ≤ τ−2`, hence `h_τ ≤ e_B ≤ τ−2`, exactly the condition for Lemma H at `i=τ`. The sequence index `τ` is valid and Lemma H gives `D_τ ≤ 2+h_τ`, so `g_τ=D_τ+h_τ ≤ 2+2h_τ ≤ 2e_B+2`. Since `g_τ` is a `B`-vertex degree, `min_{b∈B}deg(b) ≤ g_τ`, contradicting `(iii)`. |
| N-J4 | OK | Lemma S is tight but correct: any survivor is decremented at most once per step, and with `s=τ` all survivors are `0` at termination, so initial value ≤`τ`. Lemma F3 is immediate from the count of remaining steps (`τ−j+1`) with one decrement per step. Lemma T is an exact `s=τ` characterization: if a head remains at step `τ` then the predecessor shape is exactly `[D_τ,1^{D_τ},0^…]`; conversely, that shape makes the `τ`-th step land on all zeros. |
| N-J5 | OK | Theorem N’s statement is independent of `diam` and `f=α+1`; it is a separate mechanism under hypotheses (i)–(iii). The hypotheses are non-vacuous: e.g., Family I with `τ=3,c=4` has `e_B=0`, all `B` degrees `≥ τ+1`, and `τ≥2`, so `(i)-(iii)` holds (and the theorem applies). Corollary N1 is exactly the `e_B=0` specialization; Corollary N2’s algebra matches `D_i≤τ−i+2` (from `h_i=0`) and standard arithmetic for `Σ_{i=2}^{τ} (τ−i+2)=τ(τ+1)/2−1`. |

## 2. GAP/REFUTED entries

None.

## 3. Control-case checks

- **CTRL-1 (FALSE per-entry decay):** Not rescued. The mechanism only gives `D_i ≤ τ−i+2+h_i` (via H) and keeps the `h_i` correction explicit; it does not reduce to `D_i ≤ d_i−(i−1)`. On the tight example `[3,3,3,3,3,2,1]`, `D_2=3` while `d_2−1=2` in the rejected claim, but H allows `D_2≤3` with `h_2=0`.
- **CTRL-2 (FALSE naive counting):** Not forced by accepted machinery. H’s payload is local-to-head with tie-sensitive, `h_i`-adjusted decay; it does not re-derive the rejected global bound that the draft itself already marks as failing.
- **CTRL-3 (FALSE α+1 bound):** Not implied. Theorem N only needs the separate hypotheses `(i)–(iii)` and never deduces `α+1 ≥ residue+⌈d/3⌉`.
- **CTRL-4 (TIGHT instance):** Not contradicted by the accepted machinery. In `n=7,m=9,degrees [3,3,3,3,3,2,1]` with `D=(3,3,2)` (and sum `m−1` over `i≤τ`), Lemma H is saturated at `i=3` (`D_3≤2`), Lemma F3 is respected, and Lemma T is consistent with `residue=α−1` rather than forcing extra slack.

## 4. What I could not check and why

I did not run additional computational checks beyond the file-internal reported numerics. I also could not execute global-memory recall because the `global-memory` tool endpoint is not available in this runtime; therefore no `user_notice` was returned to relay verbatim.
