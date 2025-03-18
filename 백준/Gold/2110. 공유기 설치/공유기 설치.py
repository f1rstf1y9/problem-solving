import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

answer = 0

def is_valiable(distance):
    count = 1
    prev_idx = cur_idx = 0
    while count < C:
        cur_idx += 1
        if cur_idx >= len(house): return False
        if house[cur_idx] - house[prev_idx] >= distance:
            prev_idx = cur_idx
            count += 1
    return True

low, high = 0, house[-1] - house[0]
while low <= high:
    mid = (low+high) // 2
    if is_valiable(mid):
        answer = mid
        low = mid+1
    else:
        high = mid-1

print(answer)
        