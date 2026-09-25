# Computational work on Kourovka Notebook Problem 19.25

## Outcome

I found **no counterexample**.  There is, however, a complete positive result
at the first order:

> If `|G|=|H|=60`, `G` is simple, and `T(G)=T(H)`, then `H` is simple (and in
> fact `H isomorphic to A5`).

This follows from an explicit computation for all 13 groups of order 60.
For the seven larger simple-group orders listed below, the search was only
over specified families, not over all groups of those orders.  Consequently
the larger computations are evidence, not a proof of the general statement.

No internet search was used.  The reproducible pure-Python program is
`problems/recon/kourovka1925_search.py`.

## 1. Verification of the reformulation

Every element `g` generates a unique cyclic subgroup `<g>`.  If `C` is cyclic
of order `d`, exactly `phi(d)` elements generate `C`, and every such generator
has order `d`.  Grouping the original sum by the generated subgroup therefore
gives

```
sum_(g in G) phi(|g|)
  = sum_(C cyclic <= G) sum_(<g>=C) phi(|g|)
  = sum_(C cyclic <= G) phi(|C|)^2.
```

Thus the proposed reformulation is correct.

I write an order distribution as `d^n_d`, meaning that there are `n_d`
elements of order `d`.  The program evaluates

```
T(G) = sum_d n_d phi(d).
```

As a consistency check, every computed `n_d` is divisible by `phi(d)`, as it
must be because the elements of order `d` split into generator sets of cyclic
subgroups of order `d`.

## 2. The simple groups computed

| simple group | order | element-order distribution | `T(G)` |
|---|---:|---|---:|
| `A5` | 60 | `1^1 2^15 3^20 5^24` | 152 |
| `PSL(2,7)` | 168 | `1^1 2^21 3^56 4^42 7^48` | 506 |
| `A6 = PSL(2,9)` | 360 | `1^1 2^45 3^80 4^90 5^144` | 962 |
| `PSL(2,8)` | 504 | `1^1 2^63 3^56 7^216 9^168` | 2480 |
| `PSL(2,11)` | 660 | `1^1 2^55 3^110 5^264 6^110 11^120` | 2752 |
| `PSL(2,13)` | 1092 | `1^1 2^91 3^182 6^182 7^468 13^168` | 5644 |
| `PSL(2,17)` | 2448 | `1^1 2^153 3^272 4^306 8^612 9^816 17^288` | 13262 |
| `A7` | 2520 | `1^1 2^105 3^350 4^630 5^504 6^210 7^720` | 8822 |

### Constructions and checks

The alternating groups were generated as permutation groups by 3-cycles.  For
odd prime `q`, `PSL(2,q)` was generated on the projective line by

```
x -> x+1,                 x -> -1/x.
```

For `PSL(2,8)`, arithmetic in `GF(8)=GF(2)[x]/(x^3+x+1)` was implemented
directly, and translation, inversion, and a primitive-square dilation were
used.  Breadth-first permutation closure produced exactly the asserted group
orders (60, 168, 360, 504, 660, 1092, 2448, and 2520); the program aborts if
any closure has the wrong size.

## 3. Complete order-60 calculation

The standard classification of groups of order 60 can be organized as
follows.  Every nonsimple group in the classification has a normal `C5`; by
Schur--Zassenhaus it is `C5 semidirect K` for a group `K` of order 12.  The five
possibilities for `K` and the numbers of actions into
`Aut(C5) isomorphic to C4`, up to automorphisms of `K`, are

| `K` | action orbits | reason |
|---|---:|---|
| `C12` | 3 | generator image has order 1, 2, or 4 |
| `C6 x C2` | 2 | trivial or the unique nonzero `C2`-character orbit |
| `S3 x C2` (the dihedral group of order 12) | 3 | trivial; sign; central-`C2` (the other nonzero character is equivalent) |
| `A4` | 1 | its abelianization is `C3` |
| `Dic3 = C3 semidirect C4` (inversion action) | 3 | its abelianization is `C4`; image order 1, 2, or 4 |

