import sys
input = sys.stdin.readline
n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]
max_x = max(coords, key=lambda x: x[0])[0]
min_x = min(coords, key=lambda x: x[0])[0]
max_y = max(coords, key=lambda x: x[1])[1]
min_y = min(coords, key=lambda x: x[1])[1]
print((max_x - min_x) * (max_y - min_y))