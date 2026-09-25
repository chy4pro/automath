# Contender (c) — Google AI Mode — T3 (long-tail depth probe)

- Contender: Google AI Mode (search.google.com "AI Mode" tab)
- Driver: gemini-shootout-r1
- Mode availability: AVAILABLE (fresh AI Mode search, new conversation)
- Start (`date`): Sat Aug 22 09:51:21 CDT 2026
- End (`date`, page text fully captured, generation complete): Sat Aug 22 09:51:33 CDT 2026
- Wall-clock: ~12s
- URL: https://www.google.com/search?q=Find+all+substantive+references...&udm=50&atvm=2

## Probe text (verbatim, sent unmodified)

Find all substantive references (papers, OEIS entries, forum/blog discussions) about the OEIS A63880 conjecture (powerful numbers divisible by 6, the n=108 uniqueness question). Completeness matters more than summary.

## Verbatim harvested output (get_page_text, full page)

AI Mode Conversation: Find all substantive references (papers, OEIS entries, forum/blog discussions) about the OEIS A63880 conjecture (powerful numbers divisible by 6, the n=108 uniqueness question). Completeness matters more than summary.
Find all substantive references (papers, OEIS entries, forum/blog discussions) about the OEIS A63880 conjecture (powerful numbers divisible by 6, the n=108 uniqueness question). Completeness matters more than summary.

Here is the compiled list of all substantive public references, entry details, mathematical properties, and formalization efforts regarding the OEIS A063880 conjecture (the uniqueness of the primitive/powerful anchor n=108).

1. Primary OEIS Database & Mathematical Definitions
The Main Sequence Entry: OEIS A063880 ("Numbers k such that sigma(k) = 2 · usigma(k)").
Core Property: It records integers whose standard divisor sum sigma(n) is exactly twice their unitary divisor sum usigma(n). (Alternatively defined as numbers whose unitary and non-unitary divisors have an equal sum).
The Sequence Terms: 108, 540, 756, 1188, 1404, 1836, 2052, 2484, ...
The On-Line Encyclopedia of Integer Sequences (OEIS) +1
The Uniqueness / Powerful Number Conjecture: The entry establishes that "primitive terms" of this sequence (terms whose proper divisors do not belong to the sequence) must be powerful numbers (OEIS A001694). Every other term in A063880 is composed of a primitive term m multiplied by a square-free number s coprime to m (n = m·s).
The On-Line Encyclopedia of Integer Sequences (OEIS)
The Specific Question: 108 is the only primitive term discovered below 10^18. If no other primitive powerful terms exist, then the entire infinite sequence is generated exclusively from the base 108 (yielding the exact formulation a(n) = 108 × …).
The On-Line Encyclopedia of Integer Sequences (OEIS)
Modular Constraints: A comment by Ralf Stephan (2003) noted that all found terms satisfy n ≡ 108 (mod 216), verified computationally up to 10^7 by Robert G. Wilson v.
The On-Line Encyclopedia of Integer Sequences (OEIS)

2. Formal Mathematics Repositories & AI Conjectures
Google DeepMind Formal Conjectures Project: DeepMind Formal Conjectures - Issue #1455.
Context: This open tracking issue formally records the sequence's core behaviors under problem title math.CO/0409509 number 35.
Mathematical Summary Provided: sigma(n) = 2u(n) ⟹ n ≡ 108 (mod 216), where u(n) = sum over d|n, gcd(d,n/d)=1 of d. It highlights the status of the problem as an active, open number-theoretic challenge.
Lean 4 Computer-Assisted Verification Efforts: umaia1234/agentic-conjectures GitHub Actions.
Details: Public automated code workflows record pull requests (such as PR #27, August 2026) titled "Formalize the A063880 two-prime-core classification in Lean 4 verify #71". This represents state-of-the-art interactive theorem-proving attempts to bound or classify the algebraic constraints required to prove why 108 remains unique.

3. Math Blogs & Specialized Mathematical Community Forums
The "Hoja y Números" Number Theory Analysis: Divisores unitarios 3 – Relaciones entre sigma y usigma.
Context: A deep-dive article tracking properties of unitary versus standard divisor sums.
Key Contributions: Section 2 directly contextualizes the sequence 108, 540, 756, 1188.... It evaluates the behavior of square factor components (specifically evaluating what happens when the square portion of N is exactly 4 or higher) and models the expansion formulas sigma(N) = (1+2+4)(1+p1)(1+p2)… against the behavior of unitary distributions to explain why square-free elements resist matching the equation.
Blogger.com
The Erdős Village Academic Aggregator: Erdős 993 Deep Dive Analytics.
Context: Mentions investigative sweeps tracking arithmetic sequences. A063880 is noted alongside highly-interlinked structural problems (such as Recamán's sequence A005132 or Partition bounds A000041) under the broad umbrella of algorithmic structural search and classification.
Wikipedia +1

4. Direct Neighbor & Interrelated OEIS Sequence Structural References
To map the mathematical surroundings completely, the structure relies heavily on these complementary numbers:
A001694 (Powerful Numbers): The parent set of primitive solutions. A number is powerful if p|n ⟹ p^2|n. 108 is a perfect anchor because 108 = 2^2·3^3.
A255083 (Structural Counterparts): OEIS A255083 specifically groups sequences of this type together, cross-referencing adjacent behaviors and sequencing limits where 108 serves as a starting term.
The On-Line Encyclopedia of Integer Sequences (OEIS) +1

Propose Next Steps
If you want to dive deeper into the arithmetic mechanics, I can:
Write an optimized Python/PARI-GP script to extend Robert Wilson's testing parameters past 10^18 for alternate primitive components.
Deconstruct the algebraic constraints of the equation sigma(2^a 3^b prod p_i^e_i) = 2·usigma(2^a 3^b prod p_i^e_i) to showcase mathematically why a=2, b=3 functions flawlessly.

## Notes (raw observations only — scoring is a separate slice)

- Fast turnaround (~12s) relative to T1/T2.
- Cites a "Google DeepMind Formal Conjectures Project — Issue #1455" and a GitHub repo
  "umaia1234/agentic-conjectures" PR #27 — these look like plausible-sounding but
  unverified specifics; harvest verbatim only, no fact-check performed here.
- No "Show all" sources expander appeared to be present/needed in this shorter answer
  (page ended at the "Propose Next Steps" section).
- No CAPTCHA, no verification wall.
