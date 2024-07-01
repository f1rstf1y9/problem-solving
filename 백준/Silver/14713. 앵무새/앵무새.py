from collections import deque

N = int(input())
S = []

for _ in range(N):
  words = input().split()
  S.append(deque(words))

L = input().split()

queue = deque()

idx = 0
while idx < len(L):
  for i in range(N):
    if S[i] and S[i][0] == L[idx]:
      queue.append(S[i].popleft())
      idx += 1
      break
  else:
      print('Impossible')
      break
else:
  for i in range(N):
    if S[i]:
      print('Impossible')
      break
  else:
    print('Possible')