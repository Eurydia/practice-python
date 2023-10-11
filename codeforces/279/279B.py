# https://codeforces.com/problemset/problem/279/B

from typing import List


def main() -> None:
    read_input: List[int] = list(map(int, input().split()))
    books: List[int] = list(map(int, input().split()))

    n: int = read_input[0]
    t: int = read_input[1]

    total_time: int = sum(books)
    total_books: int = n

    left: int = 0
    right: int = n - 1

    while total_time > t:
        book_left: int = books[left]
        book_right: int = books[right]
        total_books -= 1

        if book_left > book_right:
            left += 1
            total_time -= book_left
            continue
        right -= 1
        total_time -= book_right

    print(total_books)


if __name__ == "__main__":
    main()
