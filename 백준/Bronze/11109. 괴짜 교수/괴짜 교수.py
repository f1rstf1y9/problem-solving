T = int(input())

for _ in range(T):
  d, n, s, p = map(int, input().split())
  s_total_time = n*s
  p_total_time = d + n*p

  if s_total_time > p_total_time:
    print("parallelize")
  elif s_total_time < p_total_time:
    print("do not parallelize")
  else:
    print("does not matter")