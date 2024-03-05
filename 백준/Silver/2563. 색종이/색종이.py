paper = [[0]*100 for _ in range(100)]

N = int(input())
for _ in range(N):
  n, m = map(int, input().split())
  for i in range(n, n+10):
    for j in range(m, m+10):
      paper[i][j] = 1

total = 0
for i in range(100):
  total += sum(paper[i])

print(total)