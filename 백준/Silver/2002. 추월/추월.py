n = int(input())
enter = {input():i for i in range(n)}
out = {input():i for i in range(n)}

count = 0
for out_car in out.keys():
  out_idx = out[out_car]
  enter_idx = enter[out_car]
  for other_car in out.keys():
    if out[other_car] > out_idx and enter[other_car] <= enter_idx:
      count += 1
      break

print(count)