T, X = map(int, input().split())
N = int(input())
classes = [0]*T
for _ in range(N):
    _ = int(input())
    for i in map(int, input().split()):
        classes[i-1] += 1

if classes[X-1] == N:
    print("YES")
else:
    print("NO") 
    