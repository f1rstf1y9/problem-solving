import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = sorted(list(map(int, input().split())))

def lower_bound(target):
  left, right = 0, N
  while left < right:
    mid = (left + right) // 2
    if points[mid] < target:
      left = mid + 1
    else:
      right = mid
  return left

def upper_bound(target):
  left, right = 0, N
  while left < right:
      mid = (left + right) // 2
      if points[mid] <= target:
          left = mid + 1
      else:
          right = mid
  return left

for _ in range(M):
  start, end = map(int, input().split())
  left = lower_bound(start)
  right = upper_bound(end)
  print(right - left)