N = int(input())
liquids = list(map(int, input().split()))

best_value = 1e10
best_value_left = best_value_right = 0

left, right = 0, N-1

while left < right:
  current_value = liquids[left] + liquids[right]
  if abs(current_value) < abs(best_value):
    best_value = current_value
    best_value_left, best_value_right = liquids[left], liquids[right]

    if best_value == 0:
      break
  
  if current_value < 0:
    left += 1
  else:
    right -= 1

print(best_value_left, best_value_right)