# https://codeforces.com/problemset/problem/1426/A

from typing import List
from math import ceil


def main() -> None:
    t: int = int(input())

    for _ in range(t):
        read_input: List[int] = list(map(int, input().split()))
        n: int = read_input[0]
        x: int = read_input[1]

        if n in (1, 2):
            print(1)
            continue

        print(ceil((n - 2) / x) + 1)


if __name__ == "__main__":
    main()
