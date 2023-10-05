# https://codeforces.com/problemset/problem/1535/A

from typing import List


def main() -> None:
    t: int = int(input())

    result: List[bool] = []
    for _ in range(t):
        abcd: List[int] = list(map(int, input().split()))

        ab_pair: int = max(abcd[0], abcd[1])
        cd_pair: int = max(abcd[2], abcd[3])

        finals: List[int] = [
            max(abcd),
        ]
        abcd.remove(max(abcd))
        finals.append(max(abcd))

        result.append(ab_pair in finals and cd_pair in finals)

    for r in result:
        if r:
            print("YES")
        else:
            print("NO")


# 3 3 4 4 5
# 6 6 6 6 6 7 8 9 9 9 9

if __name__ == "__main__":
    main()
