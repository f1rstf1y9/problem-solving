N = int(input())
prev = input()
length = len(prev)
for _ in range(N-1):
  file = input()
  temp = ''
  for i in range(length):
    if prev[i] == file[i]:
      temp += file[i]
    else:
      temp += '?'
  prev = temp
print(prev)