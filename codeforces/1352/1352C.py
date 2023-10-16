# https://codeforces.com/problemset/problem/1352/C

from typing import List
from math import floor, ceil

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


def solve(k: int, n: int) -> int:
    # if k == 1:
    #     return 1
    # if n == 2:
    #     return (2 * k) - 1

    # return k + ((k - 1) // (n - 1))

    bn: int = ceil(n / (k - 1))
    cn: int = k - (n - ((k - 1) * (bn - 1)))

    return (k * bn) - cn


def main() -> None:
    t: int = int(input())
    result: List[int] = []
    for _ in range(t):
        nk: List[int] = list(map(int, input().split()))
        k: int = nk[0]
        n: int = nk[1]

        result.append(solve(k, n))

    for r in result:
        print(r)


if __name__ == "__main__":
    main()

    # k = 3

    # c1 = 2
    # # c1 = 3 - 1
    # # c1 = 3 - floor(1/1)

    # c2 = 1
    # # c2 = 3 - 2
    # # c2 = 3 - floor(2/1)

    # c3 = 2
    # # c3 = 3 - 1
    # # c3 = 3 - floor(3/2)

    # c4 = 1
    # # c4 = 3 - 2
    # # c4 = 3 - floor(4/2)

    # c5 = 2
    # # c5 = 3 - 1
    # # c5 = 3 - floor(5/3)


# k = 7

# c1 = 6
# # c1 = 7 - 1

# c2 = 5
# # c2 = 7 - 2

# c6 = 1
# # c2 = 7 - 6

# c7 = 6
# c7 = 7 - 1

# c8 = 5
# c8 = 7 - 2
