# ETP677 Lean certificates

This standalone Lean 4 project embeds and checks the four finite branch objects from
`problems/etp677`. It uses only Lean's bundled `Std` library and the pinned
`leanprover/lean4:v4.27.0` toolchain.

Build from this directory with:

```sh
~/.elan/bin/lake build
```

`ETP677Certs/Core.lean` defines the finite predicates, left division, `Xi`, `E`, `N`,
`delta`, perfect rows, and the combined certificate proposition. Each object module embeds
its source JSON as Lean list literals and proves its certificate using `native_decide`.
`ETP677Certs/NegativeControl.lean` proves that swapping the first two cells of the first
q=3 table row invalidates the same certificate claim.

The checked-in literal modules can be reproduced from the source JSON files with
`python3 generate_objects.py`.
