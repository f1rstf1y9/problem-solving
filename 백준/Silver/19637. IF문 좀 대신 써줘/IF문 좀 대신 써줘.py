import sys
N, M = map(int, sys.stdin.readline().split())

titles = []
for i in range(N):
  title, power = sys.stdin.readline().rstrip().split()
  power = int(power)
  titles.append((title, power))

for i in range(M):
  cur = int(sys.stdin.readline())
  l, r = 0, N
  res = 0
  while l <= r:
    mid = (l+r)//2
    if titles[mid][1] >= cur:
      res = mid
      r = mid - 1
    else:
      l = mid + 1
  print(titles[res][0])