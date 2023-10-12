# https://codeforces.com/problemset/problem/1722/A


def main() -> None:
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        s: str = input()

        if n != 5:
            print("NO")
            continue

        if set(s) == set("Timur"):
            print("YES")
            continue

        print("No")


if __name__ == "__main__":
    main()
