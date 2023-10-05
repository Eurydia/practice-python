# B9XP3X THANAKORN PHUTTHARAKSA


# 3.4, 3.6, 3.9, 3.10


# 3.4
def secret_number_game() -> None:
    secret_number = 777
    print(
        """\
+================================+
| Welcome to my game, muggle! |
| Enter an integer number |
| and guess what number I've |
| picked for you. |
| So, what is the secret number? |
+================================+
"""
    )
    while True:
        guessed: int = int(input("Enter a number: "))
        if guessed != secret_number:
            print("Ha ha! You're stuck in my loop!")
            continue

        print("Well done, muggle! You are free now")
        break


# 3.6
def collatz() -> None:
    n: int = int(input("Enter a number:"))
    steps: int = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1
        steps += 1
        print(n)
    print(f"steps= {steps}")


# 3.9
def get_unique_list() -> None:
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

    temp: list[int] = []
    for r in my_list:
        if r not in temp:
            temp.append(r)
    my_list = temp

    print("The list with unique elements only:")
    print(my_list)


# 3.10
def is_prime(n: int) -> bool:
    if n == 1:
        return False
    if n > 2 and n % 2 == 0:
        return False

    for divisor in range(2, n // 2):
        if n % divisor == 0:
            return False
    return True


def main() -> None:
    # secret_number_game()
    # collatz()
    # get_unique_list()
    for i in range(1, 20):
        if is_prime(i):
            print(i)


if __name__ == "__main__":
    main()
