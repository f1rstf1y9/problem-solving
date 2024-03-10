import sys

def is_winner(me, other):
  if me[0] > other[0]:
    return True
  if me[0] < other[0]:
    return False
  if me[1] > other[1]:
    return True
  if me[1] < other[1]:
    return False
  if me[2] > other[2]:
    return True
  return False

N, K = map(int, sys.stdin.readline().rstrip().split())
countries = [[] for i in range(N)]
for _ in range(N):
  n, *medals = map(int, sys.stdin.readline().rstrip().split())
  countries[n-1] = medals

grade = 1
for i in range(N):
  if i == K-1:
    continue
  if is_winner(countries[i], countries[K-1]):
    grade += 1

print(grade)