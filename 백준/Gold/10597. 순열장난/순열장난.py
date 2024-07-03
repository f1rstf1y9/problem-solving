sequence = input()
number_count = 0
if len(sequence) < 10:
  number_count = len(sequence)
else:
  number_count = 10 + (len(sequence)-10)//2

answer = []
def backtracking(cur_idx, cur_sequence):
  global answer
  if answer:
    return
  if cur_idx == len(sequence):
    if len(cur_sequence) == number_count:
      sorted_sequence = sorted(map(int, cur_sequence))
      for i in range(number_count):
        if sorted_sequence[i] != i+1:
          break
      else:
        answer = cur_sequence[:]
    return
  if cur_idx < len(sequence)-1:
    cur_num = sequence[cur_idx:cur_idx+2]
    if int(cur_num) <= number_count and cur_num not in cur_sequence:
      cur_sequence.append(cur_num)
      backtracking(cur_idx+2, cur_sequence)
      cur_sequence.pop()
  if sequence[cur_idx] not in cur_sequence:
    cur_sequence.append(sequence[cur_idx])
    backtracking(cur_idx+1, cur_sequence)
    cur_sequence.pop()
  

backtracking(0, [])
print(*answer)