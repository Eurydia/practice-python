# https://codeforces.com/problemset/problem/489/C

from typing import List


def main() -> None:
    read_input: List[int] = list(map(int, input().split()))
    m: int = read_input[0]
    s: int = read_input[1]

    # result_largest = -1

    # m = 1, 0 <= s <= 9
    # m = 2, 1 <= s <= 18
    # m = 3, 1 <= s <= 27

    if m == 1 and s > 9:
        print(-1, -1)
        return

    if m >= 2 and ((s < 1) or (s > (m * 9))):
        print(-1, -1)
        return

    largest: List[int] = [0 for _ in range(m)]
    leftover: int = s

    for i in range(m):
        if leftover <= 9:
            largest[i] = leftover
            break
        largest[i] = 9
        leftover -= 9

    smallest: List[int] = [0 for _ in range(m - 1)]
    smallest.append(1)
    leftover: int = s - 1
    for i in range(m):
        if leftover > 9:
            smallest[i] += 9
            leftover -= 9
        else:
            smallest[i] += leftover
            leftover = 0
    smallest.reverse()

    result_largest: int = int("".join(map(str, largest)))
    result_smallest: int = int("".join(map(str, smallest)))

    print(
        result_smallest,
        result_largest,
    )


if __name__ == "__main__":
    main()
