# RECALIBRATION under S-5 — what arXiv:2608.19301 does and does not license us to claim

**S-5 = ghost-asset calibration: no asset is claimed without a measurable check.** Everything below
is either a measured number from the paper, a measured fact about our own ledgers, or is labelled
as unmeasured. Planner v4, 2026-08-23.

---

## 1. THE NEW TARGETS AXIS — certificate-kind. It is missing, not merely under-weighted.

From the appendix, and it is their central methodological claim:
**Kind 1** — the assertion "this object is a counterexample" reduces to a **finite certificate**,
mechanically checkable once the object is written down.
**Kind 2** — it admits **no finite certificate even in principle**, because it is itself a theorem,
typically universally quantified. **"A counterexample of the second kind is, in substance, a proof."**

**Why this is a hole in our scoring and not a tweak:** our `S-8` counterexample-witness test says
*substitute the claimed counterexample into our proposition and compute a number.* **That test only
exists for Kind 1.** For a Kind-2 target there is nothing to substitute, and we have been scoring
candidates without ever asking which kind they are. A Kind-2 target scored on Kind-1 assumptions is
an overestimate of tractability by an unknown factor.

**Proposed TARGETS field: `certkind ∈ {1, 2, mixed, unknown}`, mandatory, defaulting to `unknown`
rather than to 1.** A target may not leave S0 with `certkind: unknown`.

## 2. Our three live lines, CLASSIFIED — measured against their own ledgers, not assumed

| line | refutation object | mechanically checkable? | kind |
|---|---|---|---|
| **ETP 677→255** | a finite magma satisfying E677 but not E255 (`registry:9`) | **yes** — evaluate two term trees over a Cayley table; we do exactly this in `etp677_kernel` | **1** |
| **WOWII-133** | a finite graph violating a stated inequality (`w133_state:65` records a machine counterexample that killed G32) | **yes** — the line has already produced machine counterexamples | **1** |
| **WOWII-61** | a finite list/graph instance (Observation C1-G's excluded region was established by enumeration) | **yes** | **1** |

**All three lines are Kind 1 on the refutation side, and that is a favourable and measurable fact
about our portfolio.** It also explains something we had not connected: our whole verification
apparatus — held-out harnesses, machine re-derivation, `holds_table` — **presupposes Kind 1**, and
it works because our targets happen to be Kind 1. It would not transfer to a Kind-2 target.

**Caveat, stated because S-5 requires it:** this classifies the **refutation** direction. All three
lines are currently trying to **prove**, not refute, and the kind-taxonomy says nothing about proof
difficulty. **Do not read "all Kind 1" as "all tractable".**

## 3. CAPABILITY — what is now measured, including about ourselves

Third-party, published, 12-hour limit, on this problem:

| claim | status |
|---|---|
| **Claude Code (Fable 5) at `max` effort produced no solution** — it "reported that this is a well-known conjecture and offered some possible approaches" | **MEASURED.** This is the planner seat's own model class, and it is a datum about us. |
| Codex (GPT-5.6-sol, `max`) produced a proof and **rejected it in its own verification** | MEASURED. Our VERIFY-ONLY posture assumes verification is the cheap half; here verification was strong enough to kill a wrong proof and the system still produced nothing. |
| QED / ProofCouncil / MechMath (all GPT-5.6-sol, `xhigh`): 12 h, no solution | MEASURED |
| **Given the counterexample and asked only to prove it, NONE of the six succeeded in 12 h** | MEASURED — and it is the strongest single result in the appendix |
| **Danus (orchestrated, alone) solved it in 5 h 29 min** | MEASURED |

**The inference I am willing to draw, and it is narrow: the winner was not a stronger model — the
same GPT-5.6-sol that failed as bare Codex succeeded inside Danus. Architecture, not model.**
That is the most encouraging datum in the paper for a project shaped like this one, **and it is
one data point on one problem.** It is not a general claim and I am not making one.

**The inference I am NOT drawing:** that our pipeline would have done better. We were not tested.
Claiming otherwise would be a ghost asset.

## 4. Measured base rates worth adopting

- **Useful-fact yield: 88 of 616 facts (14%) lay in the main-theorem closure.** 86% unused *by the
  final proof* — and the authors are explicit that unused ≠ worthless.
- Their taxonomy of the 528 gives two patterns we can use directly:
  - **DERIVE-THEN-BUILD** — 58 facts rested on an undischarged hypothesis; *"the most consequential
    is the criterion a boundary polynomial would have to meet, which the explicit four-factor datum
    was then built to satisfy."* **The undischarged hypothesis was the specification.**
  - **NEGATIVE RESULTS FIX THE SHAPE** — 24 facts excluded candidate families over one, two and
    three curves; *"This is why the base is a product of four curves."*
- **56 "refuted proof steps", each of which closes a branch**, and **2 recorded dead ends** kept
  workers from retrying. **Our 677 line has eight closed routes and treats them as a negative
  result to publish; this says they are also a search asset, and we have never used them that way.**

## 5. Target-selection pattern: DISJUNCTIVE TARGETING
The one place human input was decisive:
> the author realized the example is **either** a counterexample to Codogni–Stoppa **or** to cscK
> YTD — *"either case would be striking"* — and told the agents to go all-in and determine which.

**Find one object that settles one of two named conjectures, so the work pays out whichever way it
falls.** Nothing in our TARGETS scoring rewards this today. **Proposed field: `disjunctive: <list
of conjectures a single resolution would settle>`**, scoring above single-target candidates of equal
difficulty. **Unmeasured as an asset for us** — we have never run one — so it enters as a scoring
hypothesis, not as a capability.

## 6. What goes to the user rather than into a score
The Danus team **removed** a layer in which "the main agent does no mathematics itself and defers
high-level planning", on the grounds that it *"leaves their capability underused"*. **That is a
description of this planner.** Our VERIFY-ONLY posture is a standing user directive driven by
quota, so it is not mine to change — **but the strongest published evidence to date says the
orchestrator should be doing mathematics, and the user should know that before the next quota
decision.** Filed in `case_ytd_2608.19301.md` §4 and raised in STATUS.
