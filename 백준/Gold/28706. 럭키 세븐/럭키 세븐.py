import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    dp = [False]+[True]+[False]*5 # i번째 depth에 돌입했을 때, 7로 나눈 나머지가 j가 될 수 있는지?
    for depth in range(1, N+1):
        op1, v1, op2, v2 = input().split()
        temp = [False]*7
        for i in range(7):
            if dp[i]:
                mod1 = ((i + int(v1)) if op1 == '+' else (i * int(v1))) % 7
                temp[mod1] = True
                mod2 = ((i + int(v2)) if op2 == '+' else (i * int(v2))) % 7
                temp[mod2] = True
        dp = temp
    if dp[0]:
        print("LUCKY")
    else:
        print("UNLUCKY")