p = input()
for i in range(len(p)//2):
  if p[i] != p[len(p)-i-1]:
    print(0)
    break
else:
  print(1)