# https://codeforces.com/problemset/problem/935/A


def main() -> None:
    n: int = int(input())
    counter: int = 1
    for l in range(2, n + 1):
        if ((n - l) > 0) and ((n - l) % l == 0):
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
