# https://codeforces.com/problemset/problem/1915/B

def main():
  t = int(input())
  r = []
  for _ in range(t):
    for _ in range(3):
      row = input()
      if "?" not in row:
        continue
      for char in "ABC":
        if char not in row:
          r.append(char)
  print("\n".join(r))

if __name__ == "__main__":
  main()