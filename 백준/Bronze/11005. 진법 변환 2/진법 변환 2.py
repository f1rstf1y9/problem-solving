N, B = map(int, input().split())

i = 0
while B**(i+1) <= N:
    i += 1

for j in range(i, -1, -1):
  n = int(N // (B**j))
  N = N - B**j*n
  if n > 9:
    n = chr(n+55)
  print(n, end="")