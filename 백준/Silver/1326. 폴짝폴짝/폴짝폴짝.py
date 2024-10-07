from collections import deque

N = int(input())
bridge_numbers = list(map(int, input().split()))
a, b = map(lambda x:int(x)-1, input().split())

q = deque([a])
visited = [-1]*N
visited[a] = 0

while q:
  current = q.popleft()
  if current == b:
    break

  bridge_number = bridge_numbers[current]
  count = visited[current]

  for next in range(current-bridge_number, -1, -bridge_number):
    if visited[next] == -1:
      visited[next] = count+1
      q.append(next)
  
  for next in range(current+bridge_number, N, bridge_number):
    if visited[next] == -1:
      visited[next] = count+1
      q.append(next)

print(visited[b])