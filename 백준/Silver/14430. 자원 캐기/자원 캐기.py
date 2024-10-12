N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*M for _ in range(N)]
dp[0][0] = grid[0][0]

for n in range(1, N):
  dp[n][0] = dp[n-1][0] + grid[n][0]

for m in range(1, M):
  dp[0][m] = dp[0][m-1] + grid[0][m]

for n in range(1, N):
  for m in range(1, M):
    dp[n][m] = max(dp[n-1][m], dp[n][m-1]) + grid[n][m]
  
print(dp[N-1][M-1])