from itertools import product


def main() -> None:
    result = 10**6
    for perm in product(range(10), repeat=6):
        for i, e in enumerate(perm):
            if e == 4 and i < 4 and perm[i + 1] == 2:
                result -= 1

    print(result)


if __name__ == "__main__":
    main()