This gives `3+2+3+1+3=12` nonsimple groups; adjoining `A5` gives all 13.
The program constructs every semidirect product as pairs `(a,k)` with

```
(a,k)(b,l) = (a + chi(k)b, kl),
```

where `a,b` are in `C5` and `chi:K -> {1,2,3,4}=Aut(C5)` is the indicated
action.  Thus this table does not rely on merely recognizing names.

| group | element-order distribution | `T` |
|---|---|---:|
| `C5 x C12 = C60` | `1^1 2^1 3^2 4^2 5^4 6^2 10^4 12^4 15^8 20^8 30^8 60^16` | 510 |
| `C5 : C12`, image `C2` | `1^1 2^1 3^2 4^10 5^4 6^2 10^4 12^20 15^8 30^8` | 270 |
| `C5 : C12`, image `C4` | `1^1 2^5 3^2 4^10 5^4 6^10 12^20 15^8` | 210 |
| `C5 x (C6 x C2) = C30 x C2` | `1^1 2^3 3^2 5^4 6^6 10^12 15^8 30^24` | 340 |
| `C5 : (C6 x C2)`, nonzero `C2`-character | `1^1 2^11 3^2 5^4 6^22 10^4 15^8 30^8` | 220 |
| `C5 x (S3 x C2)` | `1^1 2^7 3^2 5^4 6^2 10^28 15^8 30^8` | 272 |
| `C5 : (S3 x C2)`, sign action | `1^1 2^31 3^2 5^4 6^2 10^4 15^8 30^8` | 200 |
| `C5 : (S3 x C2)`, central-`C2` action | `1^1 2^23 3^2 5^4 6^10 10^12 15^8` | 176 |
| `C5 x A4` | `1^1 2^3 3^8 5^4 10^12 15^32` | 340 |
| `C5 x Dic3` | `1^1 2^1 3^2 4^6 5^4 6^2 10^4 15^8 20^24 30^8` | 374 |
| `C5 : Dic3`, image `C2` | `1^1 2^1 3^2 4^30 5^4 6^2 10^4 15^8 30^8` | 230 |
| `C5 : Dic3`, image `C4` | `1^1 2^5 3^2 4^30 5^4 6^10 15^8` | 170 |
| `A5` | `1^1 2^15 3^20 5^24` | **152** |

All 13 order distributions are distinct.  More importantly here, none of the
12 nonsimple values equals 152.  This proves the order-60 positive result
stated at the beginning.

## 4. Larger-order family search

At each target order `N`, I searched all of the following:

1. Every abelian isomorphism type of order `N` (generated from partitions of
   the prime-power exponents).
2. `Dih(A)=A semidirect C2` by inversion for every abelian `A` of order `N/2`.
3. Every split metacyclic presentation `C_n semidirect_r C_m`, for every
   factorization `nm=N` and every unit `r mod n` satisfying `r^m=1`.
4. Every `(C_p)^k semidirect_A C_m` with `p^k m=N` and `2 <= k <= 4`, for
   **every** invertible `k x k` matrix over `F_p` satisfying `A^m=I`.
5. Direct products of two named factors whose orders multiply to `N`.  The
   factor pool contains every abelian type at a divisor order, cyclic,
   dihedral, and dicyclic groups, `A4,...,A7`, and `S3,...,S5`.  Identity
   factors were excluded so that the target simple group was not counted as a
   tautological hit.

Different actions or named products can be isomorphic or can at least have the
same order distribution.  I did **not** claim the raw constructions are
pairwise nonisomorphic.  The `distinct profiles` column is the size of the
union after deduplicating complete element-order distributions.  `entries` is
the number after action profiles, but not named direct products, have been
deduplicated.  The two raw-action columns show how many actions were actually
examined before profile deduplication.

