import sys
input = sys.stdin.readline

N = int(input())

cows_id = [int(input()) for _ in range(N)]

psum = [0]

for i in range(N):
  psum.append(psum[i]+cows_id[i])

mod_idx = [-1]*7

answer = 0

for i in range(N+1):
  mod = psum[i] % 7
  if mod_idx[mod] == -1:
    mod_idx[mod] = i
  else:
    answer = max(answer, i-mod_idx[mod])

print(answer)