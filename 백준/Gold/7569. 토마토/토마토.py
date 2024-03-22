from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato_box = []
for i in range(H):
  tomato_box.append([list(map(int, input().split())) for _ in range(N)])

delta = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
queue = deque()
  
for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomato_box[i][j][k] == 1:
        queue.append((i,j,k,tomato_box[i][j][k]))

while queue:
    i, j, k, day = queue.popleft()
    for h, r, c in delta:
      dh, dr, dc = i+h, j+r, k+c
      if 0 <= dh < H and 0 <= dr < N and 0 <= dc < M and tomato_box[dh][dr][dc] == 0:
        tomato_box[dh][dr][dc] = day+1
        queue.append((dh, dr, dc, day+1))

max_day = 0
for i in range(H):
  if max_day == -1:
    break
  for j in range(N):
    if 0 in tomato_box[i][j]:
      max_day = -1
      break
    max_day = max(max_day, max(tomato_box[i][j]))

print(max_day-1 if max_day != -1 else -1)