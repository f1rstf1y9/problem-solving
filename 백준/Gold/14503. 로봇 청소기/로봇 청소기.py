import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

delta = [(-1,0), (0,1),(1,0),(0,-1)]

room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

count = 0

while True:
  if not visited[r][c]:
    visited[r][c] = 1
    count += 1

  for i in range(4):
    d = (d+3)%4
    x, y = delta[d]
    if room[r+x][c+y] == 0 and not visited[r+x][c+y]:
      r, c = r+x, c+y
      break
  else: 
    dr, dc = r-delta[d][0], c-delta[d][1]
    if 0 < dr < N-1 and 0 < dc < M-1 and room[dr][dc] == 0:
      r, c = dr, dc
    else:
      break

print(count)