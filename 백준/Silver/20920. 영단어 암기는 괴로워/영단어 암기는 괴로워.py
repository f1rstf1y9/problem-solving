import sys
N, M = map(int, sys.stdin.readline().split())

words = {}
for _ in range(N):
  word = sys.stdin.readline().rstrip()
  if len(word) >= M:
    if words.get(word):
      words[word][0] += 1
    else:
      words[word] = [1, len(word), word]
words = sorted(words.values(), key=lambda x,:(-x[0],-x[1],x[2]))

for word in words:
  print(word[2])