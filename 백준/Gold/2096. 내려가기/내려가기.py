import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
max_dp = line
min_dp = line

for i in range(1, N):
  line = list(map(int, input().split()))
  max_dp = [
    max(max_dp[0], max_dp[1]) + line[0],
    max(max_dp) + line[1],
    max(max_dp[1], max_dp[2]) + line[2]
  ]
  min_dp = [
    min(min_dp[0], min_dp[1]) + line[0],
    min(min_dp) + line[1],
    min(min_dp[1], min_dp[2]) + line[2]]

print(max(max_dp), min(min_dp))