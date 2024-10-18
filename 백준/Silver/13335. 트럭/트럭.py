from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

time = 0
bridge = deque([0]*w)
bridge_weight = 0

while trucks or bridge_weight:
  bridge_weight -= bridge.popleft()
  if trucks:
    if trucks[0] + bridge_weight > L:
      bridge.append(0)
    else:
      truck = trucks.popleft()
      bridge.append(truck)
      bridge_weight += truck
  time += 1

print(time)