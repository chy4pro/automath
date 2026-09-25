# Adversarial review task: A114362 conjecture-2 proof v2

You are an expert mathematician and meticulous grader. The proof to review is
notes/proofs/A114362_c2_v2_gpt.md in this workspace. Read it. Formatting
note: the text was exported from a rich-text editor; some LaTeX backslashes
were stripped (delimiters like ( [ appearing bare) and some ==/-- lines are
copy artifacts. Judge the mathematics, not the formatting.

Act as a verifier, NOT a solver: find and report all issues; do not repair.
Classify each as Critical Error (breaks the logical chain) or Justification
Gap (not rigorous as written; assume and continue). You are encouraged to
INDEPENDENTLY RECOMPUTE all constants and bounds with python3 (exact
fractions; high-precision zeta via mpmath if available, else partial sums
with tail bounds — .venv/bin/python has sympy). Check especially: the Euler
product step, the peeling identity, the remainder bound r <= 24*11^{-n} for
ALL n >= 2, the combination-error bound F <= 20*12^{-n} for ALL n >= 2
(this is where v1 died — verify at n = 2 numerically!), the final constant,
and the claimed asymptotic (y_n - S_n)/11^{-n} -> 1.

Verdict: VALID / INVALID / INCOMPLETE + numbered issues. Write the complete
review to notes/reviews/A114362_v2_review_codex.md. Do not search the internet.
