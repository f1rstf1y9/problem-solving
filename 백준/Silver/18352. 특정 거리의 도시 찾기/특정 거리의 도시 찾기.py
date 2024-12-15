from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
roads = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda x: int(x)-1, input().split())
    roads[A].append(B)

distances = [-1]*N

q = deque([X-1])
distances[X-1] = 0
has_city_at_K = False

while q:
    cur_city = q.popleft()
    for next_city in roads[cur_city]:
        if distances[next_city] == -1:
            distances[next_city] = distances[cur_city] + 1
            if distances[next_city] < K:
                q.append(next_city)
            if distances[next_city] == K:
                has_city_at_K = True

if has_city_at_K:
    for i in range(N):
        if distances[i] == K:
            print(i+1)
else:
    print(-1)


            

