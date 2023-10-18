# https://codeforces.com/problemset/problem/1676/B

from typing import Tuple


def main() -> None:
    t: int = int(input())
    # res: list[int] = []
    for _ in range(t):
        _: int = int(input())
        as_: Tuple[int] = tuple(map(int, input().split()))
        min_candies: int = min(as_)

        # res.append(sum(a - min_candies for a in as_))
        print(sum(a - min_candies for a in as_))

    # for r in res:
    #     print(r)


if __name__ == "__main__":
    main()
