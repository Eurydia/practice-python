def main() -> None:
    beatles: list[str] = []
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harriso")

    for _ in range(2):
        beatles.append(input("add a band member"))

    del beatles[3]
    del beatles[4]
    beatles.insert("Ringo Starr")


if __name__ == "__main__":
    main()
