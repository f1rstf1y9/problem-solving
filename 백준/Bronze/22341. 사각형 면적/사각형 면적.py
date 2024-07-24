N, C = map(int, input().split())
width = height = N
for _ in range(C):
    x, y = map(int, input().split())
    if x >= height or y >= width:
        continue;
    if x * width >= y * height:
        height = x
    else:
        width = y

print(width*height)