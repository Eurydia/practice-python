# https://codeforces.com/problemset/problem/1352/C

from typing import List

# from math import loor


# (8, 7)
# 1 2 3 4 5 6 7
#             ^
# k + (7 // 8)


# (8, 11)
# 1 2 3 4 5 6 7 9 10 11 12
#                       ^
# a(1) = 1
# a(2) = 2
# ...
# a(6) = 6
# a(7) = 7
# a(8) = 9 = n + (n // 8)
# a(11) = 11 + (n // 8)
# a(15) = 15 + (n // 8) = 17
# a(x) = x + (x // y)


# (2, 11)
# 1 3 5 7 9 11 13 15 17 19 21
# a(x) = x + (x // y)
# a(3) = 3 + (3 // 2) = 4

# n = 2
# (2k - 1); k >= 1

# n = 3
# 1 2 4 5 7 8 10 11
# (3k - 2); k >= 1
# a(1) = 1
# a(2) = 2
# a(3) = 4 = 3 + ceil(3/3)
# a(4) = 5 = 4 + ceil(4/3)
# a(5) = 7 = 5 + ceil(5/3)
# a(6) = 8 = 6 + ceil(6/3)
#


# (7 97)


def solve(n: int, k: int) -> int:
    if k == 1:
        return 1
    if n == 2:
        return (2 * k) - 1

    return k + ((k - 1) // (n - 1))

    # not_divisible: List[int] = []
    # curr: int = k
    # while len(not_divisible) < k:
    #     if curr % n != 0:
    #         not_divisible.append(curr)
    #     curr += 1
    # return not_divisible[len(not_divisible) - 1]

    # counter: int = 0
    # curr: int = 0
    # while counter < k:
    #     curr += 1
    #     if curr % n != 0:
    #         counter += 1
    # return curr

    # return term + (term // modulo)
    # ls: List[List[int]] = [[x, x + 1] for x in range(1, k + 2, 2)]
    # if k % 2 == 1:
    #     return ls[len(ls) - 1][0]
    # return ls[len(ls) - 2][1]


def main() -> None:
    t: int = int(input())
    result: List[int] = []
    for _ in range(t):
        nk: List[int] = list(map(int, input().split()))
        n: int = nk[0]
        k: int = nk[1]

        result.append(solve(n, k))

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
