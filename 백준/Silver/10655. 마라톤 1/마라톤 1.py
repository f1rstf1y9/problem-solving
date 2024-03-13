import sys
N = int(sys.stdin.readline())
checkpoints = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

distances = [abs(checkpoints[i][0]-checkpoints[i+1][0]) + abs(checkpoints[i][1]-checkpoints[i+1][1]) for i in range(N-1)]

sum_d = sum(distances)
min_d = 1e9

for i in range(N-2):
  cur_d = sum_d - distances[i] - distances[i+1] + abs(checkpoints[i][0]-checkpoints[i+2][0]) + abs(checkpoints[i][1]-checkpoints[i+2][1])
  if cur_d < min_d:
    min_d = cur_d

print(min_d)