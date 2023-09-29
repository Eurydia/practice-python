# https://codeforces.com/problemset/problem/1791/A

from typing import Set


def main() -> None:
    SET: Set[str] = set(char for char in "codeforces")

    for _ in range(int(input())):
        char: str = input()
        print("YES" if char in SET else "NO")


if __name__ == "__main__":
    main()
