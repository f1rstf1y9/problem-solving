N, M = map(int, input().split())
mars_value = [list(map(int, input().split())) for _ in range(N)]

dp_left = [0]*M # 왼쪽에서 오는 것 고려
dp_right = [0]*M # 오른쪽에서 오는 것 고려
dp = [0]*M # 왼쪽, 오른쪽 비교 후 더 큰 가치를 고려

# 첫째줄 초기화
dp[0] = mars_value[0][0]
for i in range(1, M):
    dp[i] = dp[i-1] + mars_value[0][i]

# 나머지 줄
for i in range(1, N):
    dp_left[0] = dp[0]+mars_value[i][0]
    dp_right[M-1] = dp[M-1]+mars_value[i][M-1]
    for j in range(1, M):
        dp_left[j] = max(dp[j], dp_left[j-1]) + mars_value[i][j]
    for j in range(M-2, -1, -1):
        dp_right[j] = max(dp[j], dp_right[j+1]) + mars_value[i][j]
    for j in range(M):
        dp[j] = max(dp_left[j], dp_right[j])

print(dp[M-1])