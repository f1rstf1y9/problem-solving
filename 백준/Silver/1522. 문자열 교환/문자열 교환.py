import sys
ab_str = list(sys.stdin.readline().rstrip())

a_cnt = ab_str.count('a')
min_cnt = len(ab_str)
for i in range(-a_cnt, len(ab_str)-a_cnt):
  cnt = 0
  for j in range(a_cnt):
    if ab_str[i+j] == 'b':
      cnt += 1
  min_cnt = min(cnt, min_cnt)
print(min_cnt)