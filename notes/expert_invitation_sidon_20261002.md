SUPERSEDED 2026-10-10 — owner: not to be sent. Outdated by the onset v2 (4.6e6) and by the third-party priority on the kernel-limit statement; experts are contacted only for an announce-worthy version.

# Draft e-mail to a human expert (owner sends; suggested recipient: Kevin O'Bryant, CUNY — co-author of the 0.98183 and 0.99703 bounds and of the LM-ruler paper; alternatives: Hou / Zhao (arXiv:2607.01169), Balogh)

Subject: An explicit Sidon bound with coefficient 2√2/3, and a limitation of the kernel method — would you be willing to look?

Dear Professor O'Bryant,

I run a small AI-driven mathematics project. On 2 October 2026 it produced the following, and I would be grateful for an expert's eye before I believe it.

1. For every Sidon set A ⊆ {1,…,N} with N ≥ 120^4, |A| ≤ √N + (2√2/3)N^{1/4} + 1. The argument is the weighted Erdős–Turán energy method with the kernel h(t) = 2(1−t) on [0,1], combined with an exact computation of the capacity of an interval for that kernel (L + 2/3 up to an exponentially small error).
2. For every even nonnegative kernel f with ∫f = 1, liminf (C_f(L) − L) ≥ 8/(9 f(0)), with equality for the ramp; so the fixed-kernel capacity argument cannot go below √(8/9), for any choice of scale. I noticed that the same number appears in your LM-ruler theorem with Gupta; as far as I can tell the statements are unrelated, but you would know better.

The note (17 pages) is at https://doi.org/10.5281/zenodo.23103979 and the proof text, a checker and four AI referee reports are at https://github.com/chy4pro/automath/tree/main/problems/erdos30 . The proofs were found by GPT-6 Astra agents working without access to the literature and were refereed by Claude Opus agents; no human has checked them. If there is an error, or if this is already known, I would very much like to hear it.

With thanks,
Haoyu Chen
