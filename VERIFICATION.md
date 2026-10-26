# Verification record

**Run date:** 26 October 2026.  
**Reference runtime:** Python 3.12.14, standard library only.  
**Reproduce:** `python3 verify_prime_lens.py`.

## Exactness of the calculator

The script compared the lens procedure with an independently coded sieve of Eratosthenes for all **1,000,001 integers from 0 through 1,000,000**: 78,498 primes, **zero mismatches**. This is a finite implementation check. The universal correctness proof is in [SPECIFICATION.md](SPECIFICATION.md), section 4; it rests on every composite having a prime factor at most its square root, and on the candidate walk containing every such factor after the walls.

Selected exact results under the script's interview-count convention (no optional small-number table):

| Input | Prime? | Candidate interviews | First divisor | Digit-sum glance |
|---:|:---:|---:|---:|:---|
| 25 | No | 1 | 5 | 7 |
| 211 | Yes | 4 | — | 4 |
| 437 | No | 6 | 19 | 14 |
| 997 | Yes | 10 | — | 25 |
| 2,207 = 47² − 2 | Yes | 14 | — | 11 |
| 486,385 | No | 1 | 5 | 34 → 7 |
| 1,000,001 | No | 33 | 101 | 2 |
| 999,999,999,989 | Yes | 333,332 | — | 107 → 8 |

For the last input, `floor(sqrt(N)) = 999,999`, so clearing the complete admissible divisor sequence is an exact proof of that *particular* verdict. It does not support a blanket speed claim or a new complexity lower bound.

## Targeted law checks

The script also checks:

- Decimal digit sum and the original number have the same remainder mod 3 throughout 0–1,000,000.
- The four base-12 final digits 1, 5, 7, eleven are exactly the odd/non-Fid addresses in that range.
- All sampled primes above 3 satisfy `p² ≡ 1 (mod 24)`, `p² + 2 ≡ 0 (mod 3)`, and `p² − 2 ≡ 5 (mod 6)`. The universal proof uses parity, mod 3, and CRT; the sample is a check.
- Every mod-24 unit squares to 1. The mod-30 units are `[1,7,11,13,17,19,23,29]`, with cyclic gaps `[6,4,2,4,2,4,6,2]`, **exactly the supplied GAPS vector**. The two cycles should not be conflated.
- For the first few next unguarded primes, their squares survive every smaller prime guard. The theorem covers every next unguarded prime.

## Deliberate attempts to falsify overbroad readings

| Overbroad reading | Decisive check | Correct scope |
|:---|:---|:---|
| A digit-sum glance transfers primality | 25→7; 997→25 | It transfers only remainder mod 3 |
| The two walls certify every survivor | 25 passes, yet equals 5² | They certify the address only |
| Every prime square is 1 mod 24 | 3²=9 mod 24 | Every prime **greater than 3** |
| “Span minus two” forces an even Π-box count | Five-position picture has three interior cells | Need a separate exact definition of count |
| Interior seats between consecutive odd primes are even | 3..5 has one interior seat; 7..11 has three | The **prime gap**, not interior count, is even |
| Supplied GAPS belong to the mod-24 octet | Its cyclic gaps are `[4,2,4,2,4,2,4,2]` | Supplied GAPS belong to the mod-30 wheel |
| Mod-24 units and mod-30 units have the same square-one group structure | 7²≡19 mod 30 | The square-one group claim is about mod 24 |
| A fixed wheel is a universal prime test | The first unguarded prime's square passes | The interview must grow or another exact method must be used |

The guard-twin alternation is retained as a failed conjecture: 47² − 2 = 2,207 is prime. The wheel-30 match is a positive finding; the separate 24-bit opcode semantics still need an authorial definition.

## What this does not test

The supplied source material does not define an independent Π-box forward-walk, re-chunking/honour rule, “twinless six,” width rotation, additive ladder, or Mandelbulb map well enough to run a faithful test. A conditional box can be defined so its count equals an odd-prime gap and is therefore even, but that identity would be built into its definition. The accompanying author workbook asks for the missing input/output rules. No claim about originality, cryptographic security, or universal performance is established by this test record.
