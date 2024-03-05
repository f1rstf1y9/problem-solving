sentences = []
for _ in range(5):
  sentences.append(input())

for i in range(15):
  for j in range(5):
    if len(sentences[j]) > i:
      print(sentences[j][i], end="")