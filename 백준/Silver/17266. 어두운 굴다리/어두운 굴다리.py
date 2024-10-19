import math

N = int(input())
M = int(input())
positions = list(map(int, input().split()))

distances = [positions[0]]
for i in range(M-1):
  distances.append(math.ceil((positions[i+1] - positions[i])/2))
distances.append(N-positions[M-1])

print(max(distances))