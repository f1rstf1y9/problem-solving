from collections import deque

N = int(input())
towers = [1e9]+list(map(int, input().split()))

stack = deque([(1e9,0)])
for i in range(1,N+1):
  while stack and stack[-1][0] < towers[i]:
    stack.pop()
  print(stack[-1][1], end=" ")
  stack.append((towers[i], i))