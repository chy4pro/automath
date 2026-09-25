CLEAN: All four named joints pass under the stated assumptions and I found no step that is wrong or unrepairable.

| Joint | Verdict | One-line check |
|---|---|---|
| J1 | OK | For each of the four `G[B]` isomorphism types, the listed `F-b` options are exactly the disjoint nonempty pairs of occurring types with no `G[B]` edge; the `C2`/`C3` deductions use the same pair list and account for occurring/occurrence and singleton constraints consistently. |
| J2 | OK | In `k=3` and `k=2` traces, the inequalities on `D_3`, the decremented-step counts, and the resulting contradictions are consistent with the stated formulas (`D_3 = Z+1-e_B` and the explicit `L^1/L^2` bounds) and no admissible tie-ordering in the relevant hard-core subcases changes the required head-value relations. |
| J3 | OK | `Lemma U` is correct as written (`max(R)≤3` and `Δ ≥ #(R=3)` ⇒ all 3’s are removed on step 1, so `D_2,D_3≤2`, hence `Σ_{i≤3}D_i≤Δ+4`); each application in `k≤1` has `Δ = X`, `max(R)≤3`, and the needed `count(3) ≤ X` conditions are explicitly met in the branch calculations. |
| J4 | OK | `k=2` algebra is coherent: `m = Σ_B deg_B - e_B` with the stated `e_B` values, the explicit HH steps in `e_B=2` match the derived parameterized form, and boundary cases (`a₀-1=0`, `b₀+c₀-1=0`) are numerically handled. |
| J5 | OK | The split `k=0,1,2,3` is exhaustive (`k = #{b∈B:deg(b)≥4} ∈ {0,1,2,3}`), and the proof works inside the contradiction hypothesis `f=α+1` and `residue=α` throughout; no lemma is used outside its stated hypotheses. |

### Control-case check

- `CTRL-1` (**FALSE**): The proof explicitly avoids the false global inequality and does not derive `D_i ≤ d_i-(i−1)`; it uses the localized Lemma `H`, which is compatible with the false example.
- `CTRL-2` (**FALSE**): No argument in these claims proves a general `f(G) ≥ α(G)+ceil(d/3)` from the τ=3 hard-core hypotheses; the structure only addresses `f=α+1`/`residue=α` contradictions.
- `CTRL-3` (**FALSE**): The proof does not derive `α+1 ≥ residue+ceil(d/3)` in general; it does not establish the witness-refuted relation from the local mechanism.
- `CTRL-4` (**TIGHT**, not false): In the tight sequence `[3,3,3,3,3,2,1]` (`μ=(0,0,1,1,0,0,2)`), `m=9` and `D=(3,3,2)` in the subcase `k=0`, giving `m- (D_1+D_2+D_3)=1`; this matches the requested tight slack and is not contradicted into `≥2`.

### Concrete τ=3 case-check example

Use the `e_B=2` family example with types
`μ=(1,0,1,0,0,1,1)` on `B={0,1,2}` (`0-1-2` is the path):
- `A` types: `μ({0})=1`, `μ({2})=1`, `μ({0,2})=1`, `μ({0,1,2})=1`.
- One edge set realization:
  `E={ (0,1),(1,2),(3,0),(4,2),(5,0),(5,2),(6,0),(6,1),(6,2) }`.
- It has `n=7`, `α=4`, `τ=3`, `diam=4`, every `G-v` cyclic (so `f=α+1`), and residues/HH:
  degree sequence `[4,4,3,3,2,1,1]`, HH heads `[4,3,1,1]` (residue `3=α-1`).
- Case classification: `k=2`, `e_B=2`.
- Proof branch checks numerically:
  `L¹ = [3,2,2,1,1,1]`, `L²=[1,1,1,1,0]`, so `D_3=1` with four ones in `L²`, matching the explicit subcase contradiction mechanism.

### What I could not check

I did not brute-force all possible multiplicity tuples with large bounds; I checked the full task-required draft ranges available in the repository scripts (`MAX=5` family/parameter outputs) and used direct HH calculations for the required representative branches. I did not find missing or incorrect links in this scope. 
