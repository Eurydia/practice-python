# https://codeforces.com/problemset/problem/1760/A

from typing import List


def main() -> None:
    t: int = int(input())

    for _ in range(t):
        abc: List[int] = list(map(int, input().split()))
        abc.sort()

        print(abc[1])


if __name__ == "__main__":
    main()
