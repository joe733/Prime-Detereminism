# Fiduci Prime Lens: defined and proved core

**Status:** A mathematically exact specification of the address filter and trial-division calculator. “Proved” refers to the propositions proved below, not to historical priority or to every visual instrument in the wider Fiduci project.

## 1. Domain and language

The input is a nonnegative integer $N$. In ordinary arithmetic, 0 and 1 are neither prime nor composite; 2 and 3 are prime. An integer $N>1$ is prime if its only positive divisors are 1 and $N$. The Fiduci language calls a possible location an **address**, an established prime an **atom**, and a composite which passed the first two walls a **shadow** or **honorary prime**. “Honorary prime” is a label *inside the instrument*; it never means prime in ordinary arithmetic.

The three mod-3 columns, for $n\ge1$, are

$$
\mathrm{Fi}_n=3n-2,\qquad \mathrm{Du}_n=3n-1,\qquad \mathrm{Ci}_n=3n.
$$

They correspond to residues 1, 2, and 0 modulo 3. The point/line/triangle words are visual names. **Fid** means divisible by 3. **Odd**, **Even**, and **Fid** are useful overlapping flags, *not* three mutually exclusive parity states. In particular, 9 is both odd and Fid.

## 2. Address theorem and exact selector

An integer passes the two walls precisely when it is odd and not divisible by 3. Equivalently, it is 1 or 5 modulo 6. Every prime greater than 3 must pass; the converse fails at 25.

**Proof.** A prime greater than 3 cannot be divisible by 2 or 3. Among the six residues modulo 6, exactly 1 and 5 have neither divisor. Conversely, $25\equiv1\pmod6$ but $25=5^2$. The rejected residues occupy four of every six positions, so the rejected-address density is exactly two-thirds. $\square$

The supplied candidate selector is

$$
C_n=3n-\frac{3-(-1)^n}{2}\quad(n\ge2).
$$

If $n=2k$, then $C_n=6k-1$; if $n=2k+1$, then $C_n=6k+1$. It generates $5,7,11,13,\ldots$, with alternating $+2,+4$ steps: **every candidate address above 3 once and in order**, including composites. This selector proves candidacy, not primality.

## 3. Digit sums and the under-32 glance

For decimal digits $a_i$, $N=\sum_i a_i10^i\equiv\sum_i a_i\pmod3$, since $10\equiv1\pmod3$. Repeated digit sums preserve Fi/Du/Ci membership. A digit sum divisible by 3 proves compositeness when $N>3$; a nonzero sum only reports a candidate column. Reduction to an integer at most 32 is bookkeeping, **not a primality-preserving map**: $25\to7$, yet 25 is composite; $997\to25$, yet 997 is prime.

A direct table for inputs 0–32 is permitted as an optimization. A lookup is not an interview; any displayed count must distinguish the two. Among odd, non-Fid inputs from 5 through 31, only 25 is composite. This bounded observation does not transfer to large numbers which reduce into that range.

## 4. Exact five-gate procedure

1.  **Pre-forms:** return the standard verdict for 0, 1, 2, or 3, with the chosen shape description beside it.
2.  **Wall ×2:** for larger even inputs, return composite, factor 2, and zero candidate interviews.
3.  **Wall ×3:** for remaining multiples of 3, return composite, factor 3, and zero candidate interviews.
4.  **Address:** report the $6k\pm1$ lane. This is a candidate verdict only.
5.  **Interview:** test $d=5,7,11,13,\ldots$, the ordered $6k\pm1$ candidates, while $d^2\le N$. Increment the counter for each actual divisibility test. At the first hit, return composite, factor $d$, cofactor $N/d$, and count. If all clear, return prime and count.

The dual display pairs the usual integer verdict (prime, composite, neither) with the shape-register description (atom, shadow/member, or pre-form). The counter is the number of actual candidate divisibility operations, not a bound, duration, or intrinsic measure of hardness. The optional table can change this number and must be disclosed. A refusal above an implementation cap is not a mathematical verdict.

**Correctness theorem.** This procedure returns the right standard verdict for every nonnegative integer $N$.

**Proof.** The special inputs and wall hits are immediate. For an input surviving both walls, if it is composite, write $N=ab$ with $1<a\le b$. Then $a\le\sqrt N$, so $N$ has a prime factor $q\le\sqrt N$. Because 2 and 3 do not divide $N$, $q\ge5$ and $q\equiv1$ or 5 modulo 6. The ordered interview therefore reaches $q$ while $q^2\le N$, unless a divisor was already found. If none divides, $N$ cannot be composite and is prime. An earlier candidate divisor than the least prime factor is impossible, even though the iterator may also test composite candidates. $\square$

