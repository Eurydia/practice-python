# https://codeforces.com/problemset/problem/1722/B


def main() -> None:
    t: int = int(input())
    for _ in range(t):
        _ = input()
        str_a: str = input().replace("G", "B")
        str_b: str = input().replace("G", "B")

        if str_a == str_b:
            print("Yes")
            continue
        print("No")


if __name__ == "__main__":
    main()
