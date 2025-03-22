import sys
input = sys.stdin.readline

max_value = max_count = 0

def backtracking(current_value, current_idx, current_count):
    global max_value, max_count
    
    if current_value == max_value:
        max_count = min(max_count, current_count)
    if current_value > max_value:
        max_value, max_count = current_value, current_count
        
    if current_idx == N:
        return
        
    backtracking(current_value | guitars[current_idx], current_idx+1, current_count+1)
    backtracking(current_value, current_idx+1, current_count)
    

N, M = map(int, input().split())

guitars = [int(input().split()[1].replace('Y', '1').replace('N', '0'), 2) for _ in range(N)]

backtracking(0, -1, 0)

if max_value == 0:
    print(-1)
else:
    print(max_count)
