t = int(input())
r = []

lookup = tuple(
    filter(
        lambda x: str(x)[-1] != "3",
        filter(
            lambda x: x % 3 != 0,
            (i for i in range(1, 1667)),
        ),
    )
)

while t > 0:
    k: int = int(input())
    r.append(lookup[k - 1])

    t -= 1


for i in r:
    print(i)
