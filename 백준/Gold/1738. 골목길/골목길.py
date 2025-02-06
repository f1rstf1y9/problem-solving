def bellman_ford(start, end):
    distances = [float('INF')] * (n+1)
    parent = [-1] * (n+1)
    distances[start] = 0
    for _ in range(n-1):
        for u, v, w in edges:
            if distances[u] != float('INF') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                parent[v] = u
    
    for u, v, w in edges:
        if distances[u] != float('INF') and distances[u] + w < distances[v] and is_valid_cycle(v, end):
            return []
    
    if distances[end] == float('INF'):
        return []
    
    return parent

def is_valid_cycle(v, end):
    stack = [v]
    visited = [False]*(n+1)
    while stack:
        cur_node = stack.pop()
        if cur_node == end:
            return True
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
    return False
                
def get_path(start, end, parent):
    node = end
    path = [end]
    while node != start:
        path.append(parent[node])
        node = parent[node]
    return path[::-1]

n, m = map(int, input().split())
edges = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, -w))
    graph[u].append(v)

parent = bellman_ford(1, n)
if parent:
    print(*get_path(1, n, parent))
else:
    print(-1)