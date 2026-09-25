#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/../../.." && pwd)
proofenv="$repo_root/lean/proofenv"

(
  cd "$proofenv"
  "$HOME/.elan/bin/lake" env lean K1695/TranspositionLemma.lean
) >"$script_dir/transposition_rebuild.log" 2>&1

(
  cd "$proofenv"
  "$HOME/.elan/bin/lake" env lean K1695/TranspositionLemmaFull.lean
) >"$script_dir/full_rebuild.log" 2>&1

(
  cd "$proofenv"
  "$HOME/.elan/bin/lake" env lean "$script_dir/FidelityScratch.lean"
) >"$script_dir/axioms_and_examples.log" 2>&1

printf '%s\n' 'PASS: both source rebuilds and the fidelity scratch audit completed'
