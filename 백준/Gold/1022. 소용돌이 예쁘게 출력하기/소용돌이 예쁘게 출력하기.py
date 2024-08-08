r1, c1, r2, c2 = map(int, input().split())

length = max([abs(r1), abs(r2), abs(c1), abs(c2)]) * 2 + 1
bias = length // 2
height = r2-r1+1
width = c2-c1+1

matrix = [[0] * width for _ in range(height)]
cur_num = 1
max_num = 1

delta = [(0,1), (-1,0),(0,-1),(1,0)]

r, c = 0, 0
depth = 1
delta_idx = 0

pos_list = []

while r != bias+1 and c != bias+1 and len(pos_list) < height*width:
  if r1 <= r <= r2 and c1 <= c <= c2:
    pos_list.append((r, c, cur_num))
    max_num = cur_num
  cur_num += 1

  if (r == depth-1 and c == depth) or (r == -depth and c == depth) or (r == -depth and c == -depth):
    delta_idx = (delta_idx+1) % 4
  elif (r == depth and c == -depth):
    delta_idx = (delta_idx+1) % 4
    depth += 1

  dx, dy = delta[delta_idx]
  r += dx
  c += dy

number_length = len(str(max_num))

pos_list.sort()

for i in range(height * width):
  n = pos_list[i][2]
  cur_length = len(str(n))
  print(" "*(number_length - cur_length) + str(n), end=" ")
  if (i % width == width-1):
    print()