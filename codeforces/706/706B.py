# https://codeforces.com/problemset/problem/706/B

from typing import List


def upperbound(m: int, xs: List[int]) -> int:
    low: int = 0
    high: int = len(xs) - 1

    while low < high:
        mid: int = low + ((high - low) // 2)
        if xs[mid] <= m:
            low = mid + 1
        else:
            high = mid

    if xs[low] <= m:
        return low + 1

    return low


def main() -> None:
    n: int = int(input())
    xs: List[int] = [int(x) for x in input().split()]
    q: int = int(input())
    ms: List[int] = [int(input()) for _ in range(q)]

    xs.sort()

    for m in ms:
        print(upperbound(m, xs))


if __name__ == "__main__":
    main()
