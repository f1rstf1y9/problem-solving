N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

last_lamp = lamps[0]
height = lamps[0]

for i in range(1, M):
  gap = lamps[i] - last_lamp
  cur_height = gap//2 + gap%2
  height = max(height, cur_height)
  last_lamp = lamps[i]

height = max(height, N-last_lamp)

print(height)