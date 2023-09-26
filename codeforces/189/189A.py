# https://codeforces.com/problemset/problem/189/A


def main() -> None:
    [n, a, b, c] = list(map(int, input().split(" ")))

    min_len: int = min(a, b, c)
    med_len: int = min(max(a, b), max(b, c))
    max_len: int = max(a, b, c)

    def cut(
        curr_len: int,
        curr_pieces: int,
    ) -> int:
        if curr_len - min_len >= 0:
            return cut(
                curr_len - min_len,
                curr_pieces + 1,
            )
        if curr_len - med_len >= 0:
            return cut(
                curr_len - med_len,
                curr_pieces + 1,
            )
        if curr_len - max_len >= 0:
            return cut(
                curr_len - max_len,
                curr_pieces + 1,
            )
        return curr_pieces

    print(cut(n, 0))


if __name__ == "__main__":
    main()
