N = int(input())
body = [input() for _ in range(N)]

left_arm = right_arm = waist = left_leg = right_leg = 0
head = [-1,-1]
heart = [-1,-1]

for i in range(N):
  for j in range(N):
    if body[i][j] == "*":
      if head == [-1,-1]:
        head = [i,j]
      elif head[0] == i-1:
        if head[1] == j:
          heart = [i,j]
        elif heart == [-1,-1]:
          left_arm += 1
        else:
          right_arm += 1
      elif head[1] == j:
        waist += 1
      elif head[1] > j:
        left_leg += 1
      elif head[1] < j:
        right_leg += 1

print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, waist, left_leg, right_leg)