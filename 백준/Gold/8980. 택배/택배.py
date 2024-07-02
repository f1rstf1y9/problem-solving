from collections import deque

N, C = map(int, input().split())
M = int(input())

town_boxes = {x: [] for x in range(1, N+1)}

for _ in range(M):
  from_town, to_town, count = map(int, input().split())
  town_boxes[to_town].append((from_town, count))

for i in range(1, N+1):
  town_boxes[i].sort(key=lambda x: (-x[0], x[1]))

cur_count = 0
cur_boxes = deque()
answer = 0

for i in range(N, 0,-1):
  
  cur_idx = 0
  next_boxes = deque()

  while cur_boxes:
    from_town, count = cur_boxes.popleft()
    if from_town == i:
      cur_count -= count
      continue
    next_boxes.append((from_town, count))
  cur_boxes = next_boxes

  while cur_count < C and cur_idx < len(town_boxes[i]):
    from_town, count = town_boxes[i][cur_idx]
    if cur_count + count <= C:
      cur_count += count
      cur_boxes.append((from_town, count))
      answer += count
    elif cur_count != C:
      cur_boxes.append((from_town, C - cur_count))
      answer += (C-cur_count)
      cur_count = C
    cur_idx += 1
    
print(answer)