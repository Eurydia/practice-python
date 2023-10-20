# https://codeforces.com/problemset/problem/1703/B

# from typing import List, Dict
from collections import Counter


def main() -> None:
    t: int = int(input())

    for _ in range(t):
        n: int = input()
        s: str = input()
        counter: Counter = Counter(s)
        print(sum(counter.values()) + len(counter.keys()))


if __name__ == "__main__":
    main()
