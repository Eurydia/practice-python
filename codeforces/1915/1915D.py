# https://codeforces.com/problemset/problem/1915/D

# CV -> CV.CV
# CVCCV -> CVC.CV
# CVCCVC


def main():
    t = int(input())
    r = []

    V = "ae"

    for _ in range(t):
        _ = input()
        word: "str" = input()
        length: "int" = len(word)

        syllables: "list[list[str]]" = []
        i = 0
        while i < length - 3:
            if word[i + 3] in V:
                curr = word[i : i + 2]
                i += 2
            else:
                curr = word[i : i + 3]
                i += 3
            syllables.append(curr)
        syllables.append(word[i:])
        r.append(".".join(syllables))

    print("\n".join(r))


if __name__ == "__main__":
    main()
