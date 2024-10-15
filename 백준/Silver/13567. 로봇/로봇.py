import sys
input = sys.stdin.readline

M, n = map(int, input().split())

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = 0, 0
dir_idx = 0

orders = [input().split() for _ in range(n)]

for order, order_num in orders:
  order_num = int(order_num)
  if order == "TURN":
    dir_idx = (dir_idx-1)%4 if order_num else (dir_idx+1)%4
  else:
    dx, dy = order_num * directions[dir_idx][0], order_num * directions[dir_idx][1]
    nx, ny = x + dx, y + dy
    if not (0 <= nx <= M and 0 <= ny <= M):
      print(-1)
      break
    x, y = nx, ny
else:
  print(x, y)