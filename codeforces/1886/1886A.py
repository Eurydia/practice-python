# https://codeforces.com/contest/1886/problem/0

from typing import List


def solve(n: int) -> List[int]:
    for x in range(1, n + 1):
        if x % 3 == 0:
            continue
        for y in range(2, n - x + 1):
            if y % 3 == 0:
                continue

            if x == y:
                continue

            z: int = n - x - y
            if z % 3 == 0:
                continue

            if z in (x, y):
                continue

            return [x, y, z]
    return [-1, -1, -1]


def main() -> None:
    t: int = int(input())

    result: List[List[int]] = []

    for _ in range(t):
        n: int = int(input())
        result.append(solve(n))

    for r in result:
        if r == [-1, -1, -1]:
            print("NO")
            continue
        print("YES")
        print(" ".join(map(str, r)))


if __name__ == "__main__":
    main()
