// Adversarial (simulated-annealing) search for counterexamples to WOWII 133 in the
// C4-free branch:  minimise  slack = path(G) - rad(G) - floor(l(G))  over connected
// C4-free graphs on n vertices.   usage: ./sa133 n seed iters
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXV 32
static int NV;
static inline int pc(unsigned x) { return __builtin_popcount(x); }

static int connectedG(int *adj, int n) {
  int seen = 1, fr = 1;
  while (fr) {
    int nf = 0;
    for (int v = 0; v < n; v++) if (fr >> v & 1) nf |= adj[v];
    nf &= ~seen; seen |= nf; fr = nf;
  }
  return seen == (1 << n) - 1;
}
static int hasC4(int *adj, int n) {
  for (int u = 0; u < n; u++)
    for (int v = u + 1; v < n; v++)
      if (pc(adj[u] & adj[v]) >= 2) return 1;
  return 0;
}
static int radiusG(int *adj, int n) {
  int best = 1000;
  for (int s = 0; s < n; s++) {
    int seen = 1 << s, fr = 1 << s, d = 0;
    while (1) {
      int nf = 0;
      for (int v = 0; v < n; v++) if (fr >> v & 1) nf |= adj[v];
      nf &= ~seen; if (!nf) break;
      seen |= nf; fr = nf; d++;
    }
    if (d < best) best = d;
  }
  return best;
}
static int alpha_rec(int *adj, int mask) {
  if (!mask) return 0;
  int v = -1, bd = -1;
  for (int u = 0; u < NV; u++)
    if (mask >> u & 1) { int dg = pc(adj[u] & mask); if (dg > bd) { bd = dg; v = u; } }
  if (bd == 0) return pc(mask);
  int a = alpha_rec(adj, mask & ~(1 << v));
  int b = 1 + alpha_rec(adj, mask & ~((1 << v) | adj[v]));
  return a > b ? a : b;
}
static int bestpath;
static void dfsp(int *adj, int last, int pmask, int forbid, int len, int full) {
  if (len > bestpath) bestpath = len;
  int avail = full & ~pmask & ~forbid;
  if (len + pc(avail) <= bestpath) return;
  int cands = adj[last] & avail, nf = forbid | adj[last];
  while (cands) {
    int w = cands & -cands; cands ^= w;
    dfsp(adj, __builtin_ctz(w), pmask | w, nf, len + 1, full);
  }
}
static int pathnum(int *adj, int n) {
  bestpath = 0;
  int full = (1 << n) - 1;
  for (int s = 0; s < n; s++) dfsp(adj, s, 1 << s, 0, 1, full);
  return bestpath;
}
/* real-valued slack times n:  n*(path-rad) - sum_v alpha(N(v))   (A7 quantity) */
static int rslack(int *adj, int n, int *pp, int *pr, int *pS) {
  NV = n;
  int r = radiusG(adj, n);
  long S = 0;
  for (int v = 0; v < n; v++) S += alpha_rec(adj, adj[v]);
  int p = pathnum(adj, n);
  if (pp) { *pp = p; *pr = r; *pS = (int)S; }
  return n * (p - r) - (int)S;
}
static int slack(int *adj, int n, int *pp, int *pr, int *pf) {
  NV = n;
  int r = radiusG(adj, n);
  long S = 0;
  for (int v = 0; v < n; v++) S += alpha_rec(adj, adj[v]);
  int fl = (int)(S / n);
  int p = pathnum(adj, n);
  if (pp) { *pp = p; *pr = r; *pf = fl; }
  return p - r - fl;
}

static unsigned long long rs;
static unsigned rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (unsigned)(rs >> 11); }

int main(int argc, char **argv) {
  int n = argc > 1 ? atoi(argv[1]) : 14;
  rs = (argc > 2 ? atoll(argv[2]) : 1) * 2862933555777941757ULL + 3037000493ULL;
  long iters = argc > 3 ? atoll(argv[3]) : 200000;
  int adj[MAXV];
  /* start from a cycle (connected, C4-free for n>=5) */
  memset(adj, 0, sizeof(adj));
  for (int i = 0; i < n; i++) { int j = (i + 1) % n; adj[i] |= 1 << j; adj[j] |= 1 << i; }
  int cur = rslack(adj, n, 0, 0, 0);
  int best = cur, bestadj[MAXV];
  memcpy(bestadj, adj, sizeof(adj));
  double T = 1.2;
  for (long it = 0; it < iters; it++) {
    T = (1.2 * (1.0 - (double)it / iters) + 0.02) * n;
    int u = rnd() % n, v = rnd() % n;
    if (u == v) continue;
    int trial[MAXV];
    memcpy(trial, adj, sizeof(trial));
    trial[u] ^= 1 << v; trial[v] ^= 1 << u;
    if (hasC4(trial, n)) continue;
    if (!connectedG(trial, n)) continue;
    int s = rslack(trial, n, 0, 0, 0);
    if (s <= cur || (double)rnd() / 2097152.0 < 4.0 * __builtin_exp(-(s - cur) / T)) {
      memcpy(adj, trial, sizeof(adj));
      cur = s;
      if (s < best) {
        best = s; memcpy(bestadj, adj, sizeof(adj));
        {
          int p, r, f;
          int isl = slack(adj, n, &p, &r, &f);
          if (isl >= 0 && s >= 0) goto cont;
          printf("!!! %s n=%d path=%d rad=%d floorl=%d rslack=%d  E=[",
                 isl < 0 ? "COUNTEREXAMPLE(133)" : "A7-VIOLATION", n, p, r, f, s);
          for (int a = 0; a < n; a++) for (int b = a + 1; b < n; b++) if (adj[a] >> b & 1) printf("(%d,%d)", a, b);
          printf("]\n");
          if (isl < 0) return 1;
        }
        cont: ;
      }
    }
  }
  int p, r, f;
  int isl = slack(bestadj, n, &p, &r, &f);
  printf("n=%2d done: min n*rslack=%d intslack=%d (path=%d rad=%d floor(l)=%d)  E=[", n, best, p, r, f);
  for (int a = 0; a < n; a++) for (int b = a + 1; b < n; b++) if (bestadj[a] >> b & 1) printf("(%d,%d)", a, b);
  printf("]\n");
  (void)best;
  return 0;
}
