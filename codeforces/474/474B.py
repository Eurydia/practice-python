# https://codeforces.com/problemset/problem/474/B


from typing import List, Dict


def main() -> None:
    n: int = int(input())
    as_: List[int] = list(map(int, input().split()))
    m: int = int(input())
    qs: List[int] = list(map(int, input().split()))

    LOOKUP: Dict[int, int] = {}

    counter: int = 1
    for p, a in enumerate(as_, 1):
        for _ in range(a):
            LOOKUP[counter] = p
            counter += 1

    for q in qs:
        print(LOOKUP[q])


if __name__ == "__main__":
    main()
