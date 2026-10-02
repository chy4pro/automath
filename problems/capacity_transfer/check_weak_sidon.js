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

const scales=[[1n,1n],[2n,1n],[3n,2n],[5n,2n],[9n,2n],[12n,1n],[23n,2n],[25n,1n]];
for(const [p,q] of scales)lattice(p,q);
assert(90n**4n===65610000n,'90^4');
assert(6n*20n**2n<49n**2n,'sqrt6<49/20');
assert(r(8,3).lt(r(25,9)),'gamma<5/3');
assert(r(2,7).div(r(49,20)).eq(r(40,343)),'logarithm/radical envelope');
assert(r(90).mul(r(40,343)).eq(r(3600,343)),'exponent at onset');
const factorial=n=>{let v=1n;for(let j=2n;j<=n;j++)v*=j;return v;};
let series=r(0);for(let j=0n;j<=6n;j++)series=series.add(r(1,factorial(j)));
assert(series.eq(r(1957,720)),'e series lower bound');
const den=24n*343n**4n;let num=0n;
for(let j=0n;j<=4n;j++)num+=170n**j*343n**(4n-j)*(24n/factorial(j));
const lhs=1957n**10n*num, rhs=36000n*720n**10n*den;
assert(lhs===449233538381596942864443106714320805345633416n,'printed certificate lhs');
assert(rhs===447728960659239231243811144335360000000000000n,'printed certificate rhs');
assert(lhs>rhs,'exp(3600/343)>36000 certificate');
assert(r(4,3).sub(r(10,810)).sub(r(4,24300)).eq(r(8024,6075)),'P0 margin');
assert(r(13,10).lt(r(8024,6075)),'P0>13/10');
assert(r(49,40).add(r(1,45)).add(r(1,2430)).add(r(1,182250)).lt(r(5,4)),'tail<5/4');
assert(r(13,10).sub(r(5,4)).eq(r(1,20)),'final positive margin');
scalarIdentity(r(8,3),2n,x=>[
  r(4,3).mul(x.mul(x)).sub(r(4,3)),r(-2,3).mul(x)
]);
assert(sumUnique([0,1,2],false),'three-term AP is weak Sidon');
assert(!sumUnique([0,1,2],true),'three-term AP is not strong Sidon');
assert(!sumUnique([0,1,2,3],false),'four-term AP violates weak Sidon');
let accepted=0,energyChecks=0,repeatedCases=0;
for(let mask=0;mask<(1<<14);mask++){
  const A=subset(mask,14);if(!sumUnique(A,false))continue;accepted++;
  const k=A.length,counts=diffCounts(A),centers=new Set();let repeats=0;
  for(const [d,count] of counts){
    assert(count<=2,'r(d)<=2');
    if(count===2){
      repeats++;repeatedCases++;
      const lows=A.filter(p=>A.includes(p+d));assert(lows.length===2,'two lower endpoints');
      assert(lows[1]===lows[0]+d,'repeated difference is a three-term AP');
      const center=lows[1];assert(!centers.has(center),'distinct repeat steps have distinct centers');
      centers.add(center);assert(center>A[0]&&center<A[k-1],'center is interior');
    }
  }
  if(k>=2)assert(repeats<=k-2,'P<=k-2');else assert(repeats===0,'small cardinalities');
  for(const [p,q] of scales){
    const D=3n*p**3n,w0=weight(0,p,q),E=energy(A,p,q),K=BigInt(k);
    let decomposition=w0*K;for(const[d,c]of counts)decomposition+=2n*BigInt(c)*weight(d,p,q);
    assert(E===decomposition,'ordered energy decomposition');
    assert(E*q<=p*D+4n*K*D*q,'weak scalar energy bound');
    if(k>=2)assert(3n*E*q<=3n*p*D+(12n*K-16n)*D*q,'sharper k>=2 energy bound');
    energyChecks++;
  }
}
assert(accepted>0&&repeatedCases>0,'nonvacuous enumeration');
console.log(JSON.stringify({status:'PASS',arithmetic:'exact BigInt/rational',subsets:1<<14,
  weakSidonSets:accepted,energyChecks,repeatedDifferenceInstances:repeatedCases,
  analyticScope:'finite checks plus exact onset certificate; not a new proof of COMMON_CAPACITY'}));

