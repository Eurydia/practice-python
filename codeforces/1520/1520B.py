# https://codeforces.com/problemset/problem/1520/B

from typing import List


def main() -> None:
    t: int = int(input())

    result: List[int] = []

    for _ in range(t):
        n: int = int(input())

        # 10 -> 9
        # 20 -> 10
        # 30 -> 11
        # 100 -> 18

        # 111 -> 19
        # 222 -> 20
        # 1000 -> 27

        # 101 -> 9 + 9 + ?
        # 112 -> 9 + 9 + ? (1)

        if n < 10:
            result.append(n)
            continue
        # n = 100 -> 18
        mover: int = 100
        counter: int = 9
        while n >= mover:
            mover *= 10
            counter += 9

        # 100
        base_line: int = int("".join("1" for _ in str(n)))
        curr_step: int = base_line
        while curr_step <= n:
            counter += 1
            curr_step += base_line

        result.append(counter)

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
