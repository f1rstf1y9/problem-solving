from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y):
  stack = deque([(x, y)])
  while stack:
    x, y = stack.pop()
    color = grid[x][y]
    if color == "G":
      grid[x][y] = "R"
    
    for dx, dy in delta:
      nx, ny = x+dx, y+dy
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
        visited[nx][ny] = 1
        stack.append((nx, ny))

N = int(input())
grid = [list(input()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
not_weakness_cnt = weakness_cnt = 0

for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      visited[i][j] = True
      not_weakness_cnt += 1
      dfs(i, j)

visited = [[False]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      visited[i][j] = True
      weakness_cnt += 1
      dfs(i, j)

print(not_weakness_cnt, weakness_cnt)
