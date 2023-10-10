# https://codeforces.com/problemset/problem/1374/B

from typing import List


def main() -> None:
    t: int = int(input())

    result: List[str] = []

    for _ in range(t):
        n: int = int(input())
        counter: int = 0
        while n > 1:
            if n % 6 == 0:
                n //= 6
                counter += 1
                continue
            if n % 2 == 0:
                counter = -1
                break
            n *= 2
            counter += 1

        result.append(counter)

    for r in result:
        print(r)


if __name__ == "__main__":
    main()

# 2 -> 4 -> 8 -> 16 -> 32 -> 64 -> 128
