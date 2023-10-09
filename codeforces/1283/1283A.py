# https://codeforces.com/problemset/problem/1283/A

from typing import List


def main() -> None:
    t: int = int(input())

    MIDNIGHT: int = 24 * 60

    result: List[int] = []
    while t > 0:
        t -= 1
        read_input: List[int] = list(map(int, input().split()))
        h: int = read_input[0]
        m: int = read_input[1]

        result.append(MIDNIGHT - (h * 60) - m)

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
