import Std.Tactic

namespace ETP677Certs

/-- A finite candidate object. Its point count is derived from `q`, rather than trusted data. -/
structure Object where
  q : Nat
  table : List (List Nat)
  lines : List (List Nat)
  nu : List Nat
  deriving Repr

def Object.n (o : Object) : Nat := o.q * o.q + o.q + 1

private def allN (n : Nat) (p : Nat → Bool) : Bool :=
  (List.range n).all p

private def countN (n : Nat) (p : Nat → Bool) : Nat :=
  (List.range n).foldl (fun total x => if p x then total + 1 else total) 0

private def valueAt (xs : List Nat) (i : Nat) : Nat := xs.getD i 0

private def rowAt (o : Object) (r : Nat) : List Nat := o.table.getD r []

private def lineAt (o : Object) (c : Nat) : List Nat := o.lines.getD c []

/-- The table as the requested total map on `Fin n`. Malformed literals are rejected by
`dimensionsB`; defaults here only make every definition total and executable. -/
def T (o : Object) (a w : Fin o.n) : Fin o.n :=
  ⟨valueAt (rowAt o a.val) w.val % o.n, Nat.mod_lt _ (by simp [Object.n])⟩

private def natToFin (o : Object) (x : Nat) : Fin o.n :=
  ⟨x % o.n, Nat.mod_lt _ (by simp [Object.n])⟩

private def uniqueB (xs : List Nat) : Bool :=
  xs.eraseDups.length == xs.length

/-- Checks literal dimensions, bounds, and the declared projective-plane line sizes. -/
def dimensionsB (o : Object) : Bool :=
  o.table.length == o.n &&
  o.table.all (fun row => row.length == o.n && row.all (· < o.n)) &&
  o.lines.length == o.n &&
  o.lines.all (fun line =>
    line.length == o.q + 1 && line.all (· < o.n) && uniqueB line) &&
  o.nu.length == o.n && o.nu.all (· < o.n)

/-- (B1): every row is a permutation of `Fin n`. -/
def b1B (o : Object) : Bool :=
  allN o.n fun r =>
    allN o.n fun v => countN o.n (fun w => valueAt (rowAt o r) w == v) == 1

/-- (B2): column `c` has its repeated value exactly on `lines[c]`, all other values
occur at most once, and exactly `q` values are absent. -/
def b2B (o : Object) : Bool :=
  allN o.n fun c =>
    let special := valueAt o.nu c
    let line := lineAt o c
    let occurs (v : Nat) := countN o.n fun r => valueAt (rowAt o r) c == v
    occurs special == o.q + 1 &&
    allN o.n (fun r => (valueAt (rowAt o r) c == special) == line.contains r) &&
    allN o.n (fun v => v == special || occurs v ≤ 1) &&
    countN o.n (fun v => occurs v == 0) == o.q

/-- (B3): every distinct pair of points is on exactly one declared line. -/
def b3B (o : Object) : Bool :=
  allN o.n fun x =>
    allN o.n fun y =>
      x == y || countN o.n (fun c =>
        (lineAt o c).contains x && (lineAt o c).contains y) == 1

/-- (B4): `nu` is a bijection of `Fin n`. -/
def b4B (o : Object) : Bool :=
  allN o.n fun v => countN o.n (fun c => valueAt o.nu c == v) == 1

def branchObjectB (o : Object) : Bool :=
  dimensionsB o && b1B o && b2B o && b3B o && b4B o

private def firstWhere : List Nat → (Nat → Bool) → Nat
  | [], _ => 0
  | x :: xs, p => if p x then x else firstWhere xs p

/-- Left division: the unique `w` with `T a w = v` on a branch object. -/
def ldiv (o : Object) (a v : Fin o.n) : Fin o.n :=
  let w := firstWhere (List.range o.n) fun i => valueAt (rowAt o a.val) i == v.val
  ⟨w % o.n, Nat.mod_lt _ (by simp [Object.n])⟩

def Xi (o : Object) (t x : Fin o.n) : Fin o.n :=
  ldiv o x (ldiv o t x)

/-- `E t v = #{x | Xi t x = v}`. -/
def E (o : Object) (t v : Fin o.n) : Nat :=
  countN o.n fun x => (Xi o t (natToFin o x)).val == v.val

/-- `N t v = #{a | T a t = v}`. -/
def N (o : Object) (t v : Fin o.n) : Nat :=
  countN o.n fun a => (T o (natToFin o a) t).val == v.val

/-- `delta v = (sum_t E t v) - n`, represented in `Int` to retain negative values. -/
def delta (o : Object) (v : Fin o.n) : Int :=
  Int.ofNat ((List.range o.n).foldl
    (fun total t => total + E o (natToFin o t) v) 0) - Int.ofNat o.n

def perfectB (o : Object) (r : Nat) : Bool :=
  r < o.n && allN o.n (fun v =>
    E o (natToFin o r) (natToFin o v) == N o (natToFin o r) (natToFin o v))

def deltaZeroB (o : Object) : Bool :=
  allN o.n fun v => delta o (natToFin o v) == 0

def BranchObject (o : Object) : Prop := branchObjectB o = true

def Perfect (o : Object) (r : Nat) : Prop := perfectB o r = true

def DeltaZero (o : Object) : Prop := deltaZeroB o = true

def PerfectRows (o : Object) (rows : List Nat) : Prop :=
  rows.all (perfectB o) = true

/-- The exact conjunction certified by each object theorem. -/
def Certificate (o : Object) (rows : List Nat) : Prop :=
  BranchObject o ∧ PerfectRows o rows ∧ DeltaZero o

/-- Swap the first two cells of the first row: a genuine two-cell perturbation. -/
def swapFirstTwoCells (o : Object) : Object :=
  let changedTable := match o.table with
    | (x :: y :: tail) :: rows => (y :: x :: tail) :: rows
    | table => table
  { o with table := changedTable }

end ETP677Certs
