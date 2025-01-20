import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(start):
    distances = [float('INF')]*(N+1)
    distances[start] = 0
    hq = [(0, start)]
    
    while hq:
        cur_cost, cur_node = heappop(hq)
        
        if cur_cost > distances[cur_node]:
            continue
            
        for next_node, next_cost in graph[cur_node]:
            new_cost = cur_cost + next_cost
            if distances[next_node] > new_cost:
                distances[next_node] = new_cost
                heappush(hq, (new_cost, next_node))
    
    return distances

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())

from_v1_distances = dijkstra(v1)
from_v2_distances = dijkstra(v2)

v1_start, v1_end = from_v1_distances[1], from_v1_distances[N]
v2_start, v2_end = from_v2_distances[1], from_v2_distances[N]
answer = min(v1_start+v2_end, v1_end+v2_start) + from_v1_distances[v2]

print(answer if answer < float('INF') else -1)