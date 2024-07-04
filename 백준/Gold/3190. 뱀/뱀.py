from collections import deque

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]

for _ in range(K):
  r, c = map(int, input().split())
  board[r-1][c-1] = 1

L = int(input())

snake = deque([(0,0)])
cur_d = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

board[0][0] = 2
change_list = deque(input().split() for _ in range(L))
is_finished = False
time = 0

while not is_finished:
  time += 1
  
  head_x, head_y = snake[-1][0]+directions[cur_d][0], snake[-1][1]+directions[cur_d][1]
  tail_x, tail_y = snake[0][0], snake[0][1]

  if 0 <= head_x < N and 0 <= head_y < N: 
    snake.append((head_x, head_y))
    if board[head_x][head_y] == 0:
      board[head_x][head_y] = 2
      board[tail_x][tail_y] = 0
      snake.popleft()
    elif board[head_x][head_y] == 1:
      board[head_x][head_y] = 2
    else:
      is_finished = True
  else:
    is_finished = True

  if change_list and int(change_list[0][0]) == time:
    _, d = change_list.popleft()
    if d == 'D':
      cur_d = (cur_d + 1) % 4
    else:
      cur_d = (cur_d - 1) % 4  

print(time)