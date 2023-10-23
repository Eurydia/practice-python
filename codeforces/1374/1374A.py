# https://codeforces.com/problemset/problem/1374/C


def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        s: str = input()

        moves_needed: int = 0
        current_value: int = 0
        for c in s:
            if c == "(":
                current_value -= 1
                continue

            current_value += 1

            if current_value > moves_needed:
                moves_needed = current_value
        print(moves_needed)


if __name__ == "__main__":
    main()
