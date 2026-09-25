/* ROUND 3-C (line k1695, 2026-08-24): refutation frontier for Kourovka 16.95.
 *
 * Question: is there an invertible A over a small field with NO permutation matrix P
 * making AP cyclic?  Such an A refutes a 20-year-old Kourovka problem and is verifiable
 * in seconds by anyone.  P-K1 (selection probe) and round3_census.py closed
 * GL(2,q) q<=9, GL(3,q) q<=5, GL(4,2).  This program is the next shell out, in C
 * because the Python scan dies there: GL(4,3), GL(5,2), GL(3,7), GL(3,8), GL(3,9).
 *
 * It also records the two structural hypotheses the census introduced:
 *   H1  some P with at most 2 cycles works        (0 violations so far)
 *   H2  some P of type (n) or (n-1,1) works       (FALSE: 6 matrices in GL(4,2))
 *
 * CONTROLS (asserted; any failure aborts before a single census row is emitted):
 *   NEG-1  identity I judged NOT cyclic (n>=2)
 *   NEG-2  scalar 2I judged NOT cyclic (q>2)
 *   POS-1  companion matrix of x^n-1 judged cyclic
 *   POS-2  enumerated |GL(n,q)| equals prod_i (q^n - q^i)
 *   KAT    over GF(2), A=J-I: n=6 has NO good n-cycle but a good (5,1); n=4 has a good
 *          n-cycle.  (Reproduces k1695_state.md R8, computed by different code.)
 * Exact table arithmetic only; no floating point.  Per-cell wall cap.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <assert.h>

typedef unsigned char u8;
static int Q, P_CHAR, KEXT;
static u8 ADD[16][16], MUL[16][16], NEGT[16], INVT[16];

static void build_field(int q){
    int p=2,k=0,t; Q=q;
    while(p*p<=q && q%p) p++;
    if(q%p) p=q;
    t=q; while(t%p==0){t/=p;k++;}
    if(t!=1){fprintf(stderr,"q=%d not a prime power\n",q);exit(1);}
    P_CHAR=p; KEXT=k;
    if(k==1){
        for(int a=0;a<q;a++)for(int b=0;b<q;b++){ADD[a][b]=(a+b)%p;MUL[a][b]=(a*b)%p;}
    } else {
        /* irreducible monic polys, low->high */
        int f[5]={0}; 
        if(p==2&&k==2){f[0]=1;f[1]=1;f[2]=1;}
        else if(p==2&&k==3){f[0]=1;f[1]=1;f[2]=0;f[3]=1;}
        else if(p==3&&k==2){f[0]=1;f[1]=0;f[2]=1;}
        else {fprintf(stderr,"no irreducible for %d^%d\n",p,k);exit(1);}
        for(int a=0;a<q;a++)for(int b=0;b<q;b++){
            int da[5],db[5],c[9]={0},x=a,y=b,v=0;
            for(int i=0;i<k;i++){da[i]=x%p;x/=p;}
            for(int i=0;i<k;i++){db[i]=y%p;y/=p;}
            for(int i=0;i<k;i++)for(int j=0;j<k;j++)c[i+j]=(c[i+j]+da[i]*db[j])%p;
            for(int i=2*k-2;i>=k;i--) if(c[i]){int co=c[i];c[i]=0;
                for(int j=0;j<k;j++) c[i-k+j]=((c[i-k+j]-co*f[j])%p+p)%p;}
            for(int i=k-1;i>=0;i--) v=v*p+c[i];
            MUL[a][b]=(u8)v;
            v=0; for(int i=k-1;i>=0;i--) v=v*p+((da[i]+db[i])%p);
            ADD[a][b]=(u8)v;
        }
    }
    for(int a=0;a<q;a++){for(int b=0;b<q;b++) if(ADD[a][b]==0){NEGT[a]=b;break;}}
    INVT[0]=0;
    for(int a=1;a<q;a++){for(int b=1;b<q;b++) if(MUL[a][b]==1){INVT[a]=b;break;}}
    for(int a=0;a<q;a++){ if(ADD[a][0]!=a||MUL[a][1]!=a){fprintf(stderr,"field axioms\n");exit(1);} }
    for(int a=1;a<q;a++) if(MUL[a][INVT[a]]!=1){fprintf(stderr,"inv table\n");exit(1);}
}

