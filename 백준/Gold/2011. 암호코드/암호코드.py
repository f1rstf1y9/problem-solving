import sys
input = sys.stdin.readline

pwd = input().strip()
N = len(pwd)
if pwd[0] == '0':
    print(0)
    exit()
    
dp = [1] + [0]*(N-1)

if N > 1:
    dp[1] = (1 if 1 <= int(pwd[1]) <= 9 else 0) + (1 if 10 <= int(pwd[0]+pwd[1]) <= 26 else 0)

for i in range(2, N):
    p1 = 1 if 1 <= int(pwd[i]) <= 9 else 0
    p2 = 1 if 10 <= int(pwd[i-1]+pwd[i]) <= 26 else 0
    dp[i] = (dp[i-1]*p1 + dp[i-2]*p2) % 1000000

print(dp[len(pwd)-1])