from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ways = [0]*101
for _ in range(N+M):
    start, end = map(int, input().split())
    ways[start] = end

dice_cnts = [100]*101

q = deque([1])
dice_cnts[1] = 0

while q:
    num = q.popleft()
    if ways[num]:
        next_num = ways[num]
        if dice_cnts[next_num] > dice_cnts[num]:
            dice_cnts[next_num] = dice_cnts[num]
            q.append(next_num)
    else:
        for i in range(1,7):
            next_num = num + i
            if next_num <= 100 and dice_cnts[next_num] > dice_cnts[num]+1:
                dice_cnts[next_num] = dice_cnts[num]+1
                q.append(next_num)

print(dice_cnts[100])              