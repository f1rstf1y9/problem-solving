N, A, B = map(int, input().split())
pretty_2x1 = list(sorted(map(int, input().split())))
pretty_2x2 = list(sorted(map(int, input().split())))

floor_pretty = 0

if N%2:
    floor_pretty += pretty_2x1.pop()
    N -= 1
    A -= 1

while N:
    if pretty_2x2 and len(pretty_2x1) > 1:
        if pretty_2x2[-1] > pretty_2x1[-1] + pretty_2x1[-2]:
            floor_pretty += pretty_2x2.pop()
        else:
            floor_pretty += (pretty_2x1.pop() + pretty_2x1.pop())
    elif pretty_2x2:
        floor_pretty += pretty_2x2.pop()
    else:
        floor_pretty += (pretty_2x1.pop() + pretty_2x1.pop())
    N -= 2

print(floor_pretty)