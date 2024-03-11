import sys

while True:
  a, b, c = map(int, sys.stdin.readline().split())
  if (a, b, c) == (0, 0, 0):
    break
  if max(a, b, c) >= sum((a, b, c)) - max(a, b, c):
    print("Invalid")
  elif a == b == c:
    print("Equilateral")
  elif a != b and a != c and b != c:
        print("Scalene")     
  else:
    print("Isosceles")