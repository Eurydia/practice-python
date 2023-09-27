# https://codeforces.com/problemset/problem/706/B

from typing import List


def main() -> None:
    n: int = int(input())
    xs: List[int] = [int(x) for x in input().split()]
    q: int = int(input())
    ms: List[int] = [int(input()) for _ in range(q)]

    prefix_sum: List[int] = [0 for _ in range(n)]
    for x in xs:
        prefix_sum[x] += 1


if __name__ == "__main__":
    main()
