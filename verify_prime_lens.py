#!/usr/bin/env python3
"""Reproducible finite checks for the Fiduci Prime Lens specification.

Only the Python standard library is used. A finite test is not a proof of a
universal mathematical claim; the proof of exactness is in the manuscript.
"""

from math import isqrt


def lens(n: int) -> tuple[bool, int, int | None]:
    """Return (prime, candidate_interviews, first_divisor).

    This variant does not use the optional under-32 lookup table.
    The wall checks do not increment candidate_interviews.
    """
    if n < 2:
        return False, 0, None
    if n in (2, 3):
        return True, 0, None
    if n % 2 == 0:
        return False, 0, 2
    if n % 3 == 0:
        return False, 0, 3
    interviews = 0
    limit = isqrt(n)
    for d in range(5, limit + 1, 6):
        interviews += 1
        if n % d == 0:
            return False, interviews, d
        if d + 2 <= limit:
            interviews += 1
            if n % (d + 2) == 0:
                return False, interviews, d + 2
    return True, interviews, None


def eratosthenes(limit: int) -> bytearray:
    """Independent reference: sieve prime flags for 0..limit inclusive."""
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return flags


def digit_chain(n: int) -> list[int]:
    chain = []
    if n >= 10:
        n = sum(map(int, str(n)))
        chain.append(n)
    while n > 32:
        n = sum(map(int, str(n)))
        chain.append(n)
    return chain or [n]


def main() -> None:
    limit = 1_000_000
    reference = eratosthenes(limit)
    errors = [n for n in range(limit + 1) if lens(n)[0] != bool(reference[n])]
    print(f"0..{limit}: {limit + 1} inputs, {sum(reference)} primes, "
          f"{len(errors)} mismatches")
    assert not errors, f"first mismatches: {errors[:10]}"

    expected = {
        25: (False, 1, 5),
        211: (True, 4, None),
        437: (False, 6, 19),
        997: (True, 10, None),
        2207: (True, 14, None),
        486385: (False, 1, 5),
        1000001: (False, 33, 101),
        999999999989: (True, 333332, None),
    }
    for n, verdict in expected.items():
        actual = lens(n)
        print(f"{n}: {actual}, digit chain {digit_chain(n)}")
        assert actual == verdict, (n, actual, verdict)

    units24 = [r for r in range(24) if r % 2 and r % 3]
    assert units24 == [1, 5, 7, 11, 13, 17, 19, 23]
    assert all(r * r % 24 == 1 for r in units24)
    assert all(
        n % 3 == sum(map(int, str(n))) % 3 for n in range(limit + 1)
    )
    assert all(
        (n % 12 in (1, 5, 7, 11)) == (n % 2 != 0 and n % 3 != 0)
        for n in range(limit + 1)
    )
    primes = [p for p in range(limit + 1) if reference[p]]
    assert all(
        p * p % 24 == 1 and (p * p + 2) % 3 == 0
        and (p * p - 2) % 6 == 5
        for p in primes if p > 3
    )
    for p in (5, 7, 11, 13):
        # Earlier prime guards cannot divide the first unguarded square.
        assert all((p * p) % q != 0 for q in primes if q < p)
    odd_primes = [p for p in range(3, limit + 1, 2) if reference[p]]
    assert all((b - a) % 2 == 0 for a, b in zip(odd_primes, odd_primes[1:]))
    print("Digit sums, base-12 addresses, prime squares, fixed guards, "
          "octet squares, and odd-prime-gap parity checks passed.")

    supplied_gaps = [6, 4, 2, 4, 2, 4, 6, 2]
    cyclic_octet_gaps = [
        b - a for a, b in zip(units24, units24[1:] + [units24[0] + 24])
    ]
    units30 = [r for r in range(30) if r % 2 and r % 3 and r % 5]
    cyclic_wheel30_gaps = [
        b - a for a, b in zip(units30, units30[1:] + [units30[0] + 30])
    ]
    assert units30 == [1, 7, 11, 13, 17, 19, 23, 29]
    assert cyclic_wheel30_gaps == supplied_gaps
    assert sum(supplied_gaps) == 30 != sum(cyclic_octet_gaps)
    assert cyclic_octet_gaps != supplied_gaps
    opcodes = [3, 7, 11, 13, 17, 19, 23, 29]
    assert [b - a for a, b in zip(opcodes, opcodes[1:])] != supplied_gaps[:7]
    print(f"Mod-24 octet gaps: {cyclic_octet_gaps}; mod-30 wheel gaps: "
          f"{cyclic_wheel30_gaps} (exact supplied G).")
    for a, b in ((3, 5), (7, 11)):
        gap = b - a
        print(f"Box reading {a}..{b}: gap {gap}, inclusive seats {gap + 1}, "
              f"strictly interior seats {gap - 1}.")


if __name__ == "__main__":
    main()
