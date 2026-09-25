# ETP677 extension reduction

This Lean 4 project formalizes the L1--L6 interpretation chain used by the pair-indexed
extension search for the finite implication E677 to E255.

The project uses the repository's existing Mathlib checkout through a local path dependency;
no network access is needed. Build it with:

```sh
~/.elan/bin/lake build
```

`Ext677.lean` contains all definitions, supporting lemmas, the six requested named theorems,
and `#print axioms` commands. Their captured output is in `AXIOMS.txt`.
