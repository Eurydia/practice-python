def main() -> None:
    VOWELS: set[str] = set("AEIOU")

    word: str = input("enter a word:")

    word_without_vowels: str = ""
    for char in word:
        if not (char.upper() in VOWELS):
            word_without_vowels += char
    print(word_without_vowels)


if __name__ == "__main__":
    main()
