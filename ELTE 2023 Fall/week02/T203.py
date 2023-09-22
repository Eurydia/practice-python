def main() -> None:
    john: int = 3
    mary: int = 5
    adam: int = 6

    print(john, mary, adam, sep=",")

    total_appls: int = john + mary + adam
    print(f"{total_appls=}")


if __name__ == "__main__":
    main()
