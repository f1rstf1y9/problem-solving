from collections import deque
import sys

left = deque(sys.stdin.readline().rstrip())
right = deque([])
M = int(sys.stdin.readline().rstrip())

for _ in range(M):
  m = sys.stdin.readline().rstrip().split()
  if m[0] == "L" and left:
    right.appendleft(left.pop())
  elif m[0] == "D" and right:
    left.append(right.popleft())
  elif m[0] == "B" and left:
    left.pop()
  elif m[0] == "P":
    left.append(m[1])

print(*left, *right, sep="")