# https://codeforces.com/problemset/problem/731/A


def to_ascii(char: str) -> int:
    return ord(char) - ord("a")


def main() -> None:
    s: str = input()

    curr_char: str = "a"
    rotations: int = 0
    for char in s:
        turn_right: int = max(
            to_ascii(char) - to_ascii(curr_char),
            to_ascii(curr_char) - to_ascii(char),
        )
        turn_left: int = 26 - turn_right

        rotations += min(turn_right, turn_left)
        curr_char = char

    print(rotations)


if __name__ == "__main__":
    main()
