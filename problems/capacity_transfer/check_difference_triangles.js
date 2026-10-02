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
assert(20364n*20365n/2n===207356430n,'preceding onset product');
assert(20365n*20366n/2n===207376795n,'onset product');
assert(20364n*20365n/2n<120n**4n,'counting insufficient at 20364');
assert(20365n*20366n/2n>120n**4n,'counting sufficient at 20365');
assert(r(5,4).add(r(1,8)).lt(r(2)),'explicit inversion remainder');
const scales=[[1n,1n],[3n,2n],[5n,2n],[7n,1n],[19n,2n],[12n,1n]];
for(const[p,q]of scales)lattice(p,q);
const C1=diffCounts([0,1,3]),C2=diffCounts([0,1,4]);
assert([...C1.values()].every(c=>c===1)&&[...C2.values()].every(c=>c===1),'rows individually Golomb');
assert([...C1.keys()].some(d=>C2.has(d)),'individual Golomb does not imply DTS');
let families=0,energyChecks=0,threeRowFamilies=0;
for(let m=1;m<=9;m++)for(let K=2;K<=4;K++){
  const rows=[];
  for(let mask=0;mask<(1<<m);mask++){
    const A=[0,...subset(mask,m).map(x=>x+1)];if(A.length!==K)continue;
    const c=diffCounts(A);if([...c.values()].some(v=>v!==1))continue;
    let dm=0;for(const d of c.keys())dm|=1<<(d-1);
    rows.push({A,dm});
  }
  function visit(start,chosen,used){
    if(chosen.length){
      families++;const n=chosen.length;if(n===3)threeRowFamilies++;
      const scope=Math.max(...chosen.map(row=>row.A[row.A.length-1]));
      let count=0;for(let d=1;d<=m;d++)if(used&(1<<(d-1)))count++;
      assert(count===n*K*(K-1)/2,'global positive-difference count');
      assert(BigInt(n*K*(K-1)/2)<=BigInt(scope),'scope counting bound');
      for(const[p,q]of scales){
        const D=3n*p**3n,N=BigInt(n),KK=BigInt(K);
        let E=0n;for(const row of chosen)E+=energy(row.A,p,q);
        const diagonal=N*KK*weight(0,p,q);let off=0n;
        for(let d=1;d<=m;d++)if(used&(1<<(d-1)))off+=2n*weight(d,p,q);
        assert(E===diagonal+off,'sum of row energies, no cross-row terms');
        assert(E*q<=diagonal*q+p*D,'one shared lattice budget');energyChecks++;
      }
    }
    if(chosen.length===3)return;
    for(let i=start;i<rows.length;i++)if((used&rows[i].dm)===0)
      visit(i+1,[...chosen,rows[i]],used|rows[i].dm);
  }
  visit(0,[],0);
}
let substitutions=0,nonintegral=0;
for(const n of [1n,2n,3n,7n])for(const m of [11n,17n,29n])
for(const T of [r(1),r(3,2),r(7,3)])for(const K of [r(2),r(5)]){
  const M=r(m),N=r(n),X=M.div(N),S=T.div(N),eps=r(1,137);
  const original=M.div(T).add(r(2,3)).add(eps).mul(T.div(N).add(r(4,3).mul(K)));
  const changed=X.div(S).add(r(2,3)).add(eps).mul(S.add(r(4,3).mul(K)));
  assert(original.eq(changed),'m/n and T/n real substitution');
  assert(M.div(T).eq(X.div(S)),'exponential argument unchanged');
  if(X.d!==1n)nonintegral++;substitutions++;
}
assert(families>0&&threeRowFamilies>0&&nonintegral>0,'nonvacuous coverage');
console.log(JSON.stringify({status:'PASS',arithmetic:'exact BigInt/rational',
  scopeMax:9,marksPerRowMax:4,rowsPerFamilyMax:3,families,threeRowFamilies,
  energyChecks,substitutions,nonintegralParameterExamples:nonintegral,
  analyticScope:'finite checks and exact 20365 onset; not a new proof of COMMON_CAPACITY'}));

