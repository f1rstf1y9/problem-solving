import sys, math
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    boards[x][y] = 1
    areas = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]
            if 0 <= nx < N and 0 <= ny < N and boards[nx][ny] == 0:
                boards[nx][ny] = 1
                queue.append((nx, ny))
                areas += 1

    return areas


N, M, K = map(int, input().split())

boards = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

total_nums = 0
use_seed = False

for i in range(N):
    for j in range(N):
        if boards[i][j] == 0:
            areas = bfs(i, j)
            nums = math.ceil(areas / K)
            total_nums += nums
            use_seed = True

if not use_seed:
    print('IMPOSSIBLE')
elif total_nums <= M:
    print('POSSIBLE')
    print(M - total_nums)
else:
    print('IMPOSSIBLE')