# https://codeforces.com/problemset/problem/520/B

from typing import List


def main() -> None:
    nm: List[int] = list(map(int, input().split()))
    n: int = nm[0]
    m: int = nm[1]
    steps: int = 0
    while n != m:
        if m > n:
            if m % 2 == 0:
                m //= 2
                steps += 1
            else:
                m += 1
                steps += 1
        else:
            diff: int = n - m
            m += diff
            steps += diff
    print(steps)


if __name__ == "__main__":
    main()
