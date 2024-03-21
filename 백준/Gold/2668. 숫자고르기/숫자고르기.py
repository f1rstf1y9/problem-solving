import sys
input = sys.stdin.readline

N = int(input())
top = [x for x in range(N+1)]
bottom = [0]

for i in range(1, N+1):
  bottom.append(int(input()))

def dfs(cur_top, start, nums):
  visited[cur_top] = 1
  if bottom[cur_top] == start:
    return nums
  if visited[bottom[cur_top]]:
    return []
  return dfs(top[bottom[cur_top]], start, nums+[bottom[cur_top]])

group = []
for i in range(1, N+1):
  visited = [0 for _ in range(N+1)]
  group += dfs(i, i, [i])
print(len(set(group)))
print(*sorted(set(group)), sep="\n")