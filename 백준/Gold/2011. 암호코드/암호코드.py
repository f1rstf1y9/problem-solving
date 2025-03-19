import sys
input = sys.stdin.readline

pwd = input().strip()
N = len(pwd)
if pwd[0] == '0':
    print(0)
    exit()
    
dp = [1] + [0]*(N-1)

for i in range(1, N):
    p1 = 1 if 1 <= int(pwd[i]) <= 9 else 0
    p2 = 1 if 10 <= int(pwd[i-1]+pwd[i]) <= 26 else 0
    
    if i == 1:
        dp[i] = p1 + p2
    else:
        dp[i] = (dp[i-1]*p1 + dp[i-2]*p2) % 1000000

print(dp[N-1])