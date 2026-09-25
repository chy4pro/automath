CALIBRATION
K2  residue=1 expected=1 OK
C3  residue=1 expected=1 OK
C4  residue=2 expected=2 OK
C5  residue=2 expected=2 OK
C6  residue=2 expected=2 OK
C7  residue=3 expected=3 OK
C8  residue=3 expected=3 OK
C9  residue=3 expected=3 OK

SEARCH BOX
Every unlabeled graph on 2..7 vertices, connected or disconnected (graph atlas).
Random G(n,p): n=8..10, p=0.18,0.35,0.55,0.78, 18 fixed seeds per (n,p).
Extra cycles C3..C9 and cliques K2..K7.
For every graph: every maximum independent set A.
For every reductio trajectory: canonical tie order plus five fresh seeded random tie orders.

COUNTS
graphs=1480 connected=1159 maximum_independent_sets=4627
reductio_graphs=849 reductio_A=3447 trajectories=20682
hard_core_frame_graphs=8 frame_A=9 hard_core_graphs=0
MB_degree_count_instances=9 MB_degree_count_slack_zero=9

SLACK COUNTS (selected)
L=0: slack 0 (648)
L=1: slack 1 (1068)
L=2: slack 1 (192), 2 (1572), 3 (672)
L=3: minimum slack 2
L=4: minimum slack 2
L=5: minimum slack 3

BOUNDARIES HIT
L=0,1,2,tau; p=0; tau=2,3,4; nu=0,1; i0=1 (tau=1) and i0=tau;
Delta=tau and Delta=tau+1; B_lo_plus empty and nonempty.
Disconnected controls: 2K2 has residue 2 and heads [1,1]; E4 has residue 4 and no heads.
Nongraphical controls under splitAt/Nat truncation:
  [3,3,1] -> residue 1, heads [3,2]
  [5,1] -> residue 1, heads [5]
  [4,4,1,0] -> residue 2, heads [4,3]

CONTROL INSTANCES
Reductio-only C5: E=[01,04,12,23,34], alpha=residue=2, diameter=2, f=4;
all five maximum independent sets tested.
Hard-core-frame control: E=[02,13,24,25,34,35], A={0,1,4,5},
connected, nonforest, diameter=4, alpha=4, f=5, residue=3; F-b pair ({2},{3}).

FAILURES=0
