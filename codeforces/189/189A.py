# https://codeforces.com/problemset/problem/189/A

from typing import List


def main() -> None:
    [n, a, b, c] = list(map(int, input().split()))

    ks: List[int] = [a, b, c]
    ks.sort()

    longest = 0
    for kx in range((n // ks[2]) + 1):
        kx_len: int = kx * ks[2]

        for ky in range((n // ks[1]) + 1):
            ky_len: int = ky * ks[1]

            if ((n - kx_len - ky_len) % ks[0]) == 0:
                kz: int = (n - kx_len - ky_len) // ks[0]

                longest = max(
                    kx + ky + kz,
                    longest,
                )
                break

    print(longest)


if __name__ == "__main__":
    main()
