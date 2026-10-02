#!/usr/bin/env python3
"""Exact arithmetic and exhaustive finite checks for SIDON_BOUND_PROOF.md.

Python 3.8+; standard library only.  No floating point enters a mathematical
comparison.  Time measurements serve only the explicitly reported search budget.

    python3 check_sidon_bound.py
    python3 check_sidon_bound.py --max-n 60 --node-budget 0 --seconds 0
    python3 check_sidon_bound.py --numerics-only

The default searches ALL N <= 60, with a shared 5,000,000-node / 120-second
budget.  A budget interruption prints rigorous lower/upper bounds, says
INCOMPLETE, and exits 2.  Zero removes that particular budget.  An assertion
failure exits nonzero.  Only exhaustive completion or a proved pruning bound
can certify a maximum.  A witness alone never certifies maximality.

The finite search is a branch-and-bound enumeration of normalized strong Sidon
sets (Golomb rulers).  It derives minimum spans for successive cardinalities;
those spans give maxima for every smaller interval simultaneously.  No stored
table of optimal rulers, SAT solver, or external mathematical library is used.

The finite sanity checks do not verify the renewal or signed-measure proof and
do not apply the theorem below its stated onset.  Status of the proof document:
same-vendor reviewed only.  Running this program does not change that status.
"""

import argparse
from fractions import Fraction as Q
from math import isqrt
import sys
from time import monotonic


N0 = 207360000


def require(condition, message):
    """Do not use assert: python -O must not disable a verification."""
    if not condition:
        raise AssertionError(message)


