n = int(input())
c, p, a = 0, 0, 0
for i in range(n-2):
  c += 1
  p += c
  a += p

print(f"{a}\n3")