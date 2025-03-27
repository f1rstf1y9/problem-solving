from math import gcd
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    
    max_count = M*N//gcd(M,N)
    
    count = x
    a = x

    while count <= max_count:
        if a > N:
            a = a%N if a%N else N
            
        if a == y:
            print(count)
            break
            
        a += M
        count += M
    else:
        print(-1)