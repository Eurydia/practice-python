# https://codeforces.com/problemset/problem/1850/A

from typing import List


def main() -> None:
    t: int = int(input())

    for _ in range(t):
        read_input: List[int] = list(map(int, input().split()))

        read_input.sort()

        if read_input[1] + read_input[2] >= 10:
            print("YES")
            continue

        print("NO")


if __name__ == "__main__":
    main()
