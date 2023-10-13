# https://codeforces.com/contest/1881/problem/B

from typing import Set, List


def main() -> None:
    t: int = int(input())
    result: List[str] = []

    for _ in range(t):
        xs: Set[int] = set(map(int, input().split()))

        target: int = min(xs)

        if any(x % target != 0 for x in xs):
            result.append("NO")
            continue

        cuts_needed: int = 0
        for x in xs:
            cuts_needed += (x // target) - 1

        if cuts_needed > 3:
            result.append("NO")
            continue

        result.append("YES")

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
