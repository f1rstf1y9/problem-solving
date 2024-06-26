import sys
import bisect

input = sys.stdin.readline
N, Q = map(int, input().split())
S = input()

Ridx = []
Bidx = []

for i, char in enumerate(S):
  if char == 'R':
    Ridx.append(i)
  elif char == 'B':
    Bidx.append(i)

for _ in range(Q):
  a, b = map(int, input().split())
  
  r1 = bisect.bisect_left(Ridx, a)
  r2 = bisect.bisect_right(Ridx, b) - 1
  b1 = bisect.bisect_left(Bidx, a)
  b2 = bisect.bisect_right(Bidx, b) - 1

  if r2 - r1 + 1 < 2 or b2 - b1 + 1 < 2:
    print('-1')
    continue
  
  if Ridx[r1 + 1] >= Bidx[b2 - 1]:
    print('-1')
    continue
  
  print(f"{Ridx[r1]} {Ridx[r1 + 1]} {Bidx[b2 - 1]} {Bidx[b2]}")