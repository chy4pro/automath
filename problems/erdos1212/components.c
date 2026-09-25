// Component structure of the admissible visible-lattice graph in [2,N]^2 (Erdos 1212, strengthened).
// admissible(x,y): gcd(x,y)==1, x>1, y>1, and (x composite or y composite). Edges: unit steps.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
static int *par; static int findp(int a){while(par[a]!=a){par[a]=par[par[a]];a=par[a];}return a;}
int main(int argc,char**argv){int N=atoi(argv[1]); long M=(long)(N+1)*(N+1);
 char*comp=calloc(N+2,1); comp[0]=comp[1]=1; for(int i=2;(long)i*i<=N;i++) if(!comp[i]) for(int j=i*i;j<=N;j+=i) comp[j]=1;
 char*adm=calloc(M,1); long cnt=0;
 for(int x=2;x<=N;x++) for(int y=2;y<=N;y++) if((comp[x]||comp[y]) && gcd(x,y)==1){adm[(long)x*(N+1)+y]=1;cnt++;}
 par=malloc(M*sizeof(int)); for(long i=0;i<M;i++) par[i]=(int)i;
 for(int x=2;x<=N;x++) for(int y=2;y<=N;y++){ long i=(long)x*(N+1)+y; if(!adm[i]) continue;
   if(x<N && adm[i+(N+1)]){int a=findp(i),b=findp(i+(N+1)); if(a!=b) par[a]=b;}
   if(y<N && adm[i+1]){int a=findp(i),b=findp(i+1); if(a!=b) par[a]=b;} }
 int*sz=calloc(M,sizeof(int)); for(long i=0;i<M;i++) if(adm[i]) sz[findp(i)]++;
 long best=0,second=0; int broot=-1; for(long i=0;i<M;i++){ if(sz[i]>best){second=best;best=sz[i];broot=(int)i;} else if(sz[i]>second) second=sz[i]; }
 int minx=N,maxx=0,miny=N,maxy=0; long touchN=0; int minsum=2*N;
 for(int x=2;x<=N;x++) for(int y=2;y<=N;y++){ long i=(long)x*(N+1)+y; if(adm[i]&&findp(i)==broot){ if(x<minx)minx=x; if(x>maxx)maxx=x; if(y<miny)miny=y; if(y>maxy)maxy=y; if(x==N||y==N) touchN++; if(x+y<minsum) minsum=x+y; } }
 printf("N=%d admissible=%ld density=%.4f largest=%ld (%.1f%%) second=%ld span x[%d,%d] y[%d,%d] min(x+y)=%d far-edge vertices=%ld\n",N,cnt,(double)cnt/((double)(N-1)*(N-1)),best,100.0*best/cnt,second,minx,maxx,miny,maxy,minsum,touchN);
 return 0;}
