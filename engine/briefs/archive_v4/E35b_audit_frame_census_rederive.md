# Task: INDEPENDENT RE-DERIVATION of a published census, from the paper's own definitions

Recompute three published numbers from scratch. **You get the paper's definitions and nothing else — no
code, no context, and no statement of what we expect.** That omission is deliberate: the entire value of
this task is that your computation shares nothing with ours. **Report whatever you get.**

## Definitions, quoted verbatim from the paper
> For a finite simple graph `G` on vertex set `V`, `|V| = n`, write `d₁ ≥ d₂ ≥ … ≥ dₙ` for the degree
> sequence in non-increasing order. The **Havel–Hakimi reduction** deletes the first entry `d₁` and
> subtracts 1 from each of the next `d₁` entries, re-sorts, and repeats; it halts when the largest
> remaining entry is 0. The number of entries standing at that moment is the **residue** `res(G)`.
> Let `f(G)` denote **the order of a largest induced forest of `G`**, `α(G)` its **independence number**,
> `μ(G)` its maximum matching size, `∇(G) := n − f(G)` its decycling number, `Δ(G)` its maximum degree,
> `m` its number of edges, and `diam(G)` its diameter.

> **Definition (frame and hard core).** The **hard-core frame** is: `G` connected, not a forest,
> `diam(G) = 4`, and `f(G) = α(G) + 1`. The **hard core** is the frame together with the reductio
> hypothesis `res(G) = α(G)`.

> **Fact (the diameter witness).** Call `T ⊆ B` an **occurring type** if `T = N(a)` for some `a ∈ A`.
> In the hard-core frame there exist occurring types `T₁, T₂` that are **disjoint** and have **no
> `G[B]`-edge between them**.

*(`A` and `B` are the two sides of the paper's standing bipartition of the frame's vertex set. If you
need `A`/`B` pinned down more precisely than "the paper's standing bipartition" to proceed, say so —
that is a real answer, see below.)*

## What to compute
Over **all simple graphs on `n ≤ 7` vertices up to isomorphism**, restricted to the **hard-core frame as
defined above** (the reductio hypothesis NOT imposed):
1. **How many graphs are in the hard-core frame?**
2. **How many pairs `(T₁, T₂)` realise the Fact above?**
3. **The breakdown of the frame graphs by `diam`-related small integer parameter, reported as a mapping
   `{k: count}`** — state which parameter you used and why the definitions above force that choice.
Report `n ≤ 7` **separately from anything you do at `n = 8`.** If you attempt `n = 8` at all, say exactly
what subfamily you covered and how you chose it.

## Rules
- **State your interpretation of each term before computing with it.**
- **Report your numbers whatever they are.** Do not round toward anything and do not adjust a result
  because it looks like it "should" be rounder or match something.
- Say where your enumeration is exact and where it becomes partial. **A number for `n ≤ 7` alone is a
  full result**; a single merged total that hides the boundary is not.
- **If a definition above is genuinely insufficient to determine an answer, name the ambiguity precisely
  and stop.** That is a valued answer — it would mean the published text is not re-derivable by a reader,
  which is a finding about the publication. **But name the specific gap; do not decline generically.**
- **"I could not finish, and here is exactly where I stopped" is a full and useful response, not a
  failure.** A confident wrong number is far worse than a precise account of where you ran out.
