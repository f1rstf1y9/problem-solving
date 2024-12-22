N = int(input())
candies = [list(input()) for _ in range(N)]

def get_max_candy_cnt():
    max_candy_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candies[i][j] == candies[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_candy_cnt = max(max_candy_cnt, cnt)
        
        cnt = 1
        for j in range(1, N):
            if candies[j][i] == candies[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_candy_cnt = max(max_candy_cnt, cnt)
    return max_candy_cnt
    

max_candy_cnt = 0
for i in range(N):
    for j in range(N):
        if i < N-1 and candies[i][j] != candies[i+1][j]:
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            max_candy_cnt = max(max_candy_cnt, get_max_candy_cnt())
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
        if j < N-1 and candies[i][j] != candies[i][j+1]:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            max_candy_cnt = max(max_candy_cnt, get_max_candy_cnt())
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

print(max_candy_cnt)