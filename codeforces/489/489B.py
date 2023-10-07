# https://codeforces.com/problemset/problem/489/B


from typing import List


def main() -> None:
    n: int = int(input())
    boy_skills: List[int] = list(map(int, input().split()))

    m: int = int(input())
    girl_skills: List[int] = list(map(int, input().split()))

    boy_skills.sort()
    girl_skills.sort()

    boy_index: int = 0
    girl_index: int = 0
    pairs_counter: int = 0

    while boy_index < n and girl_index < m:
        if (
            abs(boy_skills[boy_index] - girl_skills[girl_index])
            <= 1
        ):
            pairs_counter += 1
            boy_index += 1
            girl_index += 1
        elif boy_skills[boy_index] < girl_skills[girl_index]:
            boy_index += 1
        else:
            girl_index += 1

    print(pairs_counter)


if __name__ == "__main__":
    main()
