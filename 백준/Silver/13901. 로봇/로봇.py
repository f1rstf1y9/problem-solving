R, C = map(int, input().split())
room = [[0]*C for _ in range(R)]

k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = 1

r, c = map(int, input().split())
directions = [(-1,0),(1,0),(0,-1),(0,1)]
direction_order = [directions[order-1] for order in map(int, input().split())]

room[r][c] = 3
cur_direction = 0

while True:
    for i in range(4):
        dr, dc = direction_order[cur_direction]
        nr, nc = r+dr, c+dc
        
        if 0 <= nr < R and 0 <= nc < C and not room[nr][nc]:
            r, c = nr, nc
            room[r][c] = 3
            break
        cur_direction = (cur_direction + 1) % 4
    else:
        print(r, c)
        break
else:
    print(r, c)
