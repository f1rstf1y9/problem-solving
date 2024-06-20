x, y = map(int, input().split())
shop_cnt = int(input())

shops = [list(map(int, input().split())) for _ in range(shop_cnt)]
d_direction, d_offset = map(int, input().split())

min_distance_total = 0

for shop_direction, shop_offset in shops:
  directions = [d_direction, shop_direction]
  if directions in [[1,1], [2,2], [3,3], [4,4]]:
    min_distance_total += abs(d_offset - shop_offset)
  elif directions in [[1,3], [3,1]]:
    min_distance_total += d_offset + shop_offset
  elif directions in [[1,4]]:
    min_distance_total += x - d_offset + shop_offset
  elif directions in [[4,1]]:
    min_distance_total += d_offset + x - shop_offset
  elif directions in [[2,3]]:
    min_distance_total += d_offset + y - shop_offset
  elif directions in [[3,2]]:
    min_distance_total += y - d_offset + shop_offset
  elif directions in [[2,4]]:
    min_distance_total += x - d_offset + y - shop_offset
  elif directions in [[4,2]]:
    min_distance_total += y - d_offset + x - shop_offset
  elif directions in [[1,2], [2,1]]:
    min_distance_total += min(d_offset + shop_offset, x*2 - d_offset - shop_offset) + y
  elif directions in [[3,4], [4,3]]:
    min_distance_total += min(d_offset + shop_offset, y*2 - d_offset - shop_offset) + x

print(min_distance_total)