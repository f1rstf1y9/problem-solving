import sys
input = sys.stdin.readline
N = int(input())

requests = list(map(int, input().split()))
requests.sort()
budget_total = int(input())
requests_total = sum(requests)

ans = 0
remain = budget_total
max_total = 0
if requests_total <= budget_total:
  print(requests[-1])
else:
  i = -1
  while (i < N-1):
    if i != -1:
      remain -= requests[i]
    max_money = remain // (N-i-1)
    if max_money <= requests[i+1]:
      if max_total <= remain + max_money*(N-i-1):
        max_total, ans = remain + max_money*(N-i-1), max_money
    i += 1
  print(ans)