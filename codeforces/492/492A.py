# https://codeforces.com/problemset/problem/492/A


def main() -> None:
    n: int = int(input())

    levels: int = 0
    curr_cubes_needed: int = 1
    next_cubes_needed: int = 1
    while curr_cubes_needed <= n:
        levels += 1
        n -= curr_cubes_needed

        next_cubes_needed += 1
        curr_cubes_needed += next_cubes_needed
    print(levels)

    # 1 3 6 10


if __name__ == "__main__":
    main()
