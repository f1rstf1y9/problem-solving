import sys

vowel = ['a','e', 'i', 'o', 'u']

while True:
  pw = sys.stdin.readline().rstrip()
  
  if pw == "end": break

  prev_letter = ''
  prev_kind = ''
  conti_cnt = 0
  vowel_include = False
  
  for c in pw:
    if prev_letter not in ('e', 'o') and prev_letter == c:
      print(f"<{pw}> is not acceptable.")
      break
    if c in vowel:
      vowel_include = True
      if prev_kind == 'c':
        conti_cnt = 1
      else:
        conti_cnt += 1
      prev_letter, prev_kind = c, 'v'
    else:
      if prev_kind == 'v':
        conti_cnt = 1
      else:
        conti_cnt += 1
      prev_letter, prev_kind = c, 'c'
    if conti_cnt == 3:
      print(f"<{pw}> is not acceptable.")
      break
  else:
    if vowel_include:
      print(f"<{pw}> is acceptable.")
    else:
      print(f"<{pw}> is not acceptable.")