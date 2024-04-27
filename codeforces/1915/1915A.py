# https://codeforces.com/problemset/problem/1915/A

def main():
  t = int(input())
  r = []
  for _ in range(t):
    a,b,c = input().split(" ")
    if a == b:
      r.append(c)
    elif a == c:
      r.append(b)
    else:
      r.append(a)
  print("\n".join(r))
if __name__ == "__main__":
  main()