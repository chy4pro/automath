# Primary-source read: Erdős #377 and #859

2026-09-09, dialogue automath-b6, orchestrator Claude Opus 5. **No dispatch.**

This is the step that Tuza failed on 09-08, when I dispatched on an AI summary rather than on
the paper's own text. Both papers below were downloaded from Erdős's collected papers and read
page by page. The scans carry no text layer and poppler is not installed here, so the page
JPEGs were extracted from the PDFs with a short pure-Python script
(`scratchpad/extract_jpg.py`, DCTDecode XObjects) and read as images. No dependency installed.

Sources, verified against the erdosproblems LaTeX bibliography:

- **[EGRS75]** Erdős, Graham, Ruzsa, Straus, *On the Prime Factors of (2n choose n)*,
  Math. Comp. **29** no. 129 (Jan 1975), 83–92. Received 6 June 1974.
  `https://users.renyi.hu/~p_erdos/1975-27.pdf`
- **[Er70]** Erdős, *Some Extremal Problems in Combinatorial Number Theory*, Mathematical
  Essays Dedicated to A. J. Macintyre, Ohio Univ. Press (1970), 123–133, §3 on p. 130.
  `https://users.renyi.hu/~p_erdos/1970-21.pdf`

---

## #377 — EGRS 1975

### What the paper actually proves

`f(n) = sum over primes p <= n with p not dividing C(2n,n) of 1/p` (p. 83). The paper's own
words on the open question: "The most striking fact is that we cannot decide if f(n) is
unbounded." So the site's framing of #377 is faithful to the source.

Their **Fact (1)**, p. 84, is the Kummer digit characterisation, and it is the engine of the
whole paper: `C(2n,n)` is not divisible by p exactly when every base-p digit of n is less
than p/2. **The digit route is their route, not a reformulation I brought to it.**

- **Theorem 2**: the mean of f is `c_0 = sum over k >= 2 of (log k)/2^k`.
- **Theorem 3**: the mean of `f^2` is `c_0^2`. Corollary: `f(n) = c_0 + o(1)` for almost all n.
- **(6), p. 89**: a localised version, for almost all n, over primes in `(n^alpha, n^beta)`.
- **Theorem 4**: for `alpha < 1`, `#{m <= n^alpha : m does not divide C(2n,n)} = c(alpha) n^alpha + o(n^alpha)`,
  with `c(alpha) -> 1` as `alpha -> 0`, followed by the parenthesis
  **"(In fact, c(alpha) can be explicitly calculated.)"** — and they never calculate it.

### The finding that matters

The erdosproblems page says they prove `f(n) <= c log log n` for some `c < 1`. **The paper
never states that inequality.** What it states, on p. 90, is the complementary form

> (7)  `sum over p <= n with p dividing C(2n,n) of 1/p  >  c log log n`

introduced by "By methods similar to those we have employed earlier, it is not difficult to
prove the following". The site's version follows from (7) by Mertens, so the site is not
wrong, but **three things are lost in the paraphrase, and all three are in our favour**:

1. **No numerical value of c is given anywhere in the paper, and no proof of (7) is given at
   all** — only the assertion that it is not difficult. So there is no published explicit
   constant to beat, exactly as there was no n-only bound for #708 before we started.
2. They record what they believe the truth is and say they cannot reach it: "There is no
   doubt that (7) holds for any `c > 1 - eps`, and this would follow, of course, from the
   boundedness of f(n)." So the slack between "some c" and "any c < 1" is explicitly
   acknowledged as open by the authors. **Filter step 4c is satisfied: the paper does not
   quietly record the sharper constant elsewhere.**
3. The paper states a **sharper conjecture that erdosproblems.com does not record**:
   `sum* over p <= n of 1/p = (1/2 + o(1)) log log n`, where the star restricts to primes p
   with `n = kp + r`, `p/2 < r < p`, k integral — that is, primes for which the *last* base-p
   digit of n already exceeds p/2. The 1/2 is the one-digit heuristic.

Also unlisted: p. 91 (8), `exp((log n)^(1/2-eps)) < A(n) < exp((log n)^(1/2+eps))` off a
density-zero set, where `A(n)` is the least integer not dividing `C(2n,n)`, with the remark
"It would not be difficult to obtain sharper results than (8), but an asymptotic formula
seems hard." Table 1 gives the first 100 values of A(n), numerics by N. J. A. Sloane.

