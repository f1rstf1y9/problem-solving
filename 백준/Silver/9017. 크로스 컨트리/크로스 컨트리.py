T = int(input())
for _ in range(T):
  N = int(input())
  teams = list(map(int, input().split()))

  teams_info = {}  
  for i in range(1, max(teams)+1):
    if teams.count(i) == 6:
      teams_info[i] = [0, 0, -1, i]

  grade = 1
  for i in range(N):
    if teams_info.get(teams[i]):
      t = teams[i]
      teams_info[t][1] += 1
      if teams_info[t][1] <= 4:
        teams_info[t][0] += grade
      if teams_info[t][1] == 5:
        teams_info[t][2] = grade
      grade += 1
  teams_grade = sorted(teams_info.values(), key=lambda x: (x[0], x[2]))
  print(teams_grade[0][-1])