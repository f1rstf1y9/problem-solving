N, C = map(int, input().split())
width = height = N
for _ in range(C):
    x, y = map(int, input().split())
    if x < width and y < height:
        if x * height > width * y:
            width = x
        else:
            height = y
    elif x < width:
        width = x
    elif y < height:
        height = y
print(width*height)