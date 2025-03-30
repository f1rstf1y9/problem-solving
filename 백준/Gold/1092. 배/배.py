import sys
from bisect import bisect_right

input = sys.stdin.readline

N = int(input())
weight_limits = list(sorted(map(int, input().split()), reverse=True))
M = int(input())
weights = list(sorted(map(int, input().split())))

prev_count = count = 0
time = 1

while count < M:
    for weight_limit in weight_limits:
        idx = bisect_right(weights,weight_limit)-1
        if 0 > idx: continue
        
        del weights[idx]
        count += 1
        
    if prev_count == count:
        print(-1)
        break
    prev_count = count
    time += 1
else:
    print(time-1)
        