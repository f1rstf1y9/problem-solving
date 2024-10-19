import math

N = int(input())
M = int(input())
positions = list(map(int, input().split()))

distances = [positions[0]]
for i in range(M-1):
  distances.append(math.ceil((positions[i+1]-positions[i])/2))
distances.append(N-positions[M-1])

low = 1
high = N

def can_iluminate(H):
  for distance in distances:
    if distance > H:
      return False
  return True

while low <= high:
  mid = (low+high)//2  
  if can_iluminate(mid):
    high = mid - 1
  else:
    low = mid + 1
print(low)