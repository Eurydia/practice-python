# https://codeforces.com/problemset/problem/1807/A

from typing import List


def main() -> None:
    t: int = int(input())

    for _ in range(t):
        abc: List[int] = list(map(int, input().split()))

        if abc[0] + abc[1] == abc[2]:
            print("+")
        else:
            print("-")


if __name__ == "__main__":
    main()
