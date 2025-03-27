import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    
    count = 1
    a = x

    while count <= N:
        if a > N:
            a = a%N if a%N else N
            
        if a == y:
            print(M*(count-1)+x)
            break
            
        a += M
        count += 1
    else:
        print(-1)
        
