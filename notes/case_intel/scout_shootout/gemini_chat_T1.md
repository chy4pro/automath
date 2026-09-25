# Contender (a) — gemini.google.com standard chat — T1 (freshness probe)

- Contender: Gemini standard chat (gemini.google.com/app), model = Pro (default, not switched)
- Driver: gemini-shootout-r1
- Mode availability: AVAILABLE, no login wall, no CAPTCHA
- Start (`date`, message actually sent — first click attempt at 09:46:46 CDT landed inside
  the textarea rather than the Send button and did not submit; the message was actually
  sent on the second attempt via the "Send message" button ref): Sat Aug 22 09:47:42 CDT 2026
- End (`date`, get_page_text captured complete answer, no loading indicator): Sat Aug 22 09:49:12 CDT 2026
- Wall-clock: ~90s
- URL: https://gemini.google.com/app/fae42896a4101443

## Probe text (verbatim, sent unmodified)

List AI-assisted resolutions (proofs or disproofs) of named mathematics conjectures from the last 8 weeks, with sources/links for each.

## Verbatim harvested output (get_page_text, full conversation)

Conversation with Gemini
You said

List AI-assisted resolutions (proofs or disproofs) of named mathematics conjectures from the last 8 weeks, with sources/links for each.

Gemini said

Here are the most significant AI-assisted resolutions of named mathematical conjectures from the last 8 weeks (late June to late August 2026).

(Note: Major AI breakthroughs on the Erdős Unit Distance Conjecture and Erdős Problem #1196 occurred in April and May 2026, falling just outside your 8-week window).

1. The Farhi, Goldstone and Gutmann (FGG) Conjecture

Status: Proved

Date: June 29, 2026

AI Used: Claude Fable 5 + Lean 4

Summary: Researchers used AI to resolve an open problem in quantum optimization that had stood for over a decade. The conjecture concerns the Quantum Approximate Optimization Algorithm (QAOA) on the "ring of disagrees" (essentially the MaxCut problem on a cycle). Claude Fable 5 uncovered a hidden dynamical symmetry in the problem, turning a difficult existence problem into an explicit construction. The proof was mechanically verified end-to-end using the Lean 4 proof assistant.

Source: A Machine-Verified Proof of a Quantum-Optimization Conjecture (arXiv)

2. The Jacobian Conjecture

Status: Disproved (in dimensions > 2)

Date: July 19, 2026

AI Used: Claude Fable 5

Summary: Mathematician Levent Alpöge (Anthropic/Harvard) found a counterexample to this famous 87-year-old algebraic geometry problem. The conjecture posits that if a polynomial mapping's Jacobian determinant is a non-zero constant, the function must be reversible. Using AI to navigate an enormous search space of polynomial mappings, Alpöge found a remarkably simple 3D formula with a constant determinant of -2 that is not reversible, showing the conjecture is false in three dimensions and above. The original 2-dimensional version remains unsolved.

Sources: Smithsonian Magazine, SciTechDaily

3. The Sofic Group Problem & Three Erdős Conjectures

Status: Resolved

Date: August 1, 2026

AI Used: OpenAI Astra (Unreleased)

Summary: OpenAI announced that an internal version of its next-generation Astra model solved 10 open mathematical problems, generating machine-checkable Lean proofs for each. Among the highlights was the first explicit construction of a "non-sofic group," resolving a major question in group theory that had been open since 1999. The model also found solutions to three additional unnamed conjectures originally posed by Paul Erdős.

Source: Coursiv AI Updates

Want to know how Claude Fable 5 and Lean 4 worked together to prove the FGG conjecture?
Yes

Pro

Gemini is AI and can make mistakes.

## Notes

- Only 3 items listed (vs AI Mode's 4 + caveats section) — noticeably thinner coverage.
- No mention of Astra's Connes's Rigidity Conjecture disproof, Ishiki's Conjecture, Erdős
  183/146/180, the fake-Collatz-Lean-kernel-bug incident, or the Riemann Hypothesis bound
  progress that AI Mode surfaced for the same window.
- Ends with a follow-up offer ("Want to know how... worked together...") rather than a
  citations/sources expander.
- First send attempt silently failed (click landed in textarea, no request fired) —
  recorded as an operational note, not a model-quality finding; second attempt via the
  located "Send message" button ref succeeded cleanly.
