# https://codeforces.com/problemset/problem/80/A


from typing import Dict


# def is_prime(k: int) -> bool:
#     for d in range(2, (k // 2) + 1):
#         if k % d == 0:
#             return False
#     return True


# def next_prime(n: int) -> int:
#     curr: int = n + 1

#     while not is_prime(curr):
#         curr += 1
#     return curr


lookup: Dict[int, int] = {
    2: 3,
    3: 5,
    5: 7,
    7: 11,
    11: 13,
    13: 17,
    17: 19,
    19: 23,
    23: 29,
    29: 31,
    31: 37,
    37: 41,
    41: 43,
    43: 47,
    47: 53,
}


def main() -> None:
    [n, m] = list(map(int, input().split()))
    if lookup[n] == m:
        print("YES")
    else:
        print("NO")
    # lookup: Dict[int, int] = {}
    # for n in range(2, 50):
    #     if is_prime(n):
    #         lookup[n] = next_prime(n)
    # print(lookup)


if __name__ == "__main__":
    main()
