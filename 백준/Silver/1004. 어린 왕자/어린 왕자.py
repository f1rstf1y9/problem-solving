import math
T = int(input())
for _ in range(T):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  count = 0
  for _ in range(n):
    x, y, r = map(int, input().split())
    a, b = math.sqrt((x1-x)**2+(y1-y)**2) <= r, math.sqrt((x2-x)**2+(y2-y)**2) <= r
    if a and b:
      continue
    if a:
      count += 1
    if b:
      count += 1
  print(count)