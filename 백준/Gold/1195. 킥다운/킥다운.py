first_gear = input()
second_gear = input()

if len(second_gear) < len(first_gear):
  first_gear, second_gear = second_gear, first_gear

len_first = len(first_gear)
len_second = len(second_gear)

delta = 0
answer = len_first + len_second

for delta in range(-len_first, len_second):
  for i in range(len_first):
    if 0 <= i+delta < len_second:
      if first_gear[i] == '2' and second_gear[i+delta] == '2':
        break
  else:
    if delta < 0:
      answer = min(answer, len_second - delta)
    elif delta + len_first > len_second:
      answer = min(answer, delta + len_first)
    else:
      answer = min(answer, len_second)

print(answer)