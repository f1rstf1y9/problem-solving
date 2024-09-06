import sys

input = sys.stdin.readline

N = int(input())

lines = sorted([tuple(map(int, input().split())) for _ in range(N)])

connected_lines = [list(lines[0])]

for start, end in lines[1:]:
    if connected_lines[-1][1] >= start:
        connected_lines[-1][1] = max(end, connected_lines[-1][1])
    else:
        connected_lines.append([start, end])

length = 0
for start, end in connected_lines:
    length += (end-start)

print(length)