class Interval:
    """Closed rational intervals; operations used here are outward exact."""

    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        require(self.lo <= self.hi, "reversed interval")

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Interval) else Interval(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        products = [a * b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        require(other.lo > 0 or other.hi < 0, "division interval contains zero")
        return self * Interval(1 / other.hi, 1 / other.lo)

    def __pow__(self, exponent):
        require(isinstance(exponent, int) and exponent >= 0,
                "only nonnegative integer powers are supported")
        result = Interval(1)
        for _ in range(exponent):
            result = result * self
        return result


def root_interval(n, degree, bits=80):
    """Enclose sqrt(n) or fourth_root(n) between dyadic rationals."""
    require(n >= 0 and degree in (2, 4), "unsupported root")
    scale = 1 << bits
    radicand = n * scale ** degree
    floor_root = isqrt(radicand)
    if degree == 4:
        floor_root = isqrt(floor_root)
    require(floor_root ** degree <= radicand < (floor_root + 1) ** degree,
            "integer root enclosure")
    hi = floor_root if floor_root ** degree == radicand else floor_root + 1
    return Interval(Q(floor_root, scale), Q(hi, scale))


def numerical_checks(extra_grid):
    """Check the final inequalities using an analytic rational tail majorant.

    alpha=log(4/3)>=1/4 follows by integrating 1/t>=3/4 on [1,4/3].
    sqrt(2)<=3/2 gives alpha/sqrt(2)>=1/6.  Since e>2, and
    (x exp(-x/6))'=exp(-x/6)(1-x/6)<=0 for x>=120, the proof's
    epsilon*x is strictly below 24000/2**20 < 1/32 for EVERY x>=120.
    Thus epsilon lies in [0,1/(32*x)].  This avoids numerical exp/log and
    the grid checks enclose the actual epsilon, not an uncertified estimate.
    The grid is a regression check; the monotonicity argument is the all-N step.
    """
    require(N0 == 120 ** 4, "onset arithmetic")
    require(Q(1, 4) / Q(3, 2) == Q(1, 6), "exponential rate")
    require(Q(24000, 2 ** 20) < Q(1, 32), "tail bound at x=120")
    require(Q(1) - Q(120, 6) < 0, "tail derivative at onset")
    require(Q(3, 2) ** 2 > 2, "upper square-root bound")
    require(Q(8, 9) < 1, "gamma<1")
    require(Q(943, 1000) ** 2 - Q(8, 9) == Q(3241, 9000000),
            "coefficient comparison")
    require(Q(1, 8) + Q(3, 64) == Q(11, 64), "error coefficient")
    require(1 - Q(11, 64) == Q(53, 64) > 0, "positive final margin")

    # Exact symbolic coefficient check in Q[s]/(s^2-2), s=sqrt(2).
    def qa(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def qm(a, b):
        return (a[0] * b[0] + 2 * a[1] * b[1],
                a[0] * b[1] + a[1] * b[0])

    zero = (Q(0), Q(0))
    gamma_q = (Q(0), Q(2, 3))
    y = [(Q(1), Q(0)), gamma_q, (Q(1), Q(0))]
    polynomial = [zero for _ in range(5)]
    for i, a in enumerate(y):
        for j, b in enumerate(y):
            polynomial[i + j] = qa(polynomial[i + j], qm(a, b))
    for i, a in enumerate([(Q(-8, 9), Q(0)), (Q(0), Q(-2, 3))]):
        for j, b in enumerate(y):
            polynomial[i + j] = qa(polynomial[i + j], qm(a, b))
    polynomial[3] = qa(polynomial[3], (Q(0), Q(-2, 3)))
    polynomial[4] = qa(polynomial[4], (Q(-1), Q(0)))
    require(polynomial == [(Q(1, 9), Q(0)), (Q(0), Q(2, 27)),
                           (Q(10, 9), Q(0)), zero, zero],
            "exact expansion of P_0(x^2+gamma*x+1)")

    grid = sorted(set([N0, N0 + 1, N0 + 17, 121 ** 4, 128 ** 4,
                       2 * N0, 10 ** 9, 10 ** 12, 10 ** 16, 10 ** 24]
                      + extra_grid))
    for n in grid:
        require(n >= N0, "numerical theorem grid must satisfy N>=N0")
        # Both irrational enclosures need more bits for enormous extra N:
        # uncertainty in gamma is also multiplied by terms of order x^3.
        bits = max(80, n.bit_length() + 32)
        x = root_interval(n, 4, bits)
        s = root_interval(2, 2, bits)
        gamma = Q(2, 3) * s
        y = x ** 2 + gamma * x + 1
        epsilon = Interval(0, Q(1, 32) / x.lo)
        p0 = Q(10, 9) * x ** 2 + (gamma / 9) * x + Q(1, 9)
        error = epsilon * (Q(4, 3) * y + s * x ** 3)
        # Direct substitution, and independently the cancellation-free form.
        direct = (y ** 2 - (gamma * x + Q(8, 9) + Q(4, 3) * epsilon) * y
                  - n - gamma * x ** 3 - s * epsilon * x ** 3)
        require(x.lo >= 120, "fourth-root onset")
        require((x / s).lo >= 1, "energy lemma requires L>=1")
        require(p0.lo - error.hi > 0, "expanded polynomial positivity")
        require(direct.lo > 0, "direct polynomial positivity")
        require((error / (x ** 2)).hi < Q(11, 64), "uniform error bound")
        print("NUMERIC PASS N={} P_epsilon(y)>0 (exact rational intervals)".format(n))
    print("NUMERIC PASS: onset, symbolic expansion, tail monotonicity constants, "
          "and coefficient comparison; grid is not an all-N proof.")


def kernel(t):
    t = abs(Q(t))
    return Q(4, 3) - 2 * t + Q(2, 3) * t ** 3 if t <= 1 else Q(0)


def strong_sidon(points):
    """The precise a<=b sum convention, including doubled elements."""
    sums = [a + b for i, a in enumerate(points) for b in points[i:]]
    return len(sums) == len(set(sums))


def unique_positive_differences(points):
    differences = [b - a for i, a in enumerate(points) for b in points[i + 1:]]
    return (all(d > 0 for d in differences)
            and len(differences) == len(set(differences)))


def kernel_sanity(points, n):
    """Exact finite checks of the universal ordered-difference/kernel bound.

    Check both sides of E=4k/3+2 sum_{positive differences}f(d/T), and
    E<=4k/3+2 sum_{d>=1}f(d/T)<=4k/3+T. For T<=N also check the
    finite-interval lower energy and combined quadratic inequalities.
    The values of T are rational and include values below one. No
    large-N conclusion is used here.
    """
    require(strong_sidon(points), "sum-convention witness check")
    require(unique_positive_differences(points), "difference-convention witness check")
    k = len(points)
    for t in sorted(set([Q(1, 2), Q(1), Q(3, 2), Q(2), Q(n, 2), Q(n)])):
        energy = sum((kernel(Q(a - b) / t) for a in points for b in points), Q(0))
        diagonal = Q(4 * k, 3)
        positive = sum((kernel(Q(b - a) / t)
                        for i, a in enumerate(points) for b in points[i + 1:]), Q(0))
        all_d = sum((kernel(Q(d) / t) for d in range(1, t.numerator // t.denominator + 1)), Q(0))
        require(energy == diagonal + 2 * positive, "ordered-pair/diagonal identity")
        require(positive <= all_d, "Sidon difference injection")
        require(2 * all_d <= t, "monotone kernel sum bound")
        require(energy <= diagonal + t, "universal energy upper bound")
        if t <= n:
            length = Q(n) / t
            ceiling = (length.numerator + length.denominator - 1) // length.denominator
            # Since alpha=log(4/3), this is a rational LOWER bound on
            # 200*exp(-alpha*L). The smaller positive denominator makes
            # the following tests stronger than the lemmas' inequalities.
            # Failure of this sufficient test alone would not refute a lemma.
            epsilon_lower = 200 * Q(3, 4) ** ceiling
            denominator = length + Q(2, 3) + epsilon_lower
            require(energy * denominator >= k * k,
                    "stronger sufficient lower-energy sanity check failed; "
                    "this alone would not refute the lemma")
            require(denominator * (t + diagonal) >= k * k,
                    "stronger sufficient quadratic sanity check failed; "
                    "this alone would not refute the lemma")


def bit_count(value):
    # Python 3.8 compatibility; int.bit_count was introduced in Python 3.10.
    return value.bit_count() if hasattr(int, "bit_count") else bin(value).count("1")


def first_bits_sum(mask, count):
    total = 0
    greatest = -1
    for _ in range(count):
        if not mask:
            return None, None
        bit = mask & -mask
        greatest = bit.bit_length() - 1
        total += greatest
        mask ^= bit
    return total, greatest


def span_lower_bound(k):
    """Elementary necessary span, valid for every k-mark strong Sidon set.

    For index separation <=h there are m=h*k-h*(h+1)/2 distinct
    positive differences. Their sum is at least m(m+1)/2. Writing the sum
    as sum_i w_i*a_i gives w_i=min(h,i)-min(h,k-1-i).  With 0<=a_i<=L,
    it is at most L*sum_{w_i>0}w_i.  Maximize the resulting bound over h.
    In particular k=11,h=2 gives L>=64, excluding 11 marks when N<=60.
    """
    if k <= 1:
        return 0
    lower = k * (k - 1) // 2
    for h in range(1, k):
        m = h * k - h * (h + 1) // 2
        weights = [min(h, i) - min(h, k - 1 - i) for i in range(k)]
        c = sum(w for w in weights if w > 0)
        lower = max(lower, (m * (m + 1) // 2 + c - 1) // c)
    return lower


class SearchLimit(Exception):
    pass


class Budget:
    def __init__(self, nodes, seconds):
        self.limit = nodes
        self.seconds = seconds
        self.started = monotonic()
        self.nodes = 0

    def tick(self):
        if self.limit and self.nodes >= self.limit:
            raise SearchLimit("node budget {} reached".format(self.limit))
        # Checking time on every node makes the reported time budget transparent.
        if self.seconds and monotonic() - self.started >= self.seconds:
            raise SearchLimit("time budget {} seconds reached".format(self.seconds))
        self.nodes += 1


class RulerSearch:
    """Complete branch-and-bound for the minimum span of k normalized marks.

    Every set translates to one beginning at 0. Reflection reverses its gaps;
    for k>=3 all gaps are distinct, so exactly one reflection has first gap
    smaller than last gap.  These are the only symmetry reductions.

    `candidates` contains exactly the individually addable positions above the
    last mark. If v is chosen, new differences are v-a (a in old marks).
    A future c is forbidden precisely when c-v is old/new used, or c-a is
    one of those new differences. Bit shifts implement these exclusions.
    Joint future conflicts are checked when the later mark is inserted.

    Pruning uses only proved minimum subruler spans, the number of remaining
    candidates, sums of distinct unused adjacent gaps, and the index-band
    difference sum underlying span_lower_bound. All bounds are necessary.
    A changing incumbent only removes sets whose span is no better.
    """

    def __init__(self, k, cap, exact_spans, budget, visit=None):
        self.k = k
        self.cap = cap
        self.exact_spans = exact_spans
        self.budget = budget
        self.visit = visit
        self.best = cap + 1
        self.witness = None
        self.lower = span_lower_bound(k)
        self.bands = []
        for h in range(1, min(k - 1, 3) + 1):
            weights = [min(h, i) - min(h, k - 1 - i) for i in range(k)]
            self.bands.append((h, h * k - h * (h + 1) // 2, weights))

    def min_span(self, k):
        return self.exact_spans[k] if k < len(self.exact_spans) else span_lower_bound(k)

    def run(self):
        if self.lower > self.cap:
            self.budget.tick()
            return None
        self.dfs([0], 0, 1 << self.cap, ((1 << (self.cap + 1)) - 1) ^ 1)
        return self.witness

    def dfs(self, marks, used, reversed_marks, candidates):
        self.budget.tick()
        if self.visit:
            self.visit(marks, used, candidates)
        p = len(marks)
        r = self.k - p
        if not r:
            if self.k >= 3 and marks[1] >= marks[-1] - marks[-2]:
                return
            if marks[-1] < self.best:
                require(strong_sidon(marks), "search returned a non-Sidon witness")
                self.best = marks[-1]
                self.witness = list(marks)
            return
        if self.best == self.lower:
            return
        upper = self.best - 1
        if any(a + self.min_span(self.k - j) > upper for j, a in enumerate(marks)):
            return
        bounded_candidates = candidates & ((1 << (upper + 1)) - 1)
        if bit_count(bounded_candidates) < r:
            return

        # The r future adjacent gaps are distinct and unused. At least one
        # (the final gap) must exceed the first gap under reflection symmetry.
        available = ((1 << (upper + 1)) - 2) & ~used
        gap_sum, largest_small = first_bits_sum(available, r)
        if gap_sum is None:
            return
        if self.k >= 3 and p >= 2 and largest_small <= marks[1]:
            large = available & ~((1 << (marks[1] + 1)) - 1)
            if not large:
                return
            gap_sum += (large & -large).bit_length() - 1 - largest_small
        if marks[-1] + gap_sum > upper:
            return

        # A band sum must contain its known terms and enough smallest unused
        # differences for the unknown terms. Bound its signed-coordinate
        # expression above using already proved minimum subruler spans.
        for h, m, weights in self.bands:
            known_terms = [marks[j] - marks[i] for j in range(p)
                           for i in range(max(0, j - h), j)]
            missing_sum, _ = first_bits_sum(available, m - len(known_terms))
            if missing_sum is None:
                return
            maximum = sum(weights[i] * marks[i] for i in range(p))
            for i in range(p, self.k):
                if weights[i] < 0:
                    position = marks[-1] + self.min_span(i - p + 2)
                else:
                    position = upper - self.min_span(self.k - i)
                maximum += weights[i] * position
            if sum(known_terms) + missing_sum > maximum:
                return

        # The next mark begins an r-mark suffix.
        next_upper = upper - self.min_span(r)
        if p == 1 and self.k >= 3:
            next_upper = min(next_upper, (upper - self.min_span(self.k - 2) - 1) // 2)
        choices = bounded_candidates & ((1 << (next_upper + 1)) - 1)
        if r == 1 and self.k >= 3:
            choices &= ~((1 << (marks[-1] + marks[1] + 1)) - 1)
        while choices:
            bit = choices & -choices
            choices ^= bit
            v = bit.bit_length() - 1
            # An incumbent improvement can make the remaining loop obsolete.
            if v + self.min_span(r) >= self.best:
                break
            new_differences = reversed_marks >> (self.cap - v)
            require((new_differences & used) == 0, "candidate invariant")
            forbidden = used << v
            for a in marks:
                forbidden |= new_differences << a
            forbidden |= new_differences << v
            next_candidates = candidates & ~((1 << (v + 1)) - 1) & ~forbidden
            self.dfs(marks + [v], used | new_differences,
                     reversed_marks | (1 << (self.cap - v)), next_candidates)


def exhaustive_self_check():
    """Independent literal subset enumeration on N<=12 audits the search.

    Also checks the sum/difference convention on EVERY subset, verifies the
    kernel bound on EVERY strong Sidon subset, and checks the bitmask candidate
    invariant at every visited search node. This is an internal implementation
    test, not a separate proof implementation for the infinite theorem.
    """
    literal = {}
    sidon_count = 0
    for n in range(1, 13):
        best = 0
        for mask in range(1 << n):
            points = [i for i in range(n) if mask & (1 << i)]
            sums_ok = strong_sidon(points)
            require(sums_ok == unique_positive_differences(points),
                    "strong-Sidon/positive-difference equivalence")
            if sums_ok:
                best = max(best, len(points))
                kernel_sanity(points, n)
                sidon_count += 1
        literal[n] = best

    cap = 11
    budget = Budget(0, 0)

    def audit_node(marks, used, candidates):
        expected_used = sum(1 << (b - a) for i, a in enumerate(marks) for b in marks[i + 1:])
        require(used == expected_used, "used-difference bitmask")
        expected_candidates = sum(1 << v for v in range(marks[-1] + 1, cap + 1)
                                  if strong_sidon(marks + [v]))
        require(candidates == expected_candidates, "complete candidate bitmask")

    spans = [0, 0]
    for k in range(2, 14):
        search = RulerSearch(k, cap, spans, budget, audit_node)
        witness = search.run()
        if witness is None:
            break
        spans.append(witness[-1])
    for n, expected in literal.items():
        actual = max(k for k in range(1, len(spans)) if spans[k] < n)
        require(actual == expected, "branch-and-bound vs literal subsets at N={}".format(n))
    print("SELF-CHECK PASS: every subset for N<=12; {} Sidon subsets; "
          "{} audited search nodes.".format(sidon_count, budget.nodes))


def finite_search(max_n, node_budget, seconds):
    cap = max_n - 1
    budget = Budget(node_budget, seconds)
    spans = [0, 0]
    witnesses = {1: [0]}
    exhaustive_no_k = None
    interrupted = None
    print("SEARCH: N<= {}, span<= {}; global node budget={}, seconds={}.".format(
        max_n, cap, node_budget or "unlimited", seconds or "unlimited"), flush=True)
    for k in range(2, max_n + 2):
        before = budget.nodes
        search = RulerSearch(k, cap, spans, budget)
        try:
            witness = search.run()
        except SearchLimit as exc:
            if search.witness is not None:
                witnesses[k] = search.witness
            interrupted = "k={}: {}".format(k, exc)
            print("SEARCH INCOMPLETE: " + interrupted, flush=True)
            break
        if witness is None:
            exhaustive_no_k = k
            print("SEARCH EXACT: no {}-mark ruler of span<= {}; nodes={}.".format(
                k, cap, budget.nodes - before), flush=True)
            break
        witnesses[k] = witness
        spans.append(witness[-1])
        print("SEARCH EXACT: minimum span for k={} is {}; witness={}; nodes={}.".format(
            k, witness[-1], witness, budget.nodes - before), flush=True)

    all_exact = True
    print("TABLE: N lower_bound upper_bound status witness_in_{1,...,N}")
    for n in range(1, max_n + 1):
        lower = max(k for k, w in witnesses.items() if w[-1] < n)
        upper = max(k for k in range(1, max_n + 1) if span_lower_bound(k) < n)
        for k in range(2, len(spans)):
            if spans[k] >= n:
                upper = min(upper, k - 1)
        if exhaustive_no_k is not None:
            upper = min(upper, exhaustive_no_k - 1)
        require(lower <= upper, "inconsistent finite bounds")
        status = "EXACT" if lower == upper else "INCOMPLETE"
        all_exact = all_exact and lower == upper
        w = [a + 1 for a in witnesses[lower]]
        kernel_sanity(w, n)
        print("{} {} {} {} {}".format(n, lower, upper, status, w))
    print("SEARCH: {} nodes; {:.3f} seconds; kernel checks passed on all displayed witnesses.".format(
        budget.nodes, monotonic() - budget.started))
    if interrupted is not None or not all_exact:
        print("INCOMPLETE: no unproved maximum has been labelled exact. "
              "To complete all 60: --max-n 60 --node-budget 0 --seconds 0")
        return False
    print("FINITE PASS: exact maxima for EVERY 1<=N<={}; complete branch-and-bound "
          "with proved pruning. This is a finite sanity check below the theorem onset.".format(max_n))
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--max-n", type=int, default=60, help="check every N from 1 to this value (default 60)")
    parser.add_argument("--node-budget", type=int, default=5000000, help="shared exact-search node budget; 0=unlimited")
    parser.add_argument("--seconds", type=float, default=120, help="shared exact-search time budget; 0=unlimited")
    parser.add_argument("--grid", type=int, nargs="*", default=[], help="additional integer N>=N0 for rational interval checks")
    parser.add_argument("--numerics-only", action="store_true", help="explicitly skip all finite searches and finite self-checks")
    args = parser.parse_args()
    if args.max_n < 1:
        parser.error("--max-n must be positive")
    if (
        args.node_budget < 0 or args.seconds < 0 or args.seconds == float("inf")
        or args.seconds != args.seconds
    ):
        parser.error("budgets must be nonnegative and seconds finite")
    if any(n < N0 for n in args.grid):
        parser.error("every --grid value must satisfy N>=N0")
    numerical_checks(args.grid)
    if args.numerics_only:
        print("NUMERICS-ONLY PASS: finite N<=60 request has NOT been checked in this run.")
        return 0
    exhaustive_self_check()
    return 0 if finite_search(args.max_n, args.node_budget, args.seconds) else 2


if __name__ == "__main__":
    sys.exit(main())
