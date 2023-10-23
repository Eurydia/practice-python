# https://codeforces.com/problemset/problem/514/A

from typing import List


def main() -> None:
    x: str = input()

    result: str = ""

    for i, d_str in enumerate(x):
        d_int: int = int(d_str)

        if i == 0 and d_int == 9:
            result += d_str
            continue

        if d_int > 4:
            result += str(9 - d_int)
            continue
        result += d_str
    print(result)


if __name__ == "__main__":
    main()
