grade_score = {"A+": 4.5, "A0": 4, "B+": 3.5, "B0": 3, "C+": 2.5, "C0": 2, "D+":1.5, "D0": 1, "F": 0}

total = 0
score_total = 0

for _ in range(20):
  _, score, grade = input().split()
  score = int(score[0])
  if grade == "P":
    continue
  grade = grade_score[grade]
  total += score * grade
  score_total += score

print(total / score_total)