delta = [(0,1),(0,-1),(1,0),(-1,0)]
def move(x, y, current_num):
    if len(current_num) == 6:
        number_set.add(current_num)
        return
    
    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            move(nx, ny, current_num+board[nx][ny])


number_set = set()
board = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(5):
        move(i, j, '')

print(len(number_set))
