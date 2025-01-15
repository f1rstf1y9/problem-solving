from heapq import heappush, heappop

import sys
input = sys.stdin.readline

def dijkstra(graph, start):
    hq = [(0, 1)]
    distances = [float('INF')]*(N+1)
    distances[start] = 0
    ways = [[] for _ in range(N+1)]
    
    while hq:
        cur_cost, cur_node = heappop(hq)
        
        if cur_cost > distances[cur_node]:
            continue
        
        for next_node, next_cost in graph[cur_node]:
            new_cost = distances[cur_node] + next_cost
            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                ways[next_node] = ways[cur_node] + [(cur_node,next_node)]
                heappush(hq, (new_cost, next_node))
        
    return ways


N, M = map(int, input().split())
network = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    network[a].append((b, c))
    network[b].append((a, c))

ways = dijkstra(network, 1)

lines = set()
for way in ways:
    for line in way:
        lines.add(line)

print(len(lines))
for a, b in lines:
    print(a, b)