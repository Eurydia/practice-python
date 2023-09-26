# https://codeforces.com/problemset/problem/339/B


def main() -> None:
    n: int = int(input().split(" ")[0])

    houses: tuple[int, ...] = tuple(map(int, input().split(" ")))

    steps: int = 0
    curr_house: int = 1
    for next_house in houses:
        if curr_house > next_house:
            steps += n - curr_house + 1
            curr_house = 1

        steps += next_house - curr_house
        curr_house = next_house
    print(steps)


if __name__ == "__main__":
    main()
