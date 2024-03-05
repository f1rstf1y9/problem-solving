max_v, col, row = -1, 0, 0

board = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
  for j in range(9):
    if board[i][j] > max_v:
      max_v, col, row = board[i][j], i+1, j+1
    
print(f"{max_v}\n{col} {row}")