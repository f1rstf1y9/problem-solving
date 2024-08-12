msg_time = [list(map(int, input().split())) for _ in range(12)]

is_recieved = [False]*12
min_time = 1000 * 12

def backtracking(cur_group, cur_student, time, is_recieved, next_group):
  global min_time
  if time >= min_time:
    return
  if cur_group == 5 and is_recieved[10] and is_recieved[11]:
    min_time = time
    return
  if next_group != cur_group:
      is_recieved[next_group*2] = True
      backtracking(next_group, next_group*2, time+msg_time[cur_student][next_group*2], is_recieved, next_group)
      is_recieved[next_group*2] = False

      is_recieved[next_group*2+1] = True
      backtracking(next_group, next_group*2+1, time+msg_time[cur_student][next_group*2+1], is_recieved, next_group)
      is_recieved[next_group*2+1] = False
  elif not is_recieved[cur_group*2]:
    is_recieved[cur_group*2] = True
    backtracking(cur_group, cur_group*2, time+msg_time[cur_student][cur_group*2], is_recieved, cur_group+1)
    is_recieved[cur_group*2] = False
  elif not is_recieved[cur_group*2+1]:
    is_recieved[cur_group*2+1] = True
    backtracking(cur_group, cur_group*2+1, time+msg_time[cur_student][cur_group*2+1], is_recieved, cur_group+1)
    is_recieved[cur_group*2+1] = False

is_recieved[0] = True
backtracking(0, 0, 0, is_recieved, 0)
is_recieved[0] = False

is_recieved[1] = True
backtracking(1, 1, 0, is_recieved, 0)
is_recieved[1] = False

print(min_time)