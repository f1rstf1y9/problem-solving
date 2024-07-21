A = int(input())
X = int(input())

cur = A
answer = 1

while X:
  if X & 1:
    answer = (answer * A) % 1000000007
  A = A ** 2 % 1000000007
  X //= 2

print(answer)