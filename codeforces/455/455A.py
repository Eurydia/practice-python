# https://codeforces.com/problemset/problem/455/A

from typing import List, Dict, Set
from collections import Counter


def main() -> None:
    # n: int = int(input())
    # as_: List[int] = list(map(int, input().split()))
    n = (2,)
    as_ = [4, 2, 3, 2, 5]

    counter = Counter(as_)

    def solve(pivot: int, elements: List[int], score: int) -> int:
        if len(elements) == 0:
            return score

        max_score: int = counter[pivot] * pivot
        new_list: List[int] = [
            k for k in elements if k not in (pivot - 1, pivot, pivot + 1)
        ]

        for e in set(new_list):
            curr_score: int = solve(e, new_list, max_score)

            if curr_score > max_score:
                max_score = curr_score

        return max_score + score

    score_highest: int = -1

    for e in set(as_):
        score: int = solve(e, as_, 0)
        if score > score_highest:
            score_highest = score

    print(score_highest)


# 3 3 4 4 5
# 6 6 6 6 6 7 8 9 9 9 9

if __name__ == "__main__":
    main()
