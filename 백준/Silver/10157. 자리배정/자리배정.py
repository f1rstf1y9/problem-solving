C, R = map(int, input().split())
K = int(input())

if C*R < K:
    print(0)
else:
    seats = [[0]*C for _ in range(R)]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    cur_num = 1
    d_idx = 0
    c = r = 0
    while cur_num <= K:
        if 0 <= c < C and 0 <= r < R and not seats[r][c]:
            if cur_num == K:
                print(c+1, r+1)
                break
            seats[r][c] = cur_num
            cur_num += 1
        else:
            dr, dc = directions[d_idx]
            r, c = r-dr, c-dc
            d_idx = (d_idx+1)%4
        dr, dc = directions[d_idx]
        c, r = c+dc, r+dr
    