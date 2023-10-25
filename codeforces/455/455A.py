# https://codeforces.com/problemset/problem/455/A

from typing import List, Dict
from collections import Counter


def solve(as_: List[int], score: int) -> int:
    if len(as_) == 0:
        return score

    new_list: List[int] = []

    target: int = as_[0]
    current_score: int = score
    for a in as_:
        if a == target:
            current_score += a
            continue
        if a in (target - 1, target + 1):
            continue
        new_list.append(a)

    return solve(new_list, current_score)


def main() -> None:
    n: int = int(input())
    as_: List[int] = list(map(int, input().split()))
    print(solve(as_, 0))


# 3 3 4 4 5
# 6 6 6 6 6 7 8 9 9 9 9

if __name__ == "__main__":
    main()
