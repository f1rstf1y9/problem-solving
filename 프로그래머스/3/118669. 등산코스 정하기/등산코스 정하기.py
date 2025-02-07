from collections import deque
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    INF = int(1e8)
    
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    is_gate = [False]*(n+1)
    is_summit = [False]*(n+1)
    for g in gates:
        is_gate[g] = True
    for s in summits:
        is_summit[s] = True
        
    intensity = [INF]*(n+1)
    hq = []
    for g in gates:
        intensity[g] = 0
        heappush(hq, (0, g))
    
        
    while hq:
        cur_intensity, cur_node = heappop(hq)

        if cur_intensity > intensity[cur_node]:
            continue

        if is_summit[cur_node]:
            continue

        for next_node, next_intensity in graph[cur_node]:
            next_intensity = max(cur_intensity, next_intensity)
            if not is_gate[next_node] and next_intensity < intensity[next_node]:
                intensity[next_node] = next_intensity
                heappush(hq, (next_intensity, next_node))
    
    summits.sort()
    answer = [0, INF]
    
    for s in summits:
        if intensity[s] < answer[1]:
            answer = [s, intensity[s]]
    
    return answer