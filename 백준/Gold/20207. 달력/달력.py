N = int(input())
plans = [tuple(map(int, input().split())) for _ in range(N)]

plans.sort(key=lambda x: (x[0], -x[1]))

calendar = {day:0 for day in range(1, 366)}

for start, end in plans:
  for day in range(start, end+1):
    calendar[day] += 1

day = plans[0][0]
rectangle_area = 0
continuous_days = 0
height = 0

while day <= 365:
  if not calendar[day]:
    rectangle_area += continuous_days*height
    continuous_days = 0
    height = 0
  else:
    continuous_days += 1
    height = max(height, calendar[day])
  day += 1

print(rectangle_area + continuous_days*height)