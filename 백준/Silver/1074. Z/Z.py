N, r, c = map(int, input().split())
n = 2 ** N
answer = -1
count = 0
def fill_grid(n, x, y):
  global count, answer

  if answer != -1:
    return

  if n == 2:
    if x == r and y == c:
      answer = count
    count += 1
    if x == r and y+1 == c:
      answer = count
    count += 1
    if x+1 == r and y == c:
      answer = count
    count += 1
    if x+1 == r and y+1 == c:
      answer = count
    return
  
  next_n = n//2
  if x <= r < x+next_n and y <= c < y+next_n:
    fill_grid(next_n, x, y)
    count += 1
  else:
    count += next_n ** 2
  
  if x <= r < x+next_n and y+next_n <= c < y+next_n*2:
    fill_grid(next_n, x, y+next_n)
    count += 1
  else:
    count += next_n ** 2
  
  if x+next_n <= r < x+next_n*2 and y <= c < y+next_n:
    fill_grid(next_n, x+next_n, y)
    count += 1
  else:
    count += next_n ** 2
  
  if x+next_n <= r < x+next_n*2 and y+next_n <= c < y+next_n*2:
    fill_grid(next_n, x+next_n, y+next_n)
    count += 1
  else:
    count += next_n ** 2

fill_grid(n, 0, 0)
print(answer)