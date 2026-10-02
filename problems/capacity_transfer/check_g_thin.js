'use strict';
// Dependency-free exact checks. Number is used only for small loop/index bounds;
// all weighted inequalities, rational substitutions and certificates use BigInt.
const assert = (ok, label) => { if (!ok) throw new Error(label); };
const gcd = (a, b) => { a = a < 0n ? -a : a; while (b) [a,b]=[b,a%b]; return a; };
class R {
  constructor(n, d=1n) {
    n=BigInt(n); d=BigInt(d); assert(d!==0n,'zero denominator');
    if(d<0n){n=-n;d=-d;} const g=gcd(n,d); this.n=n/g;this.d=d/g;
  }
  add(t){return new R(this.n*t.d+t.n*this.d,this.d*t.d);}
  sub(t){return new R(this.n*t.d-t.n*this.d,this.d*t.d);}
  mul(t){return new R(this.n*t.n,this.d*t.d);}
  div(t){return new R(this.n*t.d,this.d*t.n);}
  eq(t){return this.n*t.d===t.n*this.d;}
  lt(t){return this.n*t.d<t.n*this.d;}
  le(t){return this.n*t.d<=t.n*this.d;}
}
const r=(n,d=1n)=>new R(n,d);
function weight(d,p,q) {
  d=BigInt(d); if(d<0n)d=-d; const u=d*q;
  return u>p ? 0n : 4n*p**3n-6n*u*p**2n+2n*u**3n;
}
function energy(A,p,q) {
  let e=0n;for(const a of A)for(const b of A)e+=weight(a-b,p,q);return e;
}
function diffCounts(A) {
  const out=new Map();
  for(let i=0;i<A.length;i++)for(let j=0;j<i;j++){
    const d=A[i]-A[j];out.set(d,(out.get(d)||0)+1);
  }
  return out;
}
function lattice(p,q) {
  let z=0n;for(let d=1n;d*q<=p;d++)z+=2n*weight(d,p,q);
  assert(z*q<=p*(3n*p**3n),'lattice majorant');return z;
}
function subset(mask,N) {
  const A=[];for(let i=0;i<N;i++)if(mask&(1<<i))A.push(i);return A;
}
function sumUnique(A,diagonal) {
  const seen=new Set();
  for(let i=0;i<A.length;i++)for(let j=diagonal?i:i+1;j<A.length;j++){
    const s=A[i]+A[j];if(seen.has(s))return false;seen.add(s);
  }return true;
}
function unorderedSumMax(A) {
  const counts=new Map();let max=0;
  for(let i=0;i<A.length;i++)for(let j=i;j<A.length;j++){
    const s=A[i]+A[j],v=(counts.get(s)||0)+1;counts.set(s,v);if(v>max)max=v;
  }return max;
}
// Check the scalar identity in Q[gamma] with gamma^2=gammaSquare.
// Its degree in x is at most four, so five exact rational x values
// establish equality of both coefficient polynomials.
function scalarIdentity(gammaSquare,C,expected) {
  const qa=(a,b)=>[a[0].add(b[0]),a[1].add(b[1])];
  const qm=(a,b)=>[
    a[0].mul(b[0]).add(a[1].mul(b[1]).mul(gammaSquare)),
    a[0].mul(b[1]).add(a[1].mul(b[0]))
  ];
  const qs=(a,b)=>qa(a,[r(-1).mul(b[0]),r(-1).mul(b[1])]);
  const qc=a=>[a,r(0)], gamma=[r(0),r(1)];
  for(let j=0n;j<=4n;j++){
    const x=r(j),gx=qm(gamma,qc(x));
    const y=qa(qa(qc(x.mul(x)),gx),qc(r(C)));
    const p0=qs(qs(qs(qm(y,y),qm(qa(gx,qc(gammaSquare)),y)),
                  qc(r(j**4n))),qm(gamma,qc(r(j**3n))));
    const rhs=expected(x);
    assert(p0[0].eq(rhs[0])&&p0[1].eq(rhs[1]),'scalar polynomial identity');
  }
}
function strongScalarChecks(){
  assert(120n**4n===207360000n,'120^4');
  assert(24000n*32n<2n**20n,'uniform exponential envelope');
  assert(r(8,9).lt(r(1)),'gamma<1');
  assert(r(2).le(r(9,4)),'sqrt2<=3/2');
  assert(r(1,8).add(r(3,64)).eq(r(11,64)),'tail cost');
  assert(r(1).sub(r(11,64)).eq(r(53,64)),'positive scalar margin');
  scalarIdentity(r(8,9),1n,x=>[
    r(10,9).mul(x.mul(x)).add(r(1,9)),r(1,9).mul(x)
  ]);
}

strongScalarChecks();
const scales=[[1n,1n],[2n,1n],[3n,2n],[5n,2n],[9n,2n],[12n,1n],[23n,2n],[25n,1n]];
for(const[p,q]of scales)lattice(p,q);
const counter=[0,1,2,3];
assert(unorderedSumMax(counter)===2,'unordered B2[2] negative control');
assert(diffCounts(counter).get(1)===3,'B2[2] does not imply 2-thin differences');
assert(20366n*20365n/2n>120n**4n,'diameter inverse onset');
let admitted=0,energyChecks=0;
for(let mask=0;mask<(1<<12);mask++){
  const A=subset(mask,12),counts=diffCounts(A),K=BigInt(A.length);
  for(let g=1;g<=4;g++){
    if([...counts.values()].some(c=>c>g))continue;admitted++;
    assert(K*(K-1n)/2n<=BigInt(g*11),'difference counting');
    for(const[p,q]of scales){
      const D=3n*p**3n,E=energy(A,p,q),diag=weight(0,p,q)*K;
      assert((E-diag)*q<=BigInt(g)*p*D,'g-thin nonzero energy bound');
      let expanded=diag;for(const[d,c]of counts)expanded+=2n*BigInt(c)*weight(d,p,q);
      assert(E===expanded,'diagonal counted once per element');energyChecks++;
    }
  }
}
let substitutions=0;
for(const g of [1n,2n,7n])for(const N of [r(17),r(35,2)])
for(const T of [r(1),r(3,2),r(7,3)])for(const K of [r(0),r(1),r(5)]){
  const G=r(g),X=G.mul(N),S=G.mul(T),eps=r(1,137);
  const original=N.div(T).add(r(2,3)).add(eps).mul(G.mul(T).add(r(4,3).mul(K)));
  const changed=X.div(S).add(r(2,3)).add(eps).mul(S.add(r(4,3).mul(K)));
  assert(original.eq(changed),'real-parameter substitution');
  assert(N.div(T).eq(X.div(S)),'exponential argument unchanged');substitutions++;
}
assert(admitted>0,'nonvacuous enumeration');
console.log(JSON.stringify({status:'PASS',arithmetic:'exact BigInt/rational',subsets:1<<12,
  admissibleSetAndG:admitted,energyChecks,substitutions,
  analyticScope:'finite checks and scalar constants; not a new proof of COMMON_CAPACITY'}));

