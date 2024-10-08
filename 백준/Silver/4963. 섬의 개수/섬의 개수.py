import sys
sys.setrecursionlimit(10 ** 5)

delta = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
def dfs(x, y):
  for dx, dy in delta:
    nx, ny = x+dx, y+dy
    if 0 <= nx < h and 0 <= ny < w and map_data[nx][ny]:
      map_data[nx][ny] = 0
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  map_data = [list(map(int, input().split())) for _ in range(h)]
  island_cnt = 0

  for i in range(h):
    for j in range(w):
      if map_data[i][j]:
        island_cnt += 1
        map_data[i][j] = 0
        dfs(i, j)

  print(island_cnt)