N, M = map(int, input().split())

board_string = input()
have_string = input()

max_score = 0

dp = [[0]*N for _ in range(M)] # dp[i][j] 건덕이의 i번째 글자까지 확인하고, 보드판의 j번째 글자까지 확인했을 때의 최대 점수 

dp[0] = [1 if board_string[i] == have_string[0] else 0 for i in range(N)]


for i in range(1, M):
  for j in range(N):
    if j == 0:
      dp[i][j] = dp[i-1][j+1] + (1 if board_string[j] == have_string[i] else 0)
    elif j == N-1:
      dp[i][j] = dp[i-1][j-1] + (1 if board_string[j] == have_string[i] else 0)
    else:
      score = 1 if board_string[j] == have_string[i] else 0
      dp[i][j] = max(dp[i-1][j-1] + score, dp[i-1][j+1] + score)

print(max(dp[M-1]))
