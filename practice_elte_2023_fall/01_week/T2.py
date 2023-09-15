# 40 hours / week
# 52 weeks / year


def main() -> None:
    hours: int = 10_000
    hours_per_year: int = 52 * 40
    years = hours / hours_per_year

    print(f"{years=}")


if __name__ == "__main__":
    main()
