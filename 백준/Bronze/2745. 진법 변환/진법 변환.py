N, B = input().split()
B = int(B)

ans = 0
for i in range(len(N)):
  if N[i].isalpha():
    n = ord(N[i]) - 55
  else:
    n = int(N[i])
  ans += n * (B**(len(N)-i-1))

print(ans)