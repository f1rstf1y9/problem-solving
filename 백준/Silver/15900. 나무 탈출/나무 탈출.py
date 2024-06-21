import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, input().split())
  a, b = min(a,b), max(a,b)
  tree[a].append(b)
  tree[b].append(a)

total_depth = 0
visited = [False] * (N+1)

stack = deque([(1, 0)])
while stack:
  current_node, current_depth = stack.pop()
  visited[current_node] = True
  if current_node != 1 and len(tree[current_node]) == 1:
    total_depth += current_depth
    continue
  for node in tree[current_node]:
    if not visited[node]:
      stack.append((node, current_depth+1))

print('Yes' if total_depth % 2 else 'No')