'''
마을의 개수 N : 1 ~ 50
road 길이 : 1 ~ 2000
road => 길이가 3인 배열 (a, b, c)
  - a, b : 도로가 연결하는 두 마을의 번호
  - c : 도로를 지나는데 걸리는 시간
음식 배달이 가능한 시간 K : 1 ~ 500,000

1번 마을로부터 각 마을까지 K 시간 이하로 배달이 가능한 마을의 수
'''
from heapq import heappush, heappop

INF = 10e9

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N)]
    
    for a, b, c in road:
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
        
    distances = [0] + [INF]*(N-1)
    
    def dijkstra(start):
        q = []
        
        heappush(q, (0, start))
        
        while q:
            dist, now = heappop(q)
            if distances[now] < dist:
                continue
            
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distances[i[0]]:
                    distances[i[0]] = cost
                    heappush(q, (cost, i[0]))
    
    dijkstra(0)
    
    for i in range(N):
        if distances[i] <= K:
            answer += 1
                
    
    return answer