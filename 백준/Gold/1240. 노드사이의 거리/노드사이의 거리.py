N, M = map(int, input().split())
tree = [[] for _ in range(N)]

def dfs(cur, end, distance):
  global total_distance
  if cur == end:
    total_distance = distance
    return
  
  for point, d in tree[cur]:
    if not visited[point]:
      visited[point] = True
      dfs(point, end, distance+d)
      visited[point] = False
  

for _ in range(N-1):
  point1, point2, distance = map(int, input().split())
  tree[point1-1].append((point2-1, distance))
  tree[point2-1].append((point1-1, distance))

for _ in range(M):
  start, end = map(lambda x: int(x)-1, input().split())
  visited = [False]*N
  visited[start] = True
  dfs(start, end, 0)
  print(total_distance)