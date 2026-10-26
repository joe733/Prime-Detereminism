# Prime-Detereminism

An address-first, hand-auditable presentation of prime candidacy and exact primality testing by Joe Smith / Fiduci Group. The lens names three mod-3 columns (**Fi**, **Du**, **Ci**), applies the ×2 and ×3 walls, walks the surviving $6k\pm1$ addresses, and displays every divisor interview up to the square-root frontier. An address is a candidate, never a proof of primality; 25 is the first wall-surviving composite.

Start with (SPECIFICATION.md): the **defined and proved core**, with a universal correctness proof. The supplied rhythm `[6,4,2,4,2,4,6,2]` is proved there to be the cyclic gap sequence of the mod-30 wheel. It is distinct from the mod-24 octet and the fiduci-prime opcode list, which uses 3 instead of wheel seat 1.

The [expanded manuscript](Fiduci_Prime_Lens_Formalized.md) preserves the Π-box, shape register, visual instruments, fidbit encoding, proof ledger, and clearly marked open questions. A [plain-text edition](Fiduci_Prime_Lens_Formalized.txt) is also included. No assertion labeled open is certified by the specification.

## Verify the computational claims

With Python 3 and no third-party packages:

``` sh
python3 verify_prime_lens.py
```

The script compares every integer from 0 through 1,000,000 against an independently implemented Eratosthenes sieve and checks selected large examples by exact candidate division. It also checks the mod-24 and mod-30 sequences, digit sums, prime-square residues, and fixed-guard witnesses. On the recorded run, all 1,000,001 small verdicts matched; the large prime 999,999,999,989 required 333,332 interviews. See the [verification record](VERIFICATION.md) for the precise results and attempted counterexamples. The universal proof of the procedure is in the specification. Finite tests check the implementation; **they are not a proof over all integers**.

## Status and attribution

Classical modular arithmetic, CRT, wheel sieves, prime-factor bounds, and trial division underlie the procedure. The Fiduci terminology, dual-verdict presentation, visible interview count, and visual/encoding instruments are presented as this project’s framework. Some proposed box, rotation, and 3-D claims need sharper definitions or proofs; they are labeled accordingly in the expanded manuscript. The claim that fixed finite divisor guards eventually fail **is proved**; the stronger claim that no efficient deterministic primality algorithm exists is false (see AKS in the specification).
