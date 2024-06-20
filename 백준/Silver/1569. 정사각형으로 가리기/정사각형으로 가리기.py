N = int(input())

coords = [list(map(int, input().split())) for _ in range(N)]

x_side_length = max(coords, key=lambda x:x[0])[0] - min(coords, key=lambda x:x[0])[0]
y_side_length = max(coords, key=lambda x:x[1])[1] - min(coords, key=lambda x:x[1])[1]

side_length = max(x_side_length, y_side_length)
vertex_x, vertex_y = max(coords, key=lambda x:x[0])[0] - side_length, max(coords, key=lambda x:x[1])[1] - side_length

def check_valid(vertex_x, vertex_y):
  for x, y in coords:
    if x == vertex_x and vertex_y <= y <= vertex_y + side_length:
      continue
    elif y == vertex_y and vertex_x <= x <= vertex_x + side_length:
      continue
    elif x == vertex_x + side_length and vertex_y <= y <= vertex_y + side_length:
      continue
    elif y == vertex_y + side_length and vertex_x <= x <= vertex_x + side_length:
      continue
    else:
      return False
  return True

max_x = max(coords, key=lambda x:x[0])[0]
max_y = max(coords, key=lambda x:x[1])[1]
min_x = min(coords, key=lambda x:x[0])[0]
min_y = min(coords, key=lambda x:x[1])[1]

vertices = [(max_x-side_length, max_y-side_length), (max_x-side_length, min_y), (min_x, max_y-side_length), (min_x, min_y) ]

for vertex in vertices:
  if check_valid(vertex[0], vertex[1]):
    break
else:
  side_length = -1
  
print(side_length)