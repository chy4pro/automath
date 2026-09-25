# Adversarial review task: A108211 proof draft

You are an expert mathematician and a meticulous grader for a research-level
mathematics journal. A proof draft is at `notes/proofs/A108211_draft.md` in
this workspace. Read it.

A proof is to be judged correct only if every step is rigorously justified.
Your sole task is to find and report all issues. You must act as a verifier,
NOT a solver. Do NOT attempt to correct the errors or fill the gaps you find.

Classify every issue as exactly one of:
- **Critical Error**: a step whose failure breaks the logical chain
  (invalidates the proof as written).
- **Justification Gap**: the conclusion may well be true but the argument
  given is not rigorous; assume the conclusion and continue checking
  downstream.

For each issue: quote the exact passage, explain precisely why it fails, and
state what would be needed to repair it (without doing the repair).

Note the draft itself marks Step 4 as unfinished ("TO FINALIZE") — treat the
marked gap as a known Justification Gap, but ALSO check whether the PLAN
described there can work at all (margin analysis: is the proposed telescoping
precision actually sufficient for the 1/(256 n^4) window?), and check Steps
1-3 and 5 line by line for unmarked errors (identities, inequality
directions, off-by-one in indices, the irrationality argument).

End with a verdict: VALID / INVALID (has Critical Errors) / INCOMPLETE
(gaps only), plus a numbered list of every issue found.

Do not search the internet.
