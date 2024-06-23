switch_count = int(input()) # 1~100
switch_status = list(map(int, input().split()))

student_count = int(input()) # 1~100
for _ in range(student_count):
  gender, switch_num = map(int, input().split())
  if gender == 1:
    for i in range(switch_num-1, switch_count, switch_num):
      switch_status[i] = 0 if switch_status[i] else 1
  if gender == 2:
    range_count = 0
    for i in range(1, min(switch_num, switch_count-switch_num+1)):
      range_count = i
      if switch_status[switch_num-i-1] != switch_status[switch_num+i-1]:
        range_count = i-1
        break
    for i in range(switch_num-range_count-1, switch_num+range_count):
      switch_status[i] = 0 if switch_status[i] else 1

for i in range(switch_count//20):
  print(*switch_status[i*20:(i+1)*20])
print(*switch_status[20*(switch_count//20):])