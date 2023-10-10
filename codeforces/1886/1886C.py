# https://codeforces.com/contest/1886/problem/0

from typing import List


def main() -> None:
    t: int = int(input())

    result: List[str] = []

    for _ in range(t):
        s_one: List[str] = list(input())
        n: int = int(input())
        s_curr: List[str] = [*s_one]

        while len(s_curr) < n:
            if len(s_one) > 1:
                s_one.remove(max(s_one))

            s_curr.extend(s_one)
        result.append(s_curr[n - 1])

    for r in result:
        print(r, end="")


if __name__ == "__main__":
    main()
