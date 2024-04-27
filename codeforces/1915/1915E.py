# https://codeforces.com/problemset/problem/1915/E

from itertools import product


def main():
    t = int(input())
    r = []

    for _ in range(t):
        n = int(input())
        items = input().split(" ")
        xs = list(map(int, items))

        for s in range(n):
            for size in range(2, n - s)
            odd = 0
            even = 0
            for i, x in enumerate(xs[s : s + size]):
                if i % 2 == 0:
                    even += x
                else:
                    odd += x
            found = odd == even
            if found:
                break
        r.append(found)

    print("\n".join("yes" if res else "no" for res in r))


if __name__ == "__main__":
    main()
