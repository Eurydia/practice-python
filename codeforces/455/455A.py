# https://codeforces.com/problemset/problem/455/A

from typing import List, Dict

lookup: Dict[int, int] = {}


def solve(n: int) -> int:
    # if n not in lookup:
    #     return 0

    if n == 1:
        if n in lookup:
            return lookup[1]
        return 0

    return max(solve(n - 1), solve(n - 2) + lookup[n] * n)


def main() -> None:
    n: int = int(input())
    a: List[int] = list(map(int, input().split()))

    for ak in a:
        if ak not in lookup:
            lookup[ak] = 1
        else:
            lookup[ak] += 1
    print(solve(n))


# 3 3 4 4 5
# 6 6 6 6 6 7 8 9 9 9 9

if __name__ == "__main__":
    main()
