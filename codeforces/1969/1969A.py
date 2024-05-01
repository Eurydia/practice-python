# https://codeforces.com/contest/1969/problem/A


t = int(input())
for _ in range(t):
    _ = input()
    row = list(map(int, input().split(" ")))
    found = False
    result = 3
    for index, item in enumerate(row, 1):
        found = found or (index == row[item - 1])
        if found:
            result = 2
            break

    print(result)
