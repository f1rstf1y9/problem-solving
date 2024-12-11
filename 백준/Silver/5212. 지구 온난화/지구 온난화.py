R, C = map(int, input().split())
island_map = [list(input()) for _ in range(R)]
after_island_map = [['.']*C for _ in range(R)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(R):
    for j in range(C):
        if island_map[i][j] == 'X':
            sea_cnt = 0
            for dx, dy in directions:
                nx, ny = i+dx, j+dy
                if not (0 <= nx < R and 0 <= ny < C) or island_map[nx][ny] == '.':
                    sea_cnt += 1
            if sea_cnt < 3:
                after_island_map[i][j] = 'X'

min_row, max_row, min_col, max_col = R, 0, C, 0
for i in range(R):
    for j in range(C):
        if after_island_map[i][j] == 'X':
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

for i in range(min_row, max_row + 1):
    print(''.join(after_island_map[i][min_col:max_col + 1]))
            