static int N;
static void matmul(const u8*A,const u8*B,u8*C){
    memset(C,0,N*N);
    for(int i=0;i<N;i++)for(int k=0;k<N;k++){u8 a=A[i*N+k]; if(!a) continue;
        const u8*Ma=MUL[a]; for(int j=0;j<N;j++){u8 b=B[k*N+j]; if(b) C[i*N+j]=ADD[C[i*N+j]][Ma[b]];}}
}
static int invertible(const u8*A){
    u8 M[64]; memcpy(M,A,N*N);
    for(int c=0;c<N;c++){
        int piv=-1; for(int r=c;r<N;r++) if(M[r*N+c]){piv=r;break;}
        if(piv<0) return 0;
        if(piv!=c) for(int j=0;j<N;j++){u8 t=M[c*N+j];M[c*N+j]=M[piv*N+j];M[piv*N+j]=t;}
        u8 iv=INVT[M[c*N+c]];
        for(int r=c+1;r<N;r++) if(M[r*N+c]){
            u8 f=MUL[M[r*N+c]][iv], nf=NEGT[f]; const u8*Mnf=MUL[nf];
            for(int j=c;j<N;j++) if(M[c*N+j]) M[r*N+j]=ADD[M[r*N+j]][Mnf[M[c*N+j]]];}
    }
    return 1;
}
/* cyclic  <=>  I, M, ..., M^{n-1} linearly independent in F^{n*n} */
static int cyclic(const u8*M){
    u8 rows[8][64]; int piv[8], nr=0;
    u8 cur[64], nxt[64];
    memset(cur,0,N*N); for(int i=0;i<N;i++) cur[i*N+i]=1;
    for(int s=0;s<N;s++){
        u8 v[64]; memcpy(v,cur,N*N);
        for(int r=0;r<nr;r++){u8 f=v[piv[r]]; if(f){u8 nf=NEGT[f];const u8*Mnf=MUL[nf];
            for(int t=piv[r];t<N*N;t++) if(rows[r][t]) v[t]=ADD[v[t]][Mnf[rows[r][t]]];}}
        int pp=-1; for(int t=0;t<N*N;t++) if(v[t]){pp=t;break;}
        if(pp<0) return 0;
        u8 iv=INVT[v[pp]]; const u8*Miv=MUL[iv];
        for(int t=0;t<N*N;t++) v[t]=Miv[v[t]];
        memcpy(rows[nr],v,N*N); piv[nr]=pp; nr++;
        matmul(cur,M,nxt); memcpy(cur,nxt,N*N);
    }
    return 1;
}
/* permutations, grouped by tier: 0 = type (n), 1 = (n-1,1), 2 = other 2-cycle, 3 = >=3 cycles */
static int NP; static u8 PM[5041][64]; static int TIER[5041];
static int ncycles(const int*s){int seen[8]={0},c=0;for(int i=0;i<N;i++)if(!seen[i]){c++;int j=i;while(!seen[j]){seen[j]=1;j=s[j];}}return c;}
static int is_n1(const int*s){int fx=0;for(int i=0;i<N;i++) if(s[i]==i) fx++; return (ncycles(s)==2&&fx==1);}
static void build_perms(void){
    int idx[8]; for(int i=0;i<N;i++) idx[i]=i;
    NP=0;
    int c[8]={0}, i=0;
    int tmp[8]; memcpy(tmp,idx,sizeof(idx));
    /* Heap's algorithm */
    int store[5041][8], ns=0;
    memcpy(store[ns++],tmp,sizeof(int)*N);
    while(i<N){ if(c[i]<i){ if(i%2==0){int t=tmp[0];tmp[0]=tmp[i];tmp[i]=t;} else {int t=tmp[c[i]];tmp[c[i]]=tmp[i];tmp[i]=t;}
            memcpy(store[ns++],tmp,sizeof(int)*N); c[i]++; i=0;} else {c[i]=0;i++;} }
    for(int tier=0;tier<4;tier++){
        for(int k=0;k<ns;k++){
            int*s=store[k]; int nc=ncycles(s); int tt;
            if(nc==1) tt=0; else if(is_n1(s)) tt=1; else if(nc==2) tt=2; else tt=3;
            if(tt!=tier) continue;
            memset(PM[NP],0,N*N);
            for(int j=0;j<N;j++) PM[NP][s[j]*N+j]=1;   /* P e_j = e_{s(j)} */
            TIER[NP]=tt; NP++;
        }
    }
}
static long long gl_order(int n,int q){long long o=1,qn=1;for(int i=0;i<n;i++)qn*=q;
    long long pw=1; for(int i=0;i<n;i++){o*= (qn-pw); pw*=q;} return o;}

static double LIMIT=1200.0; static clock_t T0;
static double el(void){return (double)(clock()-T0)/CLOCKS_PER_SEC;}

