'use strict';

// Task039 sonar verifier. Dependency-free, exact BigInt/rational arithmetic.
// The general theorem is proved in SONAR.md; these are finite checks.
const assert = (b, msg) => { if (!b) throw new Error(msg); };
const abs = x => x < 0n ? -x : x;
function gcd(a,b) { a=abs(a); b=abs(b); while(b) [a,b]=[b,a%b]; return a; }
function R(p,q=1n) {
  p=BigInt(p); q=BigInt(q); assert(q!==0n,'zero denominator');
  if(q<0n) {p=-p;q=-q;} const d=gcd(p,q); return {p:p/d,q:q/d};
}
const add=(a,b)=>R(a.p*b.q+b.p*a.q,a.q*b.q);
const neg=a=>R(-a.p,a.q);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>R(a.p*b.p,a.q*b.q);
const div=(a,b)=>R(a.p*b.q,a.q*b.p);
const le=(a,b)=>a.p*b.q<=b.p*a.q;
const eq=(a,b)=>a.p===b.p&&a.q===b.q;
const Z=R(0),ONE=R(1),A=R(4,3),B=R(2,3);
const show=a=>`${a.p}/${a.q}`;
function tri(d,U) { d=Math.abs(d); return d>=U ? Z : R(U-d,U); }
function rampAtHalfScale(d,t) {
  // T2=t/2, so |d|/T2=2|d|/t.
  d=Math.abs(d); if(2*d>=t) return Z;
  const u=R(2*d,t), u3=mul(mul(u,u),u);
  return add(sub(A,mul(R(2),u)),mul(B,u3));
}
function exactLambda(m,U) {
  let s=Z;
  for(let i=0;i<m;i++) for(let j=0;j<m;j++) s=add(s,tri(i-j,U));
  return s;
}
function lambdaFormula(m,U) {return sub(R(m*U),R(U*U-1,3));}
function energy(seq,U,t) {
  let s=mul(A,R(seq.length));
  for(let i=0;i<seq.length;i++) for(let j=i+1;j<seq.length;j++)
    s=add(s,mul(R(2),mul(tri(j-i,U),rampAtHalfScale(seq[j]-seq[i],t))));
  return s;
}
function energyUpper(m,U,t) {return add(mul(A,R(m)),mul(R(U-1),add(R(t,2),A)));}

// Rigorous enclosure of (3/4)^(p/q). No floating point roots or logs.
function powerEnclosure(p,q) {
  const scale=1n<<64n, num=3n**BigInt(p), den=4n**BigInt(p), Q=BigInt(q);
  const rhs=num*scale**Q;
  let lo=0n,hi=scale+1n;
  while(hi-lo>1n) {
    const mid=(lo+hi)/2n;
    if(mid**Q*den<=rhs)lo=mid;else hi=mid;
  }
  assert(lo**Q*den<=rhs && hi**Q*den>rhs,'root enclosure');
  return [R(lo,scale),R(hi,scale)];
}
const capCache=new Map();
function capEnclosure(n,t) {
  const key=`${n},${t}`;
  if(!capCache.has(key)) {
    const [lo,hi]=powerEnclosure(2*n,t), base=add(R(2*n,t),B);
    capCache.set(key,[add(base,mul(R(200),lo)),add(base,mul(R(200),hi))]);
  }
  return capCache.get(key);
}

let lambdaChecks=0,latticeChecks=0,sequenceChecks=0,sandwichChecks=0;
for(let m=1;m<=40;m++) for(let U=1;U<=m;U++) {
  assert(eq(exactLambda(m,U),lambdaFormula(m,U)),`Lambda m=${m},U=${U}`);
  lambdaChecks++;
}
for(let n=1;n<=4;n++) for(let t=1;t<=2*n;t++) {
  let s=A;
  for(let d=1;2*d<=t;d++)s=add(s,mul(R(2),rampAtHalfScale(d,t)));
  assert(le(s,add(R(t,2),A)),`ramp lattice n=${n},t=${t}`);
  latticeChecks++;
}
for(let U=1;U<=40;U++) {
  let s=Z; for(let d=1;d<U;d++)s=add(s,mul(R(2),tri(d,U)));
  assert(eq(s,R(U-1)),`triangle lattice U=${U}`); latticeChecks++;
}

