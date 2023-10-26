# https://codeforces.com/problemset/problem/1772/A


def main() -> None:
    t: int = int(input())

    for _ in range(t):
        expression: str = input()

        a, b = expression.split("+")

        print(int(a) + int(b))


if __name__ == "__main__":
    main()
