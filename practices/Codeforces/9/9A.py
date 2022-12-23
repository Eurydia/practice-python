from math import gcd

[y, w] = map(int, input().split(" "))

winning_chance = 7 - max(y, w)

divider = gcd(winning_chance, 6)

print(f"{winning_chance/divider:.0f}/{6/divider:.0f}")
