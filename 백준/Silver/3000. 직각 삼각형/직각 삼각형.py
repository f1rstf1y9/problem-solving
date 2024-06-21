import sys

input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

x_point_map = {}
y_point_map = {}
count = 0

for x, y in points:
  x_point_map.setdefault(x, []).append(y)
  y_point_map.setdefault(y, []).append(x)

for x, y in points:
  count += (len(x_point_map[x])-1) * (len(y_point_map[y])-1)

print(count)