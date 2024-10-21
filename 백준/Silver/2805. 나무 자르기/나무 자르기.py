N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
result = 0

while low <= high:
  mid = (low + high) // 2

  tree_length = 0
  for tree in trees:
    if tree > mid:
      tree_length += tree - mid
  
  if tree_length >= M:
    result = mid
    low = mid+1
  else:
    high = mid-1
  
print(result)