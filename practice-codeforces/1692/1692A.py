t = int(input())

for _ in range(t):

    [a, *bcd] = list(map(int, input().split(" ")))

    in_front = 0
    for i in bcd:
        if i > a:
            in_front += 1

    print(in_front)