const prefixesByRows=[];
for(let n=1;n<=4;n++) {
  const counts=Array(2*n+1).fill(0),seq=[],used=new Set();
  function visit() {
    const m=seq.length;
    if(m>0) {
      counts[m]++; sequenceChecks++;
      for(let U=1;U<=m;U++) for(let t=1;t<=2*n;t++) {
        const lam=lambdaFormula(m,U), E=energy(seq,U,t), upper=energyUpper(m,U,t);
        assert(le(R(m),lam),'Lambda positive diagonal bound');
        assert(le(E,upper),`energy upper n=${n},seq=${seq},U=${U},t=${t}`);
        const [Clo,Chi]=capEnclosure(n,t);
        // A lower enclosure suffices to certify the true-real sandwich.
        // If unresolved, a finer enclosure would be needed, not a tolerance.
        assert(le(lam,mul(E,Clo)),`lower sandwich unresolved/failed n=${n},seq=${seq},U=${U},t=${t}`);
        assert(le(lam,mul(upper,Clo)),`S unresolved/failed n=${n},seq=${seq},U=${U},t=${t}`);
        assert(le(Clo,Chi),'capacity enclosure order');
        sandwichChecks++;
      }
    }
    if(m===2*n)return;
    for(let y=0;y<n;y++) {
      const fresh=[];let ok=true;
      for(let i=0;i<m;i++) {
        const key=`${m-i},${y-seq[i]}`;
        if(used.has(key)){ok=false;break;}
        fresh.push(key);
      }
      if(!ok)continue;
      for(const key of fresh)used.add(key);seq.push(y);visit();seq.pop();
      for(const key of fresh)used.delete(key);
    }
  }
  visit();prefixesByRows.push({n,counts:counts.slice(1)});
}

// Negative control: the repeated gap-one vector violates the model,
// and the claimed off-diagonal upper bound must NOT pass automatically.
const bad=[0,0,0],badE=energy(bad,3,1),badUpper=energyUpper(3,3,1);
assert(!le(badE,badUpper),'negative control unexpectedly passes');
assert(eq(badE,R(76,9))&&eq(badUpper,R(23,3)),'negative control values');

// Tail base and derivative-onset facts used in the analytic proof.
assert(9n*3n**8n<4n**8n,'(3/4)^8 < 1/9');
assert(200n*48n**2n<9n**6n,'tail base at 48');
assert(48n**3n===110592n,'stated onset');
assert(le(R(35,72),R(1,2))&&!eq(R(35,72),R(1,2)),'denominator positive');

// Laurent polynomials in x, represented as exponent -> rational coefficient.
function poly(entries){const p=new Map();for(const [e,c]of entries)p.set(e,c);return p;}
function padd(p,q){const r=new Map(p);for(const[e,c]of q)r.set(e,add(r.get(e)||Z,c));return r;}
function pscale(p,c){return new Map([...p].map(([e,a])=>[e,mul(a,c)]));}
function pmul(p,q){let r=new Map();for(const[e,a]of p)for(const[f,b]of q)r.set(e+f,add(r.get(e+f)||Z,mul(a,b)));return r;}
function pshiftDegree(p,d){return new Map([...p].map(([e,c])=>[e+d,c]));}
function peq(p,q){for(const e of new Set([...p.keys(),...q.keys()]))if(!eq(p.get(e)||Z,q.get(e)||Z))return false;return true;}
const Y=poly([[3,ONE],[2,R(2)],[1,R(3)]]);
const D=poly([[0,ONE],[-1,R(-2,3)],[-2,R(-4,9)],[-4,R(-2,3)]]);
const rhsB=poly([[3,ONE],[2,R(4,3)],[1,R(5,6)],[0,R(20,9)],[-1,R(1,4)],[-2,R(4,3)]]);
const P=poly([[4,R(14)],[3,R(-184)],[2,R(-81)],[1,R(-96)],[0,R(-72)]]);
assert(peq(pshiftDegree(pscale(padd(pmul(Y,D),pscale(rhsB,R(-1))),R(36)),3),P),'explicit polynomial identity');
function substitutePlus(p,c){
  let r=new Map();const base=poly([[1,ONE],[0,R(c)]]);
  for(const[e,a]of p){assert(e>=0,'nonnegative degree');let power=poly([[0,ONE]]);for(let j=0;j<e;j++)power=pmul(power,base);r=padd(r,pscale(power,a));}
  return r;
}
const shifted=poly([[4,R(14)],[3,R(712)],[2,R(12591)],[1,R(85376)],[0,R(141496)]]);
assert(peq(substitutePlus(P,16),shifted),'positive shift x=t+16');
assert([...shifted.values()].every(c=>c.p>0n),'positive shift coefficients');

console.log(JSON.stringify({status:'PASS',arithmetic:'exact BigInt/rational; no dependencies',
  lambdaChecks,latticeChecks,sequenceChecks,sandwichChecks,prefixesByRows,
  capacityPowerEnclosures:capCache.size,
  negativeControl:{energy:show(badE),purportedUpper:show(badUpper),rejected:true},
  explicitOnset:110592,polynomialIdentity:true,positiveShift:true,
  scope:'finite error checks only; general proof is SONAR.md + COMMON_CAPACITY.md'},null,2));