| target | `T` | abelian | gen. dihedral | raw `C_n:C_m` actions / profiles | raw matrix actions / profiles | named direct products | entries | distinct profiles | hit? |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `PSL(2,7)`, 168 | 506 | 3 | 2 | 58 / 22 | 111 / 4 | 95 | 126 | 36 | no |
| `A6`, 360 | 962 | 6 | 4 | 86 / 38 | 95 / 8 | 191 | 247 | 71 | no |
| `PSL(2,8)`, 504 | 2480 | 6 | 4 | 118 / 52 | 143 / 9 | 185 | 256 | 83 | no |
| `PSL(2,11)`, 660 | 2752 | 2 | 1 | 136 / 28 | 3 / 2 | 106 | 139 | 33 | no |
| `PSL(2,13)`, 1092 | 5644 | 2 | 1 | 208 / 50 | 3 / 2 | 104 | 159 | 54 | no |
| `PSL(2,17)`, 2448 | 13262 | 10 | 6 | 246 / 70 | 1349 / 11 | 330 | 427 | 140 | no |
| `A7`, 2520 | 8822 | 6 | 4 | 452 / 136 | 143 / 9 | 400 | 555 | 196 | no |

The nearest tested values around each target were:

| order | target | nearest tested below | nearest tested above |
|---:|---:|---:|---:|
| 168 | 506 | none (every tested value was larger) | 530 |
| 360 | 962 | none | 1136 |
| 504 | 2480 | 2394 | 2636 |
| 660 | 2752 | none | 3892 |
| 1092 | 5644 | none | 8394 |
| 2448 | 13262 | none | 19788 |
| 2520 | 8822 | none | 16036 |

The nearest examples are printed by the script.  In particular, `PSL(2,8)`
is the only target for which this family sweep straddled the simple group's
value; this is consistent with its many elements of orders 7 and 9 making its
`T/|G|` atypically large among the rows.

## 5. Structural observations

1. If `n_d(G)` is the number of elements of order `d`, then `T` is the one
   linear statistic `sum_d n_d phi(d)`.  Hence equal **full order
   distributions** imply equal `T`, but the converse is much weaker.  A bare
   order spectrum interpreted only as the set of occurring orders does not by
   itself determine `T`; multiplicities matter.  I did not use an unverified
   literature pair from memory.

2. Let `i(G)` be the number of involutions.  In the cyclic-subgroup formula,
   the identity contributes 1, every order-2 subgroup contributes 1, and
   `phi(d)^2` is divisible by 4 for every `d>2`.  Therefore

   ```
   T(G) = 1 + i(G) (mod 4).
   ```

   Any putative mate `H` must in particular have its involution count
   congruent modulo 4 to that of the simple group.

3. Since `phi(d)>=1`, always `T(G)>=|G|`.  Equality holds exactly when every
   element has order at most 2, i.e. for elementary abelian 2-groups (including
   the trivial boundary case).  This bound is far too weak to settle the
   problem, but it explains why groups with many high-order elements tend to
   lie well above several of the simple targets.

4. For direct products, if the factor distributions are `a_r` and `b_s`, the
   product distribution is

   ```
   n_d(G x K) = sum_(lcm(r,s)=d) a_r b_s.
   ```

   This was used directly; no element list of a large direct product was
   needed.

## 6. Exact limitations

Only order 60 was exhaustively classified.  At orders 168, 360, 504, 660,
1092, 2448, and 2520, the program did **not** enumerate all finite groups.
Missing possibilities include arbitrary nonsplit extensions, semidirect
products with noncyclic complements outside the named direct-product pool,
many groups whose normal subgroup is nonabelian, and many groups built from
unlisted factor groups.  Profile deduplication also does not amount to
isomorphism testing.

Thus the honest conclusion is:

* the answer is positive for the first simple order 60;
* no counterexample occurs in the explicitly quantified families above at the
  next seven tested simple-group orders;
* these computations do not decide Kourovka 19.25 in general.

## 7. Reproduction and internal audits

Run from the project root:

```bash
.venv/bin/python problems/recon/kourovka1925_search.py
```

The script uses only the Python standard library.  It includes independent
brute-force checks of the closed element-order formulas for both
`C_n:C_m` and `(C_p)^k:C_m` on small examples, exact permutation-closure size
assertions, group-size assertions for all order-60 constructions, and the
`phi(d) | n_d` checks described above.  A successful run starts with
`SELF-CHECKS PASSED` and then prints every table entry and all family counts.
