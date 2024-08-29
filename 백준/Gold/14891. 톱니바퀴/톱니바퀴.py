gears = [list(input()) for _ in range(4)]

def rotate(num, direction):
    if direction == 1:
        return [gears[num][-1]] + gears[num][:-1]
    if direction == -1:
        return gears[num][1:] + [gears[num][0]]


for _ in range(int(input())):
    num, direction = map(int, input().split())

    new_gears = [gears[i][:] for i in range(4)]

    if num == 1:
        new_gears[0] = rotate(0, direction)
        if gears[0][2] != gears[1][6]:
            new_gears[1] = rotate(1, -direction)
            if gears[1][2] != gears[2][6]:
                new_gears[2] = rotate(2, direction)
                if gears[2][2] != gears[3][6]:
                    new_gears[3] = rotate(3, -direction)

    if num == 2:
        if gears[0][2] != gears[1][6]:
            new_gears[0] = rotate(0, -direction)
        new_gears[1] = rotate(1, direction)
        if gears[1][2] != gears[2][6]:
            new_gears[2] = rotate(2, -direction)
            if gears[2][2] != gears[3][6]:
                new_gears[3] = rotate(3, direction)

    if num == 3:
        if gears[1][2] != gears[2][6]:
            new_gears[1] = rotate(1, -direction)
            if gears[0][2] != gears[1][6]:
                new_gears[0] = rotate(0, direction)
        new_gears[2] = rotate(2, direction)
        if gears[2][2] != gears[3][6]:
            new_gears[3] = rotate(3, -direction)

    if num == 4:
        new_gears[3] = rotate(3, direction)
        if gears[2][2] != gears[3][6]:
            new_gears[2] = rotate(2, -direction)
            if gears[1][2] != gears[2][6]:
                new_gears[1] = rotate(1, direction)
                if gears[0][2] != gears[1][6]:
                    new_gears[0] = rotate(0, -direction)

    gears = new_gears

score = 0
if gears[0][0] == '1':
    score += 1
if gears[1][0] == '1':
    score += 2
if gears[2][0] == '1':
    score += 4
if gears[3][0] == '1':
    score += 8

print(score)