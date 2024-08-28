import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

d = [list(map(int, input().split())) for _ in range(N)]

row_sum = [sum(line) for line in d]
col_sum = [sum(line) for line in zip(*d)]

row_comb = list(combinations(range(N), 2))
col_comb = list(combinations(range(M), 2))

max_beauty = -1e6

for i1, i2 in row_comb:
    for j1, j2 in col_comb:
        duplicate = d[i1][j1] + d[i1][j2] + d[i2][j1] + d[i2][j2]
        surround = (i2-i1-1) * (j2-j1-1)
        max_beauty = max(max_beauty, row_sum[i1] + row_sum[i2] + col_sum[j1] + col_sum[j2] - duplicate + surround)

print(max_beauty)