### Deliverables, in order of certainty

1. **An explicit c in (7)**, equivalently the first explicit `c' < 1` with
   `f(n) <= c' log log n` for all large n. First explicit constant on a fifty-year-old
   inequality whose proof was never written down.
2. **An explicit `c(alpha)` in Theorem 4** — the authors assert it is explicitly calculable
   and do not do it. Bounded, checkable, formalisable.
3. The full boundedness question, and the unlisted `(1/2 + o(1))` conjecture, as stretch targets.

### G2

Nothing found that makes c explicit. The live adjacent line is Croot, Mousavi and Schmidt on
**Graham's** conjecture (Mathematika 70, 2024), and arXiv 2509.02835 on integers with small
digits in several bases, which gets "a weak answer to a conjecture of Graham concerning
divisibility of C(2n,n)". Those attack *infinitely many n with C(2n,n) coprime to a fixed set*,
which is a different statement from bounding f(n) uniformly. Same neighbourhood, different
target — but it does mean the digit machinery has active practitioners, so the G2 must be
re-run against Croot's group immediately before any dispatch.

---

## #859 — Erdős 1970, §3

### What the paper actually proves

`A_t` is the set of n for which t is representable as a sum of distinct divisors of n. It is
closed under multiples, and every element is a multiple of an element not exceeding `t!`, so
`A_t` has a density `d_t`. The upper bound argument is given **in full** and splits the
integers into two classes:

- **Class 1**: n with a divisor in `(t/(log t)^2, t)`. Erdős cites his own earlier work for
  "the density of these integers tends to 0 as t -> infinity (in fact the density is
  `O(1/(log t)^{c_1})`)".
- **Class 2**: n with no divisor in that interval. Then if t is a sum of divisors of n we must
  have `(31) d_t(n) > (log t)^2`, where `d_t(n)` counts divisors of n up to t. Since
  `(32) sum over n <= x of d_t(n) <= sum over u <= t of x/u < 2x log t`, the count of n <= x
  satisfying (31) is under `2x/log t`, so **class 2 has density at most `2/log t`** — fully
  explicit, and elementary.

Then: "Hence `d_t -> 0` (and in fact `d_t < 1/(log t)^{c_1}` for `t > t_0`). We can prove that
for `t > t_0`, `d_t > 1/(log t)^{c_2}`." And finally
"(33) Perhaps `d_t = (1 + o(1)) c_3/(log t)^{c_4}`, but (33) if true may not be quite easy to prove."

### Effectivity verdict, one half each way

- **Upper bound: effective, and modern technology sharpens it.** The class-2 half is already
  explicit at `2/log t`. The class-1 half is the divisor-in-an-interval problem, i.e. `H(x,y,z)`,
  and **Ford's 2008 Annals paper determined its order of magnitude**, with the Erdős exponent
  `delta = 1 - (1 + log log 2)/log 2 = 0.0860713...` and a `(log log)^(-3/2)` factor. Erdős did
  not have that in 1970. So an explicit upper-bound exponent is available today by feeding Ford
  into Erdős's own two-class split.
- **Lower bound: not effective as written.** "We can prove that" is the entire proof. No
  reference, no sketch, no constant. Note also the paper's own warning on p. 123 that
  `c, c_1, ...` "denote positive absolute constants **not necessarily the same at each
  occurrence**", so even the two `c_1`s above need not agree. **This half has to be rebuilt
  from scratch, and it is where the value is.**
- **A question worth raising, not a claim**: Ford's shape carries a `(log log t)^(-3/2)`
  factor, which does not fit Erdős's guessed clean form (33). Since the class-1 bound only
  bounds a superset of `A_t`, this does not disprove (33); it does make (33) worth
  interrogating rather than assuming, and Erdős himself hedged it.

### G2

No follow-up literature found. The relevant modern machinery is Ford's, and nobody appears to
have pointed it at `d_t`.

---

## Ranking after the read

Both survive. **#377 stays first**, on importance (it is Guy B33, the boundedness question is
the headline, and the authors call it the striking fact they cannot settle) and on tool fit
(their own Fact (1) hands us a pure digit condition, which is what our certificate machinery
eats). **#859 stays second**, with the note that its upper half is low-risk and close to
mechanical once Ford is plugged in — which is also its risk, since something that mechanical
may be folklore — while its lower half has no published proof at all and is the real prize.

#1084 and #1109 unchanged, third and fourth.
