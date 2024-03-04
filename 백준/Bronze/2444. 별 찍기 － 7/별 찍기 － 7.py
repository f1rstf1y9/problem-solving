n = int(input())
for i in range(n*2-1):
  v = i
  if i > n-1:
    v = n*2-i-2
  print(" "*(n-v-1), "*"*(2*v+1), sep="")