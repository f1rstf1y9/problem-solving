from math import gcd
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())

    max_count = M * N // gcd(M, N)
    count = x
    a = x

    while count <= max_count:
        if (count - y) % N == 0:
            print(count)
            break
        count += M
    else:
        print(-1)
