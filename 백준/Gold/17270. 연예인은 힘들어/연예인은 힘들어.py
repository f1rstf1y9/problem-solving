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

total_distances = sorted([(j_distances[i] + s_distances[i]) for i in range(1, V+1) if i != J and i != S and j_distances[i] != INF and s_distances[i] != INF])
min_distance = total_distances[0] if total_distances else -1


answer = -1
cur_j_distance = INF

for i in range(V, 0, -1):
    # 1번 조건 : 지헌이의 출발 위치와 성하의 출발 위치는 새로운 약속 장소가 될 수 없다.
    if i == J or i == S:
        continue
    
    # 2번 조건 : 새로운 약속 장소는 지헌이가 걸리는 최단 시간과 성하가 걸리는 최단 시간의 합이 최소가 되도록 한다.
    if j_distances[i] + s_distances[i] != min_distance:
        continue
    
    # 3번 조건 : 지헌이가 성하보다 늦게 도착하는 곳은 약속 장소가 될 수 없다.
    if j_distances[i] > s_distances[i]:
        continue
    
    # 4번 조건 : 지헌이로부터 가장 가까운 곳 > 번호가 가장 작은 장소 순으로 최종 약속 장소 결정
    if cur_j_distance > j_distances[i]:
        cur_j_distance = j_distances[i]
        answer = i
    
print(answer)