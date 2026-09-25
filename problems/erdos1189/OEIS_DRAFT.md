# OEIS submission draft — irreducible covering sets (Erdős Problem #1189)  [status: k<=8 complete; k<=7 double-verified (SAT+DFS), k=8 DFS with SAT cross-check]

Definition. A finite set of integers 1 < n_1 < ... < n_k is a COVERING SET if residues a_i can be chosen so that
every integer satisfies at least one congruence x ≡ a_i (mod n_i). It is IRREDUCIBLE if no proper subset is a
covering set. (Erdős 1980; erdosproblems.com/1189. Distinct from "minimal covering system": the set of moduli of a
minimal covering system is irreducible only if no proper subset can be re-covered with OTHER residues.)

## Sequence 1: I(k) = number of irreducible covering sets of size k
k: 1 2 3 4 5 6 7 [8]
a: 0 0 0 0 1 4 15 65
Offset 1. Comments: I(5)=1 is {2,3,4,6,12}. Simpson (1985) proved n_k <= 2^(k-1) for irreducible covering sets, which
makes each I(k) a finite computation. Lemma used for pruning (proved in erdos1189_notes.md): in an irreducible
covering set, every prime power p^e exactly dividing a modulus divides some other modulus.
Method: exhaustive enumeration of all k-sets with Σ1/n_i > 1 and n_k <= 2^(k-1) (necessary), pruned by the lemma,
coverability decided by SAT (CaDiCaL via python-sat): variables = residue choices, clauses = every residue class
mod lcm hit; irreducibility = coverability fails for all k subsets of size k-1. Program and data with witnesses: https://github.com/chy4pro/erdos-1189-irreducible-covering-sets

## Sequence 2: min n_k over irreducible covering sets of size k   (k>=5): 12 24 36 36
## Sequence 3: max n_k over irreducible covering sets of size k   (k>=5): 12 24 48 96   (Simpson bound 2^(k-1) = 16, 32, 64, 128)
## Sequence 4: max Σ 1/n_i (as a fraction) over irreducible covering sets of size k (k>=5): 1.333333 1.416667 1.458333
## Sequence 5: min lcm, max lcm of irreducible covering sets of size k (k>=5): 12/12 24/24 36/48

## Full lists (k<=7)
k=5: [2, 3, 4, 6, 12]
k=6: [2, 4, 6, 8, 12, 24]; [2, 3, 4, 6, 8, 24]; [2, 3, 4, 8, 12, 24]; [2, 3, 6, 8, 12, 24]
k=7: [2, 4, 6, 8, 12, 16, 48]; [2, 4, 6, 8, 16, 24, 48]; [2, 4, 6, 9, 12, 18, 36]; [2, 4, 6, 12, 16, 24, 48]; [2, 4, 8, 12, 16, 24, 48]; [2, 3, 4, 6, 8, 16, 48]; [2, 3, 4, 6, 9, 18, 36]; [2, 3, 4, 6, 16, 24, 48]; [2, 3, 4, 8, 12, 16, 48]; [2, 3, 4, 8, 16, 24, 48]; [2, 3, 4, 9, 12, 18, 36]; [2, 3, 4, 12, 16, 24, 48]; [2, 3, 6, 8, 12, 16, 48]; [2, 3, 6, 9, 12, 18, 36]; [2, 3, 6, 12, 16, 24, 48]

## Cross-check needed before submission
- Independent re-verification of every listed set (a second, non-SAT coverability checker) and of the lemma.
- Literature: Krukenberg (1971 thesis) enumerated covering systems with small lcm; Simpson 1985; Sun 2007; BBMST 2024
  asymptotics for minimal covering systems. Confirm no prior table of I(k).

