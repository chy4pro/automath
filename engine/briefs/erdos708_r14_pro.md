# ATTACK — Erdős Problem #708, round 14: WINDOW-ADAPTED certificates for the sparse core (TEMPLATE v2.3, prove-or-refute)

## The statement (the last gap to a linear bound for all n)
Atoms p^j ≤ m/64 with weights α_{p,j} ≥ 0, Σ_j α_{p,j} ≤ 1; S₀(n) = Σ α_{p,j} 1[p^j | n]; m > 4096; mean H = Σ α_{p,j}/p^j < 17/16.
K = {1,…,m}, I = {x+1,…,x+m}; L := Σ_{k≤m}(S₀(k) − 64)⁺, R := Σ_{b∈I}(S₀(b) − 1)⁺.   (SC_64): L ≤ R for every x ≥ 0.
PROVED (refereed): (SC_64) for 4096 < m ≤ 10^2942 (⇒ g(n) ≤ 81n for n ≤ 10^980); L ≤ mH^65/65! < 6.24·10^−90 m; L = 0 unless m ≥ P₆₅ ≈ 6.1·10^127.

## The key correction (refereed 09-05) — read carefully
The counting principle needs certificate feasibility ON THE WINDOW ONLY: if c_D ≥ 0 satisfy (F_I) Σ_{D|b} c_D ≤ (S₀(b)−1)⁺ for every b ∈ I, then
R ≥ Σ_D c_D ⌊m/D⌋. The certificate may depend on x. The round-13 'barrier' (an explicit family beyond 10^2958 where every nonnegative certificate
supported on high-point divisors has value ≤ L−1) only holds for certificates required to satisfy (F) at EVERY integer (its one binding constraint
came from n = lcm(1..m)); on the very same family the window-adapted certificate c_D = 1/36 on all moduli 2pq (p<q in the family's prime set)
is (F_I)-feasible (S₀ ≤ 72 on I) and has value ≥ 2·10^−10 m ≥ 10^84·L. Scaled numerics (threshold 2, m = (2Q)³, Q = 2^12..2^14): the all-n
class is capped at L/4…L/12 while window-adapted certificates reach 5.8–6.1·L; a full window enumeration at Q = 2^7 showed 0 violations.

## The window LP (exact reformulation of what counting can do per window)
For fixed (atoms, m, x): W(x) := max { Σ_D c_D ⌊m/D⌋ : c ≥ 0, Σ_{D|b} c_D ≤ (S₀(b)−1)⁺ ∀ b ∈ I }, D ranging over all positive integers (only
D dividing some b ∈ I matter). Then R ≥ W(x), and (SC_64) follows for the window if W(x) ≥ L. LP duality: W(x) = min { Σ_{b∈I} y_b (S₀(b)−1)⁺ :
y ≥ 0, Σ_{b∈I, D|b} y_b ≥ ⌊m/D⌋ for every D } — a fractional covering of the 'multiple counts' ⌊m/D⌋ by window points weighted by their hinge
cost. So (SC_64) for all windows ⇐ for every window and every fractional cover y: Σ_b y_b (S₀(b)−1)⁺ ≥ L. (y ≡ 1 is a cover with cost R.)

## What is PROVED (use freely)
S1 32-shadow theorem: S₀(k) > 64 ⇒ 32 pairwise coprime D_r | k with certificate 1/3 (window-independent) ⇒ R ≥ (32/3)(1−6^−31) m/k^{1/32}.
S2 Moments: Σ_K e_ℓ((a_p(k))_p) ≤ mH^ℓ/ℓ!; (t−C)⁺ ≤ e_{C+1} of summands in [0,1]; L ≤ mH^65/65!.
S3 One high point in K forces R > 63 (I contains a multiple of k). Packing lemma (masses > 64 ⇒ 32 groups in (4/3, 2]).
S4 Abstract two-sided counting with ARBITRARY base counts cannot give absolute thresholds (projective planes); the true ⌊m/D⌋ table must be used.
S5 Dead: multiples-only charging (overloads one b by an unbounded factor); uniform pair coefficients for unequal masses; naive layer-cake;
   Bernoulli rounding; fixed-degree pointwise polynomial certificates; single window-independent certificate on high-point divisors beyond 10^2958.

## Coordinator's analysis (test it)
A1 Per-window strategy: let T := {b ∈ I : S₀(b) > 72} (the 'hot' points of the window; at most … many — bound their number by the moment bound
   applied to the window: Σ_{b∈I} e_ℓ((a_p(b))_p) ≤ (m/D-type counts) ≤ (1+o(1)) m e_ℓ(h) since N_I(D) ≤ m/D + 1 — but the +1 terms sum to the number of
   moduli, which can exceed m; handle by restricting ℓ-fold products to D ≤ m). On I \ T the constraint (F_I) is mild; on T it is generous
   ((S₀(b)−1)⁺ is large). Choose a certificate supported on moduli D whose multiples in I avoid T as much as possible, or pay for T by S3-type
   contributions (each hot point b contributes (S₀(b)−1)⁺ ≥ 71 to R directly — a cover y may put mass on hot points cheaply relative to their
   many divisors).
A2 The dual is the cleaner object: a fractional cover y of the counts ⌊m/D⌋ (for all D up to m) by window points. Lower-bound its cost by
   LP weak duality against an explicit window-adapted certificate — the certificate is the tool; the dual is the adversary. Show that for any
   window the greedy 'pair certificate on the cold part + shadow certificate on the hot part' has value ≥ L: the cold part has S₀ ≤ 72 so uniform
   pair/triple coefficients (like 1/36 on 2pq) are feasible there; the hot points need coefficients scaled down on the moduli dividing them
   (there are few hot points; each affects only the moduli dividing it).
A3 The barrier family of round 13 (residues chosen so that all high points of K share one window point B with huge S₀) is the model adversary:
   on it, the certificate 1/36 on 2pq works because I contains no point with S₀ > 72. In general a window can contain many hot points
   (e.g. windows around lcm-rich integers) — construct the worst case and test the LP numerically at scaled thresholds (threshold 2 or 3, m ≤ 10^6,
   exact LP with scipy) before proving anything.

## Targets (equal rank; prove-or-refute)
T1 PROVE (SC_64) (or (SC_r), any absolute r with the matching dense branch) for ALL m via window-adapted certificates: for every window an
   explicit (F_I)-feasible nonnegative certificate with value ≥ L. Full proof, every constant explicit ⇒ g(n) ≤ 81n for all n.
T2 PROVE the dual statement directly: every fractional cover y of {⌊m/D⌋} by window points costs Σ y_b (S₀(b)−1)⁺ ≥ L (for m ≥ P₆₅, mean < 17/16).
T3 REFUTE: an explicit family (atoms, m, x) with W(x) < L for infinitely many m — i.e. a window where even window-adapted counting fails
   (this would show the counting principle itself cannot prove (SC_64); give a small scaled instance we can verify by LP); or an actual
   counterexample to (SC_64).
T4 The scaled-threshold experiment as a proved statement: for threshold C = 2 or 3 in place of 64 (and the corresponding dense branch), prove
   W(x) ≥ L for all windows and all m up to an explicit bound by an explicit certificate family — a template for the general case.
Rule: no intermediate statement is used before an adversarial agent has tried to break it on residue-defined windows with many hot points
AND on abstract multisets; status tags PROVED / CONDITIONAL / CONJECTURED; end with 'final claim ← lemmas ← unproved items'.

## Current task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; use multiagents
aggressively: (i) window-LP team (exact LP at scaled thresholds, then the certificate family); (ii) dual/covering team (T2); (iii) adversary team
(windows with many hot points; T3); (iv) referee team checking every constant. Budget: about two hours; then return the strongest rigorously
proved statement with its exact gap.

## Output contract
Numbered lemmas with status tags; every constant explicit; every construction explicit enough to be re-run; what a Lean formalisation needs.
A check that cannot fail counts as no check.
