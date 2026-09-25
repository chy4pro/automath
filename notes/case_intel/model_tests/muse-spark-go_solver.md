101 is prime, work in the field $\mathbb{F}_{101}$.

$n^2\equiv -1 \pmod{101}$. Since $10^2=100\equiv -1$, $10$ is a root, and $-10\equiv 91$ is another. They are distinct mod 101.

If $x^2\equiv -1$ then $x^2\equiv 10^2\pmod{101}$, so
$$x^2-10^2\equiv (x-10)(x+10)\equiv 0\pmod{101}.$$
Since 101 is prime, $\mathbb{Z}/101\mathbb{Z}$ is an integral domain: $101\mid ab \implies 101\mid a$ or $101\mid b$. Hence
$$101\mid x-10 \quad\text{or}\quad 101\mid x+10,$$
i.e. $x\equiv 10$ or $x\equiv -10\equiv 91\pmod{101}$. A quadratic over a field has at most 2 roots, so these are the only residue classes.

Thus $101\mid n^2+1 \iff n\equiv 10$ or $91\pmod{101}$.

Count $1\le n\le 1000$:

$1000 = 9\cdot 101 + 91$ ($9\cdot 101=909$). Each block of 101 gives one occurrence of each residue. The remaining $91$ numbers $910=9\cdot101+1$ to $1000=9\cdot101+91$ give a second occurrence for residues $1$ to $91$.

Both $10$ and $91$ are $\le 91$, so each occurs $9+1=10$ times:

$10,111,\dots,919$ (10 numbers)
$91,192,\dots,1000$ (10 numbers)

Disjoint, total $10+10=20$.

ANSWER: 20
