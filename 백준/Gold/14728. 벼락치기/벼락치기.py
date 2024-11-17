N, T = map(int, input().split())

score = [[0]*(T+1) for _ in range(N)]

for n in range(N):
    K, S = map(int, input().split())
    for t in range(1, T+1):
        if t < K:
            score[n][t] = score[n-1][t]
        else:
            score[n][t] = max(score[n-1][t], score[n-1][t-K] + S)

print(score[-1][-1])
            
    
    
    