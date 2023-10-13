# https://codeforces.com/contest/1881/problem/A

from typing import List


def main() -> None:
    t: int = int(input())
    result: List[int] = []
    for _ in range(t):
        read_input: List[int] = list(map(int, input().split()))
        n: int = read_input[0]
        m: int = read_input[1]

        x: str = input()
        s: str = input()

        counter: int = 0
        while n < m:
            x += x
            n += n
            counter += 1

        if s in x:
            result.append(counter)
            continue

        x += x
        counter += 1
        if s in x:
            result.append(counter)
            continue
        result.append(-1)
    for r in result:
        print(r)


if __name__ == "__main__":
    main()