## 5. Shadows and the fixed-guard frontier

Suppose the sieve has guarded all primes smaller than a prime $p$. Every multiple $mp$ with $2\le m<p$ has some prime factor of $m$ smaller than $p$, so it was removed earlier. The first *new, previously unremoved* strike by $p$ is $p^2$. This is the exact sense in which a prime casts its first shadow at its square. It is not its first literal multiple in a lane (35 is a lane multiple of 7 before 49, but 5 already catches it).

**Finite-guard theorem.** With every prime less than $p$ guarded and $p$ the first unguarded prime, each survivor $2\le N<p^2$ is prime, but the composite $p^2$ survives. **Proof:** any composite below $p^2$ has a prime divisor below $p$; $p^2$ has no such divisor. Thus guards {2,3} first fail at 25; adding 5 shifts the first failure to 49; adding 7 shifts it to 121. No fixed finite set of prime-divisibility guards is complete for all integers. $\square$

The first flaw 25 is permanent *as the first failure of the two-wall filter*, not as a survivor of a stronger wheel containing 5. The larger algorithm remains exact because its interview grows with $N$.

## 6. Two residue octets, one exact rhythm

The two walls leave eight classes in a 24-position cycle:

$$
U(24)=\{1,5,7,11,13,17,19,23\}.
$$

These are precisely the multiplicative units modulo 24. Each squares to 1 modulo 24, and their group is $C_2\times C_2\times C_2$. The statement concerns these eight classes, not every residue modulo 24. For every prime $p>3$, $p^2\equiv1\pmod{24}$: an odd square is 1 modulo 8 and a square not divisible by 3 is 1 modulo 3; CRT joins the two. The exceptional primes 2 and 3 do not satisfy the displayed formula. Also, for $p>3$, $p^2+2$ is divisible by 3 and $p^2-2\equiv5\pmod6$, a **candidate address**, not a prime prediction.

A different eight-seat cycle is the wheel of residues coprime to 30:

$$
U(30)=\{1,7,11,13,17,19,23,29\}.
$$

Reading clockwise from 1, including the wrap 29→31 (the next 1 modulo 30), yields successive gaps

$$
G=(6,4,2,4,2,4,6,2),\qquad\sum G_i=30.
$$

This **proves** the supplied rhythm as a wheel-30 gap vector. It is not the cyclic gap vector of $U(24)$, which is $(4,2,4,2,4,2,4,2)$. The separate fiduci-prime opcode array $[3,7,11,13,17,19,23,29]$ replaces wheel-30’s 1 with 3; it is an intentional or incidental encoding choice to be specified, not a second proof of the displayed gaps.

In base twelve, an integer coprime to 6 has last digit 1, 5, 7, or eleven (Ɛ/B in the supplied notation). This is equivalent to the two-wall address condition, since 12 is divisible by 6. It is not a prime test.

## 7. Finite checks and bounds of the claim

Run `python3 verify_prime_lens.py`. The reference script uses standard-library integer arithmetic and compares 1,000,001 inputs (0–1,000,000) with a separately implemented sieve of Eratosthenes: **0 mismatches** in the recorded run. It checks digit sums, base-twelve addresses, the mod-24 and mod-30 cycles, prime-square residues, fixed-guard witnesses, and selected large inputs. For 999,999,999,989 it exhausts 333,332 admissible candidate divisions and finds none through $\lfloor\sqrt N\rfloor=999,999$. This is an exact result for that particular input under the proved square-root theorem; it is not a claim about run time on all hardware.

The full prime indicator is not eventually periodic: if it had period $T>0$ past some threshold, choose a prime $p$ above that threshold. Repeating the period $p$ times would say $p+pT=p(1+T)$ is prime, a contradiction. This only excludes fixed periodic verdict patterns. It does **not** exclude efficient deterministic primality algorithms. For example, Agrawal, Kayal, and Saxena proved one with polynomial time in the input bit length: [*PRIMES is in P*, *Annals of Mathematics* 160 (2004), 781–793](https://annals.math.princeton.edu/2004/160-2/p12).

This specification establishes the **defined/proved calculator and residue core**. It does not certify an independent Π-box forward-walk/gap identity, “twinless six,” width rotation, additive ladders, Mandelbulb symmetry, cryptographic hardness, performance promises, or historical novelty. Those require their own definitions, proofs, and/or evidence. Their preservation and precise questions are in the separately supplied author workbook, not silently promoted to theorems here.
