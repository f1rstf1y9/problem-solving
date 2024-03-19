import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
pairs = {x:[] for x in range(1,n+1)}
for i in range(m):
  a, b = map(int, input().split())
  pairs[a].append(b)
  pairs[b].append(a)
  
is_virus = [0, 1] + [0]*(n-1)

q = deque([1])
while q:
  cur = q.pop()
  if pairs[cur]:
    for i in pairs[cur]:
      if not is_virus[i]:
        is_virus[i] = 1
        q.append(i)

print(sum(is_virus)-1)