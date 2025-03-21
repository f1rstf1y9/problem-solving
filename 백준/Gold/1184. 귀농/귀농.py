from collections import defaultdict

import sys
input = sys.stdin.readline

N = int(input())
profit = [list(map(int, input().split())) for _ in range(N)]

prefix_profit = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, N+1):
    prefix_profit[i][j] = prefix_profit[i-1][j] + prefix_profit[i][j-1] - prefix_profit[i-1][j-1] + profit[i-1][j-1]

left_bottom_rectangle = [[defaultdict(int) for _ in range(N+1)] for _ in range(N+1)]
left_top_rectangle = [[defaultdict(int) for _ in range(N+1)] for _ in range(N+1)]

for x1 in range(N):
  for y1 in range(N):
    for x2 in range(x1+1, N+1):
      for y2 in range(y1+1, N+1):
        current_rectangle = prefix_profit[x2][y2] - prefix_profit[x1][y2] - prefix_profit[x2][y1] + prefix_profit[x1][y1]
        left_bottom_rectangle[x2][y1][current_rectangle] += 1
        left_top_rectangle[x1][y1][current_rectangle] += 1

count = 0

for x1 in range(N):
  for y1 in range(N):
    for x2 in range(x1+1, N+1):
      for y2 in range(y1+1, N+1):
        current_rectangle = prefix_profit[x2][y2] - prefix_profit[x1][y2] - prefix_profit[x2][y1] + prefix_profit[x1][y1]
        count += left_bottom_rectangle[x1][y2][current_rectangle]
        count += left_top_rectangle[x2][y2][current_rectangle]

print(count)