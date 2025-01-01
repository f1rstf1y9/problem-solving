import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

q = deque([R])
visited = [0]*(N+1)
visited[R] = 1
visited_order = 2

while q:
    cur_node = q.popleft()
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = visited_order
            visited_order += 1

print(*visited[1:], sep="\n")
    