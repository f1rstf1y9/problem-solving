import math

N = int(input())
results = []

def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

def backtracking(n):
  n = str(n)
  if len(n) == N:
    results.append(n)
    return
  for i in range(1, 10):
    new_n = int(n + str(i))
    if is_prime(new_n):
      backtracking(new_n)

for n in [2, 3, 5, 7]:
  backtracking(n)

print(*sorted(results), sep='\n')