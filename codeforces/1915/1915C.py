# https://codeforces.com/problemset/problem/1915/C
import math
def main():
  t = int(input())
  r = []
  for _ in range(t):
    _ = input()
    items = input().split(" ")
    total = sum([int(item) for item in items])
    r.append(math.sqrt(total).is_integer())

  print("\n".join(["yes" if res else "no" for res in r]))

if __name__ == "__main__":
  main()