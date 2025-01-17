import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('INF')

def dijkstra(start, graph):
    hq = [(0, start)]
    distances = [INF]*(V+1)
    distances[start] = 0
    
    while hq:
        cur_cost, cur_node = heappop(hq)
        
        if cur_cost > distances[cur_node]:
            continue
        
        for next_node, next_cost in graph[cur_node]:
            new_cost = cur_cost + next_cost
            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heappush(hq, (new_cost, next_node))
    return distances

V, M = map(int, input().split())
places = [[] for _ in range(V+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    places[a].append((b, c))
    places[b].append((a, c))

J, S = map(int, input().split())

j_distances = dijkstra(J, places)
s_distances = dijkstra(S, places)

total_distances = [(j_distances[i] + s_distances[i], j_distances[i], i) for i in range(V+1) if i != J and i != S and j_distances[i] != float('INF') and s_distances[i] != float('INF')]
total_distances.sort(key=lambda x:(x[0], x[1], x[2]))

answer = -1
final_min_distance = total_distances[0][0] if total_distances else None
for distance, _, point in total_distances:
    if distance > final_min_distance:
        break
    if j_distances[point] <= s_distances[point]:
        answer = point
        break
print(answer)