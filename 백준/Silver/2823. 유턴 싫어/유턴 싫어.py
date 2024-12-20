R, C = map(int, input().split())
city_map = [input() for _ in range(R)] 

directions = [(-1,0),(1,0),(0,1),(0,-1)]

def has_blocked_road():
    for r in range(R):
        for c in range(C):
            if city_map[r][c] == '.':
                way_cnt = 0
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and city_map[nr][nc] == '.':
                        way_cnt += 1
                if way_cnt == 1:
                    return 1
    return 0

print(has_blocked_road())
            