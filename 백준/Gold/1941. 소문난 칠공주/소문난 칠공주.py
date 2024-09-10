from itertools import combinations
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    s_count, y_count = 0, 0
    if seats[x][y] == 'S':
        s_count += 1
    else:
        y_count += 1
    while q:
        x, y = q.popleft()
        if s_count + y_count == 7 and 4 <= s_count:
            return True
        for dx, dy in [(1,0), (-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if group_check[nx][ny]:
                    visited[nx][ny] = 1
                    if seats[nx][ny] == 'S':
                        s_count += 1
                    else:
                        y_count += 1
                    q.append((nx, ny))
    return False

seats = [input() for _ in range(5)]
group_combs = list(combinations([(i//5, i%5) for i in range(25)], 7))
answer = 0
for group in group_combs:
    group_check = [[0]*5 for _ in range(5)]
    visited = [[0]*5 for _ in range(5)]

    s_count = 0
    for x, y in group:
        group_check[x][y] = 1

    x, y = group[0]
    visited[x][y] = 1
    if bfs(x, y):
        answer += 1

print(answer)