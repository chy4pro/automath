FOLLOW-UP 2 (coordinator). Your Theorem 6 (0/1 hinge with absolute constant 4 for every P) is with our independent referee now; assume it
survives and go for the ONLY remaining gap to the linear bound: the FRACTIONAL case.
Target: (TH_C) Σ_{k≤m} (w_z(k) − C)⁺ ≤ Σ_{b∈I} (w_z(b) − 1)⁺ for all weights z_p ∈ [0,1], all m, all x, with an absolute C (any C; C = 4 or 8 is fine),
where w_z = Σ_p z_p v_p. Facts: (a) by LP duality (our Section 7) this gives g(n) ≤ (C+16)n for the Erdős–Surányi function — the first linear bound.
(b) It suffices to treat S(n) := Σ_p min(z_p v_p(n), 1) with weights restricted to primes (the peel w = E + S with E = Σ_p (z_p v_p − 1)⁺ ≥ 0 was
proved in our Section 9: Σ_I E ≥ Σ_K E termwise via prime-power counts), so the target is Σ_K (S − C)⁺ ≤ Σ_I (S − 1)⁺.
(c) Your Lemma 12 shows naive threshold layer-cake averaging breaks (F). Routes to try, in order: (i) apply Theorem 6 to the 0/1 weight
1_{P_j} for the level sets P_j = {p : z_p ≥ 2^{-j}} (or geometric levels q^{-j}) and combine the resulting inequalities with the weights
2^{-j} — the LEFT sides combine because (S − C)⁺ ≤ Σ_j 2^{-j}(ω_{P_j} − C_j)⁺ for suitable C_j (find the right C_j, e.g. C_j = C·2^{j}/... ), and
the RIGHT sides need Σ_j 2^{-j}(ω_{P_j}(b) − 1)⁺ ≤ (S(b) − 1)⁺·(constant) — check whether a constant loss is possible (this is exactly where
our dyadic encoding S ≤ Σ_j 2^{-j} N_j ≤ 2S lives); (ii) a direct fractional certificate: c_1 = −1, c_{p^j} = z_p (affine) plus pair terms
c_{pq} = z_p z_q·(...) and triple terms — find the analogue of your pair–triple certificate with (F) Σ_{d|n} c_d ≤ (S(n) − 1)⁺ proved by a
polynomial inequality in the variables u_p = min(z_p v_p, 1) ∈ [0,1]; (iii) the cube-root peel and the sparse/dense split with η = Σ z_p/p.
Deliver: a full proof with an explicit C, status tags, every constant, a finite-check plan; or the exact obstruction (which route fails and why,
with an explicit small counterexample to the intermediate claim). Same output contract; about two hours.
