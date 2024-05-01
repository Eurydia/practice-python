# https://codeforces.com/contest/1969/problem/B
# 01101001 -- "+3" -> 00111001 "+4" -> 00011101 ->4
#           +2         +4           +4          +4
# 01101001 -> 01110001 -> 00111001 ->  00011101 -> 00001111

# 0        +3          +2          +2          +3          +3
# 01101001 -> 00111001 -> 00110101 -> 00110011 -> 00011011 -> 0001111
t = int(input())
for _ in range(t):

    row = input()
    curr = [ch for ch in row]
    target = curr.copy()
    target.sort()

    moves = 0
    while curr != target:
        left = curr.index("1")
        right = curr.index("0", left)

        curr[left] = "0"
        curr[left + 1 : right + 1] = "1" * (right - left)
        moves += right - left + 1
    print(moves)
