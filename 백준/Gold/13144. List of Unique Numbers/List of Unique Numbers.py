from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

left = right = counts = 0
cur_count = 1
count_dict = defaultdict(int)
count_dict[numbers[right]] = 1

while left < N:
    if right+1 >= N or count_dict[numbers[right+1]]:
        counts += cur_count
        cur_count -= 1
        count_dict[numbers[left]] -= 1
        left += 1
    else:
        right += 1
        count_dict[numbers[right]] += 1
        cur_count += 1
    
print(counts)