# https://codeforces.com/problemset/problem/279/B

from typing import List


def main() -> None:
    read_input: List[int] = list(map(int, input().split()))
    books: List[int] = list(map(int, input().split()))

    n: int = read_input[0]
    t: int = read_input[1]
    offset_left: int = 0

    max_book: int = 0

    while offset_left < n:
        offset_right: int = n
        while sum(books[offset_left:offset_right]) > t:
            offset_right -= 1
        if (offset_right - offset_left) > max_book:
            max_book = offset_right - offset_left

        offset_left += 1

    print(max_book)


if __name__ == "__main__":
    main()
