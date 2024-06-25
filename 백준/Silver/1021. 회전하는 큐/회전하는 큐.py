from collections import deque
N, M = map(int, input().split())
positions = list(map(int, input().split()))

queue = deque([i for i in range(1, N+1)])
cur = 0
count = 0

while cur < M:
  if queue[0] != positions[cur]:
    left_queue = deque(queue)
    left_count = 0
    while left_queue[0] != positions[cur]:
      left_queue.append(left_queue.popleft())
      left_count += 1
    right_queue = deque(queue)
    right_count = 0
    while right_queue[0] != positions[cur]:
      right_queue.appendleft(right_queue.pop())
      right_count += 1
    if left_count < right_count:
      queue = left_queue
      count += left_count
    else:
      queue = right_queue
      count += right_count
  queue.popleft()
  cur += 1

print(count)