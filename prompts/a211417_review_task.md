# Task: S3 adversarial review of the A211417 / Bala D(r) proof

You are a VERIFIER, not a co-author: find errors, do not fix.

Target: notes/proofs/a211417_v1.md (claims: full proof of Bala's general
divisibility conjecture for A211417, all r>=1, with explicit D(r); plus the
C(k,r) sister family k=2,3,5). Verification script notes/proofs/a211417_verify.py
(runs under .venv/bin/python).

Review protocol:
1. Check the reduction: Legendre valuation formula v_p(a(n)) = #{k: Delta(n/p^k)=1}
   with Delta(x) = floor(30x)+floor(x)-floor(15x)-floor(10x)-floor(6x). Verify
   Delta has period 1, values in {0,1}, and the claimed unit-class rigidity
   (Lemma A): Delta_c = 1 for every unit c mod 30 — re-derive independently.
2. The crux is Lemma C (prime-power layering): for p^k > r the witness i is
   unique and lossless; losses confined to p^k <= r layers bounded by E(p,r)
   independent of n. Scrutinize: (a) uniqueness of witness when p^k > r;
   (b) whether "loss" is correctly quantified when several i in L_r share the
   same prime p across DIFFERENT powers; (c) edge cases n small (30n - i can be
   smaller than p^k), i = r, p in {2,3,5} exclusion.
3. Classify findings: CRITICAL ERROR vs JUSTIFICATION GAP vs EDITORIAL.
4. Independently re-run the verify script AND write your own small independent
   check (different code path) for at least: D(13)=1001 up to n=50, and one
   C(k,r) instance.
5. Verdict: VALID / INVALID / VALID-WITH-GAPS.

Output: notes/reviews/a211417_review1.md. Do not modify the proof file.
