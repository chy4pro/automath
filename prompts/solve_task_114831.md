# Independent solve task (do NOT read anything under notes/proofs/)

This is a complex competition-style math problem. Solve the problem and give
a rigorous proof. Do not search the internet. Do not read any files in this
workspace outside this task file (in particular nothing under notes/).

If you cannot find a complete solution, you must NOT guess or create a
solution that appears correct but contains hidden flaws or justification
gaps. Instead, present only significant partial results that you can
rigorously prove.

**Problem.** Define a sequence of positive integers by a(1) = 1, a(2) = 2, and
for n >= 3:
  a(n) = a(n-1) + floor( 2 a(n-1) a(n-2) / (a(n-1) + a(n-2)) ).
Prove that lim_{n -> infinity} a(n+1)/a(n) exists and determine its value.

Write your complete solution to the file notes/reviews/A114831_codex_solve.md
(you may create it). State the limit value clearly and give a full rigorous
proof of convergence, with all constants explicit.