static void controls(void){
    int qs[7]={2,3,4,5,7,8,9};
    for(int qi=0;qi<7;qi++){ build_field(qs[qi]);
        for(int n=2;n<=4;n++){ N=n;
            u8 I[64]; memset(I,0,N*N); for(int i=0;i<N;i++) I[i*N+i]=1;
            if(cyclic(I)){printf("NEG-1 FAILED q=%d n=%d\n",qs[qi],n);exit(1);}
            if(qs[qi]>2){u8 T[64];memset(T,0,N*N);for(int i=0;i<N;i++)T[i*N+i]=2;
                if(cyclic(T)){printf("NEG-2 FAILED q=%d n=%d\n",qs[qi],n);exit(1);}}
            u8 C[64]; memset(C,0,N*N); for(int i=1;i<N;i++) C[i*N+i-1]=1; C[0*N+N-1]=1;
            if(!cyclic(C)){printf("POS-1 FAILED q=%d n=%d\n",qs[qi],n);exit(1);}
        }}
    printf("NEG-1/NEG-2/POS-1 pass for q in {2,3,4,5,7,8,9} x n in {2,3,4}\n");
    /* KAT: GF(2), A = J-I, n=6 (no n-cycle, but (5,1) works) and n=4 (n-cycle works) */
    build_field(2);
    int expect[2]={0,1}, nn[2]={6,4};
    for(int e=0;e<2;e++){ N=nn[e]; build_perms();
        u8 A[64]; for(int i=0;i<N;i++)for(int j=0;j<N;j++) A[i*N+j]=(i!=j);
        int got_n=0,got_f=0; u8 M[64];
        for(int k=0;k<NP;k++){ matmul(A,PM[k],M);
            if(cyclic(M)){ if(TIER[k]==0) got_n=1; if(TIER[k]==1) got_f=1; } }
        if(got_n!=expect[e]||!got_f){printf("KAT FAILED n=%d got_n=%d got_f=%d\n",N,got_n,got_f);exit(1);}
        printf("KAT n=%d GF(2) A=J-I: n-cycle works=%d (expected %d), (n-1,1) works=%d  [R8 reproduced]\n",
               N,got_n,expect[e],got_f);
    }
    printf("--- CONTROLS PASS ---\n");
}

int main(int argc,char**argv){
    setvbuf(stdout,NULL,_IOLBF,0);
    T0=clock();
    if(argc>1) LIMIT=atof(argv[1]);
    printf("ROUND 3-C frontier scan; per-cell wall cap %.0fs\n",LIMIT);
    controls();
    int cells[][2]={{3,7},{3,8},{3,9},{4,3},{5,2}};
    int ncell=5;
    for(int ci=0;ci<ncell;ci++){
        int n=cells[ci][0], q=cells[ci][1];
        build_field(q); N=n; build_perms();
        long long total=0, h1v=0, h2v=0, cex=0, need_fb=0;
        double t0=el();
        long long space=1; for(int i=0;i<n*n;i++) space*=q;
        u8 A[64]; int dig[64]; memset(dig,0,sizeof(dig));
        int timed_out=0;
        for(long long idx=0;idx<space;idx++){
            for(int i=0;i<n*n;i++) A[i]=(u8)dig[i];
            if(invertible(A)){
                total++;
                if((total&0xFFFFF)==0 && el()-t0>LIMIT){timed_out=1;break;}
                int hit=-1; u8 M[64];
                for(int k=0;k<NP;k++){ matmul(A,PM[k],M); if(cyclic(M)){hit=TIER[k];break;} }
                if(hit<0){ cex++;
                    printf("  *** COUNTEREXAMPLE n=%d q=%d A =",n,q);
                    for(int i=0;i<n*n;i++) printf(" %d",A[i]); printf(" ***\n");
                    if(cex>=3) break; }
                else { if(hit>=1) need_fb++; if(hit>=2) h2v++; if(hit>=3) h1v++; }
            }
            for(int i=0;i<n*n;i++){ if(++dig[i]<q) break; dig[i]=0; }
        }
        long long exp_=gl_order(n,q);
        printf("n=%d q=%d |GL| enum=%lld expected=%lld POS-2=%s | no-n-cycle=%lld | H2 viol=%lld | H1 viol=%lld | CEX=%lld | %.1fs%s\n",
               n,q,total,exp_, (timed_out?"n/a(timeout)":(total==exp_?"True":"FALSE")), need_fb,h2v,h1v,cex,el()-t0,
               timed_out?"  [CELL INCOMPLETE - CAP HIT]":"");
        if(!timed_out && !cex && total!=exp_){printf("POS-2 FAILED\n");return 1;}
    }
    printf("frontier scan done, %.1fs total\n",el());
    return 0;
}
