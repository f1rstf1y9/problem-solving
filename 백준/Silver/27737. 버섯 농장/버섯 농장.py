from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, grid, visited, N): 
    queue = deque([(x, y)])
    visited[x][y] = True
    component_size = 1

    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                component_size += 1

    return component_size

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


visited = [[False] * N for _ in range(N)]

component_sizes = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            component_size = bfs(i, j, grid, visited, N)
            component_sizes.append(component_size)

spores_needed = 0

for size in component_sizes:
    spores_needed += (size + K - 1) // K

if spores_needed > M or spores_needed == 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(M - spores_needed)