N = int(input())
options = [input().split() for _ in range(N)]

alphabets = [False]*26
shortcuts_idx = [0]*N

def check_shortcut(option_idx, word_idx, cur_alphabet):
  cur_alphabet = ord(cur_alphabet.lower())
  cur_alphabet = cur_alphabet - 97
  if not alphabets[cur_alphabet]:
    shortcuts_idx[option_idx] = word_idx
    alphabets[cur_alphabet] = True
    return True
  return False

for n in range(N):
  option = options[n]
  isFound = False

  # 각 단어 첫글자 탐색
  for i in range(len(option)):
    if check_shortcut(n, (i, 0), option[i][0]):
      isFound = True
      break
    
  # 단어 첫글자에서 단축어를 지정 못했다면 모든 글자
  if not isFound:
    for i in range(len(option)):
      for j in range(len(option[i])):
        if check_shortcut(n, (i, j), option[i][j]):
          isFound = True
          break
      if isFound:
        break

for n in range(N):
  option = options[n]
  if not shortcuts_idx[n]:
    print(*option)
  else:
    words = ""
    for i in range(len(option)):
      for j in range(len(option[i])):
        if shortcuts_idx[n] == (i, j):
          words += f'[{option[i][j]}]'
        else:
          words += option[i][j]
      words += " "
    print(words)