import sys
input = sys.stdin.readline

N, K = map(int, input().split())
makgeolli = [int(input()) for _ in range(N)]

low, high = 1, max(makgeolli)
answer = 0

while low <= high:
  mid = (low + high) // 2
  
  # 모두에게 mid만큼 나눠줄 수 있는지 확인
  total = 0
  for m in makgeolli:
    total += m // mid
  
  if total >= K:
    answer = mid
    low = mid + 1
  else:
    high = mid - 1

print(answer)