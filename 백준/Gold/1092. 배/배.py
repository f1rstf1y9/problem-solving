import sys
input = sys.stdin.readline

N = int(input())
weight_limits = list(sorted(map(int, input().split()), reverse=True))
M = int(input())
weights = list(sorted(map(int, input().split()), reverse=True))

if weight_limits[0] < weights[0]:
    print(-1)
    exit()

working_time = [0]*N
for weight in weights:
    best_crane_idx = 0
    for crane_idx, weight_limit in enumerate(weight_limits):
        if weight_limit < weight:
            break
        if working_time[crane_idx] < working_time[best_crane_idx]:
            best_crane_idx = crane_idx
    working_time[best_crane_idx] += 1
print(max(working_time))