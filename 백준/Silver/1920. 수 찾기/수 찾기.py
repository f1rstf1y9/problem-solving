N = int(input())
A = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

A.sort()

for number in numbers:
  l, r = 0, N-1
  mid = (l+r)//2
  while l <= r:
    if A[mid] < number:
      l = mid + 1
    elif A[mid] > number:
      r = mid - 1
    else:
      print(1)
      break
    mid = (l+r)//2
  else:
    print(0)