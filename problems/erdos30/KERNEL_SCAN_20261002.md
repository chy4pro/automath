# Coordinator's independent numerical check of the key constant (2026-10-02, Fable; numpy, not a proof)

Discretised minimisation of the kernel energy E(μ,μ) over signed measures of mass 1 on [0, L]
(L = 4, 8, 16; 100–200 grid points per unit): 1/E_min − L → b.

| kernel h (normalised to mass 1) | a = f(0) | b | √(ab) |
|---|---|---|---|
| indicator (classical; f = tent) | 1 | 1.0000 | 1.0000 (Lindström) |
| (1−t)^0.5 | 1.122 | 0.802 | 0.9487 |
| (1−t)^0.8 | 1.242 | 0.717 | 0.9435 |
| **(1−t)^1 = the proof's kernel** | 1.329 (exact 4/3) | 0.6687 (exact 2/3) | **0.9428** |
| (1−t)^1.2 | 1.419 | 0.627 | 0.9433 |
| (1−t)^1.5 | 1.558 | 0.573 | 0.9449 |
| (1−t)^2 | 1.794 | 0.502 | 0.9487 |
| cos(πt/2) | 1.229 | 0.729 | 0.9470 |
| cos²(πt/2) | 1.494 | 0.597 | 0.9446 |
| (1−t) ± small quadratic perturbations | | | 0.9433 |

Reading: the boundary constant b = 2/3 claimed in SIDON_BOUND_PROOF.md §3–§4 is reproduced
numerically; within these families the linear kernel is a local minimiser of √(ab), and the
published numerical records (0.94349, 0.94324, 0.94301) sit where nearby kernels land. This
supports — but does not prove — that 2√2/3 is the limit of this method family.

## Numerical optimisation over kernel shapes (same day; numerics/kernel_opt.py, log kernel_opt_m16.log)

L-BFGS-B over nonnegative piecewise-constant kernels on [0,1] with 16 free values, four starts
(the ramp and three random perturbations of it): all four converge to the same optimum, which is
the ramp itself up to the left-endpoint/midpoint sampling artefact (values 1.000, 0.938, 0.875, …,
0.064 = (16−i)/16). Objective a·b = 0.889677 against 0.889743 for the midpoint-sampled ramp on the
same grid (difference 3.5·10⁻⁵ in √(ab), i.e. discretisation noise; exact value 8/9 = 0.888889).
Reading: no kernel in this class beats the ramp; the search returns the ramp from every start.
Evidence only — the optimality question is being attacked as a theorem (Codex task 030).
