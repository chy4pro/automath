# Capacity-method transfers (sonar sequences, weak Sidon sets, bounded multiplicity, difference triangle sets, Manhattan configurations, boxes)

Paper: **Interval capacity and second-order bounds for distinct-difference configurations**, Zenodo [10.5281/zenodo.23112229](https://doi.org/10.5281/zenodo.23112229) (2026-10-03). Source: `publish/automath-papers/capacity-transfer/`.

Headline: every sonar sequence with n rows and m columns satisfies m ≤ n + 3(π²/36)^{1/3} n^{2/3} + 4 n^{1/3} for n ≥ 160³ (coefficient ≈ 1.949; the best proved published constant located is 3.78, Osorio–Ruiz–Trujillo–Urbano 2014).

| File | Content |
|---|---|
| `REPORT.md` | Final proof record and verdicts (GPT-6 Astra) |
| `COMMON_CAPACITY.md` | The signed interval-capacity certificate (L + 2/3 + error) |
| `SONAR.md`, `SONAR_COSINE.md`, `KERNEL_FUNCTIONAL.md`, `KERNEL_PERTURBATION.md` | Sonar bounds; horizontal kernel functional; strict descent below π²/32 |
| `WEAK_SIDON.md`, `G_THIN.md`, `DIFFERENCE_TRIANGLES.md` | One-dimensional transfers |
| `MANHATTAN.md`, `BOXES.md`, `BOXES_ALL_N.md` | Product-kernel transfers |
| `check_*.js` | Dependency-free exact (BigInt) checkers of finite identities and accounting (they do not test the capacity step itself) |
| `G2_TRANSFER_20261002.md` | Bounded literature-status audit (no priority claim) |
| `REFEREE_SONAR_CLAUDE_A_20261002.md`, `REFEREE_1D_CLAUDE_20261002.md`, `REFEREE_2D_CLAUDE_20261002.md`, `REFEREE_PAPER_CLAUDE_20261002.md` | Isolated Claude Opus referee reports (PASS; PASS ×3; PASS; PASS-WITH-REPAIRS, applied) |

Lean: `g_thin_second_order`, `weakSidon_second_order`, `sonar_triangle_bound`, `difference_triangle_scope_bound`, `difference_triangle_expanded_bound` are kernel-checked in [`lean/sidon30`](../../lean/sidon30) (GitHub Actions run 37076247531, commit 2f981a7; axioms propext, Classical.choice, Quot.sound). The cosine sonar bound, Manhattan, boxes and the kernel functional results are not formalised.

Provenance: scout derivations by a Claude Opus agent (`notes/selection/transfer_targets_20261002.md`); proofs, repairs and Lean by GPT-6 Astra (Codex); referee reports by isolated Claude Opus agents; no human referee.
