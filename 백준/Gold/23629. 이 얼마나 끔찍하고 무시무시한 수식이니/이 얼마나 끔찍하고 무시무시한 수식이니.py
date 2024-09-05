from collections import deque
import math

exp = input()

ops = ['+', '-', 'x', '/']

answer = ''

if exp[-2] in ops:
  print('Madness!')
  exit()

for i in range(len(exp)-1):
  if exp[i] in ops and exp[i+1] in ops:
    print('Madness!')
    exit()


eng_to_num = {'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9'}

num_to_eng = {'0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'}

for eng in eng_to_num.keys():
  exp = exp.replace(eng, eng_to_num[eng])

for n in exp[:-1]:
  if n not in ops and n not in num_to_eng.keys():
    print('Madness!')
    exit()

print(exp)

exp = deque(exp)
while exp:
  num1 = ''
  num2 = ''
  op = ''

  while exp[0] not in ops and exp[0] != '=':
    num1 += exp.popleft()

  if exp[0] == '=':
    exp = num1
    break

  op = exp.popleft()

  while exp[0] not in ops and exp[0] != '=':
    num2 += exp.popleft()
  
  num1 = int(num1)
  num2 = int(num2)

  if op == '+':
    result = num1 + num2
  elif op == '-':
    result = num1 - num2
  elif op == 'x':
    result = num1 * num2
  elif op == '/':
    result = num1 / num2
    if result > 0:
      result = math.floor(result)
    else:
      result = math.ceil(result)

  if exp[0] == '=':
    exp = str(result)
    break
  else:    
    exp.appendleft(str(result))

for num in num_to_eng.keys():
  exp = exp.replace(num, num_to_eng[num])

print(exp)