/* A391118 (Erdős #693, k=2): a(n) = max gap between consecutive elements of
   B_n = { b in [n, n^2] : b has a divisor d with n < d < 2n }.
   Method: mark multiples of every d in (n,2n) inside [n, n^2] with a bitmap, then scan gaps.
   Also reports where the maximal gap starts (first b_i with b_{i+1}-b_i = a(n)).
   Usage: ./a391118 NMAX [NMIN]   (prints "n a(n) gap_start" per line). Memory: n^2/8 bytes. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
int main(int argc, char **argv) {
    long nmax = argc > 1 ? atol(argv[1]) : 100, nmin = argc > 2 ? atol(argv[2]) : 1;
    long N2 = nmax * nmax;
    uint8_t *bm = calloc(N2 / 8 + 2, 1);
    if (!bm) { fprintf(stderr, "alloc failed\n"); return 1; }
    for (long n = nmin; n <= nmax; n++) {
        long lo = n, hi = n * n;
        memset(bm, 0, hi / 8 + 2);
        for (long d = n + 1; d < 2 * n; d++)
            for (long m = ((lo + d - 1) / d) * d; m <= hi; m += d) bm[m >> 3] |= 1 << (m & 7);
        long prev = -1, best = 0, bstart = -1;
        for (long b = lo; b <= hi; b++) if (bm[b >> 3] & (1 << (b & 7))) {
            if (prev >= 0 && b - prev > best) { best = b - prev; bstart = prev; }
            prev = b;
        }
        printf("%ld %ld %ld\n", n, best, bstart);
        fflush(stdout);
    }
    return 0;
}
