import sys
N, X = map(int, sys.stdin.readline().split())
visitors = list(map(int, sys.stdin.readline().split()))
cur = sum(visitors[:X])
max_visitors = cur
max_count = 1
for i in range(X, N):
  cur = cur - visitors[i-X] + visitors[i]
  if cur > max_visitors:
    max_visitors = cur
    max_count = 1
  elif cur == max_visitors:
    max_count += 1
  
if max_visitors == 0:
  print("SAD")
else:
  print(max_visitors)
  print(max_count)