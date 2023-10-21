# https://codeforces.com/problemset/problem/1742/B

from typing import List, Set


def main() -> None:
    t: int = int(input())
    rs: List[str] = []
    for _ in range(t):
        n: int = int(input())
        as_: List[str] = input().split()

        if n == 1:
            rs.append("YES")
            continue

        seen: Set[str] = set()
        for a in as_:
            if a in seen:
                rs.append("NO")
                break
            seen.add(a)
        else:
            rs.append("YES")

    for r in rs:
        print(r)


if __name__ == "__main__":
    main()
