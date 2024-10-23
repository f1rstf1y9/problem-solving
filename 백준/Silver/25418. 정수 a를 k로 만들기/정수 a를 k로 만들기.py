A, K = map(int, input().split())

dp = [K]*(K+1) # dp[n] = A를 n으로 만들기 위해 필요한 최소 연산 횟수
dp[A] = 0

for i in range(A+1, K+1):
  dp[i] = dp[i-1] + 1
  if i%2 == 0:
    dp[i] = min(dp[i-1], dp[i//2]) + 1

print(dp[K])