## k=8 (complete): I(8) = 65; min n_k = 36; max n_k = 96; max Σ1/n = 1.555556; lcm range 72..96
[2, 3, 4, 12, 16, 24, 32, 96]
[2, 3, 4, 12, 18, 24, 36, 72]
[2, 3, 4, 12, 24, 32, 48, 96]
[2, 3, 4, 6, 16, 24, 32, 96]
[2, 3, 4, 6, 18, 24, 36, 72]
[2, 3, 4, 6, 24, 32, 48, 96]
[2, 3, 4, 6, 8, 16, 32, 96]
[2, 3, 4, 6, 8, 18, 36, 72]
[2, 3, 4, 6, 8, 32, 48, 96]
[2, 3, 4, 6, 8, 9, 18, 72]
[2, 3, 4, 6, 8, 9, 36, 72]
[2, 3, 4, 6, 9, 18, 24, 72]
[2, 3, 4, 6, 9, 24, 36, 72]
[2, 3, 4, 8, 12, 16, 32, 96]
[2, 3, 4, 8, 12, 18, 36, 72]
[2, 3, 4, 8, 12, 32, 48, 96]
[2, 3, 4, 8, 16, 24, 32, 96]
[2, 3, 4, 8, 16, 32, 48, 96]
[2, 3, 4, 8, 18, 24, 36, 72]
[2, 3, 4, 8, 24, 32, 48, 96]
[2, 3, 4, 8, 9, 12, 18, 72]
[2, 3, 4, 8, 9, 12, 36, 72]
[2, 3, 4, 8, 9, 18, 24, 36]
[2, 3, 4, 8, 9, 18, 24, 72]
[2, 3, 4, 8, 9, 24, 36, 72]
[2, 3, 4, 9, 12, 18, 24, 72]
[2, 3, 4, 9, 12, 24, 36, 72]
[2, 3, 6, 12, 16, 24, 32, 96]
[2, 3, 6, 12, 18, 24, 36, 72]
[2, 3, 6, 12, 24, 32, 48, 96]
[2, 3, 6, 8, 12, 16, 32, 96]
[2, 3, 6, 8, 12, 18, 36, 72]
[2, 3, 6, 8, 12, 32, 48, 96]
[2, 3, 6, 8, 9, 12, 18, 72]
[2, 3, 6, 8, 9, 12, 36, 72]
[2, 3, 6, 8, 9, 18, 24, 36]
[2, 3, 6, 8, 9, 18, 36, 72]
[2, 3, 6, 9, 12, 18, 24, 72]
[2, 3, 6, 9, 12, 24, 36, 72]
[2, 3, 6, 9, 18, 24, 36, 72]
[2, 4, 6, 12, 16, 24, 32, 96]
[2, 4, 6, 12, 18, 24, 36, 72]
[2, 4, 6, 12, 24, 32, 48, 96]
[2, 4, 6, 8, 12, 16, 32, 96]
[2, 4, 6, 8, 12, 18, 36, 72]
[2, 4, 6, 8, 12, 32, 48, 96]
[2, 4, 6, 8, 16, 24, 32, 96]
[2, 4, 6, 8, 16, 32, 48, 96]
[2, 4, 6, 8, 18, 24, 36, 72]
[2, 4, 6, 8, 24, 32, 48, 96]
[2, 4, 6, 8, 9, 12, 18, 72]
[2, 4, 6, 8, 9, 12, 36, 72]
[2, 4, 6, 8, 9, 18, 24, 36]
[2, 4, 6, 8, 9, 18, 24, 72]
[2, 4, 6, 8, 9, 24, 36, 72]
[2, 4, 6, 9, 12, 18, 24, 72]
[2, 4, 6, 9, 12, 24, 36, 72]
[2, 4, 8, 12, 16, 24, 32, 96]
[2, 4, 8, 12, 16, 32, 48, 96]
[2, 4, 8, 12, 18, 24, 36, 72]
[2, 4, 8, 12, 24, 32, 48, 96]
[2, 4, 8, 16, 24, 32, 48, 96]
[2, 4, 8, 9, 12, 18, 24, 36]
[2, 4, 8, 9, 12, 18, 24, 72]
[2, 4, 8, 9, 12, 24, 36, 72]
