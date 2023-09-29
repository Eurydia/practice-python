# https://codeforces.com/problemset/problem/455/A

from typing import List, Dict

lookup: Dict[int, int] = {}


def compute_net_gain(ak: int) -> int:
    if ak not in lookup:
        return 0


def main() -> None:
    n: int = int(input())
    a: List[int] = list(map(int, input().split()))

    for ak in a:
        if ak not in lookup:
            lookup[ak] = ak
        else:
            lookup[ak] += ak


# 3 3 4 4 5
# 6 6 6 6 6 7 8 9 9 9 9

if __name__ == "__main__":
    main()
