# https://codeforces.com/problemset/problem/451/B

from typing import List


def main() -> None:
    n: int = int(input())
    as_: List[int] = list(map(int, input().split()))

    l_ptr: int = 0
    r_ptr: int = 0

    for i in range(n - 1):
        if as_[i] > as_[i + 1]:
            l_ptr = i
            break

    for i in range(l_ptr, n - 1):
        if as_[i] < as_[i + 1]:
            r_ptr = i

    k = as_[l_ptr : r_ptr + 1]
    k.sort()

    if k != as_[l_ptr : r_ptr + 1]:
        print("NO")
        return
    print("YES")
    print(l_ptr + 1, r_ptr + 1)


if __name__ == "__main__":
    main()
