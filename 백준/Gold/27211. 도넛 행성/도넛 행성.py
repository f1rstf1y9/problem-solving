from collections import deque

N, M = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(N)]


visited = [[0]*M for _ in range(N)]

def dfs(x, y):
  stack = deque([(x,y)])
  while stack:
    x, y = stack.pop()
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
      nx, ny = x+dx, y+dy
      if nx < 0 or nx >= N:
        nx %= N
      if ny < 0 or ny >= M:
        ny %= M
      if not planet[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        stack.append((nx, ny))

count = 0
for i in range(N):
  for j in range(M):
    if not planet[i][j] and not visited[i][j]:
      visited[i][j] = 1
      dfs(i, j)
      count += 1

print(count)