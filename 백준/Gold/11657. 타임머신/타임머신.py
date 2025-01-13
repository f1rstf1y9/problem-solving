'''
도시 N(1 <= N <= 500)개, 버스 M(1 <= M <= 6,000)개
버스 A 출발, B 도착, C 걸리는 시간(-10,000 <= C <= 10,000)

1번 도시에서 출발해 나머지 도시로 가는 가장 빠른 시간 구하기
(문제를 그래프로 표현할 수 있고, 음의 가중치가 존재하는 상황. 음의 사이클이 발생할 수 있음. 특정한 노드에서 다른 노드까지 가는 비용의 최솟값 구하기 => 벨만 포드 알고리즘)
'''

import sys
input = sys.stdin.readline

INF = 1e9

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

dists = [INF]*(N+1)

def bf(start):
    dists[start] = 0
    for i in range(N):
        for j in range(M):
            cur, next, cost = edges[j]
            if dists[cur] != INF and dists[cur] + cost < dists[next]:
                dists[next] = dists[cur] + cost
                if i == N - 1:
                    return True
    return False

has_negative_cycle = bf(1)
if has_negative_cycle:
    print(-1)
else:
    print(*(-1 if dist == INF else dist for dist in dists[2:]), sep